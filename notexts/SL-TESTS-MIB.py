#
# PySNMP MIB module SL-TESTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TESTS-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:38 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfTotalCount, PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfCurrentCount", "PerfIntervalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, TimeTicks, IpAddress, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "TimeTicks", "IpAddress", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter32")
RowStatus, TextualConvention, DateAndTime, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DateAndTime", "TruthValue", "TimeStamp", "DisplayString")
slTests = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13))
if mibBuilder.loadTexts: slTests.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: slTests.setOrganization('PacketLight Networks Ltd.')
slTestsIfLoop = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1))
slTestsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2))
slTestsTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 0))
slTestsIfLoopTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1), )
if mibBuilder.loadTexts: slTestsIfLoopTable.setStatus('current')
slTestsIfLoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1), ).setIndexNames((0, "SL-TESTS-MIB", "slTestsIfLoopIfIndex"))
if mibBuilder.loadTexts: slTestsIfLoopEntry.setStatus('current')
slTestsIfLoopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopIfIndex.setStatus('current')
slTestsIfLoopDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopDuration.setStatus('current')
slTestsIfLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("start", 1), ("stop", 2), ("fail", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopStatus.setStatus('current')
slTestsIfLoopType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("terminal", 1), ("facility", 2), ("prbs", 3), ("otnPrbs", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopType.setStatus('current')
slTestsIfLoopMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("timeout", 1), ("toggle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopMode.setStatus('current')
slTestsIfLoopErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopErrors.setStatus('current')
slTestsIfLoopResult = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopResult.setStatus('current')
slTestsIfLoopPassedSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopPassedSeconds.setStatus('current')
slTestsTrapsLoopbackActive = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsTrapsLoopbackActive.setStatus('current')
slTestsTrapsLoopbackTableChanged = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 2)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
if mibBuilder.loadTexts: slTestsTrapsLoopbackTableChanged.setStatus('current')
slTestsTrapsLoopbackTableChanged0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 0, 2)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
if mibBuilder.loadTexts: slTestsTrapsLoopbackTableChanged0.setStatus('current')
mibBuilder.exportSymbols("SL-TESTS-MIB", slTestsIfLoopStatus=slTestsIfLoopStatus, slTestsIfLoopErrors=slTestsIfLoopErrors, slTestsTrapsLoopbackTableChanged0=slTestsTrapsLoopbackTableChanged0, slTestsTrapsLoopbackActive=slTestsTrapsLoopbackActive, slTestsTraps0=slTestsTraps0, slTests=slTests, slTestsIfLoopType=slTestsIfLoopType, slTestsIfLoopMode=slTestsIfLoopMode, slTestsIfLoopPassedSeconds=slTestsIfLoopPassedSeconds, slTestsTrapsLoopbackTableChanged=slTestsTrapsLoopbackTableChanged, slTestsIfLoopIfIndex=slTestsIfLoopIfIndex, slTestsIfLoop=slTestsIfLoop, slTestsIfLoopResult=slTestsIfLoopResult, slTestsIfLoopEntry=slTestsIfLoopEntry, slTestsIfLoopDuration=slTestsIfLoopDuration, slTestsIfLoopTable=slTestsIfLoopTable, PYSNMP_MODULE_ID=slTests, slTestsTraps=slTestsTraps)
