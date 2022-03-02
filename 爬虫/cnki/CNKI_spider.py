import requests
import time
from lxml import etree
from fateadm_api import TestFunc as TF
from selenium import webdriver
from time import sleep
from lxml import etree
from selenium.webdriver.support.select import Select


def get_vcode():
    with open('./vcode_temp.png','rb') as f:
        img_content=f.read()
    vcode = TF(img_content)
    return vcode

def auto():
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": r"O:\情报学报"}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.maximize_window()
    driver.get("https://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB&crossDbcodes=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD")
    qikan = driver.find_elements_by_xpath('//*[@id="CJFQ"]/a')[0]  # 寻找
    qikan.click()
    sleep(1.5)

    #opt = driver.find_element_by_id('txt_1_sel')
    #Select(opt).select_by_visible_text('篇名')
    keywords1 = driver.find_element_by_id('txt_1_value1')  # 寻找第一个关键词输入框
    keywords1.send_keys("土壤修复")  # 传值
    check1 = driver.find_element_by_id("mediaBox3")
    check2 = driver.find_element_by_id("mediaBox4")
    check1.click()
    check2.click()
    btn1 = driver.find_element_by_id("btnSearch")  # 寻找检索按钮
    btn1.click()  # 点击检索
    sleep(1.5)

    driver.switch_to.frame('iframeResult')  # iframe的id
    page_text = driver.page_source  # 获取页面内容
    tree1 = etree.HTML(page_text)  # etree对象
    sleep(1.5)
    fifty_url = tree1.xpath('//*[@id="id_grid_display_num"]/a[3]/@href')[0]  # 我们设置每页显示50个，有利于快速获取
    new_url = 'https://kns.cnki.net' + fifty_url  # 在selenium中，访问50页会跳往新的页面（因为这里我们是get一个新的url,正常访问知网是不会跳页面的）
    driver.get(new_url)  # 跳转
    sleep(1.5)
    count=0
    for i in range(7):
        contents = driver.find_elements_by_xpath('//a[@class="briefDl_D"]')
        for content in contents:
            count += 1
            content.click()
            #sleep(1)
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            #sleep(1)
            try:
                vcode_img=driver.find_element_by_id('CheckCodeImg')
                vcode_img.screenshot("./vcode_temp.png")
                vcode=get_vcode()
                vcode_input=driver.find_element_by_id('CheckCode')
                vcode_input.send_keys(vcode)
            except:
                pass
            down = driver.find_element_by_id('Button2')
            down.click()
            sleep(1)
            driver.close()
            driver.switch_to.window(windows[0])
            #sleep(1000)
        try:
            next = driver.find_element_by_xpath(r"//div[@class='TitleLeftCell']/a[last()]")
            next.click()
        except:
            None



if __name__ == '__main__':
    auto()