#
# PySNMP MIB module EQLDISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLDISK-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:42 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Integer32, TimeTicks, iso, IpAddress, ModuleIdentity, Unsigned32, MibIdentifier, ObjectIdentity, Counter32, Gauge32, Counter64, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Integer32", "TimeTicks", "iso", "IpAddress", "ModuleIdentity", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter32", "Gauge32", "Counter64", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eqldiskModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 3))
eqldiskModule.setRevisions(('2002-09-06 00:00',))
if mibBuilder.loadTexts: eqldiskModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqldiskModule.setOrganization('EqualLogic Inc.')
eqldiskObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 3, 1))
eqldiskNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 3, 2))
eqldiskConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 3, 3))
eqlDiskTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1), )
if mibBuilder.loadTexts: eqlDiskTable.setStatus('current')
eqlDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLDISK-MIB", "eqlDiskIndex"))
if mibBuilder.loadTexts: eqlDiskEntry.setStatus('current')
eqlDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: eqlDiskIndex.setStatus('current')
eqlDiskType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('unknown disk type')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskType.setStatus('current')
eqlDiskModelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40)).clone('unknown disk model')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskModelNumber.setStatus('current')
eqlDiskRevisionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8)).clone('?firmrev')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskRevisionNumber.setStatus('current')
eqlDiskSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20)).clone('unknown serial#')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSerialNumber.setStatus('current')
eqlDiskSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSize.setStatus('current')
eqlDiskAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("set-disk-on-line", 1), ("set-disk-off-line", 2), ("set-disk-spare", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlDiskAdminStatus.setStatus('current')
eqlDiskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("on-line", 1), ("spare", 2), ("failed", 3), ("off-line", 4), ("alt-sig", 5), ("too-small", 6), ("history-of-failures", 7), ("unsupported-version", 8), ("unhealthy", 9), ("replacement", 10), ("encrypted", 11), ("notApproved", 12), ("preempt-failed", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatus.setStatus('current')
eqlDiskErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrors.setStatus('current')
eqlDiskId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskId.setStatus('current')
eqlDiskSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 13))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSlot.setStatus('current')
eqlDiskTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("sata", 1), ("sas", 2), ("sata-ssd", 3), ("sas-ssd", 4), ("sas-sed-hdd", 5), ("sas-sed-ssd", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskTypeEnum.setStatus('current')
eqlDiskRPM = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskRPM.setStatus('current')
eqlDiskSectorSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("sector-size-512-bytes", 0), ("sector-size-4096-bytes", 1), ("sector-size-unknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSectorSize.setStatus('current')
eqlDiskManufacturingInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20)).clone('mfginfo?')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskManufacturingInfo.setStatus('current')
eqlDiskPI = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("pi-disabled", 0), ("pi-enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskPI.setStatus('current')
eqlDiskHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("smart-status-not-available", 0), ("smart-ok", 1), ("smart-tripped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskHealth.setStatus('current')
eqlDiskStatusTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2), )
if mibBuilder.loadTexts: eqlDiskStatusTable.setStatus('current')
eqlDiskStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1), )
eqlDiskEntry.registerAugmentions(("EQLDISK-MIB", "eqlDiskStatusEntry"))
eqlDiskStatusEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
if mibBuilder.loadTexts: eqlDiskStatusEntry.setStatus('current')
eqlDiskStatusXfers = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusXfers.setStatus('current')
eqlDiskStatusBytesRead = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusBytesRead.setStatus('current')
eqlDiskStatusBytesWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusBytesWritten.setStatus('current')
eqlDiskStatusBusyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusBusyTime.setStatus('current')
eqlDiskStatusNumIOs = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusNumIOs.setStatus('current')
eqlDiskStatusFailXfers = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusFailXfers.setStatus('current')
eqlDiskStatusNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusNumResets.setStatus('current')
eqlDiskStatusTotalQD = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusTotalQD.setStatus('current')
eqlDiskStatusLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskStatusLifetime.setStatus('current')
eqlDiskErrorTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3), )
if mibBuilder.loadTexts: eqlDiskErrorTable.setStatus('current')
eqlDiskErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1), )
eqlDiskEntry.registerAugmentions(("EQLDISK-MIB", "eqlDiskErrorEntry"))
eqlDiskErrorEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
if mibBuilder.loadTexts: eqlDiskErrorEntry.setStatus('current')
eqlDiskErrorPhyReady = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorPhyReady.setStatus('current')
eqlDiskErrorPhyInternal = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorPhyInternal.setStatus('current')
eqlDiskErrorCommWake = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorCommWake.setStatus('current')
eqlDiskErrorDecode10b8b = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorDecode10b8b.setStatus('current')
eqlDiskErrorDisparity = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorDisparity.setStatus('current')
eqlDiskErrorCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorCRC.setStatus('current')
eqlDiskErrorHandShake = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorHandShake.setStatus('current')
eqlDiskErrorLinkSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorLinkSeq.setStatus('current')
eqlDiskErrorTransportState = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorTransportState.setStatus('current')
eqlDiskErrorUnrecFIS = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskErrorUnrecFIS.setStatus('current')
eqlDiskSmartInfoTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4), )
if mibBuilder.loadTexts: eqlDiskSmartInfoTable.setStatus('current')
eqlDiskSmartInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1), )
eqlDiskEntry.registerAugmentions(("EQLDISK-MIB", "eqlDiskSmartInfoEntry"))
eqlDiskSmartInfoEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
if mibBuilder.loadTexts: eqlDiskSmartInfoEntry.setStatus('current')
eqlDiskSmartInfoRawReadErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoRawReadErrorRate.setStatus('current')
eqlDiskSmartInfoRawReadErrorRateWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoRawReadErrorRateWorst.setStatus('current')
eqlDiskSmartInfoThroughputPerformance = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoThroughputPerformance.setStatus('current')
eqlDiskSmartInfoThroughputPerformanceWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoThroughputPerformanceWorst.setStatus('current')
eqlDiskSmartInfoSpinUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinUpTime.setStatus('current')
eqlDiskSmartInfoSpinUpTimeWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinUpTimeWorst.setStatus('current')
eqlDiskSmartInfoStartStopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoStartStopCount.setStatus('current')
eqlDiskSmartInfoStartStopCountWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoStartStopCountWorst.setStatus('current')
eqlDiskSmartInfoReallocatedSectorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoReallocatedSectorCount.setStatus('current')
eqlDiskSmartInfoReallocatedSectorCountWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoReallocatedSectorCountWorst.setStatus('current')
eqlDiskSmartInfoReadChannelMargin = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoReadChannelMargin.setStatus('current')
eqlDiskSmartInfoReadChannelMarginWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoReadChannelMarginWorst.setStatus('current')
eqlDiskSmartInfoSeekErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSeekErrorRate.setStatus('current')
eqlDiskSmartInfoSeekErrorRateWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSeekErrorRateWorst.setStatus('current')
eqlDiskSmartInfoSeekPerformance = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSeekPerformance.setStatus('current')
eqlDiskSmartInfoSeekPerformanceWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSeekPerformanceWorst.setStatus('current')
eqlDiskSmartInfoPowerOnHours = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoPowerOnHours.setStatus('current')
eqlDiskSmartInfoPowerOnHoursWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoPowerOnHoursWorst.setStatus('current')
eqlDiskSmartInfoSpinupRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinupRetries.setStatus('current')
eqlDiskSmartInfoSpinupRetriesWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinupRetriesWorst.setStatus('current')
eqlDiskSmartInfoDriveRecalibRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoDriveRecalibRetryCount.setStatus('current')
eqlDiskSmartInfoDriveRecalibRetryCountWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoDriveRecalibRetryCountWorst.setStatus('current')
eqlDiskSmartInfoPowerCycleCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoPowerCycleCount.setStatus('current')
eqlDiskSmartInfoPowerCycleCountWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoPowerCycleCountWorst.setStatus('current')
eqlDiskSmartInfoReadSoftErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoReadSoftErrorRate.setStatus('current')
eqlDiskSmartInfoReadSoftErrorRateWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoReadSoftErrorRateWorst.setStatus('current')
eqlDiskSmartInfoEmergencyRetractCycles = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoEmergencyRetractCycles.setStatus('current')
eqlDiskSmartInfoEmergencyRetractCyclesWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoEmergencyRetractCyclesWorst.setStatus('current')
eqlDiskSmartInfoLoadUnloadCycles = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoLoadUnloadCycles.setStatus('current')
eqlDiskSmartInfoLoadUnloadCyclesWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoLoadUnloadCyclesWorst.setStatus('current')
eqlDiskSmartInfoHDDTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoHDDTemp.setStatus('current')
eqlDiskSmartInfoHDDTempWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoHDDTempWorst.setStatus('current')
eqlDiskSmartInfoOnTheFlyErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOnTheFlyErrorRate.setStatus('current')
eqlDiskSmartInfoOnTheFlyErrorRateWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOnTheFlyErrorRateWorst.setStatus('current')
eqlDiskSmartInfoSelfTestReallocSectors = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSelfTestReallocSectors.setStatus('current')
eqlDiskSmartInfoSelfTestReallocSectorsWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSelfTestReallocSectorsWorst.setStatus('current')
eqlDiskSmartInfoPendingDefects = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoPendingDefects.setStatus('current')
eqlDiskSmartInfoPendingDefectsWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoPendingDefectsWorst.setStatus('current')
eqlDiskSmartInfoOfflineSurfaceScan = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOfflineSurfaceScan.setStatus('current')
eqlDiskSmartInfoOfflineSurfaceScanWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOfflineSurfaceScanWorst.setStatus('current')
eqlDiskSmartInfoUltraDMACRCErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoUltraDMACRCErrorRate.setStatus('current')
eqlDiskSmartInfoUltraDMACRCErrorRateWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 42), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoUltraDMACRCErrorRateWorst.setStatus('current')
eqlDiskSmartInfoWritePreampErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoWritePreampErrors.setStatus('current')
eqlDiskSmartInfoWritePreampErrorsWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoWritePreampErrorsWorst.setStatus('current')
eqlDiskSmartInfoOffTrackErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOffTrackErrors.setStatus('current')
eqlDiskSmartInfoOffTrackErrorsWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOffTrackErrorsWorst.setStatus('current')
eqlDiskSmartInfoDAMErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoDAMErrorRate.setStatus('current')
eqlDiskSmartInfoDAMErrorRateWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoDAMErrorRateWorst.setStatus('current')
eqlDiskSmartInfoECCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 49), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoECCErrors.setStatus('current')
eqlDiskSmartInfoECCErrorsWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoECCErrorsWorst.setStatus('current')
eqlDiskSmartInfoSoftECCCorrection = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 51), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSoftECCCorrection.setStatus('current')
eqlDiskSmartInfoSoftECCCorrectionWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSoftECCCorrectionWorst.setStatus('current')
eqlDiskSmartInfoThermalAsperityRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoThermalAsperityRate.setStatus('current')
eqlDiskSmartInfoThermalAsperityRateWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoThermalAsperityRateWorst.setStatus('current')
eqlDiskSmartInfoSpinHighCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinHighCount.setStatus('current')
eqlDiskSmartInfoSpinHighCountWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinHighCountWorst.setStatus('current')
eqlDiskSmartInfoSpinBuzz = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinBuzz.setStatus('current')
eqlDiskSmartInfoSpinBuzzWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoSpinBuzzWorst.setStatus('current')
eqlDiskSmartInfoOfflineSeekPerformance = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 59), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOfflineSeekPerformance.setStatus('current')
eqlDiskSmartInfoOfflineSeekPerformanceWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 60), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoOfflineSeekPerformanceWorst.setStatus('current')
eqlDiskSmartInfoThresholdExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 3, 1, 4, 1, 61), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDiskSmartInfoThresholdExceeded.setStatus('current')
eqldiskMgmtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 3, 2, 1))
eqlDiskStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 12740, 3, 2, 1, 1)).setObjects(("EQLDISK-MIB", "eqlDiskStatus"), ("EQLDISK-MIB", "eqlDiskSlot"))
if mibBuilder.loadTexts: eqlDiskStatusChange.setStatus('current')
mibBuilder.exportSymbols("EQLDISK-MIB", eqlDiskSmartInfoThresholdExceeded=eqlDiskSmartInfoThresholdExceeded, eqlDiskErrorLinkSeq=eqlDiskErrorLinkSeq, eqlDiskSerialNumber=eqlDiskSerialNumber, eqldiskMgmtNotifications=eqldiskMgmtNotifications, eqlDiskType=eqlDiskType, eqlDiskIndex=eqlDiskIndex, eqlDiskErrorPhyInternal=eqlDiskErrorPhyInternal, eqlDiskSmartInfoSpinBuzzWorst=eqlDiskSmartInfoSpinBuzzWorst, eqlDiskSmartInfoSpinupRetriesWorst=eqlDiskSmartInfoSpinupRetriesWorst, eqlDiskSmartInfoThermalAsperityRateWorst=eqlDiskSmartInfoThermalAsperityRateWorst, eqlDiskSmartInfoThroughputPerformanceWorst=eqlDiskSmartInfoThroughputPerformanceWorst, eqlDiskSmartInfoRawReadErrorRate=eqlDiskSmartInfoRawReadErrorRate, eqlDiskSmartInfoDriveRecalibRetryCountWorst=eqlDiskSmartInfoDriveRecalibRetryCountWorst, eqlDiskSmartInfoSoftECCCorrection=eqlDiskSmartInfoSoftECCCorrection, eqlDiskSmartInfoDriveRecalibRetryCount=eqlDiskSmartInfoDriveRecalibRetryCount, eqlDiskSmartInfoPowerOnHours=eqlDiskSmartInfoPowerOnHours, eqlDiskSmartInfoSoftECCCorrectionWorst=eqlDiskSmartInfoSoftECCCorrectionWorst, eqlDiskSmartInfoSpinHighCountWorst=eqlDiskSmartInfoSpinHighCountWorst, eqlDiskSmartInfoSeekErrorRateWorst=eqlDiskSmartInfoSeekErrorRateWorst, eqlDiskSmartInfoPowerOnHoursWorst=eqlDiskSmartInfoPowerOnHoursWorst, eqlDiskStatusTable=eqlDiskStatusTable, eqlDiskSmartInfoECCErrors=eqlDiskSmartInfoECCErrors, eqlDiskSmartInfoUltraDMACRCErrorRate=eqlDiskSmartInfoUltraDMACRCErrorRate, eqlDiskSmartInfoSpinUpTimeWorst=eqlDiskSmartInfoSpinUpTimeWorst, eqlDiskSlot=eqlDiskSlot, eqlDiskSize=eqlDiskSize, eqlDiskErrorDisparity=eqlDiskErrorDisparity, eqlDiskSmartInfoOfflineSurfaceScan=eqlDiskSmartInfoOfflineSurfaceScan, eqlDiskSmartInfoThroughputPerformance=eqlDiskSmartInfoThroughputPerformance, eqlDiskSmartInfoEmergencyRetractCyclesWorst=eqlDiskSmartInfoEmergencyRetractCyclesWorst, eqlDiskSmartInfoSelfTestReallocSectors=eqlDiskSmartInfoSelfTestReallocSectors, eqlDiskEntry=eqlDiskEntry, eqlDiskStatusXfers=eqlDiskStatusXfers, eqlDiskHealth=eqlDiskHealth, eqlDiskSmartInfoSeekPerformanceWorst=eqlDiskSmartInfoSeekPerformanceWorst, eqlDiskSmartInfoPendingDefects=eqlDiskSmartInfoPendingDefects, eqlDiskSmartInfoPowerCycleCountWorst=eqlDiskSmartInfoPowerCycleCountWorst, eqldiskModule=eqldiskModule, eqlDiskSmartInfoReadSoftErrorRateWorst=eqlDiskSmartInfoReadSoftErrorRateWorst, eqlDiskTypeEnum=eqlDiskTypeEnum, eqlDiskSmartInfoHDDTemp=eqlDiskSmartInfoHDDTemp, eqlDiskStatusTotalQD=eqlDiskStatusTotalQD, eqlDiskRPM=eqlDiskRPM, eqlDiskSmartInfoDAMErrorRate=eqlDiskSmartInfoDAMErrorRate, eqlDiskStatusBusyTime=eqlDiskStatusBusyTime, eqlDiskErrorHandShake=eqlDiskErrorHandShake, eqlDiskSmartInfoSpinupRetries=eqlDiskSmartInfoSpinupRetries, eqlDiskErrorPhyReady=eqlDiskErrorPhyReady, eqlDiskStatusNumResets=eqlDiskStatusNumResets, eqlDiskSmartInfoReadChannelMargin=eqlDiskSmartInfoReadChannelMargin, eqlDiskSmartInfoOnTheFlyErrorRate=eqlDiskSmartInfoOnTheFlyErrorRate, eqlDiskStatusChange=eqlDiskStatusChange, eqlDiskErrorUnrecFIS=eqlDiskErrorUnrecFIS, eqlDiskStatusBytesWritten=eqlDiskStatusBytesWritten, eqlDiskModelNumber=eqlDiskModelNumber, eqlDiskSmartInfoReallocatedSectorCount=eqlDiskSmartInfoReallocatedSectorCount, eqlDiskSmartInfoSpinHighCount=eqlDiskSmartInfoSpinHighCount, eqlDiskTable=eqlDiskTable, eqlDiskSmartInfoOffTrackErrors=eqlDiskSmartInfoOffTrackErrors, eqlDiskStatusNumIOs=eqlDiskStatusNumIOs, eqlDiskStatus=eqlDiskStatus, eqlDiskStatusEntry=eqlDiskStatusEntry, eqlDiskSmartInfoOnTheFlyErrorRateWorst=eqlDiskSmartInfoOnTheFlyErrorRateWorst, eqlDiskSmartInfoSeekErrorRate=eqlDiskSmartInfoSeekErrorRate, eqlDiskRevisionNumber=eqlDiskRevisionNumber, eqlDiskPI=eqlDiskPI, eqlDiskManufacturingInfo=eqlDiskManufacturingInfo, eqldiskConformance=eqldiskConformance, eqlDiskSmartInfoReallocatedSectorCountWorst=eqlDiskSmartInfoReallocatedSectorCountWorst, eqlDiskSmartInfoSpinBuzz=eqlDiskSmartInfoSpinBuzz, eqlDiskStatusBytesRead=eqlDiskStatusBytesRead, eqlDiskErrorEntry=eqlDiskErrorEntry, eqlDiskSmartInfoStartStopCount=eqlDiskSmartInfoStartStopCount, eqlDiskSmartInfoStartStopCountWorst=eqlDiskSmartInfoStartStopCountWorst, eqlDiskSectorSize=eqlDiskSectorSize, eqlDiskSmartInfoLoadUnloadCycles=eqlDiskSmartInfoLoadUnloadCycles, eqlDiskSmartInfoHDDTempWorst=eqlDiskSmartInfoHDDTempWorst, eqlDiskErrors=eqlDiskErrors, eqlDiskId=eqlDiskId, eqlDiskErrorCRC=eqlDiskErrorCRC, eqlDiskSmartInfoOfflineSeekPerformance=eqlDiskSmartInfoOfflineSeekPerformance, eqlDiskSmartInfoOffTrackErrorsWorst=eqlDiskSmartInfoOffTrackErrorsWorst, eqlDiskSmartInfoWritePreampErrorsWorst=eqlDiskSmartInfoWritePreampErrorsWorst, eqlDiskStatusLifetime=eqlDiskStatusLifetime, eqlDiskSmartInfoRawReadErrorRateWorst=eqlDiskSmartInfoRawReadErrorRateWorst, eqlDiskSmartInfoEntry=eqlDiskSmartInfoEntry, eqlDiskErrorTable=eqlDiskErrorTable, eqlDiskSmartInfoECCErrorsWorst=eqlDiskSmartInfoECCErrorsWorst, eqlDiskErrorDecode10b8b=eqlDiskErrorDecode10b8b, eqlDiskSmartInfoPowerCycleCount=eqlDiskSmartInfoPowerCycleCount, eqlDiskSmartInfoUltraDMACRCErrorRateWorst=eqlDiskSmartInfoUltraDMACRCErrorRateWorst, eqlDiskSmartInfoDAMErrorRateWorst=eqlDiskSmartInfoDAMErrorRateWorst, eqlDiskErrorCommWake=eqlDiskErrorCommWake, eqlDiskSmartInfoSpinUpTime=eqlDiskSmartInfoSpinUpTime, eqlDiskSmartInfoEmergencyRetractCycles=eqlDiskSmartInfoEmergencyRetractCycles, PYSNMP_MODULE_ID=eqldiskModule, eqlDiskSmartInfoOfflineSurfaceScanWorst=eqlDiskSmartInfoOfflineSurfaceScanWorst, eqlDiskErrorTransportState=eqlDiskErrorTransportState, eqlDiskAdminStatus=eqlDiskAdminStatus, eqldiskNotifications=eqldiskNotifications, eqlDiskSmartInfoReadChannelMarginWorst=eqlDiskSmartInfoReadChannelMarginWorst, eqlDiskStatusFailXfers=eqlDiskStatusFailXfers, eqlDiskSmartInfoThermalAsperityRate=eqlDiskSmartInfoThermalAsperityRate, eqlDiskSmartInfoOfflineSeekPerformanceWorst=eqlDiskSmartInfoOfflineSeekPerformanceWorst, eqldiskObjects=eqldiskObjects, eqlDiskSmartInfoTable=eqlDiskSmartInfoTable, eqlDiskSmartInfoReadSoftErrorRate=eqlDiskSmartInfoReadSoftErrorRate, eqlDiskSmartInfoSelfTestReallocSectorsWorst=eqlDiskSmartInfoSelfTestReallocSectorsWorst, eqlDiskSmartInfoSeekPerformance=eqlDiskSmartInfoSeekPerformance, eqlDiskSmartInfoWritePreampErrors=eqlDiskSmartInfoWritePreampErrors, eqlDiskSmartInfoLoadUnloadCyclesWorst=eqlDiskSmartInfoLoadUnloadCyclesWorst, eqlDiskSmartInfoPendingDefectsWorst=eqlDiskSmartInfoPendingDefectsWorst)
