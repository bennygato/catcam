'''
checkout http://blog.csdn.net/bennygato/article/details/51582715 for 
more instructions
'''
#encoding=utf-8
 
import time
from weibo import APIClient

def get_access_token(app_key, app_secret, callback_url):
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    # 获取授权页面网址
    auth_url = client.get_authorize_url()
    print auth_url
    
    # 在浏览器中访问这个URL，会跳转到回调地址，回调地址后面跟着code，输入code
    code = raw_input("Input code:")
    r = client.request_access_token(code)
    access_token = r.access_token
    # token过期的UNIX时间
    expires_in = r.expires_in
    print 'access_token:',access_token
    print 'expires_in:', expires_in

    return access_token, expires_in

if __name__ == '__main__':
    app_key = 'xxxxxxx'
    app_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    callback_url = 'https://api.weibo.com/oauth2/default.html'

    access_token, expires_in = get_access_token(app_key, app_secret, callback_url)
    # 上面的语句运行一次后，可保存得到的access token，不必每次都申请
    # access_token = 'xxxxx'
    # expires_in = 'xxxxx'

    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    client.set_access_token(access_token, expires_in)
	
    idx = 1
    default_msg_part_1 = 'This is no.'
    default_msg_part_2 = ' msg sent automatically from benny"s robot HAHAHA'
 
    # send a weibo with img
    f = open('test.jpg', 'rb')
    r = client.statuses.upload.post(status=u'test: weibo with an img. -benny', pic=f)
    f.close() # APIClient不会自动关闭文件，需要手动关闭

    # send text weibo every 200sec
    while True:
        line = default_msg_part_1 + str(idx) + default_msg_part_2
	utext = unicode(line,"UTF-8") 
        client.post.statuses__update(status=utext) 
	idx = idx + 1
        time.sleep(200)    

