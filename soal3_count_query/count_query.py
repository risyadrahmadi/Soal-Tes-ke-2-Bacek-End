# count_query.py

def count_queries(INPUT, QUERY):
    # Membuat dictionary untuk menghitung frekuensi kata dalam INPUT
    freq = {}
    for word in INPUT:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    # Menghitung jumlah kemunculan setiap query
    result = []
    for q in QUERY:
        count = freq.get(q, 0)
        result.append(count)
    
    return result

if __name__ == "__main__":
    # Contoh penggunaan
    INPUT = ['xc', 'dz', 'bbb', 'dz']
    QUERY = ['bbb', 'ac', 'dz']
    output = count_queries(INPUT, QUERY)
    print(f"INPUT: {INPUT}")
    print(f"QUERY: {QUERY}")
    print(f"OUTPUT: {output}")
