#cinema_price.py
def cinema_price():
    film=input('Выберете фильм\n')
    day=input('Выберете дату\n')
    time=int(input('Выберете время\n'))
    num=int(input('Выберете количество билетов\n'))
    if film=='Пятница' and time==12:
        price=250
    elif film=='Пятница'and time==16:
        price=350
    elif film=='Пятница'and time==20:
        price=450
    elif film=='Чемпионы'and time==10:
        price=250
    elif film=='Чемпионы'and time==13:
        price=350
    elif film=='Чемпионы'and time==16:
        price=350
    elif film=='Пернатая банда'and time==10:
        price=350
    elif film=='Пернатая банда'and time==14:
        price=450
    elif film=='Пернатая банда'and time==18:
        price=450
    else:
        return'Данного сеанса на выбранную дату нет'
    total_sum=price*num
    if day=='Сегодня' and num>=20:
        total_sum=total_sum*0.8
        return total_sum
    elif day=='Сегодня' and num<20:
        return total_sum
    elif day=='Завтра'and num>=20:
        total_sum=total_sum*0.8*0.95
        return total_sum
    elif day=='Завтра'and num<20:
        total_sum=total_sum*0.95
        return total_sum
print(cinema_price())
