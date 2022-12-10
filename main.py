
def asalsayı(sayı):
    sayı = int(sayı)
    for i in range(2,sayı):
        islem = str(sayı / i).split('.')
        if islem[1] == "0":
            return "Asal Değil "+str(i)+" bölünüyor"
        if islem[1] == "0":
            break
        elif i == sayı-1:
            return "Asal"
        
    
print(asalsayı(24242424))
