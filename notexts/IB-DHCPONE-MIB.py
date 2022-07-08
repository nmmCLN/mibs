#
# PySNMP MIB module IB-DHCPONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DHCPONE-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:22:44 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
IbString, IbIpAddr, ibDHCPOne = mibBuilder.importSymbols("IB-SMI-MIB", "IbString", "IbIpAddr", "ibDHCPOne")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, IpAddress, MibIdentifier, enterprises, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Unsigned32, iso, Integer32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "MibIdentifier", "enterprises", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Unsigned32", "iso", "Integer32", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDhcpModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1))
ibDhcpModule.setRevisions(('2010-03-23 00:00', '2008-02-14 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))
if mibBuilder.loadTexts: ibDhcpModule.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: ibDhcpModule.setOrganization('Infoblox')
ibDHCPSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1), )
if mibBuilder.loadTexts: ibDHCPSubnetTable.setStatus('current')
ibDHCPSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1), ).setIndexNames((0, "IB-DHCPONE-MIB", "ibDHCPSubnetNetworkAddress"))
if mibBuilder.loadTexts: ibDHCPSubnetEntry.setStatus('current')
ibDHCPSubnetNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 1), IbIpAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetNetworkAddress.setStatus('current')
ibDHCPSubnetNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 2), IbIpAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetNetworkMask.setStatus('current')
ibDHCPSubnetPercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetPercentUsed.setStatus('current')
ibDHCPStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3))
ibDhcpTotalNoOfDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfDiscovers.setStatus('current')
ibDhcpTotalNoOfRequests = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfRequests.setStatus('current')
ibDhcpTotalNoOfReleases = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfReleases.setStatus('current')
ibDhcpTotalNoOfOffers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfOffers.setStatus('current')
ibDhcpTotalNoOfAcks = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfAcks.setStatus('current')
ibDhcpTotalNoOfNacks = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfNacks.setStatus('current')
ibDhcpTotalNoOfDeclines = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfDeclines.setStatus('current')
ibDhcpTotalNoOfInforms = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfInforms.setStatus('current')
ibDhcpTotalNoOfOthers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfOthers.setStatus('current')
ibDhcpDeferredQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpDeferredQueueSize.setStatus('current')
ibDHCPDDNSStats = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5))
ibDHCPDDNSAvgLatency5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency5.setStatus('current')
ibDHCPDDNSAvgLatency15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency15.setStatus('current')
ibDHCPDDNSAvgLatency60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency60.setStatus('current')
ibDHCPDDNSAvgLatency1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency1440.setStatus('current')
ibDHCPDDNSTimeoutCount5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount5.setStatus('current')
ibDHCPDDNSTimeoutCount15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount15.setStatus('current')
ibDHCPDDNSTimeoutCount60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount60.setStatus('current')
ibDHCPDDNSTimeoutCount1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount1440.setStatus('current')
mibBuilder.exportSymbols("IB-DHCPONE-MIB", ibDhcpTotalNoOfRequests=ibDhcpTotalNoOfRequests, ibDhcpTotalNoOfInforms=ibDhcpTotalNoOfInforms, ibDhcpDeferredQueueSize=ibDhcpDeferredQueueSize, ibDHCPDDNSTimeoutCount60=ibDHCPDDNSTimeoutCount60, ibDHCPDDNSAvgLatency60=ibDHCPDDNSAvgLatency60, ibDhcpTotalNoOfOffers=ibDhcpTotalNoOfOffers, ibDHCPDDNSTimeoutCount15=ibDHCPDDNSTimeoutCount15, ibDhcpTotalNoOfOthers=ibDhcpTotalNoOfOthers, ibDHCPDDNSTimeoutCount1440=ibDHCPDDNSTimeoutCount1440, ibDHCPSubnetTable=ibDHCPSubnetTable, ibDHCPDDNSAvgLatency15=ibDHCPDDNSAvgLatency15, ibDhcpTotalNoOfAcks=ibDhcpTotalNoOfAcks, ibDHCPSubnetPercentUsed=ibDHCPSubnetPercentUsed, ibDHCPStatistics=ibDHCPStatistics, ibDhcpModule=ibDhcpModule, ibDHCPDDNSAvgLatency5=ibDHCPDDNSAvgLatency5, ibDHCPSubnetNetworkMask=ibDHCPSubnetNetworkMask, ibDhcpTotalNoOfReleases=ibDhcpTotalNoOfReleases, ibDHCPSubnetNetworkAddress=ibDHCPSubnetNetworkAddress, ibDhcpTotalNoOfDiscovers=ibDhcpTotalNoOfDiscovers, ibDHCPDDNSStats=ibDHCPDDNSStats, ibDhcpTotalNoOfNacks=ibDhcpTotalNoOfNacks, ibDHCPSubnetEntry=ibDHCPSubnetEntry, PYSNMP_MODULE_ID=ibDhcpModule, ibDhcpTotalNoOfDeclines=ibDhcpTotalNoOfDeclines, ibDHCPDDNSTimeoutCount5=ibDHCPDDNSTimeoutCount5, ibDHCPDDNSAvgLatency1440=ibDHCPDDNSAvgLatency1440)
