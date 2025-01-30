# shamir_secret_sharing.py

import random
from functools import reduce
from typing import List, Tuple

def is_prime(n: int) -> bool:
    """Проверка, является ли число простым."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def next_prime(n: int) -> int:
    """Нахождение следующего простого числа больше n."""
    while True:
        n += 1
        if is_prime(n):
            return n

def generate_polynomial(secret: int, threshold: int, prime: int) -> List[int]:
    """
    Генерация коэффициентов полинома.
    
    :param secret: Секрет (свободный член полинома).
    :param threshold: Пороговое значение (степень полинома = threshold - 1).
    :param prime: Простое число для поля.
    :return: Список коэффициентов полинома.
    """
    coeffs = [secret] + [random.randint(0, prime - 1) for _ in range(threshold - 1)]
    return coeffs

def evaluate_polynomial(coeffs: List[int], x: int, prime: int) -> int:
    """
    Вычисление значения полинома в точке x.
    
    :param coeffs: Коэффициенты полинома.
    :param x: Точка для вычисления.
    :param prime: Простое число для поля.
    :return: Значение полинома в точке x.
    """
    result = 0
    for power, coeff in enumerate(coeffs):
        result = (result + coeff * pow(x, power, prime)) % prime
    return result

def split_secret(secret: int, n: int, k: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Разделение секрета на n частей с порогом k.
    
    :param secret: Секрет для разделения.
    :param n: Общее количество частей.
    :param k: Пороговое количество частей для восстановления.
    :return: Простое число и список shares.
    """
    if k > n:
        raise ValueError("Пороговое значение k не может превышать общее количество частей n.")
    
    prime = next_prime(max(secret, n))
    coeffs = generate_polynomial(secret, k, prime)
    
    shares = []
    for i in range(1, n + 1):
        share = evaluate_polynomial(coeffs, i, prime)
        shares.append((i, share))
    
    return prime, shares

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Расширенный алгоритм Евклида для нахождения НОД и коэффициентов Безу."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a: int, prime: int) -> int:
    """Нахождение мультипликативного обратного элемента a по модулю prime."""
    g, x, _ = extended_gcd(a, prime)
    if g != 1:
        raise ValueError(f"Обратный элемент для {a} по модулю {prime} не существует.")
    else:
        return x % prime

def restore_secret(shares: List[Tuple[int, int]], prime: int) -> int:
    """
    Восстановление секрета из shares с использованием интерполяции Лагранжа.
    
    :param shares: Список shares (x, y).
    :param prime: Простое число для поля.
    :return: Восстановленный секрет.
    """
    if len(shares) == 0:
        raise ValueError("Нет shares для восстановления секрета.")
    
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        numerator = 1
        denominator = 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                numerator = (numerator * (-xm)) % prime
                denominator = (denominator * (xj - xm)) % prime
        lagrange_coefficient = numerator * mod_inverse(denominator, prime)
        secret = (prime + secret + (yj * lagrange_coefficient)) % prime
    return secret

def encode_string_to_int(s: str) -> int:
    """Преобразование строки в целое число."""
    return int.from_bytes(s.encode('utf-8'), 'big')

def decode_int_to_string(n: int) -> str:
    """Преобразование целого числа обратно в строку."""
    byte_length = (n.bit_length() + 7) // 8
    return n.to_bytes(byte_length, 'big').decode('utf-8')

def main():
    print("Метод Шамира для разделения и восстановления секрета")
    choice = input("Выберите действие (split/restore): ").strip().lower()
    
    if choice == 'split':
        secret_input = input("Введите секрет (строка или число): ").strip()
        if secret_input.isdigit():
            secret = int(secret_input)
            is_string = False
        else:
            secret = encode_string_to_int(secret_input)
            is_string = True
        
        n = int(input("Введите общее количество частей (n): "))
        k = int(input("Введите пороговое количество частей для восстановления (k): "))
        
        prime, shares = split_secret(secret, n, k)
        print(f"Простое число (prime): {prime}")
        print("Сгенерированные части (shares):")
        for share in shares:
            print(f"Share {share[0]}: {share[1]}")
    
    elif choice == 'restore':
        prime = int(input("Введите простое число (prime), использованное при разделении: "))
        k = int(input("Введите пороговое количество частей для восстановления (k): "))
        print(f"Введите {k} частей (формат: x y):")
        shares = []
        for _ in range(k):
            share_input = input().strip().split()
            if len(share_input) != 2:
                print("Неверный формат. Пожалуйста, введите две цифры, разделённые пробелом.")
                return
            x, y = map(int, share_input)
            shares.append((x, y))
        
        secret = restore_secret(shares, prime)
        try:
            # Попытка декодировать как строку
            secret_str = decode_int_to_string(secret)
            print(f"Восстановленный секрет (строка): {secret_str}")
        except UnicodeDecodeError:
            # Если не получается декодировать, выводим как число
            print(f"Восстановленный секрет (число): {secret}")
    
    else:
        print("Неверный выбор. Пожалуйста, выберите 'split' или 'restore'.")

if __name__ == "__main__":
    main()
