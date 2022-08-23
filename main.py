# from videoyoutube import youtubeStatistics
import videoyoutube
import time

while True:
    myTime = str(time.strftime(("%d-%m-%Y %H:%M:%S")))
    file = open('log.txt', 'wb')
    file = open('log.txt', 'a+')
    
    # def youtubeLog(youtubeStatistics,printConsole):
    #     youtubeStatistics()

    # def speedTest(metricUpload,metricDownload):
    #     metricDownload()
    #     metricUpload()

    file.write(myTime+youtubeStatistics+"\n")


    closeFile = file.close()