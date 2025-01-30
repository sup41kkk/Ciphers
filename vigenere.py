import math

def vigenere_cipher_russian(plaintext, key):
    # Определение русского алфавита с буквой 'ё'
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letter_to_index = {char: idx for idx, char in enumerate(alphabet)}
    index_to_letter = {idx: char for idx, char in enumerate(alphabet)}
    
    # Предобработка: приведение к нижнему регистру и удаление пробелов
    plaintext = plaintext.lower().replace(' ', '')
    key = key.lower().replace(' ', '')
    
    # Преобразование букв в индексы
    try:
        plaintext_indices = [letter_to_index[c] for c in plaintext]
    except KeyError as e:
        raise ValueError(f"Недопустимый символ в открытом тексте: {e}")
    
    try:
        key_indices = [letter_to_index[c] for c in key]
    except KeyError as e:
        raise ValueError(f"Недопустимый символ в ключе: {e}")
    
    # Количество столбцов
    columns = 6
    # Разбиение открытого текста на строки по 6 букв
    num_rows = math.ceil(len(plaintext_indices) / columns)
    
    # Разбиение ключа на строки по 6 букв
    key_matrix = [key_indices[i:i+columns] for i in range(0, len(key_indices), columns)]
    
    # Формирование полного ключа, повторяя блоки ключа по необходимости
    key_full = []
    for row in range(num_rows):
        key_row = key_matrix[row % len(key_matrix)]
        key_full.extend(key_row)
    
    # Обрезаем ключ до длины открытого текста
    key_full = key_full[:len(plaintext_indices)]
    
    # Шифрование: добавление индексов и взятие по модулю 33
    ciphertext_indices = [(p + k) % 33 for p, k in zip(plaintext_indices, key_full)]
    
    # Преобразование индексов обратно в буквы
    ciphertext = ''.join([index_to_letter[idx] for idx in ciphertext_indices])
    
    return ciphertext

def main():
    # Открытый текст
    plaintext = "шифрвиженератакженеявляетсянадежным"
    # Ключ
    key = "скрыть"
    # Шифрование
    ciphertext = vigenere_cipher_russian(plaintext, key)
    print("Зашифрованный текст:", ciphertext)

if __name__ == "__main__":
    main()
