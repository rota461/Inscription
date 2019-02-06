
import configparser
import os

class Settings:
    def __init__(self):
        self.cdir = os.getcwd()
        self.config = configparser.ConfigParser()
        
        self.PATH = []

        self.read_config()

    def read_config(self):
        conf_path = os.path.join(self.cdir, 'config.ini')
        self.config.read(conf_path)
        self.PATH = self.config['PATH'] 
