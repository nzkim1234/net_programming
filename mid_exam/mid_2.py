url = 'https://search.daum.net/search?w=tot&q=bigdata'
splitted_url = url.split('?')[1].split('&')
dic = {}
for sp_url in splitted_url:
    key, value = sp_url.split('=')
    dic[key] = value

print(dic)
dic['q'] = 'iot'
print(dic)