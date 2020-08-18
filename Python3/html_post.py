import requests

resp = requests.post("http://165.227.106.113/post.php", data={}, auth=('admin', '71urlkufpsdnlkadsf'))

print(resp)
