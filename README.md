# xor-crypter
Save this code to a file, e.g., xor_exe.py.
 You can use the script from the command line to encode an exe file into another exe file using XOR encryption. 
 To process a file, 
 use python xor_exe.py -i your_input_exe_file.exe -o your_output_encoded_exe_file.exe -k your_xor_key.
  The your_xor_key should be an integer between 0 and 255.


  notes for generate_xor_key.py

  Save this code to a file, e.g., generate_xor_key.py. Run the script using python generate_xor_key.py, 
  and it will print a randomly generated single-byte XOR key.


  --------------------------
  python xor_exe.py -i demogame.exe -o game.exe -k 255
