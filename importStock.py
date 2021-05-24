import requests
from bs4 import BeautifulSoup
import gspread
import pyrebase

# Firebase configuration if we are using this
config ={
    "apiKey": "AIzaSyAbHTO3Ufs5rI6QXS4MKMEoqQ7ei6gHiUU",
    "authDomain": "sharemarketindex-2efa1.firebaseapp.com",
    "projectId": "sharemarketindex-2efa1",
    "storageBucket": "sharemarketindex-2efa1.appspot.com",
    "messagingSenderId": "722529550315",
    "appId": "1:722529550315:web:83ee0f88a5ca4d2833a3ae",
    "measurementId": "G-TTX4S7FNRR",
    "databaseURL": "https://sharemarketindex-2efa1-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

# Connect to firebase
firebase = pyrebase.initialize_app(config)
dataBase = firebase.database()

# Connect to sheets if needed
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1PtkNfz_youMtW7DQ5meMZNJGJ0aMz8V_wINLceilTjo')
worksheet = sh.sheet1

# Headers
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

# return company's needed data
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
    
    return value

# Collet Data from the companies
def starto():
    companiesUrl = "http://merolagani.com/LatestMarket.aspx"
    req = requests.get(companiesUrl, headers = headers)
    companySoup = BeautifulSoup(req.text, 'html.parser')

    #retrieve companies
    companyDataTable = companySoup.find('table', {'data-live' : 'live-trading'})

    with open("companies.txt", 'w') as file:
        tbody = companyDataTable.find('tbody')
        for a in tbody.find_all('a', {'target' : '_blank'}):
            file.write(a.text + "\n")

    myCompanies = list()
    with open("companies.txt", 'r') as file:
        data = file.read()
        myCompanies.append(data.split())

    count = 0
    for companies in myCompanies:
        for scrip in companies:
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

            sectorValue = getValue("Sector", dataTable)
            epsValue = getValue("EPS", dataTable)
            peValue = getValue("P/E Ratio", dataTable)
            percentageChangeValue = getValue("% Change", dataTable)
            dividendValue = getValue("% Dividend", dataTable)
            bonusValue = getValue("% Bonus", dataTable)
            rightShareValue = getValue("Right Share", dataTable)
            averageValue = getValue("120 Day Average", dataTable)

            '''Inserts into google sheet'''
            # scripInsert =[companyName, symbol, sectorValue, marketPrice, epsValue, peValue, dividendValue, bonusValue, rightShareValue, averageValue]
            # worksheet.append_row(scripInsert)

            ''' Firebase Data insertion command ''' 
            data = {
                "CompanyName" : companyName, 
                "Symbol" : symbol,
                "Market Price" : marketPrice,
                "EPS" : epsValue,
                "PE" : peValue,
                "Dividend" : dividendValue,
                "Bonus" : bonusValue,
                "RightShare" : rightShareValue,
                "120 Average" : averageValue,
            }

            dataBase.child("Companies Info").child(symbol).set(data)

            count += 1
            print(count, ". Company name : " + companyName)
            # print("Symbol       : " + symbol)
            # print("Sector       : " + sectorValue)
            # print("Market Price : " + marketPrice)
            # print("EPS          : " + epsValue)
            # print("P/E          : " + peValue)
            # print("Dividend     : " + dividendValue + "%")
            # print("Bonus        : " + bonusValue + "%")
            # print("Right Share  : " + rightShareValue)
            # print("120 Average  : " + averageValue)
            # print("Data Insesrted")


            #Searches the row for given symbol
            # test = worksheet.col_values(2)
            # rownum = test.index(symbol) + 1
            # row = worksheet.row_values(rownum) 
            # worksheet.update

# Main function
if __name__ == "__main__":
    while True:
        starto()
        wantToExit = input("Run Again? y/n? : ")
        if(wantToExit.lower() == 'n'):
            break