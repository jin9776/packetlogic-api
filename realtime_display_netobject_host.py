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



def display_netobject_data(root):
    print(time.ctime())
    #print(root)
    for child in root:        
         print(child.fullpath)
         if (hasattr(child, 'parent')):
            print(child.parent)
         print("     speed (bps) in/out: %8d %8d" % (child.speed[0] * 8, child.speed[1] * 8))
         print("             cps in/out: %8d %8d" % child.cps)
         print("      connection total/unest: %8d %8d" % child.connections)        
    #print

rt.add_netobj_callback(display_netobject_data, "/", include_hosts=True)
rt.update_forever(10)