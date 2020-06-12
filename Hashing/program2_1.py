import hashlib

lines = 0

def copyFile(file):  
    input_output = open("elvis_h.txt", "w")
    inp = open(str(file) , "r")                  #Function to copy text from original file
    for line in inp:
        input_output.write(line)
    inp.close()


def hashing(file):                   #it generates concat file with both original and hash text
    input_output = open("elvis_h.txt", "a")
    copyFile(file)                   #copiamos el contenido del archivo original
    inp2 = open(str(file) , "r")
    global lines
    input_output.write("\n################# HASH #################\n")
    
    
    plain = inp2.read()
    print(str(plain))
    plain = plain.strip()
    plain = plain.encode('utf-8')
    sha_1a = hashlib.sha1()
    sha_1a.update(plain)
    input_output.write(sha_1a.hexdigest())
    print(lines)  
    return lines                  #it count the number of lines on original file

def validation(original, new):
    if original == new:
        return True
    else:
        return False    


def validate_hash(file):                #to verify integrity on the file
    flag = True
    verif_hash = ""                     #auxiliar to save the new hash
    verif_lines = ""                    #auxiliar var to save each line of the origibal message
    hash_original = ""                  #auxiliar to save the original in file hash
    
    f_validate = open(str(file), "r")   
    validate = f_validate.readlines()
    lineas_msg = len(validate) - 3

    hash_original = validate[lineas_msg+2].strip('\n')      #getting the original hashing witouth jumpline
    
    for lineasmsg in range(0, lineas_msg):                  
        verif_lines = verif_lines + validate[lineasmsg]     #adding each line from the origial message
    
    #print(verif_lines)                                     #i file message saved on aux variable
    verif_lines = verif_lines.strip()
    verif_lines = verif_lines.encode('utf-8')
    sha_1 = hashlib.sha1()
    sha_1.update(verif_lines)
    verif_hash = sha_1.hexdigest()
    #print("Verif hash: " + verif_hash)
    #print("Origi hash: " + hash_original)
    flag = validation(hash_original, verif_hash) 
    print(flag)   
    return flag
