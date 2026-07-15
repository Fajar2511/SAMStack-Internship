print("Day 3 Tasks:")

print("----- Task 1 -----")
sen = input("Enter a sentence with unique characters = ")
Myset = set(sen)
Count = len(Myset)
print("Unique characters = ", Myset)
print("Count:", Count)


print("\n----- Task 2 -----")
Data = "AI is amazing, but AI requires data! Data is everything."
data = Data.lower()
data = data.replace(".", " ").replace("!", " ").replace(",", " ")
data = data.split()
freq = {}
for word in data:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

print("\n----- Task 3 -----")
word = input("Enter a word to check if its palindrome = ")
rev = "" 

for char in word:
    rev=char+rev 

if word == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")