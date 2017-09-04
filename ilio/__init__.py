def read(path, *args, **kwargs):
    '''
    read and return content of file.
    '''
    with open(path, *args, **kwargs) as f:
        return f.read()


def write(path, content, *args, **kwargs):
    '''
    write content to file.
    '''
    if len(args) == 0 and 'mode' not in kwargs:
        args = ('w',)
    with open(path, *args, **kwargs) as f:
        f.write(content)


def append(path, content, *args, **kwargs):
    '''
    append content to file.
    '''
    if len(args) == 0 and 'mode' not in kwargs:
        args = ('a',)
    write(path, content, *args, **kwargs)


fread = read
fwrite = write
fappend = append
