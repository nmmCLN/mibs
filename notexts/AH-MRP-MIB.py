#
# PySNMP MIB module AH-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-MRP-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:44 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
AhString, ahAPMRP, AhNodeID = mibBuilder.importSymbols("AH-SMI-MIB", "AhString", "ahAPMRP", "AhNodeID")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, TimeTicks, ObjectIdentity, iso, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity", "iso", "NotificationType", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("AH-MRP-MIB", ahNeighberAPId=ahNeighberAPId, ahTxViDataFrames=ahTxViDataFrames, ahTxBeDataFrames=ahTxBeDataFrames, ahRXDataOctets=ahRXDataOctets, ahTxDataFrames=ahTxDataFrames, ahLinkCost=ahLinkCost, ahRxDataFrames=ahRxDataFrames, ahRxMulticastFrames=ahRxMulticastFrames, ahTxDataOctets=ahTxDataOctets, ahRxBroadcastFrames=ahRxBroadcastFrames, AhLinkType=AhLinkType, ahLinkUptime=ahLinkUptime, ahNeighborTable=ahNeighborTable, ahRxUnicastFrames=ahRxUnicastFrames, ahTxUnicastFrames=ahTxUnicastFrames, PYSNMP_MODULE_ID=ahMRP, ahTxMulticastFrames=ahTxMulticastFrames, ahLinkType=ahLinkType, ahTxBroadcastFrames=ahTxBroadcastFrames, ahRSSI=ahRSSI, ahTxMgtFrames=ahTxMgtFrames, ahTxVoDataFrames=ahTxVoDataFrames, ahNeighborEntry=ahNeighborEntry, ahRxMgtFrames=ahRxMgtFrames, ahTxBgDataFrames=ahTxBgDataFrames, ahMRP=ahMRP)
