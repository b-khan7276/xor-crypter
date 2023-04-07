import sys
import os
import argparse

def xor_encrypt_decrypt(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as file:
            binary_data = file.read()
        
        encrypted_data = bytearray()
        for b in binary_data:
            encrypted_data.append(b ^ key)

        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

        print(f"Processed file successfully saved to: {output_file}")
    except Exception as e:
        print(f"Error during processing: {e}")

def main():
    parser = argparse.ArgumentParser(description="XOR encryption and decryption for exe files")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input exe file path")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output exe file path")
    parser.add_argument("-k", "--key", type=int, required=True, help="Single-byte XOR key (0-255)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Input file '{args.input}' does not exist.")
        sys.exit(1)

    if args.key < 0 or args.key > 255:
        print("Invalid XOR key. Please provide a key between 0 and 255.")
        sys.exit(1)

    xor_encrypt_decrypt(args.input, args.output, args.key)

if __name__ == "__main__":
    main()
