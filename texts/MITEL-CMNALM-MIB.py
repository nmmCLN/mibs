#
# PySNMP MIB module MITEL-CMNALM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-CMNALM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:27:53 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
mitelIdentification, mitelConfCompliances, mitelPropCommon, mitelConfGroups = mibBuilder.importSymbols("MITEL-MIB", "mitelIdentification", "mitelConfCompliances", "mitelPropCommon", "mitelConfGroups")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Counter64, Integer32, TimeTicks, Counter32, Unsigned32, ObjectIdentity, IpAddress, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter64", "Integer32", "TimeTicks", "Counter32", "Unsigned32", "ObjectIdentity", "IpAddress", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
mitelCmnAlarms = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1))
mitelCmnAlarms.setRevisions(('2014-02-11 12:00', '2005-02-21 21:34', '2004-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelCmnAlarms.setRevisionsDescriptions(('The MITEL Alarms-Specific Common MIB module.', 'Added the mitelAlmActiveTblIndex to the mitelNotifActiveAlarm.', 'MITEL Alarms-Specific Common MIB Version 1.0.0.1 - Draft',))
if mibBuilder.loadTexts: mitelCmnAlarms.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitelCmnAlarms.setOrganization('MITEL Networks Corporation')
if mibBuilder.loadTexts: mitelCmnAlarms.setContactInfo('Standards Group,\n                           Postal:    MITEL Networks Corporation\n                           350 Legget Drive, PO Box 13089\n                           Kanata, Ontario\n                           Canada  K2K 2W7\n                           Tel: +1 613 592 2122\n                           Fax: +1 613 592 4784\n                           URL: www.mitel.com')
if mibBuilder.loadTexts: mitelCmnAlarms.setDescription('Replaced E-Mail: std@mitel.com with URL: www.mitel.com.')
class ItuPerceivedSeverity(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information\n               Model', 1995\n               ITU Recommendation X.733, 'Information Technology - Open\n               Systems Interconnection - System Management: Alarm\n               Reporting Function', 1992"
    description = 'ITU perceived severity values'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class MitelCmnAlarmThresholdType(TextualConvention, Integer32):
    reference = 'Mitel SNMP MIB Support Guide - DK113065'
    description = 'The different types of thresholds that can be supported.\n                '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("percentage", 1), ("absoluteValue", 2), ("indeterminate", 3))

mitelCmnAlmObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1))
if mibBuilder.loadTexts: mitelCmnAlmObjects.setStatus('current')
if mibBuilder.loadTexts: mitelCmnAlmObjects.setDescription('Overall system alarm information.')
mitelCmnAlmNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 2))
if mibBuilder.loadTexts: mitelCmnAlmNotifications.setStatus('current')
if mibBuilder.loadTexts: mitelCmnAlmNotifications.setDescription('Alarms Notifications.')
mitelCmnAlmConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 3))
if mibBuilder.loadTexts: mitelCmnAlmConformance.setStatus('current')
if mibBuilder.loadTexts: mitelCmnAlmConformance.setDescription('Conformance statement.')
mitelAlmSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1))
if mibBuilder.loadTexts: mitelAlmSystem.setStatus('current')
if mibBuilder.loadTexts: mitelAlmSystem.setDescription('Overall system alarm information.')
mitelAlmSysSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 1), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmSysSeverity.setStatus('current')
if mibBuilder.loadTexts: mitelAlmSysSeverity.setDescription('Overall system alarm level severity.\n                           This relates to the alarms in the mitelAlmActiveTable.')
mitelAlmSysSeverityDetectTime = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmSysSeverityDetectTime.setStatus('current')
if mibBuilder.loadTexts: mitelAlmSysSeverityDetectTime.setDescription('The time that the overall system alarm level changed.')
mitelAlmSysSeverityDescr = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmSysSeverityDescr.setStatus('current')
if mibBuilder.loadTexts: mitelAlmSysSeverityDescr.setDescription('Additional details of what may have caused the system \n                           severity to change.')
mitelAlmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2), )
if mibBuilder.loadTexts: mitelAlmActiveTable.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTable.setDescription('A list of the MITEL-defined currently active alarmed \n                          objects wihin the system. This table is typically \n                          maintained in non-volatile memory, and is re-built \n                          upon agent restart.')
mitelAlmActiveTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1), ).setIndexNames((0, "MITEL-CMNALM-MIB", "mitelAlmActiveTblIndex"))
if mibBuilder.loadTexts: mitelAlmActiveTableEntry.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTableEntry.setDescription('An entry containing application information.')
mitelAlmActiveTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblIndex.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblIndex.setDescription('The index of this row. The unique object identifier\n                           of the application that is raising this alarm.')
mitelAlmActiveTblClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblClass.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblClass.setDescription('The class that the active alarm belongs to.')
mitelAlmActiveTblType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblType.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblType.setDescription('The type of alarm within its Class.')
mitelAlmActiveTblTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblTypeName.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblTypeName.setDescription('A unique descriptive name that represent the alarm\n                           type within the class.')
mitelAlmActiveTblSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 5), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblSeverity.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblSeverity.setDescription('The current severity of the active alarm type.')
mitelAlmActiveTblSeverityDetectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblSeverityDetectTime.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblSeverityDetectTime.setDescription('When the alarm type trasitioned to the current\n                           Severity level.')
mitelAlmActiveTblThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 7), MitelCmnAlarmThresholdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblThresholdType.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblThresholdType.setDescription('Threshold information as to the cause of the\n                           current severity of the alarm type.')
mitelAlmActiveTblThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblThresholdValue.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblThresholdValue.setDescription('The actual threshold value that caused the severity\n                           to change. This relates directly to the threshold type.')
mitelAlmActiveTblDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblDescr.setStatus('current')
if mibBuilder.loadTexts: mitelAlmActiveTblDescr.setDescription("A textual description of the cause of the \n                           current alarm type's severity.")
mitelNotifActiveAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 2, 1)).setObjects(("MITEL-CMNALM-MIB", "mitelAlmSysSeverity"), ("MITEL-CMNALM-MIB", "mitelAlmSysSeverityDetectTime"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblIndex"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblClass"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblType"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblTypeName"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblSeverity"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblThresholdType"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblThresholdValue"))
if mibBuilder.loadTexts: mitelNotifActiveAlarm.setStatus('current')
if mibBuilder.loadTexts: mitelNotifActiveAlarm.setDescription('This notification is generated whenever\n                          an alarm condition is detected or cleared.')
mibBuilder.exportSymbols("MITEL-CMNALM-MIB", mitelCmnAlarms=mitelCmnAlarms, mitelAlmActiveTblIndex=mitelAlmActiveTblIndex, ItuPerceivedSeverity=ItuPerceivedSeverity, mitelAlmActiveTblThresholdType=mitelAlmActiveTblThresholdType, mitelAlmActiveTblClass=mitelAlmActiveTblClass, mitelAlmActiveTblSeverity=mitelAlmActiveTblSeverity, mitelAlmSysSeverityDescr=mitelAlmSysSeverityDescr, mitelCmnAlmConformance=mitelCmnAlmConformance, mitelCmnAlmObjects=mitelCmnAlmObjects, mitelAlmActiveTableEntry=mitelAlmActiveTableEntry, mitelAlmActiveTblSeverityDetectTime=mitelAlmActiveTblSeverityDetectTime, mitelNotifActiveAlarm=mitelNotifActiveAlarm, mitelCmnAlmNotifications=mitelCmnAlmNotifications, PYSNMP_MODULE_ID=mitelCmnAlarms, mitelAlmActiveTblType=mitelAlmActiveTblType, mitelAlmActiveTblTypeName=mitelAlmActiveTblTypeName, mitelAlmActiveTable=mitelAlmActiveTable, mitelAlmActiveTblThresholdValue=mitelAlmActiveTblThresholdValue, mitelAlmActiveTblDescr=mitelAlmActiveTblDescr, mitelAlmSysSeverity=mitelAlmSysSeverity, MitelCmnAlarmThresholdType=MitelCmnAlarmThresholdType, mitelAlmSysSeverityDetectTime=mitelAlmSysSeverityDetectTime, mitelAlmSystem=mitelAlmSystem)
