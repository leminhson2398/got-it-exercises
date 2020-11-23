import bs4
import pandas as pd
import requests


url = 'https://alonhadat.com.vn/nha-dat/can-ban/nha-trong-hem/ha-noi/407/quan-ba-dinh/trang--{pageNum}.html'


def get_page_content(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")


def process_parsed_content(soup: bs4.BeautifulSoup):
    list_pr = []
    list_sq = []
    list_rd = []
    list_fl = []
    list_di = []

    content_items = soup.findAll("div", class_="content-item")
    for house in content_items:

        # parse price:
        price = "0"
        try:
            price_text = house.find("div", class_="ct_price").text
            if price_text:
                price = price_text\
                    .strip()\
                    .split(" ", 1)[1]\
                    .replace(",", ".")
        except Exception:
            pass
        list_pr.append(price)

        # parse square
        square = "0"
        try:
            square_text = house.find("div", class_="ct_dt").text
            if square_text:
                square = square_text.strip().split(" ", 2)[2]
        except Exception:
            pass
        list_sq.append(square)

        # parse road width
        road = "0"
        try:
            road_text = house.find("span", class_="road-width").text
            road = road_text.strip()
        except Exception:
            pass
        list_rd.append(road)

        # parse floors
        floors = "0"
        try:
            floors_text = house.find("span", class_="floors").text
            if floors_text:
                floors = floors_text.strip().split(" ")[0]
        except Exception:
            pass
        list_fl.append(floors)

        # parse display
        dis = "0"
        try:
            dis_text = house.find("div", class_="ct_dis").text
            if dis_text:
                dis = dis_text.strip()
        except Exception:
            pass
        list_di.append(dis)

    return (list_pr, list_sq, list_rd, list_fl, list_di)


list_price = []
list_square = []
list_road = []
list_floors = []
list_dis = []


for i in range(1, 7, 1):
    newUrl = url.format(pageNum=i)
    parsedPage = get_page_content(newUrl)
    price, square, road, floors, dis = process_parsed_content(parsedPage)

    list_price.extend(price)
    list_square.extend(square)
    list_road.extend(road)
    list_floors.extend(floors)
    list_dis.extend(dis)

dFrame = pd.DataFrame({
    'Price': list_price,
    'Dien Tich': list_square,
    'Do Rong Mat Duong': list_road,
    'So Tang': list_floors,
    'Khoang Cach': list_dis
})

dFrame.to_csv("Data.csv", encoding="utf-8", index=False)
