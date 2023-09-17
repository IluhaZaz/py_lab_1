from bs4 import BeautifulSoup

import os

import requests

films = ["https://www.kinopoisk.ru/series/1032606/"]
header = {
    "User-Agent":"Safari/537.36"
}
for film in films:
    good_comment_num = 1
    bad_comment_num = 1
    film_page = requests.get(film, headers=header).content
    soup = BeautifulSoup(film_page, "lxml")
    for comment in soup.find_all("section", class_ = "styles_root__644Yf styles_review__GN2Uy styles_rootPositive__sl4cN"):
        with open(f"C:/python_lab1/dataset/good/{good_comment_num}", "w", encoding = "utf-8") as file:
            file.write(comment.text)
            good_comment_num+=1
    for comment in soup.find_all("section", class_ = "styles_root__644Yf styles_review__GN2Uy styles_rootNegative___OV9G"):
        with open(f"C:/python_lab1/dataset/bad/{bad_comment_num}", "w", encoding = "utf-8") as file:
            file.write(comment.text)
            bad_comment_num+=1
                
        


