import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site ardeu')
else:
    print('Pode ir tá tudo nice')
