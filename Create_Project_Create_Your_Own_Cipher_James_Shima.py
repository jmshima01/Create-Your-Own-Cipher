# James Shima
# CSCI 101, Sec. H
# Create Project
# Ref: n/a
# Est. Total Time: 10 hours

# Imports:
# External library numpy required for some functions
import numpy

# Main Vars ------------------------------------
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
keep_going = 'yes'

# Intro ----------------------------------------
print("===============================================")
print(" ____________________________________ ")
print("|                                    |")
print("| Welcome to Create Your Own Cipher! |")
print("|____________________________________|")

print()
print(" ___________________________________________________________________________________________________________________")
print("|                                                                                                                   |")
print("| In this program, you will be able to choose from three different cipher types to encrypt messages, passwords, etc.|")
print("| Once you have encrpyted your data, it will be writen into a file of your choice                                   |")
print("| Lastly, a decrypter is avalible for two of the encryption types to reveal your own, or someone else's messages.   |")
print("|___________________________________________________________________________________________________________________|")

print("\nLet's get started.\nPlease choose from the three different cipher types below:")
while not((keep_going.lower() == "no")or(keep_going.lower() == 'n')): 
    print()
    print("1.) Shift Cipher")
    print("2.) Block Cipher")
    print("3.) Hash Cipher")
    print()
    user_cipher_choice = str(input("OPTION NUMBER (1-3)> "))

    while not((user_cipher_choice == '1') or (user_cipher_choice == '2') or (user_cipher_choice == '3') or (user_cipher_choice.lower() == 'one') or (user_cipher_choice.lower() == 'two') or (user_cipher_choice.lower() == 'three')):
        print("ERROR> Please only input 1, 2, or 3 to continue.")
        user_cipher_choice = str(input("OPTION NUMBER (1-3)> "))
    
    # ----------------------------

    # Option One - Shift Cipher
    if user_cipher_choice == '1' or user_cipher_choice.lower() == 'one':
        print()
        print('You chose a Shift Cipher!')
        print('Enter the shift that would like your text shifted by.')
        shif = int(input('SHIFT> '))
        print("Enter the text you would like to be encrypted.")

        pretext_one = str(input('TEXT> '))

        shift = shif
        list1 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25]
        list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        def shift_cipher(pretext_one,shift):
            if (shift not in list2) or (shift not in list1):
                shift %= 26
            
            alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
            shifted_alphabet_lower = alphabet_lower[int(shift):] + alphabet_lower[:int(shift)]
            shifted_alphabet_upper = alphabet_upper[int(shift):] + alphabet_upper[:int(shift)]
            shifted_text = ''
    
            for i in range(len(pretext_one)):
                if pretext_one[i] in alphabet_lower:
                    index = alphabet_lower.index(pretext_one[i])
                    shifted_text += shifted_alphabet_lower[index]
                elif pretext_one[i] in alphabet_upper:
                    index = alphabet_upper.index(pretext_one[i])
                    shifted_text += shifted_alphabet_upper[index]
                else:
                    shifted_text += pretext_one[i]

            return shifted_text

        print(f"\nYour new encrypted data with a shift of {shift} reads as follows:")
        print(shift_cipher(pretext_one,shift))

        print("\nLet's write your encryption to a file for you to keep.\n")
        user_file = str(input("Enter the file you would like your encryption written to\nFILE> "))
        Cipher_name = input("\nWhat is the name of your cipher?\nNAME> ")
        with open(user_file,'w') as File:
            File.write(f"{Cipher_name}:\n{shift_cipher(pretext_one, shift)}\n")
            File.write(f"\nShift:\n{shift}")

        print(f"\nWe've added the {Cipher_name} encryption to your {user_file} file.\n")

        keep_going = str(input("Would you like to create another cipher?\nYES/NO> "))
        # ----------------------------------------       



    # Option 2 ---------- Block Cipher:
    if user_cipher_choice == '2' or user_cipher_choice.lower() == 'two':
        alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        print()
        print("You chose a Block Cipher!")
        print()
        print("First, we need to create a key for your encryption.")
        print("We will make our key a 2D matrix with the same length and width.")
        key_dimensions = int(input("\nEnter the length and width (N X N) for your matrix key:\nN> "))
        key = [['b' for i in range(key_dimensions)]for j in range(key_dimensions)]

        print(f"\nLets create your {key_dimensions} X {key_dimensions} key:\n")
        for i in range(key_dimensions):
            for j in range(key_dimensions):
                key_input = int(input(f"Enter an Integer for your key.\nINT @ [{i}],[{j}]> "))
                key[i][j] = key_input 
            

        print("\nHere is the key you've created for your Block Cipher.")
        for i in key:
            print(i)

 
        print(f"\nPlease choose the number of rows to represent the text you want to be encrypted in Marix form.")
        print(f"NOTE: the length of your text will be longer/shorter by the number of rows you chose (as matrix multiplication is used in your encryption).")
        nah = 'no'
        while nah.lower() == 'no' or nah.lower() == 'n':
            text_rows = int(input("ROWS> "))
            print(f"\nThe length of the text you will encrypt will be {text_rows*key_dimensions}")
            yes = input("\nIs this the length you wanted?\nYES/NO> ")
            nah = yes
  
        text_length = text_rows * key_dimensions
        text_tbc = [['c' for i in range(key_dimensions)]for j in range(text_rows)]

        #for i in text_tbc:
            #print(i)

        print("\nEnter the text (ONLY LETTERS) of the message you wish to be encypted:")
        r = 0
        text_block = str(input(f"TEXT WITH LENGTH OF {text_rows*key_dimensions}> "))
    

        while len(text_block) != (text_rows*key_dimensions): 
            if len(text_block) > (text_rows*key_dimensions):
                print(f"ERROR> Input was too long, make sure input has exactly {text_rows*key_dimensions} characters")
            if len(text_block) < (text_rows*key_dimensions):
                print(f"ERROR> Input was too short, make sure input has exactly {text_rows*key_dimensions} characters")
            text_block = str(input(f"TEXT WITH LENGTH OF {text_rows*key_dimensions}> "))

        while True:

            count2 = 0
            for i in range(len(text_block)):
                if not((text_block[i] in alphabet_lower) or (text_block[i] in alphabet_upper)):
                    print(f"ERROR> Part of input was not a letter. Please use ONLY LETTERS")
                    text_block = str(input(f"TEXT WITH LENGTH OF {text_rows*key_dimensions}> "))
                    count2+=1

            if count2 == 0:
                break     

        for i in range(text_rows):
            for j in range(key_dimensions):
                text_tbc[i][j] = text_block[r]
                r+=1

                #chara = input("CHAR> ")
                #text_tbc[i][j] = chara
            
        print("\nHere is the text you inputed in matrix form:")
        for i in text_tbc:
            print(i)
    
        print()
        print("Here it is just normally:")
        for i in text_tbc:
            for j in i:
                print(j,end='')
        print()
    
        #Encryption Time:
        def block_encryption(text_rows, key_dimensions, key, text_tbc):
            for i in range(text_rows):
                for j in range(key_dimensions):
                    if text_tbc[i][j] in numbers:
                        text_tbc[i][j] = text_tbc[i][j]

                    elif text_tbc[i][j] in alphabet_lower:
                        text_tbc[i][j] = alphabet_lower.index(text_tbc[i][j]) + 1

                    elif text_tbc[i][j] in alphabet_upper:
                        text_tbc[i][j] = alphabet_upper.index(text_tbc[i][j]) + 1


            block_cipher = [['a' for i in range(key_dimensions)]for j in range(text_rows)]

            
            multiply = numpy.matmul(text_tbc,key)
            #print(multiply)
            list1 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25]
            list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
            for i in range(len(multiply)):
                for j in range(len(multiply[0])):
                    if (multiply[i][j] not in list2) or (multiply[i][j] not in list2):
                        multiply[i][j] = multiply[i][j] % 26
            #print(multiply)
    
       
            for i in range(len(multiply)):
                for j in range(len(multiply[0])):
                    block_cipher[i][j] = alphabet_lower[multiply[i][j]-1]
       
            encrypted_block_text = ''
            for i in block_cipher:
                for j in i:
                    encrypted_block_text += j
            return encrypted_block_text
        print()
        print(f"Your final encryption is:\n{block_encryption(text_rows, key_dimensions, key, text_tbc)}")  
        print()
        print("Lets name the cipher you created.")
        block_cipher_name = str(input("NAME> "))
        print()
        block_file_name = str(input("\nPlease input the file to be written to.\nFILE> "))
        with open(block_file_name, 'w') as File_B:
            File_B.write(f"{block_cipher_name}:")
            File_B.write("\n")
            File_B.write("\n")
            File_B.write("KEY:")
            File_B.write("\n")
            for i in key:
                File_B.write(str(i))
                File_B.write("\n")

            File_B.write("\n")
            File_B.write("Encrypted Message:")
            File_B.write("\n")
            File_B.write(block_encryption(text_rows, key_dimensions, key, text_tbc))
        
        print(f"\nThe {block_cipher_name} information has successfully been written into your {block_file_name} file.")
        print()
        keep_going = str(input("Would you like to create another cipher?\nYES/NO> "))
        # ---------------------------------------------------



    # Option 3 - Custom Hash Alg from class -------------------------- 

    if ((user_cipher_choice == '3') or (user_cipher_choice.lower() == 'three')):
        print()
        print("You chose a hash encryption!\nI would tell you a hashing joke but you'd only get it one way.")
        print()
        print("Now let's create a custom hash similar to the one we used in class.")
        print("\nHere's the steps what our hash will look like:")
        print()
        print("STEP 1: Convert all letters to their number indexes while leaving numbers alone.")
        print("STEP 2: Add all the numbers together.")
        print("STEP 3: Take the remainder of STEP 2 divided by some number you pick.")
        print("STEP 4: Add some number you pick to the remainder, then multiply the result with another number you decide.")
        print("STEP 5: Reverse the digits in STEP 4 and exchange each digit with its corresponding letter.")
        print()
        print("Now that we have our hashing algorithm lets input the text you wish to encrypt and the missing unknowns.\n")
    
        hashing_text = str(input("First, input the text to be encrypted (NOTE: Do not use special characters).\nTEXT TO BE ENCRYPTED> "))
        while True:
            count3 = 0
            for i in range(len(hashing_text)):
                if not((hashing_text[i] in alphabet_lower) or (hashing_text[i] in alphabet_upper) or (hashing_text[i] in numbers) or (hashing_text[i] == ' ')):
                    print("ERROR> Please only input letters, numbers, and spaces.")
                    hashing_text = str(input("Input the text to be encrypted (NOTE: DO NOT use special characters).\nTEXT> "))
            if count3 == 0:
                break
                
                
        print("\nNow that we have the text to be encrypted, lets input our unknowns.")
        print()
        print("Please enter a integer for the sum of your encryption text to be modded by:")
        mod_num = int(input("INT for % > "))
        print()
        print("Please enter a integer to add to the resuling remainder:")
        add_remainder = int(input("INT to add to remainder> "))
        print()
        print("Please enter a integer to multiply the result of your previous input by:")
        multiply_result = int(input("INT to multiply result> "))
        print()

        #Encryption time:
        def hash_encryption(hashing_text, mod_num, add_remainder, multiply_result):
            #num_text = ''
            alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0','1','2','3','4','5','6','7','8','9']
            hash_sum = 0
            hashing_text = hashing_text.lower()
            for i in range(len(hashing_text)):
                if hashing_text[i] in alphabet_lower:
                    #num_text += str(alphabet_lower.index(hashing_text[i])+1)
                    hash_sum += (alphabet_lower.index(hashing_text[i])+1)
                elif hashing_text[i] in alphabet_upper:
                    #num_text += str(alphabet_upper.index(hashing_text[i])+1)
                    hash_sum += (alphabet_lower.index(hashing_text[i])+1)
                elif hashing_text[i] in numbers:
                    #num_text += str(hashing_text[i])
                    hash_sum += int(hashing_text[i])
                else:
                    hash_sum += 0
            
                
            hash_sum = (hash_sum % mod_num) + add_remainder
            hash_sum *= multiply_result
            hash_result = str(hash_sum)
            hash_reversed = hash_result[::-1]
            hash_final = ''
            for i in range(len(hash_result)):
                hash_final += alphabet_lower[int(hash_reversed[i])-1]

            return hash_final

        print(f"Your hash has been created from {hashing_text} and it is...")
        print(hash_encryption(hashing_text, mod_num, add_remainder, multiply_result))
        print()
        print("Lets give your custom hash a creative name.")
        hash_name = str(input("NAME> "))
        print()
        print(f"Now we can write {hash_name} into a file of your chosing.\n") 
        print(f"Please input the file you would like your {hash_name} hash written to.")
        hash_file_name = str(input("FILE> "))

        with open(hash_file_name, 'w') as Hash_File:
            Hash_File.write(f"{hash_name}:")
            Hash_File.write("\n")
            Hash_File.write("\n")
            Hash_File.write(hash_encryption(hashing_text, mod_num, add_remainder, multiply_result))
            Hash_File.write("\n")
            Hash_File.write("\n")
            Hash_File.write("Number Inputs:")
            Hash_File.write("\n")
            Hash_File.write(str(mod_num))
            Hash_File.write("\n")
            Hash_File.write(str(add_remainder))
            Hash_File.write("\n")
            Hash_File.write(str(multiply_result))
        print(f"The {hash_name} has been successfully written to the {hash_file_name} file.")
        print()
        keep_going = str(input("Would you like to create another cipher?\nYES/NO> "))

        # ------------------------------------------------



# Decryptions for shift/block ciphers ----------------------------------------------------------

print()
keep_going2 = 'yes'

decrypt_option = str(input("Would you like to decrypt any of your ciphers?\nYES/NO> "))
#while not((keep_going2.lower() == "no")or(keep_going2.lower() == 'n')):

    

while(decrypt_option.lower() == 'yes') or (decrypt_option.lower() == 'y') or (decrypt_option.lower() == 'ya') or (decrypt_option.lower() == 'yeah'):
        print()
        print("Please choose one of the options below:")
        print("1.) Decrypt Your Shift Cipher (with shift)")
        print("2.) Decrypt Your Block Cipher")

        user_decrypt_choice = str(input("\nOPTION NUMBER> "))

        while not((user_decrypt_choice == '1') or (user_decrypt_choice == '2') or (user_decrypt_choice.lower() == 'one') or (user_decrypt_choice.lower() == 'two')):
            print("ERROR> Please only input 1 or 2 to continue.")
            user_decrypt_choice = str(input("OPTION NUMBER> "))
        #Shift Cipher Decryption (w/ shift) ----------------------------------------    
        if user_decrypt_choice.lower() == 'one' or user_decrypt_choice == '1':
            print("\nYou chose to decrypt your Shift Cipher!\n")

            deshif = int(input("Enter the shift of your encrypted text.\nSHIFT> "))
            print()
            text2decipher = str(input("Enter the encryped text.\nENCRYPTED TEXT> "))
            deshift = deshif * -1
            
            list1 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25]
            list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
            def decrypt_shift(text2decipher, deshift):
                if (deshift not in list1) or (deshift not in list2):
                    deshift = (deshif % 26)*-1
                
                alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

                deshifted_alphabet_lower = alphabet_lower[int(deshift):] + alphabet_lower[:int(deshift)]
                deshifted_alphabet_upper = alphabet_upper[int(deshift):] + alphabet_upper[:int(deshift)]
                deshifted_text = ''
    
                for i in range(len(str(text2decipher))):
                    if str(text2decipher)[i] in alphabet_lower:
                        index = alphabet_lower.index(text2decipher[i])
                        deshifted_text += deshifted_alphabet_lower[index]
                    elif str(text2decipher)[i] in alphabet_upper:
                        index = alphabet_upper.index(text2decipher[i])
                        deshifted_text += deshifted_alphabet_upper[index]
                    else:
                        deshifted_text += str(text2decipher)[i]

                return deshifted_text

            print()
            print(f"{text2decipher} shifted by {deshif} decryped is:\n{decrypt_shift(text2decipher, deshift)}")
            print()
            decrypt_option = str(input("Would you like to decrypt again?\nYES/NO> "))
            # ---------------------------------------------------------------------------------



        # --------- Decryption of block cipher ---------------------------------------------------
        if user_decrypt_choice.lower() == 'two' or user_decrypt_choice == '2':
            print("You chose to decrypt your Block Cipher!")
            
            alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0','1','2','3','4','5','6','7','8','9']
            print()
            dekey_dimensions = int(input("\nEnter the length and width (N X N) of your matrix key:\nN> "))
            dekey = [['b' for i in range(dekey_dimensions)]for j in range(dekey_dimensions)]

            
            for i in range(dekey_dimensions):
                for j in range(dekey_dimensions):
                    dekey_input = int(input(f"Enter the Integer of your key at ({i},{j})\nINT @ [{i}],[{j}]> "))
                    dekey[i][j] = dekey_input 
            

            print("\nHere is your key:")
            for i in dekey:
                print(i)

            print()
            print("Here is the inverse of your key:")

            invkey = numpy.linalg.inv(dekey)
 
            for i in invkey:
                print(i)
            
 
            print(f"What is the length of the encrypted text your are decrypting?")
            decrypt_length = int(input("LENGTH> "))
            print()
            
            while decrypt_length % dekey_dimensions != 0:
                print("ERROR> Length is not divisble with rows of your key (NOTE: Make sure the length of the text % the length of the rows in your key is zero.")
                print()
                print(f"What is the length of the encrypted text your are decrypting?")
                decrypt_length = int(input("LENGTH> "))

            detext_rows = int(decrypt_length / dekey_dimensions)
                
  
            detext_length = detext_rows * dekey_dimensions
            text_tbd = [['c' for i in range(dekey_dimensions)]for j in range(detext_rows)]

            #for i in text_tbc:
                #print(i)

            print("Enter the text (ONLY LETTERS) of your encrypted message or text.")
            v = 0
            detext_block = str(input(f"TEXT WITH LENGTH OF {decrypt_length}> "))
    

            while len(detext_block) != (decrypt_length): 
                if len(detext_block) > (decrypt_length):
                    print(f"ERROR> Input was too long, make sure input has exactly {decrypt_length} characters")
                if len(detext_block) < (decrypt_length):
                    print(f"ERROR> Input was too short, make sure input has exactly {decrypt_length} characters")
                detext_block = str(input(f"TEXT WITH LENGTH OF {decrypt_length}> "))

            while True:

                count2 = 0
                for i in range(len(detext_block)):
                    if not((detext_block[i] in alphabet_lower) or (detext_block[i] in alphabet_upper)):
                        print(f"ERROR> Part of input was not a letter. Please use ONLY LETTERS")
                        detext_block = str(input(f"TEXT WITH LENGTH OF {decrypt_length}> "))
                        count2+=1

                if count2 == 0:
                    break     

            for i in range(detext_rows):
                for j in range(dekey_dimensions):
                    text_tbd[i][j] = detext_block[v]
                    v+=1

                    #chara = input("CHAR> ")
                    #text_tbc[i][j] = chara
            
            print("\nHere is the encrypted text you inputed in matrix form:")
            for i in text_tbd:
                print(i)
    
            print()
            print("Here it is just normally:")
            for i in text_tbd:
                for j in i:
                    print(j,end='')
            print()
    
            #Encryption Time:
            def block_decryption(detext_rows, dekey_dimensions, invkey, text_tbd):
                for i in range(detext_rows):
                    for j in range(dekey_dimensions):
                        if text_tbd[i][j] in numbers:
                            text_tbd[i][j] = text_tbd[i][j]

                        elif text_tbd[i][j] in alphabet_lower:
                            text_tbd[i][j] = alphabet_lower.index(text_tbd[i][j]) + 1

                        elif text_tbc[i][j] in alphabet_upper:
                            text_tbd[i][j] = alphabet_upper.index(text_tbd[i][j]) + 1


                #deblock_cipher = [[0 for i in range(dekey_dimensions)]for j in range(detext_rows)]

                matrix_mul = numpy.matmul(text_tbd,invkey)
                for i in matrix_mul:
                    for j in i:
                        j = round(j,0)
                
                matrix_mul = matrix_mul.astype(numpy.int64)
                #print(matrix_mul)

                for i in range(len(matrix_mul)):
                    for j in range(len(matrix_mul[0])):
                        if matrix_mul[i][j] not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
                            matrix_mul[i][j] = matrix_mul[i][j] % 26

                #print(matrix_mul)
                finals = ''
                finalz = [['a' for i in range(len(matrix_mul[0]))]for j in range(len(matrix_mul))]
                for i in range(len(matrix_mul)):
                    for j in range(len(matrix_mul[0])):
                        finalz[i][j] = alphabet_lower[matrix_mul[i][j]-1]
                        finals+= finalz[i][j]


                return finals
                        
            print(f"\nYour decryption is:\n{block_decryption(detext_rows, dekey_dimensions, invkey, text_tbd)}")
            print()
            decrypt_option = str(input("Would you like to decrypt again?\nYES/NO> "))
            # ----------------------------------------------------------------------------------------------


# Exit --------------------------------------------------

print(" _____________________________________________ ")
print("|                                             |")
print("| Thank You For Using Create Your Own Cipher! |")
print("|_____________________________________________|")

print()
print("Goodbye!")
print("===============================================")

       
            

        

        
