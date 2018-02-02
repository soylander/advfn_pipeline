REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# This is the base URL. 
# It is extended with some parameters in the class (symbol and date index).
BASE_ADVFN_URL = ('https://uk.advfn.com/p.php?pid=financials'
                    '&btn=istart_date&mode=quarterly_reports')
# Example full url (APPL,0):
# https://uk.advfn.com/p.php?pid=financials&btn=istart_date&mode=quarterly_reports&symbol=NASDAQ%3AAAPL&istart_date=0

#This is where the data is saved. A new folder is created for every symbol
DATA_PATH = '/home/christian/Dev/privateProjects/magicFormula/pipeline/data/html/'

# A search string for finding out if there is data on the html page
ADVFN_STOP_TARGET = 'No financial data available from this page'

BASE_WIKI_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'