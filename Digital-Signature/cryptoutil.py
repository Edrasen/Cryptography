import hashlib

lines = 0

def copyFile2(file):  
    input_output = open("elvis_signed.txt", "w")
    inp = open(str(file) , "r")                  #Function to copy text from original file
    for line in inp:
        input_output.write(line)
    inp.close()

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
    flag = validation(hash_original, verif_hash) 
    print(flag)   
    return flag

def readF(file_name):                                      #it helps to read digest in hashed message file
    fmessage = open(file_name, "r")
    content = fmessage.readlines()
    digesto = content[len(content)-1].strip("\n")
    return digesto

def firmar(file_name, privKey_file):            #saves signed and hashed message in new file
    digesto = readF(file_name)
    copyFile2(file_name)
    fmessage = open("elvis_signed.txt", "a")    

    fpriv = open(privKey_file, "r")
    datapriv = fpriv.read()
    datosPriv = datapriv.split(",")
    for charac in digesto:
        x = pow(ord(charac), int(datosPriv[2]), int(datosPriv[1]))
        fmessage.write(str(x)+"\n")
    fmessage.close()
    fpriv.close()

def gethash(file_name):                     #function to get hash from a signed file
    verif_lines = ""
    verif_hash = ""
    file = open(file_name, "r")
    data = file.readlines()
    tam = len(data)
    tammessage = tam - 43
    for line in range(0, tammessage):
        verif_lines = verif_lines + data[line]  
    verif_lines = verif_lines.strip()
    verif_lines = verif_lines.encode('utf-8')
    sha_1 = hashlib.sha1()
    sha_1.update(verif_lines)
    verif_hash = sha_1.hexdigest()
    print(verif_hash)
    return verif_hash



def validar_firma(file_name, pubKey_file):      #it validate if hash and Signd decryption do match
    firmaDes = []
    verif = ""
    flag = True
    fverif = open(file_name, "r")
    fpub = open(pubKey_file, "r")
    Sign_data = fverif.readlines()
    datapub = fpub.read()
    datosPub = datapub.split(",")
    len_sign = len(Sign_data)
    tam = len_sign
    tamfin = tam-40
    fverif.close()
    fpub.close()
    print(tam, tamfin)
    for elem in range(tamfin, tam):
        y = pow(int(Sign_data[elem]), int(datosPub[2]), int(datosPub[1]))
        firmaDes.append(chr(y))
    verif = gethash(file_name)
    validated_sign = "".join(firmaDes)
    print(validated_sign)
    flag = validation(validated_sign, verif)
    return flag
    