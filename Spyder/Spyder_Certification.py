import re
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def getImage(url, count):
    browser = webdriver.Chrome()
    try:
        browser.get(url)
    except TimeoutException:
        print('请求超时')
    wait = WebDriverWait(browser, 1000)

    head = 'http://cwcx.zju.edu.cn/WFManager/loginAction_getCheckCodeImg.action?s='
    tail = ''
    for i in range(count):
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkcodeImg')))
        if submit:
            submit.click()
            html = browser.page_source.encode("utf-8").decode()
            time.sleep(3)
            tail = re.search('\d\d\d.[0-9]{13}', html).group()
        ImageUrl = head + tail
        save_path = 'F:/Workspace/DATA_STRUCTURE/Download1/' + str(i + 108) + '.png'
        r = requests.get(ImageUrl)
        with open(save_path, 'wb') as f:
            f.write(r.content)


def main():
    count = 50
    url = "http://cwcx.zju.edu.cn/WFManager/login.jsp"
    getImage(url, count)


if __name__ == "__main__":
    main()
