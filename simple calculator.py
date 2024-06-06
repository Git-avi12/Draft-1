#modules used
import tkinter as tk

#variables used
calculation=''

# to create a string which contains all operations
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation)

#to remove last added character from the string calculation
def remove_from_calculation():
    global calculation
    calculation=calculation[0:-1]
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation)

#to evaluate the calculation
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,'ERROR')

#to clear the text box
def clear_field():
    global calculation
    calculation =''
    text_result.delete(1.0,'end')
    
#creating gui window 
window=tk.Tk()
window.geometry('330x360')
window.title('quick GUI calculator')
window.configure(bg='white')

text_result=tk.Text(window,height=2,width=18,font=('Arial',24))
#1 column for text box,2,3,4,5 for buttons
text_result.grid(columnspan=5)

button1=tk.Button(window,text='1',command=lambda:add_to_calculation(1),width=5,font=('arial',18))
button1.grid(row=2,column=1)

button2=tk.Button(window,text='2',command=lambda:add_to_calculation(2),width=5,font=('arial',18))
button2.grid(row=2,column=2)

button3=tk.Button(window,text='3',command=lambda:add_to_calculation(3),width=5,font=('arial',18))
button3.grid(row=2,column=3)

button4=tk.Button(window,text='4',command=lambda:add_to_calculation(4),width=5,font=('arial',18))
button4.grid(row=3,column=1)

button5=tk.Button(window,text='5',command=lambda:add_to_calculation(5),width=5,font=('arial',18))
button5.grid(row=3,column=2)

button6=tk.Button(window,text='6',command=lambda:add_to_calculation(6),width=5,font=('arial',18))
button6.grid(row=3,column=3)

button7=tk.Button(window,text='7',command=lambda:add_to_calculation(7),width=5,font=('arial',18))
button7.grid(row=4,column=1)

button8=tk.Button(window,text='8',command=lambda:add_to_calculation(8),width=5,font=('arial',18))
button8.grid(row=4,column=2)

button9=tk.Button(window,text='9',command=lambda:add_to_calculation(9),width=5,font=('arial',18))
button9.grid(row=4,column=3)

button0=tk.Button(window,text='0',command=lambda:add_to_calculation(0),width=5,font=('arial',18))
button0.grid(row=5,column=1)

button1=tk.Button(window,text='1',command=lambda:add_to_calculation(1),width=5,font=('arial',18))
button1.grid(row=2,column=1)

button2=tk.Button(window,text='2',command=lambda:add_to_calculation(2),width=5,font=('arial',18))
button2.grid(row=2,column=2)

button3=tk.Button(window,text='3',command=lambda:add_to_calculation(3),width=5,font=('arial',18))
button3.grid(row=2,column=3)

button4=tk.Button(window,text='4',command=lambda:add_to_calculation(4),width=5,font=('arial',18))
button4.grid(row=3,column=1)

button5=tk.Button(window,text='5',command=lambda:add_to_calculation(5),width=5,font=('arial',18))
button5.grid(row=3,column=2)

button6=tk.Button(window,text='6',command=lambda:add_to_calculation(6),width=5,font=('arial',18))
button6.grid(row=3,column=3)

button7=tk.Button(window,text='7',command=lambda:add_to_calculation(7),width=5,font=('arial',18))
button7.grid(row=4,column=1)

button8=tk.Button(window,text='8',command=lambda:add_to_calculation(8),width=5,font=('arial',18))
button8.grid(row=4,column=2)

button9=tk.Button(window,text='9',command=lambda:add_to_calculation(9),width=5,font=('arial',18))
button9.grid(row=4,column=3)

button0=tk.Button(window,text='0',command=lambda:add_to_calculation(0),width=5,font=('arial',18))
button0.grid(row=5,column=1)

button_open=tk.Button(window,text='(',command=lambda:add_to_calculation('('),width=5,font=('arial',18))
button_open.grid(row=5,column=2)

button_close=tk.Button(window,text=')',command=lambda:add_to_calculation(')'),width=5,font=('arial',18))
button_close.grid(row=5,column=3)

button_plus=tk.Button(window,text='+',command=lambda:add_to_calculation('+'),width=5,font=('arial',18))
button_plus.grid(row=2,column=4)

button_minus=tk.Button(window,text='-',command=lambda:add_to_calculation('-'),width=5,font=('arial',18))
button_minus.grid(row=3,column=4)

button_multiply=tk.Button(window,text='*',command=lambda:add_to_calculation('*'),width=5,font=('arial',18))
button_multiply.grid(row=4,column=4)

button_divide=tk.Button(window,text='/',command=lambda:add_to_calculation('/'),width=5,font=('arial',18))
button_divide.grid(row=5,column=4)

button_equal=tk.Button(window,text='=',command=lambda:evaluate_calculation(),width=23,font=('arial',18))
button_equal.grid(row=7,column=1,columnspan=4)

button_clear=tk.Button(window,text='C',command=lambda:clear_field(),width=11,font=('arial',18))
button_clear.grid(row=6,column=1,columnspan=2)

button_del=tk.Button(window,text='DEL',command=lambda:remove_from_calculation(),width=11,font=('arial',18))
button_del.grid(row=6,column=3,columnspan=2)