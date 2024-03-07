#!/usr/bin/env python
###############################################################################
#
#                          NO WARRANTY
#
#  BECAUSE THE PROGRAM IS PROVIDED FREE OF CHARGE, THERE IS NO WARRANTY
#  FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
#  OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
#  PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
#  OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
#  TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
#  PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
#  REPAIR OR CORRECTION.
#
#  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
#  WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
#  REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
#  INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
#  OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
#  TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
#  YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
#  PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGES.
#
###############################################################################

"""
Example script to build a view and display a summary of realtime netobject information under a specified path
"""

from __future__ import print_function
import sys
import time
import packetlogic2

#
# "parse" arguments.
#

try:
    [host, user, pwd, path] = sys.argv[1:]
except ValueError:
    print("Usage: realtime_display_netobject_data.py plhost pluser plpass netobjectpath")
    print("Example: realtime_display_netobject_data.py 192.168.1.25 admin pldemo00 PSM/RNC/100-34")
    sys.exit(1)

#
# Connect to PacketLogic system
#

try:
    pl = packetlogic2.connect(host, user, pwd)
except:
    t, v, tb = sys.exc_info()
    print("Error: Couldn't connect: %s" % v)
    sys.exit(1)

#
# Get Realtime resource
#

rt = pl.Realtime()

#
# Get View Builder
#

vb = rt.get_view_builder()

#
# Define callback function
#

def display_netobject_data(root):
    print("%s %s" % (time.ctime(), ("=" * 60)))
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
rt.update_forever()