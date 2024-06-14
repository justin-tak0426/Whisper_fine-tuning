import os
import numpy as np
import librosa as lr
import soundfile as sf
from tqdm import tqdm


folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/Original dataset/KsponSpeech_01"

source_folders = []
count = 0
for item in os.listdir(folder_path):
    if os.path.isdir(os.path.join(folder_path, item)):
        subfolder_path = os.path.join(folder_path, item)
        source_folders.append(subfolder_path)
        print(subfolder_path)
        count = count+1
print("total number of folder which include data: ", count)
        
        

# txtdata 경로 설정
txtdata_folder = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/txtdata"

# txtdata 폴더에 있는 파일들의 이름 추출 (확장자 제외)
txt_file_names = [os.path.splitext(file)[0] for file in os.listdir(txtdata_folder) if file.endswith(".txt")]

destination_folder = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/wavdata"
for source_folder in tqdm(source_folders):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".pcm"):
                source_path = os.path.join(root, file)
                
                # 파일 이름 추출 (확장자 제외)
                file_name = os.path.splitext(file)[0]
                
                # txtdata 폴더에 파일 이름이 존재하는 경우에만 처리
                if file_name in txt_file_names:
                    destination_path = os.path.join(destination_folder, file_name + ".wav")

                    buf = None
                    with open(source_path, 'rb') as tf:
                        buf = tf.read()
                        buf = buf + b'0' if len(buf) % 2 else buf

                    pcm_data = np.frombuffer(buf, dtype='int16')
                    wav_data = lr.util.buf_to_float(x=pcm_data, n_bytes=2)
                    sf.write(destination_path, wav_data, 16000, format='WAV', endian='LITTLE', subtype='PCM_16')

print("Finish!")