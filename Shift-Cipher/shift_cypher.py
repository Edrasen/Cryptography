import os

def openf():
    m = open ("test.txt", "r")
    p = list(m.read())
    p1 = "".join(p)
    return p1

def de_openf():
    m = open ("cifrado.txt", "r")
    #for line in m.readlines():
    p = list(m.read())
    #print(p)
        #print(type(p))
    p1 = "".join(p)
    return p1

def toascii(p):
    l = []
    for element in p:
        l.append(ord(element))
    #print(l)
    return l

def encrp(l, key):
    M = []
    for element in l:
        element = element + key
        M.append(chr(element))
    return M

def decrp(l, key):
    M = []
    for element in l:
        if (element == 10):
            M.append(chr(element))
        else:
            element = (element + (-key))%256
            M.append(chr(element))
    return M

def createf(M):
    if os.path.exists("cifrado.txt"):
        os.remove("cifrado.txt")
    else:
        print("The file does not exist") 
    f = open("cifrado.txt", "a")
    for element in M:
        f.write(element)
    f.close()
    f = open("cifrado.txt", "r")
    #print(f.read()) 
    print("\nArchivo con MENSAJE CIFRADO creado!! :)\n")


def de_createf(M):
    if os.path.exists("descifrado.txt"):
        os.remove("descifrado.txt")
    else:
        print("The file does not exist") 
    f = open("descifrado.txt", "w")
    for element in M:
        if(element == "\n"):
            f.write("\n")
        else:
            f.write((element))
    f.close()
    f = open("descifrado.txt", "r")
    #print(f.read()) 
    print("\nArchivo con MENSAJE DESCIFRADO creado!! :)\n")
 

def main():
    i = 0
    print("\nWELCOME TO SHIFT CIPHER PROGRAM!!\n")
    while True:
        i = int(input("Seleccione una de las siguientes opciones: 1.Encrypt  2.Decrypt  3.Salir\n\n"))
        if(i == 1):
            key = int(input("\nIntroduzca la llave de cifrado: "))
            p1 = openf()
            M = encrp(toascii(p1), key)
            createf(M)

        elif(i == 2):
            key = int(input("\nIntroduzca la llave de descifrado: "))
            p1 = de_openf()
            M = decrp(toascii(p1), key)
            de_createf(M)

        elif(i == 3):
            break
main()
