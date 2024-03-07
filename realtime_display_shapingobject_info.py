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
Example script to display a summary of shaping object realtime information
"""

import sys
import time
import packetlogic2

#
# Connect to PacketLogic system
#

try:
    pl = packetlogic2.connect("192.168.2.30", "admin", "pldemo00")
except:
    t, v, tb = sys.exc_info()
    print ("Error: Couldn't connect: %s" % v)
    sys.exit(1)

#
# Get Realtime resource
#

rt = pl.Realtime()


#
# Function called on new shapingobject data
#
# The following keys are available
# * connections
# * copies
# * name
# * in RX bps
# * out RX bps
# * in RX bytes
# * out RX bytes
# * in RX packets
# * out RX packets
# * in RX pps
# * out RX pps
# * in TX bps
# * out TX bps
# * in TX bytes
# * out TX bytes
# * in TX packets
# * out TX packets
# * in TX pps
# * out TX pps
# * in avg Q
# * out avg Q
# * in drops/s
# * out drops/s
# * in marks/s
# * out marks/s
# * in max Q
# * out max Q
# * in max latency
# * out max latency
# * in total drops
# * out total drops
# * in total marks
# * out total marks
def display_shapingobject_data(data):
    print ("%s %s" % (time.ctime(), ("=" * 60)))
    print ("%-30s %10s %10s" % ("name", "flows", "copies"))
    for _id, values in data.iteritems():
        print ("%(name)-30s %(connections)10d %(copies)10d" % values)
    print

#
# Setup callback for shaping object data and run
#

rt.add_shapingobject_callback(display_shapingobject_data)
rt.update_forever()
