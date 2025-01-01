from Crypto.Cipher import AES

IV_HEX = '09080706050403020100A2B2C2D2E2F2'
PLAINTEXT_HEX = '255044462d312e350a25d0d4c5d80a34'
EXPECTED_CIPHERTEXT_HEX = 'd06bf9d0dab8e8ef880660d2af65aa82'

iv = bytes.fromhex(IV_HEX.lower())
plaintext = bytes.fromhex(PLAINTEXT_HEX.lower())
expected_ciphertext = bytes.fromhex(EXPECTED_CIPHERTEXT_HEX.lower())

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
                print(f"Found matching key: {key.hex()}")
                print(f"Ciphertext: {ciphertext.hex()}")
                print(f"IV: {iv.hex()}")
                print(f"Plaintext: {plaintext.hex()}")
                break
    else:
        print("No matching key found.")

process_keys('keysgenerated.txt')
