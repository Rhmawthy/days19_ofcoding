#penggunaan continue
#continue berfungsi untuk melompat ke aksi selanjutnya tanpa harus mengeksekusi aksi yang dibawhnya. misal 1 contoh

angka = int(input("masukkan angka:"))
number = 0

while number < angka:
    number += 1
    print(number) # aksi 1

    if number == 3:
        print("upss") 
        continue #loop akan meloncat
    print ("oke")#aksi 2
        
       
       
        
       
        
    
