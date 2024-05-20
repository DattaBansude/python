#l =10 #global variable
#def function1(n):
    #l = 5#local variable
   # m = 8#local variable
  #  print(l, m)
 #   print(n, "i have printed")
#function1("this is me")
#print(l)
#l =10 #global variable
#def function1(n):
    #l = 5#local variable
 #   m = 8#local variable
  #  global l
   # l = l+45
    #print(l, m)
    #print(n, "i have printed")
#function1("this is me")
#print(l)
x = 55
def datta():
    x = 20
    def vaibhav():
        global x
        x = 30
   # print("before calling vaibhav", x)
    vaibhav()
    print("after calling vaibhav", x)
datta()
print(x)
