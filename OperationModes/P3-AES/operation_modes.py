from PIL import Image
from Crypto.Cipher import AES

filename = "paisaje.bmp"
format = "bmp"

def pad(data):
    return data + b"\x00"*(16-len(data)%16)


def dec_pad(data):
    return data + b"\x00"*(16+len(data)%16)


def convert_to_RGB(data):
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r,g,b))
    return pixels

def process_image(filename, key, modo):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()

    original = len(data)

    if modo == 1:
        filename_out = "corazon_ECB"
        new = convert_to_RGB(aes_ecb_encrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out+"."+format, format)

    elif modo  == 2:
        filename_out = "corazon_CBC"
        new = convert_to_RGB(aes_cbc_encrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out+"."+format, format)

    elif modo  == 3:
        filename_out = "corazon_CFB"
        new = convert_to_RGB(aes_cfb_encrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out+"."+format, format)

    else:
        filename_out = "corazon_OFB"
        new = convert_to_RGB(aes_ofb_encrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out+"."+format, format)


def dec_process_image(filename, key, modo):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()

    original = len(data)

    if modo == 1:
        filename_out2 = "decCorazon_ECB"
        new = convert_to_RGB(aes_ecb_decrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out2+"."+format, format)

    elif modo  == 2:
        filename_out2 = "decCorazon_CBC"
        new = convert_to_RGB(aes_cbc_decrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out2+"."+format, format)

    elif modo  == 3:
        filename_out2 = "decCorazon_CFB"
        new = convert_to_RGB(aes_cfb_decrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out2+"."+format, format)

    else:
        filename_out2 = "decCorazon_OFB"
        new = convert_to_RGB(aes_ofb_decrypt(key, pad(data))[:original])
        im2 = Image.new(im.mode, im.size)
        im2.putdata(new)
        im2.save(filename_out2+"."+format, format)


######## ENCRYPTION FUCNTIONS #########

### ECB MODE
def aes_ecb_encrypt(key, data, mode=AES.MODE_ECB):
    aes = AES.new(key, mode)
    new_data = aes.encrypt(data)
    return new_data

### CBC MODE
def aes_cbc_encrypt(key, data ,mode=AES.MODE_CBC):
    IV = "A"*16  #We'll manually set the initialization vector to simplify things
    aes = AES.new(key, mode, IV)
    new_data = aes.encrypt(data)
    return new_data

### CFB MODE
def aes_cfb_encrypt(key, data ,mode=AES.MODE_CFB):
    IV = "A"*16  #We'll manually set the initialization vector to simplify things
    aes = AES.new(key, mode, IV)
    new_data = aes.encrypt(data)
    return new_data

### OFB MODE
def aes_ofb_encrypt(key, data ,mode=AES.MODE_OFB):
    IV = "A"*16  #We'll manually set the initialization vector to simplify things
    aes = AES.new(key, mode, IV)
    new_data = aes.encrypt(data)
    return new_data

######## DECRYPTION FUNCTIONS ########

### ECB MODE
def aes_ecb_decrypt(key, data, mode=AES.MODE_ECB):
    IV = "A"*16  #We'll manually set the initialization vector to simplify things
    aes = AES.new(key, mode)
    new_data = aes.decrypt(data)
    return new_data

### CBC MODE 
def aes_cbc_decrypt(key, data, mode=AES.MODE_CBC):
    IV = "A"*16  #We'll manually set the initialization vector to simplify things
    aes = AES.new(key, mode, IV)
    new_data = aes.decrypt(data)
    return new_data

### CFB MODE
def aes_cfb_decrypt(key, data, mode=AES.MODE_CFB):
    IV = "A"*16  #We'll manually set the initialization vector to simplify things
    aes = AES.new(key, mode, IV)
    new_data = aes.decrypt(data)
    return new_data

### OFB MODE
def aes_ofb_decrypt(key, data, mode=AES.MODE_OFB):
    IV = "A"*16  #We'll manually set the initialization vector to simplify things
    aes = AES.new(key, mode, IV)
    new_data = aes.decrypt(data)
    return new_data

def main():
    i = 0
    print("\nWELCOME TO IMAGE CIPHER PROGRAM!!\n")
    while True:
        i = int(input("Please select one of the next options: 1.Encrypt  2.Decrypt  3.Exit\n"))
        if(i == 1):
            key = input("Introduzca la llave: ")
            modo = int(input("Introduzca el modo de cifrado deseado: \n 1. ECB \n 2. CBC \n 3. CFB \n 4. OFB \n"))
            process_image(filename, key, modo)
            print("\n\nImage succesfully encrypted!! :)\n")
        elif(i == 2):
            key = input("Introduzca la llave: ")
            modo = int(input("Introduzca el modo de cifrado deseado: \n 1. ECB \n 2. CBC \n 3. CFB \n 4. OFB \n"))
            if modo == 1:
                filenamedec = "corazon_ECB.bmp"
            elif modo == 2:
                filenamedec = "corazon_CBC.bmp"
            elif modo == 3:
                filenamedec = "corazon_CFB.bmp"
            elif modo == 4:
                filenamedec = "corazon_OFB.bmp"
            dec_process_image(filenamedec, key, modo)
            print("\n\nImage succesfully decrypted!! :)\n")
        elif(i == 3):
            break
main()
