# substitution_cipher.py

def create_substitution_mapping(key):
    """
    Создает словарь для подстановки на основе ключа.
    
    :param key: Ключевое слово (должно содержать все буквы алфавита без повторений).
    :return: Два словаря: для шифрования и расшифровки.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = ''.join(sorted(set(key.lower()), key=key.index))  # Удаляем повторы, сохраняем порядок
    remaining = ''.join([c for c in alphabet if c not in key])
    substitution = key + remaining

    encrypt_mapping = {a: b for a, b in zip(alphabet, substitution)}
    decrypt_mapping = {b: a for a, b in zip(alphabet, substitution)}
    return encrypt_mapping, decrypt_mapping

def substitution_encrypt(plaintext, encrypt_mapping):
    """
    Шифрует текст подстановкой.
    
    :param plaintext: Открытый текст.
    :param encrypt_mapping: Словарь для шифрования.
    :return: Зашифрованный текст.
    """
    encrypted = ''
    for char in plaintext.lower():
        if char in encrypt_mapping:
            encrypted += encrypt_mapping[char]
        else:
            encrypted += char  # Не изменяем символы вне алфавита
    return encrypted

def substitution_decrypt(ciphertext, decrypt_mapping):
    """
    Расшифровывает текст подстановкой.
    
    :param ciphertext: Зашифрованный текст.
    :param decrypt_mapping: Словарь для расшифровки.
    :return: Расшифрованный текст.
    """
    decrypted = ''
    for char in ciphertext.lower():
        if char in decrypt_mapping:
            decrypted += decrypt_mapping[char]
        else:
            decrypted += char  # Не изменяем символы вне алфавита
    return decrypted

def main():
    print("Простой подстановочный шифр")
    choice = input("Выберите действие (encrypt/decrypt): ").strip().lower()
    text = input("Введите текст: ")
    key = input("Введите ключ (порядок букв подстановки): ")

    encrypt_mapping, decrypt_mapping = create_substitution_mapping(key)

    if choice == 'encrypt':
        result = substitution_encrypt(text, encrypt_mapping)
        print(f"Зашифрованный текст: {result}")
    elif choice == 'decrypt':
        result = substitution_decrypt(text, decrypt_mapping)
        print(f"Расшифрованный текст: {result}")
    else:
        print("Неверный выбор. Пожалуйста, выберите 'encrypt' или 'decrypt'.")

if __name__ == "__main__":
    main()
