def analyze_word(word: str):
    vowels = "аеёиоуыэюяaeiouy"
    lower_pairs = 0
    upper_pairs = 0
    vowels_count = 0

    for char in word:
        if char.lower() in vowels:
            vowels_count += 1

    for i in range(len(word) - 1):
        if word[i].islower() and word[i + 1].islower():
            lower_pairs += 1
        elif word[i].isupper() and word[i + 1].isupper():
            upper_pairs += 1

    print(f"Пары нижнего регистра: {lower_pairs}")
    print(f"Пары верхнего регистра: {upper_pairs}")
    print(f"Количество гласных букв: {vowels_count}")


def main():
    user_word = input("Введите слово: ").strip()
    if user_word:
        analyze_word(user_word)


if __name__ == "__main__":
    main()