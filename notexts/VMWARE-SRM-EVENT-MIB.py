#
# PySNMP MIB module VMWARE-SRM-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-SRM-EVENT-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:24:01 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Gauge32, MibIdentifier, IpAddress, TimeTicks, Unsigned32, Bits, Counter64, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "TimeTicks", "Unsigned32", "Bits", "Counter64", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwSRM, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwSRM")
vmwSRMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 51, 10))
vmwSRMMIB.setRevisions(('2012-02-07 00:00',))
if mibBuilder.loadTexts: vmwSRMMIB.setLastUpdated('201202070000Z')
if mibBuilder.loadTexts: vmwSRMMIB.setOrganization('VMware, Inc')
vmwSrmNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 51, 1))
vmwSRMevents = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 51, 0))
vmwSrmVmName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmVmName.setStatus('current')
vmwSrmRecoveryName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmRecoveryName.setStatus('current')
vmwSrmPromptString = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmPromptString.setStatus('current')
vmwSrmRecoveryType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("test", 1), ("recovery", 2), ("reprotect", 3), ("cleanup", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmRecoveryType.setStatus('current')
vmwSrmRecoveryState = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uninitialized", 1), ("running", 2), ("paused", 3), ("cancelled", 4), ("completed", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmRecoveryState.setStatus('current')
vmwSrmSiteString = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmSiteString.setStatus('current')
vmwSrmVmUuid = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmVmUuid.setStatus('current')
vmwSrmResult = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("warning", 3), ("cancelled", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmResult.setStatus('current')
vmwSrmCommandName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 51, 1, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwSrmCommandName.setStatus('current')
vmwareSrmRecoveryPlanExecuteTestBeginTrap = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 1)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanExecuteTestBeginTrap.setStatus('current')
vmwareSrmRecoveryPlanExecuteTestEndEvent = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 2)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanExecuteTestEndEvent.setStatus('current')
vmwareSrmRecoveryPlanExecuteBeginEvent = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 3)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanExecuteBeginEvent.setStatus('current')
vmwareVmwSrmRecoveryPlanExecuteEndEvent = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 4)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
if mibBuilder.loadTexts: vmwareVmwSrmRecoveryPlanExecuteEndEvent.setStatus('current')
vmwareVmwSrmRecoveryVmBeginEvent = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 5)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"))
if mibBuilder.loadTexts: vmwareVmwSrmRecoveryVmBeginEvent.setStatus('current')
vmwareSrmRecoveryVmEndEvent = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 6)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
if mibBuilder.loadTexts: vmwareSrmRecoveryVmEndEvent.setStatus('current')
vmwareSrmRecoveryPlanPromptDisplay = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 7)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmPromptString"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanPromptDisplay.setStatus('current')
vmwareSrmRecoveryPlanPromptResponse = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 8)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanPromptResponse.setStatus('current')
vmwareVmwSrmRecoveryPlanServerCommandBegin = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 9)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"))
if mibBuilder.loadTexts: vmwareVmwSrmRecoveryPlanServerCommandBegin.setStatus('current')
vmwareSrmRecoveryPlanServerCommandEnd = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 10)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanServerCommandEnd.setStatus('current')
vmwareSrmRecoveryPlanVmCommandBegin = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 11)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanVmCommandBegin.setStatus('current')
vmwareSrmRecoveryPlanVmCommandEnd = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 12)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanVmCommandEnd.setStatus('current')
vmwareSrmRecoveryPlanExecuteReprotectBegin = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 13)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanExecuteReprotectBegin.setStatus('current')
vmwareSrmRecoveryPlanExecuteReprotectEnd = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 14)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
if mibBuilder.loadTexts: vmwareSrmRecoveryPlanExecuteReprotectEnd.setStatus('current')
vmwareVmwSrmRecoveryPlanExecuteCleanupBegin = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 15)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
if mibBuilder.loadTexts: vmwareVmwSrmRecoveryPlanExecuteCleanupBegin.setStatus('current')
vmwSrmRecoveryPlanExecuteCleanupEnd = NotificationType((1, 3, 6, 1, 4, 1, 6876, 51, 0, 16)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
if mibBuilder.loadTexts: vmwSrmRecoveryPlanExecuteCleanupEnd.setStatus('current')
vmwSRMMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 51, 10, 2))
vmwSRMMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 1))
vmwSRMMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 2))
vmwSRMMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 1, 2)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSRMNotificationInfoGroup"), ("VMWARE-SRM-EVENT-MIB", "vmwSRMNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSRMMIBBasicCompliance = vmwSRMMIBBasicCompliance.setStatus('current')
vmwSRMNotificationInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 2, 1)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmPromptString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSRMNotificationInfoGroup = vmwSRMNotificationInfoGroup.setStatus('current')
vmwSRMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 2, 2)).setObjects(("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteTestBeginTrap"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteTestEndEvent"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteBeginEvent"), ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryPlanExecuteEndEvent"), ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryVmBeginEvent"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryVmEndEvent"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanPromptDisplay"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanPromptResponse"), ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryPlanServerCommandBegin"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanServerCommandEnd"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanVmCommandBegin"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanVmCommandEnd"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteReprotectBegin"), ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteReprotectEnd"), ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryPlanExecuteCleanupBegin"), ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryPlanExecuteCleanupEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSRMNotificationGroup = vmwSRMNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-SRM-EVENT-MIB", vmwSRMMIB=vmwSRMMIB, vmwSrmRecoveryState=vmwSrmRecoveryState, vmwareVmwSrmRecoveryPlanServerCommandBegin=vmwareVmwSrmRecoveryPlanServerCommandBegin, vmwSrmVmUuid=vmwSrmVmUuid, vmwareSrmRecoveryPlanPromptDisplay=vmwareSrmRecoveryPlanPromptDisplay, vmwareSrmRecoveryPlanExecuteReprotectBegin=vmwareSrmRecoveryPlanExecuteReprotectBegin, vmwSrmRecoveryName=vmwSrmRecoveryName, vmwareSrmRecoveryPlanExecuteBeginEvent=vmwareSrmRecoveryPlanExecuteBeginEvent, vmwareVmwSrmRecoveryPlanExecuteEndEvent=vmwareVmwSrmRecoveryPlanExecuteEndEvent, vmwareSrmRecoveryPlanVmCommandEnd=vmwareSrmRecoveryPlanVmCommandEnd, vmwareSrmRecoveryPlanVmCommandBegin=vmwareSrmRecoveryPlanVmCommandBegin, vmwSrmSiteString=vmwSrmSiteString, vmwareSrmRecoveryPlanServerCommandEnd=vmwareSrmRecoveryPlanServerCommandEnd, vmwSRMNotificationGroup=vmwSRMNotificationGroup, vmwSrmVmName=vmwSrmVmName, vmwareSrmRecoveryPlanPromptResponse=vmwareSrmRecoveryPlanPromptResponse, vmwSrmRecoveryType=vmwSrmRecoveryType, vmwareSrmRecoveryPlanExecuteTestBeginTrap=vmwareSrmRecoveryPlanExecuteTestBeginTrap, vmwSRMMIBCompliances=vmwSRMMIBCompliances, vmwareSrmRecoveryPlanExecuteReprotectEnd=vmwareSrmRecoveryPlanExecuteReprotectEnd, vmwSrmRecoveryPlanExecuteCleanupEnd=vmwSrmRecoveryPlanExecuteCleanupEnd, vmwSrmCommandName=vmwSrmCommandName, vmwSRMevents=vmwSRMevents, vmwSrmNotification=vmwSrmNotification, vmwSRMMIBGroups=vmwSRMMIBGroups, vmwareVmwSrmRecoveryPlanExecuteCleanupBegin=vmwareVmwSrmRecoveryPlanExecuteCleanupBegin, vmwareSrmRecoveryVmEndEvent=vmwareSrmRecoveryVmEndEvent, vmwSRMNotificationInfoGroup=vmwSRMNotificationInfoGroup, vmwSrmResult=vmwSrmResult, vmwareSrmRecoveryPlanExecuteTestEndEvent=vmwareSrmRecoveryPlanExecuteTestEndEvent, vmwSRMMIBBasicCompliance=vmwSRMMIBBasicCompliance, vmwareVmwSrmRecoveryVmBeginEvent=vmwareVmwSrmRecoveryVmBeginEvent, vmwSRMMIBConformance=vmwSRMMIBConformance, vmwSrmPromptString=vmwSrmPromptString, PYSNMP_MODULE_ID=vmwSRMMIB)
