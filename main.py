from plyer import notification
import requests
from bs4 import BeautifulSoup

def send_notification(title, message):
    notification.notify(
        title = title,
        message=message,
        app_icon="virus.ico",
        timeout=5

    )

def getdatafromsite(url):
    r= requests.get(url)
    return r.text
def getstatesinput():
    #temp=[item for item in input().split()]
    temp= ["Uttarakhand", "Uttar Pradesh"]
    return temp


if __name__ == '__main__':

    htmldata= getdatafromsite('https://www.mohfw.gov.in/')
    soup = BeautifulSoup( htmldata , 'html.parser')
    datastr= ""
    for tr in soup.find_all('tbody'):
        datastr+=tr.get_text()
    datastr= datastr[1:]
    data = datastr.split('\n\n')
    states= getstatesinput()
    r=0 #range for current number of states in table

    for i in data:
        if i.split('\n')[1:]:
            currlist = i.split('\n')[1:]
            print(currlist)
            if currlist[1] in states:
                print(currlist)
                title= " Cases of Covid-19 "
                message= f" State : { currlist[1]} \nIndian : {currlist[2]} Foreign : {currlist[3]} \nCured: {currlist[4]}\n Deaths: {currlist[5]}"
                send_notification(title , message)

