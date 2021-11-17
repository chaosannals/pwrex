from random import randint

PINYIN_INITIAL_RHYME = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'x', 'j' 'q', 'y', 'w', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's']
PINYIN_FOOT_RHYME = ['i', 'u', 'a', 'ia', 'ua', 'o', 'uo', 'e', 'ie', 'ue', 'ai', 'uai', 'ei', 'uei', 'ao', 'iao', 'ou', 'iou', 'an', 'ian', 'uan', 'en', 'in', 'uen', 'un', 'ang', 'iang', 'uang', 'eng', 'ing', 'ueng', 'ong', 'iong']
PINYIN_WHOLE = ['zhi', 'chi', 'shi', 'ri', 'zi', 'ci' 'si', 'yi', 'wu', 'yu', 'ye', 'yue', 'yuan', 'yin', 'yun']

NAME_FISRT = []
NAME_LAST = []


def lie_pinyin():
    '''
    '''

    c = randint(1, 2)
    if c == 1:
        w_max = len(PINYIN_WHOLE) - 1
        return PINYIN_WHOLE[randint(0, w_max)]
    else:
        ir_max = len(PINYIN_INITIAL_RHYME) - 1
        fr_max = len(PINYIN_FOOT_RHYME) - 1
        ir = PINYIN_INITIAL_RHYME[randint(0, ir_max)]
        fr = PINYIN_FOOT_RHYME[randint(0, fr_max)]
        return f'{ir}{fr}'

def lie_pinyin_string(length=3, sp=None):
    '''
    '''

    r = []
    i_max = length - 1
    for i in range(length):
        p = lie_pinyin()
        r.append(p)
        if sp is not None and i < i_max:
            r.append(sp)
    return ''.join(r)