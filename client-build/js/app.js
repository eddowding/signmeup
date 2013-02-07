define(["jquery","underscore","backbone","marionette","views/mapView","collections/signups"],function(e,t,n,r,i,s){var o=new r.Application;return o.addRegions({regionMenu:"#menu",regionMain:"#content",regionMap:"#map",regionInfobox:"#infobox"}),o.root="/",o.addInitializer(function(e){n.history.start({pushState:!0,root:o.root})}),o.addInitializer(function(e){require(["jspostcode","jquery.validate"],function(){jQuery.validator.addMethod("postcode",function(e,t){return checkPostCode(e)},"Please enter a valid UK postcode")})}),o.addInitializer(function(e){o.signups=new s,o.map=new i({collection:o.signups})}),o.vent.on("map:panto",function(e){o.map.panTo(e)}),o.vent.on("map:add_marker",function(e){o.map.showMarker(e)}),o.vent.on("postcodeform:submit",function(e){o.Router.navigate("postcode/"+e+"/",{trigger:!0})}),o.vent.on("infobox:show",function(e){require(["views/infoboxView","models/localinfoModel"],function(e,t){var n=new t({id:"UK"}),r=new e({model:n});n.fetch({success:function(){o.regionInfobox.show(r),o.regionInfobox.$el.slideDown()}})})}),window.App=o,o});