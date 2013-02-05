define([
    'app',
    'backbone',
], function(App, Backbone) {
    return Backbone.Model.extend({
        url: function() {
            var base = '/api/v1/signup/';
            return this.id ? base + this.id + '' : base;
        }
    });
});