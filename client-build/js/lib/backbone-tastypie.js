/**
 * Backbone-tastypie.js 0.1
 * (c) 2011 Paul Uithol
 * 
 * Backbone-tastypie may be freely distributed under the MIT license.
 * Add or override Backbone.js functionality, for compatibility with django-tastypie.
 */

(function(e){var t=window.Backbone;t.Tastypie={doGetOnEmptyPostResponse:!0,doGetOnEmptyPutResponse:!1,apiKey:{username:"",key:""}},t.oldSync=t.sync,t.sync=function(e,n,r){var i="";t.Tastypie.apiKey&&t.Tastypie.apiKey.username.length&&(i=_.extend({Authorization:"ApiKey "+t.Tastypie.apiKey.username+":"+t.Tastypie.apiKey.key},r.headers),r.headers=i);if(e==="create"&&t.Tastypie.doGetOnEmptyPostResponse||e==="update"&&t.Tastypie.doGetOnEmptyPutResponse){var s=new $.Deferred;return s.done(r.success),r.success=function(e,t,o){if(!!e||o.status!==201&&o.status!==202&&o.status!==204)return s.resolveWith(r.context||r,[e,t,o]);var u=o.getResponseHeader("Location")||n.id;return $.ajax({url:u,headers:i,success:s.resolve,error:s.reject})},s.fail(r.error),r.error=function(e,t,n){s.rejectWith(r.context||r,[e,t,n])},s.request=t.oldSync(e,n,r),s}return t.oldSync(e,n,r)},t.Model.prototype.idAttribute="resource_uri",t.Model.prototype.url=function(){var e=this.id;return e||(e=this.urlRoot,e=e||this.collection&&(_.isFunction(this.collection.url)?this.collection.url():this.collection.url),e&&this.has("id")&&(e=n(e)+this.get("id"))),e=e&&n(e),e||null},t.Model.prototype.parse=function(e){return e&&e.objects&&(_.isArray(e.objects)?e.objects[0]:e.objects)||e},t.Collection.prototype.parse=function(e){return e&&e.meta&&(this.meta=e.meta),e&&e.objects},t.Collection.prototype.url=function(e){var t=this.urlRoot||e&&e.length&&e[0].urlRoot;t=t&&n(t);if(e&&e.length){var r=_.map(e,function(e){var t=_.compact(e.id.split("/"));return t[t.length-1]});t+="set/"+r.join(";")+"/"}return t||null};var n=function(e){return e+(e.length>0&&e.charAt(e.length-1)==="/"?"":"/")}})();