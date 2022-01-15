#
# PySNMP MIB module AH-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-MRP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:07 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ahAPMRP, AhNodeID, AhString = mibBuilder.importSymbols("AH-SMI-MIB", "ahAPMRP", "AhNodeID", "AhString")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, ObjectIdentity, iso, Bits, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ObjectIdentity", "iso", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ahMRP = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1))
if mibBuilder.loadTexts: ahMRP.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: ahMRP.setOrganization('Aerohive Networks, Inc')
if mibBuilder.loadTexts: ahMRP.setContactInfo('info@aerohive.com\n                        1011 McCarthy Boulevard\n                        Milpitas, CA 95035')
if mibBuilder.loadTexts: ahMRP.setDescription('This module contains the MIB definition of \n\t\t\tmesh routing protocol (MRP) related information.')
class AhLinkType(TextualConvention, Integer32):
    description = 'Interface type - (ETHERNET, WIRELESS)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ahETHERNET", 0), ("ahWIRELESS", 1))

ahNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: ahNeighborTable.setStatus('current')
if mibBuilder.loadTexts: ahNeighborTable.setDescription('Table of directly connected APs')
ahNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "AH-MRP-MIB", "ahNeighberAPId"))
if mibBuilder.loadTexts: ahNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: ahNeighborEntry.setDescription('Individual entry of neighbor table')
ahNeighberAPId = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 1), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahNeighberAPId.setStatus('current')
if mibBuilder.loadTexts: ahNeighberAPId.setDescription('Uniquely identifies an AP - neighbor.')
ahLinkCost = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahLinkCost.setStatus('current')
if mibBuilder.loadTexts: ahLinkCost.setDescription('neighbour cost metrice.')
ahRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRSSI.setStatus('current')
if mibBuilder.loadTexts: ahRSSI.setDescription('An indicator for the RSSI of the neighbour node \n\t\t\tderived from last NDP message')
ahLinkUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahLinkUptime.setStatus('current')
if mibBuilder.loadTexts: ahLinkUptime.setDescription('Link up time in second')
ahLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 5), AhLinkType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahLinkType.setStatus('current')
if mibBuilder.loadTexts: ahLinkType.setDescription('Is it a ethernet link or wireless link.')
ahRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRxDataFrames.setDescription('The number of data frames received \n\t\t\tfrom the neighbor AP')
ahRXDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRXDataOctets.setStatus('current')
if mibBuilder.loadTexts: ahRXDataOctets.setDescription('The number of data octets received \n\t\t\tfrom the neighbor AP')
ahRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahRxMgtFrames.setDescription('The number of mgt frames received \n\t\t\tfrom the neighbor AP')
ahRxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxUnicastFrames.setStatus('current')
if mibBuilder.loadTexts: ahRxUnicastFrames.setDescription('The number of unitcast frames received \n\t\t\tfrom the neighbor AP')
ahRxMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: ahRxMulticastFrames.setDescription('The number of multicast frames received\n\t\t\tfrom the neighbor AP.')
ahRxBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxBroadcastFrames.setStatus('current')
if mibBuilder.loadTexts: ahRxBroadcastFrames.setDescription('The number of broadcast frames received\n\t\t\tfrom the neighbor AP.')
ahTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxDataFrames.setDescription('The number of transmitted data frames\n\t\t\tfrom the neighbor AP.')
ahTxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxMgtFrames.setDescription('The number of transmitted management frames\n\t\t\tfrom the neighbor AP.')
ahTxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxDataOctets.setStatus('current')
if mibBuilder.loadTexts: ahTxDataOctets.setDescription('The number of transmitted data in octets\n\t\t\tfrom the neighbor AP.')
ahTxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxUnicastFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxUnicastFrames.setDescription('The number of unitcast frames transmitted \n\t\t\tfrom the neighbor AP')
ahTxMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxMulticastFrames.setDescription('The number of multicast frames transmitted\n\t\t\tfrom the neighbor AP.')
ahTxBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxBroadcastFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxBroadcastFrames.setDescription('The number of broadcast frames transmitted\n\t\t\tfrom the neighbor AP.')
ahTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxBeDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxBeDataFrames.setDescription('The number of transmitted best effort priority data frames\n\t\t\tfrom the AP to its neighbor.')
ahTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxBgDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxBgDataFrames.setDescription('The number of transmitted back ground priority data frames\n\t\t\tfrom the AP to its neighbor.')
ahTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxViDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxViDataFrames.setDescription('The number of transmitted video priority data frames\n\t\t\tfrom the AP to its neighbor.')
ahTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxVoDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahTxVoDataFrames.setDescription('The number of transmitted voice priority data frames\n\t\t\tfrom the AP to its neighbor.')
mibBuilder.exportSymbols("AH-MRP-MIB", ahRXDataOctets=ahRXDataOctets, ahTxBeDataFrames=ahTxBeDataFrames, AhLinkType=AhLinkType, ahMRP=ahMRP, ahTxMulticastFrames=ahTxMulticastFrames, ahTxMgtFrames=ahTxMgtFrames, ahNeighborEntry=ahNeighborEntry, ahTxVoDataFrames=ahTxVoDataFrames, ahLinkUptime=ahLinkUptime, PYSNMP_MODULE_ID=ahMRP, ahTxViDataFrames=ahTxViDataFrames, ahTxDataOctets=ahTxDataOctets, ahRxMulticastFrames=ahRxMulticastFrames, ahRxDataFrames=ahRxDataFrames, ahTxBgDataFrames=ahTxBgDataFrames, ahRxUnicastFrames=ahRxUnicastFrames, ahTxBroadcastFrames=ahTxBroadcastFrames, ahRSSI=ahRSSI, ahTxDataFrames=ahTxDataFrames, ahRxMgtFrames=ahRxMgtFrames, ahRxBroadcastFrames=ahRxBroadcastFrames, ahTxUnicastFrames=ahTxUnicastFrames, ahLinkCost=ahLinkCost, ahNeighborTable=ahNeighborTable, ahNeighberAPId=ahNeighberAPId, ahLinkType=ahLinkType)
