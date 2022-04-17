import requests 
from bs4 import BeautifulSoup

#create Stock class
class Stock():
    def __init__(self, symbol):
        self.symbol = symbol
        self.valid_stock = True
        self.link = self.getLink()

    def getLink(self):
        self.link = 'https://finance.yahoo.com/quote/%5E' + self.symbol + '?p=%5E' + self.symbol
        #'https://finance.yahoo.com/quote/TGT?p=TGT&.tsrc=fin-srch'
        #'https://finance.yahoo.com/quote/YM%3DF?p=YM%3DF'
        #'https://finance.yahoo.com/quote/T?p=T&.tsrc=fin-srch'
        #'https://finance.yahoo.com/quote/NQ%3DF?p=NQ%3DF'
        #'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'
        #https://finance.yahoo.com/quote/ES%3DF?p=ES%3DF
        self.result = requests.get(self.link)
        self.src = self.result.content
        self.yahooFinanceData = BeautifulSoup(self.src, 'lxml')
        self.rawData = self.yahooFinanceData.find(class_='My(6px) Pos(r) smartphone_Mt(6px) W(100%)')
        if self.rawData == None:
            self.link = 'https://finance.yahoo.com/quote/' + self.symbol + '?p=' + self.symbol + '&.tsrc=fin-srch'
            self.result = requests.get(self.link)
            self.src = self.result.content
            self.yahooFinanceData = BeautifulSoup(self.src, 'lxml')
            self.rawData = self.yahooFinanceData.find(class_='My(6px) Pos(r) smartphone_Mt(6px) W(100%)')
            if self.rawData == None:
                self.valid_stock = False
                return 'Not a valid stock'
        return self.link

    def getStats(self):
        if self.valid_stock:
            self.STOCK_INFO = self.rawData.text
            self.STOCK_INFO = self.STOCK_INFO.replace('(', '')
            self.STOCK_INFO = self.STOCK_INFO.replace(')', '')
            self.STOCK_INFO = self.STOCK_INFO.replace('Advertisement', '')
            self.STOCK_INFO = self.STOCK_INFO.replace('At close: ', '')
            self.STOCK_INFO = self.STOCK_INFO.replace('EDT', '')
            self.STOCK_INFO = self.STOCK_INFO.replace('After hours:', '')
            self.STOCK_INFO = self.STOCK_INFO.rstrip()

            if self.STOCK_INFO.find('-') > 0:
                self.STOCK_INFO = self.STOCK_INFO.replace('-', ' -', 1)
            if self.STOCK_INFO.find('+') > 0:
                self.STOCK_INFO = self.STOCK_INFO.replace('+', ' +', 1)
            self.STOCK_INFO = self.STOCK_INFO.split(' ')

            return f'{self.STOCK_INFO}'
        return 'Not a valid stock'

    def getTitle(self):
        if self.valid_stock:
            self.title = self.yahooFinanceData.find('title').text
            self.title = self.title.replace('Stock Price, News, Quote & History - Yahoo Finance', '')
            return self.title
        return 'Not a valid stock'

    def sharePrice(self):
        if self.valid_stock:
            return self.STOCK_INFO[0]
        return 'Not a valid stock'