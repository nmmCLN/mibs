#
# PySNMP MIB module F5-EM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-EM-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:28:04 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
LongDisplayString, f5, bigipCompliances, bigipGroups = mibBuilder.importSymbols("F5-BIGIP-COMMON-MIB", "LongDisplayString", "f5", "bigipCompliances", "bigipGroups")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Opaque, Gauge32, enterprises, TimeTicks, Counter32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter64, ObjectIdentity, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Opaque", "Gauge32", "enterprises", "TimeTicks", "Counter32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter64", "ObjectIdentity", "MibIdentifier", "Unsigned32")
DateAndTime, TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString", "MacAddress")
enterpriseManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 3375, 3))
if mibBuilder.loadTexts: enterpriseManagement.setLastUpdated('201202072039Z')
if mibBuilder.loadTexts: enterpriseManagement.setOrganization('F5 Networks, Inc.')
if mibBuilder.loadTexts: enterpriseManagement.setContactInfo('postal: F5 Networks, Inc. \n\t \t  401 Elliott Ave. West \n                  Seattle, WA 98119\n          phone:  (206) 272-5555\n          email:  support@f5.com')
if mibBuilder.loadTexts: enterpriseManagement.setDescription('Top-level infrastructure of the F5 enterprise MIB tree.')
emDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 1))
emDeviceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 2))
emImages = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 3))
emArchives = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 4))
emGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 5))
emAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6))
emAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0))
emAlertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6, 1))
emAlertConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 0))
emDeviceList = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1))
deviceNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceNumber.setStatus('current')
if mibBuilder.loadTexts: deviceNumber.setDescription('The number of device entries in the table.')
deviceEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2), )
if mibBuilder.loadTexts: deviceEntryTable.setStatus('current')
if mibBuilder.loadTexts: deviceEntryTable.setDescription('The table of device.')
deviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "deviceName"))
if mibBuilder.loadTexts: deviceEntry.setStatus('current')
if mibBuilder.loadTexts: deviceEntry.setDescription('Columns in the deviceEntry Table')
deviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceName.setStatus('current')
if mibBuilder.loadTexts: deviceName.setDescription('The name of the device.')
deviceAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAddressType.setStatus('current')
if mibBuilder.loadTexts: deviceAddressType.setDescription('The type of IP address of the device.')
deviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAddress.setStatus('current')
if mibBuilder.loadTexts: deviceAddress.setDescription('The IP address of the device.')
groupNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupNumber.setStatus('current')
if mibBuilder.loadTexts: groupNumber.setDescription('The number of group entries in the table.')
groupEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2), )
if mibBuilder.loadTexts: groupEntryTable.setStatus('current')
if mibBuilder.loadTexts: groupEntryTable.setDescription('The table of groups.')
groupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "groupName"))
if mibBuilder.loadTexts: groupEntry.setStatus('current')
if mibBuilder.loadTexts: groupEntry.setDescription('Columns in the groupEntry Table')
groupName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupName.setStatus('current')
if mibBuilder.loadTexts: groupName.setDescription('A name for a group of managed devices.')
groupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupDescription.setStatus('current')
if mibBuilder.loadTexts: groupDescription.setDescription('A description of a group of managed devices.')
imageNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imageNumber.setStatus('current')
if mibBuilder.loadTexts: imageNumber.setDescription('The number of image entries in the table.')
imageEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2), )
if mibBuilder.loadTexts: imageEntryTable.setStatus('current')
if mibBuilder.loadTexts: imageEntryTable.setDescription('The table of images.')
imageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "imageVersion"))
if mibBuilder.loadTexts: imageEntry.setStatus('current')
if mibBuilder.loadTexts: imageEntry.setDescription('Columns in the imageEntry Table')
imageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imageVersion.setStatus('current')
if mibBuilder.loadTexts: imageVersion.setDescription('The software version, including build number and hotfixes.')
imageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imageDescription.setStatus('current')
if mibBuilder.loadTexts: imageDescription.setDescription('Further details about the contents of an iso image.')
archiveNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveNumber.setStatus('obsolete')
if mibBuilder.loadTexts: archiveNumber.setDescription('The number of archive entries in the table.')
archiveEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2), )
if mibBuilder.loadTexts: archiveEntryTable.setStatus('obsolete')
if mibBuilder.loadTexts: archiveEntryTable.setDescription('The table of archives.')
archiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "archiveSourceDevice"))
if mibBuilder.loadTexts: archiveEntry.setStatus('obsolete')
if mibBuilder.loadTexts: archiveEntry.setDescription('Columns in the archiveEntry Table')
archiveSourceDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveSourceDevice.setStatus('obsolete')
if mibBuilder.loadTexts: archiveSourceDevice.setDescription('The name of the device from which the archive came.')
archiveProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveProduct.setStatus('obsolete')
if mibBuilder.loadTexts: archiveProduct.setDescription('The type of software running on the device from which the\narchive came.')
archiveVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveVersion.setStatus('obsolete')
if mibBuilder.loadTexts: archiveVersion.setDescription('The software version, including build number, of the device\nfrom which the archive came.')
archiveTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveTimeStamp.setStatus('obsolete')
if mibBuilder.loadTexts: archiveTimeStamp.setDescription('The date and time that the archive was created.')
archiveFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveFilename.setStatus('obsolete')
if mibBuilder.loadTexts: archiveFilename.setDescription('The name of the file, not including path, of the device archive.')
archiveDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveDescription.setStatus('obsolete')
if mibBuilder.loadTexts: archiveDescription.setDescription('User supplied details regarding the archive.')
emMaxConcurrentUpdates = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emMaxConcurrentUpdates.setStatus('obsolete')
if mibBuilder.loadTexts: emMaxConcurrentUpdates.setDescription('The maximum number of simultaneous updates.')
emRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emRefreshInterval.setStatus('obsolete')
if mibBuilder.loadTexts: emRefreshInterval.setDescription('The interval between device status updates.')
emVersion = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 5, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emVersion.setStatus('obsolete')
if mibBuilder.loadTexts: emVersion.setDescription('Version of the EM software.')
emAlertObjMsg = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emAlertObjMsg.setStatus('current')
if mibBuilder.loadTexts: emAlertObjMsg.setDescription('The additional information about the related alert.')
emDeviceUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 1)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceUnreachable.setStatus('current')
if mibBuilder.loadTexts: emDeviceUnreachable.setDescription('An managed device is unreachable.')
emSoftwareInstallComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 2)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emSoftwareInstallComplete.setStatus('current')
if mibBuilder.loadTexts: emSoftwareInstallComplete.setDescription('Software installation has completed.')
emSoftwareInstallFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 3)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emSoftwareInstallFailed.setStatus('current')
if mibBuilder.loadTexts: emSoftwareInstallFailed.setDescription('Software installation has failed.')
emDeviceClockSkew = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 4)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceClockSkew.setStatus('current')
if mibBuilder.loadTexts: emDeviceClockSkew.setDescription('A device clock is out of sync with EM.')
emDiskUsage = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 5)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDiskUsage.setStatus('current')
if mibBuilder.loadTexts: emDiskUsage.setDescription('A disk partition is exceeding configured usage limits.')
emMemoryUsage = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 6)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: emMemoryUsage.setDescription('The system memory is exceeding configured usage limits.')
emHotfixInstallComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 7)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emHotfixInstallComplete.setStatus('current')
if mibBuilder.loadTexts: emHotfixInstallComplete.setDescription('A hotfix has been installed on a managed device.')
emHotfixInstallFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 8)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emHotfixInstallFailed.setStatus('current')
if mibBuilder.loadTexts: emHotfixInstallFailed.setDescription('A hotfix installation has failed.')
emCpuUsage = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 9)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emCpuUsage.setStatus('current')
if mibBuilder.loadTexts: emCpuUsage.setDescription('The cpu is exceeding configured usage limits.')
emCertificateExpiration = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 10)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emCertificateExpiration.setStatus('current')
if mibBuilder.loadTexts: emCertificateExpiration.setDescription('A device certificate will expire soon.')
emScheduledArchiveFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 11)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emScheduledArchiveFailed.setStatus('current')
if mibBuilder.loadTexts: emScheduledArchiveFailed.setDescription('A scheduled configuration archive failed.')
emDeviceActiveMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 12)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceActiveMode.setStatus('current')
if mibBuilder.loadTexts: emDeviceActiveMode.setDescription('A device changed from non-ACTIVE to ACTIVE state.')
emDeviceStandbyMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 13)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceStandbyMode.setStatus('current')
if mibBuilder.loadTexts: emDeviceStandbyMode.setDescription('A device changed from non-STANDBY to STANDBY state.')
emDeviceConfigSync = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 14)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceConfigSync.setStatus('current')
if mibBuilder.loadTexts: emDeviceConfigSync.setDescription("A device's configuration is out of sync with its peer.")
emRaidDriveFailureDetected = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 15)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emRaidDriveFailureDetected.setStatus('current')
if mibBuilder.loadTexts: emRaidDriveFailureDetected.setDescription('The system RAID drive failure has been detected.')
emRaidDriveRebuildComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 16)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emRaidDriveRebuildComplete.setStatus('current')
if mibBuilder.loadTexts: emRaidDriveRebuildComplete.setDescription('The system RAID drive rebuild is complete.')
emHaSyncFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 19)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emHaSyncFailed.setStatus('current')
if mibBuilder.loadTexts: emHaSyncFailed.setDescription('EM HA Sync has failed.')
emASMSigInstallComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 20)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigInstallComplete.setStatus('current')
if mibBuilder.loadTexts: emASMSigInstallComplete.setDescription('ASM signature has been installed on a managed device.')
emASMSigInstallFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 21)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigInstallFailed.setStatus('current')
if mibBuilder.loadTexts: emASMSigInstallFailed.setDescription('ASM signature installation has failed.')
emASMSigUpdateAvailable = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 22)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigUpdateAvailable.setStatus('current')
if mibBuilder.loadTexts: emASMSigUpdateAvailable.setDescription('ASM signature update is available.')
emASMSigUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 23)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigUpdateFailed.setStatus('current')
if mibBuilder.loadTexts: emASMSigUpdateFailed.setDescription('ASM signature update failed.')
emPerformanceStorageDays = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 25)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emPerformanceStorageDays.setStatus('current')
if mibBuilder.loadTexts: emPerformanceStorageDays.setDescription('Performance storage capacity is about to fall below configured number of days.')
emPerformanceStorageCap = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 26)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emPerformanceStorageCap.setStatus('current')
if mibBuilder.loadTexts: emPerformanceStorageCap.setDescription('Performance storage capacity is lower than the amount of space reserved.')
emPerformanceThreshold = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 27)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emPerformanceThreshold.setStatus('current')
if mibBuilder.loadTexts: emPerformanceThreshold.setDescription('Threshold has been violated for a performance-data object.')
emSchedBackupFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 28)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emSchedBackupFailed.setStatus('current')
if mibBuilder.loadTexts: emSchedBackupFailed.setDescription('Scheduled performance data backup has failed.')
emStatsCollectionRateCap = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 29)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emStatsCollectionRateCap.setStatus('current')
if mibBuilder.loadTexts: emStatsCollectionRateCap.setDescription('Performance-monitoring data collection rate exceeds recommended limit')
emDeviceOfflineMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 30)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceOfflineMode.setStatus('current')
if mibBuilder.loadTexts: emDeviceOfflineMode.setDescription('A device changed from non-OFFLINE to OFFLINE state.')
emDeviceForcedOfflineMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 31)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceForcedOfflineMode.setStatus('current')
if mibBuilder.loadTexts: emDeviceForcedOfflineMode.setDescription('A device changed from non-FORCED OFFLINE to FORCED OFFLINE state.')
emServiceContractExpiry = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 32)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emServiceContractExpiry.setStatus('current')
if mibBuilder.loadTexts: emServiceContractExpiry.setDescription('Device service contract will expire soon.')
emStatsDBConnectivityLost = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 33)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emStatsDBConnectivityLost.setStatus('current')
if mibBuilder.loadTexts: emStatsDBConnectivityLost.setDescription('Statistics database connectivity is lost.')
emGatherServiceContractFailure = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 34)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emGatherServiceContractFailure.setStatus('current')
if mibBuilder.loadTexts: emGatherServiceContractFailure.setDescription('Gathering service contract end date failed.')
emDeviceImpaired = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 35)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceImpaired.setStatus('current')
if mibBuilder.loadTexts: emDeviceImpaired.setDescription('An managed device is impaired.')
emStatsDBConnectivityRestored = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 36)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emStatsDBConnectivityRestored.setStatus('current')
if mibBuilder.loadTexts: emStatsDBConnectivityRestored.setDescription('Statistics database connectivity is restored.')
emDeviceConfigSettingChanged = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 0, 1)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceConfigSettingChanged.setStatus('obsolete')
if mibBuilder.loadTexts: emDeviceConfigSettingChanged.setDescription('A configuration has been changed on a device.')
mibBuilder.exportSymbols("F5-EM-MIB", groupDescription=groupDescription, emImages=emImages, emHaSyncFailed=emHaSyncFailed, deviceAddress=deviceAddress, emDeviceActiveMode=emDeviceActiveMode, emDeviceImpaired=emDeviceImpaired, emSchedBackupFailed=emSchedBackupFailed, archiveDescription=archiveDescription, emDeviceGroups=emDeviceGroups, imageEntryTable=imageEntryTable, emMemoryUsage=emMemoryUsage, emStatsCollectionRateCap=emStatsCollectionRateCap, deviceName=deviceName, emGlobals=emGlobals, deviceNumber=deviceNumber, groupEntry=groupEntry, emArchives=emArchives, groupName=groupName, imageEntry=imageEntry, emAlerts=emAlerts, emASMSigUpdateAvailable=emASMSigUpdateAvailable, groupNumber=groupNumber, deviceAddressType=deviceAddressType, archiveTimeStamp=archiveTimeStamp, emMaxConcurrentUpdates=emMaxConcurrentUpdates, groupEntryTable=groupEntryTable, enterpriseManagement=enterpriseManagement, imageNumber=imageNumber, emServiceContractExpiry=emServiceContractExpiry, emScheduledArchiveFailed=emScheduledArchiveFailed, archiveNumber=archiveNumber, archiveVersion=archiveVersion, emAlertObjects=emAlertObjects, emDeviceStandbyMode=emDeviceStandbyMode, emStatsDBConnectivityLost=emStatsDBConnectivityLost, emDeviceList=emDeviceList, emGatherServiceContractFailure=emGatherServiceContractFailure, emPerformanceStorageCap=emPerformanceStorageCap, deviceEntryTable=deviceEntryTable, emASMSigInstallFailed=emASMSigInstallFailed, emHotfixInstallComplete=emHotfixInstallComplete, emDeviceConfigSync=emDeviceConfigSync, emAlertObjMsg=emAlertObjMsg, emASMSigUpdateFailed=emASMSigUpdateFailed, emDevices=emDevices, PYSNMP_MODULE_ID=enterpriseManagement, archiveSourceDevice=archiveSourceDevice, deviceEntry=deviceEntry, emStatsDBConnectivityRestored=emStatsDBConnectivityRestored, emDeviceUnreachable=emDeviceUnreachable, emASMSigInstallComplete=emASMSigInstallComplete, archiveEntryTable=archiveEntryTable, imageDescription=imageDescription, emVersion=emVersion, emRaidDriveRebuildComplete=emRaidDriveRebuildComplete, emDeviceForcedOfflineMode=emDeviceForcedOfflineMode, emDiskUsage=emDiskUsage, emDeviceConfigSettingChanged=emDeviceConfigSettingChanged, emAlert=emAlert, archiveProduct=archiveProduct, imageVersion=imageVersion, emDeviceOfflineMode=emDeviceOfflineMode, emCpuUsage=emCpuUsage, emPerformanceThreshold=emPerformanceThreshold, emDeviceClockSkew=emDeviceClockSkew, emRaidDriveFailureDetected=emRaidDriveFailureDetected, archiveFilename=archiveFilename, emRefreshInterval=emRefreshInterval, emCertificateExpiration=emCertificateExpiration, emHotfixInstallFailed=emHotfixInstallFailed, emSoftwareInstallFailed=emSoftwareInstallFailed, emSoftwareInstallComplete=emSoftwareInstallComplete, emPerformanceStorageDays=emPerformanceStorageDays, emAlertConfigObjects=emAlertConfigObjects, archiveEntry=archiveEntry)
