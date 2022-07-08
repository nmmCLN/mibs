#
# PySNMP MIB module VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/VLAN
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:48 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
interface, = mibBuilder.importSymbols("ExaltComProducts", "interface")
VlanStatusT, VlanGroupT = mibBuilder.importSymbols("ExaltComm", "VlanStatusT", "VlanGroupT")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, MibIdentifier, TimeTicks, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ObjectIdentity, iso, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "TimeTicks", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ObjectIdentity", "iso", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vlan = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3))
if mibBuilder.loadTexts: vlan.setStatus('current')
if mibBuilder.loadTexts: vlan.setDescription('VLAN interfaces.')
vlanStatus = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1), VlanStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanStatus.setStatus('current')
if mibBuilder.loadTexts: vlanStatus.setDescription('This setting enables or disables VLAN support.')
vlanDefaultMgmtId = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultMgmtId.setStatus('current')
if mibBuilder.loadTexts: vlanDefaultMgmtId.setDescription('This is the Default management VLAN ID for all Ethernet\n                            Interface.')
vlanInterfaces = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6), )
if mibBuilder.loadTexts: vlanInterfaces.setStatus('current')
if mibBuilder.loadTexts: vlanInterfaces.setDescription('This is a table of Vlan interface configurations.')
vlanInterfacesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1), ).setIndexNames((0, "VLAN", "vlanDefaultId"))
if mibBuilder.loadTexts: vlanInterfacesEntry.setStatus('current')
if mibBuilder.loadTexts: vlanInterfacesEntry.setDescription('This is a Vlan table entry.')
vlanDefaultId = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultId.setStatus('current')
if mibBuilder.loadTexts: vlanDefaultId.setDescription('This is the default VLAN ID for the ETH2 Ethernet\n                            Interface.')
vlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanID.setStatus('current')
if mibBuilder.loadTexts: vlanID.setDescription('This is the list of Vlan ID in comma seperated format. For\n                             example, 2,10-20,2000.')
commitVlanSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1000), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitVlanSettings.setStatus('current')
if mibBuilder.loadTexts: commitVlanSettings.setDescription('This command allows saving, or resetting Vlan\n                            parameters to factory original. Options are:\n                            save, clear, reset; where clear will abandon\n                            unsaved changes.')
mibBuilder.exportSymbols("VLAN", vlanInterfaces=vlanInterfaces, vlanInterfacesEntry=vlanInterfacesEntry, vlanDefaultMgmtId=vlanDefaultMgmtId, commitVlanSettings=commitVlanSettings, vlanID=vlanID, vlanStatus=vlanStatus, vlanDefaultId=vlanDefaultId, vlan=vlan)
