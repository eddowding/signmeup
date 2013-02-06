define([
    'app',
    'backbone',
    'marionette',
    'jspostcode',
    'jquery.validate'
], function(App, Backbone, Marionette) {
    return Backbone.Marionette.ItemView.extend({
        template: '#postcodeForm',
        onRender: function() {
            
            this.$el.find('form').validate({
                rules: {
                    postcode: {
                        required: true,
                        postcode: true
                    }
                },
                submitHandler: function(form) {
                    var postcode = $(form).find('[name=postcode]');
                    postcode = postcode.val().replace(' ', '');
                    App.vent.trigger("postcodeform:submit", postcode);
                    return false;
                } 
            });
    }
});
});
