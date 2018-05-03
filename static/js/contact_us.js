$(document).ready(function () {
    if ($('.google-map-box').is(':visible')) {
        function initialize(lat, lng) {
            var mapCanvas = document.getElementById('google-map');
            var mapOptions = {
                center: new google.maps.LatLng(lat, lng),
                zoom: 16,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            var map = new google.maps.Map(mapCanvas, mapOptions)
        }
        var lng = $('.google-map-box .address-holder .contact-address').first().find('.lng').text();
        var lat = $('.google-map-box .address-holder .contact-address').first().find('.lat').text();
        google.maps.event.addDomListener(window, 'load', initialize(lat, lng));

        $('.google-map-box select.contact-select').on('change', function() {
            $('.google-map-box .address-holder .contact-address' ).hide();
            $('.google-map-box .address-holder .contact-address.'+this.value).show();
            var lng = $('.google-map-box .address-holder .contact-address.'+this.value).find('.lng').text();
            var lat = $('.google-map-box .address-holder .contact-address.'+this.value).find('.lat').text();
            google.maps.event.addDomListener(window, 'load', initialize(lat, lng));
        });
    }

    //var NorthAmerica = ['AG', 'BG', 'BB', 'BZ', 'HT', 'GT', 'HN', 'GD', 'DM', 'DO',
    //    'CA', 'CR', 'CU', 'MX', 'NI', 'PA', 'SV', 'VC', 'KN', 'LC', 'US', 'TT', 'JM'];
    //var SouthAmerica = ['AR', 'BO', 'BR', 'VE', 'GY', 'CO', 'PY', 'PE', 'SR', 'UY', 'CL', 'EC']

    //function GetCountry() {
    //    var geocoder = new google.maps.Geocoder();
    //    navigator.geolocation.getCurrentPosition(showPosition);
    //    function showPosition(position) {
    //        var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    //        geocoder.geocode({'latLng': latlng}, function(results, status) {
    //            if (status == google.maps.GeocoderStatus.OK) {
    //                if (results[0]) {
    //                    var loc = getCountry(results);
    //                }
    //            }
    //        });
    //    }
    //    function getCountry(results) {
    //        for (var i = 0; i < results[0].address_components.length; i++) {
    //            var shortname = results[0].address_components[i].short_name;
    //            var type = results[0].address_components[i].types;
    //            if (type.indexOf("country") != -1) {
    //                if (shortname in SouthAmerica.concat(NorthAmerica)) {
    //                    console.log('America')
    //                } else {
    //                    console.log('Europe')
    //                }
    //            }
    //        }
    //    }
    //}
});
