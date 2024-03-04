Label_Number="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Label=input(str())
Number=0
for i in range(1,len(Label)+1):
    Value=int((Label_Number.index(Label[-i])+1)*((26)**(i-1)))
    Number=Number+Value
print(Number,end="")
