define([
    'app',
    'backbone',
    'marionette',
], function(App, Backbone, Marionette) {
    return Backbone.Marionette.ItemView.extend({
        template: '#infoboxView',
        modelEvents: {
            "change": "render"
          },
    });
});
