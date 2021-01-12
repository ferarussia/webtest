#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pytube import Playlist
pl = Playlist("https://youtube.com/playlist?list=PL6QnpHKwdPYiIST1Ydh6sGo6tnC9mLaPR")


# In[2]:


# Imports
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import urllib.request
import pickle
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# In[3]:


# Configuration Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# In[4]:



# Webdriver Configuration
option = selenium.webdriver.ChromeOptions()
option.add_argument("--headless") #Running on server (mybinder)
#option.add_argument("--start-maximized") #Running Local
#pathWebDriverWindows = 'D:/ProgramFiles/chromedriver_win32/chromedriver.exe'
pathWebDriverLinux='./chromedriver'


# In[5]:


browser = selenium.webdriver.Chrome(executable_path=pathWebDriverLinux, chrome_options=option)


# In[6]:


wait = WebDriverWait(browser, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located


# In[7]:


import time
from selenium.webdriver.common.keys import Keys


# In[ ]:



# Open a web browser and load a website
# Runnig local on a windows Machine
#browser = selenium.webdriver.Chrome(executable_path=pathWebDriverWindows, chrome_options=option)
# Running on a Linux Server (mybinder)
for j in range(100):
    for i,video in enumerate(pl):
        #html='https://www.youtube.com/watch?v=9T3CsQTDwoU&list=PL6QnpHKwdPYjSd70K-CNqYp9oGplJYbVM&index=%d&mute=1&autoplay=1'%i
        try:
            print(i)
            browser.get(video)
            time.sleep(10)
            #browser.save_screenshot('%d.png'%i)
            actions = ActionChains(browser) 
            actions.send_keys(Keys.TAB * 2)
            actions.perform()
            time.sleep(10)
            elem = browser.switch_to.active_element
            elem.click()
            time.sleep(10)
            #browser.save_screenshot('%dx1.png'%i)
            #wait.until(visible((By.ID, "video-title")))
            #browser.find_element_by_id("video-title").click()
            actions = ActionChains(browser) 
            actions.send_keys(Keys.SPACE)
            actions.perform()
            time.sleep(10)
            while True:
                time.sleep(5)
                player_status = browser.execute_script("return document.getElementById('movie_player').getPlayerState()")
                print('Status',player_status)
                if player_status==2:
                    actions = ActionChains(browser) 
                    actions.send_keys(Keys.SPACE)
                    actions.perform()

                if player_status==0:
                    #browser.save_screenshot('%dx2.png'%i)
                    break
        except:
            print('erroe',i)
            #browser = selenium.webdriver.Chrome(executable_path=pathWebDriverLinux, chrome_options=option)
            pass
        
    


# In[ ]:




