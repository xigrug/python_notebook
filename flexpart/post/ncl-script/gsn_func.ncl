; -----------------------------------------------------
; AUTHOR: ZIQIANG JIANG, NANJING UNIVERSITY, 01/21/2013
; -----------------------------------------------------
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

; *****************************************************
undef("gsn_add_geom")
function gsn_add_geom(wks[1]:graphic,plot[1]:graphic,shpfile[1]:file,gsres[1]:logical)
; read some shapefiles and draw administrative boundary over a map
local geometry, segments, geomDims, segsDims, geom_segIndex, \ 
      geom_numSegs, segs_xyzIndex, segs_numPnts, lines, lon, \
      lat, segNum, startSegs, numSegs, startPT, endPT
begin

   ; read data off shapefile
   geometry = shpfile->geometry
   segments = shpfile->segments
   geomDims = dimsizes(geometry)
   segsDims = dimsizes(segments)

   ; read global attributes
   geom_segIndex = shpfile@geom_segIndex
   geom_numSegs  = shpfile@geom_numSegs
   segs_xyzIndex = shpfile@segs_xyzIndex
   segs_numPnts  = shpfile@segs_numPnts

   ; array to hold polylines
   lines = new(segsDims(0),graphic)

   ; read lon/lat off shapefile
   lon = shpfile->x
   lat = shpfile->y

   segNum = 0
   do i = 0, geomDims(0)-1
      startSegs = geometry(i,geom_segIndex)
      numSegs   = geometry(i,geom_numSegs)
      do seg = startSegs,startSegs+numSegs-1
         startPT = segments(seg,segs_xyzIndex)
         endPT   = startPT+segments(seg,segs_numPnts)-1
         lines(segNum) = gsn_add_polyline(wks,plot,lon(startPT:endPT),lat(startPT:endPT),gsres)
         ; counter for adding polylines
         segNum = segNum + 1
      end do
   end do

   return(lines)

end

; *****************************************************
undef("gsn_add_bou")
function gsn_add_bou(wks[1]:graphic,plot[1]:graphic,shpfile:string)
; Read a shapefile "BOUNT_poly.shp" and draw county boundary
local plres, bou, lns
begin

   ; resources for polylines
   plres = True
   plres@gsLineDashPattern = 0
   plres@gsLineThicknessF  = 2
   bou = addfile(shpfile+".shp","r");
   lns = gsn_add_geom(wks,plot,bou,plres)
   return(lns)

end

; *****************************************************
undef("gsn_add_river")
function gsn_add_river(wks[1]:graphic,plot[1]:graphic,shpfile:string)
; Read a shapefile "BOUNT_poly.shp" and draw county boundary
local plres, bou, lns
begin

   ; resources for polylines
   plres = True
   plres@gsLineDashPattern = 7
   plres@gsLineThicknessF  = 2
   bou = addfile(shpfile+"river.shp","r");
   lns = gsn_add_geom(wks,plot,bou,plres)
   return(lns)

end

; *****************************************************
undef("pie_chart")
function pie_chart(wks:graphic, percent[*]:numeric, name[*]:string        \
                              , colors[*]:string, pieChartRes:logical)
;                    Create a Pie Chart
; Nomenclature
;      percent     - percent [%: 0-100] for each section: sum(percent)=100
;                    percent = (/ 30, 10.5, 20, 39.5 /)/)
;      name        - names to be associated with each section
;                    name = (/ "Apple", "Spinach", "Orange", "Banana"/)
;      color         colors for each section
;                    color = (/ "red", "green", "blue", "brown" /)
;      pieChartRes - resources which affect plot appearance    
;                    Some examples
;                    pieChartRes = True
;                    pieChartRes@tiMainString= " ..."   [default is no title]
;                    pieChartRes@pcLabelType = "section"   [default]
;                    pieChartRes@pcLabelType = "block"  [labels beneath chart]
 begin
  rad       = 4.*atan(1.0)/180.                ; degress to radians
  nSections = dimsizes(percent) 
                                               ; Specify limits for X and Y axes.
  circ              = 60                       ; arbitrary
  extraSpace        = 100-circ                 ; Extra space beyond outer circle

  opts              = True                     ; local and default options
  if (pieChartRes .and. \
      isatt(pieChartRes,"pcLabelType") .and. pieChartRes@pcLabelType.eq."block") then
                                               ; block
      opts@vpXF     = 0.125                    ; default=0.2
      opts@vpYF     = 0.925                    ; default=0.8 
      opts@vpWidthF = 0.6                     ; default=0.6
      opts@vpHeightF= 0.6                     ; default=0.6
  else                                        
                                               ; section
      opts@vpXF     = 0.125                    ; default=0.2
      opts@vpYF     = 0.90                     ; default=0.8 
      opts@vpWidthF = 0.75                     ; default=0.6
      opts@vpHeightF= 0.75                     ; default=0.6
  end if

  opts@trXMinF      = -circ-extraSpace         ; min X 
  opts@trXMaxF      =  circ+extraSpace         ; max X
  opts@trYMinF      = -circ-extraSpace         ; min Y
  opts@trYMaxF      =  circ+extraSpace         ; max Y

  opts@tmXTOn       = False                    ; turn off tick marks on each side
  opts@tmXBOn       = False
  opts@tmYLOn       = False
  opts@tmYROn       = False
  opts@tmXBBorderOn = False                    ; turn off borders on each side
  opts@tmXTBorderOn = False
  opts@tmYLBorderOn = False
  opts@tmYRBorderOn = False
  opts@gsnFrame     = False                    ; do not advance frame
  opts@gsnDraw      = False                    ; do not draw
  opts@xyMonoDashPattern = True   

  if (pieChartRes .and. isatt(pieChartRes,"tiMainString")) then
      opts@tiMainString   = pieChartRes@tiMainString
      opts@tiMainOffsetYF = pieChartRes@tiMainOffsetYF
;      opts@tiMainOffsetYF = -0.05              ; move tiMainString down a bit
                                               ; leave roome for section label
      if (isatt(pieChartRes,"pcLabelType") .and. \
          pieChartRes@pcLabelType.eq."block") then
;          opts@tiMainOffsetYF = -0.065         ; no section label, move down more 
      end if
  end if
 ;print(opts)

  plotPC = gsn_xy(wks,(/0.0,0.0/),(/0.0,0.0/),opts)      ; background 
;;plotPC = gsn_csm_xy(wks,(/0.0,0.0/),(/0.0,0.0/),opts)  

  plRes  = True                                ; polyline resources
  plRes@gsLineColor        = "black"
  plRes@gsLineThicknessF   = 1.0

  gsRes  = True                                ; polymarker resources
  gsRes@gsMarkerIndex      = 16
  gsRes@gsMarkerSizeF      = 0.0115  
 ;gsRes@gsMarkerThicknessF = 0.0175
  if (pieChartRes .and. isatt(pieChartRes,"gsMarkerSizeF")) then
      gsRes@gsMarkerSizeF  = pieChartRes@gsMarkerSizeF
  end if

  txRes  = True                                ; text resources
  txRes@txJust             = "CenterLeft"
  txRes@txFontHeightF      = 0.0125            ; default=0.05
  if (pieChartRes .and. isatt(pieChartRes,"txFontHeightF")) then
      txRes@txFontHeightF = pieChartRes@txFontHeightF
  end if

  pgRes  = True                                ; polygon resources

  xOrig  = 0.0
  yOrig  = 0.0
  xLoc   = 0.0
  yLoc   = 0.0

  pcPie  = (percent/100.)*360                  ; percent of 360 degrees 
  pcStrt = 0.0 
  pcLast = pcPie(0)
  phase  = 90.0 - 0.5*pcPie(0)                 ; 'center' 1st section n=0

  do n=0,nSections-1
                                               ; create nodes for section
     npts  = max( (/round(pcPie(n),3), 1/) )
     npts2 = npts+2
     xx    = new (npts2, "double", "No_FillValue")
     yy    = new (npts2, "double", "No_FillValue")
     xx(0) = xOrig
     yy(0) = yOrig
     xx(1:npts2-2) = circ*cos((fspan(pcStrt, pcLast, npts)+phase)*rad)
     yy(1:npts2-2) = circ*sin((fspan(pcStrt, pcLast, npts)+phase)*rad)
     xx(npts2-1)   = xOrig
     yy(npts2-1)   = yOrig

     pgRes@gsFillColor   =  colors(n)          ; fill with associated color
     plotPC@$unique_string("dum")$ = gsn_add_polygon (wks, plotPC, xx, yy, pgRes)  ; color fill
     plotPC@$unique_string("dum")$ = gsn_add_polyline(wks, plotPC, xx, yy, plRes)  ; outline

     gsRes@gsMarkerColor = colors(n)           ; associate marker
     if (percent(n).lt.10) then
         text = sprintf("%5.1f", percent(n))+"  "+name(n)  ; include %
     else
         text = sprintf("%4.1f", percent(n))+"  "+name(n)  ; include %
     end if
                                               ; labels
  if (pieChartRes .and. \
      isatt(pieChartRes,"pcLabelType") .and. pieChartRes@pcLabelType.eq."block") then
                                               ; block labels
     if ((n%2).eq.0) then
         mx   = -circ+10.                      ; left  column labels    
     else
         mx   =  circ*0.1                      ; right column labels
     end if
   ;;datatondc(plotPC,0.0,-circ, xLoc, yLoc)
   ;;ny = yLoc - ????
     ny   = -(circ+9)
     ix   = 5   
     iy   = 6.0+3.4
     jy   = ny-(n/2)*iy
    ;print("jy="+jy)
     plotPC@$unique_string("dum")$ = gsn_add_polymarker(wks, plotPC,       mx   , jy, gsRes)
     plotPC@$unique_string("dum")$ = gsn_add_text      (wks, plotPC, text, mx+ix, jy, txRes)

  else    ; must be "section" labeling
                                               ; section labels
     xxInfo = (circ+0.25*extraSpace)*cos(((pcStrt+pcLast)*0.5+phase)*rad)
     yyInfo = (circ+0.25*extraSpace)*sin(((pcStrt+pcLast)*0.5+phase)*rad)
     angle  = atan2(xxInfo,yyInfo)/rad
    ;print("n="+n+"   angle="+angle+"   "+colors(n))
     ix     = 5   
     if (angle.gt.-0.001) then                 ; round
         txRes@txJust  = "CenterLeft"
         plotPC@$unique_string("dum")$ = gsn_add_polymarker(wks, plotPC,       xxInfo   , yyInfo, gsRes)
         plotPC@$unique_string("dum")$ = gsn_add_text      (wks, plotPC, text, xxInfo+ix, yyInfo, txRes)
     else
         txRes@txJust  = "CenterRight"
         plotPC@$unique_string("dum")$ = gsn_add_polymarker(wks, plotPC,       xxInfo   , yyInfo, gsRes)
         plotPC@$unique_string("dum")$ = gsn_add_text      (wks, plotPC, text, xxInfo-ix, yyInfo, txRes)
     end if

  end if

     delete(xx)
     delete(yy)

     if (n.lt.(nSections-1)) then 
         pcStrt = pcLast+0.001
         pcLast = pcLast+pcPie(n+1)
     end if
  end do

  if (.not.isatt(pieChartRes,"gsnDraw") .or. \
     (isatt(opts,"gsnDraw") .and. opts@gsnDraw)) then 
	draw(plotPC)
  end if

  if (.not.isatt(pieChartRes,"gsnFrame") .or. \
     (isatt(opts,"gsnFrame") .and. opts@gsnFrame)) then 
	frame(wks)
  end if

  return (plotPC)
 end
