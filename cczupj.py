import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome_options = Options()
#chrome_options.binary_location = r'<Chrome 可执行文件路径>'
driver = webdriver.Firefox()

driver.get('http://211.65.74.101/login_gh.aspx')


def wait_items_by_class_name(class_name):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name))
    )


def wait_item_by_id(id_):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id_))
    )

def wait_item_by_css(css_):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_))
    )

def accept_alert():
    t = 0
    time.sleep(1)
    while t < 25:
        try:
            driver.switch_to.alert.accept()
        except:
            time.sleep(0.2)
            t += 1


# page 1 - 登录
driver.find_element_by_id('UserName').send_keys('16416215')
driver.find_element_by_id('Password').send_keys('183314')
wait_item_by_id('getpassword').click()

# page 2 - 选择学生选课
# btn = driver.find_element_by_id('ImageButton1')
wait_item_by_id('ImageButton1').click()

# page 3 - 进入评教
# driver.execute_script('__doPostBack("GVxmxz", "Select$1")')
for item in wait_items_by_class_name('.dg1-item'):
    assert isinstance(item, WebElement)
    if '学生评教' in item.text:
        item.find_element_by_css_selector('input[type=button]').click()
        break

# page 4 - 点击图片
wait_item_by_id('ImageButton1').click()
#GVpjzb > tbody > tr:nth-child(6)
#GVpjzb > tbody > tr:nth-child(2)
#GVpjzb > tbody > tr:nth-child(2)
# page 5 - 评教页面
for i in range(1,len(wait_items_by_class_name('.dg1-item'))):
    driver.execute_script('__doPostBack("GVpjkc", "CmdPj$%s")' % i)
    for j in range(8):
        item = wait_item_by_css('#GVpjzb > tbody > tr:nth-child(%d)'%(j+2))
        item.find_element_by_css_selector('#GVpjzb_ctl0%d_RaBxz_0'%(j+2)).click()
    for j in range(8,20):
        item = wait_item_by_css('#GVpjzb > tbody > tr:nth-child(%d)'%(j+2))
        item.find_element_by_css_selector('#GVpjzb_ctl%d_RaBxz_0'%(j+2)).click()
    item = wait_item_by_css('#GVpjzb > tbody > tr:nth-child(2)')
    item.find_element_by_css_selector('#GVpjzb_ctl02_RaBxz_1').click()   
    # print(items)
    # for item in items:
        
    # random.choice(items).find_element_by_css_selector('#GVpjzb_ctl02_RaBxz_1"]').click()

    elem = wait_item_by_css('#DDztpj')
    elem.find_element_by_css_selector('option[value="很好"]').click()
    wait_item_by_css('#BTjc').click()
    accept_alert()

    try:
        wait_item_by_css('#BTbc').click()
        accept_alert()
    except:
        driver.back()

driver.close()
