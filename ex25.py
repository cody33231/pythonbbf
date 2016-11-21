# --coding=utf-8--

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') #split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串,参数中的' '说明这个值是个字符串str类型，''需加空格
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)#sorted()排序函数

def print_first_word(words):
    """Prints the first word after poping it off."""
    word = words.pop(0) #pop()去除列表中的元素 0 代表第一个
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)#pop()去除列表中的元素 -1 代表最后一个
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
