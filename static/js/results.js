// Set up arbor.js particle system and renderer
var sys = arbor.ParticleSystem(1000, 400,1);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;

// Variables
var test_data = $('#testdata');  // draw/test after this element
var canvas = $('canvas');  // html canvas element

// Resize canvas to window size
canvas.width('100%');
canvas.height('auto');

// Listen for window resizing - resize canvas to window size
$(window).resize(function(){
  canvas.width('100%');
  canvas.height('auto');
})


// test: open dummy json file with .getJSON and display contents using $.getJSON
$.getJSON('/static/json/crawler_results/results.json?' + new Date().getTime(), function(data){

  var nodes = data.nodes

  // add label to each node - same as name (key)
  // $.each(nodes, function(key, value){
  //   value.label=key
  // })
  $.each(nodes, function(key, value){
    // value.color="red"
    // value.shape="rectangle"
    value.shape=null
    value.label=key
  })

  // FIXME trace: display json file data in page
  // reference: https://api.jquery.com/jquery.getjson/
  test_data.text(JSON.stringify(data));

  // draw the data
  sys.graft({nodes:data.nodes, edges:data.edges});

});



// TODO Listen for node to be hovered over, and display url/label when it's
// adapted from html of arbor.js homepage arborjs.org
// $(canvas).click(function(e){
//   var pos = $(this).offset();
//   var p = {x:e.pageX-pos.left, y:e.pageY-pos.top}
//   selected = nearest = particleSystem.nearest(p);
//
//   if (selected.node !== null){
//     selected.node.color = blue;
//   }
// })


// TODO Listen for nodes to be clicked, and open that page if it is clicked
