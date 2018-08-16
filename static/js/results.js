// Set up arbor.js particle system and renderer
// var sys = arbor.ParticleSystem(1000, 400,1);
var sys = arbor.ParticleSystem();
sys.parameters({stiffness:900, repulsion:2000, gravity:true, dt:0.015});
// sys.parameters({stiffness:400, repulsion:100000, gravity:true, dt:0.015});
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

    // print these so we can find the empty node
    // console.log("Node url: " + value.url)
  })

  // FIXME trace: display json file data in page
  // reference: https://api.jquery.com/jquery.getjson/
  test_data.text(JSON.stringify(data));

  // draw the data
  sys.graft({nodes:data.nodes, edges:data.edges});

});
