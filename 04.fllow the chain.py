from urllib import request
import re
num=8022
for i in range(300):
    u = request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'% num)
    text = u.read().decode('utf8')
    try:
        num = re.search('and the next nothing is ([0-9]*)',text).group(1)
    except:
        print(text)
        break
    print(num)