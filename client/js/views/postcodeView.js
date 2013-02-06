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
        modelChanged: function() {
            lat = this.model.get('wgs84_lat')
            lon = this.model.get('wgs84_lon')
            App.vent.trigger('map:panto', [lat, lon])
        },
        onRender: function() {
            App.vent.trigger('map:setview')
            var signup = this.options.signup;
            var postcode = this.model.get('postcode')
            var form = this.$el.find('form');
            form.validate({
                rules: {
                    postcode: {
                        required: true,
                        postcode: true
                    },
                    name: 'required',
                    email:{
                        required: true,
                        email: true
                    },
                },
                submitHandler: function(form) {
                    var data = Backbone.Syphon.serialize(form);
                    // Make model from data, save it.
                    signup.set(data)
                    signup.set({postcode: postcode})
                    signup.save(signup.attributes, {
                        success: function() {
                            App.Router.navigate('thanks/',  {trigger: true} )
                        }
                    })

                    return false;
                } 
            })
        },
    });
});
