define([
    'backbone',
    'marionette',
    'leaflet',
    'openspace',
    'proj4js',
    'proj4leaflet'
], function(Backbone, Marionette, L) {
    return Backbone.View.extend({
        initialize: function(options) {
            this.start = this.options.start || new L.LatLng(51.47, -0.08);
            this.initial_zoom = this.options.start || 8
            this.on("map:setview", this.setview)
            this.iconClass = L.icon({
                iconUrl: '/static/images/marker-icon.png',
                iconSize: [28, 45],
                iconAnchor: [14, 45],
                popupAnchor: [-3, -76],
                shadowUrl: '/static/images/marker-shadow.png',
                shadowSize: [68, 95],
                shadowAnchor: [22, 94]
            });

            return this.render();
        },
        showMarker: function(signup) {
            var map = this.map;
            var icon = this.iconClass;
            var location = signup.location || signup.get('location');
            if (location != undefined) {
                L.marker(location, {icon:icon}).addTo(map);
            }
        },
        showMarkers: function() {
            var view = this;

            var bounds = view.map.getCenter();
            this.collection.bounds_str = bounds.lat + ',' + bounds.lng
            this.collection.fetch({
                success: function(collection) {
                    var objects = collection.models[0].get('objects');
                    _.each(objects, function(signup) {
                        view.showMarker(signup);
                    })
                }
            })
        },
        fixLatLng: function(latlng) {
            var newlat, newlon, lat_shiftamount, lon_shiftamount;
            lat_shiftamount = 0.000;
            lon_shiftamount = 0.000;
            var lat = latlng[0];
            var lon = latlng[1];
            if (lat > 0) {
                newlat = lat+lat_shiftamount
            } else {
                newlat = lat-lat_shiftamount
            }
            if (lon > 0) {
                newlon = lon+lon_shiftamount
            } else {
                newlon = lon-lon_shiftamount
            }
            return [newlat ,newlon]
        },
        panTo: function(latlng) {
            latlng = this.fixLatLng(latlng);
            this.map.panTo(latlng);
            this.showMarkers();
        },
        render: function() {
            var res = [2500, 1000, 500, 200, 100, 50, 25, 10, 5, 4, 2.5, 2, 1];
            
            var osgbTransform = new L.Transformation(1, 0, -1, 0);
            var osgbCrs = L.CRS.proj4js('EPSG:27700', 
            "+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-97910 +ellps=airy +datum=OSGB36 +units=m +no_defs", 
            osgbTransform);

            var scaleFn = function(zoom) {
                var tileRes = res[zoom-1];
                var scale = 1/tileRes;
                return scale;
            }
            
            var map = new L.Map('map', {
                crs: osgbCrs,
                minZoom: 1,
                maxZoom: 13,
                continuousWorld: true,
                dragging: false,
                touchZoom: false,
                scrollWheelZoom: false,
                doubleClickZoom: false,
                boxZoom: false,
                keyboard: false,
                zoomControl: false
            });

            map.options.crs.scale = scaleFn;
            
            os200 = new L.TileLayer.OS("D49792D09074EC09E0405F0ACA606F42", { tileSize: 200 });
            os250 = new L.TileLayer.OS("D49792D09074EC09E0405F0ACA606F42", { tileSize: 250 });
            if (this.initial_zoom == 10) {
                map.addLayer(os250);
            } else {
                map.addLayer(os200);
            }
            
            map.setView(this.start, this.initial_zoom);

            function adjustTileSize(e) {
                var z = e.target._animateToZoom;
                var r = res[z-1];
                if(r < 5 && r !== 2.5){
                    map.removeLayer(os200);
                    map.addLayer(os250);
                }else{
                    map.removeLayer(os250);
                    map.addLayer(os200);
                };
            }
            map.on('zoomend', adjustTileSize);
            this.map = map;
            this.showMarkers()
        },
    });
})
