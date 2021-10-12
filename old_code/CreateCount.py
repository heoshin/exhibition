from collections import Counter
with open("data/물금고등학교-익명의-숲-생활편_word.txt", "r", encoding="UTF-8") as f:
    words = f.read().splitlines() 

count = Counter(words)
count = count.most_common(500)
print(count)
with open("data/물금고등학교-익명의-숲-생활편_word_count.txt", "w", encoding="UTF-8") as f:
    for word, cnt in count:
        f.write(f"{word} : {cnt}\n")