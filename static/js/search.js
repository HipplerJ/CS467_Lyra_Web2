// preselect bfs
// https://api.jquery.com/select/


// instantiate message saying bfs has max depth of 3
var depthHelpMessage = $('#depthHelp');
var bfs = $('#method-0');
var dfs = $('#method-1');
var depthInput = $('#depth');


// instantiate hidden message saying dfs has max depth of 100


// set listener on radio button. if it changes:
// https://api.jquery.com/change/
bfs.click(function(){
  // if bfs checked, set max depth to 3 and say that in help text
  depthHelpMessage.text("Max depth for breadth first traversal is 3 steps");
  depthInput.attr("max", 3);
});

  // else set max depth to 100 and set help text

dfs.click(function(){
  depthHelpMessage.text("Max depth for depth first traversal is 100 steps");
  depthInput.attr("max", 100);
});






  // toggle hidden on bfs depth message

  // toggle hidden on dfs depth message
