"""
Word Occurrences
Estimate: 10 minutes
Actual: To be recorded after completion

def count_word_occurrences(text)
    words = text.split()
    word_count = {}
    for word in words
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

get user_text

occurrences = count_word_occurrences(user_text)

longest_word = max(occurrences.keys(), key=len)

for word in sorted(occurrences):
    print word:{len(longest_word)}} : {occurrences[word]
"""

def count_word_occurrences(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

user_text = input("Text: ")

occurrences = count_word_occurrences(user_text)

longest_word = max(occurrences.keys(), key=len)

for word in sorted(occurrences):
    print(f"{word:{len(longest_word)}} : {occurrences[word]}")
