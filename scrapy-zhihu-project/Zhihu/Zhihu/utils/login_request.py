# coding:utf8
__author__ = 'sxz'


import requests
import http.cookiejar as cookielib
import re

UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"
header = {
    "HOST":"www.zhihu.com",
    "Referer":"https://www.zhihu.com/",
    "User-Agent":UA
}
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未加载！")
def get_xsrf():
    response = session.get("https://www.zhihu.com",headers =header)
    # with open("zhihu.html","wb") as f:
    #     print(response.text)
    #     f.write(response.text.encode("utf-8")
    # req = re.compile('.*name="_xsrf" value="(.*?)"')
    # print(response.text)
    # s='<input type="hidden" name="_xsrf" value="57cbb0e2c65e9e6b13e1b834e3fbbda1"/>'
    xsrf = re.findall('.*name="_xsrf" value="(.*?)"',response.text)
    if xsrf:
        return xsrf[0]
    return ""


def get_captcha():
    import time
    t = str(int(time.time() * 1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t = session.get(captcha_url, headers=header)
    with open("captcha.jpg", "wb") as f:
        f.write(t.content)
        f.close()

    from PIL import Image
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass

    captcha = input("输入验证码\n>")
    return captcha

def zhihu_login(account,passwd):
    #知乎登录
    if re.match("^1\d{10}",account):
        print("手机号登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf":get_xsrf(),
            "phone_num":account,
            "password":passwd,
            "captcha": get_captcha()
        }

        response = session.post(post_url,data=post_data,headers=header)

        session.cookies.save()
def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf-8"))
    print ("ok")
def is_login():
    #通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/inbox"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True
if __name__=="__main__":
    # zhihu_login("****","****")
    # get_index()
    is_login()
