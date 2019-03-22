import os


def load_directory(path):
    data_dir = 'data/batch_4/{}/'.format(path)
    file_contents = {}
    for file in os.listdir(data_dir):
        with open(os.path.join(data_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
            file_contents[file] = [line for line in f.readlines() if line.strip()]
    return file_contents


def get_task1():
    return load_directory('relationAnnotation_1'), load_directory('relationAnnotation_2')


if __name__ == '__main__':
    print(get_task1())
