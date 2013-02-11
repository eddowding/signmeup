define(["backbone","marionette","leaflet","openspace","proj4js","proj4leaflet"],function(e,t,n){return e.View.extend({initialize:function(e){return this.start=this.options.start||new n.LatLng(51.47,-0.08),this.initial_zoom=this.options.start||8,this.on("map:setview",this.setview),this.iconClass=n.icon({iconUrl:"/static/images/marker-icon.png",iconSize:[28,45],iconAnchor:[14,45],popupAnchor:[-3,-76],shadowUrl:"/static/images/marker-shadow.png",shadowSize:[68,95],shadowAnchor:[22,94]}),this.render()},showMarker:function(e){var t=this.map,r=this.iconClass,i=e.location||e.get("location");i!=undefined&&n.marker(i,{icon:r}).addTo(t)},showMarkers:function(){var e=this,t=e.map.getCenter();this.collection.bounds_str=t.lat+","+t.lng,this.collection.fetch({success:function(t){var n=t.models[0].get("objects");_.each(n,function(t){e.showMarker(t)})}})},fixLatLng:function(e){var t,n,r,i;r=0,i=0;var s=e[0],o=e[1];return s>0?t=s+r:t=s-r,o>0?n=o+i:n=o-i,[t,n]},panTo:function(e){e=this.fixLatLng(e),this.map.panTo(e),this.showMarkers()},render:function(){function o(t){var n=t.target._animateToZoom,r=e[n-1];r<5&&r!==2.5?(s.removeLayer(os200),s.addLayer(os250)):(s.removeLayer(os250),s.addLayer(os200))}var e=[2500,1e3,500,200,100,50,25,10,5,4,2.5,2,1],t=new n.Transformation(1,0,-1,0),r=n.CRS.proj4js("EPSG:27700","+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-97910 +ellps=airy +datum=OSGB36 +units=m +no_defs",t),i=function(t){var n=e[t-1],r=1/n;return r},s=new n.Map("map",{crs:r,minZoom:1,maxZoom:13,continuousWorld:!0,dragging:!1,touchZoom:!1,scrollWheelZoom:!1,doubleClickZoom:!1,boxZoom:!1,keyboard:!1,zoomControl:!1});s.options.crs.scale=i,os200=new n.TileLayer.OS("D49792D09074EC09E0405F0ACA606F42",{tileSize:200}),os250=new n.TileLayer.OS("D49792D09074EC09E0405F0ACA606F42",{tileSize:250}),this.initial_zoom==10?s.addLayer(os250):s.addLayer(os200),s.setView(this.start,this.initial_zoom),s.on("zoomend",o),this.map=s,this.showMarkers()}})});