;-------------------------------------------------------------------------------------;
;       Trajectory Plot
; AUTHOR: CHONG LIU, NANJING UNIVERSITY, 04/01/2018
; Assumes Lagranto lsl-file style output with five
; header lines
;http://www.ncl.ucar.edu/Applications/Scripts/gsn_xy_4.ncl
;-------------------------------------------------------------------------------------;

;-------------------------------------------------------------------------------------;
; Loading Libraries
;-------------------------------------------------------------------------------------;

load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"   
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl" 
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
load "gsn_func.ncl"
;-------------------------------------------------------------------------------------;
; Read trajectory file 
;-------------------------------------------------------------------------------------;
; --------- Name of trajectory file --------------------------------------------------;
filename="trajectories.txt"

;---------- Read file ----------------------------------------------------------------;
delim   = " "                                              ; Delimiting character

flds  = asciiread(filename,-1,"string")
slon  = tofloat(str_get_field(flds(12:),3,delim))
slat  = tofloat(str_get_field(flds(12:),4,delim))
height = tofloat(str_get_field(flds(12:),5,delim))
ntra   = tointeger(str_get_field(flds(2),1,delim))
date   = tointeger(str_get_field(flds(0),1,delim))
print(ntra)
print(date)
;period  = -126000                                         ; -is back  
;timestp = -3600
ntim    = dimsizes(slon)/ntra                 ; # times
print(ntim)

;;caculate for plot;;
latmin=min(slon)
latmax=max(slon)
lonmin=min(slat)
lonmax=max(slat)
zmin=min(height)
zmax=max(height)
slont    = onedtond(slon,(/ntim,ntra/)) ; 3d trajectory array
slatt    = onedtond(slat,(/ntim,ntra/)) ; 3d trajectory array
zt    = onedtond(height,(/ntim,ntra/)) ; 3d trajectory array
;-------------------------------------------------------------------------------------;
; Plot trajectories
;-------------------------------------------------------------------------------------;

; --------------- Open Workstation and Colormap --------------------------------------
;wks_type = "ps"
;wks_type@wkPaperWidthF  = 14.5  ; in inches
;wks_type@wkPaperHeightF = 10.0  ; in inches
wks_type = "png"
wks_type@wkWidth = 2500
wks_type@wkHeight = 2500
wks  = gsn_open_wks(wks_type,"Forward_trajecory")           ; open workstation
;gsn_define_colormap(wks,"CBR_coldhot")          ; use the BlueDarkRed18 colormap
;gsn_define_colormap(wks,"GMT_haxby")          ; use the BlueDarkRed18 colormap
;cmap = gsn_retrieve_colormap(wks)              ; colormap

; --------------- General resources for plot -----------------------------------------

mres                  = True               ; map resource
mres@gsnDraw          = False                  ; don't draw
mres@gsnFrame         = False                  ; don't advance frame
;mres@tiMainString         = "Trajectories"     ; set the main title
;mres@tiMainFont           = "0_times_roman"        ; font of main title
;mres@gsnMaximize      = True           ; Maximize plot
mres@gsnCenterString            = "      AERC of Nanjing University - FLEXPART"+"~C~Forward trajectories ending at UTC "+tostring(date)+" 08"
mres@gsnLeftString            = " "
mres@gsnCenterStringFontHeightF =14.0 
mres@gsnRightString = " "
mres@gsnRightStringFontHeightF =14.0 
mres@vpWidthF              = 0.8                ; change aspect ratio of plot
mres@vpHeightF             = 0.58
mres@vpXF                  = 0.15
mres@vpYF                  = 0.905
;mres@tmXTOn              = True
;mres@tmXTLabelsOn         = True
;mres@tmXBOn              = False

; ----------------- World map --------------------------------------------------------
;mres@mpShapeMode = "FreeAspect" ;;;;;; fixed aspect ratio; skewing map;;;;;;;;;;;
mres@mpMaxLatF            =45 ;50;latmax+0.5             ; choose subregion  0.1 just for fine for colorbar         
mres@mpMinLatF            =25 ;20;latmin-0.5                      ; of world map
mres@mpMaxLonF            =130 ;140;lonmax+0.5
mres@mpMinLonF            =110 ;100;lonmin-0.5
mres@mpFillOn             = False                  ; color land
mres@mpOutlineOn      = False                   ; outline land/sea boarders
mres@pmTickMarkDisplayMode = "Always"          ;turn on tm      
;mres@mpDataSetName               = "Earth..4"
;mres@mpDataBaseVersion           = "MediumRes"
;mres@mpOutlineSpecifiers         = (/"China:states"/)
mres@mpOutlineOn                  =False
map = gsn_csm_map_ce(wks,mres)                     ; Draw world map 
;drawNDCGrid(wks)
;;;;add shapefile;;;
lnres                  = True
lnres@gsLineColor      = "gray50"
lnres@gsLineThicknessF = 4.0
shpid = gsn_add_shapefile_polylines(wks,map,"CHN_adm2.shp",lnres)
draw(map)
; ----------------- Polyline (including coloring of trajectories ) --------------------

; --- Specify the coloring field
cnField                  = "p"                          ; Coloring according to pressure
cnIndex                  = 4                            ; Column index for coloring field for pressure
cnLevels         = fspan(zmin,zmax,21)       ; Coloring levels
cnLabels                 = flt2string(tointeger(cnLevels))         ; Labels

Markerscolor=(/"red","blue","green"/)
Markersindex= (/4,6,7/);(/1,1,1/) ;(/4,6,7/)
; --- Resources for the polylines (except for color)
pres             = True                         ; polyline resource
pres@tfDoNDCOverlay      = True 
pres@gsLineThicknessF    = 10.0                          ; line thickness    

; --- Draw polylines 
do i = 0,ntra-1                                         ; Loop over all trajecories
  
  pres@gsLineColor   = Markerscolor(i)                         ; line thickness    
  x = slont(:,i)                              ; Longitudes for trajectory i
  y = slatt(:,i)                              ; Latitudes for trajectory i
; this controls the size and location of the first plot
  gsn_polyline(wks,map,x,y,pres)       ; draw polyline
 
end do


; ----------------- Markers ----------------------------------------------------------------

; --- Resources for the markers
kres             = True             ; marker resource
kres@gsMarkerSizeF       = 3.0                  ; marker size


; --- Draw markers
do i = 0,ntra-1                                         ; Loop over all trajecories

  kres@gsMarkerIndex       = Markersindex(i) 
  kres@gsMarkerColor       = Markerscolor(i)          ; marker color
  x = slont(:,i)                              ; Longitudes for trajectory i
  y = slatt(:,i)                              ; Latitudes for trajectory i
  gsn_polymarker(wks,map,x,y,kres)        ; mark position
  mkres=True 
  mkres@gsMarkerIndex = 12 
  mkres@gsMarkerColor ="Red" 
  mkres@gsMarkerSizeF = 20. 
  mkres@gsMarkerThicknessF =18.0
  gsn_polymarker(wks,map,slont(0,0),slatt(0,0),mkres)
end do

;*****************************************
; second plot
;*****************************************
  sres                      = True      ; plot mods desired
  sres@gsnFrame             = False     ; don't advance frame
  ;gsnYRefLineIn NCL 6.4.0
  sres@gsnTickMarksOn       = True        ; turn off tickmarks
  sres@gsnYRefLine          = 0.          ; Y-value for ref. line
  ;sres@gsnAboveYRefLineColor= "Red"   ; Color area above ref. line red
  ;sres@gsnBelowYRefLineColor= "Blue"  ; Color area below ref. line blue
  sres@gsnCenterString      = ""       ; no center string
  sres@tiYAxisString = "Height (m)"           ; y axis title
  sres@tiXAxisString = "Time"                 ; x axis title
  ;sres@tiXAxisOn            = False    ; turn off X-axis title 
  sres@tmXTOn              = False
  sres@tmYROn              = False
  sres@tmYLMinorOn         = False
  sres@tmXBMode        = "Manual"	
  sres@tmXBTickStartF  = 0
  sres@tmXBTickEndF    = 71
  sres@tmXBTickSpacingF= 24
  ;sres@tmXBLabelFont   =6
  sres@tmXBLabelFontHeightF = 0.015
  ;sres@trXMinF              = 1919      ; set X-axis max and mins
  ;sres@trXMaxF              = 2015
  ;sres@trYMinF              = -4.      ; set Y-axis max and mins
  ;sres@trYMaxF              =  3.      
  sres@xyLineThicknesses    = (/5.,5.,5./)      ; Define line thicknesses 
  sres@xyLineColors         = Markerscolor ; Define line color
  sres@xyMonoDashPattern    = True

  sres@tmYLLabelFontHeightF = 0.015  ; font height
  ;sres@tmXBMinLabelSpacingF = 6

  sres@xyMarkLineMode       = "MarkLines"
  sres@xyMarkerColors    = Markerscolor;(/"red",    "black","black"/) 
  ;sres@xyMarkerColors    = "red" 
  sres@xyMarkers         = Markersindex ;(/1,         1,      1/)          ; style 
  ;sres@xyMarker         = 2         ; style
  sres@xyMarkerSizeF    = (/4,4,4/)
  ;sres@gsnYRefLine      = (/10,500,1000/)
; this controls the size and location of the second plot
  sres@vpXF                 = 0.25;0.16   
  sres@vpYF                 = 0.25;0.25     
  sres@vpWidthF             = 0.6;0.78
  sres@vpHeightF            = 0.16;0.16

  time = ispan(0,ntim-1,1)  ; time has units of YYYY
  z = new((/3,ntim/),float)
  z(0,:)= zt(:,0)
  z(1,:)= zt(:,1)
  z(2,:)= zt(:,2) 
  sres@gsnYRefLine      = 500
  sres@gsnYRefLineDashPattern = 2
  tsmap2 = gsn_csm_xy(wks,time,z,sres)
  sres@gsnYRefLine      = 1000
  sres@gsnYRefLineDashPattern = 2
  tsmap3 = gsn_csm_xy(wks,time,z,sres)
  frame(wks)             ; advance frame after extra line drawn
