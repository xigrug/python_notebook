; -----------------------------------------------------
; AUTHOR: CHONG LIU, NANJING UNIVERSITY, 05/12/2015
; ADD 01_PLOT 24_PLOT ALL_PLOT
; OUTPUT FILE REVERSE FOR CONVERT
; INITAIL TIME IS THE LAST TIME
; Overlaying contours on a map without having lat,lon coordinates
; Turning on map tickmark labels with degree symbols
; Zooming in on a particular area on a map
; -----------------------------------------------------

load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/shea_util.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/wrf/WRFUserARW.ncl"
load "gsn_func.ncl"

begin
stime = 0
etime = 71
days  = (etime-stime+1)/24

; *****************************************************
   fname = systemfunc("csh -c 'ls ./flxout_"+"d01_"+"*'")+".nc"
   input = addfiles(fname,"r")
   input_head = addfile("./header_d01.nc","r")
   ;input_wrf = addfile("wrfout_d02_2016-04-19_00_00_00.nc","r")
   ;initial_time="2016-04-19 00:00:00"
   ;times=new(etime+1,string)
   times = str_sub_str(wrf_user_getvar(input,"times",-1),"_"," ")
   do itime = 0, dimsizes(times)-1
      YY=str_get_cols(times(itime), 0, 3)
      MM=str_get_cols(times(itime), 4, 5)
      DD=str_get_cols(times(itime), 6, 7)
      HH=str_get_cols(times(itime), 9, 10)
      times(itime) = systemfunc("date '+%Y-%m-%d_%H_00_00' -d '"+YY+"-"+MM+"-"+DD+" "+HH+":00:00 8 hour'")
   end do
   lat2d   = input_head->XLAT(:,:)
   lon2d   = input_head->XLONG(:,:)
   print(min(lat2d))
   print(min(lon2d))
   print(max(lat2d))
   print(max(lon2d))
; *****************************************************
   ; domain hourly - met
   
   d_01h_conc   = (/wrf_user_getvar(input,"CONC",-1)/)
   conc_temp = d_01h_conc
   do id = 0, days-1
      conc_temp(id,0,:,:,:,:) = dim_avg_n(d_01h_conc(stime+id*24:stime+id*24+23,0,:,:,:,:),0)
   end do
   d_24h_conc   = conc_temp(:days-1,0,:,:,:,:)
   d_all_conc   = dim_avg_n(d_01h_conc(:,0,:,:,:,:),0)*(etime-stime)
   printVarSummary(d_all_conc)
   d_conc   = dim_avg_n(d_all_conc(:,:,:,:),1)*9;levels
   res = True
   res@gsnFrame                        = False
   res@gsnDraw                         = False
   res@vpWidthF                        = 1.
   res@vpHeightF                       = 1.
   res@gsnAddCyclic                    = False                ; regional data
   cnres = res
   cnres@cnFillOn                      = True
   cnres@cnLinesOn                     = False
   cnres@cnConstFEnableFill            = True
   cnres@cnLevelSelectionMode          = "ExplicitLevels"
   cnres@cnLineLabelsOn                = False
   cnres@cnInfoLabelOn                 = False
   cnres@gsnStringFontHeightF          = .02
   cnres@gsnLeftString                 = "FLEXPART_NJU ~C~ Footprint"+"  unit: S~Z40Q~~F34~7~F~~Z100Q~m~S~3~N~~Z40Q~~F34~7~F~~Z100Q~kg~S~-1~N~"
   cnres@lbLabelBarOn                  = True
   cnres@lbOrientation                 = "Vertical"
   cnres@lbLabelStride                 = 1
   cnres@lbLabelFontHeightF            = .03
   cnres@pmLabelBarWidthF              = .1
   cnres@pmLabelBarHeightF             = 1.
   ; !!!!! any plot of data that is on a native grid, must use the "corners"
   ; method of zooming in on map.
   cnres@mpFillOn             = False                  ; color land
   cnres@mpOutlineOn      = False                   ; outline land/sea boarders
   cnres@mpLimitMode       = "Corners"            ; choose range of map
   cnres@mpLeftCornerLatF  = min(lat2d)
   cnres@mpLeftCornerLonF  = min(lon2d)
   cnres@mpRightCornerLatF = max(lat2d)
   cnres@mpRightCornerLonF = max(lon2d)
   ;cnres@mpRelativeCenterLon         = True                 ; set a center lon
   ;cnres@mpCenterLonF                = lon((nlat/2)+1,(nlon/2)+1)  ; center lon
   ;cnres@mpRelativeCenterLat         = True		        ; set a center lat
   ;cnres@mpCenterLatF                = 90.                  ; center lat
   cnres@tfDoNDCOverlay              = True                 ; do not transform data !!!!!!!!!!!
   ;cnres@mpProjection                  = "LambertConformal"
   ;cnres@mpFillOn                      = False
   ;cnres@mpGridAndLimbOn               = False
   ;cnres@mpGridSpacingF                = 20./60
   ;cnres@mpGridLineDashPattern         = 2
   ;cnres@mpGridLineColor               = "black"
   ;cnres@tmXBMajorLengthF              = .0
   ;cnres@tmYRMajorLengthF              = .0
    cnres@pmTickMarkDisplayMode = "Always" ;will turn on these tickmarks
    cnres@gsnMajorLatSpacing = 2.5              ; change maj lat tm spacing
    cnres@gsnMajorLonSpacing = 2.5              ; change maj lon tm spacing
    cnres@tmXBMinorOn        = False           ; no lon minor tickmarks
    cnres@tmYLMinorOn        = False           ; no lon minor tickmarks
   ;cnres@tmXBMode        = "Manual"	
   ;cnres@tmXBTickStartF  = 115
   ;cnres@tmXBTickEndF    = 125
   ;cnres@tmXBTickSpacingF= 2.5 
   pltres = True
   pltres@PanelPlot                    = True
   pltres@FramePlot                    = False
   pltres@NoTitles                     = True
   pltres@gsnMaximize                  = False
   plres = True
   plres@gsnPanelCenter                = False
   plres@gsnPanelBottom                = .05
   plres@gsnPanelTop                   = .95
   plres@gsnPanelLeft                  = .05
   plres@gsnPanelRight                 = .95
 
;;;plot set;;;
;do itraj=0
itraj=0
  do ilevel=0,8 
      sque=etime
      sque_day=days
; *****************************************************
     do id = 0, days-1   ; TIME LOOP
      sque_day= sque_day-1
      tt = str_get_cols(times(stime+id*24),0,9)
      ts = "Valid: Mean of "+tt
      ; plotting options for relative humidity
      opts = cnres
      opts@cnLevelSelectionMode          = "AutomaticLevels"
      vmin = round(floor(min(d_24h_conc)),1)
      vmax = round(ceil(max(d_24h_conc)),1)
      vinc = round(ceil((vmax-vmin)/200.),1)
      ;opts@cnLevels       = fspan(0,4,17)
      opts@cnLevels       = fspan(vmin+vinc,vmax-vinc,251)
      opts@gsnRightString = "Initialized at "+times(etime)+"~C~"+ts
      wks = gsn_open_wks("png","d02_"+tostring(sque_day)+"daycn_"+"conc_"+tt+"_"+tostring(itraj)+"tra_"+tostring(ilevel)+"level")
      gsn_define_colormap(wks,"WhiteBlueGreenYellowRed")
      ;opts@gsnSpreadColors     = True
      ;opts@gsnSpreadColorStart = 30
      ;opts@gsnSpreadColorEnd   = 175
      base_var = gsn_csm_contour_map(wks,d_24h_conc(id,itraj,ilevel,:,:),opts)
      boundstr = gsn_add_bou(wks,base_var,"CHN_adm2")
      ;placestr = gsn_add_polymarker(wks,plot_var,slon,slat,mkres)
      ;gres                 = True
      ;gres@gsFillColor     = "yellow"
      pres                  = True
      pres@gsLineColor      = "orange"
      pres@gsLineThicknessF = 2.0
      lat = (/36.05,  36.05, 36.15, 36.15, 36.05/)
      lon = (/120.29,  120.45, 120.45, 120.29, 120.29/)
      ;dum = gsn_add_polygon(wks,base_var,lon,lat,gres)
      dum = gsn_add_polyline(wks,base_var,lon,lat,pres)
      gsn_panel(wks,(/base_var/),(/1,1/),plres)
      delete(opts)
    end do
      
;***************************************************************************
      opts = cnres
      opts@cnLevelSelectionMode          = "AutomaticLevels"
      vmin = round(floor(min(d_all_conc(itraj,ilevel,:,:))),3)
      vmax = round(ceil(max(d_all_conc(itraj,ilevel,:,:))),3)
      vinc = round(ceil((vmax-vmin)/200.),3)
      ;opts@cnLevels       = fspan(0,4,17)
      opts@cnLevels       = fspan(vmin+vinc,vmax-vinc,251)
      opts@gsnRightString = "Initialized at "+times(etime)+"~C~"+"Valid: Mean of "+times(stime)+"~C~                         -"+times(etime)
      wks = gsn_open_wks("png","d02_allverage"+"cn_"+"conc_"+tostring(itraj)+"tra_"+tostring(ilevel)+"level")
      gsn_define_colormap(wks,"WhiteBlueGreenYellowRed")
      ;opts@gsnSpreadColors     = True
      ;opts@gsnSpreadColorStart = 30
      ;opts@gsnSpreadColorEnd   = 175
      base_var = gsn_csm_contour_map(wks,d_all_conc(itraj,ilevel,:,:),opts)
      boundstr = gsn_add_bou(wks,base_var,"CHN_adm2")
      ;placestr = gsn_add_polymarker(wks,plot_var,slon,slat,mkres)
      ;gres                 = True
      ;gres@gsFillColor     = "yellow"
      pres                  = True
      pres@gsLineColor      = "orange"
      pres@gsLineThicknessF = 2.0
      lat = (/36.05,  36.05, 36.15, 36.15, 36.05/)
      lon = (/120.29,  120.45, 120.45, 120.29, 120.29/)
      ;dum = gsn_add_polygon(wks,base_var,lon,lat,gres)
      dum = gsn_add_polyline(wks,base_var,lon,lat,pres)
      gsn_panel(wks,(/base_var/),(/1,1/),plres)
      delete(opts)
  end do
      opts = cnres
      opts@cnLevelSelectionMode          = "AutomaticLevels"
      vmin = round(floor(min(d_all_conc(itraj,:,:,:))),3)
      vmax = round(ceil(max(d_all_conc(itraj,:,:,:))),3)
      vinc = round(ceil((vmax-vmin)/200.),3)
      ;opts@cnLevels       = fspan(0,4,17)
      opts@cnLevels       = fspan(vmin+vinc,vmax-vinc,251)
      opts@gsnRightString = "Initialized at "+times(etime)+"~C~"+"Valid: Mean of "+times(stime)+"~C~                         -"+times(etime)
      wks = gsn_open_wks("png","d02_allverage"+"cn_"+"conc_"+tostring(itraj)+"tra")
      gsn_define_colormap(wks,"WhiteBlueGreenYellowRed")
      ;opts@gsnSpreadColors     = True
      ;opts@gsnSpreadColorStart = 30
      ;opts@gsnSpreadColorEnd   = 175
      base_var = gsn_csm_contour_map(wks,d_conc(itraj,:,:),opts)
      boundstr = gsn_add_bou(wks,base_var,"CHN_adm2")
      ;placestr = gsn_add_polymarker(wks,plot_var,slon,slat,mkres)
      ;gres                 = True
      ;gres@gsFillColor     = "yellow"
      pres                  = True
      pres@gsLineColor      = "orange"
      pres@gsLineThicknessF = 2.0
      lat = (/36.05,  36.05, 36.15, 36.15, 36.05/)
      lon = (/120.29,  120.45, 120.45, 120.29, 120.29/)
      ;dum = gsn_add_polygon(wks,base_var,lon,lat,gres)
      dum = gsn_add_polyline(wks,base_var,lon,lat,pres)
      gsn_panel(wks,(/base_var/),(/1,1/),plres)
      delete(opts)

;end do

   ;---Convert PNG images to animated GIF
    ;cmd ="bash aa.sh”
    ;cmd = "convert -delay 25 *.png animate_2.gif"
end
