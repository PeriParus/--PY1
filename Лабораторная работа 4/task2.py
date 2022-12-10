def get_count_char(str_): #1,2
     chars ={}
     str_ = str_.lower()  # 3
     for letter in str_:
        if letter.isalpha(): #4
            if letter in chars:
                chars[letter]+=1
            else:
                chars.get(letter)
                chars[letter]=1
     chars = dict(sorted(chars.items(), key=lambda x: x[0]))
     return chars
def percents(chars): #5
    chars_persent={}
    count=sum(chars.values())
    for key in chars.keys():
        for value in chars.values():
            value=round(chars[key]/count*100,2)
            chars_persent[key]=value
    chars_persent = dict(sorted(chars_persent.items(), key=lambda x: x[0])) #sort
    return chars_persent
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percents(get_count_char(main_str)))

