import os
import librosa
from tqdm import tqdm

def get_total_audio_duration(folder_path):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith((".wav", ".mp3", ".flac"))]
    total_duration = 0

    for audio_file in audio_files:
        file_path = os.path.join(folder_path, audio_file)
        y, sr = librosa.load(file_path)
        duration = librosa.get_duration(y=y, sr=sr)
        total_duration += duration

    return total_duration

# 사용 예시
folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/mini_wavdata"
total_duration = get_total_audio_duration(folder_path)
print(f"폴더 내 음성 파일들의 총 길이: {total_duration:.2f}초")