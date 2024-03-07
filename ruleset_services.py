#!/usr/bin/env python

import sys
import packetlogic2

try:
    pl = packetlogic2.connect("192.168.2.30", "admin", "pldemo00")
except:
    t, v, tb = sys.exc_info()
    print("Error: Couldn't connect: %s" % v)
    sys.exit(1)

r = pl.Ruleset()

print("service %s" % (("=" * 60)))
list = r.services_list()
for data in list:
    print("%s   " % (data))