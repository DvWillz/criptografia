dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z', ' ', 'ç', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

dic2 = ['5h1!', '17n1', '23a@', '24j2', '3#4d', '4h33', '47k$', '5f44', '5y4%', '54g5', '6u#', '6643', '7f$',
        '77&h', '82*', '887$', '9d#',
        '9h9@', '10&f', '1010d', '10gv1$', '11cn11', '12%g', '49jk3', 'ijn35', 'j395', '*4g', '~~53^', 'h', 'jg',
        '25F', '@!ax', '$fv', '@f', '%h', '@@f', '$#f', '$jf']


def cripto(text):
    text = text[::-1]
    criptografado = ''
    ct = 0
    cd = 0
    for i in text:
        for v in dic:
            if i == v:
                criptografado += dic2[cd] + ' '
            cd += 1
        cd = 0
        ct += 1
    criptografado = criptografado[::-1]
    return criptografado


def descripto(text):
    text = text[::-1]
    text = text.split()
    desc = ''
    t = 0
    d = 0
    for i in text:
        for v in dic2:
            if i == v:
                desc += dic[d]
            d += 1
        d = 0
        t += 1
    desc = desc[::-1]
    return desc
