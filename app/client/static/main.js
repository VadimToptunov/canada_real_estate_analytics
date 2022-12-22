const map = L.map('map').setView([43.6532, -79.3832], 6, null);

	const tiles = L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_nolabels/{z}/{x}/{y}.png', {
		attribution: 'Carto © CC BY 3.0, OpenStreetMap © ODbL',
		maxZoom: 19,
		minZoom: 4,
        name: 'Carto Light'
	}).addTo(map);

	// control that shows FSA info on hover
	const info = L.control();

	info.onAdd = function (map) {
		this._div = L.DomUtil.create('div', 'info');
		this.update();
		return this._div;
	};

	info.update = function (props) {
		const contents = props ? `<b>${props.name}</b><br />${props.density} people / mi<sup>2</sup>` : 'Hover over an FSA';
		this._div.innerHTML = `<h4>1bd appartments average prices</h4>${contents}`;
	};

	info.addTo(map);


	// get color depending on average price value

	function getColor(price) {
		return price > 1600 ? '#800026' :
			   price > 1500  ? '#BD0026' :
			   price > 1400  ? '#E31A1C' :
			   price > 1300  ? '#FC4E2A' :
			   price > 1200  ? '#FD8D3C' :
			   price > 1100  ? '#FEB24C' :
			   price > 1000  ? '#FED976' :
			   price > 900 ? '#FFEDA0':
			   price > 800 ? '#a89d32':
			   price > 700 ? '#a4a832' :
			   price > 600 ? '#7ba832' :
			   price > 500 ? '#32a846' : '#32a869'
	}

	function style(feature) {
		return {
			weight: 2,
			opacity: 1,
			color: 'yellow',
			dashArray: '3',
			fillOpacity: 1,
			// fillColor: getColor(feature.properties.arcs)
			fillColor: 'blue'
		};
	}

	function highlightFeature(e) {
		const layer = e.target;

		layer.setStyle({
			weight: 10,
			color: '#a84632',
			dashArray: '',
			fillOpacity: 2
		});

		layer.bringToFront();

		info.update(layer.feature.properties);
	}

	async function getPrices(){
		let response = await fetch('http://localhost:5000/data'); //TODO: Fix CORS Policy issue
		let data = await response.json();
		console.log(data);
		return data;
		//ToDo: get prices from the DB
	}

	define( [ "jquery" ], function($) { //ToDo: Fix require.js:5 Uncaught Error: Mismatched anonymous define() module: issue
		$().ready(function () {
			$.getJSON("canada_topo.json",function(data){
				const datalayer = L.geoJson(data, {
					onEachFeature: async function (feature, featureLayer) {
						const pricedata = await getPrices();
						featureLayer.bindPopup(feature.properties.CFSAUID);
						featureLayer.setStyle(style(pricedata.res.average_price));
						//{
						// weight: 10,
						// color: '#a84632',
						// dashArray: '3',
						// fillOpacity: 2,
						// fillColor: getColor(pricedata),
						// );
						featureLayer.bringToFront();
					}
				}).addTo(map);
				map.fitBounds(datalayer.getBounds());
			});
		});
	});

	function resetHighlight(e) {
		geojson.resetStyle(e.target);
		info.update();
	}

	function zoomToFeature(e) {
		map.fitBounds(e.target.getBounds());
	}

	function onEachFeature(feature, layer) {
		layer.on({
			mouseover: highlightFeature,
			mouseout: resetHighlight,
			click: zoomToFeature
		});
	}

	const legend = L.control({position: 'bottomright'});

	legend.onAdd = function (map) {

		const div = L.DomUtil.create('div', 'info legend');
		const grades = [500, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600];
		const labels = [];
		let from, to;

		for (let i = 0; i < grades.length; i++) {
			from = grades[i];
			to = grades[i + 1];

			labels.push(`<i style="background:${getColor(from + 1)}"></i> ${from}${to ? `&ndash;${to}` : '+'}`);
		}

		div.innerHTML = labels.join('<br>');
		return div;
	};

	legend.addTo(map);