define([
    'app',
    'backbone',
], function(App, Backbone) {
    return Backbone.Model.extend({
        url: function() {
            var postcode = this.get('postcode');
            if (postcode != undefined) {
                return "http://mapit.mysociety.org/postcode/" + postcode
            }
        },
        toJSON : function() {
            this.set('friendlyName', this.friendlyName())
            return _.clone(this.attributes);
        },
        friendlyName: function() {
            var ward = this.get("shortcuts").ward;
            this.set('ward', ward);
            if (typeof(ward) == 'number') {
                return this.get('areas')[ward].name;
            } else {
                return this.get('areas')[ward.district].name;
            }
        }
    });
});