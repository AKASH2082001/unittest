def Add(x,y):
    return x+y
def Sub(x,y):
    return x-y
def Mul(x,y):
    return x*y
def Div(x,y):
    return x/y

if __name__ == "__main__":
    a = int(input("enter the value of a"))
    b = int(input("enter the value of b"))

    add = Add(a, b)
    print(add)
    sub = Sub(a, b)
    print(sub)
    mul = Mul(a, b)
    print(mul)
    div = Div(a, b)
    print(div)