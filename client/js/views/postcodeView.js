define([
    'app',
    'backbone',
    'marionette',
    'jspostcode',
    'jquery.validate',
    'syphon'
], function(App, Backbone, Marionette) {
    return Backbone.Marionette.ItemView.extend({
        template: '#postcodeView',
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
