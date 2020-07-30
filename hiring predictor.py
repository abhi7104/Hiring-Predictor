from tkinter import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm,datasets
import csv
#pa ="E:\\Abhi\\python\\New folder\\PerpData1.csv"
df=pd.read_csv('E:\\Abhi\\python\\New folder\\PerpData1.csv')

win=Tk()
frame1=Frame(win, width=200, height=130)
frame2=Frame(win, width=200, height=130)
frame3=Frame(win, width=400, height=50)

win.title('Hire Predictor')
X=df[['PERCENTAGE','BACKLOG','INTERNSHIP','FIRSTROUND','COMMUNICATIONSKILLLS']]
y=df[['Hired']]
def Logistic():
    global result
    a=var2.get()
    b=var3.get()
    c=var4.get()
    d=var5.get()
    e=var6.get()
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
    model2=LogisticRegression()
    model2.fit(X_train,y_train)
    l=[a,b,c,d,e]
    l=np.array(l)
    l=np.array([l]).reshape(1,-1)
    result=model2.predict(l)
    if result==1:
        result='Hired'
    else:
        result="Not Hired"
    out.delete('1.0',END)
    out.insert(END,result)
    return result
def Decision_Tree():
    global result1
    a=var2.get()
    b=var3.get()
    c=var4.get()
    d=var5.get()
    e=var6.get()
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(X,y)
    l=[a,b,c,d,e]
    l=np.array(l)
    l=np.array([l]).reshape(1,-1)
    result1=clf.predict(l)
    if result1==1:
        result1='Hired'
    else:
        result1="Not Hired"
    out1.delete('1.0',END)
    out1.insert(END,result1)
    return result1
def Random_Forest():
    global result2
    clf2=RandomForestClassifier(n_estimators=10)
    clf2=clf2.fit(X,y)
    a=var2.get()
    b=var3.get()
    c=var4.get()
    d=var5.get()
    e=var6.get()
    l=[a,b,c,d,e]
    l=np.array(l)
    l=np.array([l]).reshape(1,-1)
    result2=clf2.predict(l)
    if result2==1:
        result2='Hired'
    else:
        result2="Not Hired"
    out2.delete('1.0',END)
    out2.insert(END,result2)
    return result2
def SVM():
    global result3
    C=2.0
    svc=svm.SVC(kernel='linear',C=C)
    svc=svc.fit(X,y)
    a=var2.get()
    b=var3.get()
    c=var4.get()
    d=var5.get()
    e=var6.get()
    l=[a,b,c,d,e]
    l=np.array(l)
    l=np.array([l]).reshape(1,-1)
    result3=svc.predict(l)
    if result3==1:
        result3='Hired'
    else:
        result3="Not Hired"
    out3.delete('1.0',END)
    out3.insert(END,result3)
    return result3
def res():
    b1=result
    b2=result1
    b3=result2
    b4=result3
    if b1=='Hired' and b2=='Hired' and b3=='Hired' and b4=='Hired':
        fresult='Hired'
    elif b1=='Hired' and b2=='Hired' and b3=='Hired':
        fresult='Hired'
    elif b1=='Hired' and b2=='Hired' and b4=='Hired':
        fresult='Hired'
    elif b2=='Hired' and b3=='Hired' and b4=='Hired':
        fresult='Hired'
    elif b1=='Hired' and b3=='Hired' and b4=='Hired':
        fresult='Hired'
    else:
        fresult='Not Hired'
    out4.delete('1.0',END)
    out4.insert(END,fresult)
    if fresult=='Hired':
        res=1
    else:
        res=0
    x=var1.get()
    a=var2.get()
    b=var3.get()
    c=var4.get()
    d=var5.get()
    e=var6.get()
    row = [x,a,b,c,d,e,res]
    with open('E:\\Abhi\\python\\New folder\\PerpData1.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    return
# def mess():
#     tkinter.messagebox.showinfo('window Title','Hired')
#     made by abhishek bhardwaj jims student git profile : https://github.com/abhi7104
#     tkinter.messagebox.showinfo('window Title','Not Hired')
#     return
#win.configure(bg='brown')
heading = Label(win, text='Hire Predictor',bg='brown',fg='white',font = ('Aerial' , 25),borderwidth = 10) 


name=Label(frame1, text='Name :',font=20,pady=9)
percentage=Label(frame1,text='Percentage :',font=20,padx=9,pady=9)
backlogs=Label(frame1,text='Backlogs :',font=20,padx=9,pady=9)
internship=Label(frame1,text='Internship :',font=20,padx=9,pady=9)
firstround=Label(frame1,text="Firstround :",font=20,padx=9,pady=9)
communication=Label(frame1,text='Communication :',font=20,padx=9,pady=9)


var1=StringVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()

nam=Entry(frame1,text=var1,bd=3)
per=Entry(frame1,text=var2,bd=3)
backl=Entry(frame1,text=var3,bd=3)
inte=Entry(frame1,text=var4,bd=3)
firs=Entry(frame1,text=var5,bd=3)
comm=Entry(frame1,text=var6,bd=3)

button=Button(frame2,text='Logistic',font=('Courier',11),relief=RAISED,width=13,bd=5,justify=CENTER,command=Logistic)
button1=Button(frame2,text='Decision Tree',font=('Courier',11),relief=RAISED,width=13,bd=5,justify=CENTER,command=Decision_Tree)
button2=Button(frame2,text='Random Forest',font=('Courier',11),relief=RAISED,width=13,bd=5,justify=CENTER,command=Random_Forest)
button3=Button(frame2,text='SVM',font=('Courier',11),relief=RAISED,width=13,bd=5,justify=CENTER,command=SVM)
result=Button(frame3,text='Final Result',font=('Courier',11),bd=5,width=13,command=res)

# algo=Label(frame2, text='algo',font=20,bg='brown',fg='white', borderwidth=2,relief='solid')
# algo1=Label(win,text='algo1',font=20,bg='brown',fg='white', borderwidth=2,relief='solid')
# algo2=Label(win,text='algo2',font=20,bg='brown',fg='white', borderwidth=2,relief='solid')
# algo3=Label(win,text='algo3',font=20,bg='brown',fg='white', borderwidth=2,relief='solid')
# made by abhishek bhardwaj jims student git profile : https://github.com/abhi7104
out=Text(frame2,height=3,width=8,padx=10,bd=3)
out1=Text(frame2,height=3,width=8,bd=3,padx=10)
out2=Text(frame2,height=3,width=8,bd=3,padx=10)
out3=Text(frame2,height=3,width=8,bd=3,padx=10)
out4=Text(frame3,height=3,width=8,bd=3,padx=10)

frame1.grid(row=10,column=3)
frame2.grid(row=10,column=9)
frame3.grid(row=11,column=3)

heading.grid(row=0,column=3)
name.grid(row=2,sticky=E)
percentage.grid(row=7,sticky=E)
backlogs.grid(row=13,sticky=E)
internship.grid(row=18,sticky=E)
firstround.grid(row=23,sticky=E)
communication.grid(row=28,sticky=E)

nam.grid(row=2,column=5)
per.grid(row=7,column=5)
backl.grid(row=13,column=5)
inte.grid(row=18,column=5)
firs.grid(row=23,column=5)
comm.grid(row=28,column=5)

button.grid(row=7,column=3,padx=20, pady=10)
button1.grid(row=13,column=3,padx=10, pady=10)
button2.grid(row=18,column=3,padx=10, pady=10)
button3.grid(row=23,column=3,padx=10, pady=10)


# algo.grid(row=30,column=0)
# algo1.grid(row=30,column=4)
# algo2.grid(row=30,column=8)
# algo3.grid(row=30,column=12)


out.grid(row=7,column=10,padx=10, pady=10)
out1.grid(row=13,column=10,padx=10, pady=10)
out2.grid(row=18,column=10,padx=10, pady=10)
out3.grid(row=23,column=10,padx=10, pady=10)
out4.grid(row=14,column=10,padx=10, pady=10)
result.grid(row=12,column=18)
win.mainloop()