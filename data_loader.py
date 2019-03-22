import os


def load_directory(batch, path):
    data_dir = 'data/{}/{}/'.format(batch, path)
    file_contents = {}
    for file in os.listdir(data_dir):
        with open(os.path.join(data_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
            file_contents[file] = [line for line in f.readlines() if line.strip()]
    return file_contents


def get_task1():
    batch = 'batch_4'
    return load_directory(batch, 'relationAnnotation_1'), load_directory(batch,
                                                                         'relationAnnotation_2')


def get_task2():
    batch = 'batch_5'
    return load_directory(batch, 'relationAnnotations_1'), load_directory(batch,
                                                                          'relationAnnotations_2')


if __name__ == '__main__':
    print(get_task1())
