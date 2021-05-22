import requests
from bs4 import BeautifulSoup
import gspread

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}


gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1PtkNfz_youMtW7DQ5meMZNJGJ0aMz8V_wINLceilTjo')
worksheet = sh.sheet1

def getValue(rowName, dataTable):
    value = ""
    mylist = list()
    for tbody in dataTable.find_all('tbody'):
        rows = tbody.find('tr').text
        if rowName in rows:
            rows = tbody.find('td').text
            for ch in rows:
                if " " not in ch:
                    mylist.append(ch.strip())

    for i in mylist:
        value = value + i
    
    return value;

def starto():
    scrip = input("Enter your Scrip : ")


    url = "https://merolagani.com/CompanyDetail.aspx?symbol=" + scrip
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Gets Company Name from MeroLagani website and selects the table on the left side that has the company's share details
    companyName = soup.find('span', {'id' : 'ctl00_ContentPlaceHolder1_CompanyDetail1_companyName'}).text

    #finds the data table where the needed informations are stored in
    dataTable = soup.find('table', {'id' : 'accordion'})


    # Gets the recent market price of the company
    marketPrice = soup.find('span', {'id' : 'ctl00_ContentPlaceHolder1_CompanyDetail1_lblMarketPrice'}).text

    #Gets the company's symbol 
    symbol = soup.find('input', {'id' : 'ctl00_ContentPlaceHolder1_CompanyDetail1_StockGraph1_hdnStockSymbol'})['value']
    # print(symbol)

    sectorValue = getValue("Sector", dataTable)
    epsValue = getValue("EPS", dataTable)
    peValue = getValue("P/E Ratio", dataTable)
    percentageChangeValue = getValue("% Change", dataTable)
    dividendValue = getValue("% Dividend", dataTable)
    bonusValue = getValue("% Bonus", dataTable)
    rightShareValue = getValue("Righ Share", dataTable)
    averageValue = getValue("120 Day Average", dataTable)



    # scripInsert =[companyName, symbol, getSector, marketPrice, getEps, getPE, getDividend, getBonus, getRShare, "UnderConstruction"]
    # worksheet.append_row(scripInsert)

    print("Company name : " + companyName)
    print("Symbol       : " + symbol)
    print("Sector       : " + sectorValue)
    print("Market Price : " + marketPrice)
    print("EPS          : " + epsValue)
    print("P/E          : " + peValue)
    print("Dividend     : " + dividendValue + "%")
    print("Bonus        : " + bonusValue + "%")
    print("Right Share  : " + rightShareValue)
    print("120 Average  : " + averageValue)
    print("Data Insesrted")


    #Searches the row for given symbol
    # test = worksheet.col_values(2)
    # rownum = test.index(symbol) + 1
    # row = worksheet.row_values(rownum) 
    # worksheet.update

if __name__ == "__main__":
    while True:
        starto()
        wantToExit = input("Add another company? y/n? : ")
        if(wantToExit.lower() == 'n'):
            break
