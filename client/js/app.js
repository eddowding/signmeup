define([
    // Libraries.
    'jquery',
    'underscore',
    'backbone',
    'marionette',
    'views/mapView'
    ], function($, _, Backbone, Marionette, mapView) {
    'use strict';
    
    var App = new Marionette.Application();
    
    App.addRegions({
        regionMenu: '#menu',
        regionMain: '#content',
        regionMap: '#map',
        regionInfobox: '#infobox'
    });
    
    // Set up basic paths.
    App.root = '/';
    
    App.addInitializer(function(options) {
        Backbone.history.start({
            pushState: true,
            root: App.root
        });
    })
    
    App.addInitializer(function(options) {
        App.map = new mapView();
    });
    
    App.vent.on("map:panto", function(latlng) {
        App.map.panTo(latlng);
    })
    
    App.vent.on("postcodeform:submit", function(postcode){
        App.Router.navigate('postcode/' + postcode + '/',  {trigger: true} )
    });

    App.vent.on("infobox:show", function(id){
        
        
        require([
            'views/infoboxView',
            'models/localinfoModel'
        ], function(infoboxView, localinfoModel){
            var info_model = new localinfoModel({ward: id});
            var view = new infoboxView({model: info_model});
            info_model.fetch({
                success: function() {
                    App.regionInfobox.show()
                    App.regionInfobox.$el.slideDown()
                }
            });
        
        });
        
        
        
        
    });
    
    window.App = App
    return App
})
