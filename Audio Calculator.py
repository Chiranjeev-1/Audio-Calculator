import speech_recognition as sr
import tkinter as tk
from  tkinter import  *


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate(sentence):
    operators = ['+', 'plus', 'add', 'subtract', '-', 'minus', 'Multiply', 'divide', 'break', 'brake', 'x', '/','X']
    operand1 = 0
    flag = 0
    curr_operator = ""

    value = '0'
    sent_list = sentence.split()
    for each in sent_list:
        if each not in operators:
            value = value + each
        elif each in operators and flag == 0:
            operand1,value = int(value),'0'
            local_result = operand1
            curr_operator = each
            flag = 1
        elif (each in operators and flag == 1) :

            operand2,value = int(value),'0'
            operand1 = local_result
            # print(operand1,operand2,curr_operator)
            local_result = operate(operand1,operand2,curr_operator)
            curr_operator = each





    return local_result


def operate(operand1, operand2, operator):
    print(operand1,operand2,operator)


    if operator in ["+","plus"]:
        final = add(operand1, operand2)
    elif operator in ["x","multiply","X"]:
        final = multiply(operand1, operand2)
    elif operator in ["-","minus"]:
        final = subtract(operand1, operand2)
    elif operator in ["/","divide"]:
        final = divide(operand1, operand2)


    return final


def main():
    rec = sr.Recognizer()
    rec.pause_threshold = 1.5

    try:
        with sr.Microphone() as source:
            print("speak")
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)

            result = rec.recognize_google(audio) + " break"
            print(f"recognized command {result}")
            final_answer = calculate(result )
            recognizedlabel.config(text=f"Recognized command  {result}")
            answerlabel.config(text=f"Calculated answer  {final_answer}")

    except:
        print("exception triggered")
        main()


window = tk.Tk()
title = tk.Label(window, text="Audio Calculator", bg='white', font=("monospace", 38))
window.geometry("800x600")
window.configure(background="white")


button = tk.Button(window, text="speak", command=main, bg="lightblue", fg="white",borderwidth=0,padx=15,pady=15,font=( "Helvetica",20,'bold'),border=0)

recognizedlabel = Label(window,text="",font=("arial",20),padx=20)
answerlabel = Label(window,text="",font=("arial",20),)


title.pack()
recognizedlabel.pack()
answerlabel.pack()
button.pack(pady=window.winfo_reqheight())




window.mainloop()