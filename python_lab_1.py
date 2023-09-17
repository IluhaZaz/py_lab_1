from bs4 import BeautifulSoup
from time import sleep
import os

import requests

films = ["https://www.kinopoisk.ru/film/1032606/reviews/ord/rating/status/all/perpage/200/", "https://www.kinopoisk.ru/film/4484/reviews/ord/date/status/all/perpage/200/",
         "https://www.kinopoisk.ru/film/915196/reviews/ord/date/status/all/perpage/200/", "https://www.kinopoisk.ru/film/495892/reviews/ord/date/status/all/perpage/200/",
         "https://www.kinopoisk.ru/film/404366/reviews/ord/date/status/all/perpage/200/"]
header = {"User-Agent":"YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36"}

for film in films:
    good_comment_num = 1
    bad_comment_num = 1
    soup = BeautifulSoup(requests.get(film, headers=header).content, "lxml")
    print(soup.text)
    for comment in soup.find_all("div", class_ = "response good"):
        with open(f"dataset/good/0{good_comment_num}", "w", encoding = "utf-8") as file:
            file.write(comment.text)
            good_comment_num+=1
    for comment in soup.find_all("div", class_ = "response bad"):
        with open(f"dataset/bad/0{bad_comment_num}", "w", encoding = "utf-8") as file:
            file.write(comment.text)
            bad_comment_num+=1
    sleep(5)

                
        


