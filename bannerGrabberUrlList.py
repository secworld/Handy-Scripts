import sys,socket,httplib

with open('C:\Users\iblfm1180\Desktop\urllist.txt', 'r') as f:
    for ip in f:
            host = ip.rstrip('\n')
            httpurl = str(host)+str(":80")
            httpsurl = str(host)+str(":443")
            try:
                try:
                    print httpurl
                    c = httplib.HTTPConnection(httpurl,timeout=10)
                    c.request ("GET", "/")
                    r2 = c.getresponse()
                    print r2.status
                    r1 = r2.getheaders()
                    WebServer = r2.getheader("server")
                    ContentType = r2.getheader("content-type")
                    d2 = r2.read()
                    print "\n\nBanner :"
                    print "Banner Fields :",r1
                    print "\n\nWebServer Name :",WebServer
                    print "Content Type :",ContentType
                    print "\n\nResponse is : "
                    print d2
                    print "\n\n"
                except:
                    print httpsurl
                    c = httplib.HTTPConnection(httpsurl,timeout=10)
                    c.request ("GET", "/")
                    r2 = c.getresponse()
                    print r2.status
                    r1 = r2.getheaders()
                    WebServer = r2.getheader("server")
                    ContentType = r2.getheader("content-type")
                    d2 = r2.read()
                    print "\n\nBanner :"
                    print "Banner Fields :",r1
                    print "\n\nWebServer Name :",WebServer
                    print "Content Type :",ContentType
                    print "\n\nResponse is : "
                    print d2
                    print "\n\n"
            except:
                print "Connection Timed out !!!\nTrying next ..."
                continue





            
