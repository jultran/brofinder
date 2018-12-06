var map;
function initMap() {
    if (navigator.geolocation) {
        // get position
        navigator.geolocation.getCurrentPosition(createMap);
    }
    else {
        // don't have permission for location, display generic map
        map = new google.maps.Map(document.getElementById('map'), {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 8
        });
    }
}

// use device location to create map
function createMap(position) {
    const lat = position.coords.latitude;
    const long = position.coords.longitude;

    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: lat, lng: long },
        zoom: 17
    });
}