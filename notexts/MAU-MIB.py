#
# PySNMP MIB module MAU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/MAU-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:27:00 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
IANAifJackType, IANAifMauMediaAvailable, IANAifMauAutoNegCapBits, IANAifMauTypeListBits = mibBuilder.importSymbols("IANA-MAU-MIB", "IANAifJackType", "IANAifMauMediaAvailable", "IANAifMauAutoNegCapBits", "IANAifMauTypeListBits")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, Counter64, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, MibIdentifier, Counter32, Integer32, Bits, Unsigned32, IpAddress, mib_2, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "Bits", "Unsigned32", "IpAddress", "mib-2", "ModuleIdentity")
AutonomousType, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "TruthValue", "DisplayString")
mauMod = ModuleIdentity((1, 3, 6, 1, 2, 1, 26, 6))
mauMod.setRevisions(('2007-04-21 00:00', '2003-09-19 00:00', '1999-08-24 04:00', '1997-10-31 00:00', '1993-09-30 00:00',))
if mibBuilder.loadTexts: mauMod.setLastUpdated('200704210000Z')
if mibBuilder.loadTexts: mauMod.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
snmpDot3MauMgt = MibIdentifier((1, 3, 6, 1, 2, 1, 26))
class JackType(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("other", 1), ("rj45", 2), ("rj45S", 3), ("db9", 4), ("bnc", 5), ("fAUI", 6), ("mAUI", 7), ("fiberSC", 8), ("fiberMIC", 9), ("fiberST", 10), ("telco", 11), ("mtrj", 12), ("hssdc", 13), ("fiberLC", 14))

dot3RpMauBasicGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 1))
dot3IfMauBasicGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 2))
dot3BroadMauBasicGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 3))
dot3IfMauAutoNegGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 5))
rpMauTable = MibTable((1, 3, 6, 1, 2, 1, 26, 1, 1), )
if mibBuilder.loadTexts: rpMauTable.setStatus('current')
rpMauEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 1, 1, 1), ).setIndexNames((0, "MAU-MIB", "rpMauGroupIndex"), (0, "MAU-MIB", "rpMauPortIndex"), (0, "MAU-MIB", "rpMauIndex"))
if mibBuilder.loadTexts: rpMauEntry.setStatus('current')
rpMauGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauGroupIndex.setStatus('current')
rpMauPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauPortIndex.setStatus('current')
rpMauIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauIndex.setStatus('current')
rpMauType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 4), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauType.setStatus('current')
rpMauStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("operational", 3), ("standby", 4), ("shutdown", 5), ("reset", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rpMauStatus.setStatus('current')
rpMauMediaAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 6), IANAifMauMediaAvailable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauMediaAvailable.setStatus('current')
rpMauMediaAvailableStateExits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauMediaAvailableStateExits.setStatus('current')
rpMauJabberState = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("noJabber", 3), ("jabbering", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauJabberState.setStatus('current')
rpMauJabberingStateEnters = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauJabberingStateEnters.setStatus('current')
rpMauFalseCarriers = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpMauFalseCarriers.setStatus('current')
rpJackTable = MibTable((1, 3, 6, 1, 2, 1, 26, 1, 2), )
if mibBuilder.loadTexts: rpJackTable.setStatus('current')
rpJackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 1, 2, 1), ).setIndexNames((0, "MAU-MIB", "rpMauGroupIndex"), (0, "MAU-MIB", "rpMauPortIndex"), (0, "MAU-MIB", "rpMauIndex"), (0, "MAU-MIB", "rpJackIndex"))
if mibBuilder.loadTexts: rpJackEntry.setStatus('current')
rpJackIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rpJackIndex.setStatus('current')
rpJackType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 2, 1, 2), IANAifJackType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpJackType.setStatus('current')
ifMauTable = MibTable((1, 3, 6, 1, 2, 1, 26, 2, 1), )
if mibBuilder.loadTexts: ifMauTable.setStatus('current')
ifMauEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 2, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: ifMauEntry.setStatus('current')
ifMauIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauIfIndex.setStatus('current')
ifMauIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauIndex.setStatus('current')
ifMauType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauType.setStatus('current')
ifMauStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("operational", 3), ("standby", 4), ("shutdown", 5), ("reset", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMauStatus.setStatus('current')
ifMauMediaAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 5), IANAifMauMediaAvailable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauMediaAvailable.setStatus('current')
ifMauMediaAvailableStateExits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauMediaAvailableStateExits.setStatus('current')
ifMauJabberState = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("noJabber", 3), ("jabbering", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauJabberState.setStatus('current')
ifMauJabberingStateEnters = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauJabberingStateEnters.setStatus('current')
ifMauFalseCarriers = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauFalseCarriers.setStatus('current')
ifMauTypeList = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauTypeList.setStatus('deprecated')
ifMauDefaultType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 11), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMauDefaultType.setStatus('current')
ifMauAutoNegSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegSupported.setStatus('current')
ifMauTypeListBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 13), IANAifMauTypeListBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauTypeListBits.setStatus('current')
ifMauHCFalseCarriers = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauHCFalseCarriers.setStatus('current')
ifJackTable = MibTable((1, 3, 6, 1, 2, 1, 26, 2, 2), )
if mibBuilder.loadTexts: ifJackTable.setStatus('current')
ifJackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 2, 2, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"), (0, "MAU-MIB", "ifJackIndex"))
if mibBuilder.loadTexts: ifJackEntry.setStatus('current')
ifJackIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ifJackIndex.setStatus('current')
ifJackType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 2, 1, 2), IANAifJackType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifJackType.setStatus('current')
ifMauAutoNegTable = MibTable((1, 3, 6, 1, 2, 1, 26, 5, 1), )
if mibBuilder.loadTexts: ifMauAutoNegTable.setStatus('current')
ifMauAutoNegEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 5, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: ifMauAutoNegEntry.setStatus('current')
ifMauAutoNegAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMauAutoNegAdminStatus.setStatus('current')
ifMauAutoNegRemoteSignaling = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("notdetected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegRemoteSignaling.setStatus('current')
ifMauAutoNegConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("configuring", 2), ("complete", 3), ("disabled", 4), ("parallelDetectFail", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegConfig.setStatus('current')
ifMauAutoNegCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegCapability.setStatus('deprecated')
ifMauAutoNegCapAdvertised = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMauAutoNegCapAdvertised.setStatus('deprecated')
ifMauAutoNegCapReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegCapReceived.setStatus('deprecated')
ifMauAutoNegRestart = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("norestart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMauAutoNegRestart.setStatus('current')
ifMauAutoNegCapabilityBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 9), IANAifMauAutoNegCapBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegCapabilityBits.setStatus('current')
ifMauAutoNegCapAdvertisedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 10), IANAifMauAutoNegCapBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMauAutoNegCapAdvertisedBits.setStatus('current')
ifMauAutoNegCapReceivedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 11), IANAifMauAutoNegCapBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegCapReceivedBits.setStatus('current')
ifMauAutoNegRemoteFaultAdvertised = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noError", 1), ("offline", 2), ("linkFailure", 3), ("autoNegError", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMauAutoNegRemoteFaultAdvertised.setStatus('current')
ifMauAutoNegRemoteFaultReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noError", 1), ("offline", 2), ("linkFailure", 3), ("autoNegError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMauAutoNegRemoteFaultReceived.setStatus('current')
broadMauBasicTable = MibTable((1, 3, 6, 1, 2, 1, 26, 3, 1), )
if mibBuilder.loadTexts: broadMauBasicTable.setStatus('deprecated')
broadMauBasicEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 3, 1, 1), ).setIndexNames((0, "MAU-MIB", "broadMauIfIndex"), (0, "MAU-MIB", "broadMauIndex"))
if mibBuilder.loadTexts: broadMauBasicEntry.setStatus('deprecated')
broadMauIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadMauIfIndex.setStatus('deprecated')
broadMauIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadMauIndex.setStatus('deprecated')
broadMauXmtRcvSplitType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("single", 2), ("dual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadMauXmtRcvSplitType.setStatus('deprecated')
broadMauXmtCarrierFreq = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadMauXmtCarrierFreq.setStatus('deprecated')
broadMauTranslationFreq = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadMauTranslationFreq.setStatus('deprecated')
snmpDot3MauTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 0))
rpMauJabberTrap = NotificationType((1, 3, 6, 1, 2, 1, 26, 0, 1)).setObjects(("MAU-MIB", "rpMauJabberState"))
if mibBuilder.loadTexts: rpMauJabberTrap.setStatus('current')
ifMauJabberTrap = NotificationType((1, 3, 6, 1, 2, 1, 26, 0, 2)).setObjects(("MAU-MIB", "ifMauJabberState"))
if mibBuilder.loadTexts: ifMauJabberTrap.setStatus('current')
mauModConf = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1))
mauModCompls = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1, 1))
mauModObjGrps = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1, 2))
mauModNotGrps = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1, 3))
mauRpGrpBasic = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 1)).setObjects(("MAU-MIB", "rpMauGroupIndex"), ("MAU-MIB", "rpMauPortIndex"), ("MAU-MIB", "rpMauIndex"), ("MAU-MIB", "rpMauType"), ("MAU-MIB", "rpMauStatus"), ("MAU-MIB", "rpMauMediaAvailable"), ("MAU-MIB", "rpMauMediaAvailableStateExits"), ("MAU-MIB", "rpMauJabberState"), ("MAU-MIB", "rpMauJabberingStateEnters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauRpGrpBasic = mauRpGrpBasic.setStatus('current')
mauRpGrp100Mbs = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 2)).setObjects(("MAU-MIB", "rpMauFalseCarriers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauRpGrp100Mbs = mauRpGrp100Mbs.setStatus('current')
mauRpGrpJack = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 3)).setObjects(("MAU-MIB", "rpJackType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauRpGrpJack = mauRpGrpJack.setStatus('current')
mauIfGrpBasic = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 4)).setObjects(("MAU-MIB", "ifMauIfIndex"), ("MAU-MIB", "ifMauIndex"), ("MAU-MIB", "ifMauType"), ("MAU-MIB", "ifMauStatus"), ("MAU-MIB", "ifMauMediaAvailable"), ("MAU-MIB", "ifMauMediaAvailableStateExits"), ("MAU-MIB", "ifMauJabberState"), ("MAU-MIB", "ifMauJabberingStateEnters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrpBasic = mauIfGrpBasic.setStatus('current')
mauIfGrp100Mbs = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 5)).setObjects(("MAU-MIB", "ifMauFalseCarriers"), ("MAU-MIB", "ifMauTypeList"), ("MAU-MIB", "ifMauDefaultType"), ("MAU-MIB", "ifMauAutoNegSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrp100Mbs = mauIfGrp100Mbs.setStatus('deprecated')
mauIfGrpJack = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 6)).setObjects(("MAU-MIB", "ifJackType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrpJack = mauIfGrpJack.setStatus('current')
mauIfGrpAutoNeg = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 7)).setObjects(("MAU-MIB", "ifMauAutoNegAdminStatus"), ("MAU-MIB", "ifMauAutoNegRemoteSignaling"), ("MAU-MIB", "ifMauAutoNegConfig"), ("MAU-MIB", "ifMauAutoNegCapability"), ("MAU-MIB", "ifMauAutoNegCapAdvertised"), ("MAU-MIB", "ifMauAutoNegCapReceived"), ("MAU-MIB", "ifMauAutoNegRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrpAutoNeg = mauIfGrpAutoNeg.setStatus('deprecated')
mauBroadBasic = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 8)).setObjects(("MAU-MIB", "broadMauIfIndex"), ("MAU-MIB", "broadMauIndex"), ("MAU-MIB", "broadMauXmtRcvSplitType"), ("MAU-MIB", "broadMauXmtCarrierFreq"), ("MAU-MIB", "broadMauTranslationFreq"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauBroadBasic = mauBroadBasic.setStatus('deprecated')
mauIfGrpHighCapacity = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 9)).setObjects(("MAU-MIB", "ifMauFalseCarriers"), ("MAU-MIB", "ifMauTypeListBits"), ("MAU-MIB", "ifMauDefaultType"), ("MAU-MIB", "ifMauAutoNegSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrpHighCapacity = mauIfGrpHighCapacity.setStatus('current')
mauIfGrpAutoNeg2 = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 10)).setObjects(("MAU-MIB", "ifMauAutoNegAdminStatus"), ("MAU-MIB", "ifMauAutoNegRemoteSignaling"), ("MAU-MIB", "ifMauAutoNegConfig"), ("MAU-MIB", "ifMauAutoNegCapabilityBits"), ("MAU-MIB", "ifMauAutoNegCapAdvertisedBits"), ("MAU-MIB", "ifMauAutoNegCapReceivedBits"), ("MAU-MIB", "ifMauAutoNegRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrpAutoNeg2 = mauIfGrpAutoNeg2.setStatus('current')
mauIfGrpAutoNeg1000Mbps = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 11)).setObjects(("MAU-MIB", "ifMauAutoNegRemoteFaultAdvertised"), ("MAU-MIB", "ifMauAutoNegRemoteFaultReceived"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrpAutoNeg1000Mbps = mauIfGrpAutoNeg1000Mbps.setStatus('current')
mauIfGrpHCStats = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 12)).setObjects(("MAU-MIB", "ifMauHCFalseCarriers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauIfGrpHCStats = mauIfGrpHCStats.setStatus('current')
rpMauNotifications = NotificationGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 3, 1)).setObjects(("MAU-MIB", "rpMauJabberTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rpMauNotifications = rpMauNotifications.setStatus('current')
ifMauNotifications = NotificationGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 3, 2)).setObjects(("MAU-MIB", "ifMauJabberTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifMauNotifications = ifMauNotifications.setStatus('current')
mauModRpCompl = ModuleCompliance((1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 1)).setObjects(("MAU-MIB", "mauRpGrpBasic"), ("MAU-MIB", "mauRpGrp100Mbs"), ("MAU-MIB", "mauRpGrpJack"), ("MAU-MIB", "rpMauNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauModRpCompl = mauModRpCompl.setStatus('deprecated')
mauModIfCompl = ModuleCompliance((1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 2)).setObjects(("MAU-MIB", "mauIfGrpBasic"), ("MAU-MIB", "mauIfGrp100Mbs"), ("MAU-MIB", "mauIfGrpJack"), ("MAU-MIB", "mauIfGrpAutoNeg"), ("MAU-MIB", "mauBroadBasic"), ("MAU-MIB", "ifMauNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauModIfCompl = mauModIfCompl.setStatus('deprecated')
mauModIfCompl2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 3)).setObjects(("MAU-MIB", "mauIfGrpBasic"), ("MAU-MIB", "mauIfGrpHighCapacity"), ("MAU-MIB", "mauIfGrpJack"), ("MAU-MIB", "mauIfGrpAutoNeg2"), ("MAU-MIB", "mauIfGrpAutoNeg1000Mbps"), ("MAU-MIB", "ifMauNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauModIfCompl2 = mauModIfCompl2.setStatus('deprecated')
mauModRpCompl2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 4)).setObjects(("MAU-MIB", "mauRpGrpBasic"), ("MAU-MIB", "mauRpGrp100Mbs"), ("MAU-MIB", "mauRpGrpJack"), ("MAU-MIB", "rpMauNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauModRpCompl2 = mauModRpCompl2.setStatus('current')
mauModIfCompl3 = ModuleCompliance((1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 5)).setObjects(("MAU-MIB", "mauIfGrpBasic"), ("MAU-MIB", "mauIfGrpHighCapacity"), ("MAU-MIB", "mauIfGrpHCStats"), ("MAU-MIB", "mauIfGrpJack"), ("MAU-MIB", "mauIfGrpAutoNeg2"), ("MAU-MIB", "mauIfGrpAutoNeg1000Mbps"), ("MAU-MIB", "ifMauNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mauModIfCompl3 = mauModIfCompl3.setStatus('current')
mibBuilder.exportSymbols("MAU-MIB", ifMauJabberingStateEnters=ifMauJabberingStateEnters, rpMauFalseCarriers=rpMauFalseCarriers, rpJackType=rpJackType, rpMauStatus=rpMauStatus, ifMauHCFalseCarriers=ifMauHCFalseCarriers, ifMauAutoNegTable=ifMauAutoNegTable, broadMauXmtCarrierFreq=broadMauXmtCarrierFreq, broadMauIndex=broadMauIndex, ifJackTable=ifJackTable, mauModRpCompl2=mauModRpCompl2, rpMauEntry=rpMauEntry, broadMauBasicEntry=broadMauBasicEntry, snmpDot3MauMgt=snmpDot3MauMgt, rpMauPortIndex=rpMauPortIndex, rpJackIndex=rpJackIndex, rpJackEntry=rpJackEntry, mauRpGrpBasic=mauRpGrpBasic, ifMauTable=ifMauTable, ifMauIfIndex=ifMauIfIndex, mauIfGrpAutoNeg2=mauIfGrpAutoNeg2, ifMauMediaAvailableStateExits=ifMauMediaAvailableStateExits, rpMauJabberTrap=rpMauJabberTrap, rpMauTable=rpMauTable, ifMauJabberState=ifMauJabberState, ifMauAutoNegConfig=ifMauAutoNegConfig, ifMauAutoNegAdminStatus=ifMauAutoNegAdminStatus, mauModIfCompl=mauModIfCompl, PYSNMP_MODULE_ID=mauMod, dot3IfMauAutoNegGroup=dot3IfMauAutoNegGroup, ifMauAutoNegRemoteFaultAdvertised=ifMauAutoNegRemoteFaultAdvertised, mauIfGrpHCStats=mauIfGrpHCStats, ifMauAutoNegRemoteSignaling=ifMauAutoNegRemoteSignaling, dot3RpMauBasicGroup=dot3RpMauBasicGroup, ifMauMediaAvailable=ifMauMediaAvailable, ifMauNotifications=ifMauNotifications, dot3IfMauBasicGroup=dot3IfMauBasicGroup, ifJackIndex=ifJackIndex, mauModConf=mauModConf, mauModIfCompl3=mauModIfCompl3, broadMauXmtRcvSplitType=broadMauXmtRcvSplitType, mauIfGrpAutoNeg1000Mbps=mauIfGrpAutoNeg1000Mbps, ifJackType=ifJackType, broadMauBasicTable=broadMauBasicTable, rpMauJabberState=rpMauJabberState, ifMauAutoNegSupported=ifMauAutoNegSupported, mauModObjGrps=mauModObjGrps, ifMauTypeListBits=ifMauTypeListBits, mauModNotGrps=mauModNotGrps, mauModCompls=mauModCompls, rpMauMediaAvailableStateExits=rpMauMediaAvailableStateExits, rpMauJabberingStateEnters=rpMauJabberingStateEnters, ifMauAutoNegCapabilityBits=ifMauAutoNegCapabilityBits, mauIfGrpHighCapacity=mauIfGrpHighCapacity, ifMauAutoNegCapReceived=ifMauAutoNegCapReceived, mauBroadBasic=mauBroadBasic, ifMauIndex=ifMauIndex, ifMauAutoNegRestart=ifMauAutoNegRestart, ifMauStatus=ifMauStatus, mauIfGrpJack=mauIfGrpJack, ifMauAutoNegCapAdvertisedBits=ifMauAutoNegCapAdvertisedBits, JackType=JackType, ifMauAutoNegCapReceivedBits=ifMauAutoNegCapReceivedBits, broadMauTranslationFreq=broadMauTranslationFreq, mauRpGrpJack=mauRpGrpJack, rpMauNotifications=rpMauNotifications, mauIfGrpBasic=mauIfGrpBasic, ifMauTypeList=ifMauTypeList, snmpDot3MauTraps=snmpDot3MauTraps, ifMauEntry=ifMauEntry, rpMauType=rpMauType, mauMod=mauMod, ifMauAutoNegRemoteFaultReceived=ifMauAutoNegRemoteFaultReceived, ifMauJabberTrap=ifMauJabberTrap, mauModRpCompl=mauModRpCompl, rpMauIndex=rpMauIndex, ifMauAutoNegEntry=ifMauAutoNegEntry, broadMauIfIndex=broadMauIfIndex, ifMauAutoNegCapability=ifMauAutoNegCapability, mauIfGrp100Mbs=mauIfGrp100Mbs, rpMauGroupIndex=rpMauGroupIndex, mauModIfCompl2=mauModIfCompl2, ifMauType=ifMauType, ifMauAutoNegCapAdvertised=ifMauAutoNegCapAdvertised, rpJackTable=rpJackTable, ifMauFalseCarriers=ifMauFalseCarriers, ifMauDefaultType=ifMauDefaultType, mauRpGrp100Mbs=mauRpGrp100Mbs, mauIfGrpAutoNeg=mauIfGrpAutoNeg, ifJackEntry=ifJackEntry, dot3BroadMauBasicGroup=dot3BroadMauBasicGroup, rpMauMediaAvailable=rpMauMediaAvailable)
