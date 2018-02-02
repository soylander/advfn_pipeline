from scrapers import ADVFNScraper, WikiSP500Scraper
from settings import DATA_PATH
import time

def scrape_advfn_symbol_i_date(symbol, i_date, sleep=None):
    page = ADVFNScraper(data_path = DATA_PATH)
    page.set_symbol_and_date(symbol, i_date)
    page.read_html()
    if page.data_exists():
        page.html_to_file()
    if sleep:
        time.sleep(sleep)

def scrape_advfn_symbol(symbol, i_date_start = 0, i_date_max = None, sleeptime = 1):

    page = ADVFNScraper(data_path = DATA_PATH)
    page.set_symbol_and_date(symbol, i_date_start)
    page.read_html()

    while page.data_exists():

        page.html_to_file()
        page.increase_date_index()

        if page.i_date >= i_date_max:
            print(' --STOPPED AT {}:{}-- \n'.format(page.symbol, page.i_date))
            break

        page.read_html()
        sleep(sleeptime)
    else:
        print(' --SUCCESSFUL DOWNLOAD FOR {}-- \n'.format(page.symbol))

def scrape_wiki():
    wiki_page = WikiSP500Scraper(data_path = DATA_PATH)
    wiki_page.read_html()
    wiki_page.html_to_file()

if __name__ == '__main__':

    # symbols = ['AAPL','MSFT','GOF']
    # for symbol in symbols:
    #     scrape_advfn_symbol(symbol = symbol, 
    #                         i_date_start = 0,
    #                         i_date_max = 200,
    #                         sleeptime = 0)

    scrape_advfn_symbol_i_date('AAPL', 5)


    




