#get_parity.py
def check_parity():
    x=int(input('Введите число '))
    if x%2==0:
        return 'Число четное'
    else:
        return 'Число нечетное'
print (check_parity())
