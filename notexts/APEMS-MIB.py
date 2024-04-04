#
# PySNMP MIB module APEMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APEMS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:42 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Bits, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType, MibIdentifier, ObjectIdentity, Unsigned32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType", "MibIdentifier", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
apEMSModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 8))
apEMSModule.setRevisions(('2012-07-16 00:00', '2014-06-26 00:00',))
if mibBuilder.loadTexts: apEMSModule.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apEMSModule.setOrganization('Oracle Communications')
apEMSMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 1))
apEMSNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2))
apEMSDiscoveryMode = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("discovery", 1), ("reDiscovery", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMSDiscoveryMode.setStatus('current')
apEMSNodeID = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMSNodeID.setStatus('current')
apEMSStartTime = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMSStartTime.setStatus('current')
apEMSDateTime = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMSDateTime.setStatus('current')
apEMSUser = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMSUser.setStatus('current')
apEMSDeviceAddress = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMSDeviceAddress.setStatus('current')
apEMSFunction = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("discovery", 1), ("reDiscovery", 2), ("save", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMSFunction.setStatus('current')
apEMSNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3))
apEMSConfigNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1))
apEMSConfigNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0))
apEMSDiscoveryFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 1)).setObjects(("APEMS-MIB", "apEMSDiscoveryMode"), ("APEMS-MIB", "apEMSNodeID"), ("APEMS-MIB", "apEMSStartTime"), ("APEMS-MIB", "apEMSDateTime"), ("APEMS-MIB", "apEMSUser"))
if mibBuilder.loadTexts: apEMSDiscoveryFailure.setStatus('current')
apEMSSaveFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 2)).setObjects(("APEMS-MIB", "apEMSNodeID"), ("APEMS-MIB", "apEMSStartTime"), ("APEMS-MIB", "apEMSDateTime"), ("APEMS-MIB", "apEMSUser"))
if mibBuilder.loadTexts: apEMSSaveFailure.setStatus('current')
apEMSActivateFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 3)).setObjects(("APEMS-MIB", "apEMSNodeID"), ("APEMS-MIB", "apEMSStartTime"), ("APEMS-MIB", "apEMSDateTime"), ("APEMS-MIB", "apEMSUser"))
if mibBuilder.loadTexts: apEMSActivateFailure.setStatus('current')
apEMSInvalidConfigDiscovered = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 4)).setObjects(("APEMS-MIB", "apEMSNodeID"), ("APEMS-MIB", "apEMSDateTime"))
if mibBuilder.loadTexts: apEMSInvalidConfigDiscovered.setStatus('current')
apEMSInvalidConfigInventory = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 5)).setObjects(("APEMS-MIB", "apEMSFunction"), ("APEMS-MIB", "apEMSNodeID"), ("APEMS-MIB", "apEMSStartTime"), ("APEMS-MIB", "apEMSDateTime"), ("APEMS-MIB", "apEMSUser"))
if mibBuilder.loadTexts: apEMSInvalidConfigInventory.setStatus('current')
apEMSDeviceHealthNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2))
apEMSDeviceHealthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2, 0))
apEMSNodeUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2, 0, 1)).setObjects(("APEMS-MIB", "apEMSDeviceAddress"), ("APEMS-MIB", "apEMSDateTime"))
if mibBuilder.loadTexts: apEMSNodeUnreachable.setStatus('current')
apEMSNodeUnreachableClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2, 0, 2)).setObjects(("APEMS-MIB", "apEMSDeviceAddress"), ("APEMS-MIB", "apEMSDateTime"))
if mibBuilder.loadTexts: apEMSNodeUnreachableClear.setStatus('current')
apEMSModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 4))
apEMSGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 1))
apEMSNotificationsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 2))
apEMSNotificationObjectsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 3))
apEMSConfigNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 2, 1)).setObjects(("APEMS-MIB", "apEMSDiscoveryFailure"), ("APEMS-MIB", "apEMSSaveFailure"), ("APEMS-MIB", "apEMSActivateFailure"), ("APEMS-MIB", "apEMSInvalidConfigDiscovered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEMSConfigNotificationsGroup = apEMSConfigNotificationsGroup.setStatus('current')
apEMSDeviceHealthNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 2, 2)).setObjects(("APEMS-MIB", "apEMSNodeUnreachable"), ("APEMS-MIB", "apEMSNodeUnreachableClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEMSDeviceHealthNotificationsGroup = apEMSDeviceHealthNotificationsGroup.setStatus('current')
apEMSNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 3, 1)).setObjects(("APEMS-MIB", "apEMSDiscoveryMode"), ("APEMS-MIB", "apEMSNodeID"), ("APEMS-MIB", "apEMSStartTime"), ("APEMS-MIB", "apEMSDateTime"), ("APEMS-MIB", "apEMSUser"), ("APEMS-MIB", "apEMSDeviceAddress"), ("APEMS-MIB", "apEMSFunction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEMSNotificationObjectsGroup = apEMSNotificationObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("APEMS-MIB", apEMSNodeUnreachableClear=apEMSNodeUnreachableClear, apEMSNotificationObjectsGroup=apEMSNotificationObjectsGroup, PYSNMP_MODULE_ID=apEMSModule, apEMSDiscoveryMode=apEMSDiscoveryMode, apEMSNotificationObjects=apEMSNotificationObjects, apEMSInvalidConfigInventory=apEMSInvalidConfigInventory, apEMSGroups=apEMSGroups, apEMSNotifications=apEMSNotifications, apEMSNotificationsGroups=apEMSNotificationsGroups, apEMSUser=apEMSUser, apEMSConfigNotificationsPrefix=apEMSConfigNotificationsPrefix, apEMSFunction=apEMSFunction, apEMSNodeUnreachable=apEMSNodeUnreachable, apEMSMIBObjects=apEMSMIBObjects, apEMSSaveFailure=apEMSSaveFailure, apEMSConfigNotificationsGroup=apEMSConfigNotificationsGroup, apEMSDeviceHealthNotificationsGroup=apEMSDeviceHealthNotificationsGroup, apEMSDeviceHealthNotificationsPrefix=apEMSDeviceHealthNotificationsPrefix, apEMSModuleConformance=apEMSModuleConformance, apEMSNodeID=apEMSNodeID, apEMSNotificationObjectsGroups=apEMSNotificationObjectsGroups, apEMSDiscoveryFailure=apEMSDiscoveryFailure, apEMSActivateFailure=apEMSActivateFailure, apEMSDateTime=apEMSDateTime, apEMSDeviceAddress=apEMSDeviceAddress, apEMSInvalidConfigDiscovered=apEMSInvalidConfigDiscovered, apEMSModule=apEMSModule, apEMSDeviceHealthNotifications=apEMSDeviceHealthNotifications, apEMSStartTime=apEMSStartTime, apEMSConfigNotifications=apEMSConfigNotifications)
