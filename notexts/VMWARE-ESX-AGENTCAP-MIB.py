#
# PySNMP MIB module VMWARE-ESX-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-ESX-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:53:29 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Counter32, Gauge32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, MibIdentifier, IpAddress, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter32", "Gauge32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "MibIdentifier", "IpAddress", "iso", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 1))
vmwAgentCapabilityMIB.setRevisions(('2020-03-27 00:00', '2017-10-13 00:00', '2016-04-22 00:00', '2015-01-12 00:00', '2014-08-02 00:00', '2012-10-03 00:00', '2012-07-13 00:00', '2010-10-18 00:00', '2008-10-27 00:00',))
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setLastUpdated('202003270000Z')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwEsxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1))
vmwESX70x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX70x = vmwESX70x.setProductRelease('7.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX70x = vmwESX70x.setStatus('current')
vmwESX67x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX67x = vmwESX67x.setProductRelease('6.7.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX67x = vmwESX67x.setStatus('current')
vmwESX65x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX65x = vmwESX65x.setProductRelease('6.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX65x = vmwESX65x.setStatus('current')
vmwESX60x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX60x = vmwESX60x.setProductRelease('6.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX60x = vmwESX60x.setStatus('current')
vmwESX55 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX55 = vmwESX55.setProductRelease('5.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX55 = vmwESX55.setStatus('current')
vmwESX51x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setProductRelease('5.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setStatus('current')
vmwESX50x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setProductRelease('5.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setStatus('current')
vmwESX41x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setProductRelease('4.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setStatus('current')
vmwESX40x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setProductRelease('4.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setStatus('current')
mibBuilder.exportSymbols("VMWARE-ESX-AGENTCAP-MIB", vmwESX41x=vmwESX41x, vmwESX51x=vmwESX51x, vmwAgentCapabilityMIB=vmwAgentCapabilityMIB, vmwESX60x=vmwESX60x, vmwESX55=vmwESX55, vmwESX40x=vmwESX40x, vmwESX67x=vmwESX67x, vmwESX50x=vmwESX50x, PYSNMP_MODULE_ID=vmwAgentCapabilityMIB, vmwESX70x=vmwESX70x, vmwESX65x=vmwESX65x, vmwEsxCapability=vmwEsxCapability)
