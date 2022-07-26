#
# PySNMP MIB module BTI8xx-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-INTERFACE-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:24:04 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mainSystem, = mibBuilder.importSymbols("BTI8xx-TC-MIB", "mainSystem")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfTotalCount, PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfCurrentCount", "PerfIntervalCount")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Counter64, IpAddress, NotificationType, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, TimeTicks, Unsigned32, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "IpAddress", "NotificationType", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "Gauge32", "Integer32", "Counter32")
TruthValue, MacAddress, DisplayString, DateAndTime, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "DateAndTime", "RowStatus", "TextualConvention")
interfaceConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5))
interfaceConfig.setRevisions(('2015-11-20 12:00', '2015-02-25 15:00', '2014-11-14 12:00', '2014-10-29 12:00', '2014-06-13 12:00', '2013-12-27 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: interfaceConfig.setRevisionsDescriptions(("\n            *1. Change the MAX-ACCESS(for silvercreek tool).\n              'not-accessible' -> 'read-only'\n                -interfaceConfigIndex\n                -interfaceStatisticsIndex\n                -remotePortIdLocalPort\n                -remotePortIdLocalType\n                -rateLimitPort\n                -stormCtrlPort\n\n            *2. Change the syntax.\n              2.1. syntax value range\n                interfaceStatisticsIndex (1..13) -> (1..8191)\n\n              2.2. DisplayString -> OCTET STRING\n                interfaceConfigPort\n                interfaceConfigDescription\n                interfaceConfigLag\n                remotePortIdLocalPort\n                remotePortIdLocalType\n                remotePortIdDesc\n                rateLimitPort\n                stormCtrlPort\n\n            *3. MIB code sorting.\n            ", '\n        *1. Change the access to interfaceStatisticsTable\n          > R/W -> R/O\n            interfaceStatisticsIndex\n            interfaceStatisticsInOctets\n            interfaceStatisticsInFrames\n            interfaceStatisticsInUcastPkts\n            interfaceStatisticsInMulticastPkts\n            interfaceStatisticsInBroadcastPkts\n            interfaceStatisticsOutOctets\n            interfaceStatisticsOutFrames\n            interfaceStatisticsOutUcastPkts\n            interfaceStatisticsOutMulticastPkts\n            interfaceStatisticsOutBroadcastPkts\n            interfaceStatisticsDropEvents\n            interfaceStatisticsFCSErrors\n            interfaceStatisticsUndersizePkts\n            interfaceStatisticsOversizePkts\n            interfaceStatisticsFragments\n            interfaceStatisticsJabbers\n            interfaceStatisticsSymbolErrors\n        ', '\n        *1. This item value is changed syntax \n          interfaceConfigIndex  Integer32 (1..255) -> Integer32 (1..8191)\n        ', '\n        *1. Change the sytax size\n          DisplayString(SIZE(0..256)) -> DisplayString(SIZE(0..255))\n        ', '\n        *1. This value range is changed the 13312 to 9600.\n          interfaceConfigMTU\n\n        *2. This value access is changed the read-write to read-only.\n          interfaceConfigOperStatus\n          interfaceConfigOperFlowCtrl\n          interfaceConfigAct\n\n        *3. This value range is changed the 1953125 to 1000000000.\n          stormCtrlBroadcastPps\n          stormCtrlMulticastPps\n          stormCtrlDlfPps\n        ', 'Initial version of MIB.',))
if mibBuilder.loadTexts: interfaceConfig.setLastUpdated('201511201200Z')
if mibBuilder.loadTexts: interfaceConfig.setOrganization('Actus Networks Ltd.')
if mibBuilder.loadTexts: interfaceConfig.setContactInfo('\n    Support:  +82-2-26535666\n    R&D:      +82-2-26535666\n    Fax:      +82-2-26534662\n    Email:    ymkim@actusnetworks.com\n    ')
if mibBuilder.loadTexts: interfaceConfig.setDescription('This is a top-level MIB for Actus whose purpose is to lay out\n    the top-level objects in the OID hierarchy from which\n    BTI8xx MIB OIDs descend.')
interfaceConfigTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1), )
if mibBuilder.loadTexts: interfaceConfigTable.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigTable.setDescription('Table that contains Interface Config Table.')
interfaceConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1), ).setIndexNames((0, "BTI8xx-INTERFACE-MIB", "interfaceConfigIndex"))
if mibBuilder.loadTexts: interfaceConfigEntry.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigEntry.setDescription('A list of information for Interface Config.')
interfaceConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigIndex.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigIndex.setDescription('The index value of interface Config entry.')
interfaceConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigPort.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigPort.setDescription('The index value of interface Config entry.')
interfaceConfigMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 9600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigMTU.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigMTU.setDescription('The MTU value of interface Config entry.')
interfaceConfigTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigTPID.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigTPID.setDescription('The index value of interface Config entry.\n          ex)8800, 88a8, 9100, 9200 \n          ')
interfaceConfigPVID = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigPVID.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigPVID.setDescription('The index value of interface Config entry.')
interfaceConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigAdminStatus.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigAdminStatus.setDescription('The index value of interface Config entry.')
interfaceConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigOperStatus.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigOperStatus.setDescription('The index value of interface Config entry.')
interfaceConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("force", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigMode.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigMode.setDescription('The index value of interface Config entry.')
interfaceConfigDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("full", 1), ("half", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigDuplex.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigDuplex.setDescription('The index value of interface Config entry.')
interfaceConfigSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigSpeed.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigSpeed.setDescription('The index value of interface Config entry.')
interfaceConfigAdminFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigAdminFlowCtrl.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigAdminFlowCtrl.setDescription('The index value of interface Config entry.')
interfaceConfigOperFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigOperFlowCtrl.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigOperFlowCtrl.setDescription('The index value of interface Config entry.')
interfaceConfigAct = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("act", 1), ("deAct", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigAct.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigAct.setDescription('The act value of interface Config entry.')
interfaceConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigDescription.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigDescription.setDescription('The description value of interface Config entry.')
interfaceConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigPriority.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigPriority.setDescription('The prioryty value of interface Config entry.')
interfaceConfigLag = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigLag.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigLag.setDescription('The Link Aggregation Group of interface Config entry.')
interfaceConfigLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigLearning.setStatus('current')
if mibBuilder.loadTexts: interfaceConfigLearning.setDescription(' ')
interfaceStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2), )
if mibBuilder.loadTexts: interfaceStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsTable.setDescription('Table that contains Interface Statistics Table.')
interfaceStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1), ).setIndexNames((0, "BTI8xx-INTERFACE-MIB", "interfaceStatisticsIndex"))
if mibBuilder.loadTexts: interfaceStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsEntry.setDescription('A list of information for Interface Statistics.')
interfaceStatisticsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsIndex.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsIndex.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInOctets.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsInOctets.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInFrames.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsInFrames.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInUcastPkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsInUcastPkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsInMulticastPkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsInBroadcastPkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutOctets.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsOutOctets.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutFrames.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsOutFrames.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutUcastPkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsOutUcastPkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsOutMulticastPkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsOutBroadcastPkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsDropEvents.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsDropEvents.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsFCSErrors.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsFCSErrors.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsUndersizePkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsUndersizePkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOversizePkts.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsOversizePkts.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsFragments.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsFragments.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsJabbers.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsJabbers.setDescription('The index value of interface Statistics entry.')
interfaceStatisticsSymbolErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsSymbolErrors.setStatus('current')
if mibBuilder.loadTexts: interfaceStatisticsSymbolErrors.setDescription('The index value of interface Statistics entry.')
remotePortIdTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3), )
if mibBuilder.loadTexts: remotePortIdTable.setStatus('current')
if mibBuilder.loadTexts: remotePortIdTable.setDescription('A table that contains informations for Remote Port ID .')
remotePortIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: remotePortIdEntry.setStatus('current')
if mibBuilder.loadTexts: remotePortIdEntry.setDescription('A list of information for Remote Port ID Table.')
remotePortIdLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortIdLocalPort.setStatus('current')
if mibBuilder.loadTexts: remotePortIdLocalPort.setDescription('The Interface Local Port value of Remote Port ID Table.')
remotePortIdLocalType = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortIdLocalType.setStatus('current')
if mibBuilder.loadTexts: remotePortIdLocalType.setDescription('The Interface Local Port Type value of Remote Port ID Table.')
remotePortIdDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remotePortIdDesc.setStatus('current')
if mibBuilder.loadTexts: remotePortIdDesc.setDescription('The Interface Port Description value of Remote Port ID  Table.')
rateLimitTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4), )
if mibBuilder.loadTexts: rateLimitTable.setStatus('current')
if mibBuilder.loadTexts: rateLimitTable.setDescription('A table that contains informations for rate-limit .')
rateLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rateLimitEntry.setStatus('current')
if mibBuilder.loadTexts: rateLimitEntry.setDescription('A list of information for Rate Limit Table.')
rateLimitPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rateLimitPort.setStatus('current')
if mibBuilder.loadTexts: rateLimitPort.setDescription('The Interface Local Port value of Rate Limit Table.')
rateLimitIngressRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitIngressRate.setStatus('current')
if mibBuilder.loadTexts: rateLimitIngressRate.setDescription('The Rate Limit Ingress Rate value of Rate Limit Table.')
rateLimitIngressBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitIngressBurst.setStatus('current')
if mibBuilder.loadTexts: rateLimitIngressBurst.setDescription('The Rate Limit Ingress Burst value of Rate Limit Table.')
rateLimitIngressState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitIngressState.setStatus('current')
if mibBuilder.loadTexts: rateLimitIngressState.setDescription('The Rate Limit Ingress State value of Rate Limit Table.')
rateLimitEgressRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitEgressRate.setStatus('current')
if mibBuilder.loadTexts: rateLimitEgressRate.setDescription('The Rate Limit Egress Rate value of Rate Limit Table.')
rateLimitEgressBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitEgressBurst.setStatus('current')
if mibBuilder.loadTexts: rateLimitEgressBurst.setDescription('The Rate Limit Egress Burst value of Rate Limit Table.')
rateLimitEgressState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitEgressState.setStatus('current')
if mibBuilder.loadTexts: rateLimitEgressState.setDescription('The Rate Limit Egress State value of Rate Limit Table.')
rateLimitShapingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("layer1", 0), ("layer2", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitShapingMode.setStatus('current')
if mibBuilder.loadTexts: rateLimitShapingMode.setDescription('The Rate Limit Mode value of Rate Limit Table.')
stormCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5), )
if mibBuilder.loadTexts: stormCtrlTable.setStatus('current')
if mibBuilder.loadTexts: stormCtrlTable.setDescription('A table that contains informations for rate-limit .')
stormCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: stormCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: stormCtrlEntry.setDescription('A list of information for Rate Limit Table.')
stormCtrlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stormCtrlPort.setStatus('current')
if mibBuilder.loadTexts: stormCtrlPort.setDescription('The  Port value of Storm Control Table.')
stormCtrlBroadcastPps = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlBroadcastPps.setStatus('current')
if mibBuilder.loadTexts: stormCtrlBroadcastPps.setDescription('The Broadcast PPS  value of Storm Control Table.')
stormCtrlBroadcastState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlBroadcastState.setStatus('current')
if mibBuilder.loadTexts: stormCtrlBroadcastState.setDescription('The Broadcast State  value of Storm Control Table.')
stormCtrlMulticastPps = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlMulticastPps.setStatus('current')
if mibBuilder.loadTexts: stormCtrlMulticastPps.setDescription('The Broadcast PPS  value of Storm Control Table.')
stormCtrlMulticastState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlMulticastState.setStatus('current')
if mibBuilder.loadTexts: stormCtrlMulticastState.setDescription('The Multicast State  value of Storm Control Table.')
stormCtrlDlfPps = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlDlfPps.setStatus('current')
if mibBuilder.loadTexts: stormCtrlDlfPps.setDescription('The Dlf PPS  value of Storm Control Table.')
stormCtrlDlfState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlDlfState.setStatus('current')
if mibBuilder.loadTexts: stormCtrlDlfState.setDescription('The dlf State  value of Storm Control Table.')
mibBuilder.exportSymbols("BTI8xx-INTERFACE-MIB", interfaceStatisticsInFrames=interfaceStatisticsInFrames, interfaceConfigDescription=interfaceConfigDescription, stormCtrlDlfPps=stormCtrlDlfPps, stormCtrlMulticastState=stormCtrlMulticastState, remotePortIdDesc=remotePortIdDesc, stormCtrlBroadcastPps=stormCtrlBroadcastPps, interfaceStatisticsIndex=interfaceStatisticsIndex, interfaceStatisticsOutBroadcastPkts=interfaceStatisticsOutBroadcastPkts, interfaceConfigTPID=interfaceConfigTPID, interfaceStatisticsUndersizePkts=interfaceStatisticsUndersizePkts, PYSNMP_MODULE_ID=interfaceConfig, rateLimitIngressState=rateLimitIngressState, interfaceConfigEntry=interfaceConfigEntry, interfaceConfigPVID=interfaceConfigPVID, rateLimitEgressState=rateLimitEgressState, stormCtrlEntry=stormCtrlEntry, rateLimitIngressRate=rateLimitIngressRate, rateLimitShapingMode=rateLimitShapingMode, interfaceStatisticsEntry=interfaceStatisticsEntry, interfaceStatisticsInMulticastPkts=interfaceStatisticsInMulticastPkts, remotePortIdLocalType=remotePortIdLocalType, interfaceStatisticsOutUcastPkts=interfaceStatisticsOutUcastPkts, remotePortIdEntry=remotePortIdEntry, stormCtrlPort=stormCtrlPort, interfaceStatisticsInOctets=interfaceStatisticsInOctets, interfaceStatisticsDropEvents=interfaceStatisticsDropEvents, interfaceStatisticsFCSErrors=interfaceStatisticsFCSErrors, interfaceConfigLag=interfaceConfigLag, remotePortIdLocalPort=remotePortIdLocalPort, interfaceStatisticsSymbolErrors=interfaceStatisticsSymbolErrors, rateLimitTable=rateLimitTable, rateLimitPort=rateLimitPort, rateLimitEgressBurst=rateLimitEgressBurst, interfaceConfigAct=interfaceConfigAct, remotePortIdTable=remotePortIdTable, interfaceConfigPort=interfaceConfigPort, interfaceStatisticsOutOctets=interfaceStatisticsOutOctets, interfaceConfigTable=interfaceConfigTable, interfaceStatisticsOutMulticastPkts=interfaceStatisticsOutMulticastPkts, interfaceConfigAdminStatus=interfaceConfigAdminStatus, interfaceConfigSpeed=interfaceConfigSpeed, interfaceStatisticsInUcastPkts=interfaceStatisticsInUcastPkts, rateLimitIngressBurst=rateLimitIngressBurst, interfaceConfigOperFlowCtrl=interfaceConfigOperFlowCtrl, interfaceStatisticsOutFrames=interfaceStatisticsOutFrames, interfaceConfigPriority=interfaceConfigPriority, interfaceConfigMTU=interfaceConfigMTU, interfaceStatisticsInBroadcastPkts=interfaceStatisticsInBroadcastPkts, interfaceStatisticsFragments=interfaceStatisticsFragments, interfaceStatisticsJabbers=interfaceStatisticsJabbers, interfaceConfigAdminFlowCtrl=interfaceConfigAdminFlowCtrl, stormCtrlTable=stormCtrlTable, interfaceConfig=interfaceConfig, interfaceStatisticsTable=interfaceStatisticsTable, rateLimitEntry=rateLimitEntry, interfaceConfigDuplex=interfaceConfigDuplex, interfaceStatisticsOversizePkts=interfaceStatisticsOversizePkts, interfaceConfigLearning=interfaceConfigLearning, interfaceConfigOperStatus=interfaceConfigOperStatus, interfaceConfigIndex=interfaceConfigIndex, stormCtrlMulticastPps=stormCtrlMulticastPps, stormCtrlBroadcastState=stormCtrlBroadcastState, interfaceConfigMode=interfaceConfigMode, stormCtrlDlfState=stormCtrlDlfState, rateLimitEgressRate=rateLimitEgressRate)
