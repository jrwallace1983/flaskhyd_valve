
	function onEachFeature(feature, layer) {
		var popupContent = "<p>" +
				feature.geometry.type + " " +feature.properties.street + "</p>";

		if (feature.properties && feature.properties.popupContent) {
			popupContent += feature.properties.popupContent;
		}

		layer.bindPopup(popupContent);
		if (feature.properties.street != null){ return true}
	}

	function Filter(feature) {
  		if (feature.properties.street != null){ return true}
	}