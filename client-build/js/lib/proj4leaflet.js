L.CRS.proj4js=function(){var e=function(e,t,n){typeof t!="undefined"&&(Proj4js.defs[e]=t);var r=new Proj4js.Proj(e);return{project:function(e){var t=new L.Point(e.lng,e.lat);return Proj4js.transform(Proj4js.WGS84,r,t)},unproject:function(e,t){var n=Proj4js.transform(r,Proj4js.WGS84,e.clone());return new L.LatLng(n.y,n.x,t)}}};return function(t,n,r){return L.Util.extend({},L.CRS,{code:t,transformation:r?r:new L.Transformation(1,0,-1,0),projection:e(t,n)})}}();