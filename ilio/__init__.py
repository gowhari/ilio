def read(path, mode='r'):
    '''
    read and return content of file. default mode is 'r'.
    '''
    f = open(path, mode)
    content = f.read()
    f.close()
    return content


def write(path, content, mode='w'):
    '''
    write content to file. default mode is 'w'
    '''
    f = open(path, mode)
    f.write(content)
    f.close()


def append(path, content, mode='a'):
    '''
    append content to file. default mode is 'a'
    '''
    write(path, content, mode)


fread = read
fwrite = write
fappend = append
