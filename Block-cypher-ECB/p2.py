from PIL import Image
from Crypto.Cipher import AES

filename = "corazon.bmp"
filenamedec = "corazon_enc.bmp"
filename_out2 = "corazon_dec"
filename_out = "corazon_enc"
format = "bmp"
key = "abaababbcdccdcdd"

def pad(data):
    return data + b"\x00"*(16-len(data)%16)


def dec_pad(data):
    return data + b"\x00"*(16+len(data)%16)


def convert_to_RGB(data):
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r,g,b))
    return pixels

def process_image(filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()

    original = len(data)

    new = convert_to_RGB(aes_ecb_encrypt(key, pad(data))[:original])

    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)

    im2.save(filename_out+"."+format, format)

# ECB
def aes_ecb_encrypt(key, data, mode=AES.MODE_ECB):
    aes = AES.new(key, mode)
    new_data = aes.encrypt(data)
    return new_data

def dec_process_image(filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()

    original = len(data)

    new = convert_to_RGB(aes_ecb_decrypt(key, pad(data))[:original])

    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)

    im2.save(filename_out2+"."+format, format)

def aes_ecb_decrypt(key, data, mode=AES.MODE_ECB):
    aes = AES.new(key, mode)
    new_data = aes.decrypt(data)
    return new_data

def main():
    i = 0
    print("\nWELCOME TO IMAGE CIPHER PROGRAM!!\n")
    while True:
        i = int(input("Please select one of the next options: 1.Encrypt  2.Decrypt  3.Exit\n"))
        if(i == 1):
            process_image(filename)
            print("\n\nImage succesfully encrypted!! :)\n")
        elif(i == 2):
            dec_process_image(filenamedec)
            print("\n\nImage succesfully decrypted!! :)\n")
        elif(i == 3):
            break
main()
