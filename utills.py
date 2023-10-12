from time import sleep
import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

films = [
    "https://www.kinopoisk.ru/film/1032606/reviews/ord/rating/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/4484/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/915196/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/495892/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/404366/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/276129/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/263447/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/464963/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/409/reviews/ord/rating/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/261636/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/407636/reviews/ord/rating/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/361/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/81733/reviews/ord/rating/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/373314/reviews/ord/rating/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/1294123/reviews/ord/date/status/all/perpage/200/page/",
    "https://www.kinopoisk.ru/film/261636/reviews/ord/date/status/all/perpage/200/page/"
]

def main(rewiews_limit: int, dir_path: str) -> None:
    driver = webdriver.Edge()
    driver.maximize_window()
    good_comment_num = 1
    bad_comment_num = 1

    for film in films:
        for page in range(1, 5):
            try:
                driver.get(film + str(page) + "/")
            except:
                continue
            sleep(10)
            soup = BeautifulSoup(driver.page_source, "lxml")
            try:
                driver.find_element(By.CLASS_NAME, "CheckboxCaptcha-Button")
            except:
                pass
            else:
                driver.find_element(By.CLASS_NAME, "CheckboxCaptcha-Button").click()
                sleep(10)
            film_name = (
                BeautifulSoup(str(soup.find("a", class_="breadcrumbs__link")), "lxml").text
                + "\n"
            )
            
            for comment in soup.find_all("div", class_="response good"):
                if good_comment_num <= rewiews_limit:
                    comment = BeautifulSoup(str(comment), "lxml").findChild(
                        "span", class_="_reachbanner_"
                    )
                    with open(
                        os.path.join(dir_path, "dataset", "good", str(good_comment_num).zfill(4)), "w", encoding="utf-8"
                    ) as file:
                        file.write(film_name)
                        file.write(BeautifulSoup(str(comment), "lxml").text)
                        good_comment_num += 1
            for comment in soup.find_all("div", class_="response bad"):
                if bad_comment_num <= rewiews_limit:
                    comment = BeautifulSoup(str(comment), "lxml").findChild(
                        "span", class_="_reachbanner_"
                    )
                    with open(os.path.join(dir_path, "dataset", "bad", str(bad_comment_num).zfill(4)), "w", encoding="utf-8") as file:
                        file.write(film_name)
                        file.write(BeautifulSoup(str(comment), "lxml").text)
                        bad_comment_num += 1
            if soup.find("li", class_ = "arr") == None:
                break
            sleep(3)
    driver.close()
    driver.quit()

