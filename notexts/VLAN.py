#
# PySNMP MIB module VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/VLAN
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
interface, = mibBuilder.importSymbols("ExaltComProducts", "interface")
VlanGroupT, VlanStatusT = mibBuilder.importSymbols("ExaltComm", "VlanGroupT", "VlanStatusT")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, iso, Counter64, Bits, TimeTicks, Gauge32, Unsigned32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter64", "Bits", "TimeTicks", "Gauge32", "Unsigned32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vlan = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3))
if mibBuilder.loadTexts: vlan.setStatus('current')
vlanStatus = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1), VlanStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanStatus.setStatus('current')
vlanDefaultMgmtId = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultMgmtId.setStatus('current')
vlanInterfaces = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6), )
if mibBuilder.loadTexts: vlanInterfaces.setStatus('current')
vlanInterfacesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1), ).setIndexNames((0, "VLAN", "vlanDefaultId"))
if mibBuilder.loadTexts: vlanInterfacesEntry.setStatus('current')
vlanDefaultId = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultId.setStatus('current')
vlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanID.setStatus('current')
commitVlanSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1000), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitVlanSettings.setStatus('current')
mibBuilder.exportSymbols("VLAN", vlanID=vlanID, commitVlanSettings=commitVlanSettings, vlanDefaultId=vlanDefaultId, vlanInterfacesEntry=vlanInterfacesEntry, vlanStatus=vlanStatus, vlan=vlan, vlanDefaultMgmtId=vlanDefaultMgmtId, vlanInterfaces=vlanInterfaces)
