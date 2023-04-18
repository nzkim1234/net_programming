url = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'
splitted_url = url.split('?')[1].split('&')
dic = {}

for i in splitted_url:
    key, value = i.split('=')
    dic[key] = value

print(dic)