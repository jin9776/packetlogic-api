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
path = "office"


def display_netobject_data(root):
    print("%s" % ("=" * 60))
    for child in root.children:
        print("%s/%s" % (path, child.name))
        print("     speed (bps) in/out: %8d %8d" % (child.speed[0] * 8, child.speed[1] * 8))
        print("             cps in/out: %8d %8d" % child.cps)
        print("            connections: %8d" % child.connections)
    print

#
# Build a view
#

vb.filter('Visible NetObject', path)
vb.distribution('NetObject Level', path)
rt.add_aggr_view_callback(vb, display_netobject_data)