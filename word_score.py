import tkinter as tk
from tkinter import messagebox
import random

def kelimeleri_yukle(dosya_yolu):
    kelimeler = []
    with open(dosya_yolu, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Satırdaki boşlukları temizle
            if line:  # Boş satırları atla
                parts = line.split(';')  # Ayracı ';' olarak değiştirin
                if len(parts) == 2:  # İki parçaya ayrılıp ayrılmadığını kontrol et
                    kelime, anlam = parts
                    kelimeler.append((kelime.strip(), anlam.strip()))  # Boşlukları temizle
                else:
                    print(f"Uygun formatta olmayan satır atlandı: {line}")
    return kelimeler

def sorulari_olustur(kelimeler):
    sorular = []
    # Toplam 30 soru oluşturma
    for kelime, anlam in random.sample(kelimeler, min(30, len(kelimeler))):  # 30'dan fazla kelime varsa, 30 rastgele seç
        yanlislar = random.sample([k[1] for k in kelimeler if k[1] != anlam], 4)
        secenekler = random.sample([anlam] + yanlislar, 5)
        sorular.append((kelime, anlam, secenekler))
    return sorular

class SinavApp:
    def __init__(self, master, kelimeler):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("Kelime Sınavı - Türkçe")
        self.master.configure(bg="#8F9B77")  # Haki yeşil arka plan rengi

        self.kelimeler = kelimeler
        self.sorular = sorulari_olustur(kelimeler)
        self.soru_index = 0
        self.dogru_sayisi = 0
        self.cevaplar = []

        self.soru_label = tk.Label(master, text="", wraplength=400, bg="#8F9B77", font=("Arial", 20))
        self.soru_label.pack(pady=20)

        self.var = tk.StringVar()  
        self.secenek_buttons = []

        # Seçenek butonlarının konumunu ortalayacak şekilde düzenleme
        button_frame = tk.Frame(master, bg="#8F9B77")
        button_frame.pack(pady=10)

        for i in range(5):
            button = tk.Radiobutton(button_frame, text="", variable=self.var, value="", font=("Arial", 12), bg="#8F9B77",
                                    command=self.secenek_secildi)  # Seçenek seçildiğinde kontrol için
            button.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            self.secenek_buttons.append(button)

        self.ilerle_button = tk.Button(master, text="İlerle", command=self.ilerle, font=("Arial", 20), width=10, height=2,
                                       highlightbackground="lightgreen", activebackground="green", 
                                       fg="#8F9B77", bg="brown", state=tk.DISABLED)  # Başlangıçta devre dışı
        self.ilerle_button.pack(pady=10)

        self.soru_goster()

    def soru_goster(self):
        if self.soru_index < len(self.sorular):
            kelime, anlam, secenekler = self.sorular[self.soru_index]
            self.soru_label.config(text=f"{self.soru_index + 1}. {kelime} anlamı nedir?")
            self.var.set(None)  # Seçenekleri sıfırlama
            for i, button in enumerate(self.secenek_buttons):
                button.config(text=secenekler[i], value=secenekler[i])
            self.ilerle_button.config(state=tk.DISABLED) 

        else:
            self.sonuc_goster()

    def secenek_secildi(self):
    
        if self.var.get():
            self.ilerle_button.config(state=tk.NORMAL)
        else:
            self.ilerle_button.config(state=tk.DISABLED)

    def ilerle(self):
        if not self.var.get(): 
            messagebox.showwarning("Uyarı", "Lütfen bir seçenek işaretleyin.")
            return

        secilen = self.var.get()
        dogru = self.sorular[self.soru_index][1]
        self.cevaplar.append((self.soru_index + 1, secilen, dogru))
        if secilen == dogru:
            self.dogru_sayisi += 1
        self.soru_index += 1
        self.soru_goster()

    def sonuc_goster(self):
        toplam_soru = len(self.sorular)
        yanlis_sayisi = toplam_soru - self.dogru_sayisi

        if toplam_soru == 0:
            messagebox.showinfo("Sonuç", "Hiç soru sorulmadı.")
            return

        basari_yuzdesi = (self.dogru_sayisi / toplam_soru) * 100

        sonuc_mesaji = f"Doğru Sayısı: {self.dogru_sayisi}\nYanlış Sayısı: {yanlis_sayisi}\nBaşarı Yüzdesi: {basari_yuzdesi:.2f}%"
        messagebox.showinfo("Sonuç", sonuc_mesaji)

        for index, (soru_index, verilen_cevap, dogru_cevap) in enumerate(self.cevaplar):
            if verilen_cevap != dogru_cevap:
                mesaj = f"{soru_index}. Soru: {self.sorular[soru_index - 1][0]}\nYanlış Cevap: {verilen_cevap}\nDoğru Cevap: {dogru_cevap}"
                messagebox.showinfo("Yanlış Cevap", mesaj)

def main():
    kelimeler = kelimeleri_yukle("C:/Users/ABDURRAHMAN/MATLAB/Desktop/PYTHON ÇALIŞMALAR/sözlük.txt")
    root = tk.Tk()
    app = SinavApp(root, kelimeler)
    root.mainloop()

if __name__ == "__main__":
    main()
