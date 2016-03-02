import sys,socket,httplib

ipList = raw_input("Enter the full path of the IP list file : ")
with open(ipList, 'r') as f:
    for ip in f:
            host = ip.rstrip('\n')
            httpurl = str(host)+str(":80")
            httpsurl = str(host)+str(":443")
            try:
                try:
                    print httpurl
                    c = httplib.HTTPConnection(httpurl,timeout=2)
                    c.request ("GET", "/")
                    r2 = c.getresponse()
                    print "Response code : ",r2.status
                    r1 = dict(r2.getheaders())
                    WebServer = r2.getheader("server")
                    ContentType = r2.getheader("content-type")
                    d2 = r2.read()
                    print "Banner Fields :",r1
                    print "\n\nWebServer Name :",WebServer
                    print "Content Type :",ContentType
                    #print "\n\nResponse is : "
                    #print d2
                    print "\n\n"
                except:
                    print httpsurl
                    c = httplib.HTTPConnection(httpsurl,timeout=2)
                    c.request ("GET", "/")
                    r2 = c.getresponse()
                    print "Response code : ",r2.status
                    r1 = dict(r2.getheaders())
                    WebServer = r2.getheader("server")
                    ContentType = r2.getheader("content-type")
                    d2 = r2.read()
                    print "Banner Fields :",r1
                    print "\n\nWebServer Name :",WebServer
                    print "Content Type :",ContentType
                    #print "\n\nResponse is : "
                    #print d2
                    print "\n\n"
            except:
                print "Connection Timed out !!!\nTrying next ...\n"
                continue





            
