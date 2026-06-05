import os
import sys
import pandas as pd

def run_preprocessing():
    input_path = 'Midterm_53_group.csv'
    output_dir = 'preprocessing'
    output_path = os.path.join(output_dir, 'Midterm_53_group_preprocessed.csv')
    
    print(f"[INFO] Membaca data mentah dari: {input_path}")
    if not os.path.exists(input_path):
        print(f"[ERROR] File {input_path} tidak ditemukan! Pastikan posisi file benar.")
        sys.exit(1)
        
    df = pd.read_csv(input_path)
    
    print(f"[INFO] Jumlah baris sebelum preprocessing: {df.shape[0]}")
    df_clean = df.drop_duplicates()
    print(f"[INFO] Jumlah baris setelah drop duplikat: {df_clean.shape[0]}")
    
    os.makedirs(output_dir, exist_ok=True)
    
    df_clean.to_csv(output_path, index=False)
    print(f"[SUKSES] Dataset hasil preprocessing berhasil disimpan di: {output_path}")

if __name__ == "__main__":
    run_preprocessing()
