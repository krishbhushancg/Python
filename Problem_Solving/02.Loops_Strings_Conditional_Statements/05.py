sentence=input("enter sentence: ").split()
for i in sentence:
    if len(i)<=3:
        print(f"word:{i} length: Short")
    elif len(i)>=4 and len(i)<=6:
        print(f"word:{i} length: Medium")
    else:
        print(f"word:{i} length: Long")
