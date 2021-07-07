
from os import name
from typing import Union
from bs4 import BeautifulSoup
import requests
from fake_headers import Headers


URL = "https://1lib.in"

COLUMN = [
    "id",
    "name",
    "thumbnail_url",
    "publisher",
    "publisher_url",
    "author",
    "author_url",
    "book_url",
    "year",
    "language",
    "extension",
    "size",
]

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
        SEARCH_URL = f"{URL}/s/{query.replace(' ','%20')}/?"
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


            Parameters:
                    url (str): The object Scrap().search(*args, *kwargs)
                    order (str): The sort order
            * popular - Sort by popularity (desc)
            * bestmatch - Sort by Best match (desc)
            * date - Sort by Recently added (desc)
            * titleA - Sort by Title(A-Z)
            * title - Sort by Title(Z-A)
            * year - Sort by Year of publication (desc)
            * filsize - Sort by File size (desc)
            * filesizeA - Sort by File size (asc)
            Returns:
                    (str): url with sorted feature.
        """
        return f"{url}&order={order}"


    def scrap(self, url:str):
        """
        """
        #header = Headers(browser="chrome", os="win", headers=True)
        res = requests.get(url=url).text
        soup = BeautifulSoup(markup=res, features='lxml')
    
        names = soup.find_all(name="a", attrs={"style": "text-decoration: underline;"})
        names = [i.text for i in names]
        thumb_img = soup.find_all(name="img", attrs={"class": "cover lazy"})
        thumb_img = [i.get('data-src') for i in thumb_img]
        book_url = soup.find_all(name="h3", attrs={"itemprop": "name"})
        book_url = [f"{URL}{book_url[i].a.get('href')}" for i in range(len(book_url))]
        id = [i.split('/')[5] for i in book_url]
        
        publisher = soup.find_all(name="div", attrs={"title": "Publisher"})
        publisher_url = [f"{URL}{i.find(name='a').get('href')}" for i in publisher]
        publisher = [i.find(name = "a").text for i in publisher]
        author_scrap = soup.find_all(name="div", attrs={"class": "authors"})
        author_url = []
        authors = []
        for i in author_scrap:
            authors_dict = {}
            author_url_dict = {}
            auth_per_book = i.find_all("a", {"title": "Find all the author's books"})
            if len(auth_per_book) > 1:
                for i in range(len(auth_per_book)):
                    authors_dict[i] = auth_per_book[i].text
                    author_url_dict[i] = auth_per_book[i].get("href")
                author_url.append(author_url_dict)
                authors.append(authors_dict)
            else:
                author_url.append(auth_per_book[0].get("href"))
                authors.append(auth_per_book[0].text)
        #print(len(author_url))
        #print(len(authors))
        year = soup.find_all(name="div", attrs={"class": "bookProperty property_year"})
        year = [i.find("div", {"class": "property_value"}).text for i in year]
        lang = soup.find_all(name="div", attrs={"class": "bookProperty property_language"})
        lang = [i.find("div", {"class": "property_value"}).text for i in lang]
        size_n_ext = soup.find_all(name="div", attrs={"class": "bookProperty property__file"})
        size_n_ext = [i.find("div", {"class": "property_value"}).text for i in size_n_ext]
        size = []
        extenstion = []
        for i in size_n_ext:
            size_ext = i.split(', ')
            size.append(size_ext[1])
            extenstion.append(size_ext[0])
        print(f"id {len(id)}")
        print(f"names {len(names)}")
        print(f"thumb_img {len(thumb_img)}")
        print(f"book_url {len(book_url)}")
        print(f"publisher_url {len(publisher_url)}")
        print(f"publisher {len(publisher)}")
        print(f"author_url {len(author_url)}")
        print(f"authors {len(authors)}")
        print(f"year {len(year)}")
        print(f"lang {len(lang)}")
        print(f"size {len(size)}")
        print(f"ext {len(extenstion)}")
        #return_list = []
        '''
        for i in range(len(id)):
            return_list.append(
                {
                    "id": id[i],
                    "name": names[i],
                    "thumbnail_url": thumb_img[i],
                    "publisher": publisher[i],
                    "publisher_url": publisher_url[i],
                    "author": author[i],
                    "author_url": author_url[i],
                    "book_url": book_url[i],
                    "year": year[i],
                    "language": lang[i],
                    "extension": extenstion[i],
                    "size": size[i],
                }
            )
        return return_list'''

        



    def download_url(self, url: str) -> str:
        book_res = requests.get(url=url).text
        book_soup = BeautifulSoup(markup=book_res, features="lxml")
        dl_url = f"{URL}{book_soup.find(name='a', attrs={'class': 'btn btn-primary dlButton addDownloadedBook'}).get('href')}"
        return dl_url



a = Scrap()
b = a.search(query="automate the boring stuff with python", lang=['english'], ext='pdf')
c = a.sort_search(url=b, order='filesize')
print(a.scrap(c))
