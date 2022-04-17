from Stock import *
from datetime import datetime
from Weather import *
from StockList import *
import random


Irvine = 'https://weather.com/weather/today/l/76e096b00c40084d41bbd11c609e31cd582552f0f25bfb9f04b62f141e1d0cb8'
Schaumburg = 'https://weather.com/weather/today/l/1fa97708b5b5078e93d357ba11b75be5164b4379b72e5a98d52724f60711cfca'


today = datetime.today()
now = datetime.now()


def main():
    stock_list = []

    result = requests.get('https://finance.yahoo.com/lookup/')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    soup = soup.find("tbody")

    for a in soup.find_all('a', href=True):
        stock_list.append(a.text)

    irvineTemp = getWeather(Irvine)
    schaumburgTemp = getWeather(Schaumburg)


    f = open("StockAnalyzer.txt", "a")

    f.write(today.strftime("%b-%d-%Y"))
    f.write('\n')
    f.write(now.strftime("%H:%M:%S"))
    f.write('\n')

    Target = Stock(stock_list[random.randint(0,len(stock_list)-1)])
    stock_index = random.randint(0,len(stock_list)-1)
    while not Target.valid_stock:
        Target = Stock(stock_list[stock_index])
    f.write(Target.getTitle())
    f.write('\n')
    f.write(Target.getStats())
    f.write('\n')
    f.write(Target.sharePrice())
    f.write('\n')
    f.write('\n')
    stock_list.pop(random.randint(0,len(stock_list)-1))

    Target2 = Stock(stock_list[random.randint(0,len(stock_list)-1)])
    stock_index = random.randint(0,len(stock_list)-1)
    while not Target2.valid_stock:
        Target2 = Stock(stock_list[stock_index])
    f.write(Target2.getTitle())
    f.write('\n')
    f.write(Target2.getStats())
    f.write('\n')
    f.write(Target2.sharePrice())
    f.write('\n')
    f.write('\n')
    stock_list.pop(random.randint(0,len(stock_list)-1))
    
    f.write(f'Weather in Irvine: {getWeather(Irvine)}°F\n')
    f.write(f'Weather in Schaumburg: {getWeather(Schaumburg)}°F\n')

    town = ''
    if betterWeather(Irvine, Schaumburg) == Irvine:
        town = 'Irvine'
        f.write(f'Better weather in: Irvine, buying {Target.getTitle()}\n')
    elif betterWeather(Irvine, Schaumburg) == Schaumburg:
        town = 'Schaumburg'
        f.write(f'Better weather in: Schaumburg, buying {Target2.getTitle()}\n')
    else:
        randWeather = random.randint(0,1)
        if randWeather == 0:
            town = 'Irvine'
            f.write(f'Better weather in: Irvinek, buying {Target.getTitle()}\n')
        else: 
            town = 'Schaumburg'
            f.write(f'Better weather in: Schaumburg, buying {Target2.getTitle()}\n')
        
    f.write('\n')
    f.write('\n')

    

    f.close()
if __name__ == '__main__':
    main()
