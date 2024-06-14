import os
import shutil
import librosa
from tqdm import tqdm

# wav 파일들이 있는 폴더 경로
source_folder = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/wavdata"

# 추출된 wav 파일들을 저장할 폴더 경로
destination_folder = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/mini_wavdata"

# 추출된 파일 수를 저장할 변수
extracted_count = 0

# 소스 폴더 내의 모든 파일을 순회
for filename in tqdm(os.listdir(source_folder)):
    if filename.endswith(".wav"):  # wav 파일인 경우에만 처리
        file_path = os.path.join(source_folder, filename)
        
        # librosa를 사용하여 오디오 파일 로드
        y, sr = librosa.load(file_path, sr=None)
        
        # 오디오 길이 계산 (초 단위)
        duration = librosa.get_duration(y=y, sr=sr)
        
        # 오디오 길이가 2초 이상 10초 미만인 경우
        if 2 <= duration < 10:
            # 대상 폴더로 파일 이동
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            extracted_count += 1
            #print(f"Extracted file: {filename}")

print(f"Number of extracted files: {extracted_count}")