#!/usr/bin/env python

import sys
import packetlogic2
import time

try:
    pl = packetlogic2.connect("192.168.2.30", "admin", "pldemo00")
except:
    t, v, tb = sys.exc_info()
    print("Error: Couldn't connect: %s" % v)
    sys.exit(1)

rt = pl.Realtime()

# return RealtimeNetObjectTree
data = rt.get_netobj_data("/");

print ("#%d subscribers active under" % (len(data)))
print ("%s" % (data))

for no in data:
    inspd = no.speed[0]*8.0
    outspd = no.speed[1]*8.0
    print ("%-40s in=%8.2f out=%8.2f " % (no.fullpath, inspd, outspd))
    print("              cps in/out: %8d  %8d" % (no.cps))
    print("connections totsl /unest: %8d  %8d" % (no.connections))
    print
