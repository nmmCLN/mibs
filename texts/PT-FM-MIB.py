#
# PySNMP MIB module PT-FM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-FM-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:39 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, ModuleIdentity, iso, Counter32, ObjectIdentity, Counter64, NotificationType, Gauge32, IpAddress, Integer32, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ModuleIdentity", "iso", "Counter32", "ObjectIdentity", "Counter64", "NotificationType", "Gauge32", "IpAddress", "Integer32", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
ptFM = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 3))
ptFM.setRevisions(('2016-03-21 12:00', '2016-03-09 12:00', '2016-02-10 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ptFM.setRevisionsDescriptions(('Added Managed and Reference OID to the current alarms', 'Validated.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ptFM.setLastUpdated('201603211200Z')
if mibBuilder.loadTexts: ptFM.setOrganization('Ericsson')
if mibBuilder.loadTexts: ptFM.setContactInfo('Anders Ekvall\n             Postal: Ericsson AB,\n             E-Mail: anders.ekvall@ericsson.com')
if mibBuilder.loadTexts: ptFM.setDescription('This is the MIB of PT specifics')
config = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1))
alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2))
log = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3))
ptFMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4))
class NotificationIdTC(TextualConvention, Integer32):
    description = 'Notification ID which is NONE now.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class MoClassTC(TextualConvention, Integer32):
    description = 'Textual Convention for MoClass'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class SeverityTC(TextualConvention, Integer32):
    description = 'An integer indicates the severity level, take the value of INDETERMINATE,\n\t   CRITICAL, MAJOR, MINOR, WARNING and CLEARED. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("eINDETERMINATE", 1), ("eCRITICAL", 2), ("eMAJOR", 3), ("eMINOR", 4), ("eWARNING", 5), ("eCLEARED", 6))

class ProbableCauseTC(TextualConvention, Integer32):
    description = 'Probable Cause'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class CategoryTC(TextualConvention, Integer32):
    description = 'An integer indicates the category. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("eHIGHORDERLEVEL", 1), ("eUNFILTERED", 2), ("eLOWORDERLEVEL", 3), ("eNONE", 4))

class ClearableTC(TextualConvention, Integer32):
    description = 'An integer indicates whether a notification is clearable or not.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eTRUE", 1), ("eFALSE", 2))

class EnableStatusTypeTC(TextualConvention, Integer32):
    description = 'An integer indicates the enable status type: ENABLED or DISABLED. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eENABLED", 1), ("eDISABLED", 2))

class LayerRateTC(TextualConvention, Integer32):
    description = 'An emulation for layer rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 4, 5, 7, 11, 13, 15, 16, 20, 21, 22, 25, 26, 27, 73, 74, 76, 87, 98, 99))
    namedValues = NamedValues(("eLRNOTAPPLICABLE", 1), ("eLRT3ANDDS345M", 4), ("eLRE12M", 5), ("eLRE334M", 7), ("eLRVT2ANDTU12VC12", 11), ("eLRLOWORDERTU3VC3", 13), ("eLRSTS3CANDAU4VC4", 15), ("eLRSTS12CVC44C", 16), ("eLRSECTIONOC3STS3ANDRSSTM1", 20), ("eLRSECTIONOC12STS12ANDRSSTM4", 21), ("eLRSECTIONOC48STS48ANDRSSTM16", 22), ("eLRLINEOC3STS3ANDMSSTM1", 25), ("eLRLINEOC12STS12ANDMSSTM4", 26), ("eLRLINEOC48STS48ANDMSSTM16", 27), ("eLRDSROC3STM1", 73), ("eLRDSROC12STM4", 74), ("eLRDSROC48STM16", 76), ("eLRDSRGIGABITETHERNET", 87), ("eLRENCAPSULATION", 98), ("eLRFRAGMENT", 99))

class EventTypeTC(TextualConvention, Integer32):
    description = 'An integer indicates the event type: INFORMATION or WARNING. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eINFORMATION", 1), ("eWARNING", 2))

class EventCauseTC(TextualConvention, Integer32):
    description = 'An integer indicates the event cause (only NONE is supported).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("eNONE", 0))

class SwitchTypeTC(TextualConvention, Integer32):
    description = 'An integer indicates the switch type. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("eSDHMSP", 1), ("eSDHSNCP", 2), ("eEQUIPEMEMTPROTECTION", 3), ("eSYNCHRONISATION", 4), ("eSCSWITCHOVER", 5))

class SwitchReasonTC(TextualConvention, Integer32):
    description = 'An integer indicates the switch reason. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("eNA", 1), ("eRESTORED", 2), ("eSIGNALFAIL", 3), ("eSIGNALMISMATCH", 4), ("eSIGNALDEGRADE", 5), ("eAUTOMATICSWITCH", 6), ("eMANUAL", 7), ("eREMOTEREQUEST", 8), ("ePROTECTIONDISABLED", 9), ("eMODULEFAIL", 10))

alarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1), )
if mibBuilder.loadTexts: alarmConfigTable.setStatus('current')
if mibBuilder.loadTexts: alarmConfigTable.setDescription('This configuration defines the default severity of an alarm notification.\n            ')
alarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1), ).setIndexNames((0, "PT-FM-MIB", "notificationId"), (0, "PT-FM-MIB", "moClass"))
if mibBuilder.loadTexts: alarmConfigEntry.setStatus('current')
if mibBuilder.loadTexts: alarmConfigEntry.setDescription('An entry containing management information applicable to a\n            particular interface indexed by NotificationId and moClass. ')
notificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 1), NotificationIdTC())
if mibBuilder.loadTexts: notificationId.setStatus('current')
if mibBuilder.loadTexts: notificationId.setDescription('Notification Id')
moClass = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 2), MoClassTC())
if mibBuilder.loadTexts: moClass.setStatus('current')
if mibBuilder.loadTexts: moClass.setDescription('MO Class')
severity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 3), SeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: severity.setStatus('current')
if mibBuilder.loadTexts: severity.setDescription('SeverityTC')
probableCauseQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probableCauseQualifier.setStatus('current')
if mibBuilder.loadTexts: probableCauseQualifier.setDescription('Probable Cause Qualifier')
probableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 5), ProbableCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probableCause.setStatus('current')
if mibBuilder.loadTexts: probableCause.setDescription('Probable Cause')
category = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 6), CategoryTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: category.setStatus('current')
if mibBuilder.loadTexts: category.setDescription('For non-clearable alarms, filtering category is NONE.')
clearable = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 1, 1, 7), ClearableTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clearable.setStatus('current')
if mibBuilder.loadTexts: clearable.setDescription('This attribute indicates whether this is a clearable or \n\t     non-clearable alarm notification.')
alarmPersistencyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2), )
if mibBuilder.loadTexts: alarmPersistencyConfigTable.setStatus('current')
if mibBuilder.loadTexts: alarmPersistencyConfigTable.setDescription('Alarm Persistency Configuration Table')
alarmPersistencyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1), ).setIndexNames((0, "PT-FM-MIB", "category"))
if mibBuilder.loadTexts: alarmPersistencyConfigEntry.setStatus('current')
if mibBuilder.loadTexts: alarmPersistencyConfigEntry.setDescription('An entry containing management information applicable to a\n                 particular interface.')
persistencyConfigcategory = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1, 1), CategoryTC())
if mibBuilder.loadTexts: persistencyConfigcategory.setStatus('current')
if mibBuilder.loadTexts: persistencyConfigcategory.setDescription('Persistency Configuration category')
onFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: onFilter.setStatus('current')
if mibBuilder.loadTexts: onFilter.setDescription('An integer with max value of 30. \n\t        Default is 0 sec for highOrderLevel and Unfiltered, \n\t        and 3 sec for lowOrderLevel')
offFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: offFilter.setStatus('current')
if mibBuilder.loadTexts: offFilter.setDescription('Off Filter')
notificationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3))
notificationReporting = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 1), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationReporting.setStatus('current')
if mibBuilder.loadTexts: notificationReporting.setDescription('This attribute is used to enable or disable reporting of notifications \n\t    from the AXXMETRO device. When disabled, no notifications will be sent.')
lCASExtendedAlarms = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 2), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lCASExtendedAlarms.setStatus('current')
if mibBuilder.loadTexts: lCASExtendedAlarms.setDescription('This attribute is used to enable or disable reporting of \n\t     extended LCAS notifications.')
nIMAlarms = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 3), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nIMAlarms.setStatus('current')
if mibBuilder.loadTexts: nIMAlarms.setDescription('This attribute is used to enable or disable reporting of \n\t    notifications from the NIM objects.')
pJEAlarms = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 1, 3, 4), EnableStatusTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pJEAlarms.setStatus('current')
if mibBuilder.loadTexts: pJEAlarms.setDescription('When the operator changes the value from enabled to disabled, \n\t    all active PJE alarms shall be cleared.\n\t    When the operator changes the value from disabled to enabled, \n\t    event counting shall be restarted (counters reset to 0).\n\t    This attribute has node scope, ie. it impacts all PJE alarms \n\t    on all SDH ports on the node.')
currentAlarmsTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1), )
if mibBuilder.loadTexts: currentAlarmsTable.setStatus('current')
if mibBuilder.loadTexts: currentAlarmsTable.setDescription('Current Alarms Table')
currentAlarmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1), ).setIndexNames((0, "PT-FM-MIB", "sequenceNumber"))
if mibBuilder.loadTexts: currentAlarmsEntry.setStatus('current')
if mibBuilder.loadTexts: currentAlarmsEntry.setDescription('An entry containing management information applicable to a\n            particular interface.')
sequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: sequenceNumber.setStatus('current')
if mibBuilder.loadTexts: sequenceNumber.setDescription('Sequence Number')
currentAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmTimeStamp.setStatus('current')
if mibBuilder.loadTexts: currentAlarmTimeStamp.setDescription('Time Stamp')
currentAlarmNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmNotificationId.setStatus('current')
if mibBuilder.loadTexts: currentAlarmNotificationId.setDescription('Current Alarm Notification Id')
currentAlarmManagedObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmManagedObjectId.setStatus('current')
if mibBuilder.loadTexts: currentAlarmManagedObjectId.setDescription("This object represents the managed object id of an active alarm.\n             The managed object id uniquely identifies the source of the\n             notification and consists of class and instance information\n             for the source. It is represented by a formated text string\n             which first contains the class and depending on the class a list\n             of attribute name and value pairs:\n\n             '<class>:<name>=<value>;<name>=<value>;...'\n\n             <class> : class name.\n             <name>  : attribute name.\n             <value> : attribute value.")
currentAlarmReferenceObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmReferenceObjectId.setStatus('current')
if mibBuilder.loadTexts: currentAlarmReferenceObjectId.setDescription("This object represents the referenced object id for the\n             managed object id in cases where the managed object id is\n             a virtual object id.\n             It has the same format as 'currentAlarmManagedObjectId' and\n             is represented by a formated text string which first contains\n             the class and depending on the class a list of attribute name\n             and value pairs:\n\n             '<class>:<name>=<value>;<name>=<value>;...'\n\n             <class> : class name.\n             <name>  : attribute name.\n             <value> : attribute value.")
currentAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 6), SeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: currentAlarmSeverity.setDescription('Current Alarm Severity')
currentAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 7), ProbableCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmProbableCause.setStatus('current')
if mibBuilder.loadTexts: currentAlarmProbableCause.setDescription('Current Alarm Probable Cause')
currentAlarmProbableCauseQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmProbableCauseQualifier.setStatus('current')
if mibBuilder.loadTexts: currentAlarmProbableCauseQualifier.setDescription('Current Alarm Probable Cause Qualifier')
currentAlarmAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmAdditionalText.setStatus('current')
if mibBuilder.loadTexts: currentAlarmAdditionalText.setDescription('Additional Text')
currentAlarmLayerRate = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 2, 1, 1, 10), LayerRateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmLayerRate.setStatus('current')
if mibBuilder.loadTexts: currentAlarmLayerRate.setDescription('Layer Rate')
alarmLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1))
maxNumOfEntriesForAlarm = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForAlarm.setStatus('current')
if mibBuilder.loadTexts: maxNumOfEntriesForAlarm.setDescription('Max Number Of Entries For Alarm')
lastSeqNumForAlarm = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForAlarm.setStatus('current')
if mibBuilder.loadTexts: lastSeqNumForAlarm.setDescription('Last Sequence Number For Alarm')
alarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3), )
if mibBuilder.loadTexts: alarmLogTable.setStatus('current')
if mibBuilder.loadTexts: alarmLogTable.setDescription('Alarm Log Table')
alarmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "alarmLogSequenceNumber"))
if mibBuilder.loadTexts: alarmLogEntry.setStatus('current')
if mibBuilder.loadTexts: alarmLogEntry.setDescription('An entry containing management information applicable to a\n            particular interface.')
alarmLogSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: alarmLogSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: alarmLogSequenceNumber.setDescription('AlarmLog Sequence Number')
alarmLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogTimeStamp.setStatus('current')
if mibBuilder.loadTexts: alarmLogTimeStamp.setDescription('Alarm Log TimeStamp')
alarmLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogNotificationId.setStatus('current')
if mibBuilder.loadTexts: alarmLogNotificationId.setDescription('Alarm Log Notification Id')
alarmLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 4), SeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmLogSeverity.setDescription('Alarm Log Severity')
alarmLogProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 5), ProbableCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogProbableCause.setStatus('current')
if mibBuilder.loadTexts: alarmLogProbableCause.setDescription('Alarm Log Probable Cause')
alarmLogProbableCauseQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogProbableCauseQualifier.setStatus('current')
if mibBuilder.loadTexts: alarmLogProbableCauseQualifier.setDescription('Alarm Log Probable Cause Qualifier')
alarmLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogAdditionalText.setStatus('current')
if mibBuilder.loadTexts: alarmLogAdditionalText.setDescription('Alarm Log Additional Text')
alarmLogLayerRate = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 1, 3, 1, 8), LayerRateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogLayerRate.setStatus('current')
if mibBuilder.loadTexts: alarmLogLayerRate.setDescription('Alarm Log Layer Rate')
tmnNotificationLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2))
maxNumOfEntriesForTMN = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForTMN.setStatus('current')
if mibBuilder.loadTexts: maxNumOfEntriesForTMN.setDescription('Maximum Number Of Entries For TMN')
lastSeqNumForTMN = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForTMN.setStatus('current')
if mibBuilder.loadTexts: lastSeqNumForTMN.setDescription('Last Sequence Number For TMN')
tmnNotificationLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3), )
if mibBuilder.loadTexts: tmnNotificationLogTable.setStatus('current')
if mibBuilder.loadTexts: tmnNotificationLogTable.setDescription('TMN Notification Log Table')
tmnNotificationLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "tmnSequenceNumber"))
if mibBuilder.loadTexts: tmnNotificationLogEntry.setStatus('current')
if mibBuilder.loadTexts: tmnNotificationLogEntry.setDescription('An entry containing management information applicable to a\n            particular interface.')
tmnSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: tmnSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: tmnSequenceNumber.setDescription('TMN Sequence Number')
tmnTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnTimeStamp.setStatus('current')
if mibBuilder.loadTexts: tmnTimeStamp.setDescription('TMN TimeStamp')
tmnNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnNotificationId.setStatus('current')
if mibBuilder.loadTexts: tmnNotificationId.setDescription('TMN Notification Id')
tmnAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnAdditionalText.setStatus('current')
if mibBuilder.loadTexts: tmnAdditionalText.setDescription('TMN Additional Text')
eventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3))
maxNumOfEntriesForEvent = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForEvent.setStatus('current')
if mibBuilder.loadTexts: maxNumOfEntriesForEvent.setDescription('Maximum Number Of Entries For Event')
lastSeqNumForEvent = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForEvent.setStatus('current')
if mibBuilder.loadTexts: lastSeqNumForEvent.setDescription('Last Sequence Number For Event')
eventLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3), )
if mibBuilder.loadTexts: eventLogTable.setStatus('current')
if mibBuilder.loadTexts: eventLogTable.setDescription('Event Log Table')
eventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "eventLogSequenceNumber"))
if mibBuilder.loadTexts: eventLogEntry.setStatus('current')
if mibBuilder.loadTexts: eventLogEntry.setDescription('An entry containing management information applicable to a\n            particular interface.')
eventLogSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: eventLogSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: eventLogSequenceNumber.setDescription('Event Log Sequence Number')
eventLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogTimeStamp.setStatus('current')
if mibBuilder.loadTexts: eventLogTimeStamp.setDescription('Event Log TimeStamp')
eventLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogNotificationId.setStatus('current')
if mibBuilder.loadTexts: eventLogNotificationId.setDescription('Event Log Notification Id')
eventType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 4), EventTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('current')
if mibBuilder.loadTexts: eventType.setDescription('Event Type')
eventLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogAdditionalText.setStatus('current')
if mibBuilder.loadTexts: eventLogAdditionalText.setDescription('Event Log Additional Text')
eventCause = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 3, 3, 1, 6), EventCauseTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCause.setStatus('current')
if mibBuilder.loadTexts: eventCause.setDescription('Event Cause')
protectionSwitchLog = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4))
maxNumOfEntriesForSwitch = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNumOfEntriesForSwitch.setStatus('current')
if mibBuilder.loadTexts: maxNumOfEntriesForSwitch.setDescription('Maximum Number Of Entries For Switch')
lastSeqNumForSwitch = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSeqNumForSwitch.setStatus('current')
if mibBuilder.loadTexts: lastSeqNumForSwitch.setDescription('Last Sequence Number For Switch')
protectionSwitchLogTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3), )
if mibBuilder.loadTexts: protectionSwitchLogTable.setStatus('current')
if mibBuilder.loadTexts: protectionSwitchLogTable.setDescription('Protection Switch Log Table')
protectionSwitchLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1), ).setIndexNames((0, "PT-FM-MIB", "switchLogSequenceNumber"))
if mibBuilder.loadTexts: protectionSwitchLogEntry.setStatus('current')
if mibBuilder.loadTexts: protectionSwitchLogEntry.setDescription('An entry containing management information applicable to a\n            particular interface.')
switchLogSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: switchLogSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: switchLogSequenceNumber.setDescription('Switch Log Sequence Number')
switchLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchLogTimeStamp.setStatus('current')
if mibBuilder.loadTexts: switchLogTimeStamp.setDescription('Switch Log TimeStamp')
switchLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 3), NotificationIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchLogNotificationId.setStatus('current')
if mibBuilder.loadTexts: switchLogNotificationId.setDescription('Switch Log Notification Id')
switchType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 4), SwitchTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchType.setStatus('current')
if mibBuilder.loadTexts: switchType.setDescription('Represents the type of the protection for which the switch has occurred.')
switchLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchLogAdditionalText.setStatus('current')
if mibBuilder.loadTexts: switchLogAdditionalText.setDescription('Switch Log Additional Text')
switchReason = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 3, 4, 3, 1, 6), SwitchReasonTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchReason.setStatus('current')
if mibBuilder.loadTexts: switchReason.setDescription('This attribute represents the reason for the switch.')
ptFMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 1))
ptFMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 2))
ptFMFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 1, 1)).setObjects(("PT-FM-MIB", "ptFMCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptFMFullCompliance = ptFMFullCompliance.setStatus('current')
if mibBuilder.loadTexts: ptFMFullCompliance.setDescription('The compliance statement for SNMP entities which implement everything.')
ptFMCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 3, 4, 2, 1)).setObjects(("PT-FM-MIB", "alarmLogTimeStamp"), ("PT-FM-MIB", "alarmLogNotificationId"), ("PT-FM-MIB", "alarmLogSeverity"), ("PT-FM-MIB", "alarmLogProbableCause"), ("PT-FM-MIB", "alarmLogProbableCauseQualifier"), ("PT-FM-MIB", "alarmLogAdditionalText"), ("PT-FM-MIB", "alarmLogLayerRate"), ("PT-FM-MIB", "category"), ("PT-FM-MIB", "clearable"), ("PT-FM-MIB", "currentAlarmTimeStamp"), ("PT-FM-MIB", "currentAlarmNotificationId"), ("PT-FM-MIB", "currentAlarmManagedObjectId"), ("PT-FM-MIB", "currentAlarmReferenceObjectId"), ("PT-FM-MIB", "currentAlarmSeverity"), ("PT-FM-MIB", "currentAlarmProbableCause"), ("PT-FM-MIB", "currentAlarmProbableCauseQualifier"), ("PT-FM-MIB", "currentAlarmAdditionalText"), ("PT-FM-MIB", "currentAlarmLayerRate"), ("PT-FM-MIB", "eventLogTimeStamp"), ("PT-FM-MIB", "eventLogNotificationId"), ("PT-FM-MIB", "eventType"), ("PT-FM-MIB", "eventLogAdditionalText"), ("PT-FM-MIB", "eventCause"), ("PT-FM-MIB", "lastSeqNumForAlarm"), ("PT-FM-MIB", "lastSeqNumForTMN"), ("PT-FM-MIB", "lastSeqNumForEvent"), ("PT-FM-MIB", "lastSeqNumForSwitch"), ("PT-FM-MIB", "lCASExtendedAlarms"), ("PT-FM-MIB", "maxNumOfEntriesForAlarm"), ("PT-FM-MIB", "maxNumOfEntriesForTMN"), ("PT-FM-MIB", "maxNumOfEntriesForEvent"), ("PT-FM-MIB", "maxNumOfEntriesForSwitch"), ("PT-FM-MIB", "notificationReporting"), ("PT-FM-MIB", "nIMAlarms"), ("PT-FM-MIB", "onFilter"), ("PT-FM-MIB", "offFilter"), ("PT-FM-MIB", "pJEAlarms"), ("PT-FM-MIB", "probableCauseQualifier"), ("PT-FM-MIB", "probableCause"), ("PT-FM-MIB", "severity"), ("PT-FM-MIB", "switchLogTimeStamp"), ("PT-FM-MIB", "switchLogNotificationId"), ("PT-FM-MIB", "switchType"), ("PT-FM-MIB", "switchLogAdditionalText"), ("PT-FM-MIB", "switchReason"), ("PT-FM-MIB", "tmnTimeStamp"), ("PT-FM-MIB", "tmnNotificationId"), ("PT-FM-MIB", "tmnAdditionalText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptFMCompleteGroup = ptFMCompleteGroup.setStatus('current')
if mibBuilder.loadTexts: ptFMCompleteGroup.setDescription('A collection of all current objects in this MIB module.')
mibBuilder.exportSymbols("PT-FM-MIB", switchReason=switchReason, ptFMCompliances=ptFMCompliances, switchLogAdditionalText=switchLogAdditionalText, ptFMConformance=ptFMConformance, alarmPersistencyConfigTable=alarmPersistencyConfigTable, moClass=moClass, ProbableCauseTC=ProbableCauseTC, alarmLogTable=alarmLogTable, eventLogEntry=eventLogEntry, currentAlarmReferenceObjectId=currentAlarmReferenceObjectId, eventLogTable=eventLogTable, alarmLogNotificationId=alarmLogNotificationId, protectionSwitchLog=protectionSwitchLog, currentAlarmAdditionalText=currentAlarmAdditionalText, severity=severity, lastSeqNumForAlarm=lastSeqNumForAlarm, alarmPersistencyConfigEntry=alarmPersistencyConfigEntry, alarmLogLayerRate=alarmLogLayerRate, probableCauseQualifier=probableCauseQualifier, tmnTimeStamp=tmnTimeStamp, ptFMCompleteGroup=ptFMCompleteGroup, tmnNotificationLog=tmnNotificationLog, currentAlarmsTable=currentAlarmsTable, nIMAlarms=nIMAlarms, tmnNotificationLogEntry=tmnNotificationLogEntry, tmnSequenceNumber=tmnSequenceNumber, switchType=switchType, alarmConfigTable=alarmConfigTable, switchLogNotificationId=switchLogNotificationId, config=config, alarmLogSeverity=alarmLogSeverity, notificationReporting=notificationReporting, SwitchReasonTC=SwitchReasonTC, persistencyConfigcategory=persistencyConfigcategory, switchLogTimeStamp=switchLogTimeStamp, LayerRateTC=LayerRateTC, alarmLogAdditionalText=alarmLogAdditionalText, tmnNotificationId=tmnNotificationId, alarm=alarm, EventTypeTC=EventTypeTC, ptFMGroups=ptFMGroups, ptFMFullCompliance=ptFMFullCompliance, lastSeqNumForTMN=lastSeqNumForTMN, alarmLogSequenceNumber=alarmLogSequenceNumber, maxNumOfEntriesForTMN=maxNumOfEntriesForTMN, currentAlarmManagedObjectId=currentAlarmManagedObjectId, alarmLogProbableCause=alarmLogProbableCause, eventLogNotificationId=eventLogNotificationId, eventType=eventType, currentAlarmSeverity=currentAlarmSeverity, eventLog=eventLog, lCASExtendedAlarms=lCASExtendedAlarms, alarmLogTimeStamp=alarmLogTimeStamp, lastSeqNumForEvent=lastSeqNumForEvent, tmnNotificationLogTable=tmnNotificationLogTable, alarmLog=alarmLog, alarmLogEntry=alarmLogEntry, lastSeqNumForSwitch=lastSeqNumForSwitch, switchLogSequenceNumber=switchLogSequenceNumber, alarmLogProbableCauseQualifier=alarmLogProbableCauseQualifier, currentAlarmProbableCauseQualifier=currentAlarmProbableCauseQualifier, SwitchTypeTC=SwitchTypeTC, eventLogSequenceNumber=eventLogSequenceNumber, protectionSwitchLogEntry=protectionSwitchLogEntry, log=log, pJEAlarms=pJEAlarms, currentAlarmsEntry=currentAlarmsEntry, ClearableTC=ClearableTC, tmnAdditionalText=tmnAdditionalText, currentAlarmNotificationId=currentAlarmNotificationId, notificationId=notificationId, probableCause=probableCause, maxNumOfEntriesForEvent=maxNumOfEntriesForEvent, EnableStatusTypeTC=EnableStatusTypeTC, MoClassTC=MoClassTC, offFilter=offFilter, sequenceNumber=sequenceNumber, maxNumOfEntriesForAlarm=maxNumOfEntriesForAlarm, ptFM=ptFM, currentAlarmProbableCause=currentAlarmProbableCause, eventLogAdditionalText=eventLogAdditionalText, eventCause=eventCause, eventLogTimeStamp=eventLogTimeStamp, NotificationIdTC=NotificationIdTC, currentAlarmTimeStamp=currentAlarmTimeStamp, currentAlarmLayerRate=currentAlarmLayerRate, SeverityTC=SeverityTC, alarmConfigEntry=alarmConfigEntry, notificationConfig=notificationConfig, maxNumOfEntriesForSwitch=maxNumOfEntriesForSwitch, CategoryTC=CategoryTC, clearable=clearable, PYSNMP_MODULE_ID=ptFM, protectionSwitchLogTable=protectionSwitchLogTable, EventCauseTC=EventCauseTC, category=category, onFilter=onFilter)
