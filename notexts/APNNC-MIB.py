#
# PySNMP MIB module APNNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APNNC-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
apEMSModule, = mibBuilder.importSymbols("APEMS-MIB", "apEMSModule")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, NotificationType, MibIdentifier, iso, Unsigned32, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "iso", "Unsigned32", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
apNNCModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5))
apNNCModule.setRevisions(('2012-08-20 00:00', '2012-07-16 00:00', '2013-10-11 00:00', '2013-10-14 00:00', '2014-02-27 00:00', '2014-06-26 00:00', '2015-09-15 00:00', '2017-02-15 00:00', '2017-07-07 00:00', '2018-04-25 00:00',))
if mibBuilder.loadTexts: apNNCModule.setLastUpdated('201804250000Z')
if mibBuilder.loadTexts: apNNCModule.setOrganization('Oracle Communications')
apNNCMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 1))
apNNCNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2))
apNNCServerAddressRemote = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCServerAddressRemote.setStatus('current')
apNNCServerNameRemote = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCServerNameRemote.setStatus('current')
apNNCServerAddressLocal = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCServerAddressLocal.setStatus('current')
apNNCServerNameLocal = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCServerNameLocal.setStatus('current')
apNNCFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCFailureReason.setStatus('current')
apNNCAggregationTimePercent = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCAggregationTimePercent.setStatus('deprecated')
apNNCAggregationLagPercent = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 7), Integer32()).setUnits('%').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCAggregationLagPercent.setStatus('current')
apOCSDMServerMasterAddress = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCSDMServerMasterAddress.setStatus('current')
apOCSDMServerMasterName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCSDMServerMasterName.setStatus('current')
apOCSDMServerTrapInterval = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCSDMServerTrapInterval.setStatus('current')
apEMPluginNameLocal = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 11), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMPluginNameLocal.setStatus('current')
apEMPluginRestPrefixName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 12), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEMPluginRestPrefixName.setStatus('current')
apNNCReportingUser = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 13), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCReportingUser.setStatus('current')
apNNCReportingPswdExpiryDate = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 14), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCReportingPswdExpiryDate.setStatus('current')
apNNCFraudProtectionListName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 15), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCFraudProtectionListName.setStatus('current')
apNNCFraudProtectionListSizeLimit = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 16), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCFraudProtectionListSizeLimit.setStatus('current')
apNNCNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3))
apNNCServerHealthNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1))
apNNCServerHealthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0))
apNNCServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 1)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCServerAddressRemote"), ("APNNC-MIB", "apNNCServerNameRemote"))
if mibBuilder.loadTexts: apNNCServerUnreachable.setStatus('current')
apNNCServerUnreachableClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 2)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCServerAddressRemote"), ("APNNC-MIB", "apNNCServerNameRemote"))
if mibBuilder.loadTexts: apNNCServerUnreachableClear.setStatus('current')
apNNCTrapRelayNotAliveNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 3)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"))
if mibBuilder.loadTexts: apNNCTrapRelayNotAliveNotification.setStatus('current')
apNNCTrapRelayAliveNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 4)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"))
if mibBuilder.loadTexts: apNNCTrapRelayAliveNotification.setStatus('current')
apOCSDMSeverHeartbeatReachable = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 5)).setObjects(("APNNC-MIB", "apOCSDMServerMasterAddress"), ("APNNC-MIB", "apOCSDMServerMasterName"), ("APNNC-MIB", "apOCSDMServerTrapInterval"))
if mibBuilder.loadTexts: apOCSDMSeverHeartbeatReachable.setStatus('current')
apEMPluginFailedInstall = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 6)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apEMPluginNameLocal"))
if mibBuilder.loadTexts: apEMPluginFailedInstall.setStatus('current')
apEMPluginFailedInstallClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 7)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apEMPluginNameLocal"))
if mibBuilder.loadTexts: apEMPluginFailedInstallClear.setStatus('current')
apEMPluginFailedUninstall = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 8)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apEMPluginNameLocal"))
if mibBuilder.loadTexts: apEMPluginFailedUninstall.setStatus('current')
apEMPluginFailedUninstallClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 9)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apEMPluginNameLocal"))
if mibBuilder.loadTexts: apEMPluginFailedUninstallClear.setStatus('current')
apEMPluginDuplicatedRestPrefixName = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 10)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apEMPluginNameLocal"), ("APNNC-MIB", "apEMPluginRestPrefixName"))
if mibBuilder.loadTexts: apEMPluginDuplicatedRestPrefixName.setStatus('current')
apNNCReportingNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2))
apNNCReportingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0))
apNNCReportingHdrDetectionFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 1)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"))
if mibBuilder.loadTexts: apNNCReportingHdrDetectionFailure.setStatus('current')
apNNCReportingHdrAggregationFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 2)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"), ("APNNC-MIB", "apNNCAggregationTimePercent"))
if mibBuilder.loadTexts: apNNCReportingHdrAggregationFailure.setStatus('deprecated')
apNNCReportingHdrAggregationFailureClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 3)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"), ("APNNC-MIB", "apNNCAggregationTimePercent"))
if mibBuilder.loadTexts: apNNCReportingHdrAggregationFailureClear.setStatus('deprecated')
apNNCReportingHdrAggregationLagFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 4)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"), ("APNNC-MIB", "apNNCAggregationLagPercent"))
if mibBuilder.loadTexts: apNNCReportingHdrAggregationLagFailure.setStatus('current')
apNNCReportingHdrAggregationLagFailureClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 5)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"), ("APNNC-MIB", "apNNCAggregationLagPercent"))
if mibBuilder.loadTexts: apNNCReportingHdrAggregationLagFailureClear.setStatus('current')
apNNCReportingPswdExpiration = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 6)).setObjects(("APNNC-MIB", "apNNCReportingUser"), ("APNNC-MIB", "apNNCReportingPswdExpiryDate"), ("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"))
if mibBuilder.loadTexts: apNNCReportingPswdExpiration.setStatus('current')
apNNCReportingPswdExpirationClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 7)).setObjects(("APNNC-MIB", "apNNCReportingUser"), ("APNNC-MIB", "apNNCReportingPswdExpiryDate"), ("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCFailureReason"))
if mibBuilder.loadTexts: apNNCReportingPswdExpirationClear.setStatus('current')
apOCSDMFraudProtectionNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 3))
apOCSDMFraudProtectionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 3, 0))
apOCSDMFPLSizeExceedLimit = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 3, 0, 1)).setObjects(("APNNC-MIB", "apNNCFraudProtectionListName"), ("APNNC-MIB", "apNNCFraudProtectionListSizeLimit"))
if mibBuilder.loadTexts: apOCSDMFPLSizeExceedLimit.setStatus('current')
apNNCModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4))
apNNCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 1))
apNNCNotificationsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2))
apNNCNotificationObjectsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3))
apNNCServerHealthObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 1)).setObjects(("APNNC-MIB", "apNNCServerAddressLocal"), ("APNNC-MIB", "apNNCServerNameLocal"), ("APNNC-MIB", "apNNCServerAddressRemote"), ("APNNC-MIB", "apNNCServerNameRemote"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCServerHealthObjectsGroup = apNNCServerHealthObjectsGroup.setStatus('current')
apNNCFailureObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 2)).setObjects(("APNNC-MIB", "apNNCFailureReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCFailureObjectsGroup = apNNCFailureObjectsGroup.setStatus('current')
apNNCTimePercentObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 3)).setObjects(("APNNC-MIB", "apNNCAggregationTimePercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCTimePercentObjectsGroup = apNNCTimePercentObjectsGroup.setStatus('deprecated')
apNNCTimePercentObjGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 4)).setObjects(("APNNC-MIB", "apNNCAggregationLagPercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCTimePercentObjGroup = apNNCTimePercentObjGroup.setStatus('current')
apNNCServerHealthNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 1)).setObjects(("APNNC-MIB", "apNNCServerUnreachable"), ("APNNC-MIB", "apNNCServerUnreachableClear"), ("APNNC-MIB", "apNNCTrapRelayNotAliveNotification"), ("APNNC-MIB", "apNNCTrapRelayAliveNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCServerHealthNotificationsGroup = apNNCServerHealthNotificationsGroup.setStatus('current')
apNNCReportingNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 2)).setObjects(("APNNC-MIB", "apNNCReportingHdrDetectionFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCReportingNotificationsGroup = apNNCReportingNotificationsGroup.setStatus('current')
apNNCReportingAggrNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 3)).setObjects(("APNNC-MIB", "apNNCReportingHdrAggregationFailure"), ("APNNC-MIB", "apNNCReportingHdrAggregationFailureClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCReportingAggrNotifsGroup = apNNCReportingAggrNotifsGroup.setStatus('deprecated')
apNNCReportingAggregationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 4)).setObjects(("APNNC-MIB", "apNNCReportingHdrAggregationLagFailure"), ("APNNC-MIB", "apNNCReportingHdrAggregationLagFailureClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCReportingAggregationNotificationGroup = apNNCReportingAggregationNotificationGroup.setStatus('current')
apNNCServerHealthbeatNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 5)).setObjects(("APNNC-MIB", "apOCSDMSeverHeartbeatReachable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCServerHealthbeatNotificationsGroup = apNNCServerHealthbeatNotificationsGroup.setStatus('current')
apNNCPluginNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 6)).setObjects(("APNNC-MIB", "apEMPluginFailedInstall"), ("APNNC-MIB", "apEMPluginFailedInstallClear"), ("APNNC-MIB", "apEMPluginFailedUninstall"), ("APNNC-MIB", "apEMPluginFailedUninstallClear"), ("APNNC-MIB", "apEMPluginDuplicatedRestPrefixName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCPluginNotificationsGroup = apNNCPluginNotificationsGroup.setStatus('current')
apOCSDMFraudProtectionNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 7)).setObjects(("APNNC-MIB", "apOCSDMFPLSizeExceedLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apOCSDMFraudProtectionNotificationsGroup = apOCSDMFraudProtectionNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("APNNC-MIB", apOCSDMServerMasterName=apOCSDMServerMasterName, apNNCReportingPswdExpirationClear=apNNCReportingPswdExpirationClear, apOCSDMServerMasterAddress=apOCSDMServerMasterAddress, apNNCReportingAggrNotifsGroup=apNNCReportingAggrNotifsGroup, apEMPluginFailedUninstall=apEMPluginFailedUninstall, apNNCServerUnreachableClear=apNNCServerUnreachableClear, apNNCNotificationObjects=apNNCNotificationObjects, apNNCReportingHdrAggregationLagFailureClear=apNNCReportingHdrAggregationLagFailureClear, apNNCFraudProtectionListName=apNNCFraudProtectionListName, apNNCPluginNotificationsGroup=apNNCPluginNotificationsGroup, apNNCTrapRelayNotAliveNotification=apNNCTrapRelayNotAliveNotification, apNNCServerHealthNotificationsGroup=apNNCServerHealthNotificationsGroup, apOCSDMFraudProtectionNotificationsPrefix=apOCSDMFraudProtectionNotificationsPrefix, apEMPluginRestPrefixName=apEMPluginRestPrefixName, apNNCModule=apNNCModule, apNNCFailureReason=apNNCFailureReason, apNNCTrapRelayAliveNotification=apNNCTrapRelayAliveNotification, apNNCReportingHdrDetectionFailure=apNNCReportingHdrDetectionFailure, apOCSDMServerTrapInterval=apOCSDMServerTrapInterval, apNNCReportingHdrAggregationLagFailure=apNNCReportingHdrAggregationLagFailure, apEMPluginNameLocal=apEMPluginNameLocal, apNNCAggregationLagPercent=apNNCAggregationLagPercent, apEMPluginFailedInstallClear=apEMPluginFailedInstallClear, apNNCServerAddressRemote=apNNCServerAddressRemote, apNNCFailureObjectsGroup=apNNCFailureObjectsGroup, apOCSDMFPLSizeExceedLimit=apOCSDMFPLSizeExceedLimit, apNNCTimePercentObjGroup=apNNCTimePercentObjGroup, apEMPluginFailedUninstallClear=apEMPluginFailedUninstallClear, apNNCServerHealthNotificationsPrefix=apNNCServerHealthNotificationsPrefix, apOCSDMFraudProtectionNotificationsGroup=apOCSDMFraudProtectionNotificationsGroup, apNNCTimePercentObjectsGroup=apNNCTimePercentObjectsGroup, apNNCServerNameLocal=apNNCServerNameLocal, apOCSDMFraudProtectionNotifications=apOCSDMFraudProtectionNotifications, apNNCNotificationObjectsGroups=apNNCNotificationObjectsGroups, apNNCNotifications=apNNCNotifications, apNNCServerHealthbeatNotificationsGroup=apNNCServerHealthbeatNotificationsGroup, apNNCAggregationTimePercent=apNNCAggregationTimePercent, apNNCServerUnreachable=apNNCServerUnreachable, apNNCModuleConformance=apNNCModuleConformance, apNNCReportingNotificationsGroup=apNNCReportingNotificationsGroup, apNNCNotificationsGroups=apNNCNotificationsGroups, apNNCServerNameRemote=apNNCServerNameRemote, apNNCServerHealthObjectsGroup=apNNCServerHealthObjectsGroup, apNNCServerHealthNotifications=apNNCServerHealthNotifications, apEMPluginFailedInstall=apEMPluginFailedInstall, apNNCReportingNotificationsPrefix=apNNCReportingNotificationsPrefix, apNNCReportingHdrAggregationFailure=apNNCReportingHdrAggregationFailure, apOCSDMSeverHeartbeatReachable=apOCSDMSeverHeartbeatReachable, apEMPluginDuplicatedRestPrefixName=apEMPluginDuplicatedRestPrefixName, apNNCReportingUser=apNNCReportingUser, PYSNMP_MODULE_ID=apNNCModule, apNNCServerAddressLocal=apNNCServerAddressLocal, apNNCReportingPswdExpiryDate=apNNCReportingPswdExpiryDate, apNNCReportingPswdExpiration=apNNCReportingPswdExpiration, apNNCGroups=apNNCGroups, apNNCReportingAggregationNotificationGroup=apNNCReportingAggregationNotificationGroup, apNNCReportingNotifications=apNNCReportingNotifications, apNNCFraudProtectionListSizeLimit=apNNCFraudProtectionListSizeLimit, apNNCReportingHdrAggregationFailureClear=apNNCReportingHdrAggregationFailureClear, apNNCMIBObjects=apNNCMIBObjects)
