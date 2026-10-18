# Q42. Longest and Shortest Word Pair
# Use nested loops to identify longest and shortest words without max/min.

# Test Case
# Input: `I love Python programming`

# Expected Output:
# Longest = programming
# Shortest = I

n=input("enter sentence: ").split()

smallest=(n[0])
longest=(n[0])

for i in n:
    for j in n:
        if len(j)>len(longest):
            longest=j
        if len(j)<len(smallest):
            smallest=j

print(f"longest: {longest}  smallest: {smallest}")


