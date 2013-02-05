define([
    'app',
    'backbone',
    'marionette',
], function(App, Backbone, Marionette) {
    return Backbone.Marionette.ItemView.extend({
        template: '#infoboxView',
        modelEvents: {
            "change": "modelChanged"
        },
        events: {
            'click button[type=submit]' : 'submitForm'
        },
        modelChanged: function() {
            lat = this.model.get('wgs84_lat')
            lon = this.model.get('wgs84_lon')
            App.vent.trigger('map:panto', [lat, lon])
        },
        onRender: function() {
            App.vent.trigger('map:setview', 'something')
        },
        submitForm: function(e) {
            e.preventDefault()
            var data = Backbone.Syphon.serialize(this);
            // Make model from data, save it.
        }
    });
});
