# reverse_alphabet.py

def reverse_alphabet(s):
    # Pisahkan bagian huruf dan angka
    letters = ''.join([c for c in s if c.isalpha()])
    numbers = ''.join([c for c in s if c.isdigit()])
    
    # Balik huruf
    reversed_letters = letters[::-1]
    
    # Gabungkan kembali huruf yang dibalik dengan angka
    return reversed_letters + numbers

if __name__ == "__main__":
    # Contoh penggunaan
    input_str = "NEGIE1"
    result = reverse_alphabet(input_str)
    print(f"Input: {input_str}")
    print(f"Output: {result}")
