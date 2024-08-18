from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import time
def jandi(name):
    response = driver.page_source
    soup = BeautifulSoup(response, "html.parser")
    daybefore = 1
    weekday = datetime.today().weekday()-daybefore
    if weekday <= -1:
        weekday = 7 - daybefore
        if weekday == 0:
            element = soup.find("td", {"id": "contribution-day-component-1-51"})
        elif weekday == 1:
            element = soup.find("td", {"id": "contribution-day-component-2-51"})
        elif weekday == 2:
            element = soup.find("td", {"id": "contribution-day-component-3-51"})
        elif weekday == 3:
            element = soup.find("td", {"id": "contribution-day-component-4-51"})
        elif weekday == 4:
            element = soup.find("td", {"id": "contribution-day-component-5-51"})
        elif weekday == 5:
            element = soup.find("td", {"id": "contribution-day-component-6-51"})
        elif weekday == 6:
            element = soup.find("td", {"id": "contribution-day-component-0-51"})
        else:
            element = None
    else:
        if weekday == 0:
            element = soup.find("td", {"id": "contribution-day-component-1-52"})
        elif weekday == 1:
            element = soup.find("td", {"id": "contribution-day-component-2-52"})
        elif weekday == 2:
            element = soup.find("td", {"id": "contribution-day-component-3-52"})
        elif weekday == 3:
            element = soup.find("td", {"id": "contribution-day-component-4-52"})
        elif weekday == 4:
            element = soup.find("td", {"id": "contribution-day-component-5-52"})
        elif weekday == 5:
            element = soup.find("td", {"id": "contribution-day-component-6-52"})
        elif weekday == 6:
            element = soup.find("td", {"id": "contribution-day-component-0-52"})
        else:
            element = None
    data_level = element.get("data-level")
    if data_level == "0":
        print("[ 벌금 ] "+name+"님은 커밋을 하지 않았어요.")
    else:
        print(name+"님은 잔디를 심었습니다.")

names = ['수정', '다은', '서준', '수민', '대휘', '주성']
urls = ['https://github.com/soojeongmin/','https://github.com/Chung-Daeun',
        'https://github.com/watashijxxnsuka','https://github.com/csm0062',
        'https://github.com/kimdaehwi990731','https://github.com/alohalo2']
driver = webdriver.Chrome()

for i in range(6):
    driver.get(urls[i])
    time.sleep(1)
    jandi(names[i])
