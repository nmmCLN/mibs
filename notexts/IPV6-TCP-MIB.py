#
# PySNMP MIB module IPV6-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-TCP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
Ipv6Address, Ipv6IfIndexOrZero = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address", "Ipv6IfIndexOrZero")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, experimental, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "experimental", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipv6TcpMIB = ModuleIdentity((1, 3, 6, 1, 3, 86))
ipv6TcpMIB.setRevisions(('2017-02-22 00:00', '1998-01-29 00:00',))
if mibBuilder.loadTexts: ipv6TcpMIB.setLastUpdated('201702220000Z')
if mibBuilder.loadTexts: ipv6TcpMIB.setOrganization('IETF IPv6 MIB Working Group')
tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
ipv6TcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 16), )
if mibBuilder.loadTexts: ipv6TcpConnTable.setStatus('obsolete')
ipv6TcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 16, 1), ).setIndexNames((0, "IPV6-TCP-MIB", "ipv6TcpConnLocalAddress"), (0, "IPV6-TCP-MIB", "ipv6TcpConnLocalPort"), (0, "IPV6-TCP-MIB", "ipv6TcpConnRemAddress"), (0, "IPV6-TCP-MIB", "ipv6TcpConnRemPort"), (0, "IPV6-TCP-MIB", "ipv6TcpConnIfIndex"))
if mibBuilder.loadTexts: ipv6TcpConnEntry.setStatus('obsolete')
ipv6TcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6TcpConnLocalAddress.setStatus('obsolete')
ipv6TcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6TcpConnLocalPort.setStatus('obsolete')
ipv6TcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 3), Ipv6Address())
if mibBuilder.loadTexts: ipv6TcpConnRemAddress.setStatus('obsolete')
ipv6TcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6TcpConnRemPort.setStatus('obsolete')
ipv6TcpConnIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 5), Ipv6IfIndexOrZero())
if mibBuilder.loadTexts: ipv6TcpConnIfIndex.setStatus('obsolete')
ipv6TcpConnState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6TcpConnState.setStatus('obsolete')
ipv6TcpConformance = MibIdentifier((1, 3, 6, 1, 3, 86, 2))
ipv6TcpCompliances = MibIdentifier((1, 3, 6, 1, 3, 86, 2, 1))
ipv6TcpGroups = MibIdentifier((1, 3, 6, 1, 3, 86, 2, 2))
ipv6TcpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 86, 2, 1, 1)).setObjects(("IPV6-TCP-MIB", "ipv6TcpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6TcpCompliance = ipv6TcpCompliance.setStatus('obsolete')
ipv6TcpGroup = ObjectGroup((1, 3, 6, 1, 3, 86, 2, 2, 1)).setObjects(("IPV6-TCP-MIB", "ipv6TcpConnState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6TcpGroup = ipv6TcpGroup.setStatus('obsolete')
mibBuilder.exportSymbols("IPV6-TCP-MIB", ipv6TcpConnRemPort=ipv6TcpConnRemPort, ipv6TcpConnIfIndex=ipv6TcpConnIfIndex, ipv6TcpGroups=ipv6TcpGroups, ipv6TcpMIB=ipv6TcpMIB, ipv6TcpConnTable=ipv6TcpConnTable, tcp=tcp, ipv6TcpConnLocalAddress=ipv6TcpConnLocalAddress, ipv6TcpGroup=ipv6TcpGroup, ipv6TcpConnLocalPort=ipv6TcpConnLocalPort, ipv6TcpCompliance=ipv6TcpCompliance, ipv6TcpConnRemAddress=ipv6TcpConnRemAddress, ipv6TcpConnState=ipv6TcpConnState, ipv6TcpConnEntry=ipv6TcpConnEntry, ipv6TcpConformance=ipv6TcpConformance, ipv6TcpCompliances=ipv6TcpCompliances, PYSNMP_MODULE_ID=ipv6TcpMIB)
