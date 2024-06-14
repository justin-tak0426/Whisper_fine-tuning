import os
import chardet
from collections import defaultdict
from tqdm import tqdm

# before encoding change (original data)
#folder_path = '/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/Original dataset/KsponSpeech_01'

# after encoding change
folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/KsponSpeech_01"  

source_folders = []
count = 0
for item in os.listdir(folder_path):
    if os.path.isdir(os.path.join(folder_path, item)):
        subfolder_path = os.path.join(folder_path, item)
        source_folders.append(subfolder_path)
        #print(subfolder_path)
        count = count+1
print("total number of folder which include data: ", count)
    
encoding_counts = defaultdict(int)
encoding_counts['None'] = 0
file_num = 0
for folder in tqdm(source_folders):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                file_num += 1
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    result = chardet.detect(f.read())
                    encoding = result['encoding']
                    if encoding is None:
                        #print(f"No encoding detected for file: {file}")
                        encoding_counts['None'] += 1
                    else:
                        encoding_counts[encoding] += 1

print("Encoding counts:")
for encoding, count in encoding_counts.items():
    print(f"{encoding}: {count}")
print("file number: ", file_num)