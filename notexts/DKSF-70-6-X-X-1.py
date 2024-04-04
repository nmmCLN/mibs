#
# PySNMP MIB module DKSF-70-6-X-X-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netping/DKSF-70-6-X-X-1
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:20 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
ModuleIdentity, TimeTicks, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, NotificationType, ObjectIdentity, Bits, MibIdentifier, enterprises, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "NotificationType", "ObjectIdentity", "Bits", "MibIdentifier", "enterprises", "Unsigned32", "Gauge32", "Counter64")
DisplayString, TimeStamp, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention", "TruthValue")
uniPingServerSolutionV3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25728, 70))
uniPingServerSolutionV3.setRevisions(('2016-08-24 00:00', '2015-07-14 00:00', '2015-05-29 00:00', '2014-12-03 00:00', '2014-11-26 00:00', '2014-02-02 00:00', '2014-01-29 00:00', '2014-01-21 00:00', '2013-04-11 00:00', '2012-05-31 00:00', '2012-04-17 00:00', '2012-03-23 00:00', '2011-09-23 00:00', '2011-03-24 00:00', '2010-10-14 00:00', '2010-09-20 00:00', '2010-05-31 00:00', '2010-04-14 00:00',))
if mibBuilder.loadTexts: uniPingServerSolutionV3.setLastUpdated('201608240000Z')
if mibBuilder.loadTexts: uniPingServerSolutionV3.setOrganization('Alentis Electronics')
lightcom = MibIdentifier((1, 3, 6, 1, 4, 1, 25728))
class FixedPoint1000(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

npTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 90))
npTrapEmailTo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 90, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npTrapEmailTo.setStatus('current')
npRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5500))
npRelayTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5500, 5), )
if mibBuilder.loadTexts: npRelayTable.setStatus('current')
npRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1), ).setIndexNames((0, "DKSF-70-6-X-X-1", "npRelayN"))
if mibBuilder.loadTexts: npRelayEntry.setStatus('current')
npRelayN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayN.setStatus('current')
npRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("flip", -1), ("off", 0), ("on", 1), ("watchdog", 2), ("schedule", 3), ("scheduleAndWatchdog", 4), ("logic", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayMode.setStatus('current')
npRelayStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayStartReset.setStatus('current')
npRelayMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayMemo.setStatus('current')
npRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayState.setStatus('current')
npThermo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800))
npThermoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8800, 1), )
if mibBuilder.loadTexts: npThermoTable.setStatus('current')
npThermoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1), ).setIndexNames((0, "DKSF-70-6-X-X-1", "npThermoSensorN"))
if mibBuilder.loadTexts: npThermoEntry.setStatus('current')
npThermoSensorN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoSensorN.setStatus('current')
npThermoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoValue.setStatus('current')
npThermoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoStatus.setStatus('current')
npThermoLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoLow.setStatus('current')
npThermoHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoHigh.setStatus('current')
npThermoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoMemo.setStatus('current')
npThermoValuePrecise = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 7), FixedPoint1000()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoValuePrecise.setStatus('current')
npThermoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2))
npThermoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0))
npThermoTrapSensorN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapSensorN.setStatus('current')
npThermoTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapValue.setStatus('current')
npThermoTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapStatus.setStatus('current')
npThermoTrapLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapLow.setStatus('current')
npThermoTrapHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapHigh.setStatus('current')
npThermoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapMemo.setStatus('current')
npThermoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)).setObjects(("DKSF-70-6-X-X-1", "npThermoTrapSensorN"), ("DKSF-70-6-X-X-1", "npThermoTrapValue"), ("DKSF-70-6-X-X-1", "npThermoTrapStatus"), ("DKSF-70-6-X-X-1", "npThermoTrapLow"), ("DKSF-70-6-X-X-1", "npThermoTrapHigh"), ("DKSF-70-6-X-X-1", "npThermoTrapMemo"))
if mibBuilder.loadTexts: npThermoTrap.setStatus('current')
npIo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900))
npIoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8900, 1), )
if mibBuilder.loadTexts: npIoTable.setStatus('current')
npIoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1), ).setIndexNames((0, "DKSF-70-6-X-X-1", "npIoLineN"))
if mibBuilder.loadTexts: npIoEntry.setStatus('current')
npIoLineN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLineN.setStatus('current')
npIoLevelIn = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLevelIn.setStatus('current')
npIoLevelOut = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("flip", -1), ("low", 0), ("high", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoLevelOut.setStatus('current')
npIoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoMemo.setStatus('current')
npIoPulseCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoPulseCounter.setStatus('current')
npIoSinglePulseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 25500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseDuration.setStatus('current')
npIoSinglePulseStart = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseStart.setStatus('current')
npIoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2))
npIoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0))
npIoTrapLineN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLineN.setStatus('current')
npIoTrapLevelIn = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn.setStatus('current')
npIoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapMemo.setStatus('current')
npIoTrapLevelLegend = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelLegend.setStatus('current')
npIoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)).setObjects(("DKSF-70-6-X-X-1", "npIoTrapLineN"), ("DKSF-70-6-X-X-1", "npIoTrapLevelIn"), ("DKSF-70-6-X-X-1", "npIoTrapMemo"), ("DKSF-70-6-X-X-1", "npIoTrapLevelLegend"))
if mibBuilder.loadTexts: npIoTrap.setStatus('current')
npCurLoop = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300))
npCurLoopTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8300, 1), )
if mibBuilder.loadTexts: npCurLoopTable.setStatus('current')
npCurLoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1), ).setIndexNames((0, "DKSF-70-6-X-X-1", "npCurLoopN"))
if mibBuilder.loadTexts: npCurLoopEntry.setStatus('current')
npCurLoopN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopN.setStatus('current')
npCurLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 0), ("alert", 1), ("cut", 2), ("short", 3), ("notPowered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopStatus.setStatus('current')
npCurLoopI = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopI.setStatus('current')
npCurLoopV = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopV.setStatus('current')
npCurLoopR = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopR.setStatus('current')
npCurLoopPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cyclePower", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npCurLoopPower.setStatus('current')
npCurLoopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300, 2))
npCurLoopTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0))
npCurLoopTrapN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapN.setStatus('current')
npCurLoopTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 0), ("alert", 1), ("cut", 2), ("short", 3), ("notPowered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapStatus.setStatus('current')
npCurLoopTrapI = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapI.setStatus('current')
npCurLoopTrapV = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapV.setStatus('current')
npCurLoopTrapR = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapR.setStatus('current')
npCurLoopTrapPower = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npCurLoopTrapPower.setStatus('current')
npCurLoopTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0, 1)).setObjects(("DKSF-70-6-X-X-1", "npCurLoopTrapN"), ("DKSF-70-6-X-X-1", "npCurLoopTrapStatus"), ("DKSF-70-6-X-X-1", "npCurLoopTrapI"), ("DKSF-70-6-X-X-1", "npCurLoopTrapV"), ("DKSF-70-6-X-X-1", "npCurLoopTrapR"), ("DKSF-70-6-X-X-1", "npCurLoopTrapPower"), ("DKSF-70-6-X-X-1", "npTrapEmailTo"))
if mibBuilder.loadTexts: npCurLoopTrap.setStatus('current')
npSmoke = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8200))
npSmokeTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8200, 1), )
if mibBuilder.loadTexts: npSmokeTable.setStatus('current')
npSmokeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1), ).setIndexNames((0, "DKSF-70-6-X-X-1", "npSmokeSensorN"))
if mibBuilder.loadTexts: npSmokeEntry.setStatus('current')
npSmokeSensorN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npSmokeSensorN.setStatus('current')
npSmokeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 4, 5))).clone(namedValues=NamedValues(("ok", 0), ("alarm", 1), ("off", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npSmokeStatus.setStatus('current')
npSmokePower = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSmokePower.setStatus('current')
npSmokeReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSmokeReset.setStatus('current')
npSmokeMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npSmokeMemo.setStatus('current')
npSmokeTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8200, 2))
npSmokeTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8200, 2, 0))
npSmokeTrapSensorN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8200, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npSmokeTrapSensorN.setStatus('current')
npSmokeTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8200, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 4, 5))).clone(namedValues=NamedValues(("ok", 0), ("alarm", 1), ("off", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npSmokeTrapStatus.setStatus('current')
npSmokeTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8200, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npSmokeTrapMemo.setStatus('current')
npSmokeTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8200, 2, 0, 1)).setObjects(("DKSF-70-6-X-X-1", "npSmokeTrapSensorN"), ("DKSF-70-6-X-X-1", "npSmokeTrapStatus"), ("DKSF-70-6-X-X-1", "npSmokeTrapMemo"))
if mibBuilder.loadTexts: npSmokeTrap.setStatus('current')
npRelHumidity = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400))
npRelHumTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8400, 1), )
if mibBuilder.loadTexts: npRelHumTable.setStatus('current')
npRelHumEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1), ).setIndexNames((0, "DKSF-70-6-X-X-1", "npRelHumN"))
if mibBuilder.loadTexts: npRelHumEntry.setStatus('current')
npRelHumN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumN.setStatus('current')
npRelHumValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumValue.setStatus('current')
npRelHumStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sensorFailed", 0), ("belowSafeRange", 1), ("inSafeRange", 2), ("aboveSafeRange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumStatus.setStatus('current')
npRelHumTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTempValue.setStatus('current')
npRelHumTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sensorFailed", 0), ("belowSafeRange", 1), ("inSafeRange", 2), ("aboveSafeRange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTempStatus.setStatus('current')
npRelHumMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumMemo.setStatus('current')
npRelHumSafeRangeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeHigh.setStatus('current')
npRelHumSafeRangeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeLow.setStatus('current')
npRelHumTempSafeRangeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-55, 150))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTempSafeRangeHigh.setStatus('current')
npRelHumTempSafeRangeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-55, 150))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTempSafeRangeLow.setStatus('current')
npRelHumTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 3))
npRelHumTrapDataN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTrapDataN.setStatus('current')
npRelHumTrapDataValue = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTrapDataValue.setStatus('current')
npRelHumTrapDataStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sensorFailed", 0), ("belowSafeRange", 1), ("inSafeRange", 2), ("aboveSafeRange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTrapDataStatus.setStatus('current')
npRelHumTrapDataMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTrapDataMemo.setStatus('current')
npRelHumTrapDataSafeRangeHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTrapDataSafeRangeHigh.setStatus('current')
npRelHumTrapDataSafeRangeLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumTrapDataSafeRangeLow.setStatus('current')
npRelHumTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 6))
npRelHumTrapAllEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 6, 127))
npRelHumTrapTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 7))
npRelHumTrapTempAllEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 7, 127))
npRelHumTrapAllChannels = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 6, 127, 99)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapAllChannels.setStatus('current')
npRelHumTrapAboveSafe = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 6, 103)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapAboveSafe.setStatus('current')
npRelHumTrapSafe = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 6, 102)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapSafe.setStatus('current')
npRelHumTrapBelowSafe = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 6, 101)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapBelowSafe.setStatus('current')
npRelHumTrapFail = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 6, 100)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapFail.setStatus('current')
npRelHumTrapTempAllChannels = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 7, 127, 99)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapTempAllChannels.setStatus('current')
npRelHumTrapTempAboveSafe = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 7, 103)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapTempAboveSafe.setStatus('current')
npRelHumTrapTempSafe = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 7, 102)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapTempSafe.setStatus('current')
npRelHumTrapTempBelowSafe = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 7, 101)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapTempBelowSafe.setStatus('current')
npRelHumTrapTempFail = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 7, 100)).setObjects(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"), ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrapTempFail.setStatus('current')
npGsm = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800))
npGsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 1))
npGsmFailed = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ok", 0), ("failed", 1), ("fatalError", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmFailed.setStatus('current')
npGsmRegistration = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))).clone(namedValues=NamedValues(("impossible", 0), ("homeNetwork", 1), ("searching", 2), ("denied", 3), ("unknown", 4), ("roaming", 5), ("infoUpdate", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmRegistration.setStatus('current')
npGsmStrength = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmStrength.setStatus('current')
npGsmSendSmsUtf8 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npGsmSendSmsUtf8.setStatus('current')
npGsmSendSmsWin1251 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npGsmSendSmsWin1251.setStatus('current')
npGsmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2))
npGsmTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0))
npGsmTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)).setObjects(("DKSF-70-6-X-X-1", "npGsmFailed"), ("DKSF-70-6-X-X-1", "npGsmRegistration"), ("DKSF-70-6-X-X-1", "npGsmStrength"))
if mibBuilder.loadTexts: npGsmTrap.setStatus('current')
npIr = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900))
npIrCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900, 1))
npIrPlayCmd = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrPlayCmd.setStatus('current')
npIrReset = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrReset.setStatus('current')
npIrStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("commandCompleted", 0), ("protocolError", 1), ("commandAccepted", 2), ("errorUnknown", 16), ("errorBadNumber", 17), ("errorEmptyRecord", 18), ("errorFlashChip", 19), ("errorTimeout", 20), ("errorExtBusBusy", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIrStatus.setStatus('current')
npReboot = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 911))
npSoftReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSoftReboot.setStatus('current')
npResetStack = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npResetStack.setStatus('current')
npForcedReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npForcedReboot.setStatus('current')
mibBuilder.exportSymbols("DKSF-70-6-X-X-1", npRelHumTrapDataStatus=npRelHumTrapDataStatus, npCurLoopTrapPrefix=npCurLoopTrapPrefix, npSmokeEntry=npSmokeEntry, npRelHumTrapTempAllEvents=npRelHumTrapTempAllEvents, npThermoMemo=npThermoMemo, npThermoEntry=npThermoEntry, npThermoHigh=npThermoHigh, npRelHumTrapDataSafeRangeHigh=npRelHumTrapDataSafeRangeHigh, npIoTrapLineN=npIoTrapLineN, npIoLineN=npIoLineN, npGsmSendSmsUtf8=npGsmSendSmsUtf8, npThermoLow=npThermoLow, npGsmTraps=npGsmTraps, npSmokeTrapMemo=npSmokeTrapMemo, npRelHumTrapDataMemo=npRelHumTrapDataMemo, npIoTable=npIoTable, npRelHumSafeRangeHigh=npRelHumSafeRangeHigh, npThermoTrapPrefix=npThermoTrapPrefix, npRelHumTempSafeRangeHigh=npRelHumTempSafeRangeHigh, npRelHumTrapAboveSafe=npRelHumTrapAboveSafe, npRelHumN=npRelHumN, npRelHumTrapFail=npRelHumTrapFail, npThermoSensorN=npThermoSensorN, npRelHumValue=npRelHumValue, npRelHumTempStatus=npRelHumTempStatus, npResetStack=npResetStack, npRelayEntry=npRelayEntry, npIoTrapLevelLegend=npIoTrapLevelLegend, npSmokeStatus=npSmokeStatus, npSmokeTrapSensorN=npSmokeTrapSensorN, npSmokeReset=npSmokeReset, npIrCtrl=npIrCtrl, npThermoTrapMemo=npThermoTrapMemo, npRelayMode=npRelayMode, npIoPulseCounter=npIoPulseCounter, npRelHumMemo=npRelHumMemo, npRelHumTrapTempSafe=npRelHumTrapTempSafe, npThermoStatus=npThermoStatus, npSmokeTrap=npSmokeTrap, npCurLoopTrapStatus=npCurLoopTrapStatus, npRelHumTrapDataValue=npRelHumTrapDataValue, npRelHumTempValue=npRelHumTempValue, npGsmSendSmsWin1251=npGsmSendSmsWin1251, npForcedReboot=npForcedReboot, npIoSinglePulseStart=npIoSinglePulseStart, npRelHumTrapTempAboveSafe=npRelHumTrapTempAboveSafe, npTrapInfo=npTrapInfo, npThermo=npThermo, npGsmRegistration=npGsmRegistration, npRelay=npRelay, FixedPoint1000=FixedPoint1000, npThermoValuePrecise=npThermoValuePrecise, npIrStatus=npIrStatus, npCurLoopTrapPower=npCurLoopTrapPower, npSmokePower=npSmokePower, npRelHumTrapAllEvents=npRelHumTrapAllEvents, npCurLoopTraps=npCurLoopTraps, npRelHumTable=npRelHumTable, npCurLoopEntry=npCurLoopEntry, npRelHumTrap=npRelHumTrap, npIoLevelIn=npIoLevelIn, npCurLoopI=npCurLoopI, npGsmTrapPrefix=npGsmTrapPrefix, npRelayStartReset=npRelayStartReset, npCurLoopStatus=npCurLoopStatus, npRelHumTrapSafe=npRelHumTrapSafe, npThermoValue=npThermoValue, npThermoTrapHigh=npThermoTrapHigh, npCurLoopTrapN=npCurLoopTrapN, npRelayN=npRelayN, npRelHumStatus=npRelHumStatus, npRelHumTrapDataN=npRelHumTrapDataN, npCurLoopTrapI=npCurLoopTrapI, npIo=npIo, npCurLoopTrapR=npCurLoopTrapR, npThermoTrapLow=npThermoTrapLow, npIrPlayCmd=npIrPlayCmd, npReboot=npReboot, npRelHumTrapTempFail=npRelHumTrapTempFail, npIoTrap=npIoTrap, npRelHumTrapTempBelowSafe=npRelHumTrapTempBelowSafe, npSmokeTraps=npSmokeTraps, npRelayTable=npRelayTable, npIoMemo=npIoMemo, npRelHumTrapData=npRelHumTrapData, npThermoTraps=npThermoTraps, npGsmInfo=npGsmInfo, npIoSinglePulseDuration=npIoSinglePulseDuration, npIoTraps=npIoTraps, npSmokeMemo=npSmokeMemo, npThermoTrapStatus=npThermoTrapStatus, npCurLoopTrap=npCurLoopTrap, npIrReset=npIrReset, npRelHumTrapBelowSafe=npRelHumTrapBelowSafe, npRelHumTrapTempAllChannels=npRelHumTrapTempAllChannels, npRelHumTrapDataSafeRangeLow=npRelHumTrapDataSafeRangeLow, uniPingServerSolutionV3=uniPingServerSolutionV3, npCurLoopPower=npCurLoopPower, npTrapEmailTo=npTrapEmailTo, PYSNMP_MODULE_ID=uniPingServerSolutionV3, npRelHumSafeRangeLow=npRelHumSafeRangeLow, npCurLoopTrapV=npCurLoopTrapV, npRelayMemo=npRelayMemo, npSmokeTrapPrefix=npSmokeTrapPrefix, npSmoke=npSmoke, lightcom=lightcom, npCurLoop=npCurLoop, npSoftReboot=npSoftReboot, npThermoTable=npThermoTable, npSmokeTable=npSmokeTable, npCurLoopR=npCurLoopR, npCurLoopN=npCurLoopN, npCurLoopTable=npCurLoopTable, npIoLevelOut=npIoLevelOut, npIoTrapLevelIn=npIoTrapLevelIn, npGsm=npGsm, npRelayState=npRelayState, npIoEntry=npIoEntry, npIoTrapPrefix=npIoTrapPrefix, npCurLoopV=npCurLoopV, npSmokeTrapStatus=npSmokeTrapStatus, npThermoTrap=npThermoTrap, npRelHumEntry=npRelHumEntry, npThermoTrapSensorN=npThermoTrapSensorN, npSmokeSensorN=npSmokeSensorN, npRelHumTempSafeRangeLow=npRelHumTempSafeRangeLow, npGsmStrength=npGsmStrength, npIoTrapMemo=npIoTrapMemo, npGsmFailed=npGsmFailed, npRelHumTrapTemp=npRelHumTrapTemp, npRelHumidity=npRelHumidity, npGsmTrap=npGsmTrap, npIr=npIr, npRelHumTrapAllChannels=npRelHumTrapAllChannels, npThermoTrapValue=npThermoTrapValue)
