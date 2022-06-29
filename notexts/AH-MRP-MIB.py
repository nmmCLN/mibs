#
# PySNMP MIB module AH-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-MRP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:48 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
AhString, ahAPMRP, AhNodeID = mibBuilder.importSymbols("AH-SMI-MIB", "AhString", "ahAPMRP", "AhNodeID")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, MibIdentifier, Unsigned32, Gauge32, iso, ModuleIdentity, Integer32, TimeTicks, Counter32, NotificationType, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Gauge32", "iso", "ModuleIdentity", "Integer32", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ahMRP = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1))
if mibBuilder.loadTexts: ahMRP.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: ahMRP.setOrganization('Aerohive Networks, Inc')
class AhLinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ahETHERNET", 0), ("ahWIRELESS", 1))

ahNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: ahNeighborTable.setStatus('current')
ahNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "AH-MRP-MIB", "ahNeighberAPId"))
if mibBuilder.loadTexts: ahNeighborEntry.setStatus('current')
ahNeighberAPId = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 1), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahNeighberAPId.setStatus('current')
ahLinkCost = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahLinkCost.setStatus('current')
ahRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRSSI.setStatus('current')
ahLinkUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahLinkUptime.setStatus('current')
ahLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 5), AhLinkType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahLinkType.setStatus('current')
ahRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxDataFrames.setStatus('current')
ahRXDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRXDataOctets.setStatus('current')
ahRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxMgtFrames.setStatus('current')
ahRxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxUnicastFrames.setStatus('current')
ahRxMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxMulticastFrames.setStatus('current')
ahRxBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRxBroadcastFrames.setStatus('current')
ahTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxDataFrames.setStatus('current')
ahTxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxMgtFrames.setStatus('current')
ahTxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxDataOctets.setStatus('current')
ahTxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxUnicastFrames.setStatus('current')
ahTxMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxMulticastFrames.setStatus('current')
ahTxBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxBroadcastFrames.setStatus('current')
ahTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxBeDataFrames.setStatus('current')
ahTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxBgDataFrames.setStatus('current')
ahTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxViDataFrames.setStatus('current')
ahTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahTxVoDataFrames.setStatus('current')
mibBuilder.exportSymbols("AH-MRP-MIB", ahLinkType=ahLinkType, ahLinkUptime=ahLinkUptime, ahTxDataFrames=ahTxDataFrames, ahTxMgtFrames=ahTxMgtFrames, ahNeighberAPId=ahNeighberAPId, ahRSSI=ahRSSI, ahRxUnicastFrames=ahRxUnicastFrames, ahRxBroadcastFrames=ahRxBroadcastFrames, ahRxMulticastFrames=ahRxMulticastFrames, AhLinkType=AhLinkType, ahTxMulticastFrames=ahTxMulticastFrames, PYSNMP_MODULE_ID=ahMRP, ahTxUnicastFrames=ahTxUnicastFrames, ahTxBgDataFrames=ahTxBgDataFrames, ahRXDataOctets=ahRXDataOctets, ahMRP=ahMRP, ahLinkCost=ahLinkCost, ahNeighborTable=ahNeighborTable, ahNeighborEntry=ahNeighborEntry, ahTxVoDataFrames=ahTxVoDataFrames, ahTxDataOctets=ahTxDataOctets, ahRxMgtFrames=ahRxMgtFrames, ahTxViDataFrames=ahTxViDataFrames, ahTxBeDataFrames=ahTxBeDataFrames, ahRxDataFrames=ahRxDataFrames, ahTxBroadcastFrames=ahTxBroadcastFrames)
