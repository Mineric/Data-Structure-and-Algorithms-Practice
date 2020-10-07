import urllib.request as ur
url = 'http://www.metro.tokyo.jp/index.html'
conn = ur.urlopen(url)
print(conn)
data = conn.read()

print(data) 

print(conn.getcode())

print(conn.getheader('Content-Type'))


for key, value in conn.getheaders():
    print(key, value)
