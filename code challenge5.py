File = open("Fileprogram.txt", 'r')
content = File.read()
print(content)
File.close()

File = open("Fileprogram.txt", 'w')
File.write("first fileprogram \n")
File.close()

File = open("Fileprogram.txt", 'a')
File.write("am append ")
File.close()
