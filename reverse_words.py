

def rev_words1(string, symbols):
    """Solution 1"""
    words = string.split()
    arr = []
    for word in words:
        chars = [sym for sym in symbols if sym in word]
        inds = [word.index(sym) for sym in chars]
        if not chars:
            word = word[::-1]
        else:
            for j in range(len(chars)):
                    word = word.replace(chars[j], '')[::-1][:inds[j]] + chars[j] \
                        + word.replace(chars[j], '')[::-1][inds[j]:]
                    if len(chars) > 1 and j == 0:
                        word = word[::-1]
        arr.append(word)

    # print(arr)
    return ' '.join(arr)

def rev_words2(string, symbols):
    """Solution 2"""
    words = string.split()
    arr = []
    for word in words:
        symbol_index = [(sym, word.index(sym)) for sym in symbols if sym in word]
        if not symbol_index:
            word = word[::-1]
        else:
            chars = [ch for ch in word if ch not in symbols]
            chars = chars[::-1]
            for symbol, index in symbol_index:
                chars.insert(index, symbol)
            word = ''.join(chars)
        arr.append(word)

    # print(arr)
    return ' '.join(arr)

def rev_words3(string, symbols):
    """Solution 3"""
    def reverse_word(word, symbol_index):
        n = len(word)
        rev_word = ''
        if symbol_index:
            m = len(symbol_index)
            j= 0
            for i in range(n):
                sy, idx = symbol_index[j] if j < m else ('', -1)
                # print(m, j, i, idx, sy)
                if i == idx:
                    rev_word += sy
                    j += 1
                rev_word += word[n-1-i]
        else:
            for i in range(n):
                rev_word += word[n-1-i]
        return rev_word

    rev = ''
    j = 0
    word = ''
    symbol_index = []
    for i in range(len(string)):
        if string[i] == ' ':
            if i != 0:
                # print(word, symbol_index)
                rev += reverse_word(word, symbol_index)
            rev += string[i]
            j = 0
            word = ''
            symbol_index = []
        else:
            if string[i] not in symbols:
                word += string[i]
            else:
                symbol_index.append((string[i], j))
            j += 1

    rev += reverse_word(word, symbol_index)
        

    # print(rev)
    return rev



if __name__ == '__main__':
    string = "th@s is @nterv!ew" * 1000000
    symbols = ['@', '!']
    reversed_string = rev_words1(string, symbols)
    # print(reversed_string)