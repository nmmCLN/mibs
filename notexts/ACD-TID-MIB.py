#
# PySNMP MIB module ACD-TID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-TID-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:12 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Counter64, Unsigned32, Counter32, Integer32, MibIdentifier, NotificationType, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Counter64", "Unsigned32", "Counter32", "Integer32", "MibIdentifier", "NotificationType", "Bits", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acdTid = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 14))
acdTid.setRevisions(('2011-11-11 01:00',))
if mibBuilder.loadTexts: acdTid.setLastUpdated('201111110100Z')
if mibBuilder.loadTexts: acdTid.setOrganization('Accedian Networks, Inc.')
acdTidNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 0))
acdTidMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1))
acdTidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2))
acdTidGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1))
acdTidInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2))
class AcdTidType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("configuration", 1), ("status", 2))

acdTidCfgLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidCfgLastChangeTid.setStatus('current')
acdTidStatusLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidStatusLastChangeTid.setStatus('current')
acdTidInfoTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1), )
if mibBuilder.loadTexts: acdTidInfoTable.setStatus('current')
acdTidInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1), ).setIndexNames((0, "ACD-TID-MIB", "acdTidInfoIndex"))
if mibBuilder.loadTexts: acdTidInfoEntry.setStatus('current')
acdTidInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdTidInfoIndex.setStatus('current')
acdTidInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoOID.setStatus('current')
acdTidInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 3), AcdTidType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoType.setStatus('current')
acdTidInfoDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoDescr.setStatus('current')
acdTidInfoLastChangeTid = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoLastChangeTid.setStatus('current')
acdTidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1))
acdTidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2))
acdTidGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 1)).setObjects(("ACD-TID-MIB", "acdTidCfgLastChangeTid"), ("ACD-TID-MIB", "acdTidStatusLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidGeneralGroup = acdTidGeneralGroup.setStatus('current')
acdTidTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 2)).setObjects(("ACD-TID-MIB", "acdTidInfoOID"), ("ACD-TID-MIB", "acdTidInfoType"), ("ACD-TID-MIB", "acdTidInfoDescr"), ("ACD-TID-MIB", "acdTidInfoLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidTableGroup = acdTidTableGroup.setStatus('current')
acdTidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1, 1)).setObjects(("ACD-TID-MIB", "acdTidGeneralGroup"), ("ACD-TID-MIB", "acdTidTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidCompliance = acdTidCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-TID-MIB", acdTidInfoLastChangeTid=acdTidInfoLastChangeTid, acdTidInfoDescr=acdTidInfoDescr, acdTidInfoTable=acdTidInfoTable, acdTidCfgLastChangeTid=acdTidCfgLastChangeTid, acdTidInfoEntry=acdTidInfoEntry, acdTidMIBObjects=acdTidMIBObjects, acdTidInfoType=acdTidInfoType, acdTidNotifications=acdTidNotifications, acdTid=acdTid, AcdTidType=AcdTidType, acdTidGroups=acdTidGroups, acdTidCompliance=acdTidCompliance, acdTidInfoIndex=acdTidInfoIndex, acdTidGeneral=acdTidGeneral, acdTidInfoOID=acdTidInfoOID, acdTidStatusLastChangeTid=acdTidStatusLastChangeTid, acdTidGeneralGroup=acdTidGeneralGroup, acdTidConformance=acdTidConformance, PYSNMP_MODULE_ID=acdTid, acdTidCompliances=acdTidCompliances, acdTidTableGroup=acdTidTableGroup, acdTidInfo=acdTidInfo)
