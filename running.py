# Define Integer
a = 5
print("Ulala ",a)

# Define String
name = "Ateng"
print("Ulala %s" %name)

# Print variable use String
print("Namanya %s dan nomor %d" %(name,a))

# Define List and print list
myList = [1,2,3]
print("Isi list-nya adalah %s "%myList)
print("Isi list-nya adalah",myList)

# Input
yourInput = input("Masukan sesuatu: ")
print("Ini hasil output dari inputanmu",yourInput)

# Check Data Type
x = 6
print(type(x))
x = 'Hello'
print(type(x))

# Branches
if False:
    print(1+1) # Output 2
else:
    print(1+2) # Output 3

# Length of String not allowed for numeric
string = "Si Ateng"
print(len(string))

# List
exampleList = [1,2,3,4,5,6,7,8,9,10]
print("Mengambil index ke 5 = ",exampleList[5])
print("Mengambil index awal dari belakang = ",exampleList[-1])
print("Mengambil index ke 3 sampai sebelum index ke 5 = ",exampleList[3:5])
print("Mengambil index awal sampai sebelum index 5 (index 4) = ",exampleList[:5])
print("Mengambil index awal dari belakang hingga index 3 dari belakang = ",exampleList[:-3])
