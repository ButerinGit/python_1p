alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
messsage = 'Brutte is killer!!!'
key = 3
messsage = messsage.upper()
cipher = ''

for i in messsage:
    if i in alpha:
        index = (alpha.find(i) + key) % len(alpha)

        cipher += alpha[index]
    else:
        cipher += i


print(cipher)