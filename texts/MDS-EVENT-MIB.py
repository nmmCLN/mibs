#
# PySNMP MIB module MDS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-EVENT-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:28:33 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
mdsLogging, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsLogging")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Counter64, TimeTicks, Integer32, Counter32, ObjectIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "Integer32", "Counter32", "ObjectIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mdsEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1))
mdsEventMIB.setRevisions(('2018-05-16 00:00', '2013-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsEventMIB.setRevisionsDescriptions(('Updated conformance statments based on smilint.', 'Initial version.',))
if mibBuilder.loadTexts: mdsEventMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsEventMIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsEventMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n        T 585-242-9600\n        F 585-242-9620\n\n        175 Science Parkway\n        Rochester, New York 14620\n        USA')
if mibBuilder.loadTexts: mdsEventMIB.setDescription('Notifications for GE MDS products.')
mdsEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1))
mdsEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2))
mdsEventVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1))
mdsEventName = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdsEventName.setStatus('current')
if mibBuilder.loadTexts: mdsEventName.setDescription('The name of the event.')
mdsEventInfoInCee = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdsEventInfoInCee.setStatus('current')
if mibBuilder.loadTexts: mdsEventInfoInCee.setDescription('The detailed information about the event encoded \n        in Common Event Expression (CEE) format.')
traps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0))
mdsEvent = NotificationType((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0, 1))
if mibBuilder.loadTexts: mdsEvent.setStatus('current')
if mibBuilder.loadTexts: mdsEvent.setDescription('This is the common notification sent for any events\n        generated by various subsystems in the product.')
mdsEventMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3))
mdsEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1))
mdsEventMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2))
mdsEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1, 2)).setObjects(("MDS-EVENT-MIB", "mdsEventNotificationsGroup"), ("MDS-EVENT-MIB", "mdsEventVariablesCeeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventMIBCompliance = mdsEventMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: mdsEventMIBCompliance.setDescription('The compliance statement for SNMP entities that\n        implement the MDS-EVENT-MIB.')
mdsEventNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 1)).setObjects(("MDS-EVENT-MIB", "mdsEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventNotificationsGroup = mdsEventNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: mdsEventNotificationsGroup.setDescription('The common notifications.')
mdsEventVariablesCeeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 2)).setObjects(("MDS-EVENT-MIB", "mdsEventName"), ("MDS-EVENT-MIB", "mdsEventInfoInCee"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventVariablesCeeGroup = mdsEventVariablesCeeGroup.setStatus('current')
if mibBuilder.loadTexts: mdsEventVariablesCeeGroup.setDescription('Information to support events that encode event \n        information in CEE format.')
mibBuilder.exportSymbols("MDS-EVENT-MIB", mdsEventNotificationsGroup=mdsEventNotificationsGroup, mdsEventVariables=mdsEventVariables, mdsEventMIBGroups=mdsEventMIBGroups, traps0=traps0, mdsEventInfoInCee=mdsEventInfoInCee, mdsEventMIBNotifications=mdsEventMIBNotifications, mdsEventMIBCompliance=mdsEventMIBCompliance, mdsEvent=mdsEvent, mdsEventMIBCompliances=mdsEventMIBCompliances, PYSNMP_MODULE_ID=mdsEventMIB, mdsEventMIB=mdsEventMIB, mdsEventName=mdsEventName, mdsEventMIBConformance=mdsEventMIBConformance, mdsEventVariablesCeeGroup=mdsEventVariablesCeeGroup, traps=traps, mdsEventMIBObjects=mdsEventMIBObjects)
