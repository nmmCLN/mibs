#
# PySNMP MIB module VMWARE-RESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-RESOURCES-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:24:01 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Counter32, MibIdentifier, IpAddress, TimeTicks, Unsigned32, Gauge32, Counter64, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Counter32", "MibIdentifier", "IpAddress", "TimeTicks", "Unsigned32", "Gauge32", "Counter64", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwResources, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwResources")
VmwSubsystemStatus, = mibBuilder.importSymbols("VMWARE-TC-MIB", "VmwSubsystemStatus")
vmwResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 3, 10))
vmwResourcesMIB.setRevisions(('2008-10-15 00:00', '2007-12-27 00:00',))
if mibBuilder.loadTexts: vmwResourcesMIB.setLastUpdated('200810150000Z')
if mibBuilder.loadTexts: vmwResourcesMIB.setOrganization('VMware, Inc')
vmwCPU = ObjectIdentity((1, 3, 6, 1, 4, 1, 6876, 3, 1))
if mibBuilder.loadTexts: vmwCPU.setStatus('current')
vmwNumCPUs = MibScalar((1, 3, 6, 1, 4, 1, 6876, 3, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwNumCPUs.setStatus('current')
vmwMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 3, 2))
vmwMemSize = MibScalar((1, 3, 6, 1, 4, 1, 6876, 3, 2, 1), Gauge32()).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwMemSize.setStatus('current')
vmwMemCOS = MibScalar((1, 3, 6, 1, 4, 1, 6876, 3, 2, 2), Gauge32()).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwMemCOS.setStatus('current')
vmwMemAvail = MibScalar((1, 3, 6, 1, 4, 1, 6876, 3, 2, 3), Gauge32()).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwMemAvail.setStatus('current')
vmwStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 3, 5))
vmwHostBusAdapterNumber = MibScalar((1, 3, 6, 1, 4, 1, 6876, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHostBusAdapterNumber.setStatus('current')
vmwHostBusAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2), )
if mibBuilder.loadTexts: vmwHostBusAdapterTable.setStatus('current')
vmwHostBusAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1), ).setIndexNames((0, "VMWARE-RESOURCES-MIB", "vmwHostBusAdapterIndex"))
if mibBuilder.loadTexts: vmwHostBusAdapterEntry.setStatus('current')
vmwHostBusAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)))
if mibBuilder.loadTexts: vmwHostBusAdapterIndex.setStatus('current')
vmwHbaDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaDeviceName.setStatus('current')
vmwHbaBusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1023), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaBusNumber.setStatus('current')
vmwHbaStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 4), VmwSubsystemStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaStatus.setStatus('current')
vmwHbaModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaModelName.setStatus('current')
vmwHbaDriverName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaDriverName.setStatus('current')
vmwHbaPci = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaPci.setStatus('current')
vmwResourceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 3, 10, 2))
vmwResourceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 1))
vmwResMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 2))
vmwResourceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 1, 2)).setObjects(("VMWARE-RESOURCES-MIB", "vmwResourceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwResourceMIBCompliance = vmwResourceMIBCompliance.setStatus('current')
vmwResourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 2, 1)).setObjects(("VMWARE-RESOURCES-MIB", "vmwNumCPUs"), ("VMWARE-RESOURCES-MIB", "vmwMemSize"), ("VMWARE-RESOURCES-MIB", "vmwMemCOS"), ("VMWARE-RESOURCES-MIB", "vmwMemAvail"), ("VMWARE-RESOURCES-MIB", "vmwHostBusAdapterNumber"), ("VMWARE-RESOURCES-MIB", "vmwHbaDeviceName"), ("VMWARE-RESOURCES-MIB", "vmwHbaBusNumber"), ("VMWARE-RESOURCES-MIB", "vmwHbaStatus"), ("VMWARE-RESOURCES-MIB", "vmwHbaModelName"), ("VMWARE-RESOURCES-MIB", "vmwHbaDriverName"), ("VMWARE-RESOURCES-MIB", "vmwHbaPci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwResourceGroup = vmwResourceGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-RESOURCES-MIB", vmwHostBusAdapterEntry=vmwHostBusAdapterEntry, vmwResourceGroup=vmwResourceGroup, vmwResourceMIBConformance=vmwResourceMIBConformance, PYSNMP_MODULE_ID=vmwResourcesMIB, vmwHbaDriverName=vmwHbaDriverName, vmwCPU=vmwCPU, vmwHbaBusNumber=vmwHbaBusNumber, vmwMemory=vmwMemory, vmwHostBusAdapterNumber=vmwHostBusAdapterNumber, vmwHbaStatus=vmwHbaStatus, vmwMemAvail=vmwMemAvail, vmwResMIBGroups=vmwResMIBGroups, vmwResourceMIBCompliance=vmwResourceMIBCompliance, vmwHostBusAdapterIndex=vmwHostBusAdapterIndex, vmwStorage=vmwStorage, vmwHostBusAdapterTable=vmwHostBusAdapterTable, vmwNumCPUs=vmwNumCPUs, vmwHbaPci=vmwHbaPci, vmwMemSize=vmwMemSize, vmwHbaModelName=vmwHbaModelName, vmwHbaDeviceName=vmwHbaDeviceName, vmwMemCOS=vmwMemCOS, vmwResourcesMIB=vmwResourcesMIB, vmwResourceMIBCompliances=vmwResourceMIBCompliances)
