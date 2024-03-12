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
        print("%s Localhost %s" % ("=" * 30, "=" * 30))
        print("%s/%s/%s" % (path, child.name, child.rawname))
        print("     speed (bps) in/out: %8d %8d" % (child.speed[0] * 8, child.speed[1] * 8))
        print("             cps in/out: %8d %8d" % child.cps)
        print("            connections: %8d" % child.connections)
        if child.external_quality is not None:
            print("external quality in/out: %8d %8d" % child.external_quality)
        if child.internal_quality is not None:
            print("internal quality in/out: %8d %8d" % child.internal_quality)
        if child.rtt is not None:
            print("                    rtt: %8d %8d" % child.rtt)


        print(child.rtt)
        
        for sub in child.children:
            print("%s/%s/%s" % (path, sub.name, sub.rawname))
            print("     speed (bps) in/out: %8d %8d" % (sub.speed[0] * 8, sub.speed[1] * 8))
            print("             cps in/out: %8d %8d" % sub.cps)
            print("            connections: %8d" % sub.connections)
            if sub.external_quality is not None:
                print("external quality in/out: %8d %8d" % sub.external_quality)
            if sub.internal_quality is not None:
                print("internal quality in/out: %8d %8d" % sub.internal_quality)
            if sub.rtt is not None:
                print("                    rtt: %8d %8d" % sub.rtt)
            if sub.children is not None:
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