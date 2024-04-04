#
# PySNMP MIB module EQLRAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLRAID-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:41 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlDriveGroupIndex, eqlMemberIndex = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlDriveGroupIndex", "eqlMemberIndex")
eqlStoragePoolIndex, = mibBuilder.importSymbols("EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Gauge32, iso, ModuleIdentity, Counter64, enterprises, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, NotificationType, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Gauge32", "iso", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
eqlRAIDModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 10))
eqlRAIDModule.setRevisions(('2002-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqlRAIDModule.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: eqlRAIDModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlRAIDModule.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: eqlRAIDModule.setContactInfo('Contact: Customer Support\n         Postal:  Dell Inc\n                  300 Innovative Way, Suite 301, Nashua, NH 03062\n         Tel:     +1 603-579-9762\n         E-mail:  US-NH-CS-TechnicalSupport@dell.com\n         WEB:     www.equallogic.com')
if mibBuilder.loadTexts: eqlRAIDModule.setDescription('Equallogic Inc. Storage Array raid mib\n\n         Copyright (c) 2002-2009 by Dell, Inc.\n\n         All rights reserved.  This software may not be copied, disclosed,\n         transferred, or used except in accordance with a license granted\n         by Dell, Inc.  This software embodies proprietary information\n         and trade secrets of Dell, Inc.\n        ')
eqlRAIDObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 10, 1))
eqlRAIDNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 10, 2))
eqlRAIDConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 10, 3))
eqlRAIDDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1), )
if mibBuilder.loadTexts: eqlRAIDDeviceTable.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceTable.setDescription('EqualLogic-Dynamic Table representing a list of all of \n                  the RAID devices in a group')
eqlRAIDDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"))
if mibBuilder.loadTexts: eqlRAIDDeviceEntry.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceEntry.setDescription('A sequence of attributes pertaining to a single RAID device in a group')
eqlRAIDDeviceLUNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLUNIndex.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceLUNIndex.setDescription('The LUN number of the RAID device, incremented by one for SNMP compatibility.\n\t\t\t\t\t\t\tValid LUN numbers\tbegin at zero. ')
eqlRAIDDeviceLUN = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLUN.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceLUN.setDescription('The LUN of the drive. In all cases the value of this variable will be equal to \n\t\t\t\t\t\t\teqlRAIDDeviceLUNIndex-1.')
eqlRAIDDeviceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDevice", 1), ("dataLoss", 2), ("nominal", 3), ("degraded", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceOperStatus.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceOperStatus.setDescription('The operational status of the RAID device. Values are as follows:\n\t\t\t\t\t\t\t1 - no device\n\t\t\t\t\t\t\t2 - data loss\n\t\t\t\t\t\t\t3 - nominal\n\t\t\t\t\t\t\t4 - degraded\n\t\t\t\t\t\t\t5 - failed ')
eqlRAIDDeviceUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceUUID.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceUUID.setDescription('a 16 byte identifier for the device that is guranteed to be universally\n\t\t\t\t\t\t\tunique')
eqlRAIDDeviceDriveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceDriveCount.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceDriveCount.setDescription('The number of drives used by the RAID device')
eqlRAIDDeviceLayoutOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noOp", 1), ("expSuspended", 2), ("expInProgress", 3), ("swapSuspended", 4), ("swapInProgress", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLayoutOperStatus.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceLayoutOperStatus.setDescription('The status of the currently executing layout operation on the \n\t\t\t\t\t\t\tdevice (if any)\n\t\t\t\t\t\t\t1 - no operation in progress\n\t\t\t\t\t\t\t2 - exp suspended\n\t\t\t\t\t\t\t3 - exp in progress\n\t\t\t\t\t\t\t4 - swap suspended\n\t\t\t\t\t\t\t5 - swap in progress')
eqlRAIDDeviceLayoutSectPerSU = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLayoutSectPerSU.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceLayoutSectPerSU.setDescription('The number of sectors per stripe unit in this layout')
eqlRAIDDeviceLUNCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLUNCapacity.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceLUNCapacity.setDescription('The current LUN capacity of this layout in sectors, including \n\t\t\t\t\t\t\tinternal layout operations')
eqlRAIDDeviceLostBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLostBlocks.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceLostBlocks.setDescription('The count of bad soft sectors')
eqlRAIDDeviceOutIOOps = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceOutIOOps.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceOutIOOps.setDescription('Th number of I/O operations currently in progress on the device')
eqlRAIDDeviceCacheWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCacheWrites.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceCacheWrites.setDescription('The count of the number of cache write operations in progress on the device')
eqlRAIDDeviceCacheReads = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCacheReads.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceCacheReads.setDescription('The count of the number of cache read operations in progress on the device')
eqlRAIDDeviceCompCacheWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCompCacheWrites.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceCompCacheWrites.setDescription('The number of completed cache write operations since the system was started')
eqlRAIDDeviceCompCacheReads = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCompCacheReads.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceCompCacheReads.setDescription('The number of completed cache read operations since the system was started')
eqlRAIDDeviceSectWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceSectWritten.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceSectWritten.setDescription('The number of sectors written since the system was started')
eqlRAIDDeviceSectRead = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceSectRead.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceSectRead.setDescription('The number of sectors read since the system was started')
eqlRAIDDeviceStoragePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 17), Unsigned32())
if mibBuilder.loadTexts: eqlRAIDDeviceStoragePoolIndex.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceStoragePoolIndex.setDescription('This field specifies a unique index for identifying a storage pool.')
eqlRAIDDeviceDriveGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 18), Unsigned32())
if mibBuilder.loadTexts: eqlRAIDDeviceDriveGroupIndex.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceDriveGroupIndex.setDescription('This field specifies a unique index for identifying a drive group.')
eqlRAIDLayoutTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2), )
if mibBuilder.loadTexts: eqlRAIDLayoutTable.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutTable.setDescription('EqualLogic-Dynamic Table listing the layouts in existence in a RAID device. \n                  Typically, there will only be a single entry for each device. When layout \n\t\t\t\t\t\toperations are in progress, there will be two layouts. The layout \n\t\t\t\t\t\trepresents a set of drives and a parity configuration for the drives.')
eqlRAIDLayoutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"), (0, "EQLRAID-MIB", "eqlRAIDLayoutIndex"))
if mibBuilder.loadTexts: eqlRAIDLayoutEntry.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutEntry.setDescription('a sequence of attributes belonging to a single layout group')
eqlRAIDLayoutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("first", 1), ("second", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutIndex.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutIndex.setDescription('An identifier for this instance of a layout. The layouts are 1-indexed\n\t\t\t\t\t\t\twhere the primary is index 1, and the secindary (if any) is index 2')
eqlRAIDLayoutOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDevice", 1), ("noLayout", 2), ("failed", 3), ("nominal", 4), ("degraded", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutOperStatus.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutOperStatus.setDescription('Operational status of the layout as follows:\n\t\t\t\t\t\t\t1 - no device\n\t\t\t\t\t\t\t2 - no layout\n\t\t\t\t\t\t\t3 - failed\n\t\t\t\t\t\t\t4 - nominal\n\t\t\t\t\t\t\t5 - degraded')
eqlRAIDLayoutNumParityGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutNumParityGrp.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutNumParityGrp.setDescription('The number of parity groups in this layout')
eqlRAIDLayoutParityType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 10, 5, 50))).clone(namedValues=NamedValues(("stripe", 0), ("raid1", 1), ("raid10", 10), ("raid5", 5), ("raid50", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutParityType.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutParityType.setDescription('The parity type of this layout:\n\t\t\t\t\t\t\t0 - stripe\n\t\t\t\t\t\t\t1 - raid1 mirror\n\t\t\t\t\t\t\t10- raid10 multi raid1 parity groups\n\t\t\t\t\t\t\t5 - raid5\n\t\t\t\t\t\t\t50- multi raid5 parity groups')
eqlRAIDLayoutBeginLBA = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutBeginLBA.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutBeginLBA.setDescription('The beginning RAID LBA of this layout')
eqlRAIDLayoutLength = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutLength.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDLayoutLength.setDescription('Length in sectors of this layout. This value can be used\n\t\t\t\t\t\t\t to determine the progress of layout operations.')
eqlRAIDParityGroupTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3), )
if mibBuilder.loadTexts: eqlRAIDParityGroupTable.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDParityGroupTable.setDescription('EqualLogic-Dynamic Table. Each layout on a RAID device has one or more \n                  parity groups. The groups are indexed starting at 1. \n                  Each group represents a set of drives consisting of one stripe and one \n                  parity drive with one or more data drives.\n\t\n\t\t\t\t\t\tEach groups is reconstructed and verified as a whole and can be done so\n\t\t\t\t\t\tindependently of other partity groups in the set.\n\n\t\t\t\t\t\tRAID 0, 1, and 5 have only one parity grouping per layout.\n\t\t\t\t\t\tRAID 10 and 50 have multiple parity groups per layout. ')
eqlRAIDParityGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"), (0, "EQLRAID-MIB", "eqlRAIDLayoutIndex"), (0, "EQLRAID-MIB", "eqlParityGrpIndex"))
if mibBuilder.loadTexts: eqlRAIDParityGroupEntry.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDParityGroupEntry.setDescription('a sequence of attributes belonging to a single parity group')
eqlParityGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpIndex.setStatus('current')
if mibBuilder.loadTexts: eqlParityGrpIndex.setDescription('A numeric index describing the instance of this parity group')
eqlParityGrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noDevice", 1), ("noLayout", 2), ("noGroup", 3), ("degraded", 4), ("failed", 5), ("nominal", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpOperStatus.setStatus('current')
if mibBuilder.loadTexts: eqlParityGrpOperStatus.setDescription('The operational status of the parity group:\n\t\t\t\t\t\t\t1 - no device\n\t\t\t\t\t\t\t2 - no layout\n\t\t\t\t\t\t\t3 - no group\n\t\t\t\t\t\t\t4 - degraded\n\t\t\t\t\t\t\t5 - failed\n\t\t\t\t\t\t\t6 - nominal\n\t\t\t\t\t\t\t')
eqlParityGrpDriveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpDriveCount.setStatus('current')
if mibBuilder.loadTexts: eqlParityGrpDriveCount.setDescription('The number of drives in the parity group')
eqlParityGrpOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("verify", 1), ("reconstruct", 2), ("noOp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpOperation.setStatus('current')
if mibBuilder.loadTexts: eqlParityGrpOperation.setDescription('The current parity group operation underway on this group (if any):\n\t\t\t\t\t\t\t1 - verify\n\t\t\t\t\t\t\t2 - reconstruct\n\t\t\t\t\t\t\t3 - no operation')
eqlParityGrpReconstChkpt = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpReconstChkpt.setStatus('current')
if mibBuilder.loadTexts: eqlParityGrpReconstChkpt.setDescription('Reconstruction checkpoint: The number of sectors that have been completed during \n\t\t\t\t\t\t\tthe reconstruction operation. This can be compared to the corresonding value for\n\t\t\t\t\t\t\teqlRAIDLayoutLength and eqlRAIDLayoutBeginLBA to setermine the progress of the \n\t\t\t\t\t\t\toperation.')
eqlParityGrpVerifyChkpt = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpVerifyChkpt.setStatus('current')
if mibBuilder.loadTexts: eqlParityGrpVerifyChkpt.setDescription('Verify checkpoint: The number of sectors that have been completed during \n\t\t\t\t\t\t\tthe verify operation. This can be compared to the corresonding value for\n\t\t\t\t\t\t\teqlRAIDLayoutLength and eqlRAIDLayoutBeginLBA to setermine the progress of the \n\t\t\t\t\t\t\toperation.')
eqlRAIDDriveTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4), )
if mibBuilder.loadTexts: eqlRAIDDriveTable.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDriveTable.setDescription('EqualLogic-Dynamic Table. The RAID Drive Table contains an entry for each drive\n                  in the system. The mapping between the enties in this table and the entries \n                  in the eqlDisk table\tis one to one. This table is intended to store the RAID \n                  attributes of each drive.')
eqlRAIDDriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDriveDriveLUNIndex"))
if mibBuilder.loadTexts: eqlRAIDDriveEntry.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDriveEntry.setDescription('a sequence of RAID attributes for a single drive in the group')
eqlRAIDDriveDriveLUNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveDriveLUNIndex.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDriveDriveLUNIndex.setDescription('The LUN index of the drive. In all cases the value of the index will be \n                  one greater than the value of the LUN ID of this drive. Thus, where LUNs \n                  will start at the number 0 and increment, LUN index entries will start \n                  at the number one and increment. ')
eqlRAIDDriveDriveLUN = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveDriveLUN.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDriveDriveLUN.setDescription('The LUN of the drive. In all cases the value of this variable will be equal to \n\t\t\t\t\t\teqlRAIDDriveLUNIndex-1.')
eqlRAIDDriveOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noDrive", 1), ("active", 2), ("failed", 3), ("tooSmall", 4), ("reconstruct", 5), ("swap", 6), ("spare", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveOperStatus.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDriveOperStatus.setDescription('Operational status of the drive:\n\t\t\t\t\t\t1 - no drive\n\t\t\t\t\t\t2 - active\n\t\t\t\t\t\t3 - failed\n\t\t\t\t\t\t4 - too small\n\t\t\t\t\t\t5 - reconstructing\n\t\t\t\t\t\t6 - swapping\n\t\t\t\t\t\t7 - spare')
eqlRAIDDriveUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveUUID.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDriveUUID.setDescription('A 16 byte univerally unique identifier for the drive. This should be unique \n\t\t\t\t\t\tthroughout the universe of drives in EqualLogic arrays.')
eqlRAIDDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDiskIndex.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDiskIndex.setDescription('The index value that uniquely identifies the disk.\n                     It is equal to the disk slot number plus one. The value of this will correspond \n\t\t\t\t\t\t\tto a value of eqlDiskIndex in the eqlDiskTable.')
eqlRAIDDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: eqlRAIDDeviceIndex.setDescription('The index of the device this disk belongs to.\n                     It is equal to a value of eqlRAIDDeviceLUNIndex in the eqlRAIDDeviceTable.')
eqlStoragePoolRAIDLUNTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 5), )
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNTable.setStatus('current')
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNTable.setDescription('EqualLogic-Dynamic Storage Pool RAID LUN Table')
eqlStoragePoolRAIDLUNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 5, 1), ).setIndexNames((0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLMEMBER-MIB", "eqlDriveGroupIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"))
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNEntry.setStatus('current')
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNEntry.setDescription('An entry (row) containing a RAID LUN mapping to a storage pool.')
eqlStoragePoolRAIDLUNfoo = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNfoo.setStatus('current')
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNfoo.setDescription('Bogus')
mibBuilder.exportSymbols("EQLRAID-MIB", eqlRAIDDeviceDriveGroupIndex=eqlRAIDDeviceDriveGroupIndex, eqlRAIDParityGroupEntry=eqlRAIDParityGroupEntry, eqlRAIDDeviceIndex=eqlRAIDDeviceIndex, eqlRAIDDeviceLUN=eqlRAIDDeviceLUN, eqlRAIDDeviceLayoutOperStatus=eqlRAIDDeviceLayoutOperStatus, eqlRAIDLayoutIndex=eqlRAIDLayoutIndex, eqlRAIDLayoutLength=eqlRAIDLayoutLength, eqlRAIDDriveDriveLUNIndex=eqlRAIDDriveDriveLUNIndex, eqlRAIDObjects=eqlRAIDObjects, eqlRAIDDeviceTable=eqlRAIDDeviceTable, eqlRAIDDeviceCacheWrites=eqlRAIDDeviceCacheWrites, eqlParityGrpVerifyChkpt=eqlParityGrpVerifyChkpt, eqlRAIDDriveDriveLUN=eqlRAIDDriveDriveLUN, eqlParityGrpDriveCount=eqlParityGrpDriveCount, PYSNMP_MODULE_ID=eqlRAIDModule, eqlRAIDDeviceDriveCount=eqlRAIDDeviceDriveCount, eqlRAIDLayoutOperStatus=eqlRAIDLayoutOperStatus, eqlRAIDDeviceLayoutSectPerSU=eqlRAIDDeviceLayoutSectPerSU, eqlRAIDDeviceOperStatus=eqlRAIDDeviceOperStatus, eqlRAIDDeviceCompCacheReads=eqlRAIDDeviceCompCacheReads, eqlRAIDLayoutBeginLBA=eqlRAIDLayoutBeginLBA, eqlRAIDDriveOperStatus=eqlRAIDDriveOperStatus, eqlParityGrpReconstChkpt=eqlParityGrpReconstChkpt, eqlStoragePoolRAIDLUNEntry=eqlStoragePoolRAIDLUNEntry, eqlParityGrpOperStatus=eqlParityGrpOperStatus, eqlRAIDLayoutTable=eqlRAIDLayoutTable, eqlRAIDDeviceCompCacheWrites=eqlRAIDDeviceCompCacheWrites, eqlRAIDDeviceLUNCapacity=eqlRAIDDeviceLUNCapacity, eqlRAIDDeviceStoragePoolIndex=eqlRAIDDeviceStoragePoolIndex, eqlRAIDDriveUUID=eqlRAIDDriveUUID, eqlStoragePoolRAIDLUNfoo=eqlStoragePoolRAIDLUNfoo, eqlRAIDDeviceUUID=eqlRAIDDeviceUUID, eqlParityGrpIndex=eqlParityGrpIndex, eqlRAIDParityGroupTable=eqlRAIDParityGroupTable, eqlRAIDNotifications=eqlRAIDNotifications, eqlParityGrpOperation=eqlParityGrpOperation, eqlRAIDLayoutEntry=eqlRAIDLayoutEntry, eqlRAIDDeviceOutIOOps=eqlRAIDDeviceOutIOOps, eqlRAIDDriveEntry=eqlRAIDDriveEntry, eqlRAIDDiskIndex=eqlRAIDDiskIndex, eqlRAIDDeviceSectWritten=eqlRAIDDeviceSectWritten, eqlStoragePoolRAIDLUNTable=eqlStoragePoolRAIDLUNTable, eqlRAIDConformance=eqlRAIDConformance, eqlRAIDLayoutNumParityGrp=eqlRAIDLayoutNumParityGrp, eqlRAIDModule=eqlRAIDModule, eqlRAIDDeviceSectRead=eqlRAIDDeviceSectRead, eqlRAIDDeviceCacheReads=eqlRAIDDeviceCacheReads, eqlRAIDDriveTable=eqlRAIDDriveTable, eqlRAIDDeviceLostBlocks=eqlRAIDDeviceLostBlocks, eqlRAIDLayoutParityType=eqlRAIDLayoutParityType, eqlRAIDDeviceLUNIndex=eqlRAIDDeviceLUNIndex, eqlRAIDDeviceEntry=eqlRAIDDeviceEntry)
