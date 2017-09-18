def read(path, mode='r'):
    '''
    read and return content of file. default mode is 'r'.
    '''
    with open(path, mode) as f:
        return f.read()


def write(path, content, mode='w'):
    '''
    write content to file. default mode is 'w'
    '''
    with open(path, mode) as f:
        f.write(content)


def append(path, content, mode='a'):
    '''
    append content to file. default mode is 'a'
    '''
    write(path, content, mode)


fread = read
fwrite = write
fappend = append
