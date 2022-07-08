#
# PySNMP MIB module EQLSTORAGEPOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLSTORAGEPOOL-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
eqlStorageGroupAdminAccountName, eqlLdapLoginAccessType, eqlGroupId, UTFString, eqlLdapLoginAccessName, eqlStorageGroupAdminAccountIndex = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlStorageGroupAdminAccountName", "eqlLdapLoginAccessType", "eqlGroupId", "UTFString", "eqlLdapLoginAccessName", "eqlStorageGroupAdminAccountIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ObjectIdentity, IpAddress, Bits, Counter64, Counter32, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, NotificationType, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "IpAddress", "Bits", "Counter64", "Counter32", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "NotificationType", "iso", "TimeTicks", "ModuleIdentity")
RowPointer, TruthValue, TextualConvention, RowStatus, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TruthValue", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime")
eqlStoragePoolModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 16))
eqlStoragePoolModule.setRevisions(('2005-03-17 00:00',))
if mibBuilder.loadTexts: eqlStoragePoolModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlStoragePoolModule.setOrganization('EqualLogic Inc.')
eqlStoragePoolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 16, 1))
eqlStoragePoolNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 16, 2))
eqlStoragePoolConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 16, 3))
class SiteIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class SiteIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Unsigned64(TextualConvention, Counter64):
    status = 'current'

class PoolQuotaType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("size", 1))

class StatusEnabledDefault(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("enabled", 0), ("disabled", 1))

eqlStoragePoolTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1), )
if mibBuilder.loadTexts: eqlStoragePoolTable.setStatus('current')
eqlStoragePoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"))
if mibBuilder.loadTexts: eqlStoragePoolEntry.setStatus('current')
eqlStoragePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlStoragePoolIndex.setStatus('current')
eqlStoragePoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolRowStatus.setStatus('current')
eqlStoragePoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 3), UTFString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)).clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolName.setStatus('current')
eqlStoragePoolDefaultFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolDefaultFlag.setStatus('current')
eqlStoragePoolRAIDConfigWaitFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolRAIDConfigWaitFlag.setStatus('current')
eqlStoragePoolShouldEvalMask = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolShouldEvalMask.setStatus('current')
eqlStoragePoolLastBalance = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolLastBalance.setStatus('current')
eqlStoragePoolDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolDescription.setStatus('current')
eqlStoragePoolLeadMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolLeadMemberId.setStatus('deprecated')
eqlStoragePoolUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolUUID.setStatus('current')
eqlStoragePoolExecMergeTo = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolExecMergeTo.setStatus('current')
eqlStoragePoolBorrow = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 12), StatusEnabledDefault().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolBorrow.setStatus('current')
eqlStoragePoolSnapTrimThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolSnapTrimThreshold.setStatus('current')
eqlStoragePoolSnapTrimBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 14), Counter64().clone(600)).setUnits('MB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolSnapTrimBuffer.setStatus('current')
eqlStoragePoolSnapTrimmerHWMLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 15), Integer32().clone(864000)).setUnits('secs').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolSnapTrimmerHWMLifeTime.setStatus('current')
eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 16), Integer32().clone(60)).setUnits('secs').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval.setStatus('current')
eqlStoragePoolDefaultCompressionStrategy = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("automatic", 0), ("always", 1), ("never", 2))).clone('automatic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolDefaultCompressionStrategy.setStatus('current')
eqlStoragePoolDefaultCompressionMinSnapDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 18), Integer32().clone(10)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolDefaultCompressionMinSnapDelay.setStatus('current')
eqlStoragePoolDefaultCompressionMinSnapAge = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 19), Integer32().clone(1380)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolDefaultCompressionMinSnapAge.setStatus('current')
eqlStoragePoolSnapMemberTrimThresholdAmount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 20), Counter64().clone(204800)).setUnits('MB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolSnapMemberTrimThresholdAmount.setStatus('current')
eqlStoragePoolSnapTrimRecheckTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 21), Unsigned32().clone(20)).setUnits('secs').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolSnapTrimRecheckTimer.setStatus('current')
eqlStoragePoolStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2), )
if mibBuilder.loadTexts: eqlStoragePoolStatsTable.setStatus('current')
eqlStoragePoolStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1), )
eqlStoragePoolEntry.registerAugmentions(("EQLSTORAGEPOOL-MIB", "eqlStoragePoolStatsEntry"))
eqlStoragePoolStatsEntry.setIndexNames(*eqlStoragePoolEntry.getIndexNames())
if mibBuilder.loadTexts: eqlStoragePoolStatsEntry.setStatus('current')
eqlStoragePoolStatsSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSpace.setStatus('current')
eqlStoragePoolStatsSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSpaceUsed.setStatus('current')
eqlStoragePoolStatsFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsFreeSpace.setStatus('current')
eqlStoragePoolStatsReplicationSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsReplicationSpace.setStatus('current')
eqlStoragePoolStatsReplicationSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsReplicationSpaceUsed.setStatus('current')
eqlStoragePoolStatsReplicationFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsReplicationFreeSpace.setStatus('current')
eqlStoragePoolStatsMemberNumOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsMemberNumOnline.setStatus('current')
eqlStoragePoolStatsMemberCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsMemberCount.setStatus('current')
eqlStoragePoolStatsSnapshotReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapshotReserved.setStatus('current')
eqlStoragePoolStatsSnapshotUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapshotUsed.setStatus('current')
eqlStoragePoolStatsSnapshotNumInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapshotNumInUse.setStatus('current')
eqlStoragePoolStatsSnapshotNumOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapshotNumOnline.setStatus('current')
eqlStoragePoolStatsSnapshotCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapshotCount.setStatus('current')
eqlStoragePoolStatsVolumeNumInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVolumeNumInUse.setStatus('current')
eqlStoragePoolStatsVolumeNumOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVolumeNumOnline.setStatus('current')
eqlStoragePoolStatsVolumeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVolumeCount.setStatus('current')
eqlStoragePoolStatsDelegatedSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsDelegatedSpace.setStatus('current')
eqlStoragePoolStatsDelegatedSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsDelegatedSpaceUsed.setStatus('current')
eqlStoragePoolStatsMembersInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsMembersInUse.setStatus('current')
eqlStoragePoolStatsVolumeSubscribed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 20), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVolumeSubscribed.setStatus('current')
eqlStoragePoolStatsVolumeSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 21), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVolumeSpaceAllocated.setStatus('current')
eqlStoragePoolStatsFailbackSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 22), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsFailbackSpace.setStatus('current')
eqlStoragePoolStatsThinProvFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 23), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsThinProvFreeSpace.setStatus('current')
eqlStoragePoolStatsConnectionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsConnectionCount.setStatus('current')
eqlStoragePoolStatsSnapshotResvFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 25), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapshotResvFreeSpace.setStatus('current')
eqlStoragePoolStatsVirtualVolumeNumInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVirtualVolumeNumInUse.setStatus('current')
eqlStoragePoolStatsVirtualVolumeNumOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVirtualVolumeNumOnline.setStatus('current')
eqlStoragePoolStatsSnapshotResvBorrowing = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 28), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapshotResvBorrowing.setStatus('current')
eqlStoragePoolStatsFreeSpaceBorrowing = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 29), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsFreeSpaceBorrowing.setStatus('current')
eqlStoragePoolStatsAvailableForBorrowing = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 30), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsAvailableForBorrowing.setStatus('current')
eqlStoragePoolStatsRecoverableVolBorrowing = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 31), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsRecoverableVolBorrowing.setStatus('current')
eqlStoragePoolStatsActualFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 32), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsActualFreeSpace.setStatus('current')
eqlStoragePoolStatsTotalSpaceBorrowing = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 33), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsTotalSpaceBorrowing.setStatus('current')
eqlStoragePoolStatsSnapShotBorrowing = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 34), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsSnapShotBorrowing.setStatus('current')
eqlStoragePoolStatsStorageContainerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsStorageContainerCount.setStatus('current')
eqlStoragePoolStatsStorageContainerSpaceReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 36), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsStorageContainerSpaceReserved.setStatus('current')
eqlStoragePoolStatsCompressedSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 37), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsCompressedSpaceUsed.setStatus('current')
eqlStoragePoolStatsVirtualSpaceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 38), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsVirtualSpaceSize.setStatus('current')
eqlStoragePoolStatsStorageContainerVolumeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsStorageContainerVolumeCount.setStatus('current')
eqlStoragePoolStatsStorageContainerSnapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsStorageContainerSnapCount.setStatus('current')
eqlStoragePoolStatsStorageContainerVolumesOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolStatsStorageContainerVolumesOnline.setStatus('current')
eqlStoragePoolAdminAccountTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 3), )
if mibBuilder.loadTexts: eqlStoragePoolAdminAccountTable.setStatus('current')
eqlStoragePoolAdminAccountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"), (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"))
if mibBuilder.loadTexts: eqlStoragePoolAdminAccountEntry.setStatus('current')
eqlStoragePoolAdminAccountRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolAdminAccountRowStatus.setStatus('current')
eqlStoragePoolAdminAccountQuotaType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1, 2), PoolQuotaType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolAdminAccountQuotaType.setStatus('current')
eqlStoragePoolAdminAccountQuota = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolAdminAccountQuota.setStatus('current')
eqlAdminAccountStoragePoolTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 4), )
if mibBuilder.loadTexts: eqlAdminAccountStoragePoolTable.setStatus('current')
eqlAdminAccountStoragePoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 4, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"), (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"))
if mibBuilder.loadTexts: eqlAdminAccountStoragePoolEntry.setStatus('current')
eqlAdminAccountStoragePoolAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read-only", 1), ("read-write", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAdminAccountStoragePoolAccess.setStatus('current')
eqlStoragePoolOpsTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 5), )
if mibBuilder.loadTexts: eqlStoragePoolOpsTable.setStatus('current')
eqlStoragePoolOpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"), (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolOpsIndex"))
if mibBuilder.loadTexts: eqlStoragePoolOpsEntry.setStatus('current')
eqlStoragePoolOpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlStoragePoolOpsIndex.setStatus('current')
eqlStoragePoolOpsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStoragePoolOpsRowStatus.setStatus('current')
eqlStoragePoolOpsOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("delete", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolOpsOperation.setStatus('current')
eqlStoragePoolOpsStoragePoolDestinationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 4), Unsigned32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlStoragePoolOpsStoragePoolDestinationIndex.setStatus('current')
eqlStoragePoolAdminAccountStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6), )
if mibBuilder.loadTexts: eqlStoragePoolAdminAccountStatsTable.setStatus('current')
eqlStoragePoolAdminAccountStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1), )
eqlStoragePoolAdminAccountEntry.registerAugmentions(("EQLSTORAGEPOOL-MIB", "eqlStoragePoolAdminAccountStatsEntry"))
eqlStoragePoolAdminAccountStatsEntry.setIndexNames(*eqlStoragePoolAdminAccountEntry.getIndexNames())
if mibBuilder.loadTexts: eqlStoragePoolAdminAccountStatsEntry.setStatus('current')
eqlStorageAdminAccountPoolStatsQuota = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 1), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsQuota.setStatus('current')
eqlStorageAdminAccountPoolStatsQuotaUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 2), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsQuotaUsed.setStatus('current')
eqlStorageAdminAccountPoolStatsQuotaAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 3), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsQuotaAvailable.setStatus('current')
eqlStorageAdminAccountPoolStatsSnapshotReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 4), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSnapshotReserved.setStatus('current')
eqlStorageAdminAccountPoolStatsSnapshotUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 5), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSnapshotUsed.setStatus('current')
eqlStorageAdminAccountPoolStatsSnapshotSubscribed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 6), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSnapshotSubscribed.setStatus('current')
eqlStorageAdminAccountPoolStatsSnapshotNumInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSnapshotNumInUse.setStatus('current')
eqlStorageAdminAccountPoolStatsSnapshotNumOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSnapshotNumOnline.setStatus('current')
eqlStorageAdminAccountPoolStatsSnapshotCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSnapshotCount.setStatus('current')
eqlStorageAdminAccountPoolStatsVolumeNumInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsVolumeNumInUse.setStatus('current')
eqlStorageAdminAccountPoolStatsVolumeNumOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsVolumeNumOnline.setStatus('current')
eqlStorageAdminAccountPoolStatsVolumeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsVolumeCount.setStatus('current')
eqlStorageAdminAccountPoolStatsVolumeSubscribed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 13), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsVolumeSubscribed.setStatus('current')
eqlStorageAdminAccountPoolStatsVolumeQuotaUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 14), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsVolumeQuotaUsage.setStatus('current')
eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 15), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated.setStatus('current')
eqlStorageAdminAccountPoolStatsFailbackSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 16), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsFailbackSpace.setStatus('current')
eqlStorageAdminAccountPoolStatsFailbackSubscribed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 17), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsFailbackSubscribed.setStatus('current')
eqlStorageAdminAccountPoolStatsThinProvFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 18), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsThinProvFreeSpace.setStatus('current')
eqlStorageAdminAccountPoolStatsConnectionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsConnectionCount.setStatus('current')
eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 20), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace.setStatus('current')
eqlStorageAdminAccountPoolStatsSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 21), Unsigned64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageAdminAccountPoolStatsSpaceUsed.setStatus('current')
eqlLdapLoginAccessPoolTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 7), )
if mibBuilder.loadTexts: eqlLdapLoginAccessPoolTable.setStatus('current')
eqlLdapLoginAccessPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLGROUP-MIB", "eqlLdapLoginAccessType"), (0, "EQLGROUP-MIB", "eqlLdapLoginAccessName"), (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"))
if mibBuilder.loadTexts: eqlLdapLoginAccessPoolEntry.setStatus('current')
eqlLdapLoginAccessPoolQuotaType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1, 1), PoolQuotaType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlLdapLoginAccessPoolQuotaType.setStatus('current')
eqlLdapLoginAccessPoolQuota = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlLdapLoginAccessPoolQuota.setStatus('current')
eqlLdapLoginAccessPoolQuotaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlLdapLoginAccessPoolQuotaRowStatus.setStatus('current')
eqlStoragePoolOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 16, 1, 8), )
if mibBuilder.loadTexts: eqlStoragePoolOperStatusTable.setStatus('current')
eqlStoragePoolOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 16, 1, 8, 1), )
eqlStoragePoolEntry.registerAugmentions(("EQLSTORAGEPOOL-MIB", "eqlStoragePoolOperStatusEntry"))
eqlStoragePoolOperStatusEntry.setIndexNames(*eqlStoragePoolEntry.getIndexNames())
if mibBuilder.loadTexts: eqlStoragePoolOperStatusEntry.setStatus('current')
eqlStoragePoolOperStatusCompression = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 16, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("paused", 2), ("no-capable-hardware", 3), ("no-capable-raid", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolOperStatusCompression.setStatus('current')
mibBuilder.exportSymbols("EQLSTORAGEPOOL-MIB", eqlStoragePoolDefaultFlag=eqlStoragePoolDefaultFlag, eqlStoragePoolStatsVolumeNumOnline=eqlStoragePoolStatsVolumeNumOnline, eqlStoragePoolStatsVolumeCount=eqlStoragePoolStatsVolumeCount, eqlLdapLoginAccessPoolQuotaRowStatus=eqlLdapLoginAccessPoolQuotaRowStatus, eqlStoragePoolObjects=eqlStoragePoolObjects, eqlStorageAdminAccountPoolStatsVolumeNumInUse=eqlStorageAdminAccountPoolStatsVolumeNumInUse, eqlStoragePoolStatsMembersInUse=eqlStoragePoolStatsMembersInUse, eqlStorageAdminAccountPoolStatsConnectionCount=eqlStorageAdminAccountPoolStatsConnectionCount, eqlStoragePoolUUID=eqlStoragePoolUUID, eqlStoragePoolStatsAvailableForBorrowing=eqlStoragePoolStatsAvailableForBorrowing, eqlStoragePoolAdminAccountTable=eqlStoragePoolAdminAccountTable, eqlStoragePoolTable=eqlStoragePoolTable, eqlStoragePoolStatsConnectionCount=eqlStoragePoolStatsConnectionCount, eqlStoragePoolSnapTrimThreshold=eqlStoragePoolSnapTrimThreshold, eqlStoragePoolOperStatusTable=eqlStoragePoolOperStatusTable, eqlStoragePoolExecMergeTo=eqlStoragePoolExecMergeTo, eqlStorageAdminAccountPoolStatsQuotaAvailable=eqlStorageAdminAccountPoolStatsQuotaAvailable, eqlStoragePoolStatsFreeSpaceBorrowing=eqlStoragePoolStatsFreeSpaceBorrowing, eqlStoragePoolStatsSnapshotNumOnline=eqlStoragePoolStatsSnapshotNumOnline, eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace=eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace, eqlStoragePoolStatsSnapShotBorrowing=eqlStoragePoolStatsSnapShotBorrowing, eqlLdapLoginAccessPoolTable=eqlLdapLoginAccessPoolTable, eqlStoragePoolAdminAccountStatsEntry=eqlStoragePoolAdminAccountStatsEntry, eqlStoragePoolLastBalance=eqlStoragePoolLastBalance, eqlStoragePoolOpsIndex=eqlStoragePoolOpsIndex, eqlStoragePoolStatsTable=eqlStoragePoolStatsTable, eqlStoragePoolStatsReplicationSpaceUsed=eqlStoragePoolStatsReplicationSpaceUsed, eqlStoragePoolStatsDelegatedSpace=eqlStoragePoolStatsDelegatedSpace, eqlStoragePoolStatsActualFreeSpace=eqlStoragePoolStatsActualFreeSpace, eqlStoragePoolAdminAccountEntry=eqlStoragePoolAdminAccountEntry, eqlStorageAdminAccountPoolStatsSnapshotReserved=eqlStorageAdminAccountPoolStatsSnapshotReserved, eqlStoragePoolStatsVolumeNumInUse=eqlStoragePoolStatsVolumeNumInUse, eqlStoragePoolStatsSnapshotCount=eqlStoragePoolStatsSnapshotCount, eqlStorageAdminAccountPoolStatsSnapshotSubscribed=eqlStorageAdminAccountPoolStatsSnapshotSubscribed, eqlStorageAdminAccountPoolStatsQuotaUsed=eqlStorageAdminAccountPoolStatsQuotaUsed, eqlStoragePoolStatsStorageContainerSnapCount=eqlStoragePoolStatsStorageContainerSnapCount, eqlStoragePoolAdminAccountQuota=eqlStoragePoolAdminAccountQuota, eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated=eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated, eqlLdapLoginAccessPoolQuotaType=eqlLdapLoginAccessPoolQuotaType, eqlStoragePoolStatsVolumeSubscribed=eqlStoragePoolStatsVolumeSubscribed, PoolQuotaType=PoolQuotaType, eqlStoragePoolStatsStorageContainerCount=eqlStoragePoolStatsStorageContainerCount, eqlStoragePoolStatsSpace=eqlStoragePoolStatsSpace, eqlStoragePoolStatsSnapshotNumInUse=eqlStoragePoolStatsSnapshotNumInUse, eqlStorageAdminAccountPoolStatsFailbackSubscribed=eqlStorageAdminAccountPoolStatsFailbackSubscribed, SiteIndexOrZero=SiteIndexOrZero, eqlStoragePoolStatsMemberNumOnline=eqlStoragePoolStatsMemberNumOnline, eqlStoragePoolStatsSnapshotResvBorrowing=eqlStoragePoolStatsSnapshotResvBorrowing, eqlAdminAccountStoragePoolTable=eqlAdminAccountStoragePoolTable, eqlStorageAdminAccountPoolStatsSnapshotNumOnline=eqlStorageAdminAccountPoolStatsSnapshotNumOnline, eqlStoragePoolDefaultCompressionMinSnapAge=eqlStoragePoolDefaultCompressionMinSnapAge, eqlStoragePoolStatsCompressedSpaceUsed=eqlStoragePoolStatsCompressedSpaceUsed, eqlStorageAdminAccountPoolStatsSnapshotNumInUse=eqlStorageAdminAccountPoolStatsSnapshotNumInUse, eqlStoragePoolLeadMemberId=eqlStoragePoolLeadMemberId, eqlStoragePoolOpsStoragePoolDestinationIndex=eqlStoragePoolOpsStoragePoolDestinationIndex, eqlStoragePoolSnapTrimBuffer=eqlStoragePoolSnapTrimBuffer, eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval=eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval, eqlStoragePoolOpsOperation=eqlStoragePoolOpsOperation, eqlStoragePoolRowStatus=eqlStoragePoolRowStatus, eqlStorageAdminAccountPoolStatsThinProvFreeSpace=eqlStorageAdminAccountPoolStatsThinProvFreeSpace, eqlStoragePoolSnapTrimmerHWMLifeTime=eqlStoragePoolSnapTrimmerHWMLifeTime, eqlStorageAdminAccountPoolStatsSnapshotUsed=eqlStorageAdminAccountPoolStatsSnapshotUsed, eqlStorageAdminAccountPoolStatsQuota=eqlStorageAdminAccountPoolStatsQuota, eqlStoragePoolStatsVirtualVolumeNumInUse=eqlStoragePoolStatsVirtualVolumeNumInUse, eqlStoragePoolEntry=eqlStoragePoolEntry, eqlStoragePoolOperStatusEntry=eqlStoragePoolOperStatusEntry, eqlStoragePoolStatsThinProvFreeSpace=eqlStoragePoolStatsThinProvFreeSpace, eqlStoragePoolStatsStorageContainerSpaceReserved=eqlStoragePoolStatsStorageContainerSpaceReserved, eqlStoragePoolOperStatusCompression=eqlStoragePoolOperStatusCompression, PYSNMP_MODULE_ID=eqlStoragePoolModule, eqlStoragePoolShouldEvalMask=eqlStoragePoolShouldEvalMask, eqlStoragePoolSnapMemberTrimThresholdAmount=eqlStoragePoolSnapMemberTrimThresholdAmount, eqlStoragePoolStatsSpaceUsed=eqlStoragePoolStatsSpaceUsed, eqlStoragePoolOpsRowStatus=eqlStoragePoolOpsRowStatus, eqlStoragePoolAdminAccountRowStatus=eqlStoragePoolAdminAccountRowStatus, eqlAdminAccountStoragePoolAccess=eqlAdminAccountStoragePoolAccess, eqlStorageAdminAccountPoolStatsVolumeNumOnline=eqlStorageAdminAccountPoolStatsVolumeNumOnline, eqlStorageAdminAccountPoolStatsVolumeCount=eqlStorageAdminAccountPoolStatsVolumeCount, eqlStoragePoolStatsSnapshotResvFreeSpace=eqlStoragePoolStatsSnapshotResvFreeSpace, eqlStoragePoolDescription=eqlStoragePoolDescription, eqlStoragePoolConformance=eqlStoragePoolConformance, eqlStoragePoolAdminAccountQuotaType=eqlStoragePoolAdminAccountQuotaType, eqlStoragePoolStatsReplicationFreeSpace=eqlStoragePoolStatsReplicationFreeSpace, eqlStoragePoolSnapTrimRecheckTimer=eqlStoragePoolSnapTrimRecheckTimer, eqlStoragePoolStatsReplicationSpace=eqlStoragePoolStatsReplicationSpace, eqlStoragePoolStatsFailbackSpace=eqlStoragePoolStatsFailbackSpace, eqlLdapLoginAccessPoolQuota=eqlLdapLoginAccessPoolQuota, eqlStoragePoolStatsVolumeSpaceAllocated=eqlStoragePoolStatsVolumeSpaceAllocated, eqlStorageAdminAccountPoolStatsVolumeQuotaUsage=eqlStorageAdminAccountPoolStatsVolumeQuotaUsage, SiteIndex=SiteIndex, eqlStoragePoolDefaultCompressionMinSnapDelay=eqlStoragePoolDefaultCompressionMinSnapDelay, eqlStorageAdminAccountPoolStatsFailbackSpace=eqlStorageAdminAccountPoolStatsFailbackSpace, eqlStoragePoolRAIDConfigWaitFlag=eqlStoragePoolRAIDConfigWaitFlag, eqlStoragePoolStatsVirtualVolumeNumOnline=eqlStoragePoolStatsVirtualVolumeNumOnline, eqlLdapLoginAccessPoolEntry=eqlLdapLoginAccessPoolEntry, eqlStoragePoolStatsEntry=eqlStoragePoolStatsEntry, eqlStoragePoolStatsStorageContainerVolumeCount=eqlStoragePoolStatsStorageContainerVolumeCount, eqlStoragePoolStatsTotalSpaceBorrowing=eqlStoragePoolStatsTotalSpaceBorrowing, eqlStoragePoolStatsSnapshotUsed=eqlStoragePoolStatsSnapshotUsed, eqlStoragePoolStatsRecoverableVolBorrowing=eqlStoragePoolStatsRecoverableVolBorrowing, eqlStoragePoolAdminAccountStatsTable=eqlStoragePoolAdminAccountStatsTable, StatusEnabledDefault=StatusEnabledDefault, eqlStoragePoolOpsEntry=eqlStoragePoolOpsEntry, eqlStorageAdminAccountPoolStatsVolumeSubscribed=eqlStorageAdminAccountPoolStatsVolumeSubscribed, eqlAdminAccountStoragePoolEntry=eqlAdminAccountStoragePoolEntry, eqlStoragePoolStatsVirtualSpaceSize=eqlStoragePoolStatsVirtualSpaceSize, eqlStoragePoolNotifications=eqlStoragePoolNotifications, eqlStoragePoolBorrow=eqlStoragePoolBorrow, eqlStoragePoolStatsSnapshotReserved=eqlStoragePoolStatsSnapshotReserved, eqlStoragePoolStatsDelegatedSpaceUsed=eqlStoragePoolStatsDelegatedSpaceUsed, eqlStorageAdminAccountPoolStatsSnapshotCount=eqlStorageAdminAccountPoolStatsSnapshotCount, eqlStoragePoolModule=eqlStoragePoolModule, eqlStoragePoolName=eqlStoragePoolName, Unsigned64=Unsigned64, eqlStoragePoolStatsStorageContainerVolumesOnline=eqlStoragePoolStatsStorageContainerVolumesOnline, eqlStorageAdminAccountPoolStatsSpaceUsed=eqlStorageAdminAccountPoolStatsSpaceUsed, eqlStoragePoolIndex=eqlStoragePoolIndex, eqlStoragePoolStatsFreeSpace=eqlStoragePoolStatsFreeSpace, eqlStoragePoolDefaultCompressionStrategy=eqlStoragePoolDefaultCompressionStrategy, eqlStoragePoolOpsTable=eqlStoragePoolOpsTable, eqlStoragePoolStatsMemberCount=eqlStoragePoolStatsMemberCount)
