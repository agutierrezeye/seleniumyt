import json
import socket
import time
import re

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

def create_web_driver():
    # chrome_options = Options()
    # chrome_options.add_extension(path.abspath('adblock_plus.crx'))
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()

    driver.set_window_position(0, 0)
    driver.set_window_size(800, 600)
    return driver

driver = create_web_driver()
driver.get("https://www.youtube.com/watch_popup?v=_-WWwNt8AzU")
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(20)

cookies_banner = driver.find_element(By.CLASS_NAME,"html5-video-container")

play = driver.find_element(By.CLASS_NAME, "ytp-large-play-button").click()
mute = driver.find_element(By.CLASS_NAME, "ytp-mute-button").click()
time.sleep(5)

def setQuality():
    quality = driver.find_element(By.CLASS_NAME, "ytp-settings-button").click()
    time.sleep(1)
    quality = driver.find_element(By.XPATH, "//div[@class='ytp-panel-menu']/div[3]").click()
    time.sleep(1)
    quality = driver.find_element(By.XPATH, '//span[text()="2160p"]').click()
    time.sleep(1)

actionChains = ActionChains(driver)
actionChains.context_click(cookies_banner).perform()

# estadistica = driver.find_element(By.CLASS_NAME,"ytp-popup ytp-contextmenu")
estadistica = driver.find_element(By.XPATH, "//div[@class='ytp-panel-menu']/div[7]")
estadistica.click()

# UP = '\033[1A'
# CLEAR = '\x1b[2K'

# file = open('data.txt', 'a+')

while True:
    myTime = str(time.strftime(("%d-%m-%Y %H:%M:%S")))
    fileLog = open('log.txt', 'a+')
    fileJSONData = open('log.json', "w+")

    print(f"Host:\t\t\t{socket.gethostbyname(socket.gethostname())}\n")
    listStats = driver.find_elements(By.XPATH, "//div[@class='html5-video-info-panel']/div/div[not(@style='display: none;')]/span")
    resolution = listStats[2].text
    resolutionModified = re.findall(r'[0-9]+@', resolution)[0]
    speed = listStats[5].find_element(By.XPATH, "./span[2]").text
    network = listStats[6].find_element(By.XPATH, "./span[2]").text
    buffer = listStats[7].find_element(By.XPATH, "./span[2]").text
    latency = listStats[8].find_element(By.XPATH, "./span[2]").text
    date = listStats[11].text
    print(f"Resolution:\t\t{resolution}\nResolutionModified:\t{resolutionModified}\nSpeed:\t\t\t{speed}\nNetwork Activity:\t{network}\nBuffer:\t\t\t{buffer}\nLive Latency:\t\t{latency}\nFecha:\t\t\t{date}\n")

    #pr = f"Speed:\t\t\t{speed}\nNetwork Activity:\t{network}\nBuffer:\t\t\t{buffer}\nLive Latency:\t\t{latency}\n"
    #print(pr)
    #print(f"{UP}Speed:\t\t\t{speed}{CLEAR}\n{UP}Network Activity:\t{network}{CLEAR}\n{UP}Buffer:\t\t\t{buffer}{CLEAR}\n{UP}Live Latency:\t\t{latency}{CLEAR}\n")

    # st = speedtest.Speedtest()
    # download_speed = st.download()
    # upload_speed = st.upload()

    # print('Download Speed: {:5.2f} Mb'.format(download_speed/(1024*1024)))
    # print('Upload Speed: {:5.2f} Mb'.format(upload_speed/(1024*1024)))

    fileLog.write(myTime+" "+socket.gethostbyname(socket.gethostname())+" "+resolution+" "+speed+" "+network+" "+buffer +" "+latency +' {:5.2f} '.format(0/(1024*1024))+'{:5.2f}' .format(0/(1024*1024))+" "+resolutionModified+"\n")
    fileLog.close()

    arrayJSON = [
        {'Fecha':myTime,
        'Host':socket.gethostbyname(socket.gethostname()),
        'Resolution':resolutionModified,
        'Speed':speed,
        'Network Activity':network,
        'Buffer':buffer,
        'Latency':latency,
        'Download SpeedTest':' {:5.2f} '.format(0/(1024*1024)),
        'Upload SpeedTest':'{:5.2f}' .format(0/(1024*1024))}
    ]

    # fileJSONSize = len(fileJSONData.read())
    # fileJSONData = open('log.json', "r")

    # if fileJSONSize > 0:
    #     dataJSON = json.load(fileJSONData)
    # else:
    #     dataJSON = ""

    # arrayJSON = dataJSON["prtg"]["result"] + arrayJSON

# CHANGE QUALITY IF IT IS BELOW 2160P
    if resolutionModified == "2160@":
        print("")
    else:
        setQuality()

    jsonString = json.dumps(arrayJSON)
    # fileJSON = open('log.json', 'w')
    fileJSONData.write('{"prtg": { "result": '+jsonString+"}}\n")

    time.sleep(30)