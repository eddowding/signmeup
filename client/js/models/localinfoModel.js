define([
    'app',
    'backbone',
], function(App, Backbone) {
    return Backbone.Model.extend({
        url: function() {
            return "/api/v1/localinfo/" + this.get("id") + '/';
        },
        defaults:  {
            info : {
                local_food: 0,
            }
        }
    });
});