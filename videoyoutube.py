from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import speedtest

import time 
import datetime
import socket

# driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

def create_web_driver():
    driver = webdriver.Chrome()

    driver.set_window_position(0, 0)
    driver.set_window_size(800, 600)
    return driver


driver = create_web_driver()
driver.get("https://www.youtube.com/watch?v=_-WWwNt8AzU")


time.sleep(3)

cookies_banner = driver.find_element(By.CLASS_NAME,"html5-video-container")
actionChains = ActionChains(driver)

actionChains.context_click(cookies_banner).perform()

#estadistica = driver.find_element(By.CLASS_NAME,"ytp-popup ytp-contextmenu")
estadistica = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[6]")
estadistica.click()

UP = '\033[1A'
CLEAR = '\x1b[2K'

# file = open('data.txt', 'a+')

while True:
    myTime = str(time.strftime(("%d-%m-%Y %H:%M:%S")))
    # file = open('log.txt', 'a+')

    print(f"Host:\t\t\t{socket.gethostbyname(socket.gethostname())}\n")
    res = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[23]/div/div[3]/span").text
    spd = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[23]/div/div[9]/span/span[2]").text
    nac = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[23]/div/div[10]/span/span[2]").text
    bff = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[23]/div/div[11]/span/span[2]").text
    lila = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[23]/div/div[12]/span/span[2]").text
    date = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[23]/div/div[16]/span").text
    printConsole = print(f"Resolution:\t\t{res}\nSpeed:\t\t\t{spd}\nNetwork Activity:\t{nac}\nBuffer:\t\t\t{bff}\nLive Latency:\t\t{lila}\nFecha:\t\t\t{date}\n")
    #pr = f"Speed:\t\t\t{spd}\nNetwork Activity:\t{nac}\nBuffer:\t\t\t{bff}\nLive Latency:\t\t{lila}\n"
    #print(pr)
    #print(f"{UP}Speed:\t\t\t{spd}{CLEAR}\n{UP}Network Activity:\t{nac}{CLEAR}\n{UP}Buffer:\t\t\t{bff}{CLEAR}\n{UP}Live Latency:\t\t{lila}{CLEAR}\n")
    
    # st = speedtest.Speedtest() 
    # download_speed = st.download()
    # upload_speed = st.upload()
    
    # print('Download Speed: {:5.2f} Mb'.format(download_speed/(1024*1024)))
    # # print('Upload Speed: {:5.2f} Mb'.format(upload_speed/(1024*1024)))
    # file = open('log.txt', 'a+')
    global youtubeStatistics
    youtubeStatistics = (socket.gethostbyname(socket.gethostname())+" "+res+" "+spd+" "+nac+" "+bff +" "+lila)
    # file.close()
    time.sleep(1)