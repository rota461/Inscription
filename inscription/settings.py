
import configparser
import os

class Settings(object):
    def __init__(self):
        self.cdir = os.path.dirname(os.path.abspath(__file__))
        self.config = configparser.ConfigParser()

        self.PATH = []
        self.TEMPLATE = []

    def read_config(self, path):
        conf_path = os.path.join(path, 'config.ini')
        self.config.read(conf_path)

        self.PATH = self.config['PATH'] 
        self.TEMPLATE = self.config['TEMPLATE']