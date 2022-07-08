#
# PySNMP MIB module ARRIS-C3-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-NTP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:07 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, IpAddress, Counter32, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "IpAddress", "Counter32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Unsigned32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
cmtsC3NTPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7))
if mibBuilder.loadTexts: cmtsC3NTPMIB.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: cmtsC3NTPMIB.setOrganization('Arris International')
if mibBuilder.loadTexts: cmtsC3NTPMIB.setContactInfo('   Network Management\n                Postal: Arris International.\n                        4400 Cork Airport Business Park\n                        Cork Airport, Kinsale Road\n                        Cork, Ireland.\n                Tel:    +353 21 7305 800\n                Fax:    +353 21 4321 972')
if mibBuilder.loadTexts: cmtsC3NTPMIB.setDescription('This MIB manages the NTP software on the Arris CMTS C3')
dcxNTPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1))
dcxNTPServerTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1), )
if mibBuilder.loadTexts: dcxNTPServerTable.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerTable.setDescription('This table contains a list of the NTP servers that the CMTS is\n        configured to use.  If the table is empty, then no NTP servers\n        are specified, and the time will be read from the on-board RTC\n        (Real Time Clock).  Each NTP server in this table will be queried,\n        but only the master NTP server will be used to update the system\n        time.')
dcxNTPServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1), ).setIndexNames((0, "ARRIS-C3-NTP-MIB", "dcxNTPServerIp"))
if mibBuilder.loadTexts: dcxNTPServerEntry.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerEntry.setDescription('An entry describing an NTP server.  Entries are ordered by dcxNTPServerIndex.')
dcxNTPServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: dcxNTPServerIp.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerIp.setDescription("The IP address to which this entry's addressing information pertains.")
dcxNTPServerInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 2), Integer32().clone(300)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxNTPServerInterval.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerInterval.setDescription('The interval for which the CMTS will wait before trying to connect to the NTP server (in seconds).')
dcxNTPServerSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxNTPServerSuccess.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerSuccess.setDescription('The number of times the NTP server has been successfully polled.')
dcxNTPServerAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxNTPServerAttempts.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerAttempts.setDescription('The number of times the NTP server has been polled.')
dcxNTPServerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxNTPServerOffset.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerOffset.setDescription('The offset (in seconds) from which the NTP server differs from the CMTS.')
dcxNTPServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxNTPServerStatus.setStatus('current')
if mibBuilder.loadTexts: dcxNTPServerStatus.setDescription('Controls and reflects the status of rows in this table.  Rows in this table may be created by either the create-and-go or create-and-wait paradigms.  There is no restriction on changing values in a row of this table while the row is active.')
dcxNTPMasterServer = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxNTPMasterServer.setStatus('current')
if mibBuilder.loadTexts: dcxNTPMasterServer.setDescription('This value contains the IP of the current master NTP server as specified in dcxNTPServerTable.  An IP address of 0.0.0.0 will be displayed if the NTP master server is not in the list, or not configured.')
mibBuilder.exportSymbols("ARRIS-C3-NTP-MIB", dcxNTPServerEntry=dcxNTPServerEntry, dcxNTPServerTable=dcxNTPServerTable, dcxNTPObjects=dcxNTPObjects, dcxNTPServerAttempts=dcxNTPServerAttempts, cmtsC3NTPMIB=cmtsC3NTPMIB, PYSNMP_MODULE_ID=cmtsC3NTPMIB, dcxNTPMasterServer=dcxNTPMasterServer, dcxNTPServerInterval=dcxNTPServerInterval, dcxNTPServerSuccess=dcxNTPServerSuccess, dcxNTPServerOffset=dcxNTPServerOffset, dcxNTPServerStatus=dcxNTPServerStatus, dcxNTPServerIp=dcxNTPServerIp)
