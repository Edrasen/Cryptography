from PIL import Image
from Crypto.Cipher import DES


filename = "paisaje.bmp"
format = "bmp"

def pad(data):
    return data + b"\x00"*(8-len(data)%8)

def dec_pad(data):
    return data + b"\x00"*(8+len(data)%8)

def convert_to_RGB(data):
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r,g,b))
    return pixels

def process_image(filename, key, mode):
    filename_out = ""
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()

    original = len(data)

    if mode == 1:
        op_mode = DES.MODE_ECB
        filename_out = "corazon_ECB"
    elif mode == 2:
        op_mode = DES.MODE_CBC
        filename_out = "corazon_CBC"
    elif mode == 3:
        op_mode = DES.MODE_CFB
        filename_out = "corazon_CFB"
    else:
        op_mode = DES.MODE_OFB
        filename_out = "corazon_OFB"
    
    new = convert_to_RGB(encrypt(key, pad(data), op_mode)[:original])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)
    im2.save(filename_out+"."+format, format)

def dec_process_image(filename, key, mode):
    filename_out = ""
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()

    original = len(data)

    if mode == 1:
        op_mode = DES.MODE_ECB
        filename_out = "deccorazon_ECB"
    elif mode == 2:
        op_mode = DES.MODE_CBC
        filename_out = "deccorazon_CBC"
    elif mode == 3:
        op_mode = DES.MODE_CFB
        filename_out = "deccorazon_CFB"
    else:
        op_mode = DES.MODE_OFB
        filename_out = "deccorazon_OFB"
    
    new = convert_to_RGB(decrypt(key, dec_pad(data), op_mode)[:original])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)
    im2.save(filename_out+"."+format, format)

def encrypt(key, data, mode):
    if mode == DES.MODE_ECB:
        cipher = DES.new(key, mode)
        new_data = cipher.encrypt(data)
    else:
        iv = "A"*8
        cipher = DES.new(key, mode, iv)
        new_data = cipher.encrypt(data)
    return new_data

def decrypt(key, data, mode):
    if mode == DES.MODE_ECB:
        cipher = DES.new(key, mode)
        new_data = cipher.decrypt(data)
    else:
        iv = "A"*8
        cipher = DES.new(key, mode, iv)
        new_data = cipher.decrypt(data)
    return new_data

def main():
    i = 0
    print("\nWELCOME TO IMAGE CIPHER PROGRAM!!\n")
    while True:
        modo = int(input("\nIntroduzca el modo de operación deseado: \n 1. ECB \n 2. CBC \n 3. CFB \n 4. OFB \n"))
        i = int(input("\nPlease select one of the next options: 1.Encrypt  2.Decrypt  3.Exit\n"))
        if i == 1:
            key = input("Introduzca la llave: ")
            process_image(filename, key, modo)
            print("\n\n***** IMAGE SUCCESFULLY ENCRYPTED!! :) *****\n\n")
        elif i == 2:
            key = input("Introduzca la llave: ")
            if modo == 1:
                filenamedec = "corazon_ECB.bmp"
            elif modo == 2:
                filenamedec = "corazon_CBC.bmp"
            elif modo == 3:
                filenamedec = "corazon_CFB.bmp"
            elif modo == 4:
                filenamedec = "corazon_OFB.bmp"
            dec_process_image(filenamedec, key, modo)
            print("\n\n***** IMAGE SUCCESFULLY DECRYPTED!! :) *****\n\n")
        elif i == 3:
            break

main()
