from SPARQLWrapper import SPARQLWrapper, JSON
from parse import *
from function import *

#'P(X,Y) | P(Y,Z) | P(Y,Z) -> P(X,Z)'
input_strig=input("Inserisci la stringa: ")   
ris=predicate1(input_strig)
pre=orderPred(ris)
op=getOperator(input_strig)

where,select=predToQuery(op,pre)
print('WHERE: ' + where)
print('SELECT: ' + select, '\n')

results=mQ1(where,select,9)
print('MQ1: \n' + str(results), '\n')

lista=namesDomainProperties(results)
print('Possibili istanze di proprietà: \n'+ str(lista))

nomi=getNamePredicate(input_strig)
print('Tutti i predicati: (nomi): '+ str(nomi))

l=equalPredicate(nomi)
print('Predicati senza ripetizioni: (l): ' + str(l))

comb=combinations(lista,equalPredicate(nomi))
print('********************\n')
print(singleQuery(comb, l, nomi))
print(str(pre[0][0]) + str(pre[0][1]))

singleQuery=singleQuery(comb, l, nomi)
print(predToQuery2(pre,singleQuery,nomi))

"""
[['P', 'X', 'Y'], ['P', 'Y', 'Z'], ['P', 'X', 'Z']]
P(X,Y) & P(Y,Z) -> P(X,Z)
P(X,Y) & Q(Y,Z) -> Q(X,Z)
P(X,Y) & Q(Y,Z) & E(Y,Z) -> Q(X,Z)

P(X,Y) & Q(Y) -> Q(X,Z)
{?subject ?properties ?object}
{?object  ?properties2 ?object2}
{?subject ?properties ?object2}

0) tutta la lettura del file
1) come capire se è unaira, binaria
2) per ogni P, fare una riga, che capirà se è unaria o binaria
3) capire come cazzo fare gli and e or complessi
4) aprire una parentesi all'inizio e chiuderna una poco prima dell'implica, per poi farlo in and
"""