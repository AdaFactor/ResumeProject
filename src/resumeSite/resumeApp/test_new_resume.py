import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

project_dir = os.path.dirname(os.path.abspath('../../'+__file__))
firefox_dir = '/'.join([project_dir, 'drivers/geckodriver'])
browser = webdriver.Firefox(executable_path=firefox_dir)
browser.get('http://localhost:8000/templates/new/resume')

# Login Page
# Find elements
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
login_btn = browser.find_element_by_id('btn-login')

# Sendkey Text
username.send_keys('tester')
password.send_keys('1234')
login_btn.click()

# Index Page
# Find Elements
new_resume_btn = browser.find_element_by_id('new-resume')

# SendKey Text
new_resume_btn.click()
time.sleep(1)
# Resume Page
# Find Elements
first_name_en = browser.find_element_by_id('id_first_name_en')
last_name_en = browser.find_element_by_id('id_last_name_en')
birthday = browser.find_element_by_id('id_birthday')
age = browser.find_element_by_id('id_age')
gender = Select(browser.find_element_by_id('id_gender'))
nationality = browser.find_element_by_id('id_nationality')
religion = Select(browser.find_element_by_id('id_religion'))
phone_no = browser.find_element_by_id('id_phone_no')
email = browser.find_element_by_id('id_email')
address_en = browser.find_element_by_id('id_address_en')
# education = Select(browser.find_element_by_id('id_education'))
# reference = Select(browser.find_element_by_id('id_reference'))
# language = Select(browser.find_element_by_id('id_language'))
first_name_th = browser.find_element_by_id('id_first_name_th')
last_name_th = browser.find_element_by_id('id_last_name_th')
address_th = browser.find_element_by_id('id_address_th')
# skill = Select(browser.find_element_by_id('id_skill'))
# experience = Select(browser.find_element_by_id('id_experience'))
activity = browser.find_element_by_id('id_activity')
hobby = browser.find_element_by_id('id_hobby')
save_btn = browser.find_element_by_id('submit-id-save')

# SendKeys
first_name_en.send_keys('Arkane')
last_name_en.send_keys('Kaminkure')
age.send_keys(22)
gender.select_by_index(1)
nationality.send_keys('Thai')
religion.select_by_index(1)
phone_no.send_keys('0919594945')
email.send_keys('adadesions@gmail.com')
address_en.send_keys(
    '207 AdaFactor 2nd Mahadthai Rd., Muang, Nai-muang, Nakhonratchasima 30000'
)
# education.select_by_index(0)
# reference.select_by_index(1)
# language.select_by_index(0)
first_name_th.send_keys('อาคาเณย์')
last_name_th.send_keys('ขมิ้นเครือ')
address_th.send_keys(
    '207 เอด้าเฟรกเตอร์ ชั้น 2 ถ.มหาดไทย อ.เมือง ต.ในเมือง จ.ครราชสีมา 30000'
)
# skill.select_by_index(0)
# experience.select_by_index(0)
activity.send_keys(
    '#กิจกรรมช่วยเหลือสังคม #กิจกรรมทำความดีถวายพ่อหลวง #อาสาสมัครมูลนิธิ'
)
hobby.send_keys(
    '#แก้โจทย์คณิตศาสตร์ #เขียนโปรแกรมคอมพิวเตอร์'
)

# save_btn.click()

# prefix = Select(browser.find_element_by_id('id_prefix'))
# first_name = browser.find_element_by_id('id_first_name')
# last_name = browser.find_element_by_id('id_last_name')
# citizen_id = browser.find_element_by_id('id_citizen_id')
# gender = Select(browser.find_element_by_id('id_gender'))
# date_birthday = browser.find_element_by_id('id_date_birth')
# phone_no = browser.find_element_by_id('id_phone_no')
# house_no = browser.find_element_by_id('id_house_no')
# resident_name = browser.find_element_by_id('id_resident_name')
# village_no = browser.find_element_by_id('id_village_no')
# road = browser.find_element_by_id('id_road')
# alley = browser.find_element_by_id('id_alley')
# area = Select(browser.find_element_by_id('id_area'))
# subarea = Select(browser.find_element_by_id('id_sub_area'))
# province = browser.find_element_by_id('id_province')
# post_code = browser.find_element_by_id('id_post_code')
# email = browser.find_element_by_id('id_email')
# reference_person = browser.find_element_by_id('id_reference_person')
# submit = browser.find_element_by_id('id_submit')


# Sendkey to Select
# prefix.select_by_visible_text('นาย')
# gender.select_by_visible_text('ชาย')
# time.sleep(0.5)
# area.select_by_index(1)
# time.sleep(0.5)
# subarea.select_by_index(1)
