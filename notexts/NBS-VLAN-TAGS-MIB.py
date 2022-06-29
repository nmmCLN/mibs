#
# PySNMP MIB module NBS-VLAN-TAGS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-VLAN-TAGS-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:41 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, Counter64, TimeTicks, iso, Counter32, Unsigned32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Counter64", "TimeTicks", "iso", "Counter32", "Unsigned32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsVlanTagsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 219))
if mibBuilder.loadTexts: nbsVlanTagsMib.setLastUpdated('201604291200Z')
if mibBuilder.loadTexts: nbsVlanTagsMib.setOrganization('NBS')
nbsVlanTagsPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 219, 1))
if mibBuilder.loadTexts: nbsVlanTagsPortGrp.setStatus('current')
nbsVlanTagsPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 219, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsVlanTagsPortTableSize.setStatus('current')
nbsVlanTagsPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 219, 1, 2), )
if mibBuilder.loadTexts: nbsVlanTagsPortTable.setStatus('current')
nbsVlanTagsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1), ).setIndexNames((0, "NBS-VLAN-TAGS-MIB", "nbsVlanTagsPortIfIndex"))
if mibBuilder.loadTexts: nbsVlanTagsPortEntry.setStatus('current')
nbsVlanTagsPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsVlanTagsPortIfIndex.setStatus('current')
nbsVlanTagsPortAction = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("add", 2), ("strip", 3), ("ignore", 4))).clone('ignore')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsVlanTagsPortAction.setStatus('current')
nbsVlanTagsPortVid = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsVlanTagsPortVid.setStatus('current')
nbsVlanTagsPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsVlanTagsPortPriority.setStatus('current')
mibBuilder.exportSymbols("NBS-VLAN-TAGS-MIB", nbsVlanTagsPortAction=nbsVlanTagsPortAction, nbsVlanTagsPortIfIndex=nbsVlanTagsPortIfIndex, nbsVlanTagsPortPriority=nbsVlanTagsPortPriority, nbsVlanTagsPortGrp=nbsVlanTagsPortGrp, nbsVlanTagsMib=nbsVlanTagsMib, nbsVlanTagsPortTable=nbsVlanTagsPortTable, PYSNMP_MODULE_ID=nbsVlanTagsMib, nbsVlanTagsPortTableSize=nbsVlanTagsPortTableSize, nbsVlanTagsPortVid=nbsVlanTagsPortVid, nbsVlanTagsPortEntry=nbsVlanTagsPortEntry)
