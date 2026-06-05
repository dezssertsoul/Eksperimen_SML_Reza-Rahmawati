import os
import sys
import pandas as pd

def run_preprocessing():
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    input_path = os.path.abspath(os.path.join(current_dir, '../Midterm_53_group_raw/Midterm_53_group.csv'))
    
    output_path = os.path.join(current_dir, 'Midterm_53_group_preprocessed.csv')
    
    print(f"[INFO] Membaca data mentah dari: {input_path}")
    if not os.path.exists(input_path):
        print(f"[ERROR] File tidak ditemukan di: {input_path}")
        print("[TIPS] Pastikan folder 'Midterm_53_group_raw' dan file 'Midterm_53_group.csv' sudah di-upload ke GitHub.")
        sys.exit(1)
        
    df = pd.read_csv(input_path)
    
    print(f"[INFO] Jumlah baris awal: {df.shape[0]}")
    # Proses Preprocessing: Menghapus duplikat
    df_clean = df.drop_duplicates()
    print(f"[INFO] Jumlah baris setelah preprocessing: {df_clean.shape[0]}")
    
    # Memastikan folder output (preprocessing) tersedia
    os.makedirs(current_dir, exist_ok=True)
    
    # Simpan hasil preprocessing terbaru
    df_clean.to_csv(output_path, index=False)
    print(f"[SUKSES] Dataset hasil preprocessing berhasil disimpan di: {output_path}")

if __name__ == "__main__":
    run_preprocessing()
