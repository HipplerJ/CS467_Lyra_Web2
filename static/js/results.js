// set up arbor.js particle system and renderer
var sys = arbor.ParticleSystem(1000, 400,1);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;

// variables
var test_data = $('#testdata');  // draw/test after this element
var canvas = $('canvas');  // html canvas element

// resize canvas to window size
canvas.width('100%');
canvas.height('auto');

// window resize listener - resize canvas to window size
$(window).resize(function(){
  canvas.width('100%');
  canvas.height('auto');
})

// test: open dummy json file with .getJSON and display contents using $.getJSON
$.getJSON('/static/json/test-data.json', function(data){

  var nodes = data.nodes

  // add label to each node - same as name (key)
  $.each(nodes, function(key, value){
    value.label=key
  })

  // FIXME trace: display json file data in page
  // reference: https://api.jquery.com/jquery.getjson/
  test_data.text(JSON.stringify(data));

  // draw the data
  sys.graft({nodes:data.nodes, edges:data.edges});

});
