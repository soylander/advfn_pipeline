from bs4 import BeautifulSoup
import urllib2
import os
import errno
from settings import REQUEST_HEADER, BASE_ADVFN_URL

STOP_TARGET = 'No financial data available from this page'

def make_directories(full_path):
    if not os.path.exists(os.path.dirname(full_path)):
        try:
            os.mkdir(os.path.dirname(full_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

class ADVFNScraper(object):

    def __init__(self, data_path, header = REQUEST_HEADER):
        self.data_path = data_path
        self.header = header
        self.base_url = BASE_ADVFN_URL

    def __repr__(self):
        return '<ADVFNScraper(symbol={}, i_date={})>'.format(
            self.symbol, self.i_date)

    def set_symbol_and_date(self, new_symbol, new_i_date):
        self.symbol = new_symbol
        self.i_date = str(new_i_date)

        if len(self.symbol) >= 4:
            self.exchange = 'NASDAQ'
        else:
            self.exchange = 'NYSE'

        param_symbol = '&symbol=' + self.exchange + '%3A' + self.symbol
        param_start_date_index = '&istart_date=' + self.i_date
        self.full_url = (self.base_url + param_symbol + param_start_date_index)

    def reset_with_new_symbol(self, new_symbol):
        self.set_symbol_and_date(new_symbol, 0)

    def increase_date_index(self, delta_i_date = 5):
        new_i_date = int(self.i_date) + int(delta_i_date)
        self.set_symbol_and_date(self.symbol, new_i_date)

    def read_html(self):

        if self.header:
            req = urllib2.Request(self.full_url, None, self.header)
        else:
            req = urllib2.Request(self.full_url)
        response = urllib2.urlopen(req)
        self.html = response.read()
        print('READ: ' + self.__repr__())

    def default_filename(self):
        return 'ADVFN_' + self.symbol + '_' + self.i_date + '.html'

    def html_to_file(self, filename = None, path = None, mode = 'wb'):
        if not filename:
            filename = self.default_filename()
        if not path:
            path = self.data_path
        symbol_dir = self.symbol + '/'
        full_path = path + symbol_dir + filename
        make_directories(full_path)
        with open(full_path, mode) as f:
            f.write(self.html)
        print('WRITE: ' + full_path)

    def data_exists(self):
        if STOP_TARGET not in self.html:
            return True
        return False
