from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

#1. Khai bao browser

browser=webdriver.Firefox(executable_path="./geckodriver")
#2. Mo facebook
url="https://www.facebook.com/groups/huongnghieptuvantuyensinh/"
browser.get(url)

#2a. Login facebook
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("***")
txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("***")
txtPass.send_keys(Keys.ENTER)

#3. Lay bai viet
sleep(5)
#choose1=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]")
#choose1.click()
#sleep(2)
#find = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/label/input")
#find.send_keys("hỏi")
#sleep(5)
#choose2=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/ul/li[2]/div/div[1]/div/div[1]/div/div")
#choose2.click()
#sleep(5)

# So lan truot
a=500

c=csv.writer(open("/home/taindp/PycharmProjects/crawl_csv.csv","w"))
index=0
while(a!=0):
    post = browser.find_elements_by_xpath("//div[@data-ad-preview='message']")
    sleep(10)
    print(len(post))
    print(a)
    a=a-1
    pgdn = browser.find_element_by_css_selector('body')
    pgdn.send_keys(Keys.PAGE_DOWN)
    sleep(10)

for ele in post:
    text=ele.get_attribute("textContent")
    c.writerow(text)
#4. Dung chuong trinh
sleep(5)
#5. Dong browser
browser.close()
