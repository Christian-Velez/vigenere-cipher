# file: index.py
from os import system, name
from vigenere import VigenereCipher
 
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')

def printMenu():
   clear()
   print("Main menu")
   print("a. Encrypt")
   print("b. Decrypt")
   print("e. Exit")


def encryptMenu():
   print("\nEncrypt")

   cipher = VigenereCipher()
   inputFileName : str = input('Enter the input file name: ') + ".txt"
   outputFileName : str = input('Enter the output file name (default: "e-results.txt"): ')
   key : str = input('Enter a key: ')

   if(len(outputFileName) == 0):
      outputFileName = "e-results.txt"
   else:
      outputFileName = outputFileName + ".txt"

   inputFile = open(inputFileName, "r")
   outputFile = open(outputFileName, "w")
   lines = inputFile.read().splitlines()

   print("\n\nEncrypting...")
   for line in lines:
      encrypted : str = cipher.encrypt(line, key)
      outputFile.write(encrypted + "\n")
      print(line, " = ", encrypted)

   print("\nFinished. Results in ", outputFileName)

   inputFile.close()
   outputFile.close()
   input()

def decryptMenu():
   print("\nDecrypt")
   cipher = VigenereCipher()
   inputFileName : str = input('Enter the input file name: ') + ".txt"
   outputFileName : str = input('Enter the output file name (default: "d-results.txt"): ')
   key : str = input('Enter a key: ')

   if(len(outputFileName) == 0):
      outputFileName = "d-results.txt"
   else:
      outputFileName = outputFileName + ".txt"

   inputFile = open(inputFileName, "r")
   outputFile = open(outputFileName, "w")
   lines = inputFile.read().splitlines()

   print("\n\nDecrypting...")

   for line in lines:
      decrypted : str = cipher.decrypt(line, key)
      outputFile.write(decrypted + "\n")
      print(line, " = ", decrypted)

   print("\nFinished. Results in ", outputFileName)

   inputFile.close()
   outputFile.close()
   input()




def main():
   opc = ''

   while opc != 'e':
      printMenu()
      opc = input('> ')

      if(opc == 'a'):
         encryptMenu()

      elif(opc == 'b'):
         decryptMenu()
         
main()




