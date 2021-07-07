
from typing import Union
from bs4 import BeautifulSoup
import requests
from typing import Union

URL = "https://1lib.in/"

class Scrap:


    def search(
        self,
        query:str,
        lang:Union[str, list] = None,
        year_from:int = None, 
        year_to: int = None, 
        ext:Union[str, list] = None,
        exact_matching:bool = False) -> str:
        LANG_STR = None
        EXT_STR = None
        if type(lang) is list:
            LANG_STR = ""
            for i in range(len(lang)):
                LANG_STR = LANG_STR+f"&languages%5B{i}%5D={lang[i]}"
        elif type(lang) is str:
            LANG_STR = f"&languages%5B0%5D={lang}"

        if type(ext) is list:
            EXT_STR = ""
            for i in range(len(ext)):   
                EXT_STR = EXT_STR+f"&extensions%5B{i}%5D={ext[i]}"
        elif type(ext) is str:
            EXT_STR = f"&extensions%5B0%5D={ext}"
        SEARCH_URL = f"{URL}s/{query.replace(' ','%20')}/?"
        if exact_matching == True:
            SEARCH_URL = SEARCH_URL+"e=1"
        else:
            pass
        if year_from == None:
            pass
        else:
            SEARCH_URL = SEARCH_URL+f"&yearFrom={year_from}"
        if year_to == None:
            pass
        else:
            SEARCH_URL = SEARCH_URL+f"&yearTo={year_to}"
        if LANG_STR == None:
            pass
        else:
            SEARCH_URL = SEARCH_URL+LANG_STR
        if EXT_STR == None:
            pass
        else:
            SEARCH_URL = SEARCH_URL+EXT_STR  
        return SEARCH_URL

    
    def sort_search(self, url:str, order:str) -> str:
        """
        Returns the input url with sorted search.


            _Parameters:_
                    url (str): The object Scrap().search(*args, *kwargs)
                    order (str): The sort order
            * popular - Sort by popularity (desc)
            * bestmatch - Sort by Best match (desc)
            * date - Sort by Recently added (desc)
            * titleA - Sort by Title(A-Z)
            * title - Sort by Title(Z-A)
            * **year - Sort by Year of publication (desc)
            * filsize - Sort by File size (desc)
            * filesizeA - Sort by File size (asc)
            Returns:
                    (str): url with sorted feature.
        """
        return f"{url}&order={order}"


    def scrap(self, url:str) -> str:
        """
        """
        res = requests.get(url=url).text
        soup = BeautifulSoup(markup=res, features='lxml')
        divs = soup.find_all(name='div', attrs={'class': 'resItemBox resItemBoxBooks exactMatch'})
        return divs



a = Scrap()
b = a.search(query="automate the boring stuff with python", lang='english', ext='pdf')
c = a.sort_search(url=b, order='filesize')
print(a.scrap(c))
