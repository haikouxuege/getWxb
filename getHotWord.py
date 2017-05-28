#encoding=utf-8
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_hot_word(wxid):
    url = 'http://data.wxb.com/account/content/' + str(wxid)
    headers = {
                'Cookie':'PHPSESSID=sb6r7llps17vle9kb958hra5m1; visit-wxb-id=6b03f4becf1c0dfea59ee3b60f5d3864; wxb_fp_id=666802310',
                'Host':'data.wxb.com', 
                'Referer':'http://data.wxb.com/details/contentAnalyse?id=gh_ab1ffb2c3464',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest',
                }
    html = requests.get(url, headers=headers)

    return json.loads(html.text)['data']['hot_words']

def main():
    for each in get_hot_word('gh_ab1ffb2c3464'):
        print(each)


if __name__ == '__main__':
    main()
