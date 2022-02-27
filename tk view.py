import tkinter as tk
from tkinter import messagebox as ms
from functools import partial
from pathfinding import *
from colorsys import hsv_to_rgb
from random import random
hsv=lambda h:"#%02x%02x%02x" % tuple([int(c) for c in hsv_to_rgb(h,1,255)])
coul=random()
mur="#"
fontsize=10
def colorize(to_blick=[]):
    for ind,but in enumerate(buttons):
        
        tuplepos=divmod(ind,SIZE)[::-1]
        pos=Pos(tuplepos[0],tuplepos[1])
        text=plato[pos]
        buttons[ind]["text"]=text
        if text in to_blick:
            buttons[ind]['background']=hsv(1-coul)
        elif text==mur:
            buttons[ind]['background']=hsv(coul)
            buttons[ind]["text"]=" "
        else:
            buttons[ind]['background']="#FFFFFF"

def changefor(e):
    if type(e)==tuple:
        if plato[e]==beg:
            p=pathfind(diag=isdiag.get())
            if p==None:
                ms.showerror(title='Path error',message="No path found between B and E\nPlease ensure that it the path between those two points exists and that the board is clear before finding a path")
            else:
                colorize(p)
        elif plato[e]==end:
            if rmwall.get():
                plato.__init__()
                plato[end.pos]=end
                plato[beg.pos]=beg
                colorize()
            else:
                for pos,val in plato:
                    if val!=mur:
                        plato[pos]=" "
                plato[end.pos]=end
                plato[beg.pos]=beg
                colorize()
        else:
            plato[e]=" " if plato[e]==mur else mur
            colorize()
    
def newcolor():
    global coul
    coul=random()
    colorize()
    
f=tk.Tk()
f.title('Pathfinding visualisation by momoladebrouill')
buttons=[]
g=tk.Frame(f)
g.pack()
for pos,piece in plato:
    f.grid_columnconfigure(pos[0], weight=1)
    f.grid_rowconfigure(pos[1], weight=1)
    but=tk.Button(g,
                  text=piece,
                  font=f"Consolas {fontsize}",
                  width=1,
                  height=1,
                  relief='flat',
                  command=partial(changefor, pos)
                  )
    but.grid(row=pos[1],column=pos[0],sticky='NESW')
    buttons.append(but)
g.bind('<Button-1>',changefor)
isdiag=tk.BooleanVar(f,True)
rmwall=tk.BooleanVar(f,False)
tk.Checkbutton(f,
               text="can faire des diagonales",
               onvalue=True,
               offvalue=False,
               variable=isdiag).pack()
tk.Checkbutton(f,
               text="remove walls on erase",
               onvalue=True,
               offvalue=False,
               variable=rmwall).pack()
tk.Button(f,
               text="reshake colors",
               command=newcolor).pack()
colorize()
f.mainloop()

