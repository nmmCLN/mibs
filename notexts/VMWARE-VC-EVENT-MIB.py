#
# PySNMP MIB module VMWARE-VC-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VC-EVENT-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:35:11 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Bits, Unsigned32, Counter32, NotificationType, TimeTicks, Integer32, ObjectIdentity, Counter64, MibIdentifier, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Unsigned32", "Counter32", "NotificationType", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64", "MibIdentifier", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwVC, = mibBuilder.importSymbols("VMWARE-PRODUCTS-MIB", "vmwVC")
VmwLongSnmpAdminString, = mibBuilder.importSymbols("VMWARE-TC-MIB", "VmwLongSnmpAdminString")
vmwVCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1))
vmwVCMIB.setRevisions(('2009-12-15 00:00', '2009-09-08 00:00', '2009-05-27 00:00', '2009-04-06 00:00', '2009-03-17 00:00', '2008-02-22 00:00',))
if mibBuilder.loadTexts: vmwVCMIB.setLastUpdated('200912150000Z')
if mibBuilder.loadTexts: vmwVCMIB.setOrganization('VMware, Inc')
vmwVCNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0))
vpxdAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 201)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
if mibBuilder.loadTexts: vpxdAlarm.setStatus('obsolete')
vpxdDiagnostic = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 202))
if mibBuilder.loadTexts: vpxdDiagnostic.setStatus('current')
vpxdAlarmInfo = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 203)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
if mibBuilder.loadTexts: vpxdAlarmInfo.setStatus('current')
vmwVpxdTrapType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 301), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTrapType.setStatus('obsolete')
vmwVpxdHostName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 302), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdHostName.setStatus('obsolete')
vmwVpxdVMName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 303), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdVMName.setStatus('obsolete')
vmwVpxdOldStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 304), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdOldStatus.setStatus('current')
vmwVpxdNewStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 305), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdNewStatus.setStatus('current')
vmwVpxdObjValue = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 306), VmwLongSnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdObjValue.setStatus('current')
vmwVpxdTargetObj = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 307), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTargetObj.setStatus('current')
vmwVpxdTargetObjType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 308), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("host", 2), ("vm", 3), ("other", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTargetObjType.setStatus('current')
vmwVCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2))
vmwVCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1))
vmwVCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2))
vmwVCMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 2)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVCAlarmInfoGroup"), ("VMWARE-VC-EVENT-MIB", "vmwVCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCMIBBasicCompliance = vmwVCMIBBasicCompliance.setStatus('obsolete')
vmwVCMIBBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 3)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVCAlarmGroup"), ("VMWARE-VC-EVENT-MIB", "vmwVCAlarmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCMIBBasicComplianceRev2 = vmwVCMIBBasicComplianceRev2.setStatus('current')
vmwVCAlarmInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 1)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmInfoGroup = vmwVCAlarmInfoGroup.setStatus('obsolete')
vmwVCNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 2)).setObjects(("VMWARE-VC-EVENT-MIB", "vpxdAlarm"), ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCNotificationGroup = vmwVCNotificationGroup.setStatus('obsolete')
vmwVCAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 3)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmGroup = vmwVCAlarmGroup.setStatus('current')
vmwVCAlarmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 4)).setObjects(("VMWARE-VC-EVENT-MIB", "vpxdAlarmInfo"), ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmNotificationGroup = vmwVCAlarmNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-VC-EVENT-MIB", vmwVCNotificationGroup=vmwVCNotificationGroup, vmwVCAlarmNotificationGroup=vmwVCAlarmNotificationGroup, vmwVCAlarmGroup=vmwVCAlarmGroup, vpxdAlarmInfo=vpxdAlarmInfo, vmwVCMIBCompliances=vmwVCMIBCompliances, vmwVpxdObjValue=vmwVpxdObjValue, vmwVpxdTrapType=vmwVpxdTrapType, vmwVCAlarmInfoGroup=vmwVCAlarmInfoGroup, vmwVCMIBBasicCompliance=vmwVCMIBBasicCompliance, vmwVpxdVMName=vmwVpxdVMName, vmwVCNotifications=vmwVCNotifications, vmwVCMIB=vmwVCMIB, vmwVpxdTargetObjType=vmwVpxdTargetObjType, vpxdDiagnostic=vpxdDiagnostic, vmwVpxdHostName=vmwVpxdHostName, vmwVpxdNewStatus=vmwVpxdNewStatus, vmwVpxdTargetObj=vmwVpxdTargetObj, vmwVCMIBConformance=vmwVCMIBConformance, PYSNMP_MODULE_ID=vmwVCMIB, vmwVCMIBBasicComplianceRev2=vmwVCMIBBasicComplianceRev2, vpxdAlarm=vpxdAlarm, vmwVCMIBGroups=vmwVCMIBGroups, vmwVpxdOldStatus=vmwVpxdOldStatus)
