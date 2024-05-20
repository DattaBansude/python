#faulty calculator
print("enter first number")
num1 = int(input())
print("enter second number")
num2 = int(input())
print("so what you want?/n" "+, -, *, /,%")
num3 = input()

if num1==5 and num2==10 and num3=="+":
    print("34")
elif num1==44 and num2==24 and num3=="-":
    print(0)
elif num1==2 and num2==3 and num3=="/":
    print(50)
elif num1==4 and num2==5 and num3=="*":
    print("25")
elif num3=="+":
    num4=num1+num2
    print(num4)
elif num3=="*":
    mul=num1*num2
    print(mul)
elif num3=="/":
    div=num1/num2
    print(div)
elif num3=="%":
    mod=num1%num2
    print(mod)
elif num3=="-":
    sub=num1-num2
    print(sub)
else:
    print("error! please check your input")

