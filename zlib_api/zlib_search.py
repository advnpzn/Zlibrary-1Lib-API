from bs4 import BeautifulSoup
from telegram import Message
from typing import Union
import requests
import fake_headers
from zlib_scrap import Scrap

class ZLib:
    def __init__(self) -> None:
        pass

    def search(
        self, 
        query:str, 
        lang:Union[str, list] = None,
        year_from:int = None, 
        year_to: int = None, 
        ext:Union[str, list] = None) -> dict:
        """self.query = query
        self.lang = lang
        self.year_from = year_from
        self.year_to = year_to
        self.ext = ext"""
        res = Scrap(query, lang, year_from, year_to, ext)    
    