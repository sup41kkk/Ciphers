# caesar_cipher.py

def caesar_encrypt(plaintext, shift):
    """
    Шифрует текст методом Цезаря.
    
    :param plaintext: Открытый текст для шифрования.
    :param shift: Сдвиг (целое число).
    :return: Зашифрованный текст.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in plaintext.lower():
        if char in alphabet:
            idx = (alphabet.index(char) + shift) % len(alphabet)
            encrypted += alphabet[idx]
        else:
            encrypted += char  # Не изменяем символы вне алфавита

    return encrypted

def caesar_decrypt(ciphertext, shift):
    """
    Расшифровывает текст методом Цезаря.
    
    :param ciphertext: Зашифрованный текст.
    :param shift: Сдвиг (целое число).
    :return: Расшифрованный текст.
    """
    return caesar_encrypt(ciphertext, -shift)

def main():
    print("Шифр Цезаря")
    choice = input("Выберите действие (encrypt/decrypt): ").strip().lower()
    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))

    if choice == 'encrypt':
        result = caesar_encrypt(text, shift)
        print(f"Зашифрованный текст: {result}")
    elif choice == 'decrypt':
        result = caesar_decrypt(text, shift)
        print(f"Расшифрованный текст: {result}")
    else:
        print("Неверный выбор. Пожалуйста, выберите 'encrypt' или 'decrypt'.")

if __name__ == "__main__":
    main()
