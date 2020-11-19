txt = open("article.txt", "r")
txt1 =(txt.read().lower())

to_remove = '''!()-[]{};:'"\,<>./?@#$%^&*_~â€™””'''

words = ""
for char in txt1:
   if char not in to_remove:
      words = words + char
w=words.split()

def word_count(str):
    counts = dict()
    for word in w:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(w))













