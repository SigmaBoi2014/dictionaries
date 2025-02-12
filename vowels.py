b=input("enter a word")
b=b.lower()
print(b)
vowels={"a":0,"i":0,"e":0,"o":0,"u":0}
for i in b:
    print(i)
    if i in vowels:
        vowels[i]+=1
print(vowels)