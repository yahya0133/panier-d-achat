import numpy as np
from numpy.random import shuffle
import socket
import time
from tkinter import *
from time import *
class Interface(Frame):
    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.agiven=["A :  print('Hello World')",
        "C :  #This is a comment",
        "A :  my-var",
        "D :  Both the other answers are correct",
        "B :  .py",
        "C :  Both the other answers are correct",
        "A :  print(type(x))",
        "C :  def myFunction():",
        "A :  True",
        "A :  x = 'Hello'[0]",
        "D : strip()",
        "C : upper()",
        "C : replace()",
        "C : *",
        "A : == ",
        "A : ['apple', 'banana', 'cherry']",
        "A : ('apple', 'banana', 'cherry')",
        "A : {'apple', 'banana', 'cherry'}",
        "A : {'name': 'apple', 'color': 'green'}",
        "B :  LIST ",
        "C : SET  ",
        "C : if x > y:",
        "A : while x > y:",
        "B : for x in y:",
        "D : break"]
        self.question = ["",
             "What is a correct syntax to output 'Hello World' in Python?",
             "How do you insert COMMENTS in Python code?",
             "Which one is NOT a legal variable name?",
             "How do you create a variable with the numeric value 5?",
             "What is the correct file extension for Python files?",
             "How do you create a variable with the floating number 2.8 ?",
             "What is the correct syntax to output the type of a variable or object in Python?",
             "What is the correct way to create a function in Python?",
             "In Python, 'Hello', is the same as 'Hello'?",
             "What is a correct syntax to return the first character in a string?",
             "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
             "Which method can be used to return a string in upper case letters?",
             "Which method can be used to replace parts of a string?",
             "Which operator is used to multiply numbers?",
             "Which operator can be used to compare two values?",
             "Which of these collections defines a LIST?",
             "Which of these collections defines a TUPLE?",
             "Which of these collections defines a SET?",
             "Which of these collections defines a DICTIONARY?",
             "Which collection is ordered, changeable, and allows duplicate members?",
             "Which collection does not allow duplicate members?",
             "How do you start writing an if statement in Python?",
             "How do you start writing a while loop in Python?",
             "How do you start writing a for loop in Python?",
             "Which statement is used to stop a loop?",]
        self.answer = [[],
                       ["A :  print('Hello World')","B :  echo 'Hello World'","C :  p('Hello World')","D :  echo('Hello World');"],
                       ["A :  /*This is a comment*/","B :  //This is a comment","C :  #This is a comment","D :  This is a comment"],
                       ["A :  my-var","B :  _myvar","C :  my_var","D :  Myvar"],
                       ["A :  x = int(5)","B :  x = 5","C :  x=flot(5)","D :  Both the other answers are correct"],
                       ["A :  pyth","B :  .py","C :  .pyt","D :  .pt"],
                       ["A :  x = 2.8","B :  x = float(2.8)","C :  Both the other answers are correct","D :  x=int(2.8)"],
                       ["A :  print(type(x))","B :  print(typeof(x))","C :  print(typeOf(x))","D :  print(typeof x)"],
                       ["A :  create myFunction():","B :  function myfunction(): ","C :  def myFunction():","D :  myFunction()"],
                       ["A :  True","B = False","C :No    "," Yes    "],
                       ["A :  x = 'Hello'[0]","B :  x = sub('Hello', 0, 1)","C :  x = 'Hello'.sub(0, 1)","D :  ('Hello', 0, 1)"],
                       ["A : ptrim()","B :  trim()","C : len()","D : strip()"],
                       ["A : upperCase()","B : toUpperCase()","C : upper()","D : uppercase()"],
                       ["A : repl()","B : switch()","C : replace()","D : replaceString()"],
                       ["A : %","B : #","C : *","D : x"],
                       ["A : == ","B : = ","C : <>","D : ><"],
                       ["A : ['apple', 'banana', 'cherry']","B : ('apple', 'banana', 'cherry')","C :  {'name': 'apple', 'color': 'green'}","D :  {'apple', 'banana', 'cherry'}"],
                       ["A : ('apple', 'banana', 'cherry')","B : ['apple', 'banana', 'cherry']","C : {'name': 'apple', 'color': 'green'}","D : {'apple', 'banana', 'cherry'}"],
                       ["A : {'apple', 'banana', 'cherry'}","B : {'name': 'apple', 'color': 'green'}","C : ['apple', 'banana', 'cherry']","D : ('apple', 'banana', 'cherry')"],
                       ["A : {'name': 'apple', 'color': 'green'}","B :  ['apple', 'banana', 'cherry']","C : ('apple', 'banana', 'cherry')","D : {'apple', 'banana', 'cherry'}"],
                       ["A : TUPLE","B :  LIST","C :  DICTIONARY","D : SET"],
                       ["A : LIST","B :TUPLE","C : SET","D : DICTIONARY "],
                       ["A :if (x > y)","B : if x > y then:","C : if x > y:","D : if a<=>y"],
                       ["A : while x > y:","B : x > y while {","C :  while (x > y)","D :  while x > y {"],
                       ["A : for x > y:","B : for x in y:","C : for each x in y:","D : for x in range :"],
                       ["A : stop","B : exit","C : return","D : break"]
                       ]
        self.question_done=[0]*(len(self.question))
        self.score=0
        self.message = Label(self, text="Welcome To The Python Quiz Game",
                             bg="white",
                             fg="red",
                             font=('Helvetica',12,'bold'),
                             width=90,
                             height=4)
        self.message.pack(side="top")
        self.bouton_quitter = Button(self,
                                     text="Exit",
                                     font=('Helvetica',12,'bold'),
                                     width=50,
                                     height=3,
                                     bg="red",
                                     fg="black",
                                     command=self.quit)  
        self.bouton_quitter.pack(side="bottom")
        self.bouton_start = Button(self,
                                   text="Start",
                                   font=('Helvetica',12,'bold'),
                                   width=50,
                                   height=3,
                                   bg="green",
                                   fg="black",
                                   command=self.startQestion)
        self.bouton_start.pack()
        self.totalnb = 25
        self.questions_asked =1
    def startQestion(self):
        self.nbqu= Label(self, text="Welcome To The Python Quiz Game",
                             bg="white",
                             fg="black",
                             font=('Helvetica',12,'bold'),
                             width=90,
                             height=3)
        self.nbqu.pack(side="top")
        self.bouton_a1 = Button(self,
                                text="   ",
                                width=100,
                                height=3,
                                font=('Helvetica',11,'bold'),
                                bg="light blue",
                                fg="black",
                                command = self.checkAnswer)
        self.bouton_a1.pack(side="top")
        self.bouton_a2 = Button(self,
                                text="   ",
                                width=100,
                                height=3,
                                font=('Helvetica',11,'bold'),
                                bg="light blue",
                                fg="black",
                                command = self.checkAnswer)
        self.bouton_a2.pack(side="top")
        self.bouton_a3 = Button(self,
                                text="   ",
                                width=100,
                                height=3,
                                font=('Helvetica',11,'bold'),
                                bg="light blue",
                                fg="black",
                                command = self.checkAnswer)
        self.bouton_a3.pack(side="top")
        self.bouton_a4 = Button(self,
                                text="   ",
                                width=100,
                                height=3,
                                font=('Helvetica',11,'bold'),
                                bg="light blue",
                                fg="black",
                                command = self.checkAnswer)
        self.bouton_a4.pack(side="top")
        self.scoret= Label(self, text="Welcome To The Python Quiz Game",
                             bg="white",
                             fg="black",
                             font=('Helvetica',12,'bold'),
                             width=90,
                             height=3)
        self.scoret.pack(side="bottom")
        self.bouton_start.pack_forget()
        self.nextQuestion()
    def nextQuestion(self):
        self.nb = self.chooseQuestion(self.question)
        self.nbqu["text"]=("The Question Number : {}".format(self.nb) +" Of 25")
        self.message["text"] = self.question[self.nb]
        self.ans=self.displayA(self.question,self.answer,self.nb)
        self.play()
    def play(self):
            self.bouton_a1["text"]=self.ans[0]
            self.bouton_a1["command"]=(lambda: self.checkAnswer(self.answer,self.ans[0],self.nb,self.score))
            self.bouton_a2["text"]=self.ans[1]
            self.bouton_a2["command"]=(lambda: self.checkAnswer(self.answer,self.ans[1],self.nb,self.score))
            self.bouton_a3["text"]=self.ans[2]
            self.bouton_a3["command"]=(lambda: self.checkAnswer(self.answer,self.ans[2],self.nb,self.score))
            self.bouton_a4["text"]=self.ans[3]
            self.bouton_a4["command"]=(lambda: self.checkAnswer(self.answer,self.ans[3],self.nb,self.score))
    def chooseQuestion(self,question):
        k=0
        k = +1
        if (self.question_done[k]!=0):
            while(self.question_done[k]!=0):
                k = k+1
            self.question_done[k]=1
        else :
            self.question_done[k]=1
        return k
    def displayA(self,question,answer,i):
        a = answer[i]
        order = np.arange(4)
        shuffle(order)
        a_display = [a[order[0]],a[order[1]],a[order[2]],a[order[3]]]
        return a_display
    def checkAnswer(self,answer,avn,qn,score):
        test = False
        if avn in self.agiven :
                test = True
                self.score=score+100
        else :
            test = False
            self.score=score-50


        self.scoret["text"]=("The Answer Is {}".format(test))
        if self.questions_asked < self.totalnb:
            self.nextQuestion()
            self.questions_asked += 1
        else:
            self.message["text"] = "End of Qestion"
            self.nbqu["text"]=("Good Job")
            self.bouton_a1.pack_forget()
            self.bouton_a2.pack_forget()
            self.bouton_a3.pack_forget()
            self.bouton_a4.pack_forget()
    def quit(self):
        self.nbqu["text"]=("CHECK ...")
        self.scoret["text"] = ("The Score Is  {}".format(self.score))+"  Of  2500  ."
window = Tk()
window.title("Welcom To The Python Quiz Game")
window = Interface(window)
window.mainloop()