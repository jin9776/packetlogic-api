#!/usr/bin/env python

import sys
import packetlogic2

try:
    pl = packetlogic2.connect("192.168.2.30", "admin", "pldemo00")
except:
    t, v, tb = sys.exc_info()
    print("Error: Couldn't connect: %s" % v)
    sys.exit(1)

rt = pl.Realtime()

count = 1

def f(data):
    print ("#%d subscribers active under" % (len(data)))
    for no in data:
        inspd = no.speed[0]*8.0/1000
        outspd = no.speed[1]*8.0/1000
        print ("%-40s %8.2f %8.2f" % (no.fullpath, inspd, outspd))

#rt.add_netobj_callback(f, under="/NetObjects/<Ungrouped>", include_hosts=True)
#rt.add_netobj_callback(f, under="/NetObjects/office")
rt.update_forever()