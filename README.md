# 🐇 r4bbit Ghost-Vault v2.5 (Steganography & Encryption Tool)

An elite CLI-based cybersecurity tool that combines **ASCII Caesar Cipher Encryption** with **Text-Based Steganography**. It hides your secret messages, credentials, or e-sports strategies inside fake Valorant match logs and saves them directly to a text file.

## 💡 How It Works
1. **Encryption:** Converts your text into ASCII values and shifts them with your custom secret key.
2. **Steganography:** Embeds the encrypted values behind randomized, innocent-looking Valorant esports statistics (KDA, ACS, Rank etc.) using an ID format.
3. **Decryption:** Parses the `.txt` file, extracts the secret IDs, reverses the shift using your key, and reveals the original hidden text.

## 🛠️ Features
- **Interactive CLI Console:** No need to change code; manage everything through the terminal.
- **Auto-File Generation:** Saves directly to `kasa.txt` and prints the absolute path.
- **Anti-Sniffer / Stealth Mode:** To any outsider or network sniffer, the output file looks like a harmless game log.

## 💻 Installation & Usage
```bash
# Clone the repository
git clone [https://github.com/bonnienincileklisütü/Ghost-Vault.git](https://github.com/bonnienincileklisütü/Ghost-Vault.git)

# Run the tool
python vault.py
