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
        })
    }
}