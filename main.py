#manejo de archivos
archivo1=open('holamundo.txt', 'w')
archivo1.close()
archivo1=open('holamundo.txt', 'r')
print(archivo1)
archivo1.close()
archivo1=open('holamundo.txt', 'w+')
archivo1.write("En el mundo de los ciegos el tuerto es el rey, ")
archivo1.flush
archivo1.write("Al saber lo llaman suerte")
archivo1.close()
archivo1=open('holamundo.txt', 'r+')
print(archivo1.read())
archivo1.seek(7)
print(archivo1.readline())