#
# PySNMP MIB module AVIAT-ALARM-REPORTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-ALARM-REPORTING-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:26 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
AviatYangIdentityRef, = mibBuilder.importSymbols("AVIAT-TEXTCONVENTION-MIB", "AviatYangIdentityRef")
IANAItuProbableCause, IANAItuEventType = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuProbableCause", "IANAItuEventType")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, iso, IpAddress, ObjectIdentity, Gauge32, Counter32, ModuleIdentity, MibIdentifier, Unsigned32, TimeTicks, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "iso", "IpAddress", "ObjectIdentity", "Gauge32", "Counter32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TruthValue")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatAlarmReportingModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 47))
aviatAlarmReportingModule.setRevisions(('2016-05-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aviatAlarmReportingModule.setRevisionsDescriptions(('Initial Version.',))
if mibBuilder.loadTexts: aviatAlarmReportingModule.setLastUpdated('201605260000Z')
if mibBuilder.loadTexts: aviatAlarmReportingModule.setOrganization('Aviat Networks')
if mibBuilder.loadTexts: aviatAlarmReportingModule.setContactInfo('Aviat Networks\n                         Customer Service\n\n                         Postal: 5200 Great America Parkway\n                                 Santa Clara\n                                 California 95054\n                                 United States of America\n\n                         Tel: 408 567 7000\n\n                         E-mail: mibsupport@aviatnet.com')
if mibBuilder.loadTexts: aviatAlarmReportingModule.setDescription('This MIB module is used to describe the status of alarms\n                 present in Aviat Networks products.')
aviatAlarmReportingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 47, 1))
aviatAlarmReportingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 1))
aviatAlarmReportingCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 2))
aviatAlarmReportingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2))
aviatAlarmReportingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 7))
aviatAlarmReportingMIBEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 47, 0))
class IetfEntityName(TextualConvention, OctetString):
    description = 'A name uniquely identifying an entity within the system.\n             This corresponds to the physical entity name used by the\n             ietf-entity YANG.'
    status = 'current'
    displayHint = '127t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class AviatAlarmInstanceState(TextualConvention, Integer32):
    description = 'The current state of an alarm instance'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("cleared", 0), ("raised", 1), ("unstable", 2))

class AviatAlarmReportingMode(TextualConvention, Integer32):
    description = 'Reporting mode for alarm instances on a particular entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("all", 0), ("nonSummary", 1), ("summaryOnly", 2), ("none", 3))

aviatAlarmTypeTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1), )
if mibBuilder.loadTexts: aviatAlarmTypeTable.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeTable.setDescription('This is a table containing information for all alarms\n                         types that are supported by the system.')
aviatAlarmTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1), ).setIndexNames((0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeIndex"))
if mibBuilder.loadTexts: aviatAlarmTypeEntry.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeEntry.setDescription('This is a row in the table holding information about a\n                         single supported alarm type.')
aviatAlarmTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 1), AviatYangIdentityRef())
if mibBuilder.loadTexts: aviatAlarmTypeIndex.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeIndex.setDescription('The unique Yang Identity representing a particular alarm\n                         type.')
aviatAlarmTypeSecurityEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmTypeSecurityEvent.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeSecurityEvent.setDescription('Indicates whether or not the system views the alarm\n                         type as being security related.')
aviatAlarmTypeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmTypeDescription.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeDescription.setDescription('This object specifies a human-readable message\n                         describing the alarm type.')
aviatAlarmTypeEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 4), IANAItuEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmTypeEvent.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeEvent.setDescription('The type of event associated with the alarm type.')
aviatAlarmTypeDefaultSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 5), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmTypeDefaultSeverity.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeDefaultSeverity.setDescription('This object specifies the default severity assigned to\n                         the alarm type by the system. By default, any entity that\n                         raises an alarm of this type will have this level of severity\n                         associated with the alarm instance.\n                         The following ITU-t X.733 severities are supported:\n                             critical        (3)\n                             major           (4)\n                             minor           (5)\n                             warning         (6)\n\n                         See http://www.iana.org.')
aviatAlarmInstanceLastChange = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceLastChange.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceLastChange.setDescription('The time when any alarm instance in the system last\n                         changed its state.')
aviatAlarmInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3), )
if mibBuilder.loadTexts: aviatAlarmInstanceTable.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceTable.setDescription('This is a table containing information for all alarm\n                         instances currently registered within the system.')
aviatAlarmInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1), ).setIndexNames((0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceEntity"), (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeIndex"))
if mibBuilder.loadTexts: aviatAlarmInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceEntry.setDescription('This is a row in the table holding information for a\n                         given alarm instance.')
aviatAlarmInstanceEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 1), IetfEntityName())
if mibBuilder.loadTexts: aviatAlarmInstanceEntity.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceEntity.setDescription('Each alarm instance is associated with a particular\n                         system entity. This object identifies the entity in the\n                         form of a name string. Corresponds to the physical\n                         entity name as per the ietf-entity YANG.')
aviatAlarmInstanceSecurityEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceSecurityEvent.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceSecurityEvent.setDescription('Indicates whether or not the system views the alarm\n                         instance as being security related.')
aviatAlarmInstanceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceDescription.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceDescription.setDescription('This object specifies a human-readable message\n                         describing the alarm instance.')
aviatAlarmInstanceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 4), IANAItuEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceType.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceType.setDescription('The type of event associated with the alarm instance.')
aviatAlarmInstanceCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 5), AviatAlarmInstanceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceCurrentState.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceCurrentState.setDescription('The current state of the alarm instance.\n                         Supported states are:\n                             cleared  (0)\n                             raised   (1)\n                             unstable (2)')
aviatAlarmInstanceCurrentSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 6), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceCurrentSeverity.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceCurrentSeverity.setDescription('This object shows the current severity level\n                         associated with the alarm instance:\n                             cleared        (1)\n                             indetermined   (2)\n                             critical       (3)\n                             major          (4)\n                             minor          (5)\n                             warning        (6)')
aviatAlarmInstanceRaisedSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 7), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceRaisedSeverity.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceRaisedSeverity.setDescription('The severity to be applied when this alarm instance is\n                         raised for this entity. This is either based upon the\n                         default for the alarm type, or overriden by user\n                         configuration.\n\n                         The following ITU-t X.733 severities are supported:\n                             critical       (3)\n                             major          (4)\n                             minor          (5)\n                             warning        (6)\n\n                         See http://www.iana.org.')
aviatAlarmInstanceLastStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceLastStatusChange.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceLastStatusChange.setDescription('The time when the status of the alarm instance last\n                         changed.')
aviatAlarmInstanceStatusChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceStatusChangeCount.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceStatusChangeCount.setDescription('The number of times that the entity has raised or\n                         lowered this alarm instance since the system was started.')
aviatAlarmInstanceDisabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmInstanceDisabled.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmInstanceDisabled.setDescription('Indicates whether or not an event which causes this\n                         alarm instance to be raised or lowered by this entity,\n                         will be reported.\n\n                         When disabled, status changes for the alarm will still\n                         be shown in aviatAlarmInstanceTable, but the alarm instance\n                         will no longer appear in aviatAlarmRaisedInstanceTable,\n                         a log entry will not be made, and a notification will not\n                         be generated.')
aviatAlarmRaisedInstanceLastChange = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceLastChange.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceLastChange.setDescription('The time of the last update to the raised alarms table.')
aviatAlarmRaisedInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5), )
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceTable.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceTable.setDescription('This is a table containing information for all alarm\n                         instances that are currently raised or unstable in the\n                         system.')
aviatAlarmRaisedInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1), ).setIndexNames((0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceEntity"), (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeIndex"))
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceEntry.setDescription('This is a row in the table holding information for a\n                         given raised or unstable alarm instance.')
aviatAlarmRaisedInstanceSecurityEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceSecurityEvent.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceSecurityEvent.setDescription('Indicates whether or not the system views the alarm\n                         instance as being security related.')
aviatAlarmRaisedInstanceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceDescription.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceDescription.setDescription('This object specifies a human-readable message\n                         describing the alarm instance.')
aviatAlarmRaisedInstanceSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 3), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceSeverity.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceSeverity.setDescription('This object shows the severity level associated with\n                         the alarm instance:\n                             critical       (3)\n                             major          (4)\n                             minor          (5)\n                             warning        (6)')
aviatAlarmRaisedInstanceCause = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 4), IANAItuProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceCause.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceCause.setDescription('This object shows the probable cause of the alarm\n                         instance being active.')
aviatAlarmRaisedInstanceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceTime.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceTime.setDescription('The time when the alarm instance was raised.')
aviatAlarmRaisedInstanceIsUnstable = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceIsUnstable.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceIsUnstable.setDescription('An indication of whether the alarm instance is\n                         currently considered unstable, and hence has\n                         further state changes suspended until it is\n                         considered stable again.')
aviatAlarmEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 6), )
if mibBuilder.loadTexts: aviatAlarmEntityTable.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmEntityTable.setDescription('This is a table containing information for all entities\n                         that have alarm instances registered against them.')
aviatAlarmEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 6, 1), ).setIndexNames((0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceEntity"))
if mibBuilder.loadTexts: aviatAlarmEntityEntry.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmEntityEntry.setDescription('This is a row in the table holding information for a\n                         given entity.')
aviatAlarmEntityReportingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 6, 1, 1), AviatAlarmReportingMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatAlarmEntityReportingMode.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmEntityReportingMode.setDescription('Indicates the alarm reporting mode configured for this\n                         entity. Supported modes are:\n\n                             all         (0)\n                             nonSummary  (1)\n                             summaryOnly (2)\n                             none        (3)\n\n                         The mode dictates alarm instances of which alarm types\n                         against the entity shall generate a log entry and a\n                         notification upon state change or suppression change.')
aviatAlarmEntityName = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 7, 1), IetfEntityName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aviatAlarmEntityName.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmEntityName.setDescription('The name of the entity associated with the alarm\n                         instance. Only used for the generation of\n                         notifications.')
aviatAlarmTypeID = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 7, 2), AviatYangIdentityRef()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aviatAlarmTypeID.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmTypeID.setDescription('The index of the alarm type associated with\n                         the alarm instance. Only used for the\n                         generation of notifications.')
aviatAlarmRaisedInstanceNotification = NotificationType((1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 1)).setObjects(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentSeverity"))
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceNotification.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmRaisedInstanceNotification.setDescription('This notification is generated whenever a system alarm\n                         is raised.')
aviatAlarmClearedInstanceNotification = NotificationType((1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 2)).setObjects(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"))
if mibBuilder.loadTexts: aviatAlarmClearedInstanceNotification.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmClearedInstanceNotification.setDescription('This notification is generated whenever a system alarm\n                         is cleared.')
aviatAlarmUnstableInstanceNotification = NotificationType((1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 3)).setObjects(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentSeverity"))
if mibBuilder.loadTexts: aviatAlarmUnstableInstanceNotification.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmUnstableInstanceNotification.setDescription('This notification is generated whenever a system alarm\n                         is suspended.')
aviatAlarmStabilizedInstanceNotification = NotificationType((1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 4)).setObjects(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"))
if mibBuilder.loadTexts: aviatAlarmStabilizedInstanceNotification.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmStabilizedInstanceNotification.setDescription('This notification is generated whenever a system alarm\n                         suspension is cleared.')
aviatAlarmReportingObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 1, 1)).setObjects(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeSecurityEvent"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeDescription"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeEvent"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeDefaultSeverity"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastChange"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceSecurityEvent"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceDescription"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceType"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentState"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentSeverity"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceRaisedSeverity"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceStatusChangeCount"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceDisabled"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceLastChange"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceSecurityEvent"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceDescription"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceSeverity"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceCause"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceTime"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceIsUnstable"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityReportingMode"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatAlarmReportingObjectGroup = aviatAlarmReportingObjectGroup.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmReportingObjectGroup.setDescription('These are the objects for alarms in the Alarm MIB.')
aviatAlarmReportingNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 1, 2)).setObjects(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceNotification"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmClearedInstanceNotification"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmUnstableInstanceNotification"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmStabilizedInstanceNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatAlarmReportingNotifyGroup = aviatAlarmReportingNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmReportingNotifyGroup.setDescription('Alarm notifications defined in this MIB.')
aviatAlarmReportingComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 2, 1)).setObjects(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmReportingObjectGroup"), ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmReportingNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatAlarmReportingComplV1 = aviatAlarmReportingComplV1.setStatus('current')
if mibBuilder.loadTexts: aviatAlarmReportingComplV1.setDescription('The implementation requirements for this MIB.')
mibBuilder.exportSymbols("AVIAT-ALARM-REPORTING-MIB", aviatAlarmReportingConformance=aviatAlarmReportingConformance, aviatAlarmInstanceSecurityEvent=aviatAlarmInstanceSecurityEvent, aviatAlarmRaisedInstanceDescription=aviatAlarmRaisedInstanceDescription, aviatAlarmRaisedInstanceIsUnstable=aviatAlarmRaisedInstanceIsUnstable, aviatAlarmInstanceEntity=aviatAlarmInstanceEntity, aviatAlarmRaisedInstanceCause=aviatAlarmRaisedInstanceCause, PYSNMP_MODULE_ID=aviatAlarmReportingModule, aviatAlarmUnstableInstanceNotification=aviatAlarmUnstableInstanceNotification, IetfEntityName=IetfEntityName, aviatAlarmInstanceCurrentState=aviatAlarmInstanceCurrentState, aviatAlarmReportingMIBEvents=aviatAlarmReportingMIBEvents, aviatAlarmRaisedInstanceSecurityEvent=aviatAlarmRaisedInstanceSecurityEvent, aviatAlarmInstanceCurrentSeverity=aviatAlarmInstanceCurrentSeverity, aviatAlarmInstanceDisabled=aviatAlarmInstanceDisabled, aviatAlarmInstanceTable=aviatAlarmInstanceTable, aviatAlarmEntityTable=aviatAlarmEntityTable, aviatAlarmTypeIndex=aviatAlarmTypeIndex, aviatAlarmEntityEntry=aviatAlarmEntityEntry, aviatAlarmTypeTable=aviatAlarmTypeTable, AviatAlarmInstanceState=AviatAlarmInstanceState, aviatAlarmEntityReportingMode=aviatAlarmEntityReportingMode, aviatAlarmReportingMIBObjects=aviatAlarmReportingMIBObjects, aviatAlarmReportingModule=aviatAlarmReportingModule, aviatAlarmInstanceLastChange=aviatAlarmInstanceLastChange, aviatAlarmRaisedInstanceTable=aviatAlarmRaisedInstanceTable, aviatAlarmRaisedInstanceNotification=aviatAlarmRaisedInstanceNotification, aviatAlarmTypeEntry=aviatAlarmTypeEntry, aviatAlarmReportingComplV1=aviatAlarmReportingComplV1, aviatAlarmRaisedInstanceEntry=aviatAlarmRaisedInstanceEntry, aviatAlarmInstanceEntry=aviatAlarmInstanceEntry, aviatAlarmInstanceStatusChangeCount=aviatAlarmInstanceStatusChangeCount, aviatAlarmTypeID=aviatAlarmTypeID, aviatAlarmReportingObjectGroup=aviatAlarmReportingObjectGroup, aviatAlarmInstanceRaisedSeverity=aviatAlarmInstanceRaisedSeverity, aviatAlarmInstanceDescription=aviatAlarmInstanceDescription, aviatAlarmTypeSecurityEvent=aviatAlarmTypeSecurityEvent, aviatAlarmEntityName=aviatAlarmEntityName, aviatAlarmStabilizedInstanceNotification=aviatAlarmStabilizedInstanceNotification, aviatAlarmInstanceType=aviatAlarmInstanceType, aviatAlarmReportingNotifications=aviatAlarmReportingNotifications, aviatAlarmReportingNotifyGroup=aviatAlarmReportingNotifyGroup, aviatAlarmReportingGroups=aviatAlarmReportingGroups, aviatAlarmReportingCompliance=aviatAlarmReportingCompliance, aviatAlarmTypeDefaultSeverity=aviatAlarmTypeDefaultSeverity, aviatAlarmRaisedInstanceLastChange=aviatAlarmRaisedInstanceLastChange, aviatAlarmRaisedInstanceTime=aviatAlarmRaisedInstanceTime, aviatAlarmTypeDescription=aviatAlarmTypeDescription, aviatAlarmInstanceLastStatusChange=aviatAlarmInstanceLastStatusChange, aviatAlarmClearedInstanceNotification=aviatAlarmClearedInstanceNotification, aviatAlarmTypeEvent=aviatAlarmTypeEvent, aviatAlarmRaisedInstanceSeverity=aviatAlarmRaisedInstanceSeverity, AviatAlarmReportingMode=AviatAlarmReportingMode)
