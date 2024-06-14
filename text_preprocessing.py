import os
import re
from tqdm import tqdm

folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/txtdata"  

# 숫자와 단위가 포함된 괄호와 내용 제거를 위한 정규표현식 패턴
number_unit_pattern = re.compile(r'\(\d+(?:\.\d+)?[a-zA-Z가-힣]*\)')

# 마침표와 물음표를 제외한 특수문자 제거를 위한 정규표현식 패턴
special_char_pattern = re.compile(r'[^a-zA-Z0-9가-힣\s.?]')

# /b, b/와 같은 문자열을 제거하고 공백을 유지하는 정규표현식 패턴
remove_pattern = re.compile(r'(?<!\S)/?[a-zA-Z]/?(?!\S)')

for root, dirs, files in os.walk(folder_path):
    for file in tqdm(files, desc="Processing files"):
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                
                # 숫자와 단위가 포함된 괄호와 내용 제거
                text = number_unit_pattern.sub('', text)
                
                # /b, b/와 같은 문자열을 제거하고 공백 유지
                text = remove_pattern.sub(' ', text)
                
                # 마침표와 물음표를 제외한 특수문자 제거
                text = special_char_pattern.sub('', text)
                
                # 연속된 공백을 하나의 공백으로 줄이기
                text = re.sub(r'\s+', ' ', text)
                
                # 문장 시작과 끝의 공백 제거
                text = text.strip()
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)

print("Text data preprocessing Finish!")

