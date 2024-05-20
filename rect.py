#def print2(str1):
 #   print2(str1)
  #  print("this is " + str1)

#print2("datta")
def factorial(n):#iterative
    #fac = 1
   # for i in range(n):
  #      fac = fac * (i+1)
 #   return fac
  #  """
   #      :param n: integer
     #    :return: n * n-1 * n-2 * n-3........1
   # """
    # pass
#number = int(input("enter any number\n"))
#print("factorial is : ", factorial(number))
#def print2(str1):
 #   print2(str1)
  #  print("this is " + str1)

#print2("datta")



#recursive
    if n == 1:
       return 1
    else:
        return n * factorial(n-1)
    # pass
number = int(input("enter any number\n"))
print("factorial is : ", factorial(number))