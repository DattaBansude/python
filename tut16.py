#list = ("datta", "tanu", "bhavdya","trushna")
#for item in list:
   # print(item)
#list = [["datta",2], ["tanu",3], ["bhavdya",5],["trushna",1]]
#for item, jevan in list:
  #  print(item,"itkya vela jevan karto",jevan)
#list = [["datta", 2], ["tanu", 3], ["bhavdya", 5], ["trushna", 1]]
#dict = dict(list)
#for item, jevan in dict.items():
 #       print(item, "itkya vela jevan karto", jevan)
items = [int, float,"datta","tanu",3,4,5,6,8,9,10,45,67,23,56]

for item in items:
     if str(item).isnumeric() and item>=8:
         print(item)
