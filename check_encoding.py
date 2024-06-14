import chardet

file_path = "/Users/justin/Desktop/HGU/2024_1/DeepLearning/project/datasets/"

with open(file_path, 'rb') as f:
    content = f.read()
    result = chardet.detect(content)
    print(f"Encoding: {result['encoding']}, Confidence: {result['confidence']}")