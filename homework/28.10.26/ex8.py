# Умнее среднего

ppl_amount = int(input('Введите количество людей: '))

prev_iq = 100

for i in range(ppl_amount):
    iq = int(input('Введите IQ человека: '))

    if iq == prev_iq:
        print('0')
        continue
    
    if iq > prev_iq:
        print('>')
    elif iq < prev_iq:
        print('<')

    prev_iq = iq
    