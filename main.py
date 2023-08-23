import requests
from bs4 import BeautifulSoup
import os
import time

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
         'Cookies':'guest_id=3623607; z_theme=11; PHPSESSID=ujrsgo8kv3eaf80vbaa3c7fvc8; _lr_env_src_ats=false; _lr_geo_location=JP; __qca=P0-1280843412-1692757365343; __gads=ID=d0509afee94dcc52-22aff0d004e3000c:T=1692601495:RT=1692773342:S=ALNI_Mbm3mNRWLQdUNUwH66IYqaWfFAP_Q; __gpi=UID=00000c3037ee3385:T=1692601495:RT=1692773342:S=ALNI_MZM91cjjCIp4L6jhiz6D3sDBdutlA; FCNEC=%5B%5B%22AKsRol_SZaHxx294boMd9Oi5y8lV52fUug0jGeTt8e1_14xNFEYln9jBpvgK6lJfjjxqDUl0Lhk8MFc02f5vLJ_bA2lOuCoWgjhXs8WwkU5mPbpreZ6L_nSuLVrCqKJfm-gBzzwzPcrd7UIUcQeuiWvwJrP7g9Dkkg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; _lr_retry_request=true; properSessionStorage=eyJ1dWlkIjoiMjA2ODc5NDgtODYyYy00OTQxLWEwYTgtNGNmNWQ0NTA1MDdjIiwiZGVwdGgiOjEsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuemVyb2NoYW4ubmV0L1NlcmVuYSslMjhQb2slQzMlQTltb24lMjk%2FcT0lRTMlODIlQkIlRTMlODMlQUMlRTMlODMlOEEmcD0yIiwiZ2NsaWQiOiIiLCJmYmNsaWQiOiIiLCJ1dG1fY2FtcGFpZ24iOiIiLCJ1dG1fc291cmNlIjoiIiwidXRtX21lZGl1bSI6IiIsInV0bV90ZXJtIjoiIiwidXRtX2NvbnRlbnQiOiIiLCJ1dG1fdGVtcGxhdGUiOiIiLCJ1dG1fcmVmZXJyZXIiOiIiLCJ1dG1fYWRzZXQiOiIiLCJ1dG1fc3ViaWQiOiIiLCJyZXZlbnVlIjowLCJiaWRfYXZnIjp7fSwibm9fYmlkX2NudCI6e30sImF1Y3Rpb25fY291bnQiOjEsImxhc3RfdGhyZXNob2xkIjowfQ%3D%3D',}

def open_page(url):
    html=requests.get(url,headers=headers)
    time.sleep(2)
    html=html.text
    return html

def get_urls(html,selector,class_):
    soup=BeautifulSoup(html,'lxml')
    content=soup.find_all(selector,class_=class_)
    contents=content[0].find_all('li',class_="")
    urls=[]
    for i in range(len(contents)):
        url_index=contents[i].find_all('a')
        if(len(url_index)==3):
            url=url_index[2]['href']
            urls.append(url)
    return urls

def save_picture(path,file_name,image_url):
    response = requests.get(image_url)
    image_data = response.content
    if os.path.exists(path):
        file = os.path.join(path, f"{file_name + '.png'}")
        with open(file, 'wb') as f:
            f.write(image_data)
            print(f"{'*' * 5}开始图库{'Serena'}的  {file_name}  爬取{'*' * 5}")
    else:
        os.mkdir(path)
        file = os.path.join(path, f"{file_name + '.png'}")
        with open(file, 'wb') as f:
            f.write(image_data)
            print(f"{'*' * 5}开始图库{'Serena'}的  {file_name}  爬取{'*' * 5}")

if __name__=='__main__':
    path=os.path.join(f"./{'Serena'}")
    for j in range(58):
        main_url='https://www.zerochan.net/Serena+%28Pok%C3%A9mon%29?q=%E3%82%BB%E3%83%AC%E3%83%8A&p='+str(j+1)
        main_html=open_page(main_url)
        image_urls=get_urls(main_html,'ul',"small-thumbs")
        for i in range(len(image_urls)):
            image_url=image_urls[i]
            save_picture(path,str(str(j+1)+"页图片"+str(i+1)),image_url)
    print("读取完成")


