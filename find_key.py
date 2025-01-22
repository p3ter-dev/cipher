from Crypto.Cipher import AES

iv = '09080706050403020100A2B2C2D2E2F2'
plain_text = '255044462d312e350a25d0d4c5d80a34'
expected_cipher = 'd06bf9d0dab8e8ef880660d2af65aa82'

iv = bytes.fromhex(iv.lower())
plaintext = bytes.fromhex(plain_text.lower())
expected_ciphertext = bytes.fromhex(expected_cipher.lower())

def decrypt_and_check(key_hex):
    key = bytes.fromhex(key_hex.lower())
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext == expected_ciphertext, key, ciphertext

def process_keys(filename):
    with open(filename) as fp:
        keys = fp.readlines()

    for key_hex in keys:
        key_hex = key_hex.strip()

        if len(key_hex) == 32:
            is_valid, key, ciphertext = decrypt_and_check(key_hex)
            if is_valid:
                print(f"Found the matching encryption key: {key.hex()}")
                print(f"Ciphertext: {ciphertext.hex()}")
                break
    else:
        print("No matching key found.")

process_keys('keysgenerated.txt')
