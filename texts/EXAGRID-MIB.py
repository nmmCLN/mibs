#
# PySNMP MIB module EXAGRID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exagrid/EXAGRID-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:51 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
InternationalDisplayString, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "InternationalDisplayString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, enterprises, ModuleIdentity, Unsigned32, ObjectIdentity, iso, IpAddress, Gauge32, Counter32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "enterprises", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "Counter32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
exagrid = MibIdentifier((1, 3, 6, 1, 4, 1, 14941))
exagridTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 1))
egEventParams = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 2))
exagridProductLines = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3))
exagridExX000Series = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1))
exagridExX000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 0))
exagridEx1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 1))
exagridEx2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 2))
exagridEx3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 3))
exagridEx4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 4))
exagridEx5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 5))
exagridExGW = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 6))
exagridEx10000E = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 10))
exagridEx1T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 11))
exagridEx2T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 12))
exagridEx3T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 13))
exagridEx4T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 14))
exagridEx5T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 15))
exagridEx7T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 16))
exagridEx9T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 19))
exagridEx7S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 26))
exagridEx9S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 29))
exagridEx1T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 31))
exagridEx2T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 32))
exagridEx3T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 33))
exagridEx4T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 34))
exagridEx5T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 35))
exagridEx7T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 36))
exagridEx7S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 46))
exagridEx10T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 110))
exagridEx13T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 113))
exagridEx10S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 210))
exagridEx13S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 213))
exagridEx10T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 310))
exagridEx13T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 313))
exagridEx21T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 321))
exagridEx10S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 410))
exagridEx13S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 413))
exagridEx21S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 421))
exagridServerData = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4))
exagridLandingSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 1))
exagridRetentionSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 2))
exagridDeduplicationRatio = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 3))
exagridPendingDeduplication = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 4))
exagridPendingReplication = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 5))
exagridServerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 6))
egLandingSpaceConfiguredWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceConfiguredWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egLandingSpaceConfiguredWholeGigabytes.setDescription('The amount of configured landing space scaled to GigaBytes (10^9) bytes')
egLandingSpaceConfiguredFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceConfiguredFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egLandingSpaceConfiguredFractionalGigabytes.setDescription('The amount of configured landing space below 1 Gigabyte in bytes')
egLandingSpaceAvailableWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceAvailableWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egLandingSpaceAvailableWholeGigabytes.setDescription('The amount of available landing space scaled to GigaBytes (10^9) bytes')
egLandingSpaceAvailableFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceAvailableFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egLandingSpaceAvailableFractionalGigabytes.setDescription('The amount of available landing space below 1 Gigabyte in bytes')
egRetentionSpaceConfiguredWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceConfiguredWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egRetentionSpaceConfiguredWholeGigabytes.setDescription('The amount of configured retention space scaled to GigaBytes (10^9) bytes')
egRetentionSpaceConfiguredFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceConfiguredFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egRetentionSpaceConfiguredFractionalGigabytes.setDescription('The amount of configured retention space below 1 Gigabyte in bytes')
egRetentionSpaceAvailableWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceAvailableWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egRetentionSpaceAvailableWholeGigabytes.setDescription('The amount of available retention space scaled to GigaBytes (10^9) bytes')
egRetentionSpaceAvailableFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceAvailableFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egRetentionSpaceAvailableFractionalGigabytes.setDescription('The amount of available retention space below 1 Gigabyte in bytes')
egBackupDataAvailableWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataAvailableWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egBackupDataAvailableWholeGigabytes.setDescription('The amount of data available for restore by a backup application scaled to GigaBytes (10^9) bytes')
egBackupDataAvailableFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataAvailableFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egBackupDataAvailableFractionalGigabytes.setDescription('The amount of data available for restore by a backup application below 1 Gigabyte in bytes')
egBackupDataSpaceConsumedWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataSpaceConsumedWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egBackupDataSpaceConsumedWholeGigabytes.setDescription('The amount of consumed retention space scaled to GigaBytes (10^9) bytes')
egBackupDataSpaceConsumedFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataSpaceConsumedFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egBackupDataSpaceConsumedFractionalGigabytes.setDescription('The amount of consumed retention space below 1 Gigabyte in bytes')
egPendingDeduplicationWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingDeduplicationWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egPendingDeduplicationWholeGigabytes.setDescription('The amount of data not yet deduplicated scaled to GigaBytes (10^9) bytes')
egPendingDeduplicationFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 4, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingDeduplicationFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egPendingDeduplicationFractionalGigabytes.setDescription('The amount of data not yet deduplicated below 1 Gigabyte in bytes')
egPendingDeduplicationAge = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 4, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingDeduplicationAge.setStatus('mandatory')
if mibBuilder.loadTexts: egPendingDeduplicationAge.setDescription('The amount of time that data has been available for deduplication, but has not yet been deduplicated')
egPendingReplicationWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingReplicationWholeGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egPendingReplicationWholeGigabytes.setDescription('The amount of data that has not yet completed replication scaled to GigaBytes (10^9) bytes')
egPendingReplicationFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 5, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingReplicationFractionalGigabytes.setStatus('mandatory')
if mibBuilder.loadTexts: egPendingReplicationFractionalGigabytes.setDescription('The amount of data that has not yet completed replication below 1 Gigabyte in bytes')
egPendingReplicationAge = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 5, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingReplicationAge.setStatus('mandatory')
if mibBuilder.loadTexts: egPendingReplicationAge.setDescription('The amount of time that data has been available for replication, but has not yet been replicated')
egServerAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egServerAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: egServerAlarmState.setDescription('Current alarm state of the server.\n                1 Server has no alarms\n                2 Server is in a Warning Alarm State\n                3 Server is in an Error Alarm State')
egEventParamsName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsName.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsName.setDescription('The Event Name')
egEventParamsId = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsId.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsId.setDescription('The Event Id')
egEventParamsCreateTime = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsCreateTime.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsCreateTime.setDescription('The Event Creation Time')
egEventParamsCreateTimeRaw = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsCreateTimeRaw.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsCreateTimeRaw.setDescription('The Event Creation Time (milliseconds)')
egEventParamsGridName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsGridName.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsGridName.setDescription('The Name of the Grid for the device originating the event')
egEventParamsSiteName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsSiteName.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsSiteName.setDescription('The Name of the Site for the device originating the event')
egEventParamsSiteId = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsSiteId.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsSiteId.setDescription('The Id of the Site for the device originating the event')
egEventParamsSeverity = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsSeverity.setDescription('The Event Severity')
egEventParamsDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceName.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsDeviceName.setDescription('The Name of the device originating the event')
egEventParamsDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceId.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsDeviceId.setDescription('The Id of the device originating the event')
egEventParamsDeviceSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsDeviceSerialNumber.setDescription('The Name of the device originating the event')
egEventParamsDeviceIp = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceIp.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsDeviceIp.setDescription('The IP address of the device originating the event')
egEventParamsDupCount = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDupCount.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsDupCount.setDescription('The count of recently generated duplicates of this event')
egEventParamsText = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsText.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsText.setDescription('The short description for the event')
egEventParamsDetail = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 15), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDetail.setStatus('mandatory')
if mibBuilder.loadTexts: egEventParamsDetail.setDescription('The long description for the event')
egTrap = NotificationType((1, 3, 6, 1, 4, 1, 14941, 1) + (0,1)).setObjects(("EXAGRID-MIB", "egEventParamsName"), ("EXAGRID-MIB", "egEventParamsId"), ("EXAGRID-MIB", "egEventParamsCreateTime"), ("EXAGRID-MIB", "egEventParamsCreateTimeRaw"), ("EXAGRID-MIB", "egEventParamsGridName"), ("EXAGRID-MIB", "egEventParamsSiteName"), ("EXAGRID-MIB", "egEventParamsSiteId"), ("EXAGRID-MIB", "egEventParamsSeverity"), ("EXAGRID-MIB", "egEventParamsDeviceName"), ("EXAGRID-MIB", "egEventParamsDeviceId"), ("EXAGRID-MIB", "egEventParamsDeviceIp"), ("EXAGRID-MIB", "egEventParamsDeviceSerialNumber"), ("EXAGRID-MIB", "egEventParamsDupCount"), ("EXAGRID-MIB", "egEventParamsText"), ("EXAGRID-MIB", "egEventParamsDetail"))
if mibBuilder.loadTexts: egTrap.setDescription('An event of note has been posted')
mibBuilder.exportSymbols("EXAGRID-MIB", exagridEx21T2012A=exagridEx21T2012A, egPendingDeduplicationAge=egPendingDeduplicationAge, exagridEx10T=exagridEx10T, egBackupDataAvailableFractionalGigabytes=egBackupDataAvailableFractionalGigabytes, egBackupDataAvailableWholeGigabytes=egBackupDataAvailableWholeGigabytes, egEventParamsDeviceIp=egEventParamsDeviceIp, exagridEx13T=exagridEx13T, exagridEx1T=exagridEx1T, egPendingReplicationFractionalGigabytes=egPendingReplicationFractionalGigabytes, exagridEx9S=exagridEx9S, egBackupDataSpaceConsumedWholeGigabytes=egBackupDataSpaceConsumedWholeGigabytes, exagridServerData=exagridServerData, exagridEx4T=exagridEx4T, exagridEx1000=exagridEx1000, exagridExX000=exagridExX000, exagridEx2T=exagridEx2T, egLandingSpaceConfiguredWholeGigabytes=egLandingSpaceConfiguredWholeGigabytes, exagridEx10T2012A=exagridEx10T2012A, exagridEx2000=exagridEx2000, exagridEx10000E=exagridEx10000E, egServerAlarmState=egServerAlarmState, exagridEx13S2012A=exagridEx13S2012A, exagridEx1T2012A=exagridEx1T2012A, egEventParamsDupCount=egEventParamsDupCount, exagridTraps=exagridTraps, exagridEx10S2012A=exagridEx10S2012A, egEventParamsDetail=egEventParamsDetail, exagridEx7T=exagridEx7T, exagridPendingDeduplication=exagridPendingDeduplication, exagridEx2T2012A=exagridEx2T2012A, exagridExGW=exagridExGW, egPendingDeduplicationFractionalGigabytes=egPendingDeduplicationFractionalGigabytes, egEventParamsSiteId=egEventParamsSiteId, exagridEx7S2012A=exagridEx7S2012A, exagridEx3T=exagridEx3T, exagridEx10S=exagridEx10S, egEventParamsGridName=egEventParamsGridName, exagridProductLines=exagridProductLines, exagridPendingReplication=exagridPendingReplication, exagridDeduplicationRatio=exagridDeduplicationRatio, exagridEx3000=exagridEx3000, egLandingSpaceConfiguredFractionalGigabytes=egLandingSpaceConfiguredFractionalGigabytes, egEventParamsCreateTime=egEventParamsCreateTime, exagridExX000Series=exagridExX000Series, exagridEx4T2012A=exagridEx4T2012A, egBackupDataSpaceConsumedFractionalGigabytes=egBackupDataSpaceConsumedFractionalGigabytes, exagridEx5T2012A=exagridEx5T2012A, exagridEx13T2012A=exagridEx13T2012A, egTrap=egTrap, exagridEx9T=exagridEx9T, egRetentionSpaceAvailableFractionalGigabytes=egRetentionSpaceAvailableFractionalGigabytes, exagridEx4000=exagridEx4000, egEventParamsId=egEventParamsId, exagridEx3T2012A=exagridEx3T2012A, exagridServerStatus=exagridServerStatus, egEventParamsSeverity=egEventParamsSeverity, egEventParamsDeviceSerialNumber=egEventParamsDeviceSerialNumber, egEventParamsCreateTimeRaw=egEventParamsCreateTimeRaw, egEventParamsText=egEventParamsText, egEventParamsSiteName=egEventParamsSiteName, exagridEx7S=exagridEx7S, egPendingDeduplicationWholeGigabytes=egPendingDeduplicationWholeGigabytes, egEventParamsDeviceName=egEventParamsDeviceName, egPendingReplicationWholeGigabytes=egPendingReplicationWholeGigabytes, egEventParams=egEventParams, exagridEx5T=exagridEx5T, exagridRetentionSpace=exagridRetentionSpace, exagridEx7T2012A=exagridEx7T2012A, egRetentionSpaceConfiguredWholeGigabytes=egRetentionSpaceConfiguredWholeGigabytes, exagridLandingSpace=exagridLandingSpace, egLandingSpaceAvailableFractionalGigabytes=egLandingSpaceAvailableFractionalGigabytes, egEventParamsDeviceId=egEventParamsDeviceId, exagridEx21S2012A=exagridEx21S2012A, egPendingReplicationAge=egPendingReplicationAge, egRetentionSpaceAvailableWholeGigabytes=egRetentionSpaceAvailableWholeGigabytes, egRetentionSpaceConfiguredFractionalGigabytes=egRetentionSpaceConfiguredFractionalGigabytes, egEventParamsName=egEventParamsName, exagridEx5000=exagridEx5000, egLandingSpaceAvailableWholeGigabytes=egLandingSpaceAvailableWholeGigabytes, exagrid=exagrid, exagridEx13S=exagridEx13S)
