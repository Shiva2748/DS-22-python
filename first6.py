str1=input("Enter any string")
ac=0
dc=0
sc=0
for ch in str1:
    if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1
    else:
        sc+=1
print("Alphabet count:", ac)
print("Digit count:", dc)
print("Special character count:", sc)
