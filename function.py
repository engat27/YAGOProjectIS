from SPARQLWrapper import SPARQLWrapper, JSON
from parse import *
import itertools

def predicate1(parola):
        try:
                l,out = parola.split('->')
                predicates = []
                
                for pred in l.split('|'):
                        predicates+=pred.split('&')
                predicates.append(out)
                output = []
                for i in predicates:
                        output.append(parsePred(i))
        except:
                return []
        return output

def parsePred(pred):
        if (parse("{}({},{})",pred.strip())!=None):
                return list(parse("{}({},{})",pred.strip()))
        else:
                return ['type']+list(parse("{}({})",pred.strip()))

def orderPred(parser):
        predicate=[]
        for i in range(0,len(parser)):
                predicate.append([parser[i][1]] + [parser[i][0]] + [parser[i][2]])
        print(predicate)

        return(predicate)

def getOperator(phrase):
        operators=[]
        for i in range(1,len(phrase)):
                if ((phrase[i] =='&') | (phrase[i]=='|') | (phrase[i]=='-')):
                        operators.append(phrase[i])
        operators.append('')
        return(operators)

def predToQuery(op,pred):
        query=[]
        j=0
        for i in range(0,len(pred)):
                if (op[i] == '|'):
                        query.append('{' + ' ?'+str(pred[i][0]) + ' ?'+str(pred[i][1]) +' ?'+str(pred[i][2]) + '}' + ' UNION ')
                else:
                        query.append('{' + ' ?'+str(pred[i][0]) + ' ?'+str(pred[i][1]) +' ?'+str(pred[i][2]) + '}')
        j=j+1
        select=query[len(query)-1]
        return((str(query).replace(",","").replace("'","").replace("[","").replace("]","")),select)

def mQ1(where,select,limit):

        sparql = SPARQLWrapper(("https://linkeddata1.calcul.u-psud.fr/sparql").replace("\n",""))
        select = select.replace("{","").replace("}","")

        sparql.setQuery(str(
        """select """+ select + """
        where { """+ where + """
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#Thing>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#Class>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#Restriction>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#ObjectProperty>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#DatatypeProperty>}

         FILTER (STRSTARTS(STR(?"""+select[2]+"""), "http://yago-knowledge.org/resource/"))
        }LIMIT """ + str(limit) + """
        """).replace("\n",""))

        print(str(sparql))
        g=sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return(results)

def namesDomainProperties(results):
        parole=str(results).split()
        g=[]
        parser=[]
        for parola in parole:
                if 'http://' in parola:
                        lista = parola.split('#')
                        if(len(lista)==1):
                                lista = parola.split('/')
                        parser.append(lista[len(lista)-1].replace('}','').replace(',','').replace('\'','').replace(']','').replace('"',''))

        predicate=[]
        for i in range(0,len(parser),3):
                predicate.append('yago:'+parser[i])
        return(predicate)

def getNamePredicate(phrase):
        nameP=[]
        for i in range(1,len(phrase)):
                if (phrase[i] =='(' ):
                        nameP.append(phrase[i-1])
        return(nameP)

def equalPredicate(nomi):
        aux = []
        for i in range(0, len(nomi)):
               if not (aux.__contains__(nomi[i])):
                aux.append(nomi[i])
        return aux

def combinations(pred,singlePredicate):
        solution=[]
        lst = list(itertools.combinations(pred, len(singlePredicate)))
        setLst = set(lst)
        lst=list(setLst)
        for i in range(0,len(lst)):
                solution.append(lst[i])
        return solution

def singleQuery(comb, singlePredicate, names):
        diz={}
        newComb=[]
        for i in range(0,len(comb)):
                for j in range(0,len(singlePredicate)):
                        diz[str(singlePredicate[j])] = str(comb[i][j])

                for k in range(0,len(names)):
                        newComb.append(diz[names[k]])                
        return newComb

#----------------------------------------
def predToQuery2(pred,singleQuery,nomi):
        query=[]
        j=0
        for i in range(0,len(pred)):
                query.append('{' + ' ?'+str(pred[i][0]) + " " + str(singleQuery[i])+' ?'+str(pred[i][2]) + '}')
        
        select='?'+pred[len(pred)-1][0]+' ?'+ pred[len(pred)-1][2]
        return((str(query).replace(",","").replace("'","").replace("[","").replace("]","")),select)

def mQ2(solution,limit,where):
        sparql = SPARQLWrapper(("https://linkeddata1.calcul.u-psud.fr/sparql").replace("\n",""))
        select = select.replace("{","").replace("}","")

        sparql.setQuery(str(
        """select """+ select + """
        where { """+ where + """
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#Thing>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#Class>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#Restriction>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#ObjectProperty>}
          MINUS{?"""+select[2]+""" a <http://www.w3.org/2002/07/owl#DatatypeProperty>}

         FILTER (STRSTARTS(STR(?"""+select[2]+"""), "http://yago-knowledge.org/resource/"))
        }LIMIT """ + str(limit) + """
        """).replace("\n",""))

        print(str(sparql))
        g=sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return(results)



