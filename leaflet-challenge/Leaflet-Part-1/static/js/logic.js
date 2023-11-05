
// First we andle the backgound of the map that we will addby creating a tile layer.
console.log("Creating the tile layer ...");
let mapBackgraound = L.tileLayer(
  "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png'",
  {
    attribution:
      'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
  });

// Creating the map object and adding options.
let map = L.map("map", {
  center: [
    40.7, -94.5
  ],
  zoom: 3
});

// Adding the ap to the "mapBackground" we created.
mapBackgraound.addTo(map);

// Gettingh earthquake geoJSON data y calling AJAX
d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson").then(function (data) {

  // Creating a function that returns the style of the map for a agiven feature object.
  // Here the raduis  the style is based on the earthquake magnitude
  function setStyle(feature) {
    return {
      opacity: 1,
      fillOpacity: 1,
      fillColor: markerColor(feature.geometry.coordinates[2]),
      color: "#000000",
      radius: setRadius(feature.properties.mag),
      stroke: true,
      weight: 0.5
    };
  }

  // Creating a function that sets the marker color based on the magnitude of the earthquake.
  function markerColor(depth) {
    switch (true) {
      case depth > 90:
        return "#FF0000";
      case depth > 70:
        return "#orangered";
      case depth > 50:
        return "orange";
      case depth > 30:
        return "yellow";
      case depth > 10:
        return "greenyellow";
      default:
        return "#00FF00";
    }
  }

  //Creating a function that sets the radius f circle according to the magnitude of earthquae.
  // This function should handle the radius for earthquakes with a magnitude of 0.
  function setRadius(magnitude) {
    if (magnitude === 0) {
      return 1;
    }

    return magnitude * 4;
  }

  // Adding GeoJSON layer to the map once the file is loaded.
  L.geoJson(data, {
    // Adding circleMarker from features of earthquakes on the map.
    pointToLayer: function (feature, latlng) {
      return L.circleMarker(latlng);
    },
    // Setting the style for each circleMarker using our setStyle function.
    style: setStyle,
    // We create a popup for each marker to display the magnitude and location of the earthquake after the marker has been created and styled
    onEachFeature: function (feature, layer) {
      layer.bindPopup(
        "Magnitude: "
        + feature.properties.mag
        + "<br>Depth: "
        + feature.geometry.coordinates[2]
        + "<br>Location: "
        + feature.properties.place
      );
    }
  }).addTo(map);

  // Creating legend control object.
  let legend = L.control({
    position: "bottomright"
  });

  // Adding details to the legend
  legend.onAdd = function () {
    let div = L.DomUtil.create("div", "info legend");

    let legGrades = [-10, 10, 30, 50, 70, 90];
    let legColors = [
      "#00FF00",
      "greenyellow",
      "yellow",
      "orange",
      "orangered",
      "#FF0000"
    ];

    // Looping through our intervals to generate a label with a colored square for each interval.
    for (let i = 0; i < legGrades.length; i++) {
      div.innerHTML += "<i style='background: " + legColors[i] + "'></i> "
        + legGrades[i] + (legGrades[i + 1] ? "&ndash;" + legGrades[i + 1] + "<br>" : "+");
    }
    return div;
  };

  // Finally, we our legend to the map.
  legend.addTo(map);
});
