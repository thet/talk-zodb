/* global L */
(function (L) {
  "use strict";

  var map, markers, marker, geopoints, bounds, i, size;

  map = L.map('map').setView([51.505, -0.09], 13);
  L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: 'abcd',
    minZoom: 0,
    maxZoom: 7,
    ext: 'png'
  }).addTo(map);

  markers = new L.MarkerClusterGroup({zoomToBoundsOnClick: true, spiderfyOnMaxZoom: true, maxClusterRadius: 1});  // 40
  geopoints = [
    {
      'title': 'programmatic',
      'lat': 47.200,
      'lng': 15.300,
      'popup': 'Me in Graz'
    },
    {
      'title': 'Me in the Twin Cities',
      'lat': 44.9655108,
      'lng': -93.2083529,
      'popup': 'Me in the Twin Cities'
    }
  ];
  for(i = 0; i < geopoints.length ; i = i+1){
    marker = new L.Marker([geopoints[i].lat, geopoints[i].lng])
      .bindPopup(geopoints[i].popup);
    markers.addLayer(marker);
  }
  map.addLayer(markers);
  bounds = markers.getBounds();
  map.fitBounds(bounds);
  map.setZoom(4);
  window.map = map;
}) (L);
