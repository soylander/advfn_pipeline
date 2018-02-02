from models import ADVFNScraper
import os
import errno
from settings import DATA_PATH

if __name__ == '__main__':
    
    page = ADVFNScraper(data_path = DATA_PATH)

    page.set_symbol_and_date('AAPL', 0)
    page.read_html()
    if page.data_exists():
        page.html_to_file()



