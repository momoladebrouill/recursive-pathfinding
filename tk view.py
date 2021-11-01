import tkinter as tk
from functools import partial
from pathfinding import *
mur="#"

def colorize(to_blick=[]):
    for ind,but in enumerate(buttons):
        
        tuplepos=divmod(ind,8)[::-1]
        pos=Pos(tuplepos[0],tuplepos[1])
        text=plato[pos]
        buttons[ind]["text"]=text
        if text in to_blick:
            buttons[ind]['background']="#0000FF"
        elif text==mur:
            buttons[ind]['background']="#FF0000"
        else:
            buttons[ind]['background']="#FFFFFF"

def changefor(e):
    if type(e)==tuple:
        if plato[e]==beg:
            colorize(pathfind())
        elif plato[e]==end:
            plato.__init__()
            plato[end.pos]=end
            plato[beg.pos]=beg
            colorize()
        else:
            plato[e]=" " if plato[e]==mur else mur
            colorize()
    

f=tk.Tk()
f.title('Pathfinding visualisation by momoladebrouill')
buttons=[]

for pos,piece in plato:
    f.grid_columnconfigure(pos[0], weight=1)
    f.grid_rowconfigure(pos[1], weight=1)
    but=tk.Button(f,
                  text=piece,
                  font="Consolas 25",
                  width=3,
                  height=1,
                  relief='flat',
                  command=partial(changefor, pos)
                  )
    but.grid(row=pos[1],column=pos[0],sticky='NESW')
    buttons.append(but)

f.bind('<Button-1>',changefor)
colorize()


