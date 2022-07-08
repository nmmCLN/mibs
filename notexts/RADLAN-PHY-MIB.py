#
# PySNMP MIB module RADLAN-PHY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-PHY-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:27:00 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, MibIdentifier, Counter32, Integer32, Bits, Unsigned32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "Bits", "Unsigned32", "IpAddress", "ModuleIdentity")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
rlPhy = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 90))
rlPhy.setRevisions(('2002-09-30 00:24', '2003-09-21 00:24',))
if mibBuilder.loadTexts: rlPhy.setLastUpdated('200209300024Z')
if mibBuilder.loadTexts: rlPhy.setOrganization('Radlan Computer Communication Ltd.')
class RlPhyTestType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("rlPhyTestTableNoTest", 1), ("rlPhyTestTableCableStatus", 2), ("rlPhyTestTableCableFault", 3), ("rlPhyTestTableCableLength", 4), ("rlPhyTestTableTransceiverTemp", 5), ("rlPhyTestTableTransceiverSupply", 6), ("rlPhyTestTableTxBias", 7), ("rlPhyTestTableTxOutput", 8), ("rlPhyTestTableRxOpticalPower", 9), ("rlPhyTestTableDataReady", 10), ("rlPhyTestTableLOS", 11), ("rlPhyTestTableTxFault", 12), ("rlPhyTestTableCableChannel1", 13), ("rlPhyTestTableCableChannel2", 14), ("rlPhyTestTableCableChannel3", 15), ("rlPhyTestTableCableChannel4", 16), ("rlPhyTestTableCablePolarity1", 17), ("rlPhyTestTableCablePolarity2", 18), ("rlPhyTestTableCablePolarity3", 19), ("rlPhyTestTableCablePolarity4", 20), ("rlPhyTestTableCablePairSkew1", 21), ("rlPhyTestTableCablePairSkew2", 22), ("rlPhyTestTableCablePairSkew3", 23), ("rlPhyTestTableCablePairSkew4", 24))

rlPhyTest = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 90, 1))
rlPhyTestSetTable = MibTable((1, 3, 6, 1, 4, 1, 89, 90, 1, 1), )
if mibBuilder.loadTexts: rlPhyTestSetTable.setStatus('current')
rlPhyTestSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 90, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlPhyTestSetEntry.setStatus('current')
rlPhyTestSetType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 90, 1, 1, 1, 1), RlPhyTestType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhyTestSetType.setStatus('current')
rlPhyTestGetTable = MibTable((1, 3, 6, 1, 4, 1, 89, 90, 1, 2), )
if mibBuilder.loadTexts: rlPhyTestGetTable.setStatus('current')
rlPhyTestGetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RADLAN-PHY-MIB", "rlPhyTestGetType"))
if mibBuilder.loadTexts: rlPhyTestGetEntry.setStatus('current')
rlPhyTestGetType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 1), RlPhyTestType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhyTestGetType.setStatus('current')
rlPhyTestGetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("notSupported", 4), ("unAbleToRun", 5), ("aborted", 6), ("failed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhyTestGetStatus.setStatus('current')
rlPhyTestGetResult = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhyTestGetResult.setStatus('current')
rlPhyTestGetUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))).clone(namedValues=NamedValues(("integer", 1), ("boolean", 2), ("downUP", 3), ("reverseNormal", 4), ("mdiMdix", 5), ("meter", 6), ("degree", 7), ("microVolt", 8), ("microOham", 9), ("microAmper", 10), ("microWatt", 11), ("millisecond", 12), ("alaskaPhyLength", 13), ("alaskaPhyStatus", 14), ("dbm", 15), ("decidbm", 16), ("milidbm", 17), ("abcd", 18), ("nanosecond", 19)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhyTestGetUnits.setStatus('current')
rlPhyTestGetAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notRelevant", 1), ("noAlarmSet", 2), ("lowWarning", 3), ("highWarning", 4), ("lowAlarm", 5), ("highAlarm", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhyTestGetAlarm.setStatus('current')
rlPhyTestGetTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhyTestGetTimeStamp.setStatus('current')
mibBuilder.exportSymbols("RADLAN-PHY-MIB", PYSNMP_MODULE_ID=rlPhy, rlPhyTestGetUnits=rlPhyTestGetUnits, rlPhyTestGetAlarm=rlPhyTestGetAlarm, rlPhyTestGetStatus=rlPhyTestGetStatus, rlPhyTestGetTable=rlPhyTestGetTable, rlPhyTestSetTable=rlPhyTestSetTable, rlPhy=rlPhy, rlPhyTestGetResult=rlPhyTestGetResult, rlPhyTestGetTimeStamp=rlPhyTestGetTimeStamp, rlPhyTestGetType=rlPhyTestGetType, RlPhyTestType=RlPhyTestType, rlPhyTestSetType=rlPhyTestSetType, rlPhyTest=rlPhyTest, rlPhyTestSetEntry=rlPhyTestSetEntry, rlPhyTestGetEntry=rlPhyTestGetEntry)
