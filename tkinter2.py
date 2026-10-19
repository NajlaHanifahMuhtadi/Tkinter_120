import tkinter as tk

# Membuat jendela
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550")

# Label judul
tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 14, "bold")
).pack(pady=15)

# Input 10 nilai mata pelajaran
mapel = [
    "Matematika", "Bahasa Indonesia",
    "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Informatika", "Ekonomi",
    "Sejarah", "Geografi"
]

for nama in mapel:
    tk.Label(root, text=nama).pack()
    tk.Entry(root).pack(pady=3)

# Fungsi prediksi
def prediksi():
    hasil.config(text="Teknologi Informasi")

# Tombol prediksi
tk.Button(
    root,
    text="Hasil Prediksi",
    command=prediksi
).pack(pady=15)

# Label hasil
hasil = tk.Label(root, text="Hasil Prediksi: -")
hasil.pack()

# Menjalankan aplikasi
root.mainloop()