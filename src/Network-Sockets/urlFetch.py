#!/usr/bin/

import urllib2

def main():
    # open a connections
    webUrl = urllib2.urlopen("http://digitalldesk.com")

    # get the result and print it out
    print "result of code:" + str(webUrl.getcode())

    # print url data
    data = webUrl.read()
    print data




if __name__ == "__main__":
    main()
