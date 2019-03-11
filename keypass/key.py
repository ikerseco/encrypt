import os
import random

class keyPass(object):
    def __init__(self,directorio):
        self.directorio = directorio
    
    def keypassSortu(self):
        os.chdir(self.directorio)
        dire = os.listdir(self.directorio)
        text = ""
        letrak = ["q","Q","w","W","r","R","t","Y","y","U","u","I","i","O","o","P","p","A","a","S","s","D","d","F","f","G","g","H","h","J","j","K","k","l","L","ñ","Ñ","z","Z","x","X","c","C","v","V","b","B","n","N","m","M","1","2","3","4","5","6","7","8","9","0","!","@","$","%","&","/","?","¿","^","*","Ç",";"]
        for x in dire: 
          fichategia = open(x,'rt')
          irakurri =  fichategia.read()
          for t in range(len(irakurri)):
            for j in range(random.randint(0,120)):
                nun = random.randrange(len(letrak)) 
                text += letrak[nun]
            text +=  "\n"
        fichategia = open ("keyPass.txt",'wt')
        fichategia.write(text)
        fichategia.close()
        print(text)
        print(dire)


key = keyPass("C:\\Users\\web\\Desktop\\passw")
key.keypassSortu()