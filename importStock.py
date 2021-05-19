import requests
from bs4 import BeautifulSoup
import gspread

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}


gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1PtkNfz_youMtW7DQ5meMZNJGJ0aMz8V_wINLceilTjo')
worksheet = sh.sheet1

def startto():
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

    #EPS of the company 
    getEps = ""
    eps = ['E', 'P', 'S']
    mylist = list()
    filteredList = list()
    for tbody in dataTable.find_all('tbody'):
        rows = tbody.find('tr').text
        if "EPS" in rows:
            for ch in rows:
                if " " not in ch:
                    mylist.append(ch.strip())
    for i in mylist:
        if i not in eps:
            filteredList.append(i)

    for i in filteredList:
        getEps = getEps + i
    # print(getEps)     

    #P/E Ratio
    getPE = ""
    peRatio = ['P', '/', 'E', 'R', 'a', 't', 'i', 'o']
    mylist = list()
    filteredList = list()
    for tbody in dataTable.find_all('tbody'):
        rows = tbody.find('tr').text
        if "P/E" in rows:
            for ch in rows:
                if " " not in ch:
                    mylist.append(ch.strip())
    for i in mylist:
        if i not in peRatio:
            filteredList.append(i)

    for i in filteredList:
        getPE = getPE + i
    # print(getPE)


    #Bonus
    getBonus = ""
    bonus = ['%', 'B', 'o', 'n', 'u', 's']
    mylist = list()
    filteredList = list()
    for tbody in dataTable.find_all('tbody'):
        rows = tbody.find('tr').text
        if "Bonus" in rows:
            for ch in rows:
                if " " not in ch:
                    mylist.append(ch.strip())
    for i in mylist:
        if i not in bonus:
            filteredList.append(i)

    for i in filteredList:
        getBonus = getBonus + i
    # print(getBonus)


    #Dividend
    getDividend = ""
    dividend = ['%', 'D', 'i', 'v', 'i', 'd', 'e', 'n', 'd']
    mylist = list()
    filteredList = list()
    for tbody in dataTable.find_all('tbody'):
        rows = tbody.find('tr').text
        if "Dividend" in rows:
            for ch in rows:
                if " " not in ch:
                    mylist.append(ch.strip())
    for i in mylist:
        if i not in dividend:
            filteredList.append(i)

    for i in filteredList:
        getDividend = getDividend + i
    # print(getDividend)


    #RightShare
    getRShare = ""
    rightShare = ['R','i','g','h','t','S','h','a','r','e']
    mylist = list()
    filteredList = list()
    for tbody in dataTable.find_all('tbody'):
        rows = tbody.find('tr').text
        if "RightShare" in rows:
            for ch in rows:
                if " " not in ch:
                    mylist.append(ch.strip())
    for i in mylist:
        if i not in rightShare:
            filteredList.append(i)

    for i in filteredList:
        getRShare = getRShare + i
    # print(getRShare)

    #Sector
    getSector = ""
    sector = ['S','e','c','t','o','r']
    mylist = list()
    filteredList = list()
    for tbody in dataTable.find_all('tbody'):
        rows = tbody.find('tr').text
        if "Sector" in rows:
            for ch in rows:
                if " " not in ch:
                    mylist.append(ch.strip())
    for i in mylist:
        if i not in sector:
            filteredList.append(i)

    for i in filteredList:
        getSector = getSector + i
    # print(getSector)

    # #120 Average
    # getAverage = ""
    # average = ['1','2','0','D','a','y','A','v','e','r','a','g','e']
    # mylist = list()
    # filteredList = list()
    # for tbody in dataTable.find_all('tbody'):
    #     rows = tbody.find('tr').text
    #     if "120 Day Average" in rows:
    #         for ch in rows:
    #             if " " not in ch:
    #                 mylist.append(ch.strip())
    # for i in mylist:
    #     if i not in average:
    #         filteredList.append(i)

    # for i in filteredList:
    #     getAverage = getAverage + i
    # # print(getSector)

    scripInsert =[companyName, symbol, getSector, marketPrice, getEps, getPE, getDividend, getBonus, getRShare, "UnderConstruction"]
    worksheet.append_row(scripInsert)

    print("Company name : " + companyName)
    print("Symbol       : " + symbol)
    print("Sector       : " + getSector)
    print("Market Price : " + marketPrice)
    print("EPS          : " + getEps)
    print("P/E          : " + getPE)
    print("Dividend     : " + getDividend + "%")
    print("Bonus        : " + getBonus + "%")
    print("Right Share  : " + getRShare)
  #  print("120 Average  : " + getAverage)
    print("Data Insesrted")


    #Searches the row for given symbol
    # test = worksheet.col_values(2)
    # rownum = test.index(symbol) + 1
    # row = worksheet.row_values(rownum) 
    # worksheet.update

if __name__ == "__main__":
    while True:
        startto()
        wantToExit = input("Do you wish to quit? y/n? : ")
        if(wantToExit.lower() == 'y'):
            break
