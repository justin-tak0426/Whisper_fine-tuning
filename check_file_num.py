import os

# txt 파일 개수를 확인할 폴더 경로
folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/mini_txtdata"

# 폴더 내의 파일 개수 확인
file_count = len([file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))])

print(f"Number of files in the txt folder: {file_count}")

# wav 파일 개수를 확인할 폴더 경로
folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/mini_wavdata"

# 폴더 내의 파일 개수 확인
file_count = len([file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))])

print(f"Number of files in the wav folder: {file_count}")