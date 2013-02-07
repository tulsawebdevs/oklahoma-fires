$(document).ready(function(){

    // Start and add map to screen and kick off the
    // process of adding markers to the map
    var initializeMap = function(latitude, longitude){
        var mapOptions = {
            center: new google.maps.LatLng(latitude, longitude),
            zoom: 7,
            mapTypeId: google.maps.MapTypeId.HYBRID
        };

        var map = new google.maps.Map(
            document.getElementById("map"), 
            mapOptions
        );

        $.ajax({
            url: '/fire/all/',
            success: function(data){
                data.forEach(function(element, index){
                    new google.maps.Marker({
                        position: new google.maps.LatLng(
                            element.fields.latitude,
                            element.fields.longitude
                        ),
                        map: map
                    });
                });
            }
        });
    }
    
    // start map over Tulsa
    initializeMap(36.150505,-95.958329);

});
