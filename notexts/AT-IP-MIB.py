#
# PySNMP MIB module AT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-IP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:42 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, iso, ModuleIdentity, IpAddress, Integer32, Counter64, Counter32, Unsigned32, Bits, TimeTicks, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "iso", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "Counter32", "Unsigned32", "Bits", "TimeTicks", "MibIdentifier", "NotificationType")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
atIpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602))
atIpMib.setRevisions(('2010-06-14 05:09', '2008-11-10 00:00',))
if mibBuilder.loadTexts: atIpMib.setLastUpdated('201006140509Z')
if mibBuilder.loadTexts: atIpMib.setOrganization('Allied Telesis Labs New Zealand')
class AtIpAddressAssignmentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notSet", 0), ("primary", 1), ("secondary", 2))

atIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1), )
if mibBuilder.loadTexts: atIpAddressTable.setStatus('current')
atIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1), ).setIndexNames((0, "AT-IP-MIB", "atIpAddressAddrType"), (0, "AT-IP-MIB", "atIpAddressAddr"))
if mibBuilder.loadTexts: atIpAddressEntry.setStatus('current')
atIpAddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: atIpAddressAddrType.setStatus('current')
atIpAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: atIpAddressAddr.setStatus('current')
atIpAddressPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressPrefixLen.setStatus('current')
atIpAddressLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressLabel.setStatus('current')
atIpAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressIfIndex.setStatus('current')
atIpAddressAssignmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 6), AtIpAddressAssignmentType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressAssignmentType.setStatus('current')
atIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressRowStatus.setStatus('current')
mibBuilder.exportSymbols("AT-IP-MIB", atIpAddressAssignmentType=atIpAddressAssignmentType, atIpAddressRowStatus=atIpAddressRowStatus, PYSNMP_MODULE_ID=atIpMib, atIpAddressAddrType=atIpAddressAddrType, atIpMib=atIpMib, atIpAddressTable=atIpAddressTable, atIpAddressEntry=atIpAddressEntry, atIpAddressPrefixLen=atIpAddressPrefixLen, atIpAddressIfIndex=atIpAddressIfIndex, AtIpAddressAssignmentType=AtIpAddressAssignmentType, atIpAddressAddr=atIpAddressAddr, atIpAddressLabel=atIpAddressLabel)
