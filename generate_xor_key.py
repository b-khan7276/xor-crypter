import random

def generate_xor_key():
    return random.randint(0, 255)

if __name__ == "__main__":
    key = generate_xor_key()
    print(f"Generated XOR key: {key}")
