import tkinter as tk 
import requests
from function import *
"""pyinstaller --onefile setup.py"""

window=tk.Tk()
window.geometry("500x745") 
window.title("Meta-queries with RDF graphs!")
window.grid_columnconfigure(0, weight=1)
window.resizable(False,False)
window.configure(background="white")

def showsPredicates():
   if text_input.get() :
      try:
         user_input=text_input.get()
         user_num = num_input.get()
         ris=predicate1(str(user_input))

         if ris != []:
            pre=orderPred(ris)
            op=getOperator(str(user_input))
            where,select=predToQuery(op,pre)
            results=run(where,select,int(user_num))
            p=outProperty(results)
            print(p)
            text_response=p

         else: 
            text_response="You must insert the string as in the following example Ex: P(X,Y) & Q(Y,Z) -> Q(X,Z) and 5"
      except :
         text_response = ""
   else:
      text_response="Insert property and LIMIT number: \nFIRST BOX: P(X,Y) & Q(Y,Z) -> Q(X,Z) \nSECOND BOX LIMIT: 5"
   
   textwidget = tk.Text()
   textwidget.insert(tk.END, text_response)
   textwidget.grid(row=6, column=0, sticky="WE", padx=10, pady=10)

   credits_label = tk.Label(window, text="Francesca A. Lisi, Giacomo Abbattista, Vincenzo Gattulli \n Dipartimento di Informatica & Università degli studi di Bari “Aldo Moro”, Italy", font=("Times", 11), background="white")
   credits_label.grid(row=7, column=0, sticky="S", pady=10)

welcome_label= tk.Label(window, text="Welcome! Use of metaqueries in YAGO \n\n Insert the PROPERTY and LIMIT number ", font=("Times", 15), fg="black", background="white") 
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10) 

welcome_label= tk.Label(window, text="Property", font=("Times", 10), fg="black", background="white") 
welcome_label.grid(row=1, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry()
text_input.grid(row=2, column=0, padx=10, sticky="WE")

welcome_label= tk.Label(window, text="Limit", font=("Times", 10), fg="black", background="white") 
welcome_label.grid(row=3, column=0, sticky="N", padx=20, pady=10)

num_input = tk.Entry()
num_input.grid(row=4, column=0, padx=10, sticky="WE")

download_button= tk.Button(text="RUN", command=showsPredicates , font=("Times", 20), fg="white", background="black")
download_button.grid(row=5, column=0, sticky="WE", padx=10, pady=10)

if __name__== "__main__":
   window.mainloop()


"""
import tkinter as tk 
import requests
from function import *
pyinstaller --onefile <your_script_name>.py

window=tk.Tk()
window.geometry("500x670") 
window.title("Meta-queries with RDF graphs!")
window.grid_columnconfigure(0, weight=1)
window.resizable(False,False)
window.configure(background="white")

def showsPredicates():
   if text_input.get() :
      try:
         user_input=text_input.get()
         user_num = num_input.get()
         ris=predicate1(str(user_input))

         if ris != []:
            pre=orderPred(ris)
            op=getOperator(str(user_input))
            where,select=predToQuery(op,pre)
            results=run(where,select,int(user_num))
            p=outProperty(results)
            print(p)
            text_response=p

         else: 
            text_response="You must insert the string as in the following example Ex: P(X,Y) & Q(Y,Z) -> Q(X,Z) and 5"
      except :
         text_response = ""
   else:
      text_response="Insert property and LIMIT number: \nFIRST BOX: P(X,Y) & Q(Y,Z) -> Q(X,Z) \nSECOND BOX: LIMIT=5"
   
   textwidget = tk.Text()
   textwidget.insert(tk.END, text_response)
   textwidget.grid(row=4, column=0, sticky="WE", padx=10, pady=10)

   credits_label = tk.Label(window, text="Francesca A. Lisi, Giacomo Abbattista, Vincenzo Gattulli \n Dipartimento di Informatica & Università degli studi di Bari “Aldo Moro”, Italy", font=("Times", 11), background="white")
   credits_label.grid(row=5, column=0, sticky="S", pady=10)

welcome_label= tk.Label(window, text="Welcome! Use of metaqueries in YAGO \n\n Insert the PROPERTY and LIMIT number ", font=("Times", 15), fg="black", background="white") 
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10) 

text_input = tk.Entry()
text_input.grid(row=1, column=0, padx=10, sticky="WE")

num_input = tk.Entry()
num_input.grid(row=2, column=0, padx=10, sticky="WE")

download_button= tk.Button(text="RUN", command=showsPredicates , font=("Times", 20), fg="white", background="black")
download_button.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

if __name__== "__main__":
   window.mainloop()
"""