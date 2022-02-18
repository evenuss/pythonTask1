def hapus(perintah):
    arrayText.remove(perintah)
    str1 = " " 
    
    # return string  
    return(str1.join(arrayText))


def sisip(perintah,index):
    arrayText.insert(index,perintah)
    str1 = " " 
    
    # return string  
    return(str1.join(arrayText))

def tambah(perintah):
    arrayText.append(perintah)
    str1 = " " 
    
    # return string  
    return(str1.join(arrayText))


text = str(input("Masukan Text"))
arrayText = text.split(" ")

perintah = str(input("Perintah"))

arrayPerintah = perintah.split(" ")
panggilFungsiPerintah = arrayPerintah[0]
indexPerintah = arrayPerintah[1:len(panggilFungsiPerintah)]


if panggilFungsiPerintah == "hapus":
    print(hapus(indexPerintah[0]))
elif panggilFungsiPerintah == "tambah":
    print(tambah(indexPerintah[0]))  
elif panggilFungsiPerintah == "sisip":
    print(sisip(indexPerintah[0],int(indexPerintah[1])))