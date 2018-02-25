import urllib2
def main():
    request = urllib2.Request("http://www.baidu.com")
    response = urllib2.urlopen(request)
    print response.read()

if __name__ == '__main__':
    main()
