var sys = arbor.ParticleSystem(1000, 400,1);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;
var node1 = sys.addNode('url-1',{'color':'red','shape':'rectangle','label':'oregonstate.edu'});
var node2 = sys.addNode('url-2',{'color':'green','shape':'rectangle','label':'facebook.com'});
var node3 = sys.addNode('url-3',{'color':'blue','shape':'rectangle','label':'google.com'});
sys.addEdge(node1, node2);
sys.addEdge(node1, node3);
