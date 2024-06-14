import os
import shutil
from tqdm import tqdm

# A 경로: wav 파일들이 있는 폴더 경로
wav_folder = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/mini_wavdata"

# B 경로: txt 파일들이 있는 폴더 경로
txt_folder = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/txtdata"

# C 경로: 매치되는 txt 파일들을 이동시킬 폴더 경로
destination_folder = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/mini_txtdata"

# A 경로에서 wav 파일들의 파일 이름 추출
wav_files = [os.path.splitext(file)[0] for file in os.listdir(wav_folder) if file.endswith(".wav")]

# B 경로에서 txt 파일들을 순회하며 매치되는 파일 이동
for txt_file in tqdm(os.listdir(txt_folder)):
    if txt_file.endswith(".txt"):
        txt_name = os.path.splitext(txt_file)[0]
        if txt_name in wav_files:
            # 매치되는 txt 파일의 전체 경로
            txt_path = os.path.join(txt_folder, txt_file)
            
            # 대상 폴더로 txt 파일 이동
            destination_path = os.path.join(destination_folder, txt_file)
            shutil.move(txt_path, destination_path)
            #print(f"Moved file: {txt_file}")

print("File movement completed.")