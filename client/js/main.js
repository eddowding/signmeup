/*jslint regexp: true, nomen: true, sloppy: true */
/*global window, document, define, Backbone */
require.config({
    shim: {
        'underscore': {
            exports: '_'
        },
        'backbone': {
            deps: [
                'underscore',
                'jquery'
            ],
            exports: 'Backbone'
        },
        'backbone-tastypie': {
            deps: [
                'underscore',
                'jquery',
                'backbone',
            ]
        },
        'leaflet': {
            exports: 'L',
        },
        'proj4leaflet': {
            deps: [
            'leaflet'
            ]
        },
        'openspace': {
            deps: ['leaflet']
        },
        'jspostcode': {
            deps: [
            'jquery'
            ]
        }
    },
    paths: {
        'backbone': "lib/backbone-min",
        'backbone-tastypie': "lib/backbone-tastypie",
        'backbone-analytics': "lib/backbone.analytics",
        'marionette': 'lib/backbone.marionette.min',
        'syphon': 'lib/backbone.syphon.min',
        'text': 'lib/text',
        'underscore': 'lib/underscore-min',
        'leaflet': 'lib/leaflet',
        'openspace': 'lib/openspace',
        'proj4js': 'lib/proj4js-compressed',
        'proj4leaflet': 'lib/proj4leaflet',
        'jspostcode': 'lib/jspostcode',
        'jquery.validate': 'lib/jquery.validate.min'
        
    }
});


require([
    'app',
    'router'], 
    function(App, Router) {
        App.Router = new Router();
        App.start();
    });
