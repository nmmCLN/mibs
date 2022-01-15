#
# PySNMP MIB module VMWARE-VMINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VMINFO-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:36:30 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, TimeTicks, Gauge32, ObjectIdentity, Counter64, Unsigned32, IpAddress, iso, ModuleIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64", "Unsigned32", "IpAddress", "iso", "ModuleIdentity", "Counter32", "NotificationType")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
vmwESXNotifications, = mibBuilder.importSymbols("VMWARE-ENV-MIB", "vmwESXNotifications")
vmwTraps, vmwVirtMachines = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwTraps", "vmwVirtMachines")
VmwConnectedState, = mibBuilder.importSymbols("VMWARE-TC-MIB", "VmwConnectedState")
vmwVmInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 2, 10))
vmwVmInfoMIB.setRevisions(('2011-09-17 00:00', '2010-06-22 00:00', '2008-10-23 00:00', '2007-12-27 00:00',))
if mibBuilder.loadTexts: vmwVmInfoMIB.setLastUpdated('201109170000Z')
if mibBuilder.loadTexts: vmwVmInfoMIB.setOrganization('VMware, Inc')
vmwVmTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 1), )
if mibBuilder.loadTexts: vmwVmTable.setStatus('current')
vmwVmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwVmIdx"))
if mibBuilder.loadTexts: vmwVmEntry.setStatus('current')
vmwVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmIdx.setStatus('current')
vmwVmDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmDisplayName.setStatus('current')
vmwVmConfigFile = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmConfigFile.setStatus('current')
vmwVmGuestOS = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmGuestOS.setStatus('current')
vmwVmMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 5), Integer32()).setUnits('megabytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmMemSize.setStatus('current')
vmwVmState = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmState.setStatus('current')
vmwVmVMID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmVMID.setStatus('obsolete')
vmwVmGuestState = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmGuestState.setStatus('current')
vmwVmCpus = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmCpus.setStatus('current')
vmwVmUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(36, 72))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmUUID.setStatus('current')
vmwVmHbaTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 2), )
if mibBuilder.loadTexts: vmwVmHbaTable.setStatus('current')
vmwVmHbaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwHbaVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwVmHbaIdx"))
if mibBuilder.loadTexts: vmwVmHbaEntry.setStatus('current')
vmwHbaVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwHbaVmIdx.setStatus('current')
vmwVmHbaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmHbaIdx.setStatus('current')
vmwHbaNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaNum.setStatus('current')
vmwHbaVirtDev = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaVirtDev.setStatus('current')
vmwHbaTgtTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 3), )
if mibBuilder.loadTexts: vmwHbaTgtTable.setStatus('current')
vmwHbaTgtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwHbaTgtVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwHbaTgtIdx"))
if mibBuilder.loadTexts: vmwHbaTgtEntry.setStatus('current')
vmwHbaTgtVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwHbaTgtVmIdx.setStatus('current')
vmwHbaTgtIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwHbaTgtIdx.setStatus('current')
vmwHbaTgtNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaTgtNum.setStatus('current')
vmwVmNetTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 4), )
if mibBuilder.loadTexts: vmwVmNetTable.setStatus('current')
vmwVmNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwVmNetVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwVmNetIdx"))
if mibBuilder.loadTexts: vmwVmNetEntry.setStatus('current')
vmwVmNetVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmNetVmIdx.setStatus('current')
vmwVmNetIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmNetIdx.setStatus('current')
vmwVmNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetNum.setStatus('current')
vmwVmNetName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetName.setStatus('current')
vmwVmNetConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetConnType.setStatus('obsolete')
vmwVmNetConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 6), VmwConnectedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetConnected.setStatus('current')
vmwVmMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmMAC.setStatus('current')
vmwFloppyTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 5), )
if mibBuilder.loadTexts: vmwFloppyTable.setStatus('current')
vmwFloppyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwFdVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwFdIdx"))
if mibBuilder.loadTexts: vmwFloppyEntry.setStatus('current')
vmwFdVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwFdVmIdx.setStatus('current')
vmwFdIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwFdIdx.setStatus('current')
vmwFdName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwFdName.setStatus('current')
vmwFdConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 4), VmwConnectedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwFdConnected.setStatus('current')
vmwCdromTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 6), )
if mibBuilder.loadTexts: vmwCdromTable.setStatus('current')
vmwCdromEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwCdVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwCdromIdx"))
if mibBuilder.loadTexts: vmwCdromEntry.setStatus('current')
vmwCdVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwCdVmIdx.setStatus('current')
vmwCdromIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwCdromIdx.setStatus('current')
vmwCdromName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwCdromName.setStatus('current')
vmwCdromConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 4), VmwConnectedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwCdromConnected.setStatus('current')
vmwVmID = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 101), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVmID.setStatus('current')
vmwVmConfigFilePath = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 102), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVmConfigFilePath.setStatus('current')
vmwVmPoweredOn = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 1)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmPoweredOn.setStatus('current')
vmwVmPoweredOff = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 2)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmPoweredOff.setStatus('current')
vmwVmHBLost = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 3)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmHBLost.setStatus('current')
vmwVmHBDetected = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 4)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmHBDetected.setStatus('current')
vmwVmSuspended = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 5)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmSuspended.setStatus('current')
vmwVmInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2))
vmwVmInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 1))
vmwVmInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2))
vmwResMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 1, 2)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmInfoGroup"), ("VMWARE-VMINFO-MIB", "vmwVmInfoNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwResMIBBasicCompliance = vmwResMIBBasicCompliance.setStatus('current')
vmwVmInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 1)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmDisplayName"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFile"), ("VMWARE-VMINFO-MIB", "vmwVmGuestOS"), ("VMWARE-VMINFO-MIB", "vmwVmMemSize"), ("VMWARE-VMINFO-MIB", "vmwVmState"), ("VMWARE-VMINFO-MIB", "vmwVmGuestState"), ("VMWARE-VMINFO-MIB", "vmwHbaNum"), ("VMWARE-VMINFO-MIB", "vmwHbaVirtDev"), ("VMWARE-VMINFO-MIB", "vmwHbaTgtNum"), ("VMWARE-VMINFO-MIB", "vmwVmNetNum"), ("VMWARE-VMINFO-MIB", "vmwVmNetName"), ("VMWARE-VMINFO-MIB", "vmwVmNetConnected"), ("VMWARE-VMINFO-MIB", "vmwVmMAC"), ("VMWARE-VMINFO-MIB", "vmwFdName"), ("VMWARE-VMINFO-MIB", "vmwFdConnected"), ("VMWARE-VMINFO-MIB", "vmwCdromName"), ("VMWARE-VMINFO-MIB", "vmwCdromConnected"), ("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmCpus"), ("VMWARE-VMINFO-MIB", "vmwVmUUID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVmInfoGroup = vmwVmInfoGroup.setStatus('current')
vmwVmInfoNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 2)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmPoweredOn"), ("VMWARE-VMINFO-MIB", "vmwVmPoweredOff"), ("VMWARE-VMINFO-MIB", "vmwVmHBLost"), ("VMWARE-VMINFO-MIB", "vmwVmHBDetected"), ("VMWARE-VMINFO-MIB", "vmwVmSuspended"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVmInfoNotificationGroup = vmwVmInfoNotificationGroup.setStatus('current')
vmwVmObsoleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 3)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmVMID"), ("VMWARE-VMINFO-MIB", "vmwVmNetConnType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVmObsoleteGroup = vmwVmObsoleteGroup.setStatus('obsolete')
mibBuilder.exportSymbols("VMWARE-VMINFO-MIB", vmwVmNetConnType=vmwVmNetConnType, vmwVmCpus=vmwVmCpus, vmwVmInfoGroup=vmwVmInfoGroup, vmwVmInfoMIBCompliances=vmwVmInfoMIBCompliances, vmwCdromIdx=vmwCdromIdx, vmwCdromEntry=vmwCdromEntry, vmwCdVmIdx=vmwCdVmIdx, vmwFdName=vmwFdName, vmwHbaTgtTable=vmwHbaTgtTable, vmwVmID=vmwVmID, vmwHbaTgtEntry=vmwHbaTgtEntry, vmwVmTable=vmwVmTable, vmwHbaNum=vmwHbaNum, vmwHbaTgtVmIdx=vmwHbaTgtVmIdx, vmwFdVmIdx=vmwFdVmIdx, vmwHbaTgtNum=vmwHbaTgtNum, vmwVmMAC=vmwVmMAC, vmwVmInfoMIB=vmwVmInfoMIB, vmwVmIdx=vmwVmIdx, vmwVmInfoMIBConformance=vmwVmInfoMIBConformance, vmwVmUUID=vmwVmUUID, vmwFloppyEntry=vmwFloppyEntry, vmwVmNetTable=vmwVmNetTable, vmwFdIdx=vmwFdIdx, vmwVmPoweredOff=vmwVmPoweredOff, vmwVmMemSize=vmwVmMemSize, vmwResMIBBasicCompliance=vmwResMIBBasicCompliance, vmwVmNetNum=vmwVmNetNum, vmwVmInfoNotificationGroup=vmwVmInfoNotificationGroup, vmwVmPoweredOn=vmwVmPoweredOn, vmwVmNetEntry=vmwVmNetEntry, vmwFdConnected=vmwFdConnected, vmwVmHbaEntry=vmwVmHbaEntry, vmwVmNetConnected=vmwVmNetConnected, vmwVmSuspended=vmwVmSuspended, vmwVmGuestOS=vmwVmGuestOS, vmwVmEntry=vmwVmEntry, vmwVmGuestState=vmwVmGuestState, vmwVmHbaTable=vmwVmHbaTable, vmwHbaVirtDev=vmwHbaVirtDev, vmwVmHBLost=vmwVmHBLost, vmwVmHBDetected=vmwVmHBDetected, vmwVmConfigFile=vmwVmConfigFile, vmwVmState=vmwVmState, vmwVmNetIdx=vmwVmNetIdx, vmwHbaVmIdx=vmwHbaVmIdx, vmwVmNetName=vmwVmNetName, vmwHbaTgtIdx=vmwHbaTgtIdx, vmwVmConfigFilePath=vmwVmConfigFilePath, vmwFloppyTable=vmwFloppyTable, vmwVmDisplayName=vmwVmDisplayName, vmwVmVMID=vmwVmVMID, vmwVmObsoleteGroup=vmwVmObsoleteGroup, PYSNMP_MODULE_ID=vmwVmInfoMIB, vmwCdromConnected=vmwCdromConnected, vmwVmHbaIdx=vmwVmHbaIdx, vmwVmNetVmIdx=vmwVmNetVmIdx, vmwCdromName=vmwCdromName, vmwVmInfoMIBGroups=vmwVmInfoMIBGroups, vmwCdromTable=vmwCdromTable)
