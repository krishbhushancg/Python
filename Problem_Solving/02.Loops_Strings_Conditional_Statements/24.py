text=input("enter sentence: ").split()
secret_word=input("enter secret word: ")
count=0
for i in text:
    print(i)
    if i==secret_word:
        count+=1
        print(f"starting position: {i+1}")
    else:
        print("secret word not found")
print(f"secret word appeared {count} times")

