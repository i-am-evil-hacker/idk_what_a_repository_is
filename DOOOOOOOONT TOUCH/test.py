import time
for i in range(5):
    print("-"*10)
    print("|"+("0"*i)+" "*(8-i)+"|")
    print("_"*10)
    print("\n"*3)
    time.sleep(0.5)