#!/usr/bin/python
import urllib2
import time

def get_stock(stock, start, end, pos, total):
    url = 'http://quotes.money.163.com/service/chddata.html?fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP&code=' + stock + '&start=' + start + '&end=' + end
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
    f_output = open(stock, 'w')
    f_output.writelines(fd.read())
    f_output.close()
    fd.close()
    print '(%d'%pos + '/' + '%d'%total + ') write stock ' + stock + ' complete'

if __name__ == '__main__':
    start_time = '20160101'
    end_time = time.strftime('%Y%m%d',time.localtime(time.time()))

    f_stock = open('stocks.txt')
    list_stock = []
    while 1:
        line = f_stock.readline()
        if not line:
            break
        list_stock.append(line)
    f_stock.close()
    i = 0
    total = len(list_stock)
    for tmp_stock in list_stock:
        i = i + 1
        if tmp_stock[0:2] == '00' or tmp_stock[0:2] == '30':
            stock = '1' + tmp_stock[0:6]
            get_stock(stock, start_time, end_time, i, total)
        elif tmp_stock[0:2] == '60':
            stock = '0' + tmp_stock[0:6]
            get_stock(stock, start_time, end_time, i, total)
        else:
            print 'stock is not 00 or 60 or 30'
            break
