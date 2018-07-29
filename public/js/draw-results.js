// set up arbor.js particle system and renderer
var sys = arbor.ParticleSystem(1000, 400,1);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;

// draw/test after this element
var test_data = $('#testdata');

// FIXME test: open dummy json file with .getJSON and display contents using $.getJSON
$.getJSON('json/test-data.json', function(data){

  // log to console
  console.log(data); //WORKS

  // print out json file data
  // reference: https://api.jquery.com/jquery.getjson/
  var items = [];
  $.each( data, function( key, val ) {
    items.push( "<li id='" + JSON.stringify(key) + "'>" + JSON.stringify(val) + "</li>" );
  });

  $( "<ul/>", {
    "class": "my-new-list",
    html: items.join( "" )
  }).appendTo( test_data );

});

// FIXME first example - draw 3 node graph using arbor.js
var node1 = sys.addNode('url-1',{'color':'red','shape':'rectangle','label':'oregonstate.edu'});
var node2 = sys.addNode('url-2',{'color':'green','shape':'rectangle','label':'facebook.com'});
var node3 = sys.addNode('url-3',{'color':'blue','shape':'rectangle','label':'google.com'});
sys.addEdge(node1, node2);
sys.addEdge(node1, node3);

// resize canvas to window size
var canvas = $('canvas');
canvas.width('100%');
canvas.height('auto');


// window resize listener - resize canvas to window size
$(window).resize(function(){
  canvas.width('100%');
  canvas.height('auto');
})

// particleSystem.screenSize(w,h);
