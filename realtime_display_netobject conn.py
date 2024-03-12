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


def display_netobject_data(root):
    print("%s" % ("=" * 60))
    for child in root:
        print("service : %s" % child.base_service)
        print("client ip/port : %s/%s" % (child.client))
        print("engineflags : %s" % child.engineflags)
        print("External QoE in/out : %8d / %8d" % (child.external_quality))
        print("Internal QoE in/out : %8d / %8d" % (child.internal_quality))
        print("protocol num : %s" % child.protocol)
        print("server ip/port : %s/%s" % (child.server))
        print("server host : %s" % child.server_hostname)
        print("service : %s" % child.service)
        print("speed (bps) in/out: %8d %8d" % (child.speed[0] * 8, child.speed[1] * 8))
        print("starttime(UNIX) : %s" % child.starttime)
        print("matching rules : %s" % child.shaping_rules)
        
        print

#
# Build a view
#

#vb.filter('Visible NetObject', path)
rt.add_conn_view_callback(vb, display_netobject_data)
rt.update_forever()