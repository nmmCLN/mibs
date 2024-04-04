#
# PySNMP MIB module F5-ALERT-DEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-ALERT-DEF-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:06 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
f5Compliance, platform = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "f5Compliance", "platform")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Bits, Unsigned32, Counter64, NotificationType, iso, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Bits", "Unsigned32", "Counter64", "NotificationType", "iso", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
f5Alerts = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 1))
f5Alerts.setRevisions(('2019-08-01 09:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f5Alerts.setRevisionsDescriptions(('F5 Alert Common MIB definitions.',))
if mibBuilder.loadTexts: f5Alerts.setLastUpdated('201908010941Z')
if mibBuilder.loadTexts: f5Alerts.setOrganization('F5 Networks, Inc.')
if mibBuilder.loadTexts: f5Alerts.setContactInfo('postal: F5 Networks, Inc.\n                  801 5th Ave\n                  Seattle,  WA 98104\n          phone:  (206) 272-5555\n          email:  support@f5.com')
if mibBuilder.loadTexts: f5Alerts.setDescription('Top-level infrastructure of the F5 Networks enterprise Alert MIB tree.')
class F5Severity(TextualConvention, Integer32):
    description = 'The severity of the alerts.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("na", 8))

class F5CondEffect(TextualConvention, Integer32):
    description = 'The effect of the condition.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 9999))
    namedValues = NamedValues(("clear", 0), ("assert", 1), ("event", 2), ("other", 9999))

f5AlertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0))
f5AlertNotificationObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1))
f5AlertNotificationObjectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2))
f5AlertNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 3))
alertSource = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSource.setStatus('current')
if mibBuilder.loadTexts: alertSource.setDescription('The source/facility generating this trap.')
alertEffect = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 2), F5CondEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertEffect.setStatus('current')
if mibBuilder.loadTexts: alertEffect.setDescription('The effect of the alert, whether it is raising or clearing.')
alertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 3), F5Severity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSeverity.setStatus('current')
if mibBuilder.loadTexts: alertSeverity.setDescription('The severity of the alarm.')
alertTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertTimeStamp.setStatus('current')
if mibBuilder.loadTexts: alertTimeStamp.setDescription('This object specifies the date and time the Trap was generated.')
alertDescription = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertDescription.setStatus('current')
if mibBuilder.loadTexts: alertDescription.setDescription('The alarm Trap description.')
alertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertSource"), ("F5-ALERT-DEF-MIB", "alertEffect"), ("F5-ALERT-DEF-MIB", "alertSeverity"), ("F5-ALERT-DEF-MIB", "alertTimeStamp"), ("F5-ALERT-DEF-MIB", "alertDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertGroup = alertGroup.setStatus('current')
if mibBuilder.loadTexts: alertGroup.setDescription('This is a generic Trap for reporting alerts.')
f5AlertGroupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12276, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f5AlertGroupCompliance = f5AlertGroupCompliance.setStatus('current')
if mibBuilder.loadTexts: f5AlertGroupCompliance.setDescription('This specifies the objects that are required to claim\n         compliance to F5 Alert Notifications.')
mibBuilder.exportSymbols("F5-ALERT-DEF-MIB", f5AlertNotificationGroup=f5AlertNotificationGroup, alertSeverity=alertSeverity, alertTimeStamp=alertTimeStamp, f5AlertGroupCompliance=f5AlertGroupCompliance, F5CondEffect=F5CondEffect, f5Alerts=f5Alerts, f5AlertNotificationObject=f5AlertNotificationObject, alertGroup=alertGroup, alertDescription=alertDescription, F5Severity=F5Severity, f5AlertObjects=f5AlertObjects, f5AlertNotificationObjectGroup=f5AlertNotificationObjectGroup, alertSource=alertSource, PYSNMP_MODULE_ID=f5Alerts, alertEffect=alertEffect)
