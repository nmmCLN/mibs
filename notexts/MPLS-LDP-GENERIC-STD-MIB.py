#
# PySNMP MIB module MPLS-LDP-GENERIC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-LDP-GENERIC-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
mplsLdpEntityLdpId, mplsLdpEntityIndex = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId", "mplsLdpEntityIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, RowStatus, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "StorageType")
mplsLdpGenericStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 7))
mplsLdpGenericStdMIB.setRevisions(('2004-06-03 00:00',))
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setOrganization('Multiprotocol Label Switching (mpls) Working Group')
mplsLdpGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1))
mplsLdpGenericConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2))
mplsLdpEntityGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1))
mplsLdpEntityGenericLRTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1), )
if mibBuilder.loadTexts: mplsLdpEntityGenericLRTable.setStatus('current')
mplsLdpEntityGenericLREntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1), ).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMin"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMax"))
if mibBuilder.loadTexts: mplsLdpEntityGenericLREntry.setStatus('current')
mplsLdpEntityGenericLRMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMin.setStatus('current')
mplsLdpEntityGenericLRMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMax.setStatus('current')
mplsLdpEntityGenericLabelSpace = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("perPlatform", 1), ("perInterface", 2))).clone('perPlatform')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLabelSpace.setStatus('current')
mplsLdpEntityGenericIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericIfIndexOrZero.setStatus('current')
mplsLdpEntityGenericLRStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRStorageType.setStatus('current')
mplsLdpEntityGenericLRRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRRowStatus.setStatus('current')
mplsLdpGenericGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1))
mplsLdpGenericCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2))
mplsLdpGenericModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 1)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericModuleFullCompliance = mplsLdpGenericModuleFullCompliance.setStatus('current')
mplsLdpGenericModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 2)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericModuleReadOnlyCompliance = mplsLdpGenericModuleReadOnlyCompliance.setStatus('current')
mplsLdpGenericGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1, 1)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLabelSpace"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericIfIndexOrZero"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRStorageType"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericGroup = mplsLdpGenericGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LDP-GENERIC-STD-MIB", mplsLdpEntityGenericIfIndexOrZero=mplsLdpEntityGenericIfIndexOrZero, mplsLdpEntityGenericLRMin=mplsLdpEntityGenericLRMin, mplsLdpGenericGroups=mplsLdpGenericGroups, mplsLdpEntityGenericObjects=mplsLdpEntityGenericObjects, mplsLdpEntityGenericLRRowStatus=mplsLdpEntityGenericLRRowStatus, mplsLdpGenericGroup=mplsLdpGenericGroup, mplsLdpEntityGenericLRStorageType=mplsLdpEntityGenericLRStorageType, mplsLdpGenericModuleReadOnlyCompliance=mplsLdpGenericModuleReadOnlyCompliance, mplsLdpGenericConformance=mplsLdpGenericConformance, mplsLdpGenericStdMIB=mplsLdpGenericStdMIB, mplsLdpEntityGenericLRTable=mplsLdpEntityGenericLRTable, PYSNMP_MODULE_ID=mplsLdpGenericStdMIB, mplsLdpEntityGenericLREntry=mplsLdpEntityGenericLREntry, mplsLdpGenericCompliances=mplsLdpGenericCompliances, mplsLdpEntityGenericLRMax=mplsLdpEntityGenericLRMax, mplsLdpGenericModuleFullCompliance=mplsLdpGenericModuleFullCompliance, mplsLdpEntityGenericLabelSpace=mplsLdpEntityGenericLabelSpace, mplsLdpGenericObjects=mplsLdpGenericObjects)
