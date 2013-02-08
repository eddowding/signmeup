L.TileLayer.OS=L.TileLayer.WMS.extend({defaultWmsParams:{SERVICE:"WMTS",REQUEST:"GetMap",VERSION:"1.1.1",FORMAT:"image/png"},defOptions:{maxZoom:13,minZoom:1,continuousWorld:!0,tms:!0,attribution:" & OS.Openspace"},resolutions:[2500,1e3,500,200,100,50,25,10,5,4,2.5,2,1],_url:"http://openspace.ordnancesurvey.co.uk/osmapapi/ts",initialize:function(e,t){this.options.tileSize=t.tileSize;var n=L.Util.extend({},this.defaultWmsParams),r={KEY:e};n=L.Util.extend(n,r);for(var i in t)this.options.hasOwnProperty(i)||(n[i]=t[i]);this.wmsParams=n,L.Util.setOptions(this,this.defOptions)},setOsTileSize:function(e){this.options.tileSize=e},getCurrentLayerTileSize:function(){var e=this._map.getZoom(),t=resolutions[z-1],n=t<5&&t!==2.5?250:200;return n},getTileUrl:function(e){var t=this._map,n=t.options.crs,r=t.getZoom(),i=this.resolutions[r-1],s=this.options.tileSize,o=e.multiplyBy(s),u=o.add(new L.Point(s,s)),a=n.project(t.unproject(o,r)),f=n.project(t.unproject(u,r)),l=[a.x,f.y,f.x,a.y].join(","),c=L.Util.template(this._url,{});return c+L.Util.getParamString(this.wmsParams)+"&BBOX="+l+"&WIDTH="+s+"&HEIGHT="+s+"&LAYERS="+i}}),L.tileLayer.os=function(e,t){return new L.TileLayer.OS(e,t)};