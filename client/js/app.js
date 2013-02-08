define([
    // Libraries.
    'jquery',
    'underscore',
    'backbone',
    'marionette',
    'views/mapView',
    'collections/signups'
    ], function($, _, Backbone, Marionette, mapView, signupCollection) {
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
            root: App.root
        });
    })
    
    App.addInitializer(function(options) {
        
        require([
            'jspostcode',
            'jquery.validate'
            ], function() {
                // Validators
                jQuery.validator.addMethod("postcode", function(value, element) { 
                  return checkPostCode(value)
                }, "Please enter a valid UK postcode");
            })
    });
    
    App.addInitializer(function(options) {
        App.signups = new signupCollection;
        App.map = new mapView({collection: App.signups});
    });
    
    App.vent.on("map:panto", function(latlng) {
        App.map.panTo(latlng);
    })
    App.vent.on("map:add_marker", function(signup) {
        App.map.showMarker(signup);
    })
    
    App.vent.on("postcodeform:submit", function(postcode){
        App.Router.navigate('postcode/' + postcode + '/',  {trigger: true} )
    });

    App.vent.on("infobox:show", function(id){
        require([
            'views/infoboxView',
            'models/localinfoModel'
        ], function(infoboxView, localinfoModel){
            // var info_model = new localinfoModel({ward: id});
            // Just show all of thr UK for now:
            if (App.info_model == undefined) {
                App.info_model = new localinfoModel({id: 'UK'});
                var view = new infoboxView({model: App.info_model});
                App.info_model.fetch({
                    success: function() {
                        App.regionInfobox.show(view)
                        App.regionInfobox.$el.slideDown()
                    }
                });
            } else {
                App.regionInfobox.currentView.model.fetch()
            }
        
        });
        
        
        
        
    });
    
    window.App = App
    return App
})
