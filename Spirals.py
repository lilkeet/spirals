import tkinter as tk
import turtle
import time
import random

#Constants
BG_COLOR = "black"
PENSIZE = 0
COLORS = ["black", "red", "blue", "gold", "green", "orange", "silver", "white", "pink", "purple", "cyan"]

def draw():
    t.up()
    t.goto(65,-100)
    t.clear()
    t.setheading(random.randint(0, 360))
    
    variables = {
        "length":end,
        "sides":sides_,
        "pensize":pensize_,
        "r":increment
        }
    values = {
        "length":5,
        "sides":5}
    
    #If a variable is a noninteger, replace it with a random integer
    for var, entry in variables.items():
        try:
            globals()[var] = int(entry.get())
        except ValueError:
            globals()[var] = random.randint(2, 6)
    
    
    if shape_color.get() == "":
        t.color(random.choice(COLORS))
    else:
        try:
            t.color(shape_color.get().lower())
        except turtle.TurtleGraphicsError:
            t.color(random.choice(COLORS))
        
    try:
        turtle.TurtleScreen(canvas).bgcolor(bg_color.get().lower())
    except tk._tkinter.TclError:
        turtle.TurtleScreen(canvas).bgcolor(random.choice(COLORS))
        
    
    t.pd()
    start  = time.time()
    while time.time()-start < length:
        global r
        r += 1
        
        t.circle(r, steps=sides)
        t.left(1)

#Destroys root, gets rid of coordinate args        
def exit_(x=None,y=None):
    root.destroy()

#Lowers window to see advanced entries
def advanced():
    global advanced_tab

    if advanced_tab == False:  
        root.geometry("240x400")
        advanced_tab = True
    else:
        root.geometry("240x125")
        advanced_tab = False
        
#to restart program
def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)
    
#Tkinter Windows    
root = tk.Tk()

top = tk.Toplevel(root)


#Secondary window, the turtle canvas
canvas = turtle.Canvas(top)
canvas.pack(fill="both",expand=1)
t = turtle.RawTurtle(canvas)
turtle.TurtleScreen(canvas).bgcolor("black")
t.speed(0)
t.up()

tk.Label(
    root,
    text="How long to run:\n(In seconds)"
    ).grid(row=0,column=0,rowspan=2)

end = tk.Entry(root,width=10)
end.grid(row=0,column=1)

tk.Label(
    root,
    text="How many sides:"
    ).grid(row=2,column=0)

sides_ = tk.Entry(root,width=10)
sides_.grid(row=2,column=1)

draw_btn = tk.Button(
    root,
    text="Draw",
    command=draw,
    width=10
    )
draw_btn.grid(row=3,column=0)

#Advanced tab
tk.Label(
    root,
    text=""
    ).grid(row=5,column=0, columnspan=2)

tk.Label(
    root,
    text="Shape Color:"
    ).grid(row=6,column=0)
shape_color = tk.Entry(root,width=10)
shape_color.grid(row=6,column=1)
#shape_color.insert(0, "blue")
        
tk.Label(
    root,
    text="Background Color:"
    ).grid(row=7,column=0)
bg_color = tk.Entry(root,width=10)
bg_color.grid(row=7,column=1)
#bg_color.insert(0, "black")

tk.Label(
    root,
    text="Pen Size:"
    ).grid(row=8,column=0)
pensize_ = tk.Entry(root,width=10)
pensize_.grid(row=8,column=1)
pensize_.insert(0, "0")

tk.Label(
    root,
    text="Increment:"
    ).grid(row=9,column=0)
increment = tk.Entry(root,width=10)
increment.grid(row=9,column=1)
increment.insert(0, "1")

#Exit button, esc key, and x key destroys root
exit_btn = tk.Button(
    root,
    text="Exit",
    command=exit_,
    width=10
    )
exit_btn.grid(row=3,column=1)
root.bind_all("<Escape>", exit_)
root.bind_all("x", exit_)

advanced_btn = tk.Button(
    root,
    text="(Advanced)",
    command=advanced,
    width=20
    )
advanced_btn.grid(row=4,column=0,columnspan=2)

#Set root window up
root.title("")
root.geometry("240x125")
root.resizable(0,0)
root.attributes("-topmost", True)

#Set top window up
cartesian = root.geometry()
y = cartesian[cartesian.rfind("+"):]
catesian = cartesian.strip(y)
x = cartesian[cartesian.rfind("+"):]

top.geometry("500x500"+"+"+str(int(x)+210)+y)
top.title("Spirals")
top.resizable(0,0)

#Main loop, need a bool for if advanced open
advanced_tab = False
root.mainloop()
