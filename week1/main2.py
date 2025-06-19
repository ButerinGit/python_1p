def psd(messsage,key):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    messsage = messsage.upper()
    cipher = ''

    for i in messsage:
        if i in alpha:
            index = (alpha.find(i) + key) % len(alpha)

            cipher += alpha[index]
        else:
            cipher += i
    print(cipher)

psd('booom boom',6)
psd('HUUUS HUUS',-6)