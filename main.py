from calc import add,mult,div,sub

n1 = float(input("enter your first number: "))
n2 = float(input("enter your second number: "))
inp = input("Enter your Command ")
while(inp.lower()!="stop"):
    if(inp.lower()=="add"):
        sum = add(n1,n2)
        print(n1,"+",n2,"=",sum)
    elif(inp.lower()=="sub"):
        diff = sub(n1,n2)
        print(n1,"-",n2,"=",diff)
    elif(inp.lower()=="mult"):
        pro = mult(n1,n2)
        print(n1,"x",n2,"=",pro)
    elif(inp.lower()=="div"):
        if(n2==0):
            print("cannot divide by zero")
        else:
            div = div(n1,n2)
            print(n1,"/",n2,"=",div)
    else:
        print("Unknown Command")
    print("If you want to do another operation enter yes, if you want to close the program enter stop")
    ch = input("Enter your Choice ")
    if(ch.lower()=="yes"):
        n1 = float(input("enter your first number: "))
        n2 = float(input("enter your second number: "))
        inp = input("Enter your Command ")
    else:
        break
    