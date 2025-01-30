# Cryptography Algorithms Toolkit

This repository contains implementations of classical cryptographic algorithms. Each script is a standalone program designed to encrypt and decrypt text using a specific cipher. The toolkit covers a wide range of classical techniques, including substitution-based ciphers, transposition methods, and advanced secret-sharing schemes.

---

## 1. **Affine Cipher**

The affine cipher is a substitution cipher that uses a mathematical function to encrypt and decrypt text.

### Features
- Encrypts and decrypts using the formula:
  - Encryption: `E(x) = (a * x + b) mod m`
  - Decryption: `D(x) = a_inv * (y - b) mod m`, where `a_inv` is the modular inverse of `a`.
- Ensures that `a` is coprime with `m` (typically 26 for the English alphabet).

### Usage
Run the program and choose between encryption and decryption.

Example:
```
Введите коэффициент a (взаимно простой с 26): 5
Введите коэффициент b: 8
Открытый текст: hello
Зашифрованный текст: rmwwl
```

---

## 2. **Caesar Cipher**

The Caesar cipher is a simple substitution cipher that shifts letters by a fixed number of places.

### Features
- Supports both encryption and decryption.
- Handles non-alphabetic characters without modification.

### Usage
Run the program, provide the text and the shift value, and choose an operation.

Example:
```
Введите текст: attack at dawn
Введите сдвиг: 3
Зашифрованный текст: dwwdfn dw gdzq
```

---

## 3. **Vigenère Cipher (Russian Alphabet)**

The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt text.

### Features
- Works with the Russian alphabet, including `ё`.
- Automatically repeats the key to match the plaintext length.

### Usage
Specify the plaintext and key in the script, and run the program.

Example:
```
Открытый текст: шифрвиженера
Ключ: скрыть
Зашифрованный текст: тсэфтуефжйёю
```

---

## 4. **Rail Fence Cipher**

The rail fence cipher is a transposition cipher that rearranges characters based on a zigzag pattern.

### Features
- Encrypts and decrypts text using a specified number of rails.

### Usage
Provide the text and the number of rails, and run the program.

Example:
```
Введите текст: meet at dawn
Введите количество рядов: 3
Зашифрованный текст: mta wnete da
```

---

## 5. **Substitution Cipher**

The substitution cipher replaces each letter in the plaintext with a corresponding letter from a custom key.

### Features
- Allows flexible key definition.
- Ensures that the key contains all alphabet letters without repetition.

### Usage
Provide the plaintext and key, and choose an operation.

Example:
```
Введите ключ: phqgiumeaylnofdxjkrcvstzwb
Открытый текст: hello
Зашифрованный текст: dkssn
```

---

## 6. **Playfair Cipher**

The Playfair cipher is a digraphic substitution cipher that encrypts pairs of letters using a 5x5 matrix.

### Features
- Handles repeated letters in a digraph by inserting a filler (e.g., `x`).
- Merges `j` with `i` for English text.

### Usage
Provide the text and the key, and run the program.

Example:
```
Введите текст: meet me at the park
Введите ключевое слово: monarchy
Зашифрованный текст: gatr gm at hs gb kt
```

---

## 7. **Shamir's Secret Sharing**

This script implements Shamir's Secret Sharing scheme for securely splitting and reconstructing a secret.

### Features
- Splits a secret into `n` parts with a threshold of `k` parts required for reconstruction.
- Uses modular arithmetic and polynomial interpolation.

### Usage
Run the program and choose between splitting and reconstructing a secret.

Example:
```
Введите секрет: 1234
Введите n: 5
Введите k: 3
Простое число: 1237
Сгенерированные части:
1: 567
2: 892
...
```

---

## 8. **Kasiski Examination**

This script implements the Kasiski method to analyze ciphertexts and estimate the length of the encryption key.

### Features
- Finds repeated sequences in the ciphertext.
- Calculates distances and suggests likely key lengths.

### Usage
Run the program with a ciphertext input and specify the sequence length.

Example:
```
Наиболее вероятные длины ключа: 3, 6, 9
```

---

## Technical Dependencies
The scripts require the following Python libraries:
- `numpy`
- `scipy`
- `math`
- `random`

Install dependencies using:
```
pip install numpy scipy
```

---

## Licensing
This repository is open-source and available under the MIT License for educational and research purposes.

