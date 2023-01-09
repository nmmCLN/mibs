#
# PySNMP MIB module NBS-OTNOH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-OTNOH-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:22 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, Unsigned32, IpAddress, Integer32, NotificationType, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
nbsOtnohMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 224))
if mibBuilder.loadTexts: nbsOtnohMib.setLastUpdated('201212200000Z')
if mibBuilder.loadTexts: nbsOtnohMib.setOrganization('NBS')
nbsOtnohTtiGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 224, 1))
if mibBuilder.loadTexts: nbsOtnohTtiGrp.setStatus('current')
nbsOtnohTtiTable = MibTable((1, 3, 6, 1, 4, 1, 629, 224, 1, 1), )
if mibBuilder.loadTexts: nbsOtnohTtiTable.setStatus('current')
nbsOtnohTtiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1), ).setIndexNames((0, "NBS-OTNOH-MIB", "nbsOtnohTtiIfIndex"), (0, "NBS-OTNOH-MIB", "nbsOtnohTtiScope"))
if mibBuilder.loadTexts: nbsOtnohTtiEntry.setStatus('current')
nbsOtnohTtiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsOtnohTtiIfIndex.setStatus('current')
nbsOtnohTtiScope = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("tcm1", 1), ("tcm2", 2), ("tcm3", 3), ("tcm4", 4), ("tcm5", 5), ("tcm6", 6), ("section", 7), ("path", 8))))
if mibBuilder.loadTexts: nbsOtnohTtiScope.setStatus('current')
nbsOtnohTtiSendSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiSendSapi.setStatus('current')
nbsOtnohTtiSendDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiSendDapi.setStatus('current')
nbsOtnohTtiSendOpSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiSendOpSpec.setStatus('current')
nbsOtnohTtiExpectSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiExpectSapi.setStatus('current')
nbsOtnohTtiExpectDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiExpectDapi.setStatus('current')
nbsOtnohTtiExpectOpSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiExpectOpSpec.setStatus('current')
nbsOtnohTtiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiRowStatus.setStatus('current')
mibBuilder.exportSymbols("NBS-OTNOH-MIB", nbsOtnohMib=nbsOtnohMib, nbsOtnohTtiExpectDapi=nbsOtnohTtiExpectDapi, nbsOtnohTtiScope=nbsOtnohTtiScope, nbsOtnohTtiRowStatus=nbsOtnohTtiRowStatus, nbsOtnohTtiExpectOpSpec=nbsOtnohTtiExpectOpSpec, nbsOtnohTtiIfIndex=nbsOtnohTtiIfIndex, nbsOtnohTtiSendOpSpec=nbsOtnohTtiSendOpSpec, nbsOtnohTtiSendSapi=nbsOtnohTtiSendSapi, nbsOtnohTtiEntry=nbsOtnohTtiEntry, nbsOtnohTtiGrp=nbsOtnohTtiGrp, nbsOtnohTtiExpectSapi=nbsOtnohTtiExpectSapi, PYSNMP_MODULE_ID=nbsOtnohMib, nbsOtnohTtiTable=nbsOtnohTtiTable, nbsOtnohTtiSendDapi=nbsOtnohTtiSendDapi)
