#
# PySNMP MIB module NBS-VLAN-TAGS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-VLAN-TAGS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:28:05 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, ObjectIdentity, NotificationType, ModuleIdentity, Counter32, Integer32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter32", "Integer32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsVlanTagsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 219))
if mibBuilder.loadTexts: nbsVlanTagsMib.setLastUpdated('201604291200Z')
if mibBuilder.loadTexts: nbsVlanTagsMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsVlanTagsMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsVlanTagsMib.setDescription('MIB for setting VLAN tags for tagging and stacking')
nbsVlanTagsPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 219, 1))
if mibBuilder.loadTexts: nbsVlanTagsPortGrp.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortGrp.setDescription('VLAN Tags information')
nbsVlanTagsPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 219, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsVlanTagsPortTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortTableSize.setDescription('The number of entries in nbsVlanTagsPortTable.')
nbsVlanTagsPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 219, 1, 2), )
if mibBuilder.loadTexts: nbsVlanTagsPortTable.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortTable.setDescription('')
nbsVlanTagsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1), ).setIndexNames((0, "NBS-VLAN-TAGS-MIB", "nbsVlanTagsPortIfIndex"))
if mibBuilder.loadTexts: nbsVlanTagsPortEntry.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortEntry.setDescription('')
nbsVlanTagsPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsVlanTagsPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortIfIndex.setDescription('The Mib2 ifIndex of the VLAN tag port')
nbsVlanTagsPortAction = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("add", 2), ("strip", 3), ("ignore", 4))).clone('ignore')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsVlanTagsPortAction.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortAction.setDescription('add(2) need two more arguments s-vlanId and s-vlan-priority\n           strip(3)and ignore(4) does not need any argument')
nbsVlanTagsPortVid = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsVlanTagsPortVid.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortVid.setDescription('need to be specified when VlanTagAction is add(2)')
nbsVlanTagsPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsVlanTagsPortPriority.setStatus('current')
if mibBuilder.loadTexts: nbsVlanTagsPortPriority.setDescription('need to be specified when VlanTagAction is add(2)')
mibBuilder.exportSymbols("NBS-VLAN-TAGS-MIB", nbsVlanTagsPortTableSize=nbsVlanTagsPortTableSize, nbsVlanTagsMib=nbsVlanTagsMib, nbsVlanTagsPortVid=nbsVlanTagsPortVid, nbsVlanTagsPortIfIndex=nbsVlanTagsPortIfIndex, PYSNMP_MODULE_ID=nbsVlanTagsMib, nbsVlanTagsPortTable=nbsVlanTagsPortTable, nbsVlanTagsPortGrp=nbsVlanTagsPortGrp, nbsVlanTagsPortAction=nbsVlanTagsPortAction, nbsVlanTagsPortPriority=nbsVlanTagsPortPriority, nbsVlanTagsPortEntry=nbsVlanTagsPortEntry)
