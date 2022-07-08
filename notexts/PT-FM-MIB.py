#
# PySNMP MIB module PT-FM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-FM-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:37 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, ModuleIdentity, TimeTicks, NotificationType, MibIdentifier, ObjectIdentity, IpAddress, Counter64, Gauge32, Unsigned32, Bits, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "Unsigned32", "Bits", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
ptFM = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 3))
ptFM.setRevisions(('2016-03-21 12:00', '2016-03-09 12:00', '2016-02-10 12:30',))
if mibBuilder.loadTexts: ptFM.setLastUpdated('201603211200Z')
if mibBuilder.loadTexts: ptFM.setOrganization('Ericsson')
config = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1))
alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2))
log = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3))
ptFMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4))
class NotificationIdTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class MoClassTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class SeverityTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("eINDETERMINATE", 1), ("eCRITICAL", 2), ("eMAJOR", 3), ("eMINOR", 4), ("eWARNING", 5), ("eCLEARED", 6))

class ProbableCauseTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class CategoryTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("eHIGHORDERLEVEL", 1), ("eUNFILTERED", 2), ("eLOWORDERLEVEL", 3), ("eNONE", 4))

class ClearableTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eTRUE", 1), ("eFALSE", 2))

class EnableStatusTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eENABLED", 1), ("eDISABLED", 2))

class LayerRateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 4, 5, 7, 11, 13, 15, 16, 20, 21, 22, 25, 26, 27, 73, 74, 76, 87, 98, 99))
    namedValues = NamedValues(("eLRNOTAPPLICABLE", 1), ("eLRT3ANDDS345M", 4), ("eLRE12M", 5), ("eLRE334M", 7), ("eLRVT2ANDTU12VC12", 11), ("eLRLOWORDERTU3VC3", 13), ("eLRSTS3CANDAU4VC4", 15), ("eLRSTS12CVC44C", 16), ("eLRSECTIONOC3STS3ANDRSSTM1", 20), ("eLRSECTIONOC12STS12ANDRSSTM4", 21), ("eLRSECTIONOC48STS48ANDRSSTM16", 22), ("eLRLINEOC3STS3ANDMSSTM1", 25), ("eLRLINEOC12STS12ANDMSSTM4", 26), ("eLRLINEOC48STS48ANDMSSTM16", 27), ("eLRDSROC3STM1", 73), ("eLRDSROC12STM4", 74), ("eLRDSROC48STM16", 76), ("eLRDSRGIGABITETHERNET", 87), ("eLRENCAPSULATION", 98), ("eLRFRAGMENT", 99))

class EventTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eINFORMATION", 1), ("eWARNING", 2))

class EventCauseTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class SwitchTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("eSDHMSP", 1), ("eSDHSNCP", 2), ("eEQUIPEMEMTPROTECTION", 3), ("eSYNCHRONISATION", 4), ("eSCSWITCHOVER", 5))

class SwitchReasonTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("eNA", 1), ("eRESTORED", 2), ("eSIGNALFAIL", 3), ("eSIGNALMISMATCH", 4), ("eSIGNALDEGRADE", 5), ("eAUTOMATICSWITCH", 6), ("eMANUAL", 7), ("eREMOTEREQUEST", 8), ("ePROTECTIONDISABLED", 9), ("eMODULEFAIL", 10))

alarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1), )
if mibBuilder.loadTexts: alarmConfigTable.setStatus('current')
alarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1), ).setIndexNames((0, "PT-FM-MIB", "notificationId"), (0, "PT-FM-MIB", "moClass"))
if mibBuilder.loadTexts: alarmConfigEntry.setStatus('current')
notificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 1), NotificationIdTC())
if mibBuilder.loadTexts: notificationId.setStatus('current')
moClass = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 2), MoClassTC())
if mibBuilder.loadTexts: moClass.setStatus('current')
severity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 3), SeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: severity.setStatus('current')
probableCauseQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probableCauseQualifier.setStatus('current')
probableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 5), ProbableCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probableCause.setStatus('current')
category = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 6), CategoryTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: category.setStatus('current')
clearable = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 7), ClearableTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clearable.setStatus('current')
alarmPersistencyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2), )
if mibBuilder.loadTexts: alarmPersistencyConfigTable.setStatus('current')
alarmPersistencyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1), ).setIndexNames((0, "PT-FM-MIB", "category"))
if mibBuilder.loadTexts: alarmPersistencyConfigEntry.setStatus('current')
persistencyConfigcategory = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1, 1), CategoryTC())
if mibBuilder.loadTexts: persistencyConfigcategory.setStatus('current')
onFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: onFilter.setStatus('current')
offFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: offFilter.setStatus('current')
notificationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3))
notificationReporting = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 1), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationReporting.setStatus('current')
lCASExtendedAlarms = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 2), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lCASExtendedAlarms.setStatus('current')
nIMAlarms = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 3), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nIMAlarms.setStatus('current')
pJEAlarms = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 4), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pJEAlarms.setStatus('current')
currentAlarmsTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1), )
if mibBuilder.loadTexts: currentAlarmsTable.setStatus('current')
currentAlarmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1), ).setIndexNames((0, "PT-FM-MIB", "sequenceNumber"))
if mibBuilder.loadTexts: currentAlarmsEntry.setStatus('current')
sequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: sequenceNumber.setStatus('current')
currentAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmTimeStamp.setStatus('current')
currentAlarmNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmNotificationId.setStatus('current')
currentAlarmManagedObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmManagedObjectId.setStatus('current')
currentAlarmReferenceObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmReferenceObjectId.setStatus('current')
currentAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 6), SeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmSeverity.setStatus('current')
currentAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 7), ProbableCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmProbableCause.setStatus('current')
currentAlarmProbableCauseQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmProbableCauseQualifier.setStatus('current')
currentAlarmAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmAdditionalText.setStatus('current')
currentAlarmLayerRate = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 10), LayerRateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmLayerRate.setStatus('current')
alarmLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1))
maxNumOfEntriesForAlarm = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForAlarm.setStatus('current')
lastSeqNumForAlarm = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForAlarm.setStatus('current')
alarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3), )
if mibBuilder.loadTexts: alarmLogTable.setStatus('current')
alarmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "alarmLogSequenceNumber"))
if mibBuilder.loadTexts: alarmLogEntry.setStatus('current')
alarmLogSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: alarmLogSequenceNumber.setStatus('current')
alarmLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogTimeStamp.setStatus('current')
alarmLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogNotificationId.setStatus('current')
alarmLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 4), SeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogSeverity.setStatus('current')
alarmLogProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 5), ProbableCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogProbableCause.setStatus('current')
alarmLogProbableCauseQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogProbableCauseQualifier.setStatus('current')
alarmLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogAdditionalText.setStatus('current')
alarmLogLayerRate = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 8), LayerRateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogLayerRate.setStatus('current')
tmnNotificationLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2))
maxNumOfEntriesForTMN = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForTMN.setStatus('current')
lastSeqNumForTMN = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForTMN.setStatus('current')
tmnNotificationLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3), )
if mibBuilder.loadTexts: tmnNotificationLogTable.setStatus('current')
tmnNotificationLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "tmnSequenceNumber"))
if mibBuilder.loadTexts: tmnNotificationLogEntry.setStatus('current')
tmnSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: tmnSequenceNumber.setStatus('current')
tmnTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnTimeStamp.setStatus('current')
tmnNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnNotificationId.setStatus('current')
tmnAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnAdditionalText.setStatus('current')
eventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3))
maxNumOfEntriesForEvent = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForEvent.setStatus('current')
lastSeqNumForEvent = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForEvent.setStatus('current')
eventLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3), )
if mibBuilder.loadTexts: eventLogTable.setStatus('current')
eventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "eventLogSequenceNumber"))
if mibBuilder.loadTexts: eventLogEntry.setStatus('current')
eventLogSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: eventLogSequenceNumber.setStatus('current')
eventLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogTimeStamp.setStatus('current')
eventLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogNotificationId.setStatus('current')
eventType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 4), EventTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('current')
eventLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogAdditionalText.setStatus('current')
eventCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 6), EventCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCause.setStatus('current')
protectionSwitchLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4))
maxNumOfEntriesForSwitch = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForSwitch.setStatus('current')
lastSeqNumForSwitch = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForSwitch.setStatus('current')
protectionSwitchLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3), )
if mibBuilder.loadTexts: protectionSwitchLogTable.setStatus('current')
protectionSwitchLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "switchLogSequenceNumber"))
if mibBuilder.loadTexts: protectionSwitchLogEntry.setStatus('current')
switchLogSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: switchLogSequenceNumber.setStatus('current')
switchLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchLogTimeStamp.setStatus('current')
switchLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchLogNotificationId.setStatus('current')
switchType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 4), SwitchTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchType.setStatus('current')
switchLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchLogAdditionalText.setStatus('current')
switchReason = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 6), SwitchReasonTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchReason.setStatus('current')
ptFMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 1))
ptFMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 2))
ptFMFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 1, 1)).setObjects(("PT-FM-MIB", "ptFMCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptFMFullCompliance = ptFMFullCompliance.setStatus('current')
ptFMCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 2, 1)).setObjects(("PT-FM-MIB", "alarmLogTimeStamp"), ("PT-FM-MIB", "alarmLogNotificationId"), ("PT-FM-MIB", "alarmLogSeverity"), ("PT-FM-MIB", "alarmLogProbableCause"), ("PT-FM-MIB", "alarmLogProbableCauseQualifier"), ("PT-FM-MIB", "alarmLogAdditionalText"), ("PT-FM-MIB", "alarmLogLayerRate"), ("PT-FM-MIB", "category"), ("PT-FM-MIB", "clearable"), ("PT-FM-MIB", "currentAlarmTimeStamp"), ("PT-FM-MIB", "currentAlarmNotificationId"), ("PT-FM-MIB", "currentAlarmManagedObjectId"), ("PT-FM-MIB", "currentAlarmReferenceObjectId"), ("PT-FM-MIB", "currentAlarmSeverity"), ("PT-FM-MIB", "currentAlarmProbableCause"), ("PT-FM-MIB", "currentAlarmProbableCauseQualifier"), ("PT-FM-MIB", "currentAlarmAdditionalText"), ("PT-FM-MIB", "currentAlarmLayerRate"), ("PT-FM-MIB", "eventLogTimeStamp"), ("PT-FM-MIB", "eventLogNotificationId"), ("PT-FM-MIB", "eventType"), ("PT-FM-MIB", "eventLogAdditionalText"), ("PT-FM-MIB", "eventCause"), ("PT-FM-MIB", "lastSeqNumForAlarm"), ("PT-FM-MIB", "lastSeqNumForTMN"), ("PT-FM-MIB", "lastSeqNumForEvent"), ("PT-FM-MIB", "lastSeqNumForSwitch"), ("PT-FM-MIB", "lCASExtendedAlarms"), ("PT-FM-MIB", "maxNumOfEntriesForAlarm"), ("PT-FM-MIB", "maxNumOfEntriesForTMN"), ("PT-FM-MIB", "maxNumOfEntriesForEvent"), ("PT-FM-MIB", "maxNumOfEntriesForSwitch"), ("PT-FM-MIB", "notificationReporting"), ("PT-FM-MIB", "nIMAlarms"), ("PT-FM-MIB", "onFilter"), ("PT-FM-MIB", "offFilter"), ("PT-FM-MIB", "pJEAlarms"), ("PT-FM-MIB", "probableCauseQualifier"), ("PT-FM-MIB", "probableCause"), ("PT-FM-MIB", "severity"), ("PT-FM-MIB", "switchLogTimeStamp"), ("PT-FM-MIB", "switchLogNotificationId"), ("PT-FM-MIB", "switchType"), ("PT-FM-MIB", "switchLogAdditionalText"), ("PT-FM-MIB", "switchReason"), ("PT-FM-MIB", "tmnTimeStamp"), ("PT-FM-MIB", "tmnNotificationId"), ("PT-FM-MIB", "tmnAdditionalText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptFMCompleteGroup = ptFMCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-FM-MIB", category=category, protectionSwitchLogEntry=protectionSwitchLogEntry, protectionSwitchLog=protectionSwitchLog, eventCause=eventCause, alarmLog=alarmLog, alarmLogEntry=alarmLogEntry, switchLogTimeStamp=switchLogTimeStamp, tmnAdditionalText=tmnAdditionalText, eventLogEntry=eventLogEntry, probableCause=probableCause, currentAlarmProbableCause=currentAlarmProbableCause, pJEAlarms=pJEAlarms, currentAlarmManagedObjectId=currentAlarmManagedObjectId, maxNumOfEntriesForSwitch=maxNumOfEntriesForSwitch, lCASExtendedAlarms=lCASExtendedAlarms, alarmLogAdditionalText=alarmLogAdditionalText, tmnNotificationLogEntry=tmnNotificationLogEntry, ptFM=ptFM, MoClassTC=MoClassTC, severity=severity, lastSeqNumForTMN=lastSeqNumForTMN, ptFMCompleteGroup=ptFMCompleteGroup, eventLogTable=eventLogTable, CategoryTC=CategoryTC, moClass=moClass, switchLogNotificationId=switchLogNotificationId, eventType=eventType, EventTypeTC=EventTypeTC, currentAlarmSeverity=currentAlarmSeverity, PYSNMP_MODULE_ID=ptFM, clearable=clearable, alarmLogTable=alarmLogTable, EnableStatusTypeTC=EnableStatusTypeTC, currentAlarmsTable=currentAlarmsTable, eventLogTimeStamp=eventLogTimeStamp, ProbableCauseTC=ProbableCauseTC, currentAlarmsEntry=currentAlarmsEntry, log=log, probableCauseQualifier=probableCauseQualifier, switchLogSequenceNumber=switchLogSequenceNumber, SwitchTypeTC=SwitchTypeTC, persistencyConfigcategory=persistencyConfigcategory, tmnNotificationId=tmnNotificationId, maxNumOfEntriesForEvent=maxNumOfEntriesForEvent, config=config, lastSeqNumForEvent=lastSeqNumForEvent, ptFMGroups=ptFMGroups, notificationConfig=notificationConfig, notificationReporting=notificationReporting, nIMAlarms=nIMAlarms, maxNumOfEntriesForAlarm=maxNumOfEntriesForAlarm, maxNumOfEntriesForTMN=maxNumOfEntriesForTMN, currentAlarmNotificationId=currentAlarmNotificationId, alarmPersistencyConfigTable=alarmPersistencyConfigTable, ptFMFullCompliance=ptFMFullCompliance, NotificationIdTC=NotificationIdTC, currentAlarmAdditionalText=currentAlarmAdditionalText, switchReason=switchReason, EventCauseTC=EventCauseTC, switchLogAdditionalText=switchLogAdditionalText, onFilter=onFilter, tmnNotificationLogTable=tmnNotificationLogTable, alarmLogTimeStamp=alarmLogTimeStamp, eventLog=eventLog, ptFMCompliances=ptFMCompliances, eventLogNotificationId=eventLogNotificationId, alarmLogSeverity=alarmLogSeverity, alarmPersistencyConfigEntry=alarmPersistencyConfigEntry, offFilter=offFilter, alarm=alarm, sequenceNumber=sequenceNumber, ClearableTC=ClearableTC, ptFMConformance=ptFMConformance, alarmLogSequenceNumber=alarmLogSequenceNumber, SwitchReasonTC=SwitchReasonTC, currentAlarmReferenceObjectId=currentAlarmReferenceObjectId, tmnTimeStamp=tmnTimeStamp, notificationId=notificationId, eventLogAdditionalText=eventLogAdditionalText, currentAlarmTimeStamp=currentAlarmTimeStamp, alarmLogLayerRate=alarmLogLayerRate, currentAlarmProbableCauseQualifier=currentAlarmProbableCauseQualifier, eventLogSequenceNumber=eventLogSequenceNumber, alarmLogProbableCause=alarmLogProbableCause, switchType=switchType, SeverityTC=SeverityTC, alarmConfigTable=alarmConfigTable, lastSeqNumForAlarm=lastSeqNumForAlarm, tmnNotificationLog=tmnNotificationLog, lastSeqNumForSwitch=lastSeqNumForSwitch, tmnSequenceNumber=tmnSequenceNumber, protectionSwitchLogTable=protectionSwitchLogTable, currentAlarmLayerRate=currentAlarmLayerRate, alarmConfigEntry=alarmConfigEntry, LayerRateTC=LayerRateTC, alarmLogNotificationId=alarmLogNotificationId, alarmLogProbableCauseQualifier=alarmLogProbableCauseQualifier)
