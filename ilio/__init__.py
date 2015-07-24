def read(path, mode='rb'):
    '''
    read and return content of file. default mode is 'rb'.
    '''
    f = open(path, mode)
    content = f.read()
    f.close()
    return content


def write(path, content, mode='wb'):
    '''
    write content to file. default mode is 'wb'
    '''
    f = open(path, mode)
    f.write(content)
    f.close()


def append(path, content, mode='ab'):
    '''
    append content to file. default mode is 'ab'
    '''
    write(path, content, mode)
