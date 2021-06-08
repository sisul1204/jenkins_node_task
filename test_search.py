# * coding:utf-8 *
# Author:lizhipeng
# 创建时间: 2021/6/8 9:55
import time

from selenium import webdriver

def test_search():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    time.sleep(4)
    driver.close()
