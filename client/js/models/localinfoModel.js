define([
    'app',
    'backbone',
], function(App, Backbone) {
    return Backbone.Model.extend({
        url: function() {
            return "/api/v1/infobox/" + this.get("ward") + '/';
        },
    });
});