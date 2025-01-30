# playfair_cipher.py

def generate_playfair_matrix(key):
    """
    Генерирует матрицу Плейфера на основе ключа.
    
    :param key: Ключевое слово.
    :return: 5x5 матрица Плейфера.
    """
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  # 'j' обычно объединяется с 'i'
    key = key.lower().replace('j', 'i')
    matrix = []
    seen = set()

    for char in key:
        if char in alphabet and char not in seen:
            matrix.append(char)
            seen.add(char)

    for char in alphabet:
        if char not in seen:
            matrix.append(char)

    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    """
    Находит позицию символа в матрице.
    
    :param matrix: Матрица Плейфера.
    :param char: Символ для поиска.
    :return: Кортеж (row, col).
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return (row, col)
    return None

def playfair_prepare_text(text):
    """
    Подготавливает текст для шифрования:
    - Удаляет неалфавитные символы.
    - Заменяет 'j' на 'i'.
    - Делит на биграммы, добавляя 'x' при необходимости.
    
    :param text: Входной текст.
    :return: Список биграмм.
    """
    text = text.lower().replace('j', 'i')
    text = ''.join([c for c in text if c.isalpha()])
    prepared = []
    i = 0
    while i < len(text):
        a = text[i]
        b = 'x'
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                b = 'x'
                i += 1
            else:
                i += 2
        else:
            i += 1
        prepared.append(a + b)
    return prepared

def playfair_encrypt(plaintext, key):
    """
    Шифрует текст методом Плейфера.
    
    :param plaintext: Открытый текст.
    :param key: Ключевое слово.
    :return: Зашифрованный текст.
    """
    matrix = generate_playfair_matrix(key)
    prepared_text = playfair_prepare_text(plaintext)
    ciphertext = ''

    for pair in prepared_text:
        a, b = pair
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    """
    Расшифровывает текст методом Плейфера.
    
    :param ciphertext: Зашифрованный текст.
    :param key: Ключевое слово.
    :return: Расшифрованный текст.
    """
    matrix = generate_playfair_matrix(key)
    prepared_text = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plaintext = ''

    for pair in prepared_text:
        a, b = pair
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        else:
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]

    return plaintext

def main():
    print("Шифр Плейфера")
    choice = input("Выберите действие (encrypt/decrypt): ").strip().lower()
    text = input("Введите текст: ")
    key = input("Введите ключевое слово: ")

    if choice == 'encrypt':
        result = playfair_encrypt(text, key)
        print(f"Зашифрованный текст: {result}")
    elif choice == 'decrypt':
        result = playfair_decrypt(text, key)
        print(f"Расшифрованный текст: {result}")
    else:
        print("Неверный выбор. Пожалуйста, выберите 'encrypt' или 'decrypt'.")

if __name__ == "__main__":
    main()
