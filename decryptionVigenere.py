import math
from collections import defaultdict, Counter
from functools import reduce
import string

def read_ciphertext(filename):
    """
    Читает зашифрованный текст из файла и удаляет пробелы и перевод строки.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.lower().replace(' ', '').replace('\n', '')
    return text

def kasiski_examination(ciphertext, seq_len=6):
    """
    Реализация метода Касиски для определения длины ключа.
    """
    # Найти все повторяющиеся последовательности длиной seq_len
    sequences = defaultdict(list)
    for i in range(len(ciphertext) - seq_len + 1):
        seq = ciphertext[i:i+seq_len]
        sequences[seq].append(i)
    
    # Собрать расстояния между повторениями
    distances = []
    for seq, indexes in sequences.items():
        if len(indexes) > 1:
            for i in range(len(indexes)-1):
                distance = indexes[i+1] - indexes[i]
                distances.append(distance)
    
    if not distances:
        return None  # Не удалось определить длину ключа
    
    # Найти НОД всех расстояний
    key_length = reduce(math.gcd, distances)
    return key_length

def split_into_columns(ciphertext, key_length):
    """
    Разбивает текст на столбцы по длине ключа.
    """
    columns = ['' for _ in range(key_length)]
    for index, char in enumerate(ciphertext):
        columns[index % key_length] += char
    return columns

def compute_letter_frequencies(columns, alphabet):
    """
    Подсчитывает частоты появления каждой буквы в каждом столбце.
    """
    letter_to_index = {char: idx for idx, char in enumerate(alphabet)}
    frequencies = []
    for column in columns:
        count = [0] * len(alphabet)
        for char in column:
            if char in letter_to_index:
                count[letter_to_index[char]] += 1
        frequencies.append(count)
    return frequencies

def index_of_coincidence(counts, total):
    """
    Вычисляет индекс совпадения для каждой частоты букв.
    """
    index = []
    for count in counts:
        ic = sum(c * (c - 1) for c in count) / (total * (total - 1)) if total > 1 else 0
        index.append(ic)
    return index

def mutual_index_of_coincidence(count1, count2, len1, len2):
    """
    Вычисляет взаимный индекс совпадения между двумя наборами частот.
    """
    return sum(c1 * c2 for c1, c2 in zip(count1, count2)) / (len1 * len2) if len1 > 0 and len2 > 0 else 0

def find_key_shifts(frequencies, alphabet):
    """
    Определяет сдвиги для каждого столбца ключа на основе индекса совпадения.
    """
    key_shifts = []
    expected_ic = 0.054  # Ожидаемый индекс совпадения для русского языка
    
    for count in frequencies:
        total = sum(count)
        max_ic = 0
        best_shift = 0
        for shift in range(len(alphabet)):
            shifted_count = count[shift:] + count[:shift]
            ic = mutual_index_of_coincidence(count, shifted_count, total, total)
            if ic > max_ic:
                max_ic = ic
                best_shift = shift
        key_shifts.append(best_shift)
    return key_shifts

def shift_letter(char, shift, alphabet):
    """
    Сдвигает букву на заданный сдвиг по алфавиту.
    """
    index = alphabet.find(char)
    if index == -1:
        return char  # Не изменяем символ, если его нет в алфавите
    return alphabet[(index + shift) % len(alphabet)]

def decrypt_vigenere(ciphertext, key, alphabet):
    """
    Расшифровывает текст методом Виженера с заданным ключом.
    """
    decrypted = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char in alphabet:
            c_index = alphabet.find(char)
            k_index = alphabet.find(key[i % key_length])
            p_index = (c_index - k_index) % len(alphabet)
            decrypted.append(alphabet[p_index])
        else:
            decrypted.append(char)  # Не изменяем символ, если его нет в алфавите
    return ''.join(decrypted)

def main():
    # Определение русского алфавита с буквой 'ё'
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    # Чтение зашифрованного текста из файла
    ciphertext = read_ciphertext('file1')
    print(f"Зашифрованный текст: {ciphertext}")
    
    # Метод Касиски для определения длины ключа
    key_length = kasiski_examination(ciphertext, seq_len=6)
    if key_length:
        print(f"Длина ключа, определенная методом Касиски: {key_length}")
    else:
        print("Не удалось определить длину ключа методом Касиски.")
        return
    
    # Разбиение текста на столбцы по длине ключа
    columns = split_into_columns(ciphertext, key_length)
    
    # Подсчет частот букв в каждом столбце
    frequencies = compute_letter_frequencies(columns, alphabet)
    
    # Вычисление индекса совпадения для каждого столбца
    ic = index_of_coincidence(frequencies, len(ciphertext) // key_length)
    for idx, value in enumerate(ic, 1):
        print(f"Индекс совпадения для столбца {idx}: {value:.4f}")
    
    # Определение сдвигов для ключа
    key_shifts = find_key_shifts(frequencies, alphabet)
    print(f"Предполагаемые сдвиги ключа: {key_shifts}")
    
    # Преобразование сдвигов в буквы ключа
    key = ''.join([alphabet[shift] for shift in key_shifts])
    print(f"Предполагаемый ключ: {key}")
    
    # Запрос ввода ключа у пользователя
    user_key = input("Введите ключ для расшифровки: ").lower()
    
    # Расшифровка текста
    decrypted_text = decrypt_vigenere(ciphertext, user_key, alphabet)
    print(f"Расшифрованный текст:\n{decrypted_text}")

if __name__ == "__main__":
    main()
