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


vb = rt.get_view_builder();
path = "/"

#print(vb.available_fields)
print(vb.available_filters)

def display_netobject_data(root):
    print("%s" % ("=" * 60))
    #print(root)
    for child in root.children:
        print("%s" % ("=" * 60))
        print("%s/%s/%s" % (path, child.name, child.rawname))
        print("     speed (bps) in/out: %8d %8d" % (child.speed[0] * 8, child.speed[1] * 8))
        print("             cps in/out: %8d %8d" % child.cps)
        print("            connections: %8d" % child.connections)
        print(child.external_quality)
        print(child.internal_quality)
        print(child.rtt)
        
        for sub in child.children:
            print("%s/%s/%s" % (path, sub.name, sub.rawname))
            print("     speed (bps) in/out: %8d %8d" % (sub.speed[0] * 8, sub.speed[1] * 8))
            print("             cps in/out: %8d %8d" % sub.cps)
            print("            connections: %8d" % sub.connections)
            print(sub.external_quality)
            print(sub.internal_quality)
            print(sub.rtt)
            print(sub.children)
        print
        print("%s" % ("=" * 60))
    print

#
# Build a view
#

#vb.filter('Visible NetObject', path)
#vb.distribution('NetObject Level', path)
vb.distribution("Local Host")
vb.distribution("Service")
rt.add_aggr_view_callback(vb, display_netobject_data)
rt.update_forever()