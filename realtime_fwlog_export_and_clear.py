#!/usr/bin/env python

""" 
Script to export all data in the firewall log.

NOTE! This script CLEARS the firwall log!

Example:
fwlog_export_and_clear.py 192.168.1.25 admin pldemo00

Output:
Exporting 2 entries
============================================================
192.168.1.60   217.73.97.18    80      6       HTTP    www.netintact.se
192.168.1.70   217.73.97.18    80      6       HTTP    www.netintact.se

"""

__version__ = "0.1 2008-11-14 Procera Networks"

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

import sys
import packetlogic2

try:
    [host, user, pwd] = sys.argv[1:]
except ValueError:
    print ("Usage: fwlog_export_and_clear.py plhost pluser plpass")
    print ("Example: fwlog_export_and_clear.py 192.168.1.25 admin pldemo00")
    sys.exit(1)

try:
    pl = packetlogic2.connect(host, user, pwd)
except:
    t, v, tb = sys.exc_info()
    print ("Error: Couldn't connect: %s" % v)
    sys.exit(1)

r = pl.Realtime()

# Get all!
entries = []
numentries = r.fwlog_query_offsets(0, 0)[0]['logentries']
for x in range(0, numentries, 500):
    entries += r.fwlog_query_offsets(x, min(x+500, numentries), no_reverse=True)[1]
# Grab the last set of entries that arrived during query and clear the log
entries += r.fwlog_query_offsets(numentries, -1, clear=True, no_reverse=True)[1]

# Output format
format = "%(client)s\t%(server)s\t%(serverport)s\t%(protocol)s\t%(service)s\t%(serverhostname)s\n"

print ("Exporting %d entries" % len(entries))
print ("=" * 78)
for entry in entries:
    print format % entry,