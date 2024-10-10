# longest_word.py

def longest(sentence):
    words = sentence.split()
    max_length = 0
    longest_word = ""
    
    for word in words:
        # Menghitung panjang kata
        length = len(word)
        if length > max_length:
            max_length = length
            longest_word = word
            
    return f"{longest_word}: {max_length} character"

if __name__ == "__main__":
    # Contoh penggunaan
    sentence = "Saya sangat senang mengerjakan soal algoritma"
    result = longest(sentence)
    print(f"Kalimat: \"{sentence}\"")
    print(f"Kata terpanjang: {result}")
