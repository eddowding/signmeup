define([
    'backbone', 
    'marionette', 
    'app'], 
    function (Backbone, Marionette, App) {
        return Backbone.Marionette.AppRouter.extend({
            routes: {
                ''                           : 'home',
                'postcode/:postcode/'        : 'postcode',
            },
            home: function() {
                require([
                    'views/postcodeFormView'
                ], function(postcodeFormView){
                    view = new postcodeFormView()
                    App.regionMain.show(view)
                });
            },
            postcode: function(postcode) {
                require([
                    'views/postcodeView',
                    'models/postcodeModel',
                    'models/signupModel'
                ], function(postcodeView, postcodeModel, signupModel){
                    var postcode_model = new postcodeModel({postcode: postcode});
                    var signup_model = new signupModel();
                    var view = new postcodeView({model: postcode_model});
                    postcode_model.fetch({
                        success: function() {
                            App.regionMain.show(view);
                        }
                    });
                });
            },
            
            
        })
});
