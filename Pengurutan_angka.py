def bubble_sort(arr):
    """
    Fungsi untuk mengurutkan elemen-elemen dalam sebuah array menggunakan algoritma Bubble Sort.

    Parameters:
        arr (list): Array yang akan diurutkan.

    Returns:
        None. Array akan diurutkan secara in-place.

    """
    # Untuk menghitung panjang array dan menyimpannya dalam variabel n
    n = len(arr)  
    # Looping atau perulangan untuk melakukan iterasi sebanyak n kali
    for i in range(n):  
        # Looping atau perulangan untuk membandingkan elemen-elemen array
        for j in range(0, n-i-1):  
            # sebuah decision untuk memeriksa apakah nilai elemen saat ini lebih besar dari nilai elemen berikutnya
            if arr[j] > arr[j+1]:  
                # lalu jika nilai elemen saat ini lebih besar, dilakukan pertukaran nilai antara elemen saat ini dan elemen berikutnya
                arr[j], arr[j+1] = arr[j+1], arr[j]  
                
def save_to_file(arr):
    """
    Menyimpan setiap elemen dari array ke dalam file "pengurutan_angka.txt"

    Parameters:
    arr (list): List yang berisi elemen-elemen yang akan disimpan ke dalam file

    Returns:
    None
    """
    # Membuka file "pengurutan_angka.txt" dengan mode menulis
    with open("pengurutan_angka.txt", "w") as file:  
        # perulangan melalui setiap elemen dalam array
        for number in arr:   
            # Menuliskan setiap elemen ke dalam file dengan tambahan newline
            file.write(f"{number}\n") 
            
def read_from_file():
   """
    Membaca nilai-nilai dari file "pengurutan_angka.txt" dan menampilkannya.

    Args:
    None

    Returns:
    None
    """
   # Membuka file "pengurutan_angka.txt" dalam mode baca
   with open("pengurutan_angka.txt", "r") as file: 
        # Membaca setiap baris dari file ke dalam list lines
        lines = file.readlines()
        # Menghapus leading dan trailing whitespace dari setiap baris
        lines = [line.strip() for line in lines]     
        # Menyisipkan setiap baris ke dalam string output dan Menggabungkan setiap baris menjadi satu string dengan pemisah koma
        output = ', '.join(lines)
            # Menampilkan nilai tugas yang telah dibaca dari file
        print("Nilai tugas: ", output) 
        print("\n")

def main():
    while True: 

        print("\n"+"MENU PILIHAN") 
        print("1. Input angka")
        print("2. Tampil hasil pengurutan")
        print("3. Selesai")
        
        pilihan = input("Masukkan pilihan [1/2/3]: ")
        print("\n")

        if pilihan == "1":    
            print("INPUT ANGKA")
            print("\n")
            n = int(input("Masukkan jumlah angka yang akan diinput: "))
            print("Input Angka Secara Acak")
            print("----------------------------")
        
            numbers = []
            for i in range(n):
                number = int(input(f"Angka {i+1}: "))
                numbers.append(number)
                
            bubble_sort(numbers)  
            save_to_file(numbers)  
            print("\n")
            
        elif pilihan == "2":   
            print("TAMPIL HASIL PENGURUTAN")
            print("\n")
            read_from_file() 
        
        elif pilihan == "3":
            print("Terima Kasih, Program Selesai.")
            break 
            
        else:
            print("Pilihan yang Anda masukkan tidak valid. Silakan coba lagi.")
            
main() 