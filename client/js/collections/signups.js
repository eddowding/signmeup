define([
    'backbone',
    'models/signupModel'
], function(Backbone, signupModel) {
    return Backbone.Collection.extend({
        url: function() {
            url = "/api/v1/signup/?limit=0";
            if (this.bounds_str != undefined) {
                url += "&within_distance=" + this.bounds_str
            }
            return url;
        },
        model: signupModel
    });
});