#
# PySNMP MIB module NBS-CONNECTIVITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-CONNECTIVITY-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:23 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
nbsCmmcPortIndex, nbsCmmcChassisIndex, nbsCmmcSlotIndex = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbsCmmcPortIndex", "nbsCmmcChassisIndex", "nbsCmmcSlotIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ObjectIdentity, Counter64, Gauge32, IpAddress, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "Gauge32", "IpAddress", "ModuleIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsConnectivityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 238))
if mibBuilder.loadTexts: nbsConnectivityMib.setLastUpdated('201405280000Z')
if mibBuilder.loadTexts: nbsConnectivityMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsConnectivityMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsConnectivityMib.setDescription('Read-only MIB which lists externally linked ports')
nbsConnectivityGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 238, 1))
if mibBuilder.loadTexts: nbsConnectivityGrp.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityGrp.setDescription('Connectivity information')
nbsConnectivityTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 238, 100))
if mibBuilder.loadTexts: nbsConnectivityTraps.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityTraps.setDescription('SNMP Traps or Notifications')
nbsConnectivityEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 238, 100, 0))
if mibBuilder.loadTexts: nbsConnectivityEvent.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityEvent.setDescription('Event Notification Definitions')
nbsConnectivityTable = MibTable((1, 3, 6, 1, 4, 1, 629, 238, 1, 1), )
if mibBuilder.loadTexts: nbsConnectivityTable.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityTable.setDescription('List of externally connected port pairs.\n\n                 The connectivity table entries come from discovery\n                 protocols.')
nbsConnectivityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1), ).setIndexNames((0, "NBS-CONNECTIVITY-MIB", "nbsConnectivitySourceIfIndex"), (0, "NBS-CONNECTIVITY-MIB", "nbsConnectivityOrdinalIndex"))
if mibBuilder.loadTexts: nbsConnectivityEntry.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityEntry.setDescription('Contains a description of a particular Port Connection.')
nbsConnectivitySourceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 10), InterfaceIndex())
if mibBuilder.loadTexts: nbsConnectivitySourceIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivitySourceIfIndex.setDescription('MIB II Interface index.')
nbsConnectivityOrdinalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: nbsConnectivityOrdinalIndex.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityOrdinalIndex.setDescription('The ordinal index for this entry. A given source\n                 port may have one or more destination ports.')
nbsConnectivityDestIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 20), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestIfIndex.setDescription('MIB II Interface index.')
nbsConnectivityDestIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 30), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestIPAddress.setStatus('deprecated')
if mibBuilder.loadTexts: nbsConnectivityDestIPAddress.setDescription('Deprecated. IPv4 information is in\n                 nbsConnectivityDestAddr instead.')
nbsConnectivityDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 40), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestAddrType.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestAddrType.setDescription('The address type of nbsConnectivityDestAddr.\n                 Currently ipv4 and ipv6 are supported.')
nbsConnectivityDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 50), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestAddr.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestAddr.setDescription("IP Address (Usually IPv4) of the remote port's SNMP agent")
nbsConnectivityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3), ("notSupported", 4), ("sourceBlocked", 5), ("destBlocked", 6))).clone('notSupported')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityStatus.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityStatus.setDescription('This object is used to indicate the link status.')
nbsConnectivityDestV6AddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 70), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestV6AddrType.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestV6AddrType.setDescription('The address type of nbsConnectivityDestV6Addr.')
nbsConnectivityDestV6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 80), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsConnectivityDestV6Addr.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityDestV6Addr.setDescription("IP Address (Usually IPv6) of the remote port's SNMP agent")
nbsConnectivityChanged = NotificationType((1, 3, 6, 1, 4, 1, 629, 238, 100, 0, 10)).setObjects(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"), ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"), ("NBS-CMMC-MIB", "nbsCmmcPortIndex"), ("NBS-CONNECTIVITY-MIB", "nbsConnectivityDestAddrType"), ("NBS-CONNECTIVITY-MIB", "nbsConnectivityDestAddr"), ("NBS-CONNECTIVITY-MIB", "nbsConnectivityStatus"))
if mibBuilder.loadTexts: nbsConnectivityChanged.setStatus('current')
if mibBuilder.loadTexts: nbsConnectivityChanged.setDescription('Sent after the port goes up or down.\n\n        This Notification is of severity ERROR, which means it should\n        be emitted unless disabled or nbsCmmcSysTrapTblEntLevel is set\n        to a severity worse than error(3).')
mibBuilder.exportSymbols("NBS-CONNECTIVITY-MIB", nbsConnectivityOrdinalIndex=nbsConnectivityOrdinalIndex, nbsConnectivityMib=nbsConnectivityMib, nbsConnectivityDestAddrType=nbsConnectivityDestAddrType, nbsConnectivityTraps=nbsConnectivityTraps, nbsConnectivityStatus=nbsConnectivityStatus, nbsConnectivitySourceIfIndex=nbsConnectivitySourceIfIndex, nbsConnectivityDestIfIndex=nbsConnectivityDestIfIndex, nbsConnectivityDestIPAddress=nbsConnectivityDestIPAddress, nbsConnectivityGrp=nbsConnectivityGrp, nbsConnectivityEntry=nbsConnectivityEntry, nbsConnectivityDestV6Addr=nbsConnectivityDestV6Addr, nbsConnectivityEvent=nbsConnectivityEvent, nbsConnectivityDestV6AddrType=nbsConnectivityDestV6AddrType, nbsConnectivityTable=nbsConnectivityTable, nbsConnectivityDestAddr=nbsConnectivityDestAddr, PYSNMP_MODULE_ID=nbsConnectivityMib, nbsConnectivityChanged=nbsConnectivityChanged)
