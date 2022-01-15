#
# PySNMP MIB module SL-TESTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TESTS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfTotalCount, PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfCurrentCount", "PerfIntervalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, Counter64, iso, Integer32, NotificationType, Bits, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "iso", "Integer32", "NotificationType", "Bits", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32")
RowStatus, TruthValue, TextualConvention, TimeStamp, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "TimeStamp", "DisplayString", "DateAndTime")
slTests = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13))
if mibBuilder.loadTexts: slTests.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: slTests.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slTests.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slTests.setDescription('This MIB module describes the available on-demand tests.')
slTestsIfLoop = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1))
slTestsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2))
slTestsTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 0))
slTestsIfLoopTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1), )
if mibBuilder.loadTexts: slTestsIfLoopTable.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopTable.setDescription('The port loopback test table. This table controls the \n\t\tport loopback tests.')
slTestsIfLoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1), ).setIndexNames((0, "SL-TESTS-MIB", "slTestsIfLoopIfIndex"))
if mibBuilder.loadTexts: slTestsIfLoopEntry.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopEntry.setDescription('This entry is used to operate an port loopback test.')
slTestsIfLoopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopIfIndex.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopIfIndex.setDescription('The Interface Index of the port that should be loopped back.')
slTestsIfLoopDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopDuration.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopDuration.setDescription('The test duration in 1/10 Sec. The maximum allowed\n\t\tduration is 1 hour. After this time the port configuration\n\t\treturns to its original setting and the Agent automatically\n\t\tdeletes the entry from the table.')
slTestsIfLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("start", 1), ("stop", 2), ("fail", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopStatus.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopStatus.setDescription('This variable is used to start or stop a loopback test.\n\t\tIn order to start a test the NMS should set the value to start(1).\n\t\tIf the test mode is toggle, the NMS should stop the test by setting the value\n\t\tto stop(2).\n\t\tIn the case of prbs test, after the test has stopped, \n\t\tif the test fails the value of the status shall be fail(3).')
slTestsIfLoopType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("terminal", 1), ("facility", 2), ("prbs", 3), ("otnPrbs", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopType.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopType.setDescription('The loopback type:\n          facility\n             The received signal at this interface is looped back\n             out through the corresponding transmitter in the return\n             direction.\n          terminal \n             The signal that is about to be transmitted is connected\n             to the associated incoming receiver.\n          prbs \n             send and recieve prbs pattern.\n          otnPrbs\n          \t send and receive OTN prbs')
slTestsIfLoopMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("timeout", 1), ("toggle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slTestsIfLoopMode.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopMode.setDescription('The loopback mode:\n          timeout\n             In this mode the duration of the loopback is determined\n             by the slTestsIfLoopDuration object.\n          toggle     \n             In this mode the loopback should be toggled explicitly\n             by the user.')
slTestsIfLoopErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopErrors.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopErrors.setDescription('The prbs errors are counted only of the test succeeded.')
slTestsIfLoopResult = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopResult.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopResult.setDescription('This variable is used for prbs test result indication.')
slTestsIfLoopPassedSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsIfLoopPassedSeconds.setStatus('current')
if mibBuilder.loadTexts: slTestsIfLoopPassedSeconds.setDescription('Number of seconds passed since the test started.')
slTestsTrapsLoopbackActive = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slTestsTrapsLoopbackActive.setStatus('current')
if mibBuilder.loadTexts: slTestsTrapsLoopbackActive.setDescription('The Loopback is active Yes/No.')
slTestsTrapsLoopbackTableChanged = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 2)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
if mibBuilder.loadTexts: slTestsTrapsLoopbackTableChanged.setStatus('current')
if mibBuilder.loadTexts: slTestsTrapsLoopbackTableChanged.setDescription('A slTestsTrapsLoopbackTableChanged trap is sent when the\n\t\tcontent of slTestsIfLoopTable changes. When the loop back is deleted\n\t\tthe returned value of slTestsIfLoopActivity should be false.')
slTestsTrapsLoopbackTableChanged0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 0, 2)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
if mibBuilder.loadTexts: slTestsTrapsLoopbackTableChanged0.setStatus('current')
if mibBuilder.loadTexts: slTestsTrapsLoopbackTableChanged0.setDescription('A slTestsTrapsLoopbackTableChanged trap is sent when the\n\t\tcontent of slTestsIfLoopTable changes. When the loop back is deleted\n\t\tthe returned value of slTestsIfLoopActivity should be false.')
mibBuilder.exportSymbols("SL-TESTS-MIB", slTestsIfLoopIfIndex=slTestsIfLoopIfIndex, slTestsIfLoopDuration=slTestsIfLoopDuration, slTestsIfLoopPassedSeconds=slTestsIfLoopPassedSeconds, slTestsTrapsLoopbackActive=slTestsTrapsLoopbackActive, slTests=slTests, PYSNMP_MODULE_ID=slTests, slTestsIfLoopType=slTestsIfLoopType, slTestsIfLoopEntry=slTestsIfLoopEntry, slTestsIfLoopMode=slTestsIfLoopMode, slTestsIfLoopStatus=slTestsIfLoopStatus, slTestsTraps0=slTestsTraps0, slTestsIfLoopResult=slTestsIfLoopResult, slTestsTrapsLoopbackTableChanged=slTestsTrapsLoopbackTableChanged, slTestsIfLoopTable=slTestsIfLoopTable, slTestsTraps=slTestsTraps, slTestsIfLoopErrors=slTestsIfLoopErrors, slTestsTrapsLoopbackTableChanged0=slTestsTrapsLoopbackTableChanged0, slTestsIfLoop=slTestsIfLoop)
