def read_file(file_name: str):
    file = open(file_name, 'r')
    result = file.read()
    file.close()
    return result.strip()


def read_list(file_name: str):
    return read_file(file_name).split('\n')


def read_num_list(file_name: str):
    return list(map(int, read_list(file_name)))
