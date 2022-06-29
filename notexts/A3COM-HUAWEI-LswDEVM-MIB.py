#
# PySNMP MIB module A3COM-HUAWEI-LswDEVM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/3com/A3COM-HUAWEI-LswDEVM-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:34 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
hwLswSlotIndex, hwLswFrameIndex = mibBuilder.importSymbols("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex", "hwLswFrameIndex")
huaweiUtility, lswCommon = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiUtility", "lswCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, Gauge32, ObjectIdentity, ModuleIdentity, Unsigned32, Bits, TimeTicks, Integer32, NotificationType, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Bits", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwLswdevMMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9))
hwLswdevMMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswdevMMib.setLastUpdated('201111260000Z')
if mibBuilder.loadTexts: hwLswdevMMib.setOrganization('')
hwDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1))
hwCpuTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1), )
if mibBuilder.loadTexts: hwCpuTable.setStatus('current')
hwCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwCpuIndex"))
if mibBuilder.loadTexts: hwCpuEntry.setStatus('current')
hwCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hwCpuIndex.setStatus('current')
hwCpuCostRate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCpuCostRate.setStatus('current')
hwCpuCostRatePer1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCpuCostRatePer1Min.setStatus('current')
hwCpuCostRatePer5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCpuCostRatePer5Min.setStatus('current')
hwMem = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2))
hwMemTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1), )
if mibBuilder.loadTexts: hwMemTable.setStatus('current')
hwMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwMemModuleIndex"))
if mibBuilder.loadTexts: hwMemEntry.setStatus('current')
hwMemModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hwMemModuleIndex.setStatus('current')
hwMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemSize.setStatus('current')
hwMemFree = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemFree.setStatus('current')
hwMemRawSliceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemRawSliceUsed.setStatus('current')
hwMemLgFree = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemLgFree.setStatus('current')
hwMemFail = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemFail.setStatus('current')
hwMemFailNoMem = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemFailNoMem.setStatus('current')
hwBufTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2), )
if mibBuilder.loadTexts: hwBufTable.setStatus('current')
hwBufEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwBufModuleIndex"), (0, "A3COM-HUAWEI-LswDEVM-MIB", "hwBufSize"))
if mibBuilder.loadTexts: hwBufEntry.setStatus('current')
hwBufModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hwBufModuleIndex.setStatus('current')
hwBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: hwBufSize.setStatus('current')
hwBufCurrentTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBufCurrentTotal.setStatus('current')
hwBufCurrentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBufCurrentUsed.setStatus('current')
hwFlh = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3))
hwFlhTotalSize = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhTotalSize.setStatus('current')
hwFlhTotalFree = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhTotalFree.setStatus('current')
hwFlhLastDelTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhLastDelTime.setStatus('current')
hwFlhDelState = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("executing", 1), ("ok", 2), ("error", 3), ("readOnly", 4), ("failtoopen", 5), ("blockMallocFail", 6), ("noneDelOperationSinceStart", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhDelState.setStatus('current')
hwFlhState = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("busy", 1), ("free", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhState.setStatus('current')
hwLswdevMMibObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1))
if mibBuilder.loadTexts: hwLswdevMMibObject.setStatus('current')
hwdevMFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1), )
if mibBuilder.loadTexts: hwdevMFanStatusTable.setStatus('current')
hwdevMFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwDevMFanNum"))
if mibBuilder.loadTexts: hwdevMFanStatusEntry.setStatus('current')
hwDevMFanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMFanNum.setStatus('current')
hwDevMFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("deactive", 2), ("not-install", 3), ("unsupport", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMFanStatus.setStatus('current')
hwdevMPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2), )
if mibBuilder.loadTexts: hwdevMPowerStatusTable.setStatus('current')
hwdevMPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum"))
if mibBuilder.loadTexts: hwdevMPowerStatusEntry.setStatus('current')
hwDevMPowerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMPowerNum.setStatus('current')
hwDevMPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("deactive", 2), ("not-install", 3), ("unsupport", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMPowerStatus.setStatus('current')
hwdevMSlotEnvironmentTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3), )
if mibBuilder.loadTexts: hwdevMSlotEnvironmentTable.setStatus('current')
hwdevMSlotEnvironmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"), (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"), (0, "A3COM-HUAWEI-LswDEVM-MIB", "hwdevMSlotEnvironmentType"))
if mibBuilder.loadTexts: hwdevMSlotEnvironmentEntry.setStatus('current')
hwdevMSlotEnvironmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("temperature", 1), ("humidity", 2), ("fog", 3))))
if mibBuilder.loadTexts: hwdevMSlotEnvironmentType.setStatus('current')
hwDevMSlotEnvironmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("upper", 2), ("lower", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentStatus.setStatus('current')
hwDevMSlotEnvironmentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentValue.setStatus('current')
hwDevMSlotEnvironmentUpperLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentUpperLimit.setStatus('current')
hwDevMSlotEnvironmentLowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentLowerLimit.setStatus('current')
hwLinkUpDownTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableBoth", 1), ("disableBoth", 2), ("enableLinkUpTrapOnly", 3), ("enableLinkDownTrapOnly", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLinkUpDownTrapEnable.setStatus('current')
hwdot1qTpFdbLearnStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbLearnStatus.setStatus('current')
hwCfmWriteFlash = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("write", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCfmWriteFlash.setStatus('current')
hwCfmEraseFlash = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("erase", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCfmEraseFlash.setStatus('current')
hwDevMFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 13), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwDevMFirstTrapTime.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswDEVM-MIB", hwLswdevMMibObject=hwLswdevMMibObject, hwFlhDelState=hwFlhDelState, hwDevMSlotEnvironmentValue=hwDevMSlotEnvironmentValue, hwCpuEntry=hwCpuEntry, hwBufEntry=hwBufEntry, hwMemLgFree=hwMemLgFree, hwBufCurrentTotal=hwBufCurrentTotal, hwCpuTable=hwCpuTable, hwDevMSlotEnvironmentUpperLimit=hwDevMSlotEnvironmentUpperLimit, hwMemFree=hwMemFree, hwCpuCostRate=hwCpuCostRate, hwDevMFirstTrapTime=hwDevMFirstTrapTime, hwFlhTotalSize=hwFlhTotalSize, hwFlhTotalFree=hwFlhTotalFree, hwdot1qTpFdbLearnStatus=hwdot1qTpFdbLearnStatus, PYSNMP_MODULE_ID=hwLswdevMMib, hwFlhState=hwFlhState, hwDevMFanStatus=hwDevMFanStatus, hwDevMSlotEnvironmentStatus=hwDevMSlotEnvironmentStatus, hwdevMSlotEnvironmentType=hwdevMSlotEnvironmentType, hwBufCurrentUsed=hwBufCurrentUsed, hwDevice=hwDevice, hwFlhLastDelTime=hwFlhLastDelTime, hwdevMPowerStatusTable=hwdevMPowerStatusTable, hwMemTable=hwMemTable, hwCpuCostRatePer1Min=hwCpuCostRatePer1Min, hwLswdevMMib=hwLswdevMMib, hwCpuCostRatePer5Min=hwCpuCostRatePer5Min, hwdevMFanStatusTable=hwdevMFanStatusTable, hwdevMPowerStatusEntry=hwdevMPowerStatusEntry, hwFlh=hwFlh, hwMem=hwMem, hwCpuIndex=hwCpuIndex, hwMemFail=hwMemFail, hwdevMSlotEnvironmentEntry=hwdevMSlotEnvironmentEntry, hwBufSize=hwBufSize, hwDevMSlotEnvironmentLowerLimit=hwDevMSlotEnvironmentLowerLimit, hwBufTable=hwBufTable, hwMemEntry=hwMemEntry, hwBufModuleIndex=hwBufModuleIndex, hwDevMFanNum=hwDevMFanNum, hwDevMPowerStatus=hwDevMPowerStatus, hwMemSize=hwMemSize, hwdevMFanStatusEntry=hwdevMFanStatusEntry, hwDevMPowerNum=hwDevMPowerNum, hwMemFailNoMem=hwMemFailNoMem, hwMemRawSliceUsed=hwMemRawSliceUsed, hwMemModuleIndex=hwMemModuleIndex, hwLinkUpDownTrapEnable=hwLinkUpDownTrapEnable, hwCfmEraseFlash=hwCfmEraseFlash, hwdevMSlotEnvironmentTable=hwdevMSlotEnvironmentTable, hwCfmWriteFlash=hwCfmWriteFlash)
