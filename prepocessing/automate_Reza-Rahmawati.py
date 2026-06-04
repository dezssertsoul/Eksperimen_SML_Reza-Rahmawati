import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def run_preprocessing(input_path, output_path):
    print("[-] Memulai proses otomatisasi preprocessing...")
    
    # 1. Validasi apakah file data mentah benar-benar ada
    if not os.path.exists(input_path):
        print(f"[ERROR] File mentah tidak ditemukan di: {input_path}")
        return
        
    # 2. Memuat dataset menggunakan engine Python (Solusi ParserError)
    print("[-] Membaca file data mentah (raw)...")
    df = pd.read_csv(input_path, engine='python', on_bad_lines='skip')
    
    # 3. Menghapus data duplikat secara logis
    print("[-] Menghapus baris data duplikat...")
    df = df.drop_duplicates()
    
    # 4. Melakukan Standarisasi Fitur Numerik (Length)
    print("[-] Melakukan scaling StandarScaler pada fitur Length...")
    scaler = StandardScaler()
    df['Length'] = scaler.fit_transform(df[['Length']])
    
    # 5. Menyimpan hasil akhir ke folder tujuan
    df.to_csv(output_path, index=False)
    print(f"[SUCCESS] Proses selesai! Data bersih disimpan di: {output_path}")

if __name__ == "__main__":
    # Path disesuaikan dengan struktur folder repositori PIJAK:
    # Keluar dari folder 'preprocessing', lalu masuk ke folder 'Midterm_53_group_raw'
    INPUT_FILE = '../Midterm_53_group_raw/Midterm_53_group.csv'
    OUTPUT_FILE = 'dataset_preprocessing.csv'
    
    run_preprocessing(INPUT_FILE, OUTPUT_FILE)