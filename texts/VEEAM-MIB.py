#
# PySNMP MIB module VEEAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veeam/VEEAM-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:35:01 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, NotificationType, Bits, MibIdentifier, ObjectIdentity, IpAddress, Counter64, Counter32, enterprises, TimeTicks, ModuleIdentity, Unsigned32, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "NotificationType", "Bits", "MibIdentifier", "ObjectIdentity", "IpAddress", "Counter64", "Counter32", "enterprises", "TimeTicks", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
veeam = MibIdentifier((1, 3, 6, 1, 4, 1, 31023))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 31023, 1))
backup = MibIdentifier((1, 3, 6, 1, 4, 1, 31023, 1, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1))
onBackupJobCompleted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,1)).setObjects(("VEEAM-MIB", "backupJobId"), ("VEEAM-MIB", "backupJobName"), ("VEEAM-MIB", "backupJobResult"), ("VEEAM-MIB", "backupJobComment"))
if mibBuilder.loadTexts: onBackupJobCompleted.setDescription('This trap is sent on backup/replica job completed.')
onVmBackupCompleted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,2)).setObjects(("VEEAM-MIB", "backupJobName"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "sourceHostName"), ("VEEAM-MIB", "vmBackupResult"), ("VEEAM-MIB", "vmBackupComment"))
if mibBuilder.loadTexts: onVmBackupCompleted.setDescription('This trap is sent on vm backup/replica completed.')
onLinuxFLRMountStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,3)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
if mibBuilder.loadTexts: onLinuxFLRMountStarted.setDescription('This trap is sent when Multi-OS FLR helper appliance starts.')
onLinuxFLRCopyToStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,4)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "targetHost"), ("VEEAM-MIB", "targetDir"))
if mibBuilder.loadTexts: onLinuxFLRCopyToStarted.setDescription('This trap is sent when Multi-OS FLR file recovery via Copy To operation is initiated.')
onLinuxFLRToOriginalStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,5)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
if mibBuilder.loadTexts: onLinuxFLRToOriginalStarted.setDescription('This trap is sent when Multi-OS FLR file recovery via Restore operation is initiated.')
onLinuxFLRCopyToFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,6)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferTime"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "targetHost"), ("VEEAM-MIB", "targetDir"), ("VEEAM-MIB", "csvReportFilePath"))
if mibBuilder.loadTexts: onLinuxFLRCopyToFinished.setDescription('This trap is sent when Multi-OS FLR file recovery via Copy To operation is completed.')
onLinuxFLRToOriginalFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,7)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferTime"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "csvReportFilePath"))
if mibBuilder.loadTexts: onLinuxFLRToOriginalFinished.setDescription('This trap is sent when Multi-OS FLR file recovery via Restore operation is completed.')
onWinFLRMountStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,8)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "mountServerName"))
if mibBuilder.loadTexts: onWinFLRMountStarted.setDescription('This trap is sent when Windows FLR starts to mounts a backup.')
onWinFLRToOriginalStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,9)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
if mibBuilder.loadTexts: onWinFLRToOriginalStarted.setDescription('This trap is sent when Windows FLR file recovery via Restore operation is completed.')
onWinFLRCopyToStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,10)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "targetDir"))
if mibBuilder.loadTexts: onWinFLRCopyToStarted.setDescription('This trap is sent when Windows FLR file recovery via Copy To operation is initiated.')
onWinFLRToOriginalFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,11)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "csvReportFilePath"))
if mibBuilder.loadTexts: onWinFLRToOriginalFinished.setDescription('This trap is sent when Windows FLR file recovery via Restore operation is completed.')
onWinFLRCopyToFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,12)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "targetDir"), ("VEEAM-MIB", "csvReportFilePath"))
if mibBuilder.loadTexts: onWinFLRCopyToFinished.setDescription('This trap is sent when Windows FLR file recovery via Copy To operation is completed.')
onWebDownloadStart = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,13)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
if mibBuilder.loadTexts: onWebDownloadStart.setDescription('This trap is sent when 1-Click FLR file download operation is initiated in the Enterprise Manager.')
onWebDownloadFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,14)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"))
if mibBuilder.loadTexts: onWebDownloadFinished.setDescription('This trap is sent when 1-Click FLR file download operation is completed in the Enterprise Manager.')
onSobrOffloadFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,15)).setObjects(("VEEAM-MIB", "repositoryId"), ("VEEAM-MIB", "repositoryName"), ("VEEAM-MIB", "repositoryStatus"), ("VEEAM-MIB", "extentStatusList"))
if mibBuilder.loadTexts: onSobrOffloadFinished.setDescription('This trap is sent when scale-out repository offload job is finished')
onCdpRpoReport = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,16)).setObjects(("VEEAM-MIB", "cdpPolicyName"), ("VEEAM-MIB", "cdpRpoStatus"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "cdpSla"), ("VEEAM-MIB", "cdpRpoThreshold"), ("VEEAM-MIB", "cdpMaxDelay"))
if mibBuilder.loadTexts: onCdpRpoReport.setDescription('This trap is sent when CDP policy RPO status is changed')
backupJobId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 101), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobId.setStatus('mandatory')
if mibBuilder.loadTexts: backupJobId.setDescription('Backup job id')
backupJobName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 102), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobName.setStatus('mandatory')
if mibBuilder.loadTexts: backupJobName.setDescription('Backup job name')
backupJobResult = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 103), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobResult.setStatus('mandatory')
if mibBuilder.loadTexts: backupJobResult.setDescription('Backup job result')
backupJobComment = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 104), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobComment.setStatus('mandatory')
if mibBuilder.loadTexts: backupJobComment.setDescription('Backup job comment')
vmName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 105), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmName.setStatus('mandatory')
if mibBuilder.loadTexts: vmName.setDescription('VM name.')
sourceHostName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 106), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceHostName.setStatus('mandatory')
if mibBuilder.loadTexts: sourceHostName.setDescription('Source host name')
vmBackupResult = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 107), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmBackupResult.setStatus('mandatory')
if mibBuilder.loadTexts: vmBackupResult.setDescription('VM backup result')
vmBackupComment = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 108), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmBackupComment.setStatus('mandatory')
if mibBuilder.loadTexts: vmBackupComment.setDescription('VM backup comment')
sessionId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 109), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionId.setStatus('mandatory')
if mibBuilder.loadTexts: sessionId.setDescription('Restore session ID')
initiatorName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 110), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: initiatorName.setStatus('mandatory')
if mibBuilder.loadTexts: initiatorName.setDescription('Initiated by')
initiatorSid = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 111), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: initiatorSid.setStatus('mandatory')
if mibBuilder.loadTexts: initiatorSid.setDescription('Initiated by (SID)')
vmRestorePointId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 112), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmRestorePointId.setStatus('mandatory')
if mibBuilder.loadTexts: vmRestorePointId.setDescription('Restore point ID')
vmRestorePointCreationTime = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 113), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmRestorePointCreationTime.setStatus('mandatory')
if mibBuilder.loadTexts: vmRestorePointCreationTime.setDescription('Restore point creation time')
targetHost = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 114), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: targetHost.setStatus('mandatory')
if mibBuilder.loadTexts: targetHost.setDescription('Target host')
targetDir = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 115), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: targetDir.setStatus('mandatory')
if mibBuilder.loadTexts: targetDir.setDescription('Target directory')
transferStatus = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 116), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferStatus.setStatus('mandatory')
if mibBuilder.loadTexts: transferStatus.setDescription('Restore result')
transferTime = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 117), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferTime.setStatus('mandatory')
if mibBuilder.loadTexts: transferTime.setDescription('Restore time')
transferFileList = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 118), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferFileList.setStatus('mandatory')
if mibBuilder.loadTexts: transferFileList.setDescription('Restored files')
notTransferFileList = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 119), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: notTransferFileList.setStatus('mandatory')
if mibBuilder.loadTexts: notTransferFileList.setDescription('Failed to restore')
mountServerName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 120), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountServerName.setStatus('mandatory')
if mibBuilder.loadTexts: mountServerName.setDescription('Mount server name')
repositoryId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 121), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: repositoryId.setStatus('mandatory')
if mibBuilder.loadTexts: repositoryId.setDescription('Scale-out repository ID')
repositoryName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 122), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: repositoryName.setStatus('mandatory')
if mibBuilder.loadTexts: repositoryName.setDescription('Scale-out repository name')
repositoryStatus = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 123), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: repositoryStatus.setStatus('mandatory')
if mibBuilder.loadTexts: repositoryStatus.setDescription('Scale-out repository status')
extentStatusList = MibTable((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: extentStatusList.setStatus('mandatory')
if mibBuilder.loadTexts: extentStatusList.setDescription('Scale-out repository extent status list')
extentStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124, 1), ).setMaxAccess("readonly").setIndexNames((0, "VEEAM-MIB", "extentName"))
if mibBuilder.loadTexts: extentStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: extentStatusEntry.setDescription('Scale-out repository extent status entry')
extentName = MibTableColumn((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extentName.setStatus('mandatory')
if mibBuilder.loadTexts: extentName.setDescription('Scale-out repository extent name')
extentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extentStatus.setStatus('mandatory')
if mibBuilder.loadTexts: extentStatus.setDescription('Scale-out repository extent status')
csvReportFilePath = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 125), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csvReportFilePath.setStatus('mandatory')
if mibBuilder.loadTexts: csvReportFilePath.setDescription('Path to CSV report file')
cdpPolicyName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 126), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpPolicyName.setStatus('mandatory')
if mibBuilder.loadTexts: cdpPolicyName.setDescription('CDP policy name')
cdpRpoStatus = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 127), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpRpoStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdpRpoStatus.setDescription('CDP RPO status')
cdpSla = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 128), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpSla.setStatus('mandatory')
if mibBuilder.loadTexts: cdpSla.setDescription('CDP SLA')
cdpRpoThreshold = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 129), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpRpoThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: cdpRpoThreshold.setDescription('CDP RPO reporting threshold')
cdpMaxDelay = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 130), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpMaxDelay.setStatus('mandatory')
if mibBuilder.loadTexts: cdpMaxDelay.setDescription('CDP RPO max delay')
mibBuilder.exportSymbols("VEEAM-MIB", initiatorSid=initiatorSid, initiatorName=initiatorName, onLinuxFLRCopyToStarted=onLinuxFLRCopyToStarted, transferFileList=transferFileList, traps=traps, onVmBackupCompleted=onVmBackupCompleted, onLinuxFLRCopyToFinished=onLinuxFLRCopyToFinished, onWebDownloadFinished=onWebDownloadFinished, vmBackupResult=vmBackupResult, onWinFLRMountStarted=onWinFLRMountStarted, products=products, repositoryStatus=repositoryStatus, extentName=extentName, transferStatus=transferStatus, cdpMaxDelay=cdpMaxDelay, backupJobName=backupJobName, repositoryName=repositoryName, onWebDownloadStart=onWebDownloadStart, targetDir=targetDir, extentStatusEntry=extentStatusEntry, extentStatus=extentStatus, cdpPolicyName=cdpPolicyName, onWinFLRCopyToFinished=onWinFLRCopyToFinished, backupJobResult=backupJobResult, cdpRpoStatus=cdpRpoStatus, onSobrOffloadFinished=onSobrOffloadFinished, onWinFLRCopyToStarted=onWinFLRCopyToStarted, onCdpRpoReport=onCdpRpoReport, repositoryId=repositoryId, onLinuxFLRToOriginalStarted=onLinuxFLRToOriginalStarted, backupJobComment=backupJobComment, sourceHostName=sourceHostName, vmBackupComment=vmBackupComment, sessionId=sessionId, extentStatusList=extentStatusList, onBackupJobCompleted=onBackupJobCompleted, onLinuxFLRMountStarted=onLinuxFLRMountStarted, notTransferFileList=notTransferFileList, onWinFLRToOriginalStarted=onWinFLRToOriginalStarted, csvReportFilePath=csvReportFilePath, onLinuxFLRToOriginalFinished=onLinuxFLRToOriginalFinished, onWinFLRToOriginalFinished=onWinFLRToOriginalFinished, vmRestorePointId=vmRestorePointId, cdpSla=cdpSla, transferTime=transferTime, targetHost=targetHost, cdpRpoThreshold=cdpRpoThreshold, vmRestorePointCreationTime=vmRestorePointCreationTime, backupJobId=backupJobId, backup=backup, vmName=vmName, veeam=veeam, mountServerName=mountServerName)
