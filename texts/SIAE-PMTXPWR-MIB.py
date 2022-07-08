#
# PySNMP MIB module SIAE-PMTXPWR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-PMTXPWR-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:28:18 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, ObjectIdentity, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Unsigned32, Counter64, iso, IpAddress, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Unsigned32", "Counter64", "iso", "IpAddress", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
pmTxPwr = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 13))
pmTxPwr.setRevisions(('2014-10-07 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pmTxPwr.setRevisionsDescriptions(('Changed MAX-ACCESS caluse of some object of pmTxPwrTpClassTable\n             from read-write to read-create\n            ', 'Improved description of pmTxPwrMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: pmTxPwr.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: pmTxPwr.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: pmTxPwr.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: pmTxPwr.setDescription('Performance Monitoring on Transmitted (TX) RF Power.\n            ')
pmTxPwrMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrMibVersion.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
pmTxPwrCounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2), )
if mibBuilder.loadTexts: pmTxPwrCounterTable.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrCounterTable.setDescription('Table with PmTxPwr records: one record for 1+0 configuration and two\n             record for 1+1 configuration.')
pmTxPwrCounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1), ).setIndexNames((0, "SIAE-PMTXPWR-MIB", "pmTxPwrBranchId"), (0, "SIAE-PMTXPWR-MIB", "pmTxPwrCounterBlockId"))
if mibBuilder.loadTexts: pmTxPwrCounterRecord.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrCounterRecord.setDescription('PmTxPwrCounter record.')
pmTxPwrBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrBranchId.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrBranchId.setDescription('This object identifies the Radio Branch')
pmTxPwrCounterBlockId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterBlockId.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrCounterBlockId.setDescription('This object identifies  the counters block and the counter type according to the following code:\n             1   Current Daily counters\n             2   Daily counters (Day before counters)\n             3   Current 15 minutes counters\n             4   15 minutes counters N. 1 (The most recent 15 minutes counters)\n                 ..............................................\n             n   15 minutes counters N. n\n            19   15 minutes counters N. 16 (The oldest 15 minutes counters - 4 hours before).')
pmTxPwrCounterBlockType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteenMin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterBlockType.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrCounterBlockType.setDescription('The type of the counter block.')
pmTxPwrCounterBlockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterBlockStatus.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrCounterBlockStatus.setDescription('block counter status.')
pmTxPwrCounterTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterTimeStamp.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrCounterTimeStamp.setDescription('The object is the time when the performance record is closed reported\n             as the second number since 1-Gen-1970.')
pmTxPwrTlts1Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts1Counter.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTlts1Counter.setDescription('Number of seconds when the Transmitted power is greater than the threshold 1.')
pmTxPwrTlts2Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts2Counter.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTlts2Counter.setDescription('Number of seconds when the Transmitted power is greater than the threshold 2')
pmTxPwrTlts3Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts3Counter.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTlts3Counter.setDescription('Number of seconds when the Transmitted power is greater than the threshold 3')
pmTxPwrTlts4Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts4Counter.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTlts4Counter.setDescription('Number of seconds when the Transmitted power is greater than the threshold 4')
pmTxPwrTMMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTMMax.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTMMax.setDescription('Maximum Transmitted Power Level Tide Mark.')
pmTxPwrTMMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTMMin.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTMMin.setDescription('Minimum  Transmitted Power Level Tide Mark.')
pmTxPwrAverageTxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrAverageTxLevel.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrAverageTxLevel.setDescription(' Power Transmitted  Level  (Average value)')
pmTxPwrTpClassTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3), )
if mibBuilder.loadTexts: pmTxPwrTpClassTable.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassTable.setDescription('Table with PmTxPwrTpClass records: one record for 1+0 configuration and two record\n             for 1+1 configuration.')
pmTxPwrTpClassRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1), ).setIndexNames((0, "SIAE-PMTXPWR-MIB", "pmTxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmTxPwrTpClassRecord.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassRecord.setDescription('PmTxPwrTpClass record.')
pmTxPwrTpClassBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClassBranchId.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassBranchId.setDescription('This object identifies the Radio Branch')
pmTxPwrTpClassStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassStartStop.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassStartStop.setDescription('This object is used to start and to stop the Perfomance Monitoring\n             counter evaluation.')
pmTxPwrTpClassLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClassLabel.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassLabel.setDescription('ASCII string used to identify the Tp class:\n             pmTxPwrTpClassBranchId = 1 label = Radio 1\n             pmTxPwrTpClassBranchId = 2 label = Radio 2.')
pmTxPwrTpClassTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClassTimeStamp.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassTimeStamp.setDescription('The object is the time when the performance record is closed reported\n             as the second number since 1/1/70.')
pmTxPwrTpClass15MTlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts1Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts1Alarm.setDescription('15 minutes Tlts1 threshold cross alarm with associated severity.')
pmTxPwrTpClass15MTlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts2Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts2Alarm.setDescription('15 minutes Tlts2 threshold cross alarm with associated severity.')
pmTxPwrTpClass15MTlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts3Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts3Alarm.setDescription('15 minutes Tlts3 threshold cross alarm with associated severity.')
pmTxPwrTpClass15MTlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts4Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts4Alarm.setDescription('15 minutes Tlts4 threshold cross alarm with associated severity.')
pmTxPwrTpClass24HTlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts1Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts1Alarm.setDescription('Daily Tlts1 threshold cross alarm with associated severity.')
pmTxPwrTpClass24HTlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts2Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts2Alarm.setDescription('Daily Tlts2 threshold cross alarm with associated severity.')
pmTxPwrTpClass24HTlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts3Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts3Alarm.setDescription('Daily Tlts3 threshold cross alarm with associated severity.')
pmTxPwrTpClass24HTlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 12), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts4Alarm.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts4Alarm.setDescription('Daily Tlts4 threshold cross alarm with associated severity.')
pmTxPwrTpClassTlt1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-30)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt1Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassTlt1Threshold.setDescription('Received Power Level Threshold 1 (dBm value); range -100 to -20')
pmTxPwrTpClassTlt2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-40)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt2Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassTlt2Threshold.setDescription('Received Power Level Threshold 2 (dBm value); range -100 to -20')
pmTxPwrTpClassTlt3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt3Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassTlt3Threshold.setDescription('Received Power Level Threshold 3 (dBm value); range -100 to -20')
pmTxPwrTpClassTlt4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt4Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassTlt4Threshold.setDescription('Received Power Level Threshold 4 (dBm value); range -100 to -20')
pmTxPwrTpClass15MTlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts1Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts1Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmTxPwrTpClass15MTlts1Alarm (zero value disables the alarm).')
pmTxPwrTpClass15MTlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 18), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts2Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts2Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmTxPwrTpClass15MTlts2Alarm (zero value disables the alarm).')
pmTxPwrTpClass15MTlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 19), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts3Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts3Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmTxPwrTpClass15MTlts3Alarm (zero value disables the alarm).')
pmTxPwrTpClass15MTlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 20), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts4Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts4Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmTxPwrTpClass15MTlts4Alarm (zero value disables the alarm).')
pmTxPwrTpClass24HTlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 21), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts1Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts1Threshold.setDescription('Number of seconds within a day to set pmTxPwrTpClass24HTlts1Alarm\n             (zero value disables the alarm).')
pmTxPwrTpClass24HTlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 22), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts2Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts2Threshold.setDescription('Number of seconds within a day to set pmTxPwrTpClass24HTlts2Alarm\n             (zero value disables the alarm).')
pmTxPwrTpClass24HTlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 23), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts3Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts3Threshold.setDescription('Number of seconds within a day to set pmTxPwrTpClass24HTlts3Alarm\n             (zero value disables the alarm).')
pmTxPwrTpClass24HTlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 24), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts4Threshold.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts4Threshold.setDescription('Number of seconds within a day to set pmTxPwrTpClass24HTlts4Alarm\n             (zero value disables the alarm).')
pmTxPwrTpClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassRowStatus.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClassRowStatus.setDescription('Status of this row of pmTxPwrTpClass.\n            ')
pmTxPwrTpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4), )
if mibBuilder.loadTexts: pmTxPwrTpMaintTable.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpMaintTable.setDescription('Table with Command for maintenance of Termination Point.\n             Objects in this table is not persistent. An Instance of this \n             table is created on creation of pmTxPwrTpClassTable')
pmTxPwrTpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1), ).setIndexNames((0, "SIAE-PMTXPWR-MIB", "pmTxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmTxPwrTpMaintRecord.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpMaintRecord.setDescription('PmG828 Termination Point Maintenance record.')
pmTxPwrTpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpMaintCounterClear.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpMaintCounterClear.setDescription('This object is used to clear the Perfomance Monitoring counters.')
pmTxPwrTpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpMaintAlarmClear.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpMaintAlarmClear.setDescription('This object is used to clear the Perfomance Monitoring threshold cross alarms.')
pmTxPwrTpClass15MTltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTltsAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass15MTltsAlarmSeverityCode.setDescription('Define the severity associated to the pmTxPwrTpClass15MTltsAlarm\n             and enables/disables the trap generation on status change event.')
pmTxPwrTpClass24HTltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTltsAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmTxPwrTpClass24HTltsAlarmSeverityCode.setDescription('Define the severity associated to the pmTxPwrTpClass24HTltsAlarm\n             and enables/disables the trap generation on status change event.')
mibBuilder.exportSymbols("SIAE-PMTXPWR-MIB", pmTxPwrTpClass24HTlts4Threshold=pmTxPwrTpClass24HTlts4Threshold, pmTxPwrTpClass24HTlts2Alarm=pmTxPwrTpClass24HTlts2Alarm, pmTxPwrCounterRecord=pmTxPwrCounterRecord, pmTxPwrTlts3Counter=pmTxPwrTlts3Counter, pmTxPwrBranchId=pmTxPwrBranchId, pmTxPwrTpClass15MTlts2Alarm=pmTxPwrTpClass15MTlts2Alarm, pmTxPwrTlts4Counter=pmTxPwrTlts4Counter, pmTxPwrTpClass15MTlts3Alarm=pmTxPwrTpClass15MTlts3Alarm, pmTxPwrTlts2Counter=pmTxPwrTlts2Counter, pmTxPwrCounterBlockId=pmTxPwrCounterBlockId, pmTxPwrTpClassLabel=pmTxPwrTpClassLabel, pmTxPwrTpClass24HTlts1Threshold=pmTxPwrTpClass24HTlts1Threshold, pmTxPwrTpClassRecord=pmTxPwrTpClassRecord, pmTxPwrAverageTxLevel=pmTxPwrAverageTxLevel, pmTxPwrTpClass24HTlts1Alarm=pmTxPwrTpClass24HTlts1Alarm, pmTxPwrTpClass15MTlts1Threshold=pmTxPwrTpClass15MTlts1Threshold, pmTxPwrTpMaintAlarmClear=pmTxPwrTpMaintAlarmClear, pmTxPwrTpClass15MTlts3Threshold=pmTxPwrTpClass15MTlts3Threshold, pmTxPwrCounterBlockType=pmTxPwrCounterBlockType, pmTxPwrTMMax=pmTxPwrTMMax, pmTxPwrMibVersion=pmTxPwrMibVersion, pmTxPwrTpClass24HTlts3Alarm=pmTxPwrTpClass24HTlts3Alarm, pmTxPwrTpClassTimeStamp=pmTxPwrTpClassTimeStamp, pmTxPwrTpClassTlt1Threshold=pmTxPwrTpClassTlt1Threshold, pmTxPwrTpClass24HTlts2Threshold=pmTxPwrTpClass24HTlts2Threshold, pmTxPwrTpClassTlt2Threshold=pmTxPwrTpClassTlt2Threshold, pmTxPwrTpClassBranchId=pmTxPwrTpClassBranchId, pmTxPwrTlts1Counter=pmTxPwrTlts1Counter, pmTxPwrTpClass15MTltsAlarmSeverityCode=pmTxPwrTpClass15MTltsAlarmSeverityCode, pmTxPwrTpClassStartStop=pmTxPwrTpClassStartStop, pmTxPwrTpClass24HTltsAlarmSeverityCode=pmTxPwrTpClass24HTltsAlarmSeverityCode, pmTxPwrTpClass15MTlts4Alarm=pmTxPwrTpClass15MTlts4Alarm, pmTxPwr=pmTxPwr, pmTxPwrTpClass15MTlts4Threshold=pmTxPwrTpClass15MTlts4Threshold, pmTxPwrTpClassTlt3Threshold=pmTxPwrTpClassTlt3Threshold, pmTxPwrTpClassTable=pmTxPwrTpClassTable, pmTxPwrTpClass15MTlts1Alarm=pmTxPwrTpClass15MTlts1Alarm, pmTxPwrCounterTable=pmTxPwrCounterTable, pmTxPwrTpClass24HTlts3Threshold=pmTxPwrTpClass24HTlts3Threshold, pmTxPwrTpMaintTable=pmTxPwrTpMaintTable, PYSNMP_MODULE_ID=pmTxPwr, pmTxPwrTpClassRowStatus=pmTxPwrTpClassRowStatus, pmTxPwrTpMaintCounterClear=pmTxPwrTpMaintCounterClear, pmTxPwrTpClass15MTlts2Threshold=pmTxPwrTpClass15MTlts2Threshold, pmTxPwrCounterTimeStamp=pmTxPwrCounterTimeStamp, pmTxPwrCounterBlockStatus=pmTxPwrCounterBlockStatus, pmTxPwrTpClassTlt4Threshold=pmTxPwrTpClassTlt4Threshold, pmTxPwrTpMaintRecord=pmTxPwrTpMaintRecord, pmTxPwrTpClass24HTlts4Alarm=pmTxPwrTpClass24HTlts4Alarm, pmTxPwrTMMin=pmTxPwrTMMin)
