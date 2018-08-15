// Set up arbor.js particle system and renderer
var sys = arbor.ParticleSystem(100000, 400,1);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;

// Variables
var test_data = $('#testdata');  // draw/test after this element
var canvas = $('canvas');  // html canvas element

// // Resize canvas to window size
// canvas.width('100%');
// canvas.height('auto');
//
// // Listen for window resizing - resize canvas to window size
// $(window).resize(function(){
//   canvas.width('100%');
//   canvas.height('auto');
// })


// test: open dummy json file with .getJSON and display contents using $.getJSON
$.getJSON('/static/json/crawler_results/results.json?' + new Date().getTime(), function(data){
  var nodes = data.nodes;

  $.each(nodes, function(key, value){
    value.color="silver";
    // value.shape="rectangle"
    value.shape="dot"
    value.label=null;
    // value.label=key
  })

  // FIXME trace: display json file data in page
  // reference: https://api.jquery.com/jquery.getjson/
  test_data.text(JSON.stringify(data));

  // draw the data
  sys.graft({nodes:data.nodes, edges:data.edges});

});
