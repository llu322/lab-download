def load_chinese_file(filename): # open in binary mode ('b'): reading raw bytes, no encoding yet
    f = open(filename, 'br')
    bs = f.read()
    try:
        text = bs.decode('gb2312')
        print('gb2312')
    except UnicodeDecodeError:
        text = bs.decode('big5')
        print('big5')
    return text