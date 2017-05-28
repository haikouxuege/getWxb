#encoding=utf-8
import requests
import json
import sys
import time
import getData
import getHotWord
reload(sys)   
sys.setdefaultencoding('utf8')

def url_open(page):
    url = 'http://data.wxb.com/rank/day/2017-05-26/-1?sort=index_scores+desc&page=' + str(page) + '&page_size=20'

    headers = {
            'Cookie':'PHPSESSID=qbq9lvqsrrlr7lkua19p5l2pe1; visit-wxb-id=6b03f4becf1c0dfea59ee3b60f5d3864; wxb_fp_id=666802310',
            'Host':'data.wxb.com', 
            'Referer':'http://data.wxb.com/rank?category=-1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
            }

    html = requests.get(url, headers=headers)

    return json.loads(html.text)['data']

def get_value():
    values_list = []
    #设置页数
    pages = 50
    count = 0
    for i in range(pages):
        for each in url_open(i+1):
            count += 1
            values_list.append(each['wx_origin_id'])
            '''
            print(each['name'])
            print('平均阅读：{0}'.format(each['avg_read_num']))
            print(each['wx_origin_id'])
            '''
        print('now:{0}'.format(count))
    #print(values_list)

    return values_list

def main():
    try:
        for wxid in get_value():
            with open('wxb.txt','a+') as f:
                f.write('-----------------------------------------------------------------------------------------------------------'+'\r\n')
            print('---------------------------------------------------------------------------------------------------------------------')
            for article in getData.get_data(wxid):
                print(article)
                with open('wxb.txt','a+') as f:
                    f.write(article+'\r\n')
            for word in getHotWord.get_hot_word(wxid):
                print(word)
                with open('wxb.txt','a+') as f:
                    f.write(word+'\r\n')
    except:
        print('error')
        time.sleep(10)


if __name__ == '__main__':
    main()
