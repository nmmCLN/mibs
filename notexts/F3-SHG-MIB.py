#
# PySNMP MIB module F3-SHG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-SHG-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:07:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
neIndex, = mibBuilder.importSymbols("CM-ENTITY-MIB", "neIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Integer32, Unsigned32, iso, Bits, Counter32, Counter64, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Integer32", "Unsigned32", "iso", "Bits", "Counter32", "Counter64", "Gauge32", "TimeTicks")
VariablePointer, StorageType, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "VariablePointer", "StorageType", "DisplayString", "TextualConvention", "RowStatus")
f3SHGMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27))
f3SHGMIB.setRevisions(('2012-12-04 00:00',))
if mibBuilder.loadTexts: f3SHGMIB.setLastUpdated('201212040000Z')
if mibBuilder.loadTexts: f3SHGMIB.setOrganization('ADVA Optical Networking')
f3ShgConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1))
f3ShgConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2))
f3ShgTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1), )
if mibBuilder.loadTexts: f3ShgTable.setStatus('current')
f3ShgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-SHG-MIB", "f3ShgIndex"))
if mibBuilder.loadTexts: f3ShgEntry.setStatus('current')
f3ShgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: f3ShgIndex.setStatus('current')
f3ShgAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ShgAlias.setStatus('current')
f3ShgStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 3), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ShgStorageType.setStatus('current')
f3ShgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ShgRowStatus.setStatus('current')
f3ShgMemberPortTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2), )
if mibBuilder.loadTexts: f3ShgMemberPortTable.setStatus('current')
f3ShgMemberPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-SHG-MIB", "f3ShgIndex"), (0, "F3-SHG-MIB", "f3ShgMemberPort"))
if mibBuilder.loadTexts: f3ShgMemberPortEntry.setStatus('current')
f3ShgMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1, 1), VariablePointer())
if mibBuilder.loadTexts: f3ShgMemberPort.setStatus('current')
f3ShgMemberPortStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ShgMemberPortStorageType.setStatus('current')
f3ShgMemberPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ShgMemberPortRowStatus.setStatus('current')
f3ShgMemberFlowTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 3), )
if mibBuilder.loadTexts: f3ShgMemberFlowTable.setStatus('current')
f3ShgMemberFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-SHG-MIB", "f3ShgIndex"), (0, "F3-SHG-MIB", "f3ShgMemberFlow"))
if mibBuilder.loadTexts: f3ShgMemberFlowEntry.setStatus('current')
f3ShgMemberFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 3, 1, 1), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ShgMemberFlow.setStatus('current')
f3ShgMemberFlowPointTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 4), )
if mibBuilder.loadTexts: f3ShgMemberFlowPointTable.setStatus('current')
f3ShgMemberFlowPointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 4, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-SHG-MIB", "f3ShgIndex"), (0, "F3-SHG-MIB", "f3ShgMemberFlowPoint"))
if mibBuilder.loadTexts: f3ShgMemberFlowPointEntry.setStatus('current')
f3ShgMemberFlowPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 4, 1, 1), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ShgMemberFlowPoint.setStatus('current')
f3ShgCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 1))
f3ShgGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2))
f3ShgCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 1, 1)).setObjects(("F3-SHG-MIB", "f3ShgGroup"), ("F3-SHG-MIB", "f3ShgMemberPortGroup"), ("F3-SHG-MIB", "f3ShgMemberFlowGroup"), ("F3-SHG-MIB", "f3ShgMemberFlowPointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgCompliance = f3ShgCompliance.setStatus('current')
f3ShgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 1)).setObjects(("F3-SHG-MIB", "f3ShgAlias"), ("F3-SHG-MIB", "f3ShgStorageType"), ("F3-SHG-MIB", "f3ShgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgGroup = f3ShgGroup.setStatus('current')
f3ShgMemberPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 2)).setObjects(("F3-SHG-MIB", "f3ShgMemberPortStorageType"), ("F3-SHG-MIB", "f3ShgMemberPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgMemberPortGroup = f3ShgMemberPortGroup.setStatus('current')
f3ShgMemberFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 3)).setObjects(("F3-SHG-MIB", "f3ShgMemberFlow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgMemberFlowGroup = f3ShgMemberFlowGroup.setStatus('current')
f3ShgMemberFlowPointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 4)).setObjects(("F3-SHG-MIB", "f3ShgMemberFlowPoint"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgMemberFlowPointGroup = f3ShgMemberFlowPointGroup.setStatus('current')
mibBuilder.exportSymbols("F3-SHG-MIB", f3ShgConfigObjects=f3ShgConfigObjects, f3ShgMemberPortRowStatus=f3ShgMemberPortRowStatus, PYSNMP_MODULE_ID=f3SHGMIB, f3ShgMemberFlowGroup=f3ShgMemberFlowGroup, f3ShgMemberFlowPoint=f3ShgMemberFlowPoint, f3ShgMemberFlow=f3ShgMemberFlow, f3ShgConformance=f3ShgConformance, f3ShgMemberFlowTable=f3ShgMemberFlowTable, f3ShgCompliance=f3ShgCompliance, f3ShgMemberPortTable=f3ShgMemberPortTable, f3ShgMemberPortEntry=f3ShgMemberPortEntry, f3ShgRowStatus=f3ShgRowStatus, f3ShgMemberFlowPointGroup=f3ShgMemberFlowPointGroup, f3ShgCompliances=f3ShgCompliances, f3ShgGroup=f3ShgGroup, f3ShgMemberFlowEntry=f3ShgMemberFlowEntry, f3ShgEntry=f3ShgEntry, f3ShgAlias=f3ShgAlias, f3ShgMemberFlowPointEntry=f3ShgMemberFlowPointEntry, f3SHGMIB=f3SHGMIB, f3ShgMemberPortGroup=f3ShgMemberPortGroup, f3ShgIndex=f3ShgIndex, f3ShgStorageType=f3ShgStorageType, f3ShgTable=f3ShgTable, f3ShgMemberPort=f3ShgMemberPort, f3ShgMemberPortStorageType=f3ShgMemberPortStorageType, f3ShgMemberFlowPointTable=f3ShgMemberFlowPointTable, f3ShgGroups=f3ShgGroups)
