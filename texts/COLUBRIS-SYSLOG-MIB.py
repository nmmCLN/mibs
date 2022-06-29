#
# PySNMP MIB module COLUBRIS-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SYSLOG-MIB.my
# Produced by pysmi-1.1.8 at Wed Jun 29 13:09:24 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, ModuleIdentity, NotificationType, Unsigned32, ObjectIdentity, Bits, Counter32, Gauge32, Counter64, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits", "Counter32", "Gauge32", "Counter64", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 3))
if mibBuilder.loadTexts: colubrisSyslogMIB.setLastUpdated('200402100000Z')
if mibBuilder.loadTexts: colubrisSyslogMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisSyslogMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisSyslogMIB.setDescription('Colubris Networks Syslog MIB module.')
colubrisSyslogMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1))
syslogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1))
syslogMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2))
class SyslogSeverity(TextualConvention, Integer32):
    description = 'Indicates the severity of a syslog message.\n                 NOTE: This values is the actual value the syslog daemon uses,\n                       plus 1. For example: the value for debug severity will\n                       be 8 instead of 7.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

syslogSeverityNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 1), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogSeverityNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: syslogSeverityNotificationEnabled.setDescription('Specifies if syslogSeverityNotification events are\n                 generated.')
syslogRegExMatchNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 2), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogRegExMatchNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: syslogRegExMatchNotificationEnabled.setDescription('Specifies if syslogRegExMatchNotification events are\n                 generated.')
syslogSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 3), SyslogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogSeverityLevel.setStatus('current')
if mibBuilder.loadTexts: syslogSeverityLevel.setDescription('Specifies the severity level of messages that the syslog daemon\n                 will log. Only messages with a severity level equal to or\n                 greater than syslogSeverityLevel will be logged. For example,\n                 A value of error(4) means that messages with warning, notice,\n                 info or debug severity will not be logged.')
syslogTrapSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 4), SyslogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogTrapSeverityLevel.setStatus('current')
if mibBuilder.loadTexts: syslogTrapSeverityLevel.setDescription('Specifies the severity level of messages that will generate a \n                 syslogSeverityNotification notification. For example, a value\n                 of error(4) means that messages with warning, notice, info or\n                 debug severity will never generate a notification.')
syslogMessageRegEx = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogMessageRegEx.setStatus('current')
if mibBuilder.loadTexts: syslogMessageRegEx.setDescription('Specifies the regular expression that will trigger a\n                 syslogRegExMatchNotification. When set to an empty string, \n                 there is no attempt to match the syslog message generated \n                 by the device with the content of syslogMessageRegEx.')
syslogMsgNumber = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgNumber.setStatus('current')
if mibBuilder.loadTexts: syslogMsgNumber.setDescription('A unique ID representing a message in the system log.')
syslogMsgFacility = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgFacility.setStatus('current')
if mibBuilder.loadTexts: syslogMsgFacility.setDescription('A string representing the facility that sent the message.')
syslogMsgSeverity = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 3), SyslogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgSeverity.setStatus('current')
if mibBuilder.loadTexts: syslogMsgSeverity.setDescription('The severity level of the message in the system log.')
syslogMsgText = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgText.setStatus('current')
if mibBuilder.loadTexts: syslogMsgText.setDescription('The message itself as logged in the system log.')
colubrisSyslogMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2))
colubrisSyslogMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0))
syslogSeverityNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0, 1)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
if mibBuilder.loadTexts: syslogSeverityNotification.setStatus('current')
if mibBuilder.loadTexts: syslogSeverityNotification.setDescription('Sent when the device generated a syslog message that is \n                 of the right severity level. This severity level is set by\n                 syslogTrapSeverityLevel.')
syslogRegExMatchNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0, 2)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
if mibBuilder.loadTexts: syslogRegExMatchNotification.setStatus('current')
if mibBuilder.loadTexts: syslogRegExMatchNotification.setDescription('Sent when the device generated a syslog message that \n                 matches the regular expression specified in\n                 syslogMessageRegEx.')
colubrisSyslogMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3))
colubrisSyslogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 1))
colubrisSyslogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2))
colubrisSyslogMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 1, 1)).setObjects(("COLUBRIS-SYSLOG-MIB", "colubrisSyslogMIBGroup"), ("COLUBRIS-SYSLOG-MIB", "colubrisSyslogNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSyslogMIBCompliance = colubrisSyslogMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisSyslogMIBCompliance.setDescription('The compliance statement for entities which implement\n                 the Colubris Networks Syslog MIB.')
colubrisSyslogMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2, 1)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogSeverityNotificationEnabled"), ("COLUBRIS-SYSLOG-MIB", "syslogRegExMatchNotificationEnabled"), ("COLUBRIS-SYSLOG-MIB", "syslogSeverityLevel"), ("COLUBRIS-SYSLOG-MIB", "syslogTrapSeverityLevel"), ("COLUBRIS-SYSLOG-MIB", "syslogMessageRegEx"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSyslogMIBGroup = colubrisSyslogMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisSyslogMIBGroup.setDescription('A collection of objects providing the Syslog MIB capability.')
colubrisSyslogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2, 2)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogSeverityNotification"), ("COLUBRIS-SYSLOG-MIB", "syslogRegExMatchNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSyslogNotificationGroup = colubrisSyslogNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisSyslogNotificationGroup.setDescription('A collection of supported notifications.')
mibBuilder.exportSymbols("COLUBRIS-SYSLOG-MIB", syslogMsgText=syslogMsgText, colubrisSyslogMIBGroup=colubrisSyslogMIBGroup, syslogMessage=syslogMessage, syslogRegExMatchNotificationEnabled=syslogRegExMatchNotificationEnabled, colubrisSyslogMIBConformance=colubrisSyslogMIBConformance, colubrisSyslogMIBGroups=colubrisSyslogMIBGroups, colubrisSyslogMIBNotifications=colubrisSyslogMIBNotifications, syslogConfig=syslogConfig, colubrisSyslogMIBObjects=colubrisSyslogMIBObjects, PYSNMP_MODULE_ID=colubrisSyslogMIB, syslogMsgSeverity=syslogMsgSeverity, colubrisSyslogMIBNotificationPrefix=colubrisSyslogMIBNotificationPrefix, colubrisSyslogNotificationGroup=colubrisSyslogNotificationGroup, syslogRegExMatchNotification=syslogRegExMatchNotification, SyslogSeverity=SyslogSeverity, colubrisSyslogMIBCompliance=colubrisSyslogMIBCompliance, syslogSeverityNotification=syslogSeverityNotification, syslogMsgNumber=syslogMsgNumber, colubrisSyslogMIBCompliances=colubrisSyslogMIBCompliances, syslogSeverityLevel=syslogSeverityLevel, syslogMsgFacility=syslogMsgFacility, syslogTrapSeverityLevel=syslogTrapSeverityLevel, syslogMessageRegEx=syslogMessageRegEx, colubrisSyslogMIB=colubrisSyslogMIB, syslogSeverityNotificationEnabled=syslogSeverityNotificationEnabled)
