a. Mengimpor Tkinter
import tkinter as tk
untuk memanggil Tkinter, yaitu library Python yang digunakan untuk membuat tampilan aplikasi berupa jendela, tulisan, kotak input, dan tombol.

b. Membuat jendela
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550")
untuk membuat jendela utama aplikasi. root.title() berfungsi memberikan judul pada jendela, root.geometry() mengatur ukuran jendela menjadi lebar 400 dan tinggi 550.

c. Membuat label judul
tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 14, "bold")
).pack(pady=15)
untuk menampilkan judul aplikasi. pack() digunakan untuk mengatur posisi komponen, sedangkan pady=15 memberikan jarak atas dan bawah.

d. Menentukan nama mata pelajaran
mapel = [
    "Matematika", "Bahasa Indonesia",
    "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Informatika", "Ekonomi",
    "Sejarah", "Geografi"
]
berisi daftar 10 mata pelajaran yang akan ditampilkan pada aplikasi. Daftar tersebut disimpan dalam variabel mapel agar nama mata pelajaran dapat digunakan untuk membuat label dan kotak input.

e. Membuat input nilai
for nama in mapel:
    tk.Label(root, text=nama).pack()
    tk.Entry(root).pack(pady=3)
untuk menampilkan nama mata pelajaran dan kotak untuk memasukkan nilai. Perintah for digunakan untuk mengulang proses sebanyak jumlah mata pelajaran dalam daftar. Label() menampilkan nama mata pelajaran, sedangkan Entry() membuat kotak input nilai.

f. Membuat fungsi prediksi
def prediksi():
    hasil.config(text="Teknologi Informasi")
membuat fungsi bernama prediksi(). Ketika fungsi dijalankan, tulisan pada label hasil akan diubah menjadi "Teknologi Informasi". Program tidak menghitung nilai yang dimasukkan karena hasilnya sudah ditentukan sesuai instruksi tugas.

g. Membuat tombol hasil prediksi
tk.Button(
    root,
    text="Hasil Prediksi",
    command=prediksi
).pack(pady=15)
untuk membuat tombol bertuliskan "Hasil Prediksi". command=prediksi berarti fungsi prediksi() akan dijalankan ketika tombol diklik. pady=15 memberikan jarak agar posisi tombol

h. Membuat label hasil
hasil = tk.Label(root, text="Hasil Prediksi: -")
hasil.pack()
membuat tempat untuk menampilkan hasil prediksi. Sebelum tombol diklik, tulisan yang muncul adalah "Hasil Prediksi: -". Setelah tombol diklik, tulisan berubah menjadi "Teknologi Informasi".

i. Menjalankan aplikasi
root.mainloop()

untuk menjalankan aplikasi dan menjaga jendela tetap terbuka agar pengguna dapat memasukkan nilai dan menekan tombol.