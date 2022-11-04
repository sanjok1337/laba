def Convert(string):
    li = list(string.split(" "))
    return li

while True:
    print("Choose a , b , c")
    choose = input()
    if choose == "a":
        text2 =input("Введіть текст")
        lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')'  ]   
        lst = []

        for word in text2.lower().split():
            if not word in lst_no:
                _word = word 
                if word[-1] in lst_no:
                    _word = _word[:-1]
                if word[0] in lst_no:
                    _word = _word[1:] 
                lst.append(_word)

        _dict = dict()
        for word in lst:
            _dict[word] = _dict.get(word, 0) + 1

        _list = []
        for key, value in _dict.items():
            _list.append((value, key))
            _list.sort(reverse=True)

        for freq, word in _list[0:5]:
            print(f'{word:>10} -> {freq:>3}')



    elif choose == "b":
        text = str(input("Введіть текст: "))
        print(text)
        w = text.split()
        e = ""
        for r in sorted(w):
            e = e + " " + r
        print(e)

    elif choose == "c":
        text1 = input("Введіть текст: ")
        d = text1.lower
        l = text1.split()
        q = ""
        for i in sorted(l, key=lambda b: len(b), reverse=True):
            q = q + " " + i
        k = (Convert(q))
        print(k[0:6])
    else:
        print("Wrong operation")    