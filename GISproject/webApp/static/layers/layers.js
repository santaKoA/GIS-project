var wms_layers = [];


        var lyr_OSMStandard_0 = new ol.layer.Tile({
            'title': 'OSM Standard',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' &middot; <a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors, CC-BY-SA</a>',
                url: 'http://tile.openstreetmap.org/{z}/{x}/{y}.png'
            })
        });
var format_gis_osm_pois_free_1_1 = new ol.format.GeoJSON();
var features_gis_osm_pois_free_1_1 = format_gis_osm_pois_free_1_1.readFeatures(json_gis_osm_pois_free_1_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_gis_osm_pois_free_1_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_gis_osm_pois_free_1_1.addFeatures(features_gis_osm_pois_free_1_1);
var lyr_gis_osm_pois_free_1_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_gis_osm_pois_free_1_1, 
                style: style_gis_osm_pois_free_1_1,
                interactive: true,
    title: '<img src="styles/legend/gis_osm_pois_free_1_1_43.png" /> embassy<br />'
        });

lyr_OSMStandard_0.setVisible(true);lyr_gis_osm_pois_free_1_1.setVisible(true);
var layersList = [lyr_OSMStandard_0,lyr_gis_osm_pois_free_1_1];
lyr_gis_osm_pois_free_1_1.set('fieldAliases', {'osm_id': 'osm_id', 'code': 'code', 'fclass': 'fclass', 'name': 'name', });
lyr_gis_osm_pois_free_1_1.set('fieldImages', {'osm_id': 'TextEdit', 'code': 'Range', 'fclass': 'TextEdit', 'name': 'TextEdit', });
lyr_gis_osm_pois_free_1_1.set('fieldLabels', {'osm_id': 'no label', 'code': 'no label', 'fclass': 'no label', 'name': 'no label', });
lyr_gis_osm_pois_free_1_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});