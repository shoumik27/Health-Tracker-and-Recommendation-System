import tkinter
from tkinter import*
from tkinter import messagebox
import webbrowser
t=Tk()
t.title("Health")

def login():
        f2 = Frame(bg="#091e42")
        f2.place(x=0, y=0, width=2000, height=2000)

        u = Label(f2, text="Login Page",bg="#091e42",fg="white",font=("Arial Bold",20))
        u.place(x=800, y=10)

        u1=Label(f2,text="Enter Name",bg="#091e42",fg="white")
        u1.place(x=750,y=80)
        e1=Entry(f2,font=("",12))
        e1.place(x=850,y=80,width=120)

        u2 = Label(f2, text="Enter Password",bg="#091e42",fg="white")
        u2.place(x=750, y=130)
        e2 = Entry(f2, font=("", 12),show='*')
        e2.place(x=850, y=130, width=120)

        b2=Button(f2,text="<==",command=home)
        b2.place(x=2,y=3)
        b3=Button(f2,text="login")
        b3.place(x=870,y=200,width=80,height=40)

def regis():
        f3 = Frame(bg="#091e42")
        f3.place(x=0, y=0, width=2000, height=2000)

        u = Label(f3, text="Register Page",bg="#091e42",fg="white",font=("Arial Bold",20))
        u.place(x=800, y=10)

        u1 = Label(f3, text="Enter Name",bg="#091e42",fg="white")
        u1.place(x=750, y=80)
        e1 = Entry(f3, font=("", 12))
        e1.place(x=850, y=80, width=120)

        u2 = Label(f3, text="Enter Email", bg="#091e42", fg="white")
        u2.place(x=750, y=130)
        e2 = Entry(f3, font=("", 12))
        e2.place(x=850, y=130, width=120)

        u3 = Label(f3, text="Enter C.Email", bg="#091e42", fg="white")
        u3.place(x=750, y=180)
        e3 = Entry(f3, font=("", 12))
        e3.place(x=850, y=180, width=120)

        u4 = Label(f3, text="Enter number", bg="#091e42", fg="white")
        u4.place(x=750, y=230)
        e4 = Entry(f3, font=("", 12))
        e4.place(x=850, y=230, width=120)

        u5 = Label(f3, text="Enter Password",bg="#091e42",fg="white")
        u5.place(x=750, y=280)
        e5 = Entry(f3, font=("", 12), show='*')
        e5.place(x=850, y=280, width=120)

        u6 = Label(f3, text="Enter C.Password",bg="#091e42",fg="white")
        u6.place(x=750, y=330)
        e6 = Entry(f3, font=("", 12), show='*')
        e6.place(x=850, y=330, width=120)

        b2 = Button(f3, text="<==",command=home)
        b2.place(x=2, y=3)
        b3 = Button(f3, text="regis",command=click)
        b3.place(x=870, y=400, width=80, height=40)

def click():

         root1 = tkinter.Tk()
         root1.title("Health")
         root1.geometry("2000x2000")
         root1.configure(bg="green")
         f1 = tkinter.Frame(root1, bg="yellow")
         f1.pack(side=TOP, fill="x")

         l = tkinter.Label(f1, text="HEALTH TRACKER SYSTEM",bg="yellow", font=("Arial Bold", 30))
         l.pack()
         btn = Button(root1, text="BMI", width=20, height=4,command=bmi1)
         btn.place(x=600, y=230)
         btn1 = Button(root1, text="NUTRITION CALCULATOR", width=20, height=4)
         btn1.place(x=800, y=230)
         btn2 = Button(root1, text="PULSE DETECTOR", width=20, height=4)
         btn2.place(x=1000, y=230)
         btn3 = tkinter.Button(root1, text="GENERAL", width=20, height=3,command=click1)
         btn3.place(x=600, y=480)
         btn4 = tkinter.Button(root1, text="EMERGENCY", width=20, height=3,command=click2)
         btn4.place(x=800, y=480)
         btn5 = tkinter.Button(root1, text="MENTAL PROBLEM", width=20, height=3, command=click3)
         btn5.place(x=1000, y=480)
         btn6 = tkinter.Button(root1, text="CORONA UPDATE", width=20, height=3, command=web9)
         btn6.place(x=800, y=650)

def click1():
    root2 = tkinter.Tk()
    root2.title("Health")
    root2.geometry("2000x2000")
    root2.configure(bg="green")
    f4 = tkinter.Frame(root2, bg="yellow")
    f4.pack(side=TOP, fill="x")

    l = tkinter.Label(f4, text="HEALTH TRACKER SYSTEM", bg="yellow", font=("Arial Bold", 30))
    l.pack()
    btn1 = tkinter.Button(root2, text="FEVER", width=25, height=4, command=web)
    btn1.place(x=900, y=280)
    btn2 = tkinter.Button(root2, text="HEADACHE", width=25, height=4, command=web1)
    btn2.place(x=900, y=380)



def click2():
    root3 = tkinter.Tk()
    root3.title("Health")
    root3.geometry("2000x2000")
    root3.configure(bg="green")
    f5 = tkinter.Frame(root3, bg="yellow")
    f5.pack(side=TOP, fill="x")

    l = tkinter.Label(f5, text="HEALTH TRACKER SYSTEM", bg="yellow", font=("Arial Bold", 30))
    l.pack()
    btn1 = tkinter.Button(root3, text="BREATHING PROBLEM", width=25, height=4, command=web2)
    btn1.place(x=900, y=380)
    btn2 = tkinter.Button(root3, text="HEART ATTACK", width=25, height=4, command=web8)
    btn2.place(x=900, y=480)
    btn3 = tkinter.Button(root3, text="ACCIDENT", width=25, height=4, command=web3)
    btn3.place(x=900, y=580)


def click3():
    root4 = tkinter.Tk()
    root4.title("Health")
    root4.geometry("2000x2000")
    root4.configure(bg="green")
    f6 = tkinter.Frame(root4, bg="yellow")
    f6.pack(side=TOP, fill="x")

    l = tkinter.Label(f6, text="HEALTH TRACKER SYSTEM", bg="yellow", font=("Arial Bold", 30))
    l.pack()
    btn1 = tkinter.Button(root4, text="INSOMNIA", width=25, height=4, command=web4)
    btn1.place(x=900, y=320)
    btn2 = tkinter.Button(root4, text="ANXIETY", width=25, height=4, command=web5)
    btn2.place(x=900, y=420)
    btn3 = tkinter.Button(root4, text="DEPRESSION", width=25, height=4, command=web7)
    btn3.place(x=900, y=520)
    btn4 = tkinter.Button(root4, text="SUICIDAL THOUGHTS", width=25, height=4, command=web6)
    btn4.place(x=900, y=620)

def bmi1():
    root = Tk()
    root.title("BMI Calculator")
    root.resizable(False, False)


    def calculate_bmi():
        w = weight.get()
        h = height.get()
        bmi = (w / ((h ** 2) / 1000))
        messagebox.showinfo("Results", "Your BMI is: {bmi}")

    universal_font = ('Arial', 20, 'bold')

    weight = IntVar()
    height = IntVar()

    weight_label = Label(root, text="Weight : ", font="universal_font")
    weight_label.grid(row=0, column=0)
    height_label = Label(root, text="Height : ", font="universal_font")
    height_label.grid(row=1, column=0)

    weight_entry = Entry(root, textvariable=weight, width=40, bd=6, font="universal_font")
    weight_entry.grid(row=0, column=1)
    height_entry = Entry(root, textvariable=height, width=40, bd=6, font="universal_font")
    height_entry.grid(row=1, column=1)

    btn_calculate = Button(root, width=40, text="Calculate", font="universal_font", bd=6, command=calculate_bmi)
    btn_calculate.grid(row=2, columnspan=3)


def web():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&sxsrf=ALeKk01r49dliT9DRfAl2TJdfkq1Xq0qxQ%3A1604424561530&ei=cZOhX7WEIIyQ4-EPkpmumAg&q=what+to+do+when+you+get+fever&oq=what+to+do+when+you+get+fever&gs_lcp=CgZwc3ktYWIQDFAAWABgg5kDaABwAXgAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwj1gLyg8-bsAhUMyDgGHZKMC4MQ4dUDCA0")
def web1():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&sxsrf=ALeKk0153uAPoJzmiI5te6QmYHdVR49k7w%3A1604424686691&ei=7pOhX5jZKZec4-EPhJqO-Ag&q=what+to+do+when+you+get+headache&oq=what+to+do+when+you+get+headache&gs_lcp=CgZwc3ktYWIQAzIFCAAQyQMyAggAMgIIADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgQIABBHOgcIIxDJAxAnOgoIABDJAxAUEIcCUP8EWOAaYPkgaABwAngAgAHyA4gBgRSSAQowLjEwLjIuMC4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwiYiJPc8-bsAhUXzjgGHQSNA48Q4dUDCA0&uact=5")
def web2():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&sxsrf=ALeKk02D8OKjl2rC8X4CYe7fufTHFubV7A:1604424735536&q=hospital+for+breathing+problems&spell=1&sa=X&ved=2ahUKEwjTq7jz8-bsAhXpxjgGHUdfCsUQBSgAegQIFRAq&biw=1920&bih=937")
def web3():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&biw=1920&bih=937&sxsrf=ALeKk01BXwSp-mLASdj5B5r3wjrXU3oNhA%3A1604424737410&ei=IZShX-HLGKac4-EPsqG0iAU&q=hospital+for+accident&oq=hospital+for+accident&gs_lcp=CgZwc3ktYWIQAzIFCAAQyQMyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BAgAEEc6BAgjECc6AggAOggILhDHARCvAVCPtgFYrsMBYN3HAWgAcAJ4AIABmQKIAc0MkgEFMC44LjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwih4Kr08-bsAhUmzjgGHbIQDVEQ4dUDCA0&uact=5")
def web4():
    webbrowser.open("https://www.google.com/search?q=what+to+do+when+you+get+insomnia&rlz=1C1CHBF_enIN913IN913&oq=WHAT+TO+DO+WHEN+YOU+GET+INSOMNIA&aqs=chrome.0.0i457j0i22i30l7.7904j0j7&sourceid=chrome&ie=UTF-8")
def web5():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&sxsrf=ALeKk02kHITrxhO5hsSA7R8os-qAyie3JQ:1604577205579&q=what+to+do+when+you+get+ANXIETY&spell=1&sa=X&ved=2ahUKEwjYq-nyq-vsAhWzxTgGHVgAD-4QBSgAegQICxAq&biw=1920&bih=937")
def web6():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&biw=1920&bih=937&sxsrf=ALeKk01iINJM3ZxfRWi-jPBk5vr9xTxWAQ%3A1604577260435&ei=7OejX66LGpqR4-EP4Ji1wAY&q=WHOM+OT+CONSULT+FOR+SUCIDIAL+THOUGHTS&oq=WHOM+OT+CONSULT+FOR+SUCIDIAL+THOUGHTS&gs_lcp=CgZwc3ktYWIQAzIHCCEQChCgAToHCCMQ6gIQJzoECCMQJzoICAAQyQMQkQI6BQgAEJECOgUIABCxAzoCCAA6BwgAEMkDEEM6BAgAEEM6CAgAELEDEIMBOgUIABDJAzoECAAQCjoHCAAQyQMQCjoHCAAQyQMQDToECAAQDToECC4QDToICAAQFhAKEB46CAgAEA0QBRAeOg0IABDJAxANEAUQChAeOgoIABANEAUQChAeOgoIABAIEA0QChAeOgkIABDJAxAWEB46BggAEBYQHjoECCEQFToGCCEQChAVUNkgWIjeAWCX3gFoAnABeACAAYACiAGxNpIBBjAuMjguOZgBAKABAaoBB2d3cy13aXqwAQrAAQE&sclient=psy-ab&ved=0ahUKEwiusf2MrOvsAhWayDgGHWBMDWgQ4dUDCA0&uact=5")
def web7():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&biw=1920&bih=937&sxsrf=ALeKk01xVoO525lULLw4UVID5mwHcs-YAw%3A1604577289848&ei=CeijX9qmM77H4-EP1NeT6A4&q=therapist+for+depression&oq=THERAPIST+FOR+&gs_lcp=CgZwc3ktYWIQAxgAMgUIABCRAjIFCAAQkQIyBwgAEBQQhwIyBQgAEMkDMgIIADICCAAyCAguEMcBEK8BMgIIADICCAAyAggAOgcIIxDqAhAnOgQIIxAnOggIABDJAxCRAjoFCAAQsQM6BQguELEDOgsILhCxAxDHARCjAjoICAAQsQMQgwE6BAgAEEM6BAguEEM6BwgAELEDEEM6CggAELEDEIMBEEM6BwgAEMkDEEM6AgguOggIABCxAxCRAjoICAAQsQMQyQNQ_sgCWJ6LA2DwnQNoBXAAeACAAY8CiAHoGZIBBjAuMTYuMpgBAKABAaoBB2d3cy13aXqwAQrAAQE&sclient=psy-ab")
def web8():
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN913IN913&sxsrf=ALeKk00MPtMJ1Kt0YpkmN56_eB0-L8sT7Q%3A1604594551108&ei=dyukX5WMBoaP4-EPrO280Aw&q=hospitals+for+heart+attack+in+india&oq=hospitals+for+heart+attack+in+india&gs_lcp=CgZwc3ktYWIQDFAAWABg-vUCaABwAXgAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjVo-jB7OvsAhWGxzgGHaw2D8oQ4dUDCA0")
def web9():
    webbrowser.open("https://www.worldometers.info/coronavirus/")

def home():
    t.geometry("2000x2000")
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=2000,height=2000)
    b1=Button(f1,text="login",command=login)
    b1.place(x=850,y=350,width=80,height=40)
    b2 = Button(f1, text="regis", command=regis)
    b2.place(x=950,y=350,width=80,height=40)
    t.mainloop()
home()