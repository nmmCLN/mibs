#
# PySNMP MIB module VMWARE-CIMOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-CIMOM-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:16:43 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, IpAddress, ObjectIdentity, NotificationType, ModuleIdentity, iso, Gauge32, MibIdentifier, Bits, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "IpAddress", "ObjectIdentity", "NotificationType", "ModuleIdentity", "iso", "Gauge32", "MibIdentifier", "Bits", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwEnvIndicationTime, = mibBuilder.importSymbols("VMWARE-ENV-MIB", "vmwEnvIndicationTime")
vmwProductSpecific, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific")
vmwCIMOMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 90, 10))
vmwCIMOMMIB.setRevisions(('2010-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwCIMOMMIB.setRevisionsDescriptions(('Information on a CIM object manager subsystem.',))
if mibBuilder.loadTexts: vmwCIMOMMIB.setLastUpdated('201008200000Z')
if mibBuilder.loadTexts: vmwCIMOMMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwCIMOMMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwCIMOMMIB.setDescription('This MIB module provides instrumentation of a CIM Object Manager.')
vmwCimOm = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90))
vmwCimOmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 0))
vmwCimOmHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 90, 0, 401)).setObjects(("VMWARE-ENV-MIB", "vmwEnvIndicationTime"))
if mibBuilder.loadTexts: vmwCimOmHeartbeat.setStatus('current')
if mibBuilder.loadTexts: vmwCimOmHeartbeat.setDescription('This notification, if the agent is so configured, will be sent \n         on a periodic basis to indicate cimom indication delivery is functioning.')
vmwCimOmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2))
vmwCimOmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1))
vmwCimOmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2))
vmwCimOmMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1, 4)).setObjects(("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"), ("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwCimOmMIBBasicCompliance = vmwCimOmMIBBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: vmwCimOmMIBBasicCompliance.setDescription('The compliance statement for entities which implement the \n    VMWARE-CIMOM-MIB.')
vmwCimOmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2, 2)).setObjects(("VMWARE-CIMOM-MIB", "vmwCimOmHeartbeat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwCimOmNotificationGroup = vmwCimOmNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vmwCimOmNotificationGroup.setDescription('Notifications related to CIM Object Manager subsystem.')
mibBuilder.exportSymbols("VMWARE-CIMOM-MIB", vmwCimOmMIBGroups=vmwCimOmMIBGroups, vmwCimOm=vmwCimOm, vmwCIMOMMIB=vmwCIMOMMIB, PYSNMP_MODULE_ID=vmwCIMOMMIB, vmwCimOmMIBBasicCompliance=vmwCimOmMIBBasicCompliance, vmwCimOmNotifications=vmwCimOmNotifications, vmwCimOmNotificationGroup=vmwCimOmNotificationGroup, vmwCimOmHeartbeat=vmwCimOmHeartbeat, vmwCimOmMIBConformance=vmwCimOmMIBConformance, vmwCimOmMIBCompliances=vmwCimOmMIBCompliances)
