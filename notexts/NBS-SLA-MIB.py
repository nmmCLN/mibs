#
# PySNMP MIB module NBS-SLA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-SLA-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:09 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, Unsigned32, Gauge32, Integer32, TimeTicks, IpAddress, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "Unsigned32", "Gauge32", "Integer32", "TimeTicks", "IpAddress", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSlaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 216))
if mibBuilder.loadTexts: nbsSlaMib.setLastUpdated('201610190000Z')
if mibBuilder.loadTexts: nbsSlaMib.setOrganization('NBS')
nbsSlaTrafficGenGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 216, 1))
if mibBuilder.loadTexts: nbsSlaTrafficGenGrp.setStatus('current')
nbsSlaLossGainGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 216, 2))
if mibBuilder.loadTexts: nbsSlaLossGainGrp.setStatus('current')
nbsSlaPerfMonGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 216, 3))
if mibBuilder.loadTexts: nbsSlaPerfMonGrp.setStatus('current')
nbsSlaTrafficGenTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 216, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaTrafficGenTableSize.setStatus('current')
nbsSlaTrafficGenTable = MibTable((1, 3, 6, 1, 4, 1, 629, 216, 1, 2), )
if mibBuilder.loadTexts: nbsSlaTrafficGenTable.setStatus('current')
nbsSlaTrafficGenEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1), ).setIndexNames((0, "NBS-SLA-MIB", "nbsSlaTrafficGenIfIndex"))
if mibBuilder.loadTexts: nbsSlaTrafficGenEntry.setStatus('current')
nbsSlaTrafficGenIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSlaTrafficGenIfIndex.setStatus('current')
nbsSlaTrafficGenAction = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("start", 2), ("stop", 3))).clone('stop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenAction.setStatus('current')
nbsSlaTrafficGenFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 9600)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenFrameSize.setStatus('current')
nbsSlaTrafficGenFrameSizeType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("random", 2), ("fixed", 3))).clone('fixed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenFrameSizeType.setStatus('current')
nbsSlaTrafficGenFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenFrameCount.setStatus('current')
nbsSlaTrafficGenFrameCountType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("continuous", 2), ("fixed", 3))).clone('continuous')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenFrameCountType.setStatus('current')
nbsSlaTrafficGenInterPacketGap = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(12, 134217727)).clone(1249928)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenInterPacketGap.setStatus('current')
nbsSlaTrafficGenMaxHeaders = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaTrafficGenMaxHeaders.setStatus('current')
nbsSlaTrafficGenMaxPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaTrafficGenMaxPattern.setStatus('current')
nbsSlaTrafficGenHeaders = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(48, 48)).setFixedLength(48).clone(hexValue="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenHeaders.setStatus('current')
nbsSlaTrafficGenDa = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6).clone(hexValue="000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenDa.setStatus('current')
nbsSlaTrafficGenDaType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("random", 2), ("fixed", 3), ("increment", 4))).clone('random')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenDaType.setStatus('current')
nbsSlaTrafficGenSa = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6).clone(hexValue="000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenSa.setStatus('current')
nbsSlaTrafficGenSaType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("random", 2), ("fixed", 3), ("increment", 4))).clone('random')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenSaType.setStatus('current')
nbsSlaTrafficGenTag = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4).clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenTag.setStatus('current')
nbsSlaTrafficGenTagType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("random", 2), ("fixed", 3), ("increment", 4))).clone('random')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenTagType.setStatus('current')
nbsSlaTrafficGenPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4).clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenPattern.setStatus('current')
nbsSlaTrafficGenPatternType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("random", 2), ("fixed", 3))).clone('random')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaTrafficGenPatternType.setStatus('current')
nbsSlaLossGainTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 216, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainTableSize.setStatus('current')
nbsSlaLossGainTable = MibTable((1, 3, 6, 1, 4, 1, 629, 216, 2, 2), )
if mibBuilder.loadTexts: nbsSlaLossGainTable.setStatus('current')
nbsSlaLossGainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1), ).setIndexNames((0, "NBS-SLA-MIB", "nbsSlaLossGainIfIndex"))
if mibBuilder.loadTexts: nbsSlaLossGainEntry.setStatus('current')
nbsSlaLossGainIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSlaLossGainIfIndex.setStatus('current')
nbsSlaLossGainAction = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSupported", 1), ("inactive", 2), ("start", 3), ("stop", 4), ("inProgress", 5))).clone('notSupported')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaLossGainAction.setStatus('current')
nbsSlaLossGainInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 86400)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaLossGainInterval.setStatus('current')
nbsSlaLossGainEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 4), Integer32().clone(1518)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainEthMax.setStatus('current')
nbsSlaLossGainRdAllFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdAllFrames.setStatus('current')
nbsSlaLossGainRdBadFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdBadFrames.setStatus('current')
nbsSlaLossGainRdDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdDiscards.setStatus('current')
nbsSlaLossGainRdUcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdUcastFrames.setStatus('current')
nbsSlaLossGainRdMcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdMcastFrames.setStatus('current')
nbsSlaLossGainRdBcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdBcastFrames.setStatus('current')
nbsSlaLossGainRdSize64 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize64.setStatus('current')
nbsSlaLossGainRdSize65to127 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize65to127.setStatus('current')
nbsSlaLossGainRdSize128to255 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize128to255.setStatus('current')
nbsSlaLossGainRdSize256to511 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize256to511.setStatus('current')
nbsSlaLossGainRdSize512to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize512to1023.setStatus('current')
nbsSlaLossGainRdSize1024toEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize1024toEthMax.setStatus('current')
nbsSlaLossGainRdSizeEthMaxto2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSizeEthMaxto2047.setStatus('current')
nbsSlaLossGainRdSize2048to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize2048to4095.setStatus('current')
nbsSlaLossGainRdSize4096to8191 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize4096to8191.setStatus('current')
nbsSlaLossGainRdSize8192orMore = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdSize8192orMore.setStatus('current')
nbsSlaLossGainRdFrameDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdFrameDivisor.setStatus('current')
nbsSlaLossGainRdAllOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdAllOctets.setStatus('current')
nbsSlaLossGainRdBadOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdBadOctets.setStatus('current')
nbsSlaLossGainRdOctetDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdOctetDivisor.setStatus('current')
nbsSlaLossGainRdTimeSpan = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainRdTimeSpan.setStatus('current')
nbsSlaLossGainAdAllFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdAllFrames.setStatus('current')
nbsSlaLossGainAdBadFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdBadFrames.setStatus('current')
nbsSlaLossGainAdDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdDiscards.setStatus('current')
nbsSlaLossGainAdUcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdUcastFrames.setStatus('current')
nbsSlaLossGainAdMcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdMcastFrames.setStatus('current')
nbsSlaLossGainAdBcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdBcastFrames.setStatus('current')
nbsSlaLossGainAdSize64 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize64.setStatus('current')
nbsSlaLossGainAdSize65to127 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize65to127.setStatus('current')
nbsSlaLossGainAdSize128to255 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize128to255.setStatus('current')
nbsSlaLossGainAdSize256to511 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize256to511.setStatus('current')
nbsSlaLossGainAdSize512to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize512to1023.setStatus('current')
nbsSlaLossGainAdSize1024toEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize1024toEthMax.setStatus('current')
nbsSlaLossGainAdSizeEthMaxto2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSizeEthMaxto2047.setStatus('current')
nbsSlaLossGainAdSize2048to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize2048to4095.setStatus('current')
nbsSlaLossGainAdSize4096to8191 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize4096to8191.setStatus('current')
nbsSlaLossGainAdSize8192orMore = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdSize8192orMore.setStatus('current')
nbsSlaLossGainAdFrameDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdFrameDivisor.setStatus('current')
nbsSlaLossGainAdAllOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdAllOctets.setStatus('current')
nbsSlaLossGainAdBadOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdBadOctets.setStatus('current')
nbsSlaLossGainAdOctetDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdOctetDivisor.setStatus('current')
nbsSlaLossGainAdTimeSpan = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 2, 2, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaLossGainAdTimeSpan.setStatus('current')
nbsSlaPerfMonTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 216, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonTableSize.setStatus('current')
nbsSlaPerfMonTable = MibTable((1, 3, 6, 1, 4, 1, 629, 216, 3, 2), )
if mibBuilder.loadTexts: nbsSlaPerfMonTable.setStatus('current')
nbsSlaPerfMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1), ).setIndexNames((0, "NBS-SLA-MIB", "nbsSlaPerfMonIfIndex"))
if mibBuilder.loadTexts: nbsSlaPerfMonEntry.setStatus('current')
nbsSlaPerfMonIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSlaPerfMonIfIndex.setStatus('current')
nbsSlaPerfMonAction = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("notSupported", 1), ("inactive", 2), ("start", 3), ("stop", 4), ("reflect", 5), ("forward", 6), ("inProgress", 7), ("complete", 8), ("stopping", 9))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaPerfMonAction.setStatus('current')
nbsSlaPerfMonSize = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9600)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaPerfMonSize.setStatus('current')
nbsSlaPerfMonDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 604800)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSlaPerfMonDuration.setStatus('current')
nbsSlaPerfMonTimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 5), Integer32().clone(60)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonTimeLeft.setStatus('current')
nbsSlaPerfMonEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 6), Integer32().clone(1518)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonEthMax.setStatus('current')
nbsSlaPerfMonAvgAllSizes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvgAllSizes.setStatus('current')
nbsSlaPerfMonAvg64 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg64.setStatus('current')
nbsSlaPerfMonAvg65to127 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg65to127.setStatus('current')
nbsSlaPerfMonAvg128to255 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg128to255.setStatus('current')
nbsSlaPerfMonAvg256to511 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg256to511.setStatus('current')
nbsSlaPerfMonAvg512to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg512to1023.setStatus('current')
nbsSlaPerfMonAvg1024toEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg1024toEthMax.setStatus('current')
nbsSlaPerfMonAvgEthMaxto2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvgEthMaxto2047.setStatus('current')
nbsSlaPerfMonAvg2048to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg2048to4095.setStatus('current')
nbsSlaPerfMonAvg4096to8191 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg4096to8191.setStatus('current')
nbsSlaPerfMonAvg8192orMore = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonAvg8192orMore.setStatus('current')
nbsSlaPerfMonMinAllSizes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMinAllSizes.setStatus('current')
nbsSlaPerfMonMin64 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin64.setStatus('current')
nbsSlaPerfMonMin65to127 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin65to127.setStatus('current')
nbsSlaPerfMonMin128to255 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin128to255.setStatus('current')
nbsSlaPerfMonMin256to511 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin256to511.setStatus('current')
nbsSlaPerfMonMin512to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin512to1023.setStatus('current')
nbsSlaPerfMonMin1024toEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin1024toEthMax.setStatus('current')
nbsSlaPerfMonMinEthMaxto2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMinEthMaxto2047.setStatus('current')
nbsSlaPerfMonMin2048to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin2048to4095.setStatus('current')
nbsSlaPerfMonMin4096to8191 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin4096to8191.setStatus('current')
nbsSlaPerfMonMin8192orMore = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMin8192orMore.setStatus('current')
nbsSlaPerfMonMaxAllSizes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMaxAllSizes.setStatus('current')
nbsSlaPerfMonMax64 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax64.setStatus('current')
nbsSlaPerfMonMax65to127 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax65to127.setStatus('current')
nbsSlaPerfMonMax128to255 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax128to255.setStatus('current')
nbsSlaPerfMonMax256to511 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax256to511.setStatus('current')
nbsSlaPerfMonMax512to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax512to1023.setStatus('current')
nbsSlaPerfMonMax1024toEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax1024toEthMax.setStatus('current')
nbsSlaPerfMonMaxEthMaxto2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMaxEthMaxto2047.setStatus('current')
nbsSlaPerfMonMax2048to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax2048to4095.setStatus('current')
nbsSlaPerfMonMax4096to8191 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax4096to8191.setStatus('current')
nbsSlaPerfMonMax8192orMore = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonMax8192orMore.setStatus('current')
nbsSlaPerfMonFramesAllSizes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFramesAllSizes.setStatus('current')
nbsSlaPerfMonFrames64 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames64.setStatus('current')
nbsSlaPerfMonFrames65to127 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames65to127.setStatus('current')
nbsSlaPerfMonFrames128to255 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames128to255.setStatus('current')
nbsSlaPerfMonFrames256to511 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames256to511.setStatus('current')
nbsSlaPerfMonFrames512to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames512to1023.setStatus('current')
nbsSlaPerfMonFrames1024toEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames1024toEthMax.setStatus('current')
nbsSlaPerfMonFramesEthMaxto2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFramesEthMaxto2047.setStatus('current')
nbsSlaPerfMonFrames2048to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames2048to4095.setStatus('current')
nbsSlaPerfMonFrames4096to8191 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 49), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames4096to8191.setStatus('current')
nbsSlaPerfMonFrames8192orMore = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 50), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonFrames8192orMore.setStatus('current')
nbsSlaPerfMonOctetsAllSizes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 51), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctetsAllSizes.setStatus('current')
nbsSlaPerfMonOctets64 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 52), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets64.setStatus('current')
nbsSlaPerfMonOctets65to127 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 53), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets65to127.setStatus('current')
nbsSlaPerfMonOctets128to255 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 54), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets128to255.setStatus('current')
nbsSlaPerfMonOctets256to511 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 55), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets256to511.setStatus('current')
nbsSlaPerfMonOctets512to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 56), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets512to1023.setStatus('current')
nbsSlaPerfMonOctets1024toEthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 57), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets1024toEthMax.setStatus('current')
nbsSlaPerfMonOctetsEthMaxto2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 58), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctetsEthMaxto2047.setStatus('current')
nbsSlaPerfMonOctets2048to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 59), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets2048to4095.setStatus('current')
nbsSlaPerfMonOctets4096to8191 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 60), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets4096to8191.setStatus('current')
nbsSlaPerfMonOctets8192orMore = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 216, 3, 2, 1, 61), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSlaPerfMonOctets8192orMore.setStatus('current')
mibBuilder.exportSymbols("NBS-SLA-MIB", nbsSlaPerfMonAvgAllSizes=nbsSlaPerfMonAvgAllSizes, nbsSlaPerfMonFrames256to511=nbsSlaPerfMonFrames256to511, nbsSlaPerfMonMin64=nbsSlaPerfMonMin64, nbsSlaPerfMonMax4096to8191=nbsSlaPerfMonMax4096to8191, nbsSlaLossGainAdAllFrames=nbsSlaLossGainAdAllFrames, nbsSlaLossGainRdSize2048to4095=nbsSlaLossGainRdSize2048to4095, nbsSlaPerfMonFrames65to127=nbsSlaPerfMonFrames65to127, nbsSlaPerfMonMax512to1023=nbsSlaPerfMonMax512to1023, nbsSlaLossGainTableSize=nbsSlaLossGainTableSize, nbsSlaLossGainRdSize1024toEthMax=nbsSlaLossGainRdSize1024toEthMax, nbsSlaPerfMonDuration=nbsSlaPerfMonDuration, nbsSlaTrafficGenHeaders=nbsSlaTrafficGenHeaders, nbsSlaPerfMonOctetsAllSizes=nbsSlaPerfMonOctetsAllSizes, nbsSlaPerfMonTableSize=nbsSlaPerfMonTableSize, nbsSlaTrafficGenDaType=nbsSlaTrafficGenDaType, nbsSlaPerfMonOctets256to511=nbsSlaPerfMonOctets256to511, nbsSlaLossGainRdAllFrames=nbsSlaLossGainRdAllFrames, nbsSlaPerfMonMinEthMaxto2047=nbsSlaPerfMonMinEthMaxto2047, nbsSlaLossGainRdSize512to1023=nbsSlaLossGainRdSize512to1023, nbsSlaPerfMonAvg2048to4095=nbsSlaPerfMonAvg2048to4095, nbsSlaLossGainRdSizeEthMaxto2047=nbsSlaLossGainRdSizeEthMaxto2047, nbsSlaPerfMonFramesAllSizes=nbsSlaPerfMonFramesAllSizes, nbsSlaPerfMonEthMax=nbsSlaPerfMonEthMax, nbsSlaLossGainAdSize65to127=nbsSlaLossGainAdSize65to127, nbsSlaTrafficGenInterPacketGap=nbsSlaTrafficGenInterPacketGap, nbsSlaTrafficGenTagType=nbsSlaTrafficGenTagType, nbsSlaLossGainRdBcastFrames=nbsSlaLossGainRdBcastFrames, nbsSlaTrafficGenFrameSizeType=nbsSlaTrafficGenFrameSizeType, nbsSlaPerfMonMin4096to8191=nbsSlaPerfMonMin4096to8191, nbsSlaPerfMonAvg256to511=nbsSlaPerfMonAvg256to511, nbsSlaLossGainIfIndex=nbsSlaLossGainIfIndex, nbsSlaLossGainRdUcastFrames=nbsSlaLossGainRdUcastFrames, nbsSlaLossGainRdBadOctets=nbsSlaLossGainRdBadOctets, nbsSlaLossGainRdOctetDivisor=nbsSlaLossGainRdOctetDivisor, nbsSlaTrafficGenPatternType=nbsSlaTrafficGenPatternType, nbsSlaPerfMonTable=nbsSlaPerfMonTable, nbsSlaTrafficGenPattern=nbsSlaTrafficGenPattern, nbsSlaLossGainEntry=nbsSlaLossGainEntry, nbsSlaPerfMonAvg128to255=nbsSlaPerfMonAvg128to255, nbsSlaPerfMonMin65to127=nbsSlaPerfMonMin65to127, nbsSlaLossGainAdTimeSpan=nbsSlaLossGainAdTimeSpan, nbsSlaPerfMonMax65to127=nbsSlaPerfMonMax65to127, nbsSlaPerfMonAvg8192orMore=nbsSlaPerfMonAvg8192orMore, nbsSlaPerfMonAvgEthMaxto2047=nbsSlaPerfMonAvgEthMaxto2047, nbsSlaLossGainEthMax=nbsSlaLossGainEthMax, nbsSlaTrafficGenSaType=nbsSlaTrafficGenSaType, nbsSlaLossGainAdSize1024toEthMax=nbsSlaLossGainAdSize1024toEthMax, nbsSlaLossGainAdOctetDivisor=nbsSlaLossGainAdOctetDivisor, nbsSlaTrafficGenIfIndex=nbsSlaTrafficGenIfIndex, nbsSlaPerfMonOctets8192orMore=nbsSlaPerfMonOctets8192orMore, nbsSlaPerfMonFramesEthMaxto2047=nbsSlaPerfMonFramesEthMaxto2047, nbsSlaPerfMonFrames64=nbsSlaPerfMonFrames64, nbsSlaLossGainAdSize128to255=nbsSlaLossGainAdSize128to255, nbsSlaPerfMonFrames4096to8191=nbsSlaPerfMonFrames4096to8191, nbsSlaPerfMonOctets4096to8191=nbsSlaPerfMonOctets4096to8191, nbsSlaLossGainRdAllOctets=nbsSlaLossGainRdAllOctets, nbsSlaLossGainAdBcastFrames=nbsSlaLossGainAdBcastFrames, nbsSlaLossGainAdSize8192orMore=nbsSlaLossGainAdSize8192orMore, nbsSlaMib=nbsSlaMib, nbsSlaLossGainAdMcastFrames=nbsSlaLossGainAdMcastFrames, PYSNMP_MODULE_ID=nbsSlaMib, nbsSlaPerfMonAvg1024toEthMax=nbsSlaPerfMonAvg1024toEthMax, nbsSlaPerfMonSize=nbsSlaPerfMonSize, nbsSlaPerfMonIfIndex=nbsSlaPerfMonIfIndex, nbsSlaPerfMonFrames128to255=nbsSlaPerfMonFrames128to255, nbsSlaTrafficGenFrameCount=nbsSlaTrafficGenFrameCount, nbsSlaPerfMonOctets512to1023=nbsSlaPerfMonOctets512to1023, nbsSlaLossGainAdUcastFrames=nbsSlaLossGainAdUcastFrames, nbsSlaTrafficGenTableSize=nbsSlaTrafficGenTableSize, nbsSlaPerfMonAvg64=nbsSlaPerfMonAvg64, nbsSlaPerfMonAvg65to127=nbsSlaPerfMonAvg65to127, nbsSlaPerfMonMax1024toEthMax=nbsSlaPerfMonMax1024toEthMax, nbsSlaPerfMonEntry=nbsSlaPerfMonEntry, nbsSlaLossGainAdDiscards=nbsSlaLossGainAdDiscards, nbsSlaPerfMonOctets65to127=nbsSlaPerfMonOctets65to127, nbsSlaLossGainRdSize64=nbsSlaLossGainRdSize64, nbsSlaTrafficGenFrameSize=nbsSlaTrafficGenFrameSize, nbsSlaLossGainRdSize8192orMore=nbsSlaLossGainRdSize8192orMore, nbsSlaLossGainAdSize64=nbsSlaLossGainAdSize64, nbsSlaPerfMonMin8192orMore=nbsSlaPerfMonMin8192orMore, nbsSlaLossGainRdSize4096to8191=nbsSlaLossGainRdSize4096to8191, nbsSlaPerfMonGrp=nbsSlaPerfMonGrp, nbsSlaTrafficGenMaxPattern=nbsSlaTrafficGenMaxPattern, nbsSlaTrafficGenDa=nbsSlaTrafficGenDa, nbsSlaLossGainAdSize256to511=nbsSlaLossGainAdSize256to511, nbsSlaPerfMonTimeLeft=nbsSlaPerfMonTimeLeft, nbsSlaPerfMonMaxAllSizes=nbsSlaPerfMonMaxAllSizes, nbsSlaTrafficGenGrp=nbsSlaTrafficGenGrp, nbsSlaPerfMonFrames1024toEthMax=nbsSlaPerfMonFrames1024toEthMax, nbsSlaPerfMonMax2048to4095=nbsSlaPerfMonMax2048to4095, nbsSlaPerfMonMin128to255=nbsSlaPerfMonMin128to255, nbsSlaLossGainRdSize256to511=nbsSlaLossGainRdSize256to511, nbsSlaPerfMonMin1024toEthMax=nbsSlaPerfMonMin1024toEthMax, nbsSlaPerfMonMin2048to4095=nbsSlaPerfMonMin2048to4095, nbsSlaPerfMonMax64=nbsSlaPerfMonMax64, nbsSlaPerfMonMaxEthMaxto2047=nbsSlaPerfMonMaxEthMaxto2047, nbsSlaLossGainRdMcastFrames=nbsSlaLossGainRdMcastFrames, nbsSlaLossGainAdAllOctets=nbsSlaLossGainAdAllOctets, nbsSlaPerfMonOctets2048to4095=nbsSlaPerfMonOctets2048to4095, nbsSlaLossGainTable=nbsSlaLossGainTable, nbsSlaLossGainRdBadFrames=nbsSlaLossGainRdBadFrames, nbsSlaTrafficGenTable=nbsSlaTrafficGenTable, nbsSlaPerfMonFrames8192orMore=nbsSlaPerfMonFrames8192orMore, nbsSlaPerfMonOctets64=nbsSlaPerfMonOctets64, nbsSlaLossGainRdTimeSpan=nbsSlaLossGainRdTimeSpan, nbsSlaTrafficGenEntry=nbsSlaTrafficGenEntry, nbsSlaLossGainRdFrameDivisor=nbsSlaLossGainRdFrameDivisor, nbsSlaLossGainRdSize128to255=nbsSlaLossGainRdSize128to255, nbsSlaLossGainInterval=nbsSlaLossGainInterval, nbsSlaPerfMonFrames2048to4095=nbsSlaPerfMonFrames2048to4095, nbsSlaLossGainAdSize2048to4095=nbsSlaLossGainAdSize2048to4095, nbsSlaTrafficGenTag=nbsSlaTrafficGenTag, nbsSlaTrafficGenMaxHeaders=nbsSlaTrafficGenMaxHeaders, nbsSlaTrafficGenFrameCountType=nbsSlaTrafficGenFrameCountType, nbsSlaPerfMonAction=nbsSlaPerfMonAction, nbsSlaPerfMonMax256to511=nbsSlaPerfMonMax256to511, nbsSlaLossGainAction=nbsSlaLossGainAction, nbsSlaPerfMonAvg4096to8191=nbsSlaPerfMonAvg4096to8191, nbsSlaTrafficGenSa=nbsSlaTrafficGenSa, nbsSlaLossGainGrp=nbsSlaLossGainGrp, nbsSlaLossGainAdFrameDivisor=nbsSlaLossGainAdFrameDivisor, nbsSlaPerfMonMax128to255=nbsSlaPerfMonMax128to255, nbsSlaPerfMonOctetsEthMaxto2047=nbsSlaPerfMonOctetsEthMaxto2047, nbsSlaLossGainRdDiscards=nbsSlaLossGainRdDiscards, nbsSlaLossGainRdSize65to127=nbsSlaLossGainRdSize65to127, nbsSlaPerfMonAvg512to1023=nbsSlaPerfMonAvg512to1023, nbsSlaLossGainAdBadOctets=nbsSlaLossGainAdBadOctets, nbsSlaPerfMonFrames512to1023=nbsSlaPerfMonFrames512to1023, nbsSlaPerfMonMax8192orMore=nbsSlaPerfMonMax8192orMore, nbsSlaLossGainAdSize512to1023=nbsSlaLossGainAdSize512to1023, nbsSlaPerfMonMinAllSizes=nbsSlaPerfMonMinAllSizes, nbsSlaLossGainAdSize4096to8191=nbsSlaLossGainAdSize4096to8191, nbsSlaPerfMonMin512to1023=nbsSlaPerfMonMin512to1023, nbsSlaTrafficGenAction=nbsSlaTrafficGenAction, nbsSlaPerfMonMin256to511=nbsSlaPerfMonMin256to511, nbsSlaPerfMonOctets1024toEthMax=nbsSlaPerfMonOctets1024toEthMax, nbsSlaLossGainAdSizeEthMaxto2047=nbsSlaLossGainAdSizeEthMaxto2047, nbsSlaPerfMonOctets128to255=nbsSlaPerfMonOctets128to255, nbsSlaLossGainAdBadFrames=nbsSlaLossGainAdBadFrames)
