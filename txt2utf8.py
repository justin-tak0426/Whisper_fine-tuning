import os
import chardet
from tqdm import tqdm
import shutil

folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/Original dataset/KsponSpeech_01"
destination_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/txtdata"

source_folders = []
count = 0
for item in os.listdir(folder_path):
    if os.path.isdir(os.path.join(folder_path, item)):
        subfolder_path = os.path.join(folder_path, item)
        source_folders.append(subfolder_path)
        count = count + 1
print("total number of folder which include data: ", count)


def convert_to_utf8(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            result = chardet.detect(content)
            encoding = result['encoding']
            confidence = result['confidence']
            if encoding is None or confidence < 0.8:
                # 인코딩 감지에 실패하거나 신뢰도가 낮은 경우 skip
                return 1
            else:
                decoded_content = content.decode(encoding, errors='replace')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(decoded_content)
            return 0
    except Exception as e:
        return 1

success_count = 0
failed_files = []
for folder in tqdm(source_folders):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                if convert_to_utf8(file_path) == 0:
                    # UTF-8 변환에 성공한 경우 파일 복사
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(file_path, destination_path)
                    success_count += 1
                else:
                    failed_files.append(file_path)

print("Conversion and copying completed.")
print("Files failed to convert:")
for file in failed_files:
    print(file)

print("Fail to convert UTF-8: ", len(failed_files))
print("Success to convert and save txtdata: ", success_count)