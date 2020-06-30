from configparser import ConfigParser
from util.singleton import Singleton

class Config(metaclass=Singleton):
  def __init__(self, path:str='instance/config.ini'):
    self.path = path
    self.data = ConfigParser()
    self.data.read(self.path)
