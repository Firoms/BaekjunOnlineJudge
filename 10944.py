# import random
# print(random.randrange(1, 10001))


# 랜덤 문제인데 확률이 극악이라..
# 자동화로 해결해 보겠습니다.
# 역시 백준 사이트라 그런지.. 막히네요..
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://www.acmicpc.net/status?user_id=msg0909&problem_id=10944&from_mine=1"


id = "msg0909"
pw = "angel00!"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
driver = webdriver.Chrome(executable_path="C:\\코딩\\파이썬연습\\chromedriver.exe")

driver.implicitly_wait(3)
driver.get(URL)
driver.implicitly_wait(3)


driver.find_element_by_name("login_user_id").send_keys(id)
driver.find_element_by_name("login_password").send_keys(pw)
driver.find_element_by_class_name("btn-u pull-right").click()
