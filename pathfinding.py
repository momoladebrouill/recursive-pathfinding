import random
abc="abcdefghijklmnopqrstuvwxyz"
SIZE=15

class Plato():
    def __init__(self,taillex=8,tailley=8):
        self.array=[" " for _ in range(taillex*tailley)]
        self.larg=taillex
        self.haut=tailley
        self.total=taillex*tailley
    def __repr__(self):
        t=""
        for i in range(self.total):
            if i%self.larg==0:
                t+="\n"
            t+=str(self.array[i])+" "
        return t
    def __getitem__(self,pos):
        x,y=(pos.x,pos.y) if type(pos)==Pos else pos
        return self.array[self.larg*y+x]
    def __contains__(self,pos):
        return -1<pos.x<self.larg and -1<pos.y<self.haut
    def __setitem__(self,pos,item):
        if type(pos)==Pos:
            x,y=pos.x,pos.y
        else:
            x,y=pos
        self.array[self.larg*y+x]=item
    def __iter__(self):
        self.it=0
        return self
    def __next__(self):
        try:
            self.it+=1
            return divmod(self.it-1,self.larg)[::-1],self.array[self.it-1]
        except IndexError:
            raise StopIteration
        

class Pos():
    def __init__(self,x,y):
        self.x,self.y=x,y
    def __add__(self,other):
        return Pos(self.x+other.x,self.y+other.y) if type(other)==Pos else Pos(self.x+other[0],self.y+other[1])
    def __repr__(self):
        return str(self.x)+str(self.y)
    def __mul__(self,fac):
        return Pos(self.x*fac,self.y*fac)
    def __getitem__(self,num):
        return [self.x,self.y][num]
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
class Obj():
    def __init__(self,pos,name):
        self.pos=pos
        self.name=name
        self.list=[]
    def __repr__(self):
        return self.name
    def accoucher(self,pos):
        plato[pos]=Obj(pos,str(len(self.list)))
        plato[pos].list=self.list+[self]
        return plato[pos]
    def polluer(self,diag):
        if diag:
            moves=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        else:
            moves=[(-1, 0), (0, -1), (0, 1), (1, 0)]
        newmen=[]
        for move in moves:
            new=Pos(self.pos.x+move[0],self.pos.y+move[1])
            if new in plato:
                if plato[new]==" ":
                    newmen.append(self.accoucher(new))
                elif plato[new]==end:
                    return (self.list+[self,end],)
                elif type(plato[new])==type(self):
                    if len(plato[new].list)>len(self.list)+1:
                        newmen.append(accoucher(new))
                
        return newmen
end=Obj(Pos(SIZE-1,SIZE-1),"E")
beg=Obj(Pos(0,0),"B")
plato=Plato(SIZE,SIZE)
plato[end.pos]=end
plato[beg.pos]=beg

def checkandcontinue(gen,diag):
    nextgen=[]
    for obj in gen:
        rend=obj.polluer(diag)
        if type(rend)==list:
            nextgen+=rend
        else:
            return rend
    return nextgen

def pathfind(diag=True):
    p=[beg]
    while not type(p)==tuple:
        p=checkandcontinue(p,diag)
        if p==[]:
            return None
    return p[0]

