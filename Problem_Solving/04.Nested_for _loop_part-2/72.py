# Q72. Word Pair Analyzer
# For every word pair print lengths and first-character comparison.

# Test Case
# Input: `I love code`

# Expected Output: Each pair includes both lengths and Same/Different first-character result.

n=input("enter word: ").split()

for i in range(len(n)):
    for j in range(i+1,len(n)):
        pass