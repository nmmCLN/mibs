#
# PySNMP MIB module VMWARE-OBSOLETE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-OBSOLETE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:36:32 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, ModuleIdentity, iso, ObjectIdentity, Bits, Counter32, NotificationType, Unsigned32, TimeTicks, IpAddress, MibIdentifier, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "Bits", "Counter32", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwESX, = mibBuilder.importSymbols("VMWARE-PRODUCTS-MIB", "vmwESX")
vmwCPU, vmwMemory = mibBuilder.importSymbols("VMWARE-RESOURCES-MIB", "vmwCPU", "vmwMemory")
vmwNotifications, vmwResources, vmwTraps, vmwObsolete = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwNotifications", "vmwResources", "vmwTraps", "vmwObsolete")
vmwVmID, vmwVmConfigFilePath = mibBuilder.importSymbols("VMWARE-VMINFO-MIB", "vmwVmID", "vmwVmConfigFilePath")
vmwObsoleteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 800, 1))
vmwObsoleteMIB.setRevisions(('2008-10-15 11:59',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwObsoleteMIB.setRevisionsDescriptions(('This is the first version of this mib module. Objects from VMWARE-RESOURCES-MIB, \n     VMWARE-TRAPS-MIB moved here.',))
if mibBuilder.loadTexts: vmwObsoleteMIB.setLastUpdated('200810151159Z')
if mibBuilder.loadTexts: vmwObsoleteMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwObsoleteMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwObsoleteMIB.setDescription('This MIB module contains all previously published managed objects that have been made\n      obsolete. The mib preserves OID mappings such that backward compatiblity is maintained.')
vmkLoaded = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmkLoaded.setStatus('obsolete')
if mibBuilder.loadTexts: vmkLoaded.setDescription('Has the vmkernel been loaded? (yes/no)')
vmwCpuTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 3, 1, 2), )
if mibBuilder.loadTexts: vmwCpuTable.setStatus('obsolete')
if mibBuilder.loadTexts: vmwCpuTable.setDescription('CPU Usage table by virtual machine.')
vmwCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1), ).setIndexNames((0, "VMWARE-OBSOLETE-MIB", "vmwCpuVMID"))
if mibBuilder.loadTexts: vmwCpuEntry.setStatus('obsolete')
if mibBuilder.loadTexts: vmwCpuEntry.setDescription('A record for CPU usage by a single virtual machine.')
vmwCpuVMID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)))
if mibBuilder.loadTexts: vmwCpuVMID.setStatus('current')
if mibBuilder.loadTexts: vmwCpuVMID.setDescription('ID allocated to running vm by the vmkernel.')
vmwCpuShares = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 2), Gauge32()).setUnits('unknown').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwCpuShares.setStatus('current')
if mibBuilder.loadTexts: vmwCpuShares.setDescription('Share of CPU allocated to vm by vmkernel.')
vmwCpuUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 3), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwCpuUtil.setStatus('current')
if mibBuilder.loadTexts: vmwCpuUtil.setDescription('Time the virtual machine has been running on the CPU (seconds).')
vmwMemTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 3, 2, 4), )
if mibBuilder.loadTexts: vmwMemTable.setStatus('obsolete')
if mibBuilder.loadTexts: vmwMemTable.setDescription('Table of memory usage by virtual machine.')
vmwMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1), ).setIndexNames((0, "VMWARE-OBSOLETE-MIB", "vmwMemVMID"))
if mibBuilder.loadTexts: vmwMemEntry.setStatus('obsolete')
if mibBuilder.loadTexts: vmwMemEntry.setDescription('A record for memory usage by a single virtual machine.')
vmwMemVMID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)))
if mibBuilder.loadTexts: vmwMemVMID.setStatus('obsolete')
if mibBuilder.loadTexts: vmwMemVMID.setDescription('ID allocated to running vm by the vmkernel.')
vmwMemShares = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 2), Gauge32()).setUnits('unknown').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwMemShares.setStatus('obsolete')
if mibBuilder.loadTexts: vmwMemShares.setDescription('Shares of memory allocated to vm by vmkernel.')
vmwMemConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 3), Gauge32()).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwMemConfigured.setStatus('obsolete')
if mibBuilder.loadTexts: vmwMemConfigured.setDescription('Amount of memory the vm was configured with. (KB)')
vmwMemUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 4), Gauge32()).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwMemUtil.setStatus('obsolete')
if mibBuilder.loadTexts: vmwMemUtil.setDescription('Amount of memory utilized by the vm. (KB; instantaneous)')
vmwHBATable = MibTable((1, 3, 6, 1, 4, 1, 6876, 3, 3), )
if mibBuilder.loadTexts: vmwHBATable.setStatus('obsolete')
if mibBuilder.loadTexts: vmwHBATable.setDescription('Disk adapter and target information table.')
vmwHBAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1), ).setIndexNames((0, "VMWARE-OBSOLETE-MIB", "vmwHbaIdx"))
if mibBuilder.loadTexts: vmwHBAEntry.setStatus('obsolete')
if mibBuilder.loadTexts: vmwHBAEntry.setDescription('A record for a single hba on the machine.')
vmwHbaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)))
if mibBuilder.loadTexts: vmwHbaIdx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwHbaIdx.setDescription('Index for HBA table @todo fix this!.')
vmwHbaName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaName.setStatus('obsolete')
if mibBuilder.loadTexts: vmwHbaName.setDescription('String describing the disk. Format: <devname#>:<tgt>:<lun> ')
vmwHbaVMID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaVMID.setStatus('obsolete')
if mibBuilder.loadTexts: vmwHbaVMID.setDescription('ID assigned to running vm by the vmkernel.')
vmwDiskShares = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwDiskShares.setStatus('obsolete')
if mibBuilder.loadTexts: vmwDiskShares.setDescription('Share of disk bandwidth allocated to this vm.')
vmwNumReads = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNumReads.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNumReads.setDescription('Number of reads to this disk since disk module was loaded.')
vmwKbRead = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwKbRead.setStatus('obsolete')
if mibBuilder.loadTexts: vmwKbRead.setDescription('Kilobytes read from this disk since disk module was loaded.')
vmwNumWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNumWrites.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNumWrites.setDescription('Number of writes to this disk since disk module was loaded.')
vmwKbWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwKbWritten.setStatus('obsolete')
if mibBuilder.loadTexts: vmwKbWritten.setDescription('Kilobytes written to this disk since disk module was loaded.')
vmwNetTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 3, 4), )
if mibBuilder.loadTexts: vmwNetTable.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetTable.setDescription('Network adapter statistics.')
vmwNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1), ).setIndexNames((0, "VMWARE-OBSOLETE-MIB", "vmwNetIdx"))
if mibBuilder.loadTexts: vmwNetEntry.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetEntry.setDescription('A record for a single nic on the machine.')
vmwNetIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: vmwNetIdx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetIdx.setDescription('Index for net table.')
vmwNetName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetName.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetName.setDescription('String describing the network adapter. Format: vmnic*')
vmwNetVMID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetVMID.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetVMID.setDescription('ID assigned to running vm by the vmkernel.')
vmwNetIfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetIfAddr.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetIfAddr.setDescription("MAC address of vm's virtual NIC.")
vmwNetShares = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetShares.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetShares.setDescription('Share of net bandwidth allocated to this vm.')
vmwNetPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetPktsTx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetPktsTx.setDescription('Number of pkts transmitted on this NIC since network module was\n        loaded. Deprecated in favour of pktsHCTx.')
vmwNetKbTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetKbTx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetKbTx.setDescription('Kilobytes sent from this NIC since network module was loaded.\n        Deprecated in favour of kbHCTx.')
vmwNetPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetPktsRx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetPktsRx.setDescription('Number of pkts received on this NIC since network module was loaded.\n        Deprecated in favour of pktsHCRx.')
vmwNetKbRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetKbRx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetKbRx.setDescription('Kilobytes received on this NIC since network module was loaded.\n        Deprecated in favour of kbHCRx.')
vmwNetHCPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetHCPktsTx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetHCPktsTx.setDescription('Number of pkts transmitted on this NIC since network module was loaded.')
vmwNetHCKbTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetHCKbTx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetHCKbTx.setDescription('Kilobytes sent from this NIC since network module was loaded.')
vmwNetHCPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetHCPktsRx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetHCPktsRx.setDescription('Number of pkts received on this NIC since network module was loaded.')
vmwNetHCKbRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNetHCKbRx.setStatus('obsolete')
if mibBuilder.loadTexts: vmwNetHCKbRx.setDescription('Kilobytes received on this NIC since network module was loaded.')
vpxdTrapType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 301), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpxdTrapType.setStatus('current')
if mibBuilder.loadTexts: vpxdTrapType.setDescription('This is the trap type in the preceding traps.')
vpxdHostName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 302), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpxdHostName.setStatus('current')
if mibBuilder.loadTexts: vpxdHostName.setDescription('This is the name of the host in the preceding traps.')
vpxdVMName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 303), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpxdVMName.setStatus('current')
if mibBuilder.loadTexts: vpxdVMName.setDescription('This is the name of the VM in the preceding traps.')
vpxdOldStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 304), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpxdOldStatus.setStatus('current')
if mibBuilder.loadTexts: vpxdOldStatus.setDescription('This is the old status in the preceding traps.')
vpxdNewStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 305), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpxdNewStatus.setStatus('current')
if mibBuilder.loadTexts: vpxdNewStatus.setDescription('This is the new status in the preceding traps.')
vpxdObjValue = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 306), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpxdObjValue.setStatus('current')
if mibBuilder.loadTexts: vpxdObjValue.setDescription('This is the current object value in the preceding traps.')
vmPoweredOn = NotificationType((1, 3, 6, 1, 4, 1, 6876, 0, 1)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
if mibBuilder.loadTexts: vmPoweredOn.setStatus('obsolete')
if mibBuilder.loadTexts: vmPoweredOn.setDescription('This trap is sent when a virtual machine is powered ON from a suspended \n         or a powered off state.')
vmPoweredOff = NotificationType((1, 3, 6, 1, 4, 1, 6876, 0, 2)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
if mibBuilder.loadTexts: vmPoweredOff.setStatus('obsolete')
if mibBuilder.loadTexts: vmPoweredOff.setDescription('This trap is sent when a virtual machine is powered OFF.')
vmHBLost = NotificationType((1, 3, 6, 1, 4, 1, 6876, 0, 3)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
if mibBuilder.loadTexts: vmHBLost.setStatus('obsolete')
if mibBuilder.loadTexts: vmHBLost.setDescription('This trap is sent when a virtual machine detects a loss in guest heartbeat.')
vmHBDetected = NotificationType((1, 3, 6, 1, 4, 1, 6876, 0, 4)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
if mibBuilder.loadTexts: vmHBDetected.setStatus('obsolete')
if mibBuilder.loadTexts: vmHBDetected.setDescription('This trap is sent when a virtual machine detects or regains the guest heartbeat.')
vmSuspended = NotificationType((1, 3, 6, 1, 4, 1, 6876, 0, 5)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
if mibBuilder.loadTexts: vmSuspended.setStatus('obsolete')
if mibBuilder.loadTexts: vmSuspended.setDescription('This trap is sent when a virtual machine is suspended.')
vpxdTrap = NotificationType((1, 3, 6, 1, 4, 1, 6876, 0, 201)).setObjects(("VMWARE-OBSOLETE-MIB", "vpxdTrapType"), ("VMWARE-OBSOLETE-MIB", "vpxdHostName"), ("VMWARE-OBSOLETE-MIB", "vpxdVMName"), ("VMWARE-OBSOLETE-MIB", "vpxdNewStatus"), ("VMWARE-OBSOLETE-MIB", "vpxdOldStatus"), ("VMWARE-OBSOLETE-MIB", "vpxdObjValue"))
if mibBuilder.loadTexts: vpxdTrap.setStatus('obsolete')
if mibBuilder.loadTexts: vpxdTrap.setDescription('This trap is sent when entity status changed.')
vmwObsoleteMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 800, 1, 2))
vmwObsoleteMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 1))
vmwObsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 2))
vmwObsoleteObsoleteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 1, 3)).setObjects(("VMWARE-OBSOLETE-MIB", "vmwObsoleteGroup"), ("VMWARE-OBSOLETE-MIB", "vmwOldVCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwObsoleteObsoleteMIBCompliance = vmwObsoleteObsoleteMIBCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: vmwObsoleteObsoleteMIBCompliance.setDescription('The compliance statement for entities which implement the \n    VMWARE-RESOURCE-MIB.')
vmwObsoleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 2, 2)).setObjects(("VMWARE-OBSOLETE-MIB", "vmkLoaded"), ("VMWARE-OBSOLETE-MIB", "vmwCpuShares"), ("VMWARE-OBSOLETE-MIB", "vmwCpuUtil"), ("VMWARE-OBSOLETE-MIB", "vmwMemShares"), ("VMWARE-OBSOLETE-MIB", "vmwMemConfigured"), ("VMWARE-OBSOLETE-MIB", "vmwMemUtil"), ("VMWARE-OBSOLETE-MIB", "vmwHbaName"), ("VMWARE-OBSOLETE-MIB", "vmwHbaVMID"), ("VMWARE-OBSOLETE-MIB", "vmwDiskShares"), ("VMWARE-OBSOLETE-MIB", "vmwNumReads"), ("VMWARE-OBSOLETE-MIB", "vmwKbRead"), ("VMWARE-OBSOLETE-MIB", "vmwNumWrites"), ("VMWARE-OBSOLETE-MIB", "vmwKbWritten"), ("VMWARE-OBSOLETE-MIB", "vmwNetName"), ("VMWARE-OBSOLETE-MIB", "vmwNetVMID"), ("VMWARE-OBSOLETE-MIB", "vmwNetIfAddr"), ("VMWARE-OBSOLETE-MIB", "vmwNetShares"), ("VMWARE-OBSOLETE-MIB", "vmwNetPktsTx"), ("VMWARE-OBSOLETE-MIB", "vmwNetKbTx"), ("VMWARE-OBSOLETE-MIB", "vmwNetPktsRx"), ("VMWARE-OBSOLETE-MIB", "vmwNetKbRx"), ("VMWARE-OBSOLETE-MIB", "vmwNetHCPktsTx"), ("VMWARE-OBSOLETE-MIB", "vmwNetHCKbTx"), ("VMWARE-OBSOLETE-MIB", "vmwNetHCPktsRx"), ("VMWARE-OBSOLETE-MIB", "vmwNetHCKbRx"), ("VMWARE-OBSOLETE-MIB", "vpxdTrapType"), ("VMWARE-OBSOLETE-MIB", "vpxdHostName"), ("VMWARE-OBSOLETE-MIB", "vpxdVMName"), ("VMWARE-OBSOLETE-MIB", "vpxdOldStatus"), ("VMWARE-OBSOLETE-MIB", "vpxdNewStatus"), ("VMWARE-OBSOLETE-MIB", "vpxdObjValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwObsoleteGroup = vmwObsoleteGroup.setStatus('obsolete')
if mibBuilder.loadTexts: vmwObsoleteGroup.setDescription('These objects are no longer provided, see VMWARE-VMINFO-MIB for replacement.')
vmwOldVCNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 2, 3)).setObjects(("VMWARE-OBSOLETE-MIB", "vpxdTrap"), ("VMWARE-OBSOLETE-MIB", "vmPoweredOn"), ("VMWARE-OBSOLETE-MIB", "vmPoweredOff"), ("VMWARE-OBSOLETE-MIB", "vmHBLost"), ("VMWARE-OBSOLETE-MIB", "vmHBDetected"), ("VMWARE-OBSOLETE-MIB", "vmSuspended"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwOldVCNotificationGroup = vmwOldVCNotificationGroup.setStatus('obsolete')
if mibBuilder.loadTexts: vmwOldVCNotificationGroup.setDescription('Group of objects describing notifications (traps).')
mibBuilder.exportSymbols("VMWARE-OBSOLETE-MIB", vmwCpuVMID=vmwCpuVMID, vmwMemVMID=vmwMemVMID, vmwMemUtil=vmwMemUtil, vmwNetEntry=vmwNetEntry, vmwNetVMID=vmwNetVMID, vmwCpuEntry=vmwCpuEntry, vmwNetPktsRx=vmwNetPktsRx, vmwCpuUtil=vmwCpuUtil, vmwObsoleteMIBConformance=vmwObsoleteMIBConformance, vpxdObjValue=vpxdObjValue, vmHBDetected=vmHBDetected, vmPoweredOff=vmPoweredOff, PYSNMP_MODULE_ID=vmwObsoleteMIB, vmwMemShares=vmwMemShares, vmwHbaVMID=vmwHbaVMID, vmwNetKbTx=vmwNetKbTx, vmwNetTable=vmwNetTable, vmwNetHCPktsRx=vmwNetHCPktsRx, vpxdTrapType=vpxdTrapType, vmwObsoleteMIBCompliances=vmwObsoleteMIBCompliances, vmwMemTable=vmwMemTable, vmwHBAEntry=vmwHBAEntry, vmwObsoleteMIB=vmwObsoleteMIB, vmwCpuTable=vmwCpuTable, vmwMemConfigured=vmwMemConfigured, vmwNetHCKbTx=vmwNetHCKbTx, vpxdNewStatus=vpxdNewStatus, vmwObsoleteGroup=vmwObsoleteGroup, vpxdTrap=vpxdTrap, vmwNetHCPktsTx=vmwNetHCPktsTx, vmwDiskShares=vmwDiskShares, vmwNetPktsTx=vmwNetPktsTx, vmwNetKbRx=vmwNetKbRx, vmwCpuShares=vmwCpuShares, vpxdOldStatus=vpxdOldStatus, vmwHbaName=vmwHbaName, vmPoweredOn=vmPoweredOn, vmwNetName=vmwNetName, vmHBLost=vmHBLost, vmwObsoleteObsoleteMIBCompliance=vmwObsoleteObsoleteMIBCompliance, vpxdHostName=vpxdHostName, vmwHbaIdx=vmwHbaIdx, vmwObsMIBGroups=vmwObsMIBGroups, vmwKbRead=vmwKbRead, vmwOldVCNotificationGroup=vmwOldVCNotificationGroup, vmwNumReads=vmwNumReads, vmwMemEntry=vmwMemEntry, vmwHBATable=vmwHBATable, vmkLoaded=vmkLoaded, vmwNumWrites=vmwNumWrites, vmwNetHCKbRx=vmwNetHCKbRx, vmwNetIfAddr=vmwNetIfAddr, vmwNetIdx=vmwNetIdx, vpxdVMName=vpxdVMName, vmSuspended=vmSuspended, vmwKbWritten=vmwKbWritten, vmwNetShares=vmwNetShares)
