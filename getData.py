#encoding=utf-8
import requests 
from bs4 import BeautifulSoup
import sys
import json
reload(sys)   
sys.setdefaultencoding('utf8')

def url_open(wxid):
    url = 'http://data.wxb.com/details/postRead?id=' + str(wxid)
    headers = {
                'Accept':'application/json',
                'Cookie':'PHPSESSID=qbq9lvqsrrlr7lkua19p5l2pe1; visit-wxb-id=6b03f4becf1c0dfea59ee3b60f5d3864; wxb_fp_id=666802310',
                'Host':'data.wxb.com', 
                'Referer':'http://data.wxb.com/rank?category=-1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            }
    html = requests.get(url, headers=headers)

    return html 

def get_data(wxid):
    html = url_open(wxid)
    soup = BeautifulSoup(html.text, 'lxml')
    script = soup.find_all('script')
    start = script[0].get_text().find('{"app"')
    data = script[0].get_text()[start:]
    data = json.loads(data)
    '''
    print(data['details']['detailOverview']['overviewData']['name'])
    print(data['details']['detailOverview']['overviewData']['index_scores'])
    '''
    articles = data['details']['postRead']['articleData']['articles']
    details = []
    details.append('公众号：'+data['details']['detailOverview']['overviewData']['name'])
    for article in articles:
        details.append('标题：'+article['title'])
        details.append('平均阅读：'+str(article['read_num']))
        details.append('点赞：'+str(article['like_num']))

    return details
        
if __name__ == '__main__':
    get_data()

