import sys,time
frames=list("abcdefghijklmnoqrstuvwxyz")
def animate(frames,cd):
    frames=frames[::-1]
    for i in range(len(frames)):
        sys.stdout.write((" "*(len(frames)-i))+frames[i]+"\r")
        sys.stdout.flush()
        time.sleep(cd)
while True:
    animate(frames,0.1)