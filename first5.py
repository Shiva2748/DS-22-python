str1=input("Enter any string")
c=0
for ch in str1:
    if ch in "aeiouAEIOU":
        c+=1
print("count of vowels:", c)        
        
