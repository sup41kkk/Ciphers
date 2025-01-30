# rail_fence_cipher.py

def rail_fence_encrypt(plaintext, num_rails):
    """
    Шифрует текст методом Rail Fence.
    
    :param plaintext: Открытый текст.
    :param num_rails: Количество рядов.
    :return: Зашифрованный текст.
    """
    if num_rails == 1:
        return plaintext

    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1  # 1 — вниз, -1 — вверх

    for char in plaintext:
        rails[rail] += char
        rail += direction

        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return ''.join(rails)

def rail_fence_decrypt(ciphertext, num_rails):
    """
    Расшифровывает текст методом Rail Fence.
    
    :param ciphertext: Зашифрованный текст.
    :param num_rails: Количество рядов.
    :return: Расшифрованный текст.
    """
    if num_rails == 1:
        return ciphertext

    # Создаем матрицу для заполнения
    mark = [['\n' for _ in range(len(ciphertext))] for _ in range(num_rails)]

    # Определяем положение символов
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        mark[rail][i] = '*'
        rail += direction

        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # Заполняем матрицу зашифрованными символами
    index = 0
    for r in range(num_rails):
        for c in range(len(ciphertext)):
            if mark[r][c] == '*' and index < len(ciphertext):
                mark[r][c] = ciphertext[index]
                index += 1

    # Читаем расшифрованный текст
    decrypted = ''
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        decrypted += mark[rail][i]
        rail += direction

        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return decrypted

def main():
    print("Шифр Rail Fence")
    choice = input("Выберите действие (encrypt/decrypt): ").strip().lower()
    text = input("Введите текст: ")
    num_rails = int(input("Введите количество рядов: "))

    if choice == 'encrypt':
        result = rail_fence_encrypt(text, num_rails)
        print(f"Зашифрованный текст: {result}")
    elif choice == 'decrypt':
        result = rail_fence_decrypt(text, num_rails)
        print(f"Расшифрованный текст: {result}")
    else:
        print("Неверный выбор. Пожалуйста, выберите 'encrypt' или 'decrypt'.")

if __name__ == "__main__":
    main()
