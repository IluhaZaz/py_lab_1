from bs4 import BeautifulSoup
from time import sleep
import os
from fake_useragent import UserAgent
import requests

films = ["https://www.kinopoisk.ru/film/1032606/reviews/ord/rating/status/all/perpage/200/", "https://www.kinopoisk.ru/film/4484/reviews/ord/date/status/all/perpage/200/",
         "https://www.kinopoisk.ru/film/915196/reviews/ord/date/status/all/perpage/200/", "https://www.kinopoisk.ru/film/495892/reviews/ord/date/status/all/perpage/200/",
         "https://www.kinopoisk.ru/film/404366/reviews/ord/date/status/all/perpage/200/"]
header = {"User-Agent":UserAgent().random, 
          "referrer":"https://sso.kinopoisk.ru/", 
          "cookie":"L=fQ5KeUJhVV99WnVScXNCDw5Wc353CWN+ChYkKHB1dkU=.1676924953.15259.367197.77"}
good_comment_num = 1
bad_comment_num = 1
film_count = 1
session = requests.Session()
session.auth = ('user', 'pass')
for film in films:
    soup = BeautifulSoup(session.get(film, headers=header).content, "lxml")
    film_name = BeautifulSoup(str(soup.find("a", class_ = "breadcrumbs__link")), "lxml").text
    for comment in soup.find_all("div", class_ = "response good"):
        comment = BeautifulSoup(str(comment), "lxml").findChild("span", class_="_reachbanner_")
        with open(f"dataset/good/0{good_comment_num}", "w", encoding = "utf-8") as file:
            file.write(film_name)
            file.write(BeautifulSoup(str(comment), "lxml").text)
            good_comment_num+=1
    for comment in soup.find_all("div", class_ = "response bad"):
        comment = BeautifulSoup(str(comment), "lxml").findChild("span", class_="_reachbanner_")
        with open(f"dataset/bad/0{bad_comment_num}", "w", encoding = "utf-8") as file:
            file.write(film_name)
            file.write(BeautifulSoup(str(comment), "lxml").text)
            bad_comment_num+=1
    sleep(20*film_count/1.1 - 0.2)
    film_count+=1

                
        


