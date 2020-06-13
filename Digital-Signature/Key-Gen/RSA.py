import random, sys, os, rabinMiller, cryptomath

def main():
   makeKeyFiles('my', 1024)

def generateKey(keySize):
   # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
   print('Generating p prime...')
   p = rabinMiller.generateLargePrime(keySize)
   print('Generating q prime...')
   q = rabinMiller.generateLargePrime(keySize)
   n = p * q
   print("\nN is: "+str(n) + "\n")
   # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
   print('Generating e that is relatively prime to (p-1)*(q-1)...')
   while True:
      e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
      if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
         break
   
   # Step 3: Calculate d, the mod inverse of e.
   print('Calculating d that is mod inverse of e...')
   d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
   print("\nD is: ", d)         #Esta es la que se queda el propietario
   print("\nE is: ", e)         #Esta es la que se publica junto a n
   publicKey = (n, e)
   privateKey = (n, d)
   print('\nPublic key:', publicKey)
   print('\nPrivate key:', privateKey)
   return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    #Creates two files 'x_pubkey.txt' and 'x_privkey.txt' 
    #(where x is the value in name) with the the n,e and d,e integers written in them,
    #delimited by a comma.
   if os.path.exists('%sPubkey.txt' % (name)) or os.path.exists('%sPrivkey.txt' % (name)):
      sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))
   publicKey, privateKey = generateKey(keySize)
   print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(privateKey)))) 
   print('Writing public key to file %sPubkey.txt...' % (name))
   
   fo = open('%sPubkey.txt' % (name), 'w')
   fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
   fo.close()
   print()
   print('The private key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
   print('Writing private key to file %sPrivkey.txt...' % (name))
   
   fo = open('%sPrivkey.txt' % (name), 'w')
   fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
   fo.close()

if __name__ == '__main__':
   main()
   
