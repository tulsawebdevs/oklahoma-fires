$(document).ready(function(){

  var addAllMarkers = function(map){
    for(var i in firedata){
      new google.maps.Marker({
        position: new google.maps.LatLng(firedata[i].latitude, firedata[i].longitude),
        map: map
      });
    }
  }


  // Start and add map to screen and kick off the
  // process of adding markers to the map
  var initializeMap = function(latitude, longitude){
    var mapOptions = {
      center: new google.maps.LatLng(latitude, longitude),
      zoom: 9,
      mapTypeId: google.maps.MapTypeId.HYBRID
    };

    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(latitude, longitude),
      map: map
    });

    addAllMarkers(map);
  }


  // Check for current location and get lat and long
  // then initialize the map based on that data
  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position){
      initializeMap(position.coords.latitude, position.coords.longitude);
    });
  } else {
    initializeMap(33.79740, -93.69140);
  }

});
