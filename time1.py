import time
initial = time.time()
#print(initial)
i = 0
while i<45 :
    print("DATTA IS GOOD BOY")
    i+=1
print("while loop run time:", time.time() - initial,"second")
initial1 = time.time()
for i in range(30):
    print("datta is handsome")
print("for loop run time:", time.time()-initial1,"second")
localtime =  time.asctime(time.localtime(time.time()))
print(localtime)