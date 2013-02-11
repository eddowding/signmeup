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
                independent_biz: 0,
                veg_box: 0,
                group_buying: 0,
                csa: 0,
                supermarkets: 0,
                food_bank: 0,
                home_delivery: 0,
                longer_opening: 0,
                reduced_waste: 0,
                less_packaging: 0,
                work_food: 0,
                local_food: 0,
                seasonal_food: 0,
                organic_food: 0,
                ethnic_food: 0,
                cheaper_food: 0,
                branded_food: 0,
                healthy_ready_meals: 0 
            }
        }
    });
});  