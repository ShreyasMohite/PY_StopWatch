





from tkinter import *
from datetime import datetime
import time


running=False
starttime=None




class Stopwatch:
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
            but_start['background']="black"
            but_start['foreground']="cyan"  
        def on_leave1(e):
            but_start['background']="SystemButtonFace"
            but_start['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_pause['background']="black"
            but_pause['foreground']="cyan"            
        def on_leave2(e):
            but_pause['background']="SystemButtonFace"
            but_pause['foreground']="SystemButtonText"




        def on_enter3(e):
            but_resume['background']="black"
            but_resume['foreground']="cyan"  
        def on_leave3(e):
            but_resume['background']="SystemButtonFace"
            but_resume['foreground']="SystemButtonText"

            

        def on_enter4(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave4(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




            
        
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
            
            but_start.config(state="disable")
            but_resume.config(state="disable")

        def pause():
            global running
            running=False
            

            but_start.config(state="disable")
            but_pause.config(state="disable")
            but_resume.config(state="normal")
            

        def resume():
            global running
            #global starttime
            if not running:
                running=True
                starttime=datetime.now()
                self.root.after(10,run)              

            
            but_start.config(state="disable")
            but_pause.config(state="normal")
            but_resume.config(state="disable")

        def clear():
            global running
            running=False
            txt_var.set("0.00")
          

            but_start.config(state="normal")
            but_pause.config(state="normal")
        
            
            #Hours_combo.set("Hours")
            #Minutes_combo.set("Minutes")
            #Seconds_combo.set("Seconds")


        #=============Frame==========================


            
        main_frame=Frame(self.root,width=400,height=150,relief=RIDGE,bd=3,bg="black")
        main_frame.place(x=0,y=0)

        frame_top=Frame(self.root,width=395,height=70,relief=RIDGE,bg="#168f8c",bd=3)
        frame_top.place(x=2,y=3)

        frame_bottom=Frame(self.root,width=395,height=75,relief=RIDGE,bg="#a91642",bd=3)
        frame_bottom.place(x=2,y=73)


        
        #==================Frmae_top
        label_frame=Label(frame_top,textvariable=txt_var,font=("times new roman",30,"bold"),fg="white",bg="#168f8c")
        label_frame.place(x=150,y=5)
        
           
        
        
        

        #=============================================================================



        
        but_start=Button(frame_bottom,text="Start",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=start)
        but_start.place(x=10,y=15)
        but_start.bind("<Enter>",on_enter1)
        but_start.bind("<Leave>",on_leave1)

        but_pause=Button(frame_bottom,text="Pause",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=pause)
        but_pause.place(x=100,y=15)
        but_pause.bind("<Enter>",on_enter2)
        but_pause.bind("<Leave>",on_leave2)

        but_resume=Button(frame_bottom,text="Resume",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=resume)
        but_resume.place(x=210,y=15)
        but_resume.bind("<Enter>",on_enter3)
        but_resume.bind("<Leave>",on_leave3)

        but_clear=Button(frame_bottom,text="Clear",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=clear)
        but_clear.place(x=300,y=15)
        but_clear.bind("<Enter>",on_enter4)
        but_clear.bind("<Leave>",on_leave4)






if __name__ == "__main__":
    root=Tk()
    app=Stopwatch(root)
    root.mainloop()



