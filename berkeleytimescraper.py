'''
This scrapes the important info for the classes one imports

inputs, name of the class as list ['name', 'number']
outputs: 
        list of lists:
          [num (int), 
          type (str), 
          class # (int), 
          time [[days], start, end], #start and end in minutes, days int 1-7 for the days of the week
          location [building, room],
          Instructor (str),
          Date (str),
          waitlist (int),
          final exam time [[day], start, end] (may be none if final exam was stated in an earlier num)]
'''

import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

baseurl = 'https://www.berkeleytime.com/catalog/'
def getinfo(name, number):
    #first make the url
    url = baseurl + name + '/' + str(number)
    
    ### from cs50finalproject, Matt Kristoffersen 2018
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    ###

    driver = webdriver.Chrome(options=chrome_options, executable_path=os.path.abspath('chromedriver'))
    
    driver.get(url)
    driver.implicitly_wait(3)
    button = driver.find_elements_by_class_name('section-info-button')[0]
    button.click()
    driver.implicitly_wait(3)
    raw_info = driver.find_elements_by_tag_name('td')
    finish = [tag.text for tag in raw_info]
    driver.quit()
    return formatting(finish)

def formatting(lst):
    formatted = []
    #tries to make anything it can into an integer
    for i in range(len(lst)):
        try:
            formatted.append(int(lst[i]))
        except:
            formatted.append(lst[i])
    #   either if lst is empty or nothing in the list can be integerized, then it is an invalid input
    #   and we return an empty list.
    if formatted == lst:
        return []
    #   grouping
    formatted = [formatted[i:i+9] for i in range(0, len(formatted), 9) if formatted[i]]
    #   Formatting times
    for i in range(len(formatted)):
        #class time
        formatted[i][3] = time_formatter(formatted[i][3])
        
        #location:
        if formatted[i][4] == 'OFF CAMPUS':
            formatted[i][4] == []
        else:
            formatted[i][4] = formatted[i][4].split()
        
        #Final exam time:
        if formatted[i][8]:
            formatted[i][8] = time_formatter(formatted[i][8])
    
    return formatted
        
def time_formatter(raw):
    days = {'M': [1], 'Tu': [2], 'W': [3], 'Th': [4], 'F': [5], 'S': [6], 'Su': [7], 'MWF': [1, 3, 5]}
    time_raw = raw.split()
    time = []
    time.append(days[time_raw[0]])

    #helper function
    def helper(raw, afternoon=False):
        if ':' in raw:
            minutes = 60 * int(raw[:raw.index(':')]) + int(raw[raw.index(':')+1:])
        else:
            minutes = 60 * int(raw)
        if afternoon and minutes < 720:
            return minutes + (12 * 60)
        return minutes
    
    if time_raw[2] == 'PM':
        time.append(helper(time_raw[1], True))
        time.append(helper(time_raw[4], True))
    else:
        time.append(helper(time_raw[1]))
        if time_raw[5] == 'PM':
            time.append(helper(time_raw[4], True))
        else:
            time.append(helper(time_raw[4]))
    
    return time
