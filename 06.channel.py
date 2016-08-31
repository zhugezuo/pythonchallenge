import re,zipfile

z =zipfile.ZipFile('channel.zip', 'r')
num = 90052
c = z.getinfo('%s.txt' % num).comment.decode('utf8')
print(c, end='')
for i in range(1000):
    text = z.read('%s.txt' % num).decode('utf8')
    try:
        num = re.search('Next nothing is ([0-9]*)',text).group(1)
    except:
        break
    c=z.getinfo('%s.txt' % num).comment.decode('utf8')
    print(c, end='')

z.close()

