firma = []
firmaDes = []

def readF(file_name):
    fmessage = open(file_name, "r")
    content = fmessage.readlines()
    digesto = content[len(content)-1].strip("\n")
    return digesto

def firmar(file_name, pubKey_file):
    digesto = readF(file_name)
    fmessage = open(file_name, "a")    

    fpub = open(pubKey_file, "r")
    datapub = fpub.read()
    datosPub = datapub.split(",")
    for charac in digesto:
        x = pow(ord(charac), int(datosPub[2]), int(datosPub[1]))
        fmessage.write(str(x))
    fmessage.close()
    fpub.close()


def validar_firma(file_name, privKey_file):
    fpriv = open(privKey_file, "r")
    datapriv = fpriv.read()
    datosPriv = datapriv.split(",")
    for elem in firma:
        y = pow(int(elem), int(datosPriv[2]), int(datosPriv[1]))
        firmaDes.append(chr(y))

print("".join(firmaDes))