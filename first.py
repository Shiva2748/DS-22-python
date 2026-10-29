def fun(a,b,c):
    for num in str(a):
        if num in str(b) and num in str(c):
            num=int(num)
            print(type(num))
            return num
            
    return -1

a=int(input())
b=int(input())
c=int(input())
print(fun(a,b,c))
