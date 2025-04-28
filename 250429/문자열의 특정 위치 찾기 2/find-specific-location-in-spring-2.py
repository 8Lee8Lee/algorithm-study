words = ["apple", "banana", "grape", "blueberry", "orange"]

target = input()

matched_words = []

for word in words:
    if word[2] == target or word[3] == target:
        matched_words.append(word)

for w in matched_words:
    print(w)
print(len(matched_words))