define([
    'backbone', 
    'marionette', 
    'app'], 
    function (Backbone, Marionette, App) {
        return Backbone.Marionette.AppRouter.extend({
            routes: {
                ''                           : 'home',
                'postcode/:postcode/'        : 'postcode',
                'thanks/'                     : 'thanks',
                'share/'                     : 'share',
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
                    var view = new postcodeView({model: postcode_model, signup: signup_model});
                    postcode_model.fetch({
                        success: function() {
                            signup_model.set({location: [postcode_model.get('wgs84_lat'), postcode_model.get('wgs84_lon')]});
                            App.regionMain.show(view);
                            App.vent.trigger("infobox:show");
                        }
                    });
                });
            },
            thanks: function() {
                    require([
                        'views/thankyouView',
                    ], function(thankyouView){
                        App.vent.trigger('infobox:show')
                        var view = new thankyouView();
                            App.regionMain.show(view)
                        });
                
            },
            share: function() {
                    require([
                        'views/shareView',
                    ], function(shareView){
                        App.vent.trigger('infobox:show')
                        var view = new shareView();
                            App.regionMain.show(view)
                        });
                
            }
            
        })
});
