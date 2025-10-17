import winsound as w
l=list("abcdefghijklmnopqrstuvwxyz")
import sys 
import time
def animate(frames:list,fps:float=60,Title:bool=False):
    a=0
    new=False
    if not Title:
        while True:
            if new:
                print()
                new=False
            for i in range(len(frames)):
                s.stdout.write((" "*(i-a))+(frames[i-a])+("\r"))
                s.stdout.flush()
                w.Beep(500,100)
                time.sleep(1/fps)
            a+=1
            if a==len(frames):
                a=0
                new=True
    else:
        while True:
            for i in range(len(frames)):
                a=len(frames)-1
                #for alternate animation ie,|\-/ at the same time at diff animate times ig
frames = ["[=     ]", "[ =    ]", "[  =   ]", "[   =  ]", "[    = ]", "[     =]", "[    = ]", "[   =  ]", "[  =   ]", "[ =    ]"]
def animate1(txt:str=" Hello World! ",cd:float=0.1,number_of_times:int=10,dir:str="left"):
    try:
        while True:
            sys.stdout.write("\t\t\t"+(txt*number_of_times) + "\r")
            sys.stdout.flush()
            time.sleep(0.1)
            if dir=="left":
                txt=txt[1:]+txt[0]
            elif dir=="right":
                txt=txt[-1]+txt[:-1]
    except KeyboardInterrupt:
        print("\nAnimation Stopped.")  
animate1()