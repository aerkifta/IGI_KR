import re
import statistics
from collections import Counter
from itertools import islice

# === Ввод данных ===
text = input("Введите текст: ").strip()

# === Настройки N и K ===
try:
    N = int(input("Введите длину N-граммы (по умолчанию 4): ") or 4)
    K = int(input("Введите топ-K частых N-грамм (по умолчанию 10): ") or 10)
except ValueError:
    print("Ошибка: N и K должны быть целыми числами.")
    exit(1)

# === Предобработка текста ===
# Приводим к нижнему регистру
text_clean = text.lower()

# Удаляем знаки препинания
text_clean = re.sub(r'[^\w\s\.!?]', '', text_clean)

# Разделение на предложения (по . ! ?)
sentences = re.split(r'[.!?]', text_clean)
sentences = [s.strip() for s in sentences if s.strip()]

# Разделение на слова
words = re.findall(r'\b\w+\b', text_clean)

# === 1. Частота слов ===
word_counts = Counter(words)

print("\n=== Частота слов ===")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# === 2. Среднее количество слов в предложении ===
sentence_lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]

avg_length = sum(sentence_lengths) / len(sentence_lengths)
median_length = statistics.median(sentence_lengths)

print(f"\nСреднее количество слов в предложении: {avg_length:.2f}")
print(f"Медианное количество слов в предложении: {median_length}")

# === 3. Топ-K N-грамм ===
# Только буквенные символы
letters_only = re.sub(r'[^a-zA-Zа-яА-Я]', '', text_clean)

ngrams = [letters_only[i:i+N] for i in range(len(letters_only) - N + 1)]
ngram_counts = Counter(ngrams).most_common(K)

print(f"\nТоп-{K} буквенных {N}-грамм:")
for gram, freq in ngram_counts:
    print(f"{gram}: {freq}")
