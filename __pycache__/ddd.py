from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF
import rdflib

g=rdflib.Graph()
g.load('https://linkeddata1.calcul.u-psud.fr/sparql')

qres = g.query(
""" SELECT ?prop
WHERE {
{
?prop a rdf:Property.
FILTER(regex(?prop,"http://yago-knowledge.org/resource.","i"))

      } LIMIT 10""")

for row in qres:
    print("%s %s" % row )