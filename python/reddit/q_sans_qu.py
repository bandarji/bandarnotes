def qwords_withoutqu():
    i = 0
    all_words = '/usr/share/dict/words'
    with open(all_words) as words, open('/tmp/qnoqu.txt', 'w') as f_out:
        for word in words:
            if 'q' in word and 'qu' not in word:
                i += 1
                print('{:<4} {}'.format(i, word.strip()))
                f_out.write(word)

qwords_withoutqu()

# $ python q__sans_qu.py 
# 1    Iraq
# 2    Iraqi
# 3    Iraqian
# 4    Louiqa
# 5    miqra
# 6    nastaliq
# 7    Pontacq
# 8    q
# 9    qasida
# 10   qere
# 11   qeri
# 12   qintar
# 13   qoph
# 14   Saqib
# 15   shoq
# 16   Tareq

# $ cat /tmp/qnoqu.txt 
# Iraq
# Iraqi
# Iraqian
# Louiqa
# miqra
# nastaliq
# Pontacq
# q
# qasida
# qere
# qeri
# qintar
# qoph
# Saqib
# shoq
# Tareq
