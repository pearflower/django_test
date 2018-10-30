def convert_str2_iso(str):
    '''将utf-8编码的字符串转换成iso编码的
    :param str:
    :return:
    '''
    return bytes(str,'utf-8').decode('iso-8859-1')

def convert_str2_utf(str):
    '''将iso编码的字符串转换成utf-8编码的
    :param str:
    :return:
    '''
    return bytes(str,'iso-8859-1').decode('utf-8')