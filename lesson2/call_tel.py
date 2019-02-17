#call_tel.py
def call_tel():
    code=int(input("Введите код города "))
    long=int(input('Введите длительность Вашего разговора '))
    if code==343:
        price=long*15
        return price
    elif code==381:
        price=long*18
        return price
    elif code==473:
        price=long*13
        return price
    elif code==485:
        price=long*11
        return price
print('Цена разговора ',call_tel(), 'рублей')
