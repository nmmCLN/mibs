#
# PySNMP MIB module APAPPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAPPS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ApPhyPortType, ApCommMonitorState, ApRedundancyState, ApServerStatus, ApPresence, ApHardwareModuleFamily, ApAclType = mibBuilder.importSymbols("ACMEPACKET-TC", "ApPhyPortType", "ApCommMonitorState", "ApRedundancyState", "ApServerStatus", "ApPresence", "ApHardwareModuleFamily", "ApAclType")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, NotificationType, Counter64, MibIdentifier, iso, Unsigned32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Gauge32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "iso", "Unsigned32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Gauge32", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
apAppsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 16))
apAppsModule.setRevisions(('2012-03-07 00:00', '2014-06-26 00:00',))
if mibBuilder.loadTexts: apAppsModule.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apAppsModule.setOrganization('Oracle Communications')
apAppsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1))
apAppsMIBGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 1))
apAppsMIBTabularObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2))
apAppsENUMTabularObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1))
apAppsDNSTabularObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2))
apAppsNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2))
apAppsNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 1))
apAppsNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2))
apAppsEnumNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 1))
apAppsEnumNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 1, 0))
apAppsDnsNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 2))
apAppsDnsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 2, 0))
apAppsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3))
apAppsObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1))
apAppsNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2))
apAppsAclObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 4))
apAppsENUMServerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1), )
if mibBuilder.loadTexts: apAppsENUMServerStatusTable.setStatus('current')
apAppsENUMServerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1), ).setIndexNames((0, "APAPPS-MIB", "apAppsENUMConfigName"), (0, "APAPPS-MIB", "apAppsENUMServerInetAddressType"), (0, "APAPPS-MIB", "apAppsENUMServerInetAddress"))
if mibBuilder.loadTexts: apAppsENUMServerStatusEntry.setStatus('current')
apAppsENUMConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsENUMConfigName.setStatus('current')
apAppsENUMServerInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsENUMServerInetAddressType.setStatus('current')
apAppsENUMServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsENUMServerInetAddress.setStatus('current')
apAppsENUMServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 4), ApServerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsENUMServerStatus.setStatus('current')
apAppsDnsServerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1), )
if mibBuilder.loadTexts: apAppsDnsServerStatusTable.setStatus('current')
apAppsDnsServerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1), ).setIndexNames((0, "APAPPS-MIB", "apAppsDnsInterfaceName"), (0, "APAPPS-MIB", "apAppsDnsServerInetAddressType"), (0, "APAPPS-MIB", "apAppsDnsServerInetAddress"))
if mibBuilder.loadTexts: apAppsDnsServerStatusEntry.setStatus('current')
apAppsDnsInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsDnsInterfaceName.setStatus('current')
apAppsDnsServerInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsDnsServerInetAddressType.setStatus('current')
apAppsDnsServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsDnsServerInetAddress.setStatus('current')
apAppsDnsServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 4), ApServerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppsDnsServerStatus.setStatus('current')
apEnumServerRateStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2), )
if mibBuilder.loadTexts: apEnumServerRateStatsTable.setStatus('current')
apEnumServerRateStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1), )
apAppsENUMServerStatusEntry.registerAugmentions(("APAPPS-MIB", "apEnumServerRateStatsEntry"))
apEnumServerRateStatsEntry.setIndexNames(*apAppsENUMServerStatusEntry.getIndexNames())
if mibBuilder.loadTexts: apEnumServerRateStatsEntry.setStatus('current')
apEnumServerRateMsgRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 5), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnumServerRateMsgRcvd.setStatus('current')
apEnumServerRateMsgSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 6), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnumServerRateMsgSent.setStatus('current')
apEnumServerRateReqRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 7), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnumServerRateReqRcvd.setStatus('current')
apEnumServerRateReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 8), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnumServerRateReqSent.setStatus('current')
apEnumServerRateRspRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 9), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnumServerRateRspRcvd.setStatus('current')
apEnumServerRateRspSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 10), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnumServerRateRspSent.setStatus('current')
apAppsENUMServerStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 1, 0, 1)).setObjects(("APAPPS-MIB", "apAppsENUMConfigName"), ("APAPPS-MIB", "apAppsENUMServerInetAddressType"), ("APAPPS-MIB", "apAppsENUMServerInetAddress"), ("APAPPS-MIB", "apAppsENUMServerStatus"))
if mibBuilder.loadTexts: apAppsENUMServerStatusChangeTrap.setStatus('current')
apAppsDnsServerStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 2, 0, 1)).setObjects(("APAPPS-MIB", "apAppsDnsInterfaceName"), ("APAPPS-MIB", "apAppsDnsServerInetAddressType"), ("APAPPS-MIB", "apAppsDnsServerInetAddress"), ("APAPPS-MIB", "apAppsDnsServerStatus"))
if mibBuilder.loadTexts: apAppsDnsServerStatusChangeTrap.setStatus('current')
apAppsENUMServerStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1, 1)).setObjects(("APAPPS-MIB", "apAppsENUMConfigName"), ("APAPPS-MIB", "apAppsENUMServerInetAddressType"), ("APAPPS-MIB", "apAppsENUMServerInetAddress"), ("APAPPS-MIB", "apAppsENUMServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMServerStatusGroup = apAppsENUMServerStatusGroup.setStatus('current')
apAppsDnsServerStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1, 2)).setObjects(("APAPPS-MIB", "apAppsDnsInterfaceName"), ("APAPPS-MIB", "apAppsDnsServerInetAddressType"), ("APAPPS-MIB", "apAppsDnsServerInetAddress"), ("APAPPS-MIB", "apAppsDnsServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDnsServerStatusGroup = apAppsDnsServerStatusGroup.setStatus('current')
apAppsENUMServerRateStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1, 3)).setObjects(("APAPPS-MIB", "apEnumServerRateMsgRcvd"), ("APAPPS-MIB", "apEnumServerRateMsgSent"), ("APAPPS-MIB", "apEnumServerRateReqRcvd"), ("APAPPS-MIB", "apEnumServerRateReqSent"), ("APAPPS-MIB", "apEnumServerRateRspRcvd"), ("APAPPS-MIB", "apEnumServerRateRspSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMServerRateStatsGroup = apAppsENUMServerRateStatsGroup.setStatus('current')
apAppsEnumServerNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 1)).setObjects(("APAPPS-MIB", "apAppsENUMServerStatusChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsEnumServerNotificationsGroup = apAppsEnumServerNotificationsGroup.setStatus('current')
apAppsDnsServerNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 2)).setObjects(("APAPPS-MIB", "apAppsDnsServerStatusChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDnsServerNotificationsGroup = apAppsDnsServerNotificationsGroup.setStatus('current')
apAppsCommMonitorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 3))
apCommMonitorStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 3, 1), )
if mibBuilder.loadTexts: apCommMonitorStatsTable.setStatus('current')
apCommMonitorStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 3, 1, 1), ).setIndexNames((0, "APAPPS-MIB", "apCommMonitorInetAddressType"), (0, "APAPPS-MIB", "apCommMonitorInetAddress"))
if mibBuilder.loadTexts: apCommMonitorStatsEntry.setStatus('current')
apCommMonitorInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 3, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: apCommMonitorInetAddressType.setStatus('current')
apCommMonitorInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 3, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: apCommMonitorInetAddress.setStatus('current')
apCommMonitorState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 3, 1, 1, 3), ApCommMonitorState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apCommMonitorState.setStatus('current')
apCommMonitorNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 3))
apCommMonitorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 3, 0))
apMonitorCollectorDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 3, 0, 1)).setObjects(("APAPPS-MIB", "apCommMonitorState"))
if mibBuilder.loadTexts: apMonitorCollectorDownTrap.setStatus('current')
apMonitorCollectorClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 3, 0, 2)).setObjects(("APAPPS-MIB", "apCommMonitorState"))
if mibBuilder.loadTexts: apMonitorCollectorClearTrap.setStatus('current')
apCommMonitorNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 3))
apCommMonitorNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 3, 1)).setObjects(("APAPPS-MIB", "apMonitorCollectorDownTrap"), ("APAPPS-MIB", "apMonitorCollectorClearTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCommMonitorNotificationsGroup = apCommMonitorNotificationsGroup.setStatus('current')
apAclDropObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 4, 1))
apAclDropType = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 16, 4, 1, 1), ApAclType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apAclDropType.setStatus('current')
apAclDropCount = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 16, 4, 1, 2), Counter32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apAclDropCount.setStatus('current')
apAclDropRatio = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 16, 4, 1, 3), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apAclDropRatio.setStatus('current')
apAppsAclNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 4))
apAppsAclNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 4, 0))
apAclDropOverThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 4, 0, 1)).setObjects(("APAPPS-MIB", "apAclDropType"), ("APAPPS-MIB", "apAclDropCount"), ("APAPPS-MIB", "apAclDropRatio"))
if mibBuilder.loadTexts: apAclDropOverThresholdTrap.setStatus('current')
apAclDropOverThresholdClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 4, 0, 2)).setObjects(("APAPPS-MIB", "apAclDropType"), ("APAPPS-MIB", "apAclDropCount"), ("APAPPS-MIB", "apAclDropRatio"))
if mibBuilder.loadTexts: apAclDropOverThresholdClearTrap.setStatus('current')
apAclNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 4))
apAclDropNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 4, 1)).setObjects(("APAPPS-MIB", "apAclDropOverThresholdTrap"), ("APAPPS-MIB", "apAclDropOverThresholdClearTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAclDropNotificationsGroup = apAclDropNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("APAPPS-MIB", apAppsNotifPrefix=apAppsNotifPrefix, apAppsDnsServerInetAddressType=apAppsDnsServerInetAddressType, apEnumServerRateMsgSent=apEnumServerRateMsgSent, apAppsNotificationGroups=apAppsNotificationGroups, apAppsConformance=apAppsConformance, apEnumServerRateReqSent=apEnumServerRateReqSent, apAppsDnsServerStatus=apAppsDnsServerStatus, apAppsENUMServerStatusEntry=apAppsENUMServerStatusEntry, apAppsDnsInterfaceName=apAppsDnsInterfaceName, apMonitorCollectorDownTrap=apMonitorCollectorDownTrap, apAppsDNSTabularObjects=apAppsDNSTabularObjects, apAppsDnsServerStatusEntry=apAppsDnsServerStatusEntry, apMonitorCollectorClearTrap=apMonitorCollectorClearTrap, apAclDropType=apAclDropType, apAppsENUMServerStatusGroup=apAppsENUMServerStatusGroup, apCommMonitorState=apCommMonitorState, apAclDropObjects=apAclDropObjects, apAppsDnsServerInetAddress=apAppsDnsServerInetAddress, apAppsNotifObjects=apAppsNotifObjects, apCommMonitorNotif=apCommMonitorNotif, apAclNotificationGroups=apAclNotificationGroups, apAppsENUMServerStatus=apAppsENUMServerStatus, apEnumServerRateReqRcvd=apEnumServerRateReqRcvd, apAclDropCount=apAclDropCount, apAppsENUMServerInetAddress=apAppsENUMServerInetAddress, apAppsENUMServerStatusTable=apAppsENUMServerStatusTable, apCommMonitorNotificationsGroup=apCommMonitorNotificationsGroup, apAclDropOverThresholdTrap=apAclDropOverThresholdTrap, apAppsDnsNotifications=apAppsDnsNotifications, apEnumServerRateRspSent=apEnumServerRateRspSent, apAppsENUMServerRateStatsGroup=apAppsENUMServerRateStatsGroup, apAppsObjectGroups=apAppsObjectGroups, apAppsENUMServerInetAddressType=apAppsENUMServerInetAddressType, apEnumServerRateStatsEntry=apEnumServerRateStatsEntry, apCommMonitorInetAddress=apCommMonitorInetAddress, apAppsDnsServerNotificationsGroup=apAppsDnsServerNotificationsGroup, apAppsMIBObjects=apAppsMIBObjects, PYSNMP_MODULE_ID=apAppsModule, apAppsMIBTabularObjects=apAppsMIBTabularObjects, apAppsModule=apAppsModule, apAppsDnsServerStatusTable=apAppsDnsServerStatusTable, apAppsAclNotif=apAppsAclNotif, apAppsAclNotifications=apAppsAclNotifications, apAppsDnsServerStatusGroup=apAppsDnsServerStatusGroup, apAclDropNotificationsGroup=apAclDropNotificationsGroup, apEnumServerRateStatsTable=apEnumServerRateStatsTable, apAppsEnumServerNotificationsGroup=apAppsEnumServerNotificationsGroup, apAppsMIBGeneralObjects=apAppsMIBGeneralObjects, apCommMonitorNotificationGroups=apCommMonitorNotificationGroups, apAppsEnumNotifications=apAppsEnumNotifications, apAppsEnumNotif=apAppsEnumNotif, apAclDropRatio=apAclDropRatio, apEnumServerRateRspRcvd=apEnumServerRateRspRcvd, apAppsAclObjects=apAppsAclObjects, apCommMonitorStatsTable=apCommMonitorStatsTable, apCommMonitorInetAddressType=apCommMonitorInetAddressType, apAppsENUMServerStatusChangeTrap=apAppsENUMServerStatusChangeTrap, apAppsNotificationObjects=apAppsNotificationObjects, apAppsCommMonitorObjects=apAppsCommMonitorObjects, apAppsDnsNotif=apAppsDnsNotif, apAppsENUMTabularObjects=apAppsENUMTabularObjects, apCommMonitorStatsEntry=apCommMonitorStatsEntry, apAclDropOverThresholdClearTrap=apAclDropOverThresholdClearTrap, apAppsENUMConfigName=apAppsENUMConfigName, apCommMonitorNotifications=apCommMonitorNotifications, apEnumServerRateMsgRcvd=apEnumServerRateMsgRcvd, apAppsDnsServerStatusChangeTrap=apAppsDnsServerStatusChangeTrap)
