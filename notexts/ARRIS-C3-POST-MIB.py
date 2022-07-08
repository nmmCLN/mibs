#
# PySNMP MIB module ARRIS-C3-POST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-POST-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:05 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Unsigned32, NotificationType, Counter64, Integer32, TimeTicks, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Unsigned32", "NotificationType", "Counter64", "Integer32", "TimeTicks", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmtsC3POSTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13))
if mibBuilder.loadTexts: cmtsC3POSTMIB.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: cmtsC3POSTMIB.setOrganization('Arris International')
dcxPOSTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1))
dcxCPUWANPOSTGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1))
dcxCPUWANPOSTTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1), )
if mibBuilder.loadTexts: dcxCPUWANPOSTTable.setStatus('current')
dcxCPUWANPOSTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1), ).setIndexNames((0, "ARRIS-C3-POST-MIB", "dcxCPUWANPOSTType"))
if mibBuilder.loadTexts: dcxCPUWANPOSTEntry.setStatus('current')
dcxCPUWANPOSTType = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)))
if mibBuilder.loadTexts: dcxCPUWANPOSTType.setStatus('current')
dcxCPUWANPOSTDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxCPUWANPOSTDescr.setStatus('current')
dcxCPUWANPOSTResult = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("passed", 0), ("skipped", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxCPUWANPOSTResult.setStatus('current')
dcx3212POSTGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2))
dcx3212POSTTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1), )
if mibBuilder.loadTexts: dcx3212POSTTable.setStatus('current')
dcx3212POSTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1), ).setIndexNames((0, "ARRIS-C3-POST-MIB", "dcx3212POSTType"))
if mibBuilder.loadTexts: dcx3212POSTEntry.setStatus('current')
dcx3212POSTType = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)))
if mibBuilder.loadTexts: dcx3212POSTType.setStatus('current')
dcx3212POSTDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcx3212POSTDescr.setStatus('current')
dcx3212POSTResult = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("passed", 0), ("failed", 1), ("skipped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcx3212POSTResult.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-POST-MIB", dcx3212POSTGroup=dcx3212POSTGroup, PYSNMP_MODULE_ID=cmtsC3POSTMIB, dcxCPUWANPOSTDescr=dcxCPUWANPOSTDescr, dcx3212POSTTable=dcx3212POSTTable, dcxCPUWANPOSTGroup=dcxCPUWANPOSTGroup, dcxCPUWANPOSTEntry=dcxCPUWANPOSTEntry, dcxCPUWANPOSTType=dcxCPUWANPOSTType, dcxCPUWANPOSTTable=dcxCPUWANPOSTTable, dcxPOSTObjects=dcxPOSTObjects, dcx3212POSTType=dcx3212POSTType, dcxCPUWANPOSTResult=dcxCPUWANPOSTResult, dcx3212POSTResult=dcx3212POSTResult, dcx3212POSTEntry=dcx3212POSTEntry, cmtsC3POSTMIB=cmtsC3POSTMIB, dcx3212POSTDescr=dcx3212POSTDescr)
