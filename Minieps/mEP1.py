x = float(input())
op = input()
y = float(input())

if op == "+":
    print(x,op,y,"=",x+y)   
elif op == "-":
    print(x,op,y,"=",x-y)
elif op == "*":
    print(x,op,y,"=",x*y)
elif op == "//":
    if y!=0:
        print(x,op,y,"=",x//y)
    else:
        print("Divisao por 0!")           
elif op == "**":
    print(x,op,y,"=",x**y)
elif op == "%":   
    if y!=0:
        print(x,op,y,"=",x%y)
    else:
        print("Divisao por 0!")
else:
    print("Operacao nao reconhecida!")