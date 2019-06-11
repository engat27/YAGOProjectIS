
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://linkeddata1.calcul.u-psud.fr/sparql")
sparql.setQuery("""
    select  ?X ?P2 ?Z
        where {
            {?X ?P ?Y}
            {?Y ?P2 ?Z}
            {?X ?P2 ?Z}
            FILTER (STRSTARTS(STR(?P2), "http://yago-knowledge.org/resource/"))
        }LIMIT 5""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print(results)