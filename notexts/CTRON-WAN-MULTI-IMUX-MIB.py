#
# PySNMP MIB module CTRON-WAN-MULTI-IMUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WAN-MULTI-IMUX-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ctWanServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctWanServices")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctWanMultiMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2))
ctWANMMuxGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1))
ctWANMMuxMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWANMMuxMaxNum.setStatus('mandatory')
ctWanMMuxTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2), )
if mibBuilder.loadTexts: ctWanMMuxTable.setStatus('mandatory')
ctWanMMuxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxId"))
if mibBuilder.loadTexts: ctWanMMuxEntry.setStatus('mandatory')
ctWanMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxId.setStatus('mandatory')
ctWanMMuxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxIfIndex.setStatus('mandatory')
ctWanMMuxMaxNumGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxMaxNumGroups.setStatus('mandatory')
ctWanMMuxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxAdmin.setStatus('mandatory')
ctWanMMuxGroupTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3), )
if mibBuilder.loadTexts: ctWanMMuxGroupTable.setStatus('mandatory')
ctWanMMuxGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupMMuxId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupId"))
if mibBuilder.loadTexts: ctWanMMuxGroupEntry.setStatus('mandatory')
ctWanMMuxGroupMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupMMuxId.setStatus('mandatory')
ctWanMMuxGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupId.setStatus('mandatory')
ctWanMMuxGroupAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupAdmin.setStatus('mandatory')
ctWanMMuxGroupNumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupNumChannels.setStatus('mandatory')
ctWanMMuxGroupAddChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupAddChannel.setStatus('mandatory')
ctWanMMuxGroupDelChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupDelChannel.setStatus('mandatory')
ctWanMMuxChannelTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4), )
if mibBuilder.loadTexts: ctWanMMuxChannelTable.setStatus('mandatory')
ctWanMMuxChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelMMuxId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelGroupId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelId"))
if mibBuilder.loadTexts: ctWanMMuxChannelEntry.setStatus('mandatory')
ctWanMMuxChannelMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelMMuxId.setStatus('mandatory')
ctWanMMuxChannelGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelGroupId.setStatus('mandatory')
ctWanMMuxChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelId.setStatus('mandatory')
ctWanMMuxChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelIfIndex.setStatus('mandatory')
ctWanMMuxChannelPhysNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelPhysNum.setStatus('mandatory')
ctWanMMuxChannelBwAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelBwAvail.setStatus('mandatory')
ctWanMMuxChannelByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelByteCount.setStatus('mandatory')
ctWanMMuxChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-WAN-MULTI-IMUX-MIB", ctWanMMuxChannelGroupId=ctWanMMuxChannelGroupId, ctWanMMuxGroupId=ctWanMMuxGroupId, ctWanMultiMux=ctWanMultiMux, ctWanMMuxGroupDelChannel=ctWanMMuxGroupDelChannel, ctWanMMuxGroupEntry=ctWanMMuxGroupEntry, ctWanMMuxAdmin=ctWanMMuxAdmin, ctWANMMuxGeneralGroup=ctWANMMuxGeneralGroup, ctWanMMuxChannelIfIndex=ctWanMMuxChannelIfIndex, ctWanMMuxTable=ctWanMMuxTable, ctWanMMuxChannelId=ctWanMMuxChannelId, ctWanMMuxGroupTable=ctWanMMuxGroupTable, ctWanMMuxGroupAddChannel=ctWanMMuxGroupAddChannel, ctWanMMuxChannelEntry=ctWanMMuxChannelEntry, ctWanMMuxIfIndex=ctWanMMuxIfIndex, ctWanMMuxGroupMMuxId=ctWanMMuxGroupMMuxId, ctWanMMuxGroupAdmin=ctWanMMuxGroupAdmin, ctWanMMuxChannelByteCount=ctWanMMuxChannelByteCount, ctWanMMuxChannelTable=ctWanMMuxChannelTable, ctWanMMuxChannelBwAvail=ctWanMMuxChannelBwAvail, ctWanMMuxEntry=ctWanMMuxEntry, ctWanMMuxId=ctWanMMuxId, ctWanMMuxGroupNumChannels=ctWanMMuxGroupNumChannels, ctWanMMuxChannelPhysNum=ctWanMMuxChannelPhysNum, ctWANMMuxMaxNum=ctWANMMuxMaxNum, ctWanMMuxChannelStatus=ctWanMMuxChannelStatus, ctWanMMuxChannelMMuxId=ctWanMMuxChannelMMuxId, ctWanMMuxMaxNumGroups=ctWanMMuxMaxNumGroups)
