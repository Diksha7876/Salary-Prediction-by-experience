from tkinter import *
import joblib
import numpy as np

m=joblib.load("Salary Predictor.joblib")

def fun():
    exp=float(e1.get())
    ab=np.array(exp)
    res=ab.reshape(-1,1)
    sal=m.predict(res)[0]
    lblshow.config(text=f"Your salary will be : {str(sal)[:5]} rupees")

a=Tk()
a.title('Salary Predictor')
a.geometry('600x270')
a.config(background='pink')

l1=Label(a,text='Salary Predictor',font=('Robort',26,'bold'),bg='deeppink')
l1.pack(ipady=10,fill='x')

e1=Entry(a,font=('Robort',20))
e1.pack(pady=15)

b=Button(a,text="Predict",font=('Robort',15),bg='hotpink',fg='black',command=fun)
b.pack()

lblshow=Label(a,text="",font=('Robort',19),fg='deeppink',bg='pink')
lblshow.pack(pady=15)

a.mainloop()