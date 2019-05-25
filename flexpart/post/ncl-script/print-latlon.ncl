load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/shea_util.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/wrf/WRFUserARW.ncl"
load "gsn_func.ncl"

begin

; *****************************************************

   input_head = addfile("/data/reg/trajectory/flexpart/output/2018-04-01-Backward/header_d01.nc","r")
   ;input_wrf = addfile("wrfout_d02_2016-04-19_00_00_00.nc","r")
   
   lat2d   = input_head->XLAT(:,:)
   lon2d   = input_head->XLONG(:,:)
   print(min(lat2d))
   print(min(lon2d))
   print(max(lat2d))
   print(max(lon2d))
end
