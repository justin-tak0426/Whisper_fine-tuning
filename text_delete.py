import os
import re
from tqdm import tqdm

folder_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/preprocessed_datasets/txtdata"  # txt 파일들이 있는 폴더 경로로 변경

# 한글 정규식 패턴
korean_pattern = re.compile(r'[가-힣]')

# 삭제할 문서의 수를 저장할 변수
delete_count = 0

# 폴더 내의 모든 파일을 순회
for filename in tqdm(os.listdir(folder_path)):
    if filename.endswith(".txt"):  # txt 파일인 경우에만 처리
        file_path = os.path.join(folder_path, filename)
        
        # 파일 내용 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # 한글이 존재하지 않는 경우
            if not korean_pattern.search(content):
                # 파일 삭제
                os.remove(file_path)
                delete_count += 1
                #print(f"Deleted file: {file_path}")

# 남아있는 파일 개수 계산
remaining_count = len([file for file in os.listdir(folder_path) if file.endswith(".txt")])

print(f"Number of documents deleted: {delete_count}")
print(f"Number of remaining documents: {remaining_count}")