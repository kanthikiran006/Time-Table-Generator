from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("1500x800")
root.config(bg = "white")
dict = {
    "jayaprakashnaidulenka@gmail.com" : "prakash",
    "maniveer@gmail.com" : "m",
    "kanthikiran@gmail.com" : "k"

}
global dict1
dict1 = {
    "8:00-8:50"   : [0,""],
    "8:50-9:40"   : [0,""],
    "9:45-10:35"  : [0,""],
    "10:40-11:30" : [0,""],
    "11:35-12:25" : [0,""],
    "12:30-1:20"  : [0,""],
    "1:25-2:15"   : [0,""],
    "2:20-3:10"   : [0,""],
    "3:10-4:00"   : [0,""],
    "4:00-4:50"   : [0,""]
}
global dict2
dict2 = {
    "8:00-8:50"   : [0,""],
    "8:50-9:40"   : [0,""],
    "9:45-10:35"  : [0,""],
    "10:40-11:30" : [0,""],
    "11:35-12:25" : [0,""],
    "12:30-1:20"  : [0,""],
    "1:25-2:15"   : [0,""],
    "2:20-3:10"   : [0,""],
    "3:10-4:00"   : [0,""],
    "4:00-4:50"   : [0,""]
}
global dict3
dict3 = {
    "8:00-8:50"   : [0,""],
    "8:50-9:40"   : [0,""],
    "9:45-10:35"  : [0,""],
    "10:40-11:30" : [0,""],
    "11:35-12:25" : [0,""],
    "12:30-1:20"  : [0,""],
    "1:25-2:15"   : [0,""],
    "2:20-3:10"   : [0,""],
    "3:10-4:00"   : [0,""],
    "4:00-4:50"   : [0,""]
}
global dict4
dict4 = {
    "8:00-8:50"   : [0,""],
    "8:50-9:40"   : [0,""],
    "9:45-10:35"  : [0,""],
    "10:40-11:30" : [0,""],
    "11:35-12:25" : [0,""],
    "12:30-1:20"  : [0,""],
    "1:25-2:15"   : [0,""],
    "2:20-3:10"   : [0,""],
    "3:10-4:00"   : [0,""],
    "4:00-4:50"   : [0,""]
}
global dict5
dict5 = {
    "8:00-8:50"   : [0,""],
    "8:50-9:40"   : [0,""],
    "9:45-10:35"  : [0,""],
    "10:40-11:30" : [0,""],
    "11:35-12:25" : [0,""],
    "12:30-1:20"  : [0,""],
    "1:25-2:15"   : [0,""],
    "2:20-3:10"   : [0,""],
    "3:10-4:00"   : [0,""],
    "4:00-4:50"   : [0,""]
}
try:
    with open("slots.txt") as f:
        d = f.readlines()
except FileNotFoundError:
    o1 = [[" Day Order ","Slot - A","Available seats","Slot - B","Available seats","Slot - C","Available seats","Room no:"],
        ["Day Order-1","8:00-9:40",60,"9:45-10:35",60,"10:40-11:30",60,501],["Day Order-2","9:45-10:35",60,"10:40-11:30",60,"11:35-1:20",60,502],
        ["Day Order-3","12:30-2:15",60,"2:20-3:10",60,"3:10-4:00",60,503],["Day Order-4","8:00-9:40",60,"9:45-10:35",60,"10:40-11:30",60,504],
        ["Day Order-5","9:45-10:35",60,"10:40-11:30",60,"11:35-1:20",60,505]]
    o2 = [[" Day Order ","Slot - A","Available seats","Slot - B","Available seats","Slot - C","Available seats","Room no:"],
                ["Day Order-1","9:45-11:30",60,"11:35-12:25",60,"2:20-3:10",60,501],["Day Order-2","8:00-9:40",60,"9:45-10:35",60,"11:35-12:25",60,502],
                ["Day Order-3","12:30-2:15",60,"2:20-3:10",60,"3:10-4:00",60,503],["Day Order-4","8:00-9:40",60,"9:45-10:35",60,"11:35-12:25",60,504],
                ["Day Order-5","9:45-11:30",60,"11:35-12:25",60,"2:20-3:10",60,505]]
    o3 = [[" Day Order ","Slot - A","Available seats","Slot - B","Available seats","Slot - C","Available seats","Room no:"],
            ["Day Order-1","12:30-2:15",60,"2:20-3:10",60,"3:10-4:00",60,501],["Day Order-2","8:00-9:40",60,"9:45-10:35",60,"11:35-12:25",60,502],
            ["Day Order-3","9:45-11:30",60,"11:35-12:25",60,"2:20-3:10",60,503],["Day Order-4","10:40-12:25",60,"1:25-2:15",60,"2:20-3:10",60,504],
            ["Day Order-5","8:00-9:40",60,"9:45-10:35",60,"11:35-12:25",60,505]]
    o4 = [[" Day Order ","Slot - A","Available seats","Slot - B","Available seats","Slot - C","Available seats","Room no:"],
            ["Day Order-1","9:45-11:30",60,"11:35-12:25",60,"2:20-3:10",60,501],["Day Order-2","8:00-9:40",60,"9:45-10:35",60,"11:35-12:25",60,502],
            ["Day Order-3","12:30-2:15",60,"2:20-3:10",60,"3:10-4:00",60,503],["Day Order-4","8:00-9:40",60,"9:45-10:35",60,"11:35-12:25",60,504],
            ["Day Order-5","9:45-11:30",60,"11:35-12:25",60,"2:20-3:10",60,505]]
    o5 = [[" Day Order ","Slot - A","Available seats","Slot - B","Available seats","Slot - C","Available seats","Room no:"],
            ["Day Order-1","8:00-9:40",60,"9:45-10:35",60,"10:40-11:30",60,501],["Day Order-2","9:45-10:35",60,"10:40-11:30",60,"11:35-1:20",60,502],
            ["Day Order-3","12:30-2:15",60,"2:20-3:10",60,"3:10-4:00",60,503],["Day Order-4","8:00-9:40",60,"9:45-10:35",60,"10:40-11:30",60,504],
            ["Day Order-5","9:45-10:35",60,"10:40-11:30",60,"11:35-1:20",60,505]]
    b = o1+o2+o3+o4+o5
    for i in range(30):
        for j in range(8):
            b[i][j] = str(b[i][j])
    for i in range(30):
        b[i] = ",".join(b[i])+"\n"
    with open("slots.txt","w") as f:
        for i in b:
            f.writelines(i)
    with open("slots.txt") as f:
        d = f.readlines()
j = 0
global b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,e1,e2,e3,e4,e5,f1,f2,f3,f4,f5,h1,h2,h3,h4,h5,g1,g2,g3,g4,g5,t1,t2,t3,t4,t5,v1,v2,v3,v4,v5
b1,b2,b3,b4,b5 = [],[],[],[],[]
for i in d:
    a = i[:-1].split(",")
    if j%6 !=0:
        a[2] = int(a[2])
        a[4] = int(a[2])
        a[6] = int(a[2])
    if j<6:
        b1.append(a)
    if j>=6 and j<12:
        b2.append(a)
    if j>=12 and j<18:
        b3.append(a)
    if j>=18 and j<24:
        b4.append(a)
    if j>=24 and j<30:
        b5.append(a)
    j+=1
c1=e1=f1=h1=g1=t1=v1=b1
c2=e2=f2=h2=g2=t2=v2=b2
c3=e3=f3=h3=g3=t3=v3=b3
c4=e4=f4=h4=g4=t4=v4=b4
c5=e5=f5=h5=g5=t5=v5=b5
global msg 
def confirm(h,i,j,msg,k,d):
    root = Tk()
    root.geometry("300x100")
    root.title("confirmation")
    l = Label(root,text = msg)
    l.pack()
    def ok():
        h[i][j]-=1
        global count
        count+=1
        if count == 20:
            root.destroy()
            w1()
        root.destroy()
    def cancel():
        a = str(h[i][k])
        try:
            d[a][0]=0
            d[a][1]=""
        except KeyError:
            a = a.split("-")
            b = a[0].split(":")
            b = (int(b[0])*60)+int(b[1])+50
            o = b//60
            if o>12:
                o%=12
            m = a[0]+"-"+str(o)+":"+str(b%60)
            d[m][0]=0
            d[m][1]=""
            try:
                m = str(o)+":"+str(b%60)+"-"+a[1]
                d[m][0]=0
                d[m][1]=""
            except KeyError:
                b +=5
                if o>12:
                    o%=12
                m = str(o)+":"+str(b%60)+"-"+a[1]
                d[m][0]=0
                d[m][1]=""
        root.destroy()
    Button(root,text = "ok",bg = "cyan",width = 10,font = ("Arial",10,"bold"),command=ok).place(x = 70,y = 70)
    Button(root,text = "cancel",bg = "cyan",width = 10,font = ("Arial",10,"bold"),command=cancel).place(x = 180,y = 70)
    root.mainloop()
def clash():
    root = Tk()
    root.geometry("300x100")
    root.title("clash")
    l = Label(root,text = "you are already selected this slot",fg = "red",font = ("Arial",10,"bold"))
    l.pack()
    def ok():
        root.destroy()
    Button(root,text = "ok",bg = "cyan",width = 10,font = ("Arial",10,"bold"),command=ok).place(x = 100,y = 70)
    root.mainloop()
def w3():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Compiler Design",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 650,y = 0)
    l = Label(s,text = "You must select '3 hr 20 mins' slots",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L1","Ast.Prof",15,"Click here","Available"],
        ["L2","Ast.Prof",15,"Click here","Available"],["L3","Ast.Prof",15,"Click here","Available"],
        ["L4","Ast.Prof",15,"Click here","Available"],["L5","Ast.Prof",15,"Click here","Available"]]
    def w31():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L1\n room no:501\nCD"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L1\n room no:501\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L1\n room no:501\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L1\n room no:501\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L1\n room no:502\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L1\n room no:502\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L1\n room no:502\nCD"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L1\n room no:502\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(b1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L1\n room no:503\nCD"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L1\n room no:503\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(b1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L1\n room no:503\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L1\n room no:503\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(b1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L1\n room no:504\nCD"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L1\n room no:504\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L1\n room no:504\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L1\n room no:504\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L1\n room no:505\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L1\n room no:505\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L1\n room no:505\nCD"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L1\n room no:505\nCD"
                global msg
                msg = "Faculty Name : L1 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(b1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global b1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = b1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = b1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w32():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L2\n room no:401\nCD"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L2\n room no:401\nCD"
                global msg
                msg = "Faculty Name : L2 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(b2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L2\n room no:401\nCD"
                global msg
                msg = "Faculty Name : L2 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L2\n room no:401\nCD"
                global msg
                msg = "Faculty Name : L2 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L2\n room no:402\nCD"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L2\n room no:402\nCD"
                global msg
                msg = "Faculty Name : L2 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L2\n room no:402\nCD"
                global msg
                msg = "Faculty Name : L2 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L2\n room no:402\nCD"
                global msg
                msg = "Faculty Name : L2 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L2\n room no:403\nCD"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L2\n room no:403\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(b2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L2\n room no:403\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L2\n room no:403\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(b2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L2\n room no:404\nCD"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L2\n room no:404\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L2\n room no:404\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L2\n room no:404\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L2\n room no:405\nCD"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L2\n room no:405\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(b2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L2\n room no:405\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L2\n room no:405\nCD"
                global msg
                msg ="Faculty Name : L2 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global b2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = b2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = b2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w33():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L3\n room no:601\nCD"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L3\n room no:601\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(b3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L3\n room no:601\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L3\n room no:601\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(b3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L3\n room no:602\nCD"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L3\n room no:602\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L3\n room no:602\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L3\n room no:602\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L3\n room no:603\nCD"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L3\n room no:603\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(b3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L3\n room no:603\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L3\n room no:603\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L3\n room no:604\nCD"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L3\n room no:604\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(b3,4,2,msg,1,dict4)          
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L3\n room no:604\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(b3,4,4,msg,3,dict4)  
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L3\n room no:604\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L3\n room no:605\nCD"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L3\n room no:605\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L2\n room no:605\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L3\n room no:605\nCD"
                global msg
                msg = "Faculty Name : L3 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b3,5,6,msg,5,dict5)  
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global b3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = b3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = b3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w34():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L4\n room no:701\nCD"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L4\n room no:701\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(b4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L4\n room no:701\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L4\n room no:701\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L4\n room no:702\nCD"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L4\n room no:702\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L4\n room no:702\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L4\n room no:702\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L4\n room no:703\nCD"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L4\n room no:703\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(b4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L4\n room no:703\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L4\n room no:703\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(b4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L4\n room no:704\nCD"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L4\n room no:704\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L4\n room no:704\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L4\n room no:704\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L4\n room no:705\nCD"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L4\n room no:705\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(b4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L4\n room no:705\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(b4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L4\n room no:705\nCD"
                global msg
                msg = "Faculty Name : L4 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global b4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = b4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = b4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w35():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L5\n room no:801\nCD"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L5\n room no:801\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L5\n room no:801\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L1\n room no:801\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L5\n room no:802\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L5\n room no:802\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L5\n room no:802\nCD"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L5\n room no:802\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(b5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L5\n room no:803\nCD"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L5\n room no:803\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(b5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L5\n room no:803\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(b5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L5\n room no:803\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(b5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L5\n room no:804\nCD"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L5\n room no:804\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(b5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L5\n room no:804\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L5\n room no:804\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L5\n room no:805\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(b5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L5\n room no:805\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(b5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L5\n room no:805\nCD"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L5\n room no:805\nCD"
                global msg
                msg = "Faculty Name : L5 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(b5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global b5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = b5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = b5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w31,w32,w33,w34,w35]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w4():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Data base management systems",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 450,y = 0)
    l = Label(s,text = "You must select '2 hr 30 mins' class",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L6","Ast.Prof",15,"Click here","Available"],
        ["L7","Ast.Prof",15,"Click here","Available"],["L8","Ast.Prof",15,"Click here","Available"],
        ["L9","Ast.Prof",15,"Click here","Available"],["L10","Ast.Prof",15,"Click here","Available"]]
    def w41():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L6\n room no:506\nDBMS"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L6\n room no:506\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L6\n room no:506\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L6\n room no:506\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L6\n room no:507\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L6\n room no:507\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L6\n room no:507\nDBMS"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L6\n room no:507\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(c1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L6\n room no:508\nDBMS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L6\n room no:508\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(c1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L6\n room no:508\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L6\n room no:508\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(c1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L6\n room no:509\nDBMS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L6\n room no:509\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L6\n room no:509\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L6\n room no:509\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L6\n room no:510\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L6\n room no:510\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L6\n room no:510\nDBMS"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L6\n room no:510\nDBMS"
                global msg
                msg = "Faculty Name : L6 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(c1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global c1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = c1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = c1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w42():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L7\n room no:406\nDBMS"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L7\n room no:406\nDBMS"
                global msg
                msg = "Faculty Name : L7 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(c2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L7\n room no:406\nDBMS"
                global msg
                msg = "Faculty Name : L7 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L7\n room no:406\nDBMS"
                global msg
                msg = "Faculty Name : L7 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L7\n room no:408\nDBMS"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L7\n room no:408\nDBMS"
                global msg
                msg = "Faculty Name : L7 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L7\n room no:408\nDBMS"
                global msg
                msg = "Faculty Name : L7 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L7\n room no:408\nDBMS"
                global msg
                msg = "Faculty Name : L7 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L7\n room no:407\nDBMS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L7\n room no:407\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(c2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L7\n room no:407\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L7\n room no:407\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(c2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L7\n room no:409\nDBMS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L7\n room no:409\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L7\n room no:409\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L7\n room no:409\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L7\n room no:410\nDBMS"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L7\n room no:410\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(c2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L7\n room no:410\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L7\n room no:410\nDBMS"
                global msg
                msg ="Faculty Name : L7 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global c2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = c2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = c2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w43():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L8\n room no:606\nDBMS"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L8\n room no:606\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(c3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L8\n room no:606\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L8\n room no:606\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(c3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L8\n room no:607\nDBMS"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L8\n room no:607\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L8\n room no:607\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L8\n room no:607\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L8\n room no:608\nDBMS"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L8\n room no:608\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(c3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L8\n room no:608\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L8\n room no:608\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L8\n room no:609\nDBMS"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L8\n room no:609\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(c3,4,2,msg,1,dict4)       
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L8\n room no:609\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(c3,4,4,msg,3,dict4)  
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L8\n room no:609\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L8\n room no:610\nDBMS"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L8\n room no:610\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L8\n room no:610\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L8\n room no:610\nDBMS"
                global msg
                msg = "Faculty Name : L8 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c3,5,6,msg,5,dict5)  
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global c3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = c3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = c3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w44():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L9\n room no:706\nDBMS"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L9\n room no:706\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(c4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L9\n room no:706\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L9\n room no:706\nDBMS"
                global msg
                msg = "Faculty Name : L4 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L9\n room no:707\nDBMS"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L9\n room no:707\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L9\n room no:707\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L9\n room no:707\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L9\n room no:708\nDBMS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L9\n room no:708\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(c4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L9\n room no:708\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L9\n room no:708\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(c4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L9\n room no:709\nDBMS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L9\n room no:709\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L9\n room no:709\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L9\n room no:709\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L9\n room no:710\nDBMS"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L9\n room no:710\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(c4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L9\n room no:710\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(c4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L9\n room no:710\nDBMS"
                global msg
                msg = "Faculty Name : L9 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global c4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = c4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = c4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w45():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L10\n room no:806\nDBMS"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L10\n room no:806\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L10\n room no:806\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L10\n room no:806\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L10\n room no:807\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L10\n room no:807\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L10\n room no:807\nDBMS"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L10\n room no:807\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(c5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L10\n room no:808\nDBMS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L10\n room no:808\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(c5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L10\n room no:808\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(c5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L10\n room no:808\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(c5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L10\n room no:809\nDBMS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L10\n room no:809\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(c5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L10\n room no:809\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L10\n room no:809\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L10\n room no:810\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(c5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L10\n room no:810\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(c5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L10\n room no:810\nDBMS"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L10\n room no:810\nDBMS"
                global msg
                msg = "Faculty Name : L10 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(c5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global c5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = c5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = c5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w41,w42,w43,w44,w45]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w5():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Computer Networks",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 580,y = 0)
    l = Label(s,text = "You must select '3 hr 20 mins' class",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L11","Ast.Prof",15,"Click here","Available"],
        ["L12","Ast.Prof",12,"Click here","Available"],["L13","Ast.Prof",10,"Click here","Available"],
        ["L14","Ast.Prof",9,"Click here","Available"],["L15","Ast.Prof",5,"Click here","Available"]]
    def w51():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L11\n room no:511\nCN"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L11\n room no:511\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L11\n room no:511\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L11\n room no:511\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L11\n room no:512\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L11\n room no:512\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L11\n room no:512\nCN"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L11\n room no:512\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(e1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L11\n room no:513\nCN"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L11\n room no:513\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(e1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L11\n room no:513\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L11\n room no:513\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(e1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L11\n room no:514\nCN"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L11\n room no:514\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L11\n room no:514\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L11\n room no:514\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L11\n room no:515\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L11\n room no:515\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L11\n room no:515\nCN"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L11\n room no:510\nCN"
                global msg
                msg = "Faculty Name : L11 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(e1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global e1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = e1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = e1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w52():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L12\n room no:411\nCN"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L12\n room no:411\nCN"
                global msg
                msg = "Faculty Name : L12 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(e2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L12\n room no:411\nCN"
                global msg
                msg = "Faculty Name : L12 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L12\n room no:411\nCN"
                global msg
                msg = "Faculty Name : L12 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L12\n room no:412\nCN"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L12\n room no:412\nCN"
                global msg
                msg = "Faculty Name : L12 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L12\n room no:412\nCN"
                global msg
                msg = "Faculty Name : L12 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L12\n room no:412\nCN"
                global msg
                msg = "Faculty Name : L12 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L12\n room no:413\nCN"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L12\n room no:413\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(e2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L12\n room no:413\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L12\n room no:413\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(e2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L12\n room no:414\nCN"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L12\n room no:414\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L12\n room no:414\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L12\n room no:414\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L12\n room no:415\nCN"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L12\n room no:415\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(e2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L12\n room no:415\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L12\n room no:415\nCN"
                global msg
                msg ="Faculty Name : L12 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global e2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = e2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = e2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w53():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L13\n room no:611\nCN"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L13\n room no:611\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(e3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L13\n room no:611\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L13\n room no:611\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(e3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L13\n room no:612\nCN"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L13\n room no:612\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L13\n room no:612\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L13\n room no:612\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L13\n room no:613\nCN"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L13\n room no:613\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(e3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L13\n room no:613\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L13\n room no:613\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L13\n room no:614\nCN"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L13\n room no:614\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(e3,4,2,msg,1,dict4)          
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L13\n room no:614\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(e3,4,4,msg,3,dict4)  
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L13\n room no:614\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L13\n room no:615\nCN"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L13\n room no:615\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L13\n room no:615\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L13\n room no:615\nCN"
                global msg
                msg = "Faculty Name : L13 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e3,5,6,msg,5,dict5)  
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global e3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = e3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = e3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w54():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L14\n room no:711\nCN"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L14\n room no:711\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(e4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L14\n room no:711\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L14\n room no:711\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L14\n room no:712\nCN"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L14\n room no:712\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L14\n room no:712\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L14\n room no:712\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L14\n room no:713\nCN"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L14\n room no:713\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(e4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L14\n room no:713\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L14\n room no:713\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(e4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L14\n room no:714\nCN"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L14\n room no:709\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L14\n room no:714\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L14\n room no:714\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L14\n room no:715\nCN"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L14\n room no:710\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(e4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L14\n room no:715\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(e4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L14\n room no:715\nCN"
                global msg
                msg = "Faculty Name : L14 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global e4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = e4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = e4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w55():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L15\n room no:811\nCN"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L15\n room no:811\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L15\n room no:811\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L15\n room no:811\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L15\n room no:812\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L15\n room no:812\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L15\n room no:812\nCN"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L15\n room no:812\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(e5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L15\n room no:813\nCN"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L15\n room no:813\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(e5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L15\n room no:813\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(e5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L15\n room no:813\nCN"
                global msg
                msg = "Faculty Name : L10 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(e5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L15\n room no:814\nCN"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L15\n room no:814\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(e5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L15\n room no:814\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L15\n room no:814\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L15\n room no:815\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(e5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L15\n room no:815\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(e5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L15\n room no:815\nCN"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L15\n room no:815\nCN"
                global msg
                msg = "Faculty Name : L15 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(e5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global e5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = e5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = e5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w51,w52,w53,w54,w55]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w6():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Operating Systems",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 580,y = 0)
    l = Label(s,text = "You must select '3 hr 20 mins' class",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L16","Prof",20,"Click here","Available"],
        ["L17","Ast.Prof",17,"Click here","Available"],["L18","Ast.Prof",13,"Click here","Available"],
        ["L19","Ast.Prof",10,"Click here","Available"],["L20","Ast.Prof",8,"Click here","Available"]]
    def w61():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L16\n room no:510\nOS"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L16\n room no:510\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L16\n room no:510\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L16\n room no:510\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L16\n room no:509\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L16\n room no:509\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L16\n room no:509\nOS"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L16\n room no:509\nOS"
                global msg
                msg = "Faculty Name : L16\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(f1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L16\n room no:508\nOS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L16\n room no:508\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(f1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L16\n room no:508\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L16\n room no:508\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(f1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L16\n room no:507\nOS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L16\n room no:507\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L16\n room no:507\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L16\n room no:507\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L16\n room no:515\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L16\n room no:506\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L16\n room no:506\nOS"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L16\n room no:506\nOS"
                global msg
                msg = "Faculty Name : L16 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(f1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global f1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = f1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = f1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w62():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L17\n room no:405\nOS"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L17\n room no:405\nOS"
                global msg
                msg = "Faculty Name : L17 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(f2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L17\n room no:405\nOS"
                global msg
                msg = "Faculty Name : L17 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L17\n room no:405\nOS"
                global msg
                msg = "Faculty Name : L17 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L17\n room no:404\nOS"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L17\n room no:404\nOS"
                global msg
                msg = "Faculty Name : L17 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L17\n room no:404\nOS"
                global msg
                msg = "Faculty Name : L17 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L17\n room no:404\nOS"
                global msg
                msg = "Faculty Name : L17 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L17\n room no:403\nOS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L17\n room no:403\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(f2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L17\n room no:403\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L17\n room no:403\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(f2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L17\n room no:402\nOS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L17\n room no:402\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L17\n room no:402\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L17\n room no:402\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L17\n room no:401\nOS"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L17\n room no:401\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(f2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L17\n room no:401\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L17\n room no:401\nOS"
                global msg
                msg ="Faculty Name : L17 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global f2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = f2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = f2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w63():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L18\n room no:610\nOS"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L18\n room no:610\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(f3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L18\n room no:610\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L18\n room no:610\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(f3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L18\n room no:609\nOS"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L18\n room no:609\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L18\n room no:609\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L18\n room no:609\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L18\n room no:608\nOS"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L18\n room no:608\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(f3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L18\n room no:608\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L18\n room no:608\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L18\n room no:607\nOS"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L18\n room no:607\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(f3,4,2,msg,1,dict4)      
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L18\n room no:607\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(f3,4,4,msg,3,dict4) 
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L18\n room no:607\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L18\n room no:606\nOS"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L18\n room no:606\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L18\n room no:606\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L18\n room no:606\nOS"
                global msg
                msg = "Faculty Name : L18 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f3,5,6,msg,5,dict5)  
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global f3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = f3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = f3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w64():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L19\n room no:716\nOS"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L19\n room no:716\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(f4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L19\n room no:716\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L19\n room no:716\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L19\n room no:717\nOS"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L19\n room no:717\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L19\n room no:717\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L19\n room no:717\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L19\n room no:718\nOS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L19\n room no:718\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(f4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L19\n room no:718\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L19\n room no:718\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(f4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L19\n room no:719\nOS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L19\n room no:719\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L19\n room no:719\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L19\n room no:719\nOS"
                global msg
                msg = "Faculty Name : L19\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L19\n room no:720\nOS"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L19\n room no:720\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(f4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L19\n room no:720\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(f4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L19\n room no:720\nOS"
                global msg
                msg = "Faculty Name : L19 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global f4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = f4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = f4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w65():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L20\n room no:805\nOS"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L20\n room no:805\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L20\n room no:805\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L20\n room no:805\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L20\n room no:804\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L20\n room no:804\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L20\n room no:804\nOS"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L20\n room no:804\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(f5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L20\n room no:803\nOS"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L20\n room no:803\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(f5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L20\n room no:803\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(f5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L20\n room no:803\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(f5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L20\n room no:802\nOS"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L20\n room no:802\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(f5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L20\n room no:802\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L20\n room no:802\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L20\n room no:801\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(f5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L20\n room no:801\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(f5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L20\n room no:801\nOS"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L20\n room no:801\nOS"
                global msg
                msg = "Faculty Name : L20 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(f5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global f5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = f5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = f5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w61,w62,w63,w64,w65]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w7():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Algorithms",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 600,y = 0)
    l = Label(s,text = "You must select '2 hr 30 mins' class",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L21","Prof",16,"Click here","Available"],
        ["L22","Ast.Prof",14,"Click here","Available"],["L23","Ast.Prof",13,"Click here","Available"],
        ["L24","Ast.Prof",10,"Click here","Available"],["L25","Ast.Prof",8,"Click here","Available"]]
    def w71():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L21\n room no:101\nALGO"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L21\n room no:101\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L21\n room no:101\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L21\n room no:101\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L21\n room no:102\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L21\n room no:102\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L21\n room no:102\nALGO"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L21\n room no:101\nALGO"
                global msg
                msg = "Faculty Name : L21\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(g1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L21\n room no:103\nALGO"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L21\n room no:103\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(g1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L21\n room no:103\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L21\n room no:103\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(g1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L21\n room no:103\nALGO"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L21\n room no:103\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L21\n room no:104\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L21\n room no:104\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L21\n room no:104\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L21\n room no:105\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L21\n room no:105\nALGO"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L21\n room no:105\nALGO"
                global msg
                msg = "Faculty Name : L21 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(g1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global g1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = g1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = g1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w72():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L22\n room no:201\nALGO"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L22\n room no:201\nALGO"
                global msg
                msg = "Faculty Name : L22 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(g2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L22\n room no:201\nALGO"
                global msg
                msg = "Faculty Name : L22 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L22\n room no:201\nALGO"
                global msg
                msg = "Faculty Name : L22 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L22\n room no:202\nALGO"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L22\n room no:202\nALGO"
                global msg
                msg = "Faculty Name : L22 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L22\n room no:202\nALGO"
                global msg
                msg = "Faculty Name : L22 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L22\n room no:202\nALGO"
                global msg
                msg = "Faculty Name : L22 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L22\n room no:203\nALGO"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L22\n room no:203\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(g2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L22\n room no:203\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L22\n room no:203\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(g2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L22\n room no:204\nALGO"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L22\n room no:204\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L22\n room no:204\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L22\n room no:204\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L22\n room no:205\nALGO"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L22\n room no:205\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(g2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L22\n room no:205\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L22\n room no:205\nALGO"
                global msg
                msg ="Faculty Name : L22 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global g2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = g2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = g2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w73():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L23\n room no:206\nALGO"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L23\n room no:206\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(g3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L23\n room no:206\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L23\n room no:206\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(g3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L23\n room no:207\nALGO"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L23\n room no:207\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L23\n room no:207\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L23\n room no:207\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L23\n room no:208\nALGO"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L23\n room no:208\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(g3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L23\n room no:208\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L23\n room no:208\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L23\n room no:209\nALGO"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L23\n room no:209\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(g3,4,2,msg,1,dict4)          
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L23\n room no:209\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(g3,4,4,msg,3,dict4)  
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L23\n room no:209\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L23\n room no:210\nALGO"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L23\n room no:210\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L23\n room no:210\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L23\n room no:210\nALGO"
                global msg
                msg = "Faculty Name : L23 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g3,5,6,msg,5,dict5)    
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global g3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = g3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = g3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w74():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L24\n room no:216\nALGO"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L24\n room no:216\nALGO"
                global msg
                msg = "Faculty Name : L24\n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(g4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L24\n room no:216\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L24\n room no:216\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L24\n room no:217\nALGO"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L24\n room no:217\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L24\n room no:217\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L24\n room no:217\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L24\n room no:218\nALGO"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L24\n room no:218\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(g4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L24\n room no:218\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L24\n room no:218\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(g4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L24\n room no:219\nALGO"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L24\n room no:219\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L24\n room no:219\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L24\n room no:219\nALGO"
                global msg
                msg = "Faculty Name : L24\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L24\n room no:220\nALGO"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L24\n room no:220\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(g4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L24\n room no:220\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(g4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L24\n room no:220\nALGO"
                global msg
                msg = "Faculty Name : L24 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global g4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = g4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = g4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w75():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L25\n room no:815\nALGO"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L25\n room no:815\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L25\n room no:815\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L25\n room no:815\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L25\n room no:814\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L25\n room no:814\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L25\n room no:814\nALGO"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L25\n room no:814\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(g5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L25\n room no:813\nALGO"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L25\n room no:813\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(g5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L25\n room no:813\nALGO"
                global msg
                msg = "Faculty Name : L25\n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(g5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L25\n room no:813\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(g5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L25\n room no:812\nALGO"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L25\n room no:812\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(g5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L25\n room no:812\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L25\n room no:812\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L25\n room no:811\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(g5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L25\n room no:811\nALGO"
                global msg
                msg = "Faculty Name : L25 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(g5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L25\n room no:811\nALGO"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L25\n room no:811\nALGO"
                global msg
                msg = "Faculty Name : L25\n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(g5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global g5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = g5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = g5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w71,w72,w73,w74,w75]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w8():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Discrete Mathematics",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 550,y = 0)
    l = Label(s,text = "You must select '3 hr 20 mins' class",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L26","Prof",16,"Click here","Available"],
        ["L27","Ast.Prof",14,"Click here","Available"],["L28","Ast.Prof",13,"Click here","Available"],
        ["L29","Ast.Prof",10,"Click here","Available"],["L30","Ast.Prof",8,"Click here","Available"]]
    def w81():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L26\n room no:301\nDM"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L26\n room no:301\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L26\n room no:301\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L26\n room no:301\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L26\n room no:302\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L26\n room no:302\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L26\n room no:302\nDM"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L26\n room no:302\nDM"
                global msg
                msg = "Faculty Name : L26\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(h1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L26\n room no:303\nDM"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L26\n room no:303\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(h1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L26\n room no:303\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L26\n room no:303\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(h1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L26\n room no:303\nDM"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L26\n room no:303\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L26\n room no:304\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L26\n room no:304\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L26\n room no:304\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L26\n room no:305\nDM"
                global msg
                msg = "Faculty Name : L26\n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L26\n room no:305\nDM"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L26\n room no:305\nDM"
                global msg
                msg = "Faculty Name : L26 \n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(h1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global h1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = h1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = h1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w82():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L27\n room no:206\nDM"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L27\n room no:206\nDM"
                global msg
                msg = "Faculty Name : L27 \n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(h2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L27\n room no:206\nDM"
                global msg
                msg = "Faculty Name : L27 \n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L27\n room no:206\nDM"
                global msg
                msg = "Faculty Name : L27 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L27\n room no:207\nDM"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L27\n room no:207\nDM"
                global msg
                msg = "Faculty Name : L27 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L27\n room no:207\nDM"
                global msg
                msg = "Faculty Name : L27 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L27\n room no:207\nDM"
                global msg
                msg = "Faculty Name : L27 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L27\n room no:208\nDM"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L27\n room no:208\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(h2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L27\n room no:208\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L27\n room no:208\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(h2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L27\n room no:209\nDM"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L27\n room no:209\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L27\n room no:209\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L27\n room no:209\nDM"
                global msg
                msg ="Faculty Name : L27\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L27\n room no:210\nDM"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L27\n room no:210\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(h2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L27\n room no:210\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L27\n room no:210\nDM"
                global msg
                msg ="Faculty Name : L27 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global h2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = h2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = h2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w83():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L28\n room no:306\nDM"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L28\n room no:306\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(h3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L28\n room no:306\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L28\n room no:306\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(h3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L28\n room no:307\nDM"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L28\n room no:307\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L28\n room no:307\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L28\n room no:307\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L28\n room no:308\nDM"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L28\n room no:308\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(h3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L28\n room no:308\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L28\n room no:308\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L28\n room no:309\nDM"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L28\n room no:309\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(h3,4,2,msg,1,dict4)          
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L28\n room no:309\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(h3,4,4,msg,3,dict4)  
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L28\n room no:309\nDM"
                global msg
                msg = "Faculty Name : L28\n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L28\n room no:310\nDM"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L28\n room no:310\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L28\n room no:310\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L28\n room no:310\nDM"
                global msg
                msg = "Faculty Name : L28 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h3,5,6,msg,5,dict5)    
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global h3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = h3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = h3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w84():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L29\n room no:316\nDM"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L29\n room no:316\nDM"
                global msg
                msg = "Faculty Name : L29\n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(h4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L29\n room no:316\nDM"
                global msg
                msg = "Faculty Name : L29\n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L29\n room no:316\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L29\n room no:317\nDM"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L29\n room no:317\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L29\n room no:317\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L29\n room no:317\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L29\n room no:318\nDM"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L29\n room no:218\nDM"
                global msg
                msg = "Faculty Name : L29\n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(h4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L29\n room no:318\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L29\n room no:318\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(h4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L29\n room no:319\nDM"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L29\n room no:319\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L29\n room no:319\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L29\n room no:319\nDM"
                global msg
                msg = "Faculty Name : L29\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L29\n room no:320\nDM"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L29\n room no:320\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(h4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L29\n room no:320\nDM"
                global msg
                msg = "Faculty Name : L29\n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L29\n room no:320\nDM"
                global msg
                msg = "Faculty Name : L29 \n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global h4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = h4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = h4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w85():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L30\n room no:915\nDM"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L30\n room no:915\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L30\n room no:915\nDM"
                global msg
                msg = "Faculty Name : L30\n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L30\n room no:915\nDM"
                global msg
                msg = "Faculty Name : L30\n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L30\n room no:914\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L30\n room no:914\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L30\n room no:914\nDM"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L30\n room no:914\nDM"
                global msg
                msg = "Faculty Name : L30\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(h5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L30\n room no:913\nDM"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L30\n room no:913\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(h5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L30\n room no:913\nDM"
                global msg
                msg = "Faculty Name : L30\n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(h5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L30\n room no:913\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(h5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L30\n room no:912\nDM"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L30\n room no:912\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(h5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L30\n room no:912\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L30\n room no:912\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L30\n room no:911\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(h5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L30\n room no:911\nDM"
                global msg
                msg = "Faculty Name : L30 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(h5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L30\n room no:911\nDM"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L30\n room no:911\nDM"
                global msg
                msg = "Faculty Name : L30\n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(h5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global h5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = h5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = h5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w81,w82,w83,w84,w85]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w9():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Automata Theory",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 650,y = 0)
    l = Label(s,text = "You must select '2 hr 30 mins' class",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L31","Ast.Prof",10,"Click here","Available"],
        ["L32","Ast.Prof",10,"Click here","Available"],["L33","Ast.Prof",7,"Click here","Available"],
        ["L34","Ast.Prof",6,"Click here","Available"],["L35","Ast.Prof",4,"Click here","Available"]]
    def w91():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L31\n room no:1301\nTOC"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L31\n room no:1301\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L31\n room no:1301\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L31\n room no:1301\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L31\n room no:1302\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L31\n room no:1302\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L31\n room no:1302\nTOC"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L31\n room no:1302\nTOC"
                global msg
                msg = "Faculty Name : L31\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(t1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L31\n room no:1303\nTOC"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L31\n room no:1303\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(t1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L31\n room no:1303\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L31\n room no:1303\nTOC"
                global msg
                msg = "Faculty Name : L31\n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(t1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L31\n room no:1303\nTOC"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L31\n room no:1303\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L31\n room no:1304\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L31\n room no:1304\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L31\n room no:1304\nTOC"
                global msg
                msg = "Faculty Name : L31 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L31\n room no:1305\nTOC"
                global msg
                msg = "Faculty Name : L31\n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L31\n room no:1305\nTOC"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L31\n room no:1305\nTOC"
                global msg
                msg = "Faculty Name : L31\n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(t1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global t1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = t1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = t1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w92():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L32\n room no:1206\nTOC"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L32\n room no:1206\nTOC"
                global msg
                msg = "Faculty Name : L32\n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(t2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L32\n room no:1206\nTOC"
                global msg
                msg = "Faculty Name : L32\n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L32\n room no:1206\nTOC"
                global msg
                msg = "Faculty Name : L32\n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L32\n room no:1207\nTOC"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L32\n room no:1207\nTOC"
                global msg
                msg = "Faculty Name : L32 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L32\n room no:1207\nTOC"
                global msg
                msg = "Faculty Name : L32 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L32\n room no:1207\nTOC"
                global msg
                msg = "Faculty Name : L32\n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L32\n room no:1208\nTOC"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L32\n room no:1208\nTOC"
                global msg
                msg ="Faculty Name : L32\n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(t2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L32\n room no:1208\nTOC"
                global msg
                msg ="Faculty Name : L32\n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L32\n room no:1208\nTOC"
                global msg
                msg ="Faculty Name : L32\n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(t2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L32\n room no:1209\nTOC"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L32\n room no:1209\nTOC"
                global msg
                msg ="Faculty Name : L32\n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L32\n room no:1209\nTOC"
                global msg
                msg ="Faculty Name : L32\n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L32\n room no:1209\nTOC"
                global msg
                msg ="Faculty Name : L32\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L32\n room no:1210\nTOC"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L32\n room no:1210\nTOC"
                global msg
                msg ="Faculty Name : L31 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(t2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L32\n room no:1210\nTOC"
                global msg
                msg ="Faculty Name : L32 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L32\n room no:1210\nTOC"
                global msg
                msg ="Faculty Name : L32\n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global t2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = t2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = t2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w93():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L33\n room no:1306\nTOC"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L33\n room no:1306\nTOC"
                global msg
                msg = "Faculty Name : L33 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(t3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L33\n room no:1306\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L33\n room no:1306\nTOC"
                global msg
                msg = "Faculty Name : L33 \n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(t3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L33\n room no:1307\nTOC"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L33\n room no:307\nTOC"
                global msg
                msg = "Faculty Name : L33 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L33\n room no:1307\nTOC"
                global msg
                msg = "Faculty Name : L33 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L33\n room no:1307\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L33\n room no:308\nTOC"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L33\n room no:308\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(t3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L33\n room no:1308\nTOC"
                global msg
                msg = "Faculty Name : L33 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L33\n room no:1308\nTOC"
                global msg
                msg = "Faculty Name : L33 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L33\n room no:1309\nTOC"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L33\n room no:1309\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(t3,4,2,msg,1,dict4)          
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L33\n room no:1309\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(t3,4,4,msg,3,dict4)  
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L33\n room no:1309\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L33\n room no:1310\nTOC"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L33\n room no:1310\nTOC"
                global msg
                msg = "Faculty Name : L33 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L33\n room no:1310\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L33\n room no:1310\nTOC"
                global msg
                msg = "Faculty Name : L33\n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t3,5,6,msg,5,dict5)    
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global t3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = t3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = t3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w94():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L34\n room no:1316\nTOC"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L34\n room no:1316\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(t4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L34\n room no:1316\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L34\n room no:1316\nTOC"
                global msg
                msg = "Faculty Name : L34 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L34\n room no:1317\nTOC"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L34\n room no:1317\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L34\n room no:1317\nTOC"
                global msg
                msg = "Faculty Name : L34 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L34\n room no:1317\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(h4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L34\n room no:1318\nTOC"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L34\n room no:1318\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(t4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L34\n room no:1318\nTOC"
                global msg
                msg = "Faculty Name : L34 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L34\n room no:1318\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(t4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L34\n room no:1319\nTOC"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L34\n room no:1319\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L34\n room no:1319\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L34\n room no:1319\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L34\n room no:1320\nTOC"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L34\n room no:1320\nTOC"
                global msg
                msg = "Faculty Name : L34 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(t4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L34\n room no:1320\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(t4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L34\n room no:1320\nTOC"
                global msg
                msg = "Faculty Name : L34\n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global t4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = t4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = t4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w95():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L35\n room no:905\nTOC"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L35\n room no:905\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L35\n room no:905\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L35\n room no:905\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L35\n room no:904\nTOC"
                global msg
                msg = "Faculty Name : L35 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L35\n room no:904\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L35\n room no:904\nTOC"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L35\n room no:904\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(t5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L35\n room no:903\nTOC"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L35\n room no:903\nTOC"
                global msg
                msg = "Faculty Name : L35 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(t5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L35\n room no:903\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(t5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L35\n room no:903\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(t5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L35\n room no:902\nTOC"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L35\n room no:902\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(t5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L35\n room no:902\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L35\n room no:902\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L35\n room no:901\nTOC"
                global msg
                msg = "Faculty Name : L35\n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(t5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L35\n room no:901\nTOC"
                global msg
                msg = "Faculty Name : L35 \n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(t5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L35\n room no:901\nTOC"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L35\n room no:901\nTOC"
                global msg
                msg = "Faculty Name : L30\n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(t5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global t5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = t5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = t5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w91,w92,w93,w94,w95]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w10():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Computational Logic",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 590,y = 0)
    l = Label(s,text = "You must select '2 hr 30 mins' class",fg = "red",font = ("Arial",13,"bold"))
    l.place(x = 650,y = 470)
    a = [["Faculty Name","Designation","Years of Experiance","Slots","Status"],["L36","Ast.Prof",10,"Click here","Available"],
        ["L37","Ast.Prof",10,"Click here","Available"],["L38","Ast.Prof",7,"Click here","Available"],
        ["L39","Ast.Prof",6,"Click here","Available"],["L40","Ast.Prof",4,"Click here","Available"]]
    def w101():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d111():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L36\n room no:1001\nCL"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L36\n room no:1001\nCL"
                global msg
                msg = "Faculty Name : L36 \n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v1,1,2,msg,1,dict1)
        def d112():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L36\n room no:1001\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v1,1,4,msg,3,dict1)       
        def d113():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L36\n room no:1001\nCL"
                global msg
                msg = "Faculty Name : L36 \n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v1,1,6,msg,5,dict1)             
        def d121():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L36\n room no:1002\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v1,2,2,msg,1,dict2)        
        def d122():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L36\n room no:1002\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v1,2,4,msg,3,dict2)  
        def d123():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L36\n room no:1002\nCL"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L36\n room no:1002\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(v1,2,6,msg,5,dict2)  
        def d131():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L36\n room no:1003\nCL"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L36\n room no:1003\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(v1,3,2,msg,1,dict3)  
        def d132():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L36\n room no:1003\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v1,3,4,msg,3,dict3) 
        def d133():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L36\n room no:1003\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(v1,3,6,msg,5,dict3) 
        def d141():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L36\n room no:1003\nCL"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L36\n room no:1303\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v1,4,2,msg,1,dict4) 
        def d142():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L36\n room no:1004\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v1,4,4,msg,3,dict4)           
        def d143():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L36\n room no:1004\nCL"
                global msg
                msg = "Faculty Name : L36 \n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v1,4,6,msg,5,dict4)      
        def d151():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L36\n room no:1004\nCL"
                global msg
                msg = "Faculty Name : L36 \n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v1,5,2,msg,1,dict5) 
        def d152():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L36\n room no:1005\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v1,5,4,msg,3,dict5) 
        def d153():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L36\n room no:1005\nCL"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L36\n room no:1005\nCL"
                global msg
                msg = "Faculty Name : L36\n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(v1,5,6,msg,5,dict5) 
        f = [[d111,d112,d113],[d121,d122,d123],[d131,d132,d133],[d141,d142,d143],[d151,d152,d153]]
        q = 100
        m = 0
        v = []
        global v1
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = v1[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = v1[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w102():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d211():
            global dict1
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L37\n room no:1006\nCL"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L37\n room no:1006\nCL"
                global msg
                msg = "Faculty Name : L37\n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(v2,1,2,msg,1,dict1)        
        def d212():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L37\n room no:1006\nCL"
                global msg
                msg = "Faculty Name : L37\n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v2,1,4,msg,3,dict1)   
        def d213():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L37\n room no:1006\nCL"
                global msg
                msg = "Faculty Name : L37\n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v2,1,6,msg,5,dict1)       
        def d221():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L37\n room no:1007\nCL"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L37\n room no:1007\nCL"
                global msg
                msg = "Faculty Name : L37 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v2,2,2,msg,1,dict2)      
        def d222():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L37\n room no:1007\nCL"
                global msg
                msg = "Faculty Name : L37 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v2,2,4,msg,3,dict2) 
        def d223():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L37\n room no:1007\nCL"
                global msg
                msg = "Faculty Name : L37\n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v2,2,6,msg,5,dict2) 
        def d231():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L37\n room no:1008\nCL"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L37\n room no:1008\nCL"
                global msg
                msg ="Faculty Name : L37\n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(v2,3,2,msg,1,dict3) 
        def d232():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L37\n room no:1308\nCL"
                global msg
                msg ="Faculty Name : L37\n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v2,3,4,msg,3,dict3) 
        def d233():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L37\n room no:1008\nCL"
                global msg
                msg ="Faculty Name : L37\n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(v2,3,6,msg,5,dict3) 
        def d241():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L37\n room no:1009\nCL"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L37\n room no:1009\nCL"
                global msg
                msg ="Faculty Name : L37\n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v2,4,2,msg,1,dict4) 
        def d242():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L37\n room no:1009\nCL"
                global msg
                msg ="Faculty Name : L37\n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v2,4,4,msg,3,dict4)
        def d243():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L37\n room no:1009\nCL"
                global msg
                msg ="Faculty Name : L37\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v2,4,6,msg,5,dict4)
        def d251():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L37\n room no:1010\nCL"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L37\n room no:1010\nCL"
                global msg
                msg ="Faculty Name : L37 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(v2,5,2,msg,1,dict5)
        def d252():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L37\n room no:1010\nCL"
                global msg
                msg ="Faculty Name : L37 \n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v2,5,4,msg,3,dict5)
        def d253():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L37\n room no:1010\nCL"
                global msg
                msg ="Faculty Name : L37\n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v2,5,6,msg,5,dict5)    
        f = [[d211,d212,d213],[d221,d222,d223],[d231,d232,d233],[d241,d242,d243],[d251,d252,d253]]
        q = 100
        m = 0
        v = []
        global v2
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = v2[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = v2[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w103():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d311():
            global dict1
            if dict1["12:30-1:20"][0]==1:
                clash()
            else:
                dict1["12:30-1:20"][0] = 1
                dict1["12:30-1:20"][1]= "L38\n room no:1106\nCL"
                dict1["1:25-2:15"][0] = 1
                dict1["1:25-2:15"][1]= "L38\n room no:1106\nCL"
                global msg
                msg = "Faculty Name : L38 \n Day order : 1 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(v3,1,2,msg,1,dict1)
        def d312():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L38\n room no:1106\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v3,1,4,msg,3,dict1)
        def d313():
            global dict1
            if dict1["3:10-4:00"][0]==1:
                clash()
            else:
                dict1["3:10-4:00"][0] = 1
                dict1["3:10-4:00"][1]= "L38\n room no:1106\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 1 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(v3,1,6,msg,5,dict1)
        def d321():
            global dict2
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L38\n room no:1107\nCL"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L38\n room no:1107\nCL"
                global msg
                msg = "Faculty Name : L38 \n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v3,2,2,msg,1,dict2)      
        def d322():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L38\n room no:1107\nCL"
                global msg
                msg = "Faculty Name : L38 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v3,2,4,msg,3,dict2) 
        def d323():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L38\n room no:1107\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v3,2,6,msg,5,dict2) 
        def d331():
            global dict3
            if dict3["9:45-10:35"]==1:
                clash()
            else:
                dict3["9:45-10:35"][0] = 1
                dict3["9:45-10:35"][1]= "L38\n room no:308\nCL"
                dict3["10:40-11:30"][0] = 1
                dict3["10:40-11:30"][1]= "L38\n room no:308\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 3 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(v3,3,2,msg,1,dict3)          
        def d332():
            global dict3
            if dict3["11:35-12:25"][0]==1:
                clash()
            else:
                dict3["11:35-12:25"][0] = 1
                dict3["11:35-12:25"][1]= "L38\n room no:1108\nCL"
                global msg
                msg = "Faculty Name : L38 \n Day order : 3 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v3,3,4,msg,3,dict3)  
        def d333():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L38\n room no:1108\nCL"
                global msg
                msg = "Faculty Name : L38 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v3,3,6,msg,5,dict3)  
        def d341():
            global dict4
            if dict4["10:40-11:30"][0]==1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L38\n room no:1109\nCL"
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L38\n room no:1109\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 4 \n Slot time : 10:40-12:25\n click ok to confirm"
                confirm(v3,4,2,msg,1,dict4)          
        def d342():
            global dict4
            if dict4["1:25-2:15"][0]==1:
                clash()
            else:
                dict4["1:25-2:15"][0] = 1
                dict4["1:25-2:15"][1]= "L38\n room no:1109\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 4 \n Slot time : 1:25-2:15\n click ok to confirm"
                confirm(v3,4,4,msg,3,dict4)  
        def d343():
            global dict4
            if dict4["2:20-3:10"][0]==1:
                clash()
            else:
                dict4["2:20-3:10"][0] = 1
                dict4["2:20-3:10"][1]= "L38\n room no:1109\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 4 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v3,4,6,msg,5,dict4)  
        def d351():
            global dict5
            if dict5["8:00-8:50"][0]==1:
                clash()
            else:
                dict5["8:00-8:50"][0] = 1
                dict5["8:00-8:50"][1]= "L38\n room no:1110\nCL"
                dict5["8:50-9:40"][0] = 1
                dict5["8:50-9:40"][1]= "L38\n room no:1110\nCL"
                global msg
                msg = "Faculty Name : L38 \n Day order : 5 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v3,5,2,msg,1,dict5)      
        def d352():
            global dict5
            if dict5["9:45-10:35"][0]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L38\n room no:1110\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v3,5,4,msg,3,dict5)  
        def d353():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L38\n room no:1110\nCL"
                global msg
                msg = "Faculty Name : L38\n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v3,5,6,msg,5,dict5)    
        f = [[d311,d312,d313],[d321,d322,d323],[d331,d332,d333],[d341,d342,d343],[d351,d352,d353]]
        q = 100
        m = 0
        v = []
        global v3
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = v3[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = v3[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w104():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d411():
            if dict1["9:45-10:35"]==1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L39\n room no:1116\nCL"
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L39\n room no:1116\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 1 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(v4,1,2,msg,1,dict1)     
        def d412():
            global dict1
            if dict1["11:35-12:25"][0]==1:
                clash()
            else:
                dict1["11:35-12:25"][0] = 1
                dict1["11:35-12:25"][1]= "L39\n room no:1116\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 1 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v4,1,4,msg,3,dict1) 
        def d413():
            global dict1
            if dict1["2:20-3:10"][0]==1:
                clash()
            else:
                dict1["2:20-3:10"][0] = 1
                dict1["2:20-3:10"][1]= "L39\n room no:1116\nCL"
                global msg
                msg = "Faculty Name : L39 \n Day order : 1 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v4,1,6,msg,5,dict1)  
        def d421():
            global dict1
            if dict2["8:00-8:50"][0]==1:
                clash()
            else:
                dict2["8:00-8:50"][0] = 1
                dict2["8:00-8:50"][1]= "L39\n room no:1117\nCL"
                dict2["8:50-9:40"][0] = 1
                dict2["8:50-9:40"][1]= "L39\n room no:1117\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 2 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v4,2,2,msg,1,dict2)        
        def d422():
            global dict2
            if dict2["9:45-10:35"][0]==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L39\n room no:1117\nCL"
                global msg
                msg = "Faculty Name : L39 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v4,2,4,msg,3,dict2)   
        def d423():
            global dict2
            if dict2["11:35-12:25"][0]==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L39\n room no:1117\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 2 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v4,2,6,msg,5,dict2)
        def d431():
            global dict2
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L39\n room no:1118\nCL"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L39\n room no:1118\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(v4,3,2,msg,1,dict3)
        def d432():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L39\n room no:1118\nCL"
                global msg
                msg = "Faculty Name : L39 \n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v4,3,4,msg,3,dict3)
        def d433():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L39\n room no:1118\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 3 \n Slot time : 3:10-4:00\n click ok to confirm"
                confirm(v4,3,6,msg,5,dict3)
        def d441():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1]= "L39\n room no:1119\nCL"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1]= "L39\n room no:1119\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v4,4,2,msg,1,dict4)   
        def d442():
            global dict4
            if dict4["9:45-10:35"][0]==1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L39\n room no:1119\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v4,4,4,msg,3,dict4) 
        def d443():
            global dict4
            if dict4["11:35-12:25"][0]==1:
                clash()
            else:
                dict4["11:35-12:25"][0] = 1
                dict4["11:35-12:25"][1]= "L39\n room no:1119\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 4 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v4,4,6,msg,5,dict4) 
        def d451():
            global dict5
            if dict5["9:45-10:35"]==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L39\n room no:1120\nCL"
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L39\n room no:1320\nCL"
                global msg
                msg = "Faculty Name : L39 \n Day order : 5 \n Slot time : 9:45-11:30\n click ok to confirm"
                confirm(v4,5,2,msg,1,dict5)         
        def d452():
            global dict5
            if dict5["11:35-12:25"][0]==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L39\n room no:1120\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 5 \n Slot time : 11:35-12:25\n click ok to confirm"
                confirm(v4,5,4,msg,3,dict5) 
        def d453():
            global dict5
            if dict5["2:20-3:10"][0]==1:
                clash()
            else:
                dict5["2:20-3:10"][0] = 1
                dict5["2:20-3:10"][1]= "L39\n room no:1120\nCL"
                global msg
                msg = "Faculty Name : L39\n Day order : 5 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v4,5,6,msg,5,dict5)  
        f = [[d411,d412,d413],[d421,d422,d423],[d431,d432,d433],[d441,d442,d443],[d451,d452,d453]]
        q = 100
        m = 0
        v = []
        global v4
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = v4[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = v4[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)
    def w105():
        r = Toplevel(s)
        r.title("new window")
        r.geometry("1500x800")
        def d511():
            global dict1
            if dict1["8:00-8:50"][0]==1:
                clash()
            else:
                dict1["8:00-8:50"][0] = 1
                dict1["8:00-8:50"][1] = "L40\n room no:915\nCL"
                dict1["8:50-9:40"][0] = 1
                dict1["8:50-9:40"][1] = "L40\n room no:915\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 1 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v5,1,2,msg,1,dict1)
        def d512():
            global dict1
            if dict1["9:45-10:35"][0] == 1:
                clash()
            else:
                dict1["9:45-10:35"][0] = 1
                dict1["9:45-10:35"][1]= "L40\n room no:915\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 1 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v5,1,4,msg,3,dict1)           
        def d513():
            global dict1
            if dict1["10:40-11:30"][0] == 1:
                clash()
            else:
                dict1["10:40-11:30"][0] = 1
                dict1["10:40-11:30"][1]= "L40\n room no:915\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 1 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v5,1,6,msg,5,dict1)             
        def d521():
            global dict2
            if dict2["9:45-10:35"][0] ==1:
                clash()
            else:
                dict2["9:45-10:35"][0] = 1
                dict2["9:45-10:35"][1]= "L40\n room no:914\nCL"
                global msg
                msg = "Faculty Name : L40 \n Day order : 2 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v5,2,2,msg,1,dict2)  
        def d522():
            global dict2
            if dict2["10:40-11:30"][0]==1:
                clash()
            else:
                dict2["10:40-11:30"][0] = 1
                dict2["10:40-11:30"][1]= "L40\n room no:914\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 2 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v5,2,4,msg,3,dict2)  
        def d523():
            global dict2
            if dict2["11:35-12:25"][0] ==1:
                clash()
            else:
                dict2["11:35-12:25"][0] = 1
                dict2["11:35-12:25"][1]= "L40\n room no:914\nCL"
                dict2["12:30-1:20"][0]=1
                dict2["12:30-1:20"][0]= "L40\n room no:914\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 2 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(v5,2,6,msg,5,dict2)
        def d531():
            global dict3
            if dict3["12:30-1:20"][0]==1:
                clash()
            else:
                dict3["12:30-1:20"][0] = 1
                dict3["12:30-1:20"][1]= "L40\n room no:913\nCL"
                dict3["1:25-2:15"][0] = 1
                dict3["1:25-2:15"][1]= "L40\n room no:903\nCL"
                global msg
                msg = "Faculty Name : L40 \n Day order : 3 \n Slot time : 12:30-2:15\n click ok to confirm"
                confirm(v5,3,2,msg,1,dict3)
        def d532():
            global dict3
            if dict3["2:20-3:10"][0]==1:
                clash()
            else:
                dict3["2:20-3:10"][0] = 1
                dict3["2:20-3:10"][1]= "L40\n room no:913\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 3 \n Slot time : 2:20-3:10\n click ok to confirm"
                confirm(v5,3,4,msg,3,dict3)
        def d533():
            global dict3
            if dict3["3:10-4:00"][0]==1:
                clash()
            else:
                dict3["3:10-4:00"][0] = 1
                dict3["3:10-4:00"][1]= "L40\n room no:913\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 3 \n Slot time : 3:15-4:00\n click ok to confirm"
                confirm(v5,3,6,msg,5,dict3)
        def d541():
            global dict4
            if dict4["8:00-8:50"][0]==1:
                clash()
            else:
                dict4["8:00-8:50"][0] = 1
                dict4["8:00-8:50"][1] = "L40\n room no:912\nCL"
                dict4["8:50-9:40"][0] = 1
                dict4["8:50-9:40"][1] = "L40\n room no:912\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 4 \n Slot time : 8:00-9:40\n click ok to confirm"
                confirm(v5,4,2,msg,1,dict4)
        def d542():
            global dict4
            if dict4["9:45-10:35"][0] == 1:
                clash()
            else:
                dict4["9:45-10:35"][0] = 1
                dict4["9:45-10:35"][1]= "L40\n room no:912\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 4 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v5,4,4,msg,3,dict4)        
        def d543():
            global dict4
            if dict4["10:40-11:30"][0] == 1:
                clash()
            else:
                dict4["10:40-11:30"][0] = 1
                dict4["10:40-11:30"][1]= "L40\n room no:912\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 4 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v5,4,6,msg,5,dict4)       
        def d551():
            global dict5
            if dict5["9:45-10:35"][0] ==1:
                clash()
            else:
                dict5["9:45-10:35"][0] = 1
                dict5["9:45-10:35"][1]= "L40\n room no:911\nCL"
                global msg
                msg = "Faculty Name : nCL\n Day order : 5 \n Slot time : 9:45-10:35\n click ok to confirm"
                confirm(v5,5,2,msg,1,dict5)            
        def d552():
            global dict5
            if dict5["10:40-11:30"][0]==1:
                clash()
            else:
                dict5["10:40-11:30"][0] = 1
                dict5["10:40-11:30"][1]= "L40\n room no:911\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 5 \n Slot time : 10:40-11:30\n click ok to confirm"
                confirm(v5,5,4,msg,3,dict5)  
        def d553():
            global dict5
            if dict5["11:35-12:25"][0] ==1:
                clash()
            else:
                dict5["11:35-12:25"][0] = 1
                dict5["11:35-12:25"][1]= "L40\n room no:911\nCL"
                dict5["12:30-1:20"][0]=1
                dict5["12:30-1:20"][0]= "L40\n room no:911\nCL"
                global msg
                msg = "Faculty Name : L40\n Day order : 5 \n Slot time : 11:35-1:20\n click ok to confirm"
                confirm(v5,5,6,msg,5,dict5)  
        f = [[d511,d512,d513],[d521,d522,d523],[d531,d532,d533],[d541,d542,d543],[d551,d552,d553]]
        q = 100
        m = 0
        v = []
        global v5
        for i in range(6):
            h = []
            for j in range(8):
                h.append("")  
            v.append(h) 
        for i in range(6):
            p = 200
            n=0
            for j in range(8):
                if j%2 == 1 and i !=0 and j != 7:
                    v[i][j] = Button(r,text = v5[i][j],width = 20,fg = "red",font = ("Arial",10,"bold"),command=f[m][n])
                    n+=1
                else:
                    v[i][j] = Label(r,text = v5[i][j],width = 20,fg = "blue",font = ("Arial",10,"bold"))
                v[i][j].place(x = p,y = q)
                p+=150
            
            q+=50
            if i !=0:
                m+=1
        def de():
            r.destroy()
        bb = Button(r,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
        bb.place(x = 30,y = 700)

    w = [w101,w102,w103,w104,w105]
    u = 0
    p = 100
    for i in range(6):
        q = 300
        for j in range(5):
            if j == 3 and i != 0:
                e = Button(s,text = f"{a[i][j]}",width = 30,fg = "red",font = ("Arial",10,"bold"),command=w[u])
                u+=1
            else:
                e = Label(s,text = f"{a[i][j]}",width = 30,fg = "blue",font = ("Arial",10,"bold"))
            e.place(x = q,y = p)
            q+=180
        p+=50
    def de():
        s.destroy()
    bb = Button(s,text = "< back",fg = "Black",font = ("Arial",10,"bold"),command=de)
    bb.place(x = 30,y = 700)
def w2():
    s = Toplevel(root)
    s.title("new window")
    s.geometry("1500x800")
    l = Label(s,text = "Register the following courses of 5th semester",fg = "red",font = ("Arial",20,"bold"))
    l.place(x = 500,y =50)
    def a():
        s.destroy()
    b = Button(s,text = "   Compiler design  ",fg = "red",font = ("Courier",10,"bold"),command = w3)
    b.place(x = 550,y = 140)
    b = Button(s,text = "        DBMS        ",fg = "red",font = ("Courier",10,"bold"),command = w4)
    b.place(x = 750,y = 140)
    b = Button(s,text = " Computer Networks  ",fg = "red",font = ("Courier",10,"bold"),command = w5)
    b.place(x = 550,y = 200)
    b = Button(s,text = "  operating system  ",fg = "red",font = ("Courier",10,"bold"),command = w6)
    b.place(x = 750,y = 200)
    b = Button(s,text = "     Algorithms     ",fg = "red",font = ("Courier",10,"bold"),command = w7)
    b.place(x = 550,y = 260)
    b = Button(s,text = "Discerete mathematics",fg = "red",font = ("Courier",10,"bold"),command = w8)
    b.place(x = 750,y = 260)
    b = Button(s,text = "   Automata Theory   ",fg = "red",font = ("Courier",10,"bold"),command = w9)
    b.place(x = 550,y = 320)
    b = Button(s,text = " Computational logic ",fg = "red",font = ("Courier",10,"bold"),command = w10)
    b.place(x = 750,y = 320)
    b = Button(s,text = "Previous",bg = "cyan",command=a)
    b.place(x = 650,y= 700)
    b = Button(s,text = "Next",bg = "cyan",command=a)
    b.place(x = 720,y= 700)
    global count
def TT():
    s = Tk()
    s.geometry("1500x1000")
    l = Label(s,text = "Here is your day wise class schedule for upcoming semester",fg = "red",font = ("Arial",21,"bold"))
    l.place(x = 200,y = 50)
    Label(s,text = "",width = 18).grid(row = 0,column = 0)
    Label(s,text = "",width = 18).grid(row = 1,column = 0)
    Label(s,text = "",width = 18).grid(row = 2,column = 0)
    Label(s,text = "",width = 18).grid(row = 3,column = 0)
    Label(s,text = "",width = 18).grid(row = 4,column = 0)
    Label(s,text = "",width = 18).grid(row = 5,column = 0)
    Label(s,text = "",width = 18).grid(row = 6,column = 0)
    Label(s,text = "",width = 18).grid(row = 7,column = 0)
    l = Label(s,text = f"Hi {kk.get()[:-10]},",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 20,y = 0)
    tt = [["Day","8:00-8:50","8:50-9:40","9:45-10:35","10:40-11:30","11:35-12:25","12:30-1:20","1:25-2:15","2:20-3:10","3:10-4:00","4:00-4:50"]]
    a = ["Day order 1"]
    for i in dict1.keys():
        if dict1[i][0] == 1:
            a.append(dict1[i][1])
            a[-1] = a[-1].replace("\n","-")
            dict1[i] = [0,""]
        else:
            a.append("null")
    tt.append(a)
    a = ["Day order 2"]
    for i in dict2.keys():
        if dict2[i][0] == 1:
            a.append(dict2[i][1])
            a[-1] = a[-1].replace("\n","-")
            dict2[i] = [0,""]
        else:
            a.append("null")
    tt.append(a)
    a = ["Day order 3"]
    for i in dict3.keys():
        if dict3[i][0] == 1:
            a.append(dict3[i][1])
            a[-1] = a[-1].replace("\n","-")
            dict3[i] = [0,""]
        else:
            a.append("null")
    tt.append(a)
    a = ["Day order 4"]
    for i in dict4.keys():
        if dict4[i][0] == 1:
            a.append(dict4[i][1])
            a[-1] = a[-1].replace("\n","-")
            dict4[i] = [0,""]
        else:
            a.append("null")
    tt.append(a)
    a = ["Day order 5"]
    for i in dict5.keys():
        if dict5[i][0] == 1:
            a.append(dict5[i][1])
            a[-1] = a[-1].replace("\n","-")
            dict5[i] = [0,""]
        else:
            a.append("null")
    tt.append(a)
    x = tt
    for i in range(6):
        for j in range(11):
            if i == 0 or j == 0:
                g = "blue"
                e = Entry(s,width = 15,bg = g,font = ("Arial",15,"bold"))
            else:
                g = "green"
            if x[i][j] == "null":
                k = "0"
                g = "white"
                e = Entry(s,width = 15,bg = g,font = ("Arial",12,"bold"))
            else:
                k = x[i][j]
                k = k.replace(" room no:"," ")
                k = "    "+k
                e = Entry(s,width = 15,bg = g,font = ("Arial",12,"bold"))
            e.insert(END,k)
            e.grid(row = i+8,column = j)
    for i in range(6):
        tt[i] = ",".join(tt[i])+"\n"
    with open(f"{kk.get()[:-10]}-tt.txt","w") as f:
        f.writelines(tt)
    with open("slots.txt","r+") as f:
        f.truncate()
    b = b1+b2+b3+b4+b5
    for i in range(30):
        for j in range(8):
            b[i][j] = str(b[i][j])
    def ar():
        root.destroy()
        s.destroy()
    Button(s,text = "EXIT",bg = "red",command = ar).place(x = 1460,y = 700)
    for i in range(30):
        b[i] = ",".join(b[i])+"\n"
    with open("slots.txt","w") as f:
        for i in b:
            f.writelines(i)
    s.mainloop()
def w1():
        s1 = Toplevel(root)
        s1.title("new window")
        s1.geometry("1500x800")
        if count <20:
            l = Label(s1,text = f"Hi {kk.get()[:-10]},",fg = "red",font = ("Arial",25,"bold"))
            l.place(x = 40,y = 10)
            l = Label(s1,text = "we are looking for you",fg = "red",font = ("Arial",20,"bold"))
            l.place(x = 100,y =50)
            def a():
                global jj
                jj.config(text = "")
                s1.destroy()
            b = Button(s1,text = "Click Here",fg = "red",font = ("Courier",10,"bold"),command = w2)
            b.place(x = 100,y=100)
            l = Label(s1,text = "to enroll for next semester",fg = "blue",font = ("Courier",15,"bold"))
            l.place(x = 210,y = 100)
            b = Button(s1,text = "Home",bg = "cyan",command=a)
            b.place(x = 700,y= 700)
        else:           
            cc = Canvas(s1,width=700,height = 400,bg = "orange",highlightthickness=0)
            pp = PhotoImage(file = "scrpi.png")
            cc.create_image(350,200,image = pp)
            cc.place(x = 450,y = 150)
            l = Label(s1,text = "You are enrolled all the assigned courses of this semster",fg = "orange",font = ("Arial",20,"bold"))
            l.place(x = 210,y = 50)
            b = Button(s1,text = "Generate TimeTable",bg = "green",font = ("Arial",12,"bold"),command = TT)
            b.place(x = 1050,y=50 )
            b = Button(s1,text = "Home",bg = "cyan",command = a)
            b.place(x = 700,y= 700)
global count
count = 0
global id
id = ""
global kk
c = Canvas(root,width=400,height = 450,bg = "white",highlightthickness=0)
p = PhotoImage(file = "loginpage2.png")
c.create_image(200,260,image = p)
c.place(x = 550,y = 150)
l = Label(root,text = "LOGIN",fg = "Teal", font = ("Arial",20,"bold"))
l.place(x = 560,y = 160)
l = Label(root,text = "EMAIL ID",fg = "Teal", font = ("Arial",15,"bold"))
l.place(x = 575,y = 350)
kk = Entry(width = 30,bg = "white",font = ("Arial",10,"bold"))
kk.place(x = 575,y = 380)
l = Label(root,text = "Password",fg = "Teal", font = ("Arial",15,"bold"))
l.place(x = 575,y = 430)
i = Entry(root,show = "*",width = 30,bg = "white",font = ("Arial",10,"bold"))
i.place(x = 575,y = 465)
def tg():
    s1 = Toplevel(root)
    s1.title("new window")
    s1.geometry("1500x800")
    with open(f"{kk.get()[:-10]}-tt.txt") as f:
        d = f.readlines()
    x = []
    for i in d:
        y = i[:-1].split(",")
        x.append(y)
    l = Label(s1,text = "Here is your day wise class schedule for upcoming semester",fg = "red",font = ("Arial",21,"bold"))
    l.place(x = 200,y = 40)
    Label(s1,text = "",width = 18).grid(row = 0,column = 0)
    Label(s1,text = "",width = 18).grid(row = 1,column = 0)
    Label(s1,text = "",width = 18).grid(row = 2,column = 0)
    Label(s1,text = "",width = 18).grid(row = 3,column = 0)
    Label(s1,text = "",width = 18).grid(row = 4,column = 0)
    Label(s1,text = "",width = 18).grid(row = 5,column = 0)
    Label(s1,text = "",width = 18).grid(row = 6,column = 0)
    Label(s1,text = "",width = 18).grid(row = 7,column = 0)
    l = Label(s1,text = f"Hi {kk.get()[:-10]},",fg = "red",font = ("Arial",25,"bold"))
    l.place(x = 20,y = 0)
    for i in range(6):
        for j in range(11):
            if i == 0 or j == 0:
                g = "blue"
                e = Entry(s1,width = 15,bg = g,font = ("Arial",15,"bold"))
            else:
                g = "green"
            if x[i][j] == "null":
                k = "0"
                g = "white"
                e = Entry(s1,width = 15,bg = g,font = ("Arial",12,"bold"))
            else:
                k = x[i][j]
                k = k.replace(" room no:"," ")
                k = "    "+k
                e = Entry(s1,width = 15,bg = g,font = ("Arial",12,"bold"))
            e.insert(END,k)
            e.grid(row = i+8,column = j)
    def tr():
        root.destroy()
    Button(s1,text = "EXIT",bg = "red",command = tr).place(x = 1460,y = 700)

def ma():
    try:
        try:
            with open("scrp.txt") as f:
                a = f.read()
            a = a.split(",")
        except FileNotFoundError:
            a = []
        id = kk.get()[:-9]
        if kk.get() in a:
            tg()
        elif dict[kk.get()] == i.get():
            print(id)
            try:
                with open("scrp.txt") as f:
                    a = f.read()
                a+=","+kk.get()
            except FileNotFoundError:
                a = kk.get()
            with open("scrp.txt","w") as f:
                f.write(a)

            global jj
            jj = Label(root,text = "Login successfull",fg = "Lime",font = ("Arial",15,"bold"))
            jj.place(x = 590,y = 640)
            w1()
        else:
            Label(root,text = "Invalid Password",fg = "Red",font = ("Arial",15,"bold")).place(x = 590,y = 640)
    except KeyError:
            Label(root,text = "Invalid Email id",fg = "Red",font = ("Arial",15,"bold"),highlightthickness=0).place(x = 590,y = 640)
b = Button(root,text = "Login",bg = "Turquoise",font = ("Arial",17,"bold"),command = ma)
b.place(x = 710,y=558 )

root.mainloop()