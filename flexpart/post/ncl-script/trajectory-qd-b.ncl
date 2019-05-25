;-------------------------------------------------------------------------------------;
;       Trajectory Plot
; AUTHOR: CHONG LIU, NANJING UNIVERSITY, 04/01/2018
; Assumes Lagranto lsl-file style output with five
; header lines
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

nhead   = 6                                                ; # header lines
ntra   = 1
head    = readAsciiHead(filename,nhead-1)          ; Read header lines
ncol    = 41                 ; # columns
data    = asciiread(filename,-1,"float")           ; Read data in as float
n       = dimsizes(data);                                  ; Number of entries in data
ifirst  = 18                                                ; First data element !!the first float 第几个数字开始
ifinal  = n-1                                              ; Last data element
period  = -126000                                         ; -is back  
timestp = -3600
ntim    = floattoint( period/timestp)*2+1                 ; # times
print(ntim)
;traj    = onedtond(data(ifirst:ifinal),(/ntim,ntra,ncol/)) ; 3d trajectory array
traj    = onedtond(data(ifirst:ifinal),(/ntim,ncol/)) ; 2d trajectory array

traj@MODEL       = "FLEXPART"

; Set names of dimensions and assign values
traj!0    = "TIME"
;traj!1    = "TRA"
traj!1    = "FIELD"
traj&TIME = fspan(0,period,ntim)
print(traj)
;;caculate for plot;;
latmin=min(traj(:,3))
print(latmin)
latmax=max(traj(:,3))
print(latmax)
lonmin=min(traj(:,2))
print(lonmin)
lonmax=max(traj(:,2))
print(lonmax)
zmin=min(traj(:,4))
print(zmin)
zmax=max(traj(:,4))
print(zmax)
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
wks  = gsn_open_wks(wks_type,"Backward_trajecory")           ; open workstation
;gsn_define_colormap(wks,"CBR_coldhot")          ; use the BlueDarkRed18 colormap
gsn_define_colormap(wks,"GMT_haxby")          ; use the BlueDarkRed18 colormap
cmap = gsn_retrieve_colormap(wks)              ; colormap

; --------------- General resources for plot -----------------------------------------

mres                  = True               ; map resource
mres@gsnDraw          = False                  ; don't draw
mres@gsnFrame         = False                  ; don't advance frame
;mres@tiMainString         = "Trajectories"     ; set the main title
;mres@tiMainFont           = "0_times_roman"        ; font of main title
;mres@gsnMaximize      = True           ; Maximize plot
mres@gsnLeftString            = "WRF/FLEXPART Backward"+\
        "~C~Nanjing University AERC"
mres@gsnLeftStringFontHeightF =14.0 
mres@gsnRightString = "Trajectories~C~ Height(m)"
mres@gsnRightStringFontHeightF =14.0 
mres@vpWidthF              = 0.70                ; change aspect ratio of plot
mres@vpHeightF             = 0.70
mres@vpXF                  = 0.15
mres@vpYF                  = 0.88

; ----------------- World map --------------------------------------------------------
;mres@mpShapeMode = "FreeAspect" ;;;;;; fixed aspect ratio; skewing map;;;;;;;;;;;
mres@mpMaxLatF            =45 ;latmax+0.5             ; choose subregion  0.1 just for fine for colorbar         
mres@mpMinLatF            =25 ;latmin-0.5                      ; of world map
mres@mpMaxLonF            =130 ;lonmax+0.5
mres@mpMinLonF            =110 ;lonmin-0.5
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
lnres@gsLineColor      = "grey1"
lnres@gsLineThicknessF = 8.0
shpid = gsn_add_shapefile_polylines(wks,map,"CHN_adm2.shp",lnres)
draw(map)
; ----------------- Polyline (including coloring of trajectories ) --------------------

; --- Specify the coloring field
cnField                  = "p"                          ; Coloring according to pressure
cnIndex                  = 4                            ; Column index for coloring field for pressure
cnLevels         = fspan(zmin,zmax,21)       ; Coloring levels
cnLabels                 = flt2string(tointeger(cnLevels))         ; Labels
print(cnLabels)

; --- Resources for the polylines (except for color)
pres             = True                         ; polyline resource
pres@tfDoNDCOverlay      = True 
pres@gsLineThicknessF    = 45.0                          ; line thickness    


; --- Resources for the colorbar/labelbar
lres                          = True
lres@vpWidthF                 = 0.10                    ; Width of Labelbar
lres@vpHeightF                = 0.60                    ; Height of Labelbar
lres@lbPerimOn                = False                   ; Turn off perimeter.
;lres@lbOrientation            = "Horizontal"            ; Default is "Vertical"
lres@amLabelBarOrthogonalPosF = -1.0
lres@lbLabelAlignment         = "InteriorEdges"         ; Default is "BoxCenters".
lres@lbFillColors             = cmap(2:,:)              ; Colors for boxes.
lres@lbMonoFillPattern        = True                    ; Fill them all solid.
lres@lbLabelFontHeightF       = 0.015                   ; Font Height
lres@lbLabelAutoStride        = True                    ; Auto correct labels
lres@vpYF                     = 0.80                    ; location of left edge!!!!!!!!!!
lres@vpXF                     = 0.88                    ; location of top edge

; --- Draw polylines 
;do i = 0,ntra-1                                         ; Loop over all trajecories

  x = traj(0:(ntim-1),2)                              ; Longitudes for trajectory i
  y = traj(0:(ntim-1),3)                              ; Latitudes for trajectory i

  do k = 0,ntim-3                                       ; Loop over all times!!!!!!!!!!!!

      pres@gsLineColor = GetFillColor(cnLevels,cmap,traj(k,cnIndex))   ; color of polyline
      gsn_polyline  (wks,map,(/x(k),x(k+1)/),(/y(k),y(k+1)/),pres)       ; draw polyline
 
  end do    

;end do


; --- Draw colorbar/labelbar
gsn_labelbar_ndc(wks,dimsizes(cnLevels)+1,cnLabels,0.8,0.8,lres)


; ----------------- Markers ----------------------------------------------------------------

; --- Resources for the markers
kres             = True             ; marker resource
kres@gsMarkerSizeF       = 3.0                  ; marker size
kres@gsMarkerColor       = "black"          ; marker color
kres@gsMarkerIndex       = 4 


; --- Draw markers
;do i = 0,ntra-1                                         ; Loop over all trajecories

  x = traj(0:(ntim-1),2)                              ; Longitudes for trajectory i
  y = traj(0:(ntim-1),3)                              ; Latitudes for trajectory i

  do k = 0,ntim-3,1                                       ; Loop over all times

      gsn_polymarker(wks,map,x(k),y(k),kres)        ; mark position
 
  end do    
  mkres=True 
  mkres@gsMarkerIndex = 12 
  mkres@gsMarkerColor ="Red" 
  mkres@gsMarkerSizeF = 20. 
  mkres@gsMarkerThicknessF =18.0
  gsn_polymarker(wks,map,traj(0,2),traj(0,3),mkres)
;end do


; ----------------- Advance frame ----------------------------------- --------------------

frame(wks) 
