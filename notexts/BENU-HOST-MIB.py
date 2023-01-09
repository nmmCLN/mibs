#
# PySNMP MIB module BENU-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-HOST-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:39 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, Gauge32, Unsigned32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Bits, Integer32, ModuleIdentity, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Gauge32", "Unsigned32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Bits", "Integer32", "ModuleIdentity", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bHostMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5))
bHostMIB.setRevisions(('2015-11-03 00:00', '2015-04-28 00:00', '2015-04-27 00:00', '2015-01-05 00:00', '2015-01-04 00:00', '2014-12-17 00:00', '2014-09-22 00:00', '2014-03-21 00:00', '2013-05-27 00:00',))
if mibBuilder.loadTexts: bHostMIB.setLastUpdated('201511030000Z')
if mibBuilder.loadTexts: bHostMIB.setOrganization('Benu Networks')
bHostMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1))
if mibBuilder.loadTexts: bHostMIBObjects.setStatus('current')
bHostNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0))
if mibBuilder.loadTexts: bHostNotifObjects.setStatus('current')
bHostNotifVariables = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2))
if mibBuilder.loadTexts: bHostNotifVariables.setStatus('current')
bSWTaskInfoTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1), )
if mibBuilder.loadTexts: bSWTaskInfoTable.setStatus('current')
bSWTaskInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1), ).setIndexNames((0, "BENU-HOST-MIB", "bSWTaskIndex"))
if mibBuilder.loadTexts: bSWTaskInfoEntry.setStatus('current')
bSWTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bSWTaskIndex.setStatus('current')
bSWTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskName.setStatus('current')
bSWTaskProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskProcessID.setStatus('current')
bSWTaskLoadIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskLoadIntervalDuration.setStatus('current')
bSWTaskRunStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRunStateTime.setStatus('current')
bSWTaskCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCPUUsage.setStatus('current')
bSWTaskAvgCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsage.setStatus('current')
bSWTaskMaxCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskMaxCPUUsage.setStatus('current')
bSWTaskCodeSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCodeSegmentSize.setStatus('current')
bSWTaskDataSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskDataSegmentSize.setStatus('current')
bSWTaskResidentPhyMem = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskResidentPhyMem.setStatus('current')
bSWTaskVirtMemUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskVirtMemUsage.setStatus('current')
bSWTaskSharedMem = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskSharedMem.setStatus('current')
bSWTaskVirtMemPeakUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskVirtMemPeakUsage.setStatus('current')
bSWTaskAvgCPUUsageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHighThreshold.setStatus('current')
bSWTaskAvgCPUUsageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLowThreshold.setStatus('current')
bSWTaskCPUUsageLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCPUUsageLimit.setStatus('current')
bSWTaskRestartLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartLimit.setStatus('current')
bSWTaskRestartability = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartability.setStatus('current')
bSWTaskRestartCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartCount.setStatus('current')
bSysTotalMem = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysTotalMem.setStatus('current')
bSysMemUsed = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysMemUsed.setStatus('current')
bSysMemFree = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysMemFree.setStatus('current')
bSysTotalCPUUtilAvailable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysTotalCPUUtilAvailable.setStatus('current')
bSysAvgCPUUtil15Sec = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil15Sec.setStatus('current')
bSysAvgCPUUtil1Min = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil1Min.setStatus('current')
bSysAvgCPUUtil5Min = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil5Min.setStatus('current')
bCPUMonInterval = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bCPUMonInterval.setStatus('current')
bSWTaskDiedReason = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cpuUsageLimitReached", 1), ("unKnown", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWTaskDiedReason.setStatus('current')
bSWProcessName = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessName.setStatus('current')
bSWProcessID = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessID.setStatus('current')
bSWProcessAvgCPUUsageLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageLowThreshold.setStatus('current')
bSWProcessAvgCPUUsageHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageHighThreshold.setStatus('current')
bSWTaskAvgCPUUsageLow = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 1)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageLowThreshold"))
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLow.setStatus('current')
bSWTaskAvgCPUUsageHigh = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 2)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageHighThreshold"))
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHigh.setStatus('current')
bSWTaskDied = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 3)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWTaskDiedReason"))
if mibBuilder.loadTexts: bSWTaskDied.setStatus('current')
bSWTaskRestartLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 4)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"))
if mibBuilder.loadTexts: bSWTaskRestartLimitReached.setStatus('current')
mibBuilder.exportSymbols("BENU-HOST-MIB", bSWTaskDied=bSWTaskDied, bSWTaskRestartLimitReached=bSWTaskRestartLimitReached, bSWProcessAvgCPUUsageLowThreshold=bSWProcessAvgCPUUsageLowThreshold, bHostNotifVariables=bHostNotifVariables, bSysTotalMem=bSysTotalMem, bSWTaskAvgCPUUsage=bSWTaskAvgCPUUsage, bSysMemFree=bSysMemFree, bSWTaskAvgCPUUsageLowThreshold=bSWTaskAvgCPUUsageLowThreshold, bCPUMonInterval=bCPUMonInterval, bHostMIBObjects=bHostMIBObjects, bSWTaskIndex=bSWTaskIndex, bSWTaskAvgCPUUsageHigh=bSWTaskAvgCPUUsageHigh, bSWTaskRestartCount=bSWTaskRestartCount, bSWTaskCPUUsage=bSWTaskCPUUsage, bSWTaskResidentPhyMem=bSWTaskResidentPhyMem, bSWProcessAvgCPUUsageHighThreshold=bSWProcessAvgCPUUsageHighThreshold, bSWTaskVirtMemUsage=bSWTaskVirtMemUsage, bSWTaskProcessID=bSWTaskProcessID, bHostMIB=bHostMIB, bSWTaskLoadIntervalDuration=bSWTaskLoadIntervalDuration, bHostNotifObjects=bHostNotifObjects, bSysMemUsed=bSysMemUsed, bSWTaskInfoTable=bSWTaskInfoTable, bSWTaskSharedMem=bSWTaskSharedMem, bSWTaskRestartLimit=bSWTaskRestartLimit, bSWTaskCodeSegmentSize=bSWTaskCodeSegmentSize, bSWTaskCPUUsageLimit=bSWTaskCPUUsageLimit, PYSNMP_MODULE_ID=bHostMIB, bSWTaskVirtMemPeakUsage=bSWTaskVirtMemPeakUsage, bSysAvgCPUUtil5Min=bSysAvgCPUUtil5Min, bSWTaskDiedReason=bSWTaskDiedReason, bSysAvgCPUUtil1Min=bSysAvgCPUUtil1Min, bSWProcessName=bSWProcessName, bSWTaskAvgCPUUsageHighThreshold=bSWTaskAvgCPUUsageHighThreshold, bSWTaskRestartability=bSWTaskRestartability, bSWProcessID=bSWProcessID, bSysTotalCPUUtilAvailable=bSysTotalCPUUtilAvailable, bSWTaskName=bSWTaskName, bSWTaskRunStateTime=bSWTaskRunStateTime, bSWTaskInfoEntry=bSWTaskInfoEntry, bSWTaskMaxCPUUsage=bSWTaskMaxCPUUsage, bSysAvgCPUUtil15Sec=bSysAvgCPUUtil15Sec, bSWTaskAvgCPUUsageLow=bSWTaskAvgCPUUsageLow, bSWTaskDataSegmentSize=bSWTaskDataSegmentSize)
