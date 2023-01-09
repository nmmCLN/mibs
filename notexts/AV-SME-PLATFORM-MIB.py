#
# PySNMP MIB module AV-SME-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AV-SME-PLATFORM-MIB.mib
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:26 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
mibs, = mibBuilder.importSymbols("AVAYAGEN-MIB", "mibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysDescr, = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr")
Integer32, Gauge32, Counter32, MibIdentifier, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, Bits, Unsigned32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32", "ModuleIdentity", "iso")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
avSMEPlatformMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 48))
avSMEPlatformMIB.setRevisions(('2013-01-11 14:05', '2010-07-06 13:47', '2010-07-02 14:37',))
if mibBuilder.loadTexts: avSMEPlatformMIB.setLastUpdated('201301111405Z')
if mibBuilder.loadTexts: avSMEPlatformMIB.setOrganization('Avaya Inc.')
smepGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1))
smepGenMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 1))
smepGenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2))
smepGenConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3))
smepGTEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0))
smepGTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1))
smepGTEventStdSeverity = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 1), ItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventStdSeverity.setStatus('current')
smepGTEventDateTime = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 2), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventDateTime.setStatus('current')
smepGTEventDevID = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventDevID.setStatus('current')
smepGTEventAppEntity = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("voiceMailPro", 1), ("onex", 2), ("ipOffice", 3), ("jade", 4), ("webmanagement", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventAppEntity.setStatus('current')
smepGTEventAppEvent = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("crash", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventAppEvent.setStatus('current')
smepGenColdStartEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenColdStartEvent.setStatus('current')
smepGenWarmStartEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 2)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenWarmStartEvent.setStatus('current')
smepGenLinkDownEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 3)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: smepGenLinkDownEvent.setStatus('current')
smepGenLinkUpEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 4)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: smepGenLinkUpEvent.setStatus('current')
smepGenAuthFailureEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 5)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenAuthFailureEvent.setStatus('current')
smepGenAppEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 6)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
if mibBuilder.loadTexts: smepGenAppEvent.setStatus('current')
smepGenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1))
smepGenGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2))
smepGenCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenNotificationObjectsGroup"), ("AV-SME-PLATFORM-MIB", "smepGenEntGenNotificationsGroup"), ("AV-SME-PLATFORM-MIB", "smepGenAppNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenCompliance = smepGenCompliance.setStatus('deprecated')
smepGenNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenNotificationObjectsGroup = smepGenNotificationObjectsGroup.setStatus('current')
smepGenEntGenNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 2)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenColdStartEvent"), ("AV-SME-PLATFORM-MIB", "smepGenWarmStartEvent"), ("AV-SME-PLATFORM-MIB", "smepGenLinkDownEvent"), ("AV-SME-PLATFORM-MIB", "smepGenLinkUpEvent"), ("AV-SME-PLATFORM-MIB", "smepGenAuthFailureEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenEntGenNotificationsGroup = smepGenEntGenNotificationsGroup.setStatus('current')
smepGenAppNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 3)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenAppEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenAppNotificationsGroup = smepGenAppNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("AV-SME-PLATFORM-MIB", smepGeneric=smepGeneric, smepGTEventDevID=smepGTEventDevID, smepGTEvents=smepGTEvents, smepGenCompliance=smepGenCompliance, smepGenTraps=smepGenTraps, smepGTEventStdSeverity=smepGTEventStdSeverity, smepGenWarmStartEvent=smepGenWarmStartEvent, avSMEPlatformMIB=avSMEPlatformMIB, smepGenAppEvent=smepGenAppEvent, smepGenLinkUpEvent=smepGenLinkUpEvent, smepGenCompliances=smepGenCompliances, smepGenNotificationObjectsGroup=smepGenNotificationObjectsGroup, smepGTEventAppEvent=smepGTEventAppEvent, smepGTObjects=smepGTObjects, smepGenConformance=smepGenConformance, smepGenGroups=smepGenGroups, smepGenAuthFailureEvent=smepGenAuthFailureEvent, smepGenEntGenNotificationsGroup=smepGenEntGenNotificationsGroup, smepGenColdStartEvent=smepGenColdStartEvent, smepGenAppNotificationsGroup=smepGenAppNotificationsGroup, PYSNMP_MODULE_ID=avSMEPlatformMIB, smepGTEventAppEntity=smepGTEventAppEntity, smepGenMibs=smepGenMibs, smepGTEventDateTime=smepGTEventDateTime, smepGenLinkDownEvent=smepGenLinkDownEvent)
