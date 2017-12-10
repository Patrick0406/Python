#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import ConfigParser

def create_session():
    cf = ConfigParser.ConfigParser()
    cf.read('config.ini')
    cookies = cf.items('cookies')
    cookies = dict(cookies)
    from pprint import pprint
    pprint(cookies)
    email = cf.get('info','email')
    password = cf.get('info', 'password')

    session = requests.session()
    login_data = {'email' : email, 'password' : password}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
        'Host': 'www.zhihu.com',
        'Referer': 'http://www.zhihu.com/'
    }
    r = session.post('http://www.zhihu.com/login/email', data=login_data, headers=header)

    if r.json()['r'] == 1:
        print 'Login Failed, reason is:',
        for m in r.json()['data']:
             print r.json()['data'][m]
        print 'So we use cookies to login in...'
        has_cookies = False
        for key in cookies:
            if key != '__name__' and cookies[key] != '':
                has_cookies = True
                break
        if has_cookies is False:
            raise  ValueError('请填写config.ini文件中的cookies项.')
        else:
            r = session.get('http://www.zhihu.com/login/email', cookies=cookies)

    with open('login.html','w') as fp:
        fp.write(r.content)

    return session, cookies


if __name__ == '__main__':
    requests_session, requests_cookies = create_session()

    url = 'http://www.zhihu.com/topic/19552832'
    content = requests_session.get(url, cookies=requests_cookies).content
    with open('url.html', 'w') as fp:
        fp.write(content)

