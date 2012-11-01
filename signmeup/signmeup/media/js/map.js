var points_data

function setHomeView() {
    return map.setView([54.805, -3.09], 6)
}

var map = L.map('map', {
    scrollWheelZoom: false,
    touchZoom: false,
    doubleClickZoom: false,
    zoomControl: false,
    boxZoom: false
})
setHomeView();

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 
    {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);


function move_to_postcode(postcode) {
    if (postcode) {
        $.getJSON('http://mapit.mysociety.org/postcode/' + postcode, function(data) {
            var latlng = new L.LatLng(data.wgs84_lat, data.wgs84_lon);
            map.setView(latlng, 14)
            map.on('moveend', function() {
                load_points()
            })
        })
    }
}

function load_points() {
    box = map.getBounds()
    points = [
        box._southWest.lat,
        box._southWest.lng,
        box._northEast.lat,
        box._northEast.lng
    ]
    return $.getJSON('/api/v1/signup/?format=json&within_box=' + points.join(), function(data) {
        add_points(data)
    })
}


function add_points(points_data) {
    for (point in points_data.objects) {
        p = points_data.objects[point]
        var marker = L.marker(p.location).addTo(map);
    }
}





