from bs4 import BeautifulSoup
from utils import make_directory
import urllib2
from settings import (REQUEST_HEADER, BASE_ADVFN_URL, ADVFN_STOP_TARGET, 
    BASE_WIKI_URL)

class BaseScraper(object):

    def __init__(self, data_path, header, base_url, stop_target = ''):
        self.data_path = data_path
        self.header = header
        self.base_url = base_url
        self.full_url = base_url
        self.stop_target = stop_target

    def read_html(self):
        self.generate_full_url()
        if self.header:
            req = urllib2.Request(self.full_url, None, self.header)
        else:
            req = urllib2.Request(self.full_url)
        response = urllib2.urlopen(req)
        self.html = response.read()
        print('READ: ' + self.__repr__())

    def default_filename(self):
        return 'Undefined_File'

    def default_relative_path(self):
        # The html_to_file will create this directory
        # Example: 'My_dir/'
        return ''

    def generate_full_url(self):
        # Purpose of this function is to be overridden if additional parameters
        # should be added to the base url.
        pass

    def html_to_file(self, filename = None, path = None, mode = 'wb', 
            dir_name = None):
        if not filename:
            filename = self.default_filename()
        if not path:
            path = self.data_path
        if not dir_name:
            dir_name = self.default_relative_path()
        full_path = path + dir_name + filename
        make_directory(full_path)
        with open(full_path, mode) as f:
            f.write(self.html)
        print('WRITE: ' + full_path)

    def data_exists(self):
        if self.stop_target not in self.html:
            return True
        return False

class ADVFNScraper(BaseScraper):

    def __init__(self, data_path, header = REQUEST_HEADER):
        super(ADVFNScraper, self).__init__(data_path, header, BASE_ADVFN_URL, 
            ADVFN_STOP_TARGET)

    def __repr__(self):
        return '<ADVFNScraper(symbol={}, i_date={})>'.format(
            self.symbol, str(self.i_date))

    def set_symbol_and_date(self, new_symbol, new_i_date):
        self.symbol = new_symbol
        self.i_date = new_i_date

        if len(self.symbol) >= 4:
            self.exchange = 'NASDAQ'
        else:
            self.exchange = 'NYSE'

    def generate_full_url(self):
        param_symbol = '&symbol=' + self.exchange + '%3A' + self.symbol
        param_start_date_index = '&istart_date=' + str(self.i_date)
        self.full_url = (self.base_url + param_symbol + param_start_date_index)

    def reset_with_new_symbol(self, new_symbol):
        self.set_symbol_and_date(new_symbol, 0)

    def increase_date_index(self, delta_i_date = 5):
        new_i_date = self.i_date + delta_i_date
        self.set_symbol_and_date(self.symbol, new_i_date)

    def default_filename(self):
        return 'advfn_' + self.symbol.lower() + '_' + str(self.i_date) + '.html'

    def default_relative_path(self):
        return 'advfn_companies/' + self.symbol.lower() + '/'

class WikiSP500Scraper(BaseScraper):

    def __init__(self, data_path, header = REQUEST_HEADER):
        super(WikiSP500Scraper, self).__init__(data_path, header, 
            BASE_WIKI_URL)

    def default_filename(self):
        from datetime import datetime, date
        today = datetime.today()
        return 'wiki_sp500_' + str(today.year) + '_' + str(today.month) + '.html'

    def default_relative_path(self):
        return 'wiki_sp500/'
