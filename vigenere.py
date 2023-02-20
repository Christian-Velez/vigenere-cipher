# file: vigenere.py

class VigenereCipher():
   def __init__(self) -> None:
      self.size = 89


   # Mathematical modulus operation
   def modulus(self, x: int) -> int:
      result: int = x % self.size

      if(result < 0):
         return result + self.size

      return result


   # Omits " and /"
   def isValidAsciiValue(self, value: int) -> bool:
      return value != 34 and value != 47


   # ASCII value to Z89
   def asciiToZ89(self, asciiValue: int) -> int:
      if(not self.isValidAsciiValue(asciiValue)):
         raise Exception("Invalid character: ", chr(asciiValue))

      if(asciiValue < 34):
         return asciiValue - 32

      if(asciiValue < 47):
         return asciiValue - 33

      return asciiValue - 34
   

   # Z89 value to ASCII
   def z89toAscii(self, z89Value: int) -> int:
      if(z89Value < 2):
         return z89Value + 32
      
      if(z89Value < 14):
         return z89Value + 33

      return z89Value + 34


   # Manipulates the key to have the same length as the input text
   def generateKeyStream(self, text: str, key: str) -> str:
      repeat : int = len(text) // len(key)
      remainder : int = len(text) % len(key)
      keyStream : str = (key * repeat) + key[:remainder]
      return keyStream


   # Receives a text and returns an array of integers representing z89 values   
   def textToZ89(self, text: str) -> list[int]:
      characters: list[str] = list(text)
      asciiValues: list[str] = list(map(ord, characters))
      z89Values: list[int] = list(map( self.asciiToZ89, asciiValues))
      return z89Values


   def encrypt(self, plainText: str, key: str) -> str:
      keyStream: str = self.generateKeyStream(plainText, key)

      entryInZ89: list[int] = self.textToZ89(plainText)
      keyStreamInZ89: list[int] = self.textToZ89(keyStream)
      resultInZ89: list[int] = []

      for i in range(len(entryInZ89)):
         value: int = self.modulus(entryInZ89[i] + keyStreamInZ89[i])
         resultInZ89.append(value)

 
      resultInAscii: list[int] = list(map(self.z89toAscii, resultInZ89))
      resultInCharacters: list[int] = list(map(chr, resultInAscii))

      return "".join(resultInCharacters)


   def decrypt(self, encryptedText: str, key: str) -> str:
      keyStream: str = self.generateKeyStream(encryptedText, key)

      encryptedTextInZ89: list[int] = self.textToZ89(encryptedText)
      keyStreamInZ89: list[int] = self.textToZ89(keyStream)
      resultInZ89: list[int] = []


      for i in range(len(encryptedTextInZ89)):
         value = self.modulus(encryptedTextInZ89[i] - keyStreamInZ89[i])
         resultInZ89.append(value)


      resultInAscii: list[int] = list(map(self.z89toAscii, resultInZ89))
      resultInCharacters: list[int] = list(map(chr, resultInAscii))

      return "".join(resultInCharacters)
