#!/usr/bin/env python

import sys
import packetlogic2

try:
    pl = packetlogic2.connect("192.168.2.30", "admin", "pldemo00")
except:
    t, v, tb = sys.exc_info()
    print("Error: Couldn't connect: %s" % v)
    sys.exit(1)

rt = pl.Realtime();

# return RealtimeNetObjectTree
data = rt.get_services_data();

print ("#%d subscribers active under" % (len(data)))
print ("%s" % (data))
print(dir(data))

for no in data:
    print(no)
    inspd = data.get(no).get("speed_in") * 8.0
    outspd = data.get(no).get("speed_out") * 8.0
    print("     speed (bps) in/out: %8d  %8d" % (inspd, outspd))
    print("             cps in/out: %8d  %8d" % (data.get(no).get("cps") ))
    print("            connections: %8d" % (data.get(no).get("connections")))
    print
