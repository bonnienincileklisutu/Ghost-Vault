import os
import time
import random

def ghost_encrypt_line(text, key):
    sahte_veri_havuzu = [
        "KDA: 24/12/8 - Neon",
        "ACS: 285 - Omen",
        "Ping: 14ms - TR East",
        "Win Rate: %68.4",
        "HS Rate: %32.1",
        "Clutch: 1v3 Won",
        "Rank: Ascendant 1",
        "Agent: Cypher Locked"
    ]
    
    kasa_satirlari = []
    for char in text:
        sifreli_ascii = ord(char) + key
        sahte_satir = random.choice(sahte_veri_havuzu)
        kasa_satirlari.append(f"{sahte_satir} // id:{sifreli_ascii}\n")
    return kasa_satirlari

def ghost_decrypt_file(dosya_adi, key):
    orijinal_mesaj = ""
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            satirlar = f.readlines()
            
        for satir in satirlar:
            if "// id:" in satir:
                gizli_id = satir.split("// id:")[1].strip()
                orijinal_mesaj += chr(int(gizli_id) - key)
        return orijinal_mesaj
    except FileNotFoundError:
        return "[!] HATA: Veri kasası dosyası (kasa.txt) bulunamadı!"
    except Exception:
        return "[!] HATA: Şifre çözülürken bir hata oluştu veya anahtar yanlış!"

def konsol_paneli():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*55)
        print("         r4bbit GHOST-VAULT TOOL v2.1          ")
        print("="*55)
        print("[1] Yeni Gizli Veri Kasası Oluştur (.txt kaydet)")
        print("[2] Mevcut Kasadaki Şifreyi Çöz (kasa.txt oku)")
        print("[3] Sistemi Kapat")
        print("="*55)
        
        secim = input("[+] Operasyon numarasını girin: ")
        
        if secim == "1":
            print("\n--- KASA OLUŞTURMA MODU ---")
            mesaj = input("[>] Gizlenecek mesajı/taktiği girin: ")
            
            while True:
                try:
                    anahtar = int(input("[>] Gizli anahtar sayısını girin (Örn: 5): "))
                    break
                except ValueError:
                    print("[!] Lütfen sadece bir sayı girin!")
            
            kasa_verisi = ghost_encrypt_line(mesaj, anahtar)
            
            # Dosyaya Yazma İşlemi
            with open("kasa.txt", "w", encoding="utf-8") as f:
                f.writelines(kasa_verisi)
            
            # Dosyanın gittiği tam adresi bulan siber güvenlik komutu:
            tam_adres = os.path.abspath("kasa.txt")
                
            print("\n" + "-"*55)
            print("[✔] GHOST-VAULT OPERASYONU BAŞARILI!")
            print(f"[i] Dosyanın kaydedildiği tam yer:\n👉 {tam_adres}")
            print("-"*55)
            input("\nMenüye dönmek için ENTER'a bas...")
            
        elif secim == "2":
            print("\n--- ŞİFRE ÇÖZME MODU ---")
            while True:
                try:
                    anahtar = int(input("[>] Kasanın gizli anahtarını girin: "))
                    break
                except ValueError:
                    print("[!] Lütfen sadece bir sayı girin!")
            
            print("\n[!] 'kasa.txt' dosyası taranıyor...")
            time.sleep(0.5)
            
            cozulen_mesaj = ghost_decrypt_file("kasa.txt", anahtar)
            print("-"*55)
            print(f"[✔] Kasadan Çıkarılan Gerçek Mesaj:\n\n{cozulen_mesaj}")
            print("-"*55)
            input("\nMenüye dönmek için ENTER'a bas...")
            
        elif secim == "3":
            print("\n[-] Ghost-Vault kapatılıyor... Güvenli sürüşler r4bbit.")
            time.sleep(1)
            break
        else:
            print("[!] Geçersiz komut! İşlemci reddetti.")
            time.sleep(1)

if __name__ == "__main__":
    konsol_paneli()