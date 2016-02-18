// Start and add map to screen and kick off the
// process of adding markers to the map
var initializeMap = function(latitude, longitude){
    var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';

    var mapOptions = {
        center: {lat: latitude, lng: longitude},
        zoom: 7,
        mapTypeId: google.maps.MapTypeId.HYBRID
    };

    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    $.ajax({
        url: '/api/events/',
        success: function(data){
            data.forEach(function(element, index){
                new google.maps.Marker({
                    position: new google.maps.LatLng(
                        element.latitude,
                        element.longitude
                    ),
                    map: map,
                    icon: iconBase + 'firedept.png'
                });
            });
        }
    });
};

// start map over Tulsa
initializeMap(36.150505,-95.958329);
