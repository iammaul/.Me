def border():
    print('-'*25)

def name():
    name = ['Muhammad',2,'Amanda',False,98,'Maulana','Malik','Ibrahim']
    name.remove(2), name.remove(False), name.remove(98)
    print('Halo, ')
    print('Perkenalkan, saya ', name)

def age():
    import datetime as dt
    
    date = 17
    month = 12
    year = 2002
    
    time = dt.date(year, month, date)
    print(f'Saya lahir tanggal {date}')
    print('Bulan ',month)
    print('Tahun ',year)
        
    now = dt.date.today()
    print('Hari ini tanggal ',now)
    days_age = now - time
    year_age = days_age.days // 365
    print('Sekarang saya berumur ',year_age)


print("="*20+' INTRODUCTION '+'='*20)
name()
border()
age()
border()

