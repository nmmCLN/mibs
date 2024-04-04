#
# PySNMP MIB module F5-PLATFORM-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-PLATFORM-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:00 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
platform, f5Compliance = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform", "f5Compliance")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Counter64, MibIdentifier, iso, Bits, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Counter64", "MibIdentifier", "iso", "Bits", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
f5PlatformStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 2))
if mibBuilder.loadTexts: f5PlatformStats.setLastUpdated('202101300000Z')
if mibBuilder.loadTexts: f5PlatformStats.setOrganization('F5 Networks, Inc.')
f5PlatformStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1))
platformCpuStatsTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1))
platformDiskStatsTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2))
platformTemperatureTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3))
platformMemoryStatsTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4))
platformFpgaTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5))
platformFwTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6))
platformFantrayTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7))
class PlatformStatsIndex(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class String(DisplayString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 255)

cpuProcessorStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1), )
if mibBuilder.loadTexts: cpuProcessorStatsTable.setStatus('current')
cpuProcessorStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"), (0, "F5-PLATFORM-STATS-MIB", "cpuIndex"))
if mibBuilder.loadTexts: cpuProcessorStatsEntry.setStatus('current')
index = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 1), PlatformStatsIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: index.setStatus('current')
cpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuIndex.setStatus('current')
cpuCacheSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 3), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuCacheSize.setStatus('current')
cpuCoreCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 4), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuCoreCnt.setStatus('current')
cpuFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 5), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuFreq.setStatus('current')
cpuStepping = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 6), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuStepping.setStatus('current')
cpuThreadCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 7), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuThreadCnt.setStatus('current')
cpuModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 8), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuModelName.setStatus('current')
cpuUtilizationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2), )
if mibBuilder.loadTexts: cpuUtilizationStatsTable.setStatus('current')
cpuUtilizationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"))
if mibBuilder.loadTexts: cpuUtilizationStatsEntry.setStatus('current')
cpuCore = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuCore.setStatus('current')
cpuCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 2), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuCurrent.setStatus('current')
cpuTotal5secAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 3), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuTotal5secAvg.setStatus('current')
cpuTotal1minAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 4), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuTotal1minAvg.setStatus('current')
cpuTotal5minAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 5), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuTotal5minAvg.setStatus('current')
cpuCoreStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3), )
if mibBuilder.loadTexts: cpuCoreStatsTable.setStatus('current')
cpuCoreStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"), (0, "F5-PLATFORM-STATS-MIB", "coreIndex"))
if mibBuilder.loadTexts: cpuCoreStatsEntry.setStatus('current')
coreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coreIndex.setStatus('current')
coreName = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coreName.setStatus('current')
coreCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 3), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: coreCurrent.setStatus('current')
coreTotal5secAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 4), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: coreTotal5secAvg.setStatus('current')
coreTotal1minAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 5), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: coreTotal1minAvg.setStatus('current')
coreTotal5minAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 6), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: coreTotal5minAvg.setStatus('current')
diskInfoTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1), )
if mibBuilder.loadTexts: diskInfoTable.setStatus('current')
diskInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"), (0, "F5-PLATFORM-STATS-MIB", "diskName"))
if mibBuilder.loadTexts: diskInfoEntry.setStatus('current')
diskName = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskName.setStatus('current')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('current')
diskVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskVendor.setStatus('current')
diskVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskVersion.setStatus('current')
diskSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSerialNo.setStatus('current')
diskSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSize.setStatus('current')
diskType = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskType.setStatus('current')
diskUtilizationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2), )
if mibBuilder.loadTexts: diskUtilizationStatsTable.setStatus('current')
diskUtilizationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"), (0, "F5-PLATFORM-STATS-MIB", "diskName"))
if mibBuilder.loadTexts: diskUtilizationStatsEntry.setStatus('current')
diskPercentageUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPercentageUsed.setStatus('current')
diskTotalIops = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 4), Counter64()).setUnits('IOPs').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTotalIops.setStatus('current')
diskReadIops = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 5), Counter64()).setUnits('IOPs').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadIops.setStatus('current')
diskReadMerged = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadMerged.setStatus('current')
diskReadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 7), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadBytes.setStatus('current')
diskReadLatencyMs = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 8), Counter64()).setUnits('ms').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadLatencyMs.setStatus('current')
diskWriteIops = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 9), Counter64()).setUnits('IOPs').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteIops.setStatus('current')
diskWriteMerged = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteMerged.setStatus('current')
diskWriteBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 11), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteBytes.setStatus('current')
diskWriteLatencyMs = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 12), Counter64()).setUnits('ms').setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteLatencyMs.setStatus('current')
temperatureStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1), )
if mibBuilder.loadTexts: temperatureStatsTable.setStatus('current')
temperatureStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"))
if mibBuilder.loadTexts: temperatureStatsEntry.setStatus('current')
tempCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setUnits('centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: tempCurrent.setStatus('current')
tempAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setUnits('centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: tempAverage.setStatus('current')
tempMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setUnits('centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: tempMinimum.setStatus('current')
tempMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setUnits('centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: tempMaximum.setStatus('current')
memoryStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1), )
if mibBuilder.loadTexts: memoryStatsTable.setStatus('current')
memoryStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"))
if mibBuilder.loadTexts: memoryStatsEntry.setStatus('current')
memAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 2), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: memAvailable.setStatus('current')
memFree = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 3), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: memFree.setStatus('current')
memPercentageUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: memPercentageUsed.setStatus('current')
memPlatformTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 5), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: memPlatformTotal.setStatus('current')
memPlatformUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 6), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: memPlatformUsed.setStatus('current')
fpgaTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1), )
if mibBuilder.loadTexts: fpgaTable.setStatus('current')
fpgaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"), (0, "F5-PLATFORM-STATS-MIB", "fpgaIndex"))
if mibBuilder.loadTexts: fpgaEntry.setStatus('current')
fpgaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpgaIndex.setStatus('current')
fpgaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpgaVersion.setStatus('current')
fwTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1), )
if mibBuilder.loadTexts: fwTable.setStatus('current')
fwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"), (0, "F5-PLATFORM-STATS-MIB", "fwName"))
if mibBuilder.loadTexts: fwEntry.setStatus('current')
fwName = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwName.setStatus('current')
fwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwVersion.setStatus('current')
configurable = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurable.setStatus('current')
fwUpdateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwUpdateStatus.setStatus('current')
fantrayStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1), )
if mibBuilder.loadTexts: fantrayStatsTable.setStatus('current')
fantrayStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1), ).setIndexNames((0, "F5-PLATFORM-STATS-MIB", "index"))
if mibBuilder.loadTexts: fantrayStatsEntry.setStatus('current')
fan_1_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 1), Integer32()).setLabel("fan-1-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_1_speed.setStatus('current')
fan_2_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 2), Integer32()).setLabel("fan-2-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_2_speed.setStatus('current')
fan_3_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 3), Integer32()).setLabel("fan-3-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_3_speed.setStatus('current')
fan_4_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 4), Integer32()).setLabel("fan-4-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_4_speed.setStatus('current')
fan_5_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 5), Integer32()).setLabel("fan-5-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_5_speed.setStatus('current')
fan_6_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 6), Integer32()).setLabel("fan-6-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_6_speed.setStatus('current')
fan_7_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 7), Integer32()).setLabel("fan-7-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_7_speed.setStatus('current')
fan_8_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 8), Integer32()).setLabel("fan-8-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_8_speed.setStatus('current')
fan_9_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 9), Integer32()).setLabel("fan-9-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_9_speed.setStatus('current')
fan_10_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 10), Integer32()).setLabel("fan-10-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_10_speed.setStatus('current')
fan_11_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 11), Integer32()).setLabel("fan-11-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_11_speed.setStatus('current')
fan_12_speed = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 12), Integer32()).setLabel("fan-12-speed").setUnits('RPM').setMaxAccess("readonly")
if mibBuilder.loadTexts: fan_12_speed.setStatus('current')
platformConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2))
platformGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1))
platformCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 2))
platformCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 2, 1)).setObjects(("F5-PLATFORM-STATS-MIB", "platformCPUGroup"), ("F5-PLATFORM-STATS-MIB", "platformDiskGroup"), ("F5-PLATFORM-STATS-MIB", "platformTempGroup"), ("F5-PLATFORM-STATS-MIB", "platformMemGroup"), ("F5-PLATFORM-STATS-MIB", "platformFpgaGroup"), ("F5-PLATFORM-STATS-MIB", "platformFwVersionGroup"), ("F5-PLATFORM-STATS-MIB", "platformFantrayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformCompliance = platformCompliance.setStatus('current')
platformCPUGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 1)).setObjects(("F5-PLATFORM-STATS-MIB", "index"), ("F5-PLATFORM-STATS-MIB", "cpuIndex"), ("F5-PLATFORM-STATS-MIB", "cpuCacheSize"), ("F5-PLATFORM-STATS-MIB", "cpuCoreCnt"), ("F5-PLATFORM-STATS-MIB", "cpuFreq"), ("F5-PLATFORM-STATS-MIB", "cpuStepping"), ("F5-PLATFORM-STATS-MIB", "cpuThreadCnt"), ("F5-PLATFORM-STATS-MIB", "cpuModelName"), ("F5-PLATFORM-STATS-MIB", "cpuCore"), ("F5-PLATFORM-STATS-MIB", "cpuCurrent"), ("F5-PLATFORM-STATS-MIB", "cpuTotal5secAvg"), ("F5-PLATFORM-STATS-MIB", "cpuTotal1minAvg"), ("F5-PLATFORM-STATS-MIB", "cpuTotal5minAvg"), ("F5-PLATFORM-STATS-MIB", "coreIndex"), ("F5-PLATFORM-STATS-MIB", "coreCurrent"), ("F5-PLATFORM-STATS-MIB", "coreTotal5secAvg"), ("F5-PLATFORM-STATS-MIB", "coreTotal1minAvg"), ("F5-PLATFORM-STATS-MIB", "coreTotal5minAvg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformCPUGroup = platformCPUGroup.setStatus('current')
platformDiskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 2)).setObjects(("F5-PLATFORM-STATS-MIB", "diskName"), ("F5-PLATFORM-STATS-MIB", "diskModel"), ("F5-PLATFORM-STATS-MIB", "diskVendor"), ("F5-PLATFORM-STATS-MIB", "diskVersion"), ("F5-PLATFORM-STATS-MIB", "diskSerialNo"), ("F5-PLATFORM-STATS-MIB", "diskSize"), ("F5-PLATFORM-STATS-MIB", "diskType"), ("F5-PLATFORM-STATS-MIB", "diskPercentageUsed"), ("F5-PLATFORM-STATS-MIB", "diskTotalIops"), ("F5-PLATFORM-STATS-MIB", "diskReadIops"), ("F5-PLATFORM-STATS-MIB", "diskReadMerged"), ("F5-PLATFORM-STATS-MIB", "diskReadBytes"), ("F5-PLATFORM-STATS-MIB", "diskReadLatencyMs"), ("F5-PLATFORM-STATS-MIB", "diskWriteIops"), ("F5-PLATFORM-STATS-MIB", "diskWriteMerged"), ("F5-PLATFORM-STATS-MIB", "diskWriteBytes"), ("F5-PLATFORM-STATS-MIB", "diskWriteLatencyMs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformDiskGroup = platformDiskGroup.setStatus('current')
platformTempGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 3)).setObjects(("F5-PLATFORM-STATS-MIB", "tempCurrent"), ("F5-PLATFORM-STATS-MIB", "tempAverage"), ("F5-PLATFORM-STATS-MIB", "tempMinimum"), ("F5-PLATFORM-STATS-MIB", "tempMaximum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformTempGroup = platformTempGroup.setStatus('current')
platformMemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 4)).setObjects(("F5-PLATFORM-STATS-MIB", "memAvailable"), ("F5-PLATFORM-STATS-MIB", "memFree"), ("F5-PLATFORM-STATS-MIB", "memPercentageUsed"), ("F5-PLATFORM-STATS-MIB", "memPlatformTotal"), ("F5-PLATFORM-STATS-MIB", "memPlatformUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformMemGroup = platformMemGroup.setStatus('current')
platformFpgaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 5)).setObjects(("F5-PLATFORM-STATS-MIB", "fpgaIndex"), ("F5-PLATFORM-STATS-MIB", "fpgaVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformFpgaGroup = platformFpgaGroup.setStatus('current')
platformFwVersionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 6)).setObjects(("F5-PLATFORM-STATS-MIB", "fwName"), ("F5-PLATFORM-STATS-MIB", "fwVersion"), ("F5-PLATFORM-STATS-MIB", "configurable"), ("F5-PLATFORM-STATS-MIB", "fwUpdateStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformFwVersionGroup = platformFwVersionGroup.setStatus('current')
platformFantrayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 7)).setObjects(("F5-PLATFORM-STATS-MIB", "fan_1_speed"), ("F5-PLATFORM-STATS-MIB", "fan_2_speed"), ("F5-PLATFORM-STATS-MIB", "fan_3_speed"), ("F5-PLATFORM-STATS-MIB", "fan_4_speed"), ("F5-PLATFORM-STATS-MIB", "fan_5_speed"), ("F5-PLATFORM-STATS-MIB", "fan_6_speed"), ("F5-PLATFORM-STATS-MIB", "fan_7_speed"), ("F5-PLATFORM-STATS-MIB", "fan_8_speed"), ("F5-PLATFORM-STATS-MIB", "fan_9_speed"), ("F5-PLATFORM-STATS-MIB", "fan_10_speed"), ("F5-PLATFORM-STATS-MIB", "fan_11_speed"), ("F5-PLATFORM-STATS-MIB", "fan_12_speed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    platformFantrayGroup = platformFantrayGroup.setStatus('current')
mibBuilder.exportSymbols("F5-PLATFORM-STATS-MIB", cpuCurrent=cpuCurrent, tempAverage=tempAverage, diskPercentageUsed=diskPercentageUsed, diskReadIops=diskReadIops, diskSize=diskSize, fwName=fwName, fwEntry=fwEntry, cpuCore=cpuCore, diskTotalIops=diskTotalIops, cpuUtilizationStatsTable=cpuUtilizationStatsTable, fwTable=fwTable, cpuCoreCnt=cpuCoreCnt, diskWriteMerged=diskWriteMerged, memoryStatsTable=memoryStatsTable, temperatureStatsEntry=temperatureStatsEntry, cpuUtilizationStatsEntry=cpuUtilizationStatsEntry, tempMinimum=tempMinimum, memPlatformUsed=memPlatformUsed, cpuTotal5secAvg=cpuTotal5secAvg, fantrayStatsEntry=fantrayStatsEntry, platformFpgaGroup=platformFpgaGroup, cpuCoreStatsEntry=cpuCoreStatsEntry, memPlatformTotal=memPlatformTotal, diskReadMerged=diskReadMerged, cpuThreadCnt=cpuThreadCnt, fan_5_speed=fan_5_speed, PlatformStatsIndex=PlatformStatsIndex, coreIndex=coreIndex, tempMaximum=tempMaximum, fan_1_speed=fan_1_speed, diskVersion=diskVersion, fan_8_speed=fan_8_speed, fantrayStatsTable=fantrayStatsTable, coreCurrent=coreCurrent, coreTotal5secAvg=coreTotal5secAvg, tempCurrent=tempCurrent, platformConformance=platformConformance, fan_7_speed=fan_7_speed, platformFantrayTable=platformFantrayTable, diskReadBytes=diskReadBytes, memPercentageUsed=memPercentageUsed, platformMemoryStatsTable=platformMemoryStatsTable, cpuStepping=cpuStepping, diskWriteLatencyMs=diskWriteLatencyMs, memAvailable=memAvailable, coreName=coreName, fan_10_speed=fan_10_speed, platformGroups=platformGroups, memoryStatsEntry=memoryStatsEntry, coreTotal1minAvg=coreTotal1minAvg, temperatureStatsTable=temperatureStatsTable, diskModel=diskModel, fan_6_speed=fan_6_speed, platformCompliances=platformCompliances, cpuTotal1minAvg=cpuTotal1minAvg, fpgaTable=fpgaTable, cpuModelName=cpuModelName, String=String, fpgaEntry=fpgaEntry, platformCompliance=platformCompliance, cpuIndex=cpuIndex, index=index, diskReadLatencyMs=diskReadLatencyMs, cpuProcessorStatsEntry=cpuProcessorStatsEntry, diskWriteIops=diskWriteIops, platformCpuStatsTable=platformCpuStatsTable, diskVendor=diskVendor, cpuCacheSize=cpuCacheSize, cpuProcessorStatsTable=cpuProcessorStatsTable, memFree=memFree, platformTempGroup=platformTempGroup, fan_2_speed=fan_2_speed, f5PlatformStatsObjects=f5PlatformStatsObjects, fan_11_speed=fan_11_speed, diskWriteBytes=diskWriteBytes, platformCPUGroup=platformCPUGroup, platformFwTable=platformFwTable, fan_12_speed=fan_12_speed, platformFantrayGroup=platformFantrayGroup, coreTotal5minAvg=coreTotal5minAvg, fan_4_speed=fan_4_speed, f5PlatformStats=f5PlatformStats, fpgaVersion=fpgaVersion, cpuTotal5minAvg=cpuTotal5minAvg, configurable=configurable, fwUpdateStatus=fwUpdateStatus, diskUtilizationStatsEntry=diskUtilizationStatsEntry, diskType=diskType, platformMemGroup=platformMemGroup, platformTemperatureTable=platformTemperatureTable, platformFwVersionGroup=platformFwVersionGroup, fpgaIndex=fpgaIndex, cpuFreq=cpuFreq, diskName=diskName, fwVersion=fwVersion, PYSNMP_MODULE_ID=f5PlatformStats, diskInfoTable=diskInfoTable, cpuCoreStatsTable=cpuCoreStatsTable, diskSerialNo=diskSerialNo, platformDiskGroup=platformDiskGroup, fan_3_speed=fan_3_speed, fan_9_speed=fan_9_speed, platformFpgaTable=platformFpgaTable, platformDiskStatsTable=platformDiskStatsTable, diskInfoEntry=diskInfoEntry, diskUtilizationStatsTable=diskUtilizationStatsTable)
