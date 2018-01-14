import requests

def get_out_ip():
    url = r'http://1212.ip138.com/ic.asp'
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip)
    return ip

get_out_ip()
