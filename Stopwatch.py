from tkinter import *
from datetime import datetime
import time


running=False
starttime=None
class stopwat:
    def __init__(self,root):
        self.root=root
        self.root.title("StopWatch")
        self.root.geometry("400x150")
        self.root.resizable(0,0)
        #self.root.iconbitmap("polygon.ico")

        txt_var=StringVar()
        txt_var.set("00.00")

       


        #=======================hower_on_button
        def on_enter1(e):
            But_start['background']="black"
            But_start['foreground']="cyan"
  
        def on_leave1(e):
            But_start['background']="SystemButtonFace"
            But_start['foreground']="SystemButtonText"

        def on_enter2(e):
            But_pause['background']="black"
            But_pause['foreground']="cyan"
  
        def on_leave2(e):
            But_pause['background']="SystemButtonFace"
            But_pause['foreground']="SystemButtonText"


        def on_enter3(e):
            But_resume['background']="black"
            But_resume['foreground']="cyan"
  
        def on_leave3(e):
            But_resume['background']="SystemButtonFace"
            But_resume['foreground']="SystemButtonText"

        def on_enter4(e):
            But_clear['background']="black"
            But_clear['foreground']="cyan"
  
        def on_leave4(e):
            But_clear['background']="SystemButtonFace"
            But_clear['foreground']="SystemButtonText"
        
        #=============================================================

        def run():
            current_time=datetime.now()
            diff=current_time - starttime
            txt_var.set("%d:%02d"%(diff.seconds,diff.microseconds//100000))

            if running:
                self.root.after(10,run)

        

       
            
            
        


        def start():
            global running
            global starttime
            if not running:
                running=True
                starttime=datetime.now()
                self.root.after(10,run)
            
            But_start.config(state="disable")
            But_resume.config(state="disable")

        def pause():
            global running
            running=False
            

            But_start.config(state="disable")
            But_pause.config(state="disable")
            But_resume.config(state="normal")
            

        def resume():
            global running
            #global starttime
            if not running:
                running=True
                starttime=datetime.now()
                self.root.after(10,run)              

            
            But_start.config(state="disable")
            But_pause.config(state="normal")
            But_resume.config(state="disable")

        def clear():
            global running
            running=False
            txt_var.set("0.00")
          

            But_start.config(state="normal")
            But_pause.config(state="normal")
        
            
            #Hours_combo.set("Hours")
            #Minutes_combo.set("Minutes")
            #Seconds_combo.set("Seconds")


        #=============Frame==========================
        Main_Frame=Frame(self.root,width=400,height=150,relief=RIDGE,bd=3,bg="black")
        Main_Frame.place(x=0,y=0)

        Frame_top=Frame(self.root,width=395,height=70,relief=RIDGE,bg="#168f8c",bd=3)
        Frame_top.place(x=2,y=3)

        Frame_bottom=Frame(self.root,width=395,height=75,relief=RIDGE,bg="#a91642",bd=3)
        Frame_bottom.place(x=2,y=73)
        #==================Frmae_top
        label=Label(Frame_top,textvariable=txt_var,font=("times new roman",30,"bold"),fg="white",bg="#168f8c")
        label.place(x=150,y=5)
        
           
        
        
        

        #=============================================================================
        But_start=Button(Frame_bottom,text="Start",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=start)
        But_start.place(x=10,y=15)
        But_start.bind("<Enter>",on_enter1)
        But_start.bind("<Leave>",on_leave1)

        But_pause=Button(Frame_bottom,text="Pause",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=pause)
        But_pause.place(x=100,y=15)
        But_pause.bind("<Enter>",on_enter2)
        But_pause.bind("<Leave>",on_leave2)

        But_resume=Button(Frame_bottom,text="Resume",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=resume)
        But_resume.place(x=210,y=15)
        But_resume.bind("<Enter>",on_enter3)
        But_resume.bind("<Leave>",on_leave3)

        But_clear=Button(Frame_bottom,text="Clear",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=clear)
        But_clear.place(x=300,y=15)
        But_clear.bind("<Enter>",on_enter4)
        But_clear.bind("<Leave>",on_leave4)






if __name__ == "__main__":
    root=Tk()
    app=stopwat(root)
    root.mainloop()
