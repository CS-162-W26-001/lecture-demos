def read_file() -> list[str]:
    words = []
    with open('persuasion.txt', 'r') as file:
        for line in file:
            words_in_line = line.split(" ")
            for word in words_in_line:
                words.append(word)
    return words

def word_count(words: list[str]) -> dict[str, int]:
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def main() -> None:
    words_in_novel = read_file()
    print("Words in novel", len(words_in_novel))
    print("First 20 words", words_in_novel[0:20])

    word_frequency = word_count(words_in_novel)
    print('the', word_frequency['the'])
    print("Unique words", len(word_frequency))

    print('Anne', word_frequency['Anne'])
    print('Frederick', word_frequency['Frederick'])
    print('Wentworth', word_frequency['Wentworth'])

    test_value = "Spock"
    if test_value in word_frequency:
        print('Spock', word_frequency['Spock'])

    frequency_counts = []
    for item in word_frequency:
        key = item
        value = word_frequency[item]
        pair = (value, key)
        frequency_counts.append(pair)
    frequency_counts.sort(reverse=True)
    print(frequency_counts[0:100])

if __name__ == "__main__":
    main()
