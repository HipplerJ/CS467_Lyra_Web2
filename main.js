var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000); // FIXME - get portno from user

// Homepage - user input forms
app.get('/',function(req,res){
  res.render('home');
});

// Graphical display page
app.get('/display', function(req,res){
  var context = {};
  context.msg = "get request to graphical display page";
  res.render('display', context);
});

// FIXME User posts input here (currently displays submitted data)
app.post('/post-data', function(req,res){
  var postData = "";
  for (var prop in req.body)
  {
    postData += "<li>" + prop + ": " + req.body[prop] + " </li>";
  }
  res.render('post-data', {list:postData});
});

// TODO progress bar page handler

app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});
