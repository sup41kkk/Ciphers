# affine_cipher.py

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """
    Находит мультипликативный обратный элемент для a по модулю m.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Обратный элемент для a={a} по модулю m={m} не существует.")

def affine_encrypt(plaintext, a, b):
    """
    Шифрует текст аффинным шифром.
    
    :param plaintext: Открытый текст.
    :param a: Коэффициент a (должен быть взаимно простым с m).
    :param b: Коэффициент b.
    :return: Зашифрованный текст.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    m = len(alphabet)
    if gcd(a, m) != 1:
        raise ValueError(f"Коэффициент a={a} не взаимно прост с m={m}.")
    
    encrypted = ''
    for char in plaintext.lower():
        if char in alphabet:
            x = alphabet.index(char)
            encrypted += alphabet[(a * x + b) % m]
        else:
            encrypted += char  # Не изменяем символы вне алфавита

    return encrypted

def affine_decrypt(ciphertext, a, b):
    """
    Расшифровывает текст аффинным шифром.
    
    :param ciphertext: Зашифрованный текст.
    :param a: Коэффициент a.
    :param b: Коэффициент b.
    :return: Расшифрованный текст.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    m = len(alphabet)
    a_inv = mod_inverse(a, m)
    
    decrypted = ''
    for char in ciphertext.lower():
        if char in alphabet:
            y = alphabet.index(char)
            decrypted += alphabet[(a_inv * (y - b)) % m]
        else:
            decrypted += char  # Не изменяем символы вне алфавита

    return decrypted

def main():
    print("Аффинный шифр")
    choice = input("Выберите действие (encrypt/decrypt): ").strip().lower()
    text = input("Введите текст: ")
    a = int(input("Введите коэффициент a (взаимно простой с 26): "))
    b = int(input("Введите коэффициент b: "))

    if choice == 'encrypt':
        try:
            result = affine_encrypt(text, a, b)
            print(f"Зашифрованный текст: {result}")
        except ValueError as e:
            print(e)
    elif choice == 'decrypt':
        try:
            result = affine_decrypt(text, a, b)
            print(f"Расшифрованный текст: {result}")
        except ValueError as e:
            print(e)
    else:
        print("Неверный выбор. Пожалуйста, выберите 'encrypt' или 'decrypt'.")

if __name__ == "__main__":
    main()
