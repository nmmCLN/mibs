#
# PySNMP MIB module NBS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-STATS-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:05:51 2023
# On host fv-az1114-438 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32, TimeTicks, Unsigned32, Counter32, ModuleIdentity, IpAddress, Gauge32, MibIdentifier, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32", "TimeTicks", "Unsigned32", "Counter32", "ModuleIdentity", "IpAddress", "Gauge32", "MibIdentifier", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsStatsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 233))
if mibBuilder.loadTexts: nbsStatsMib.setLastUpdated('201303130000Z')
if mibBuilder.loadTexts: nbsStatsMib.setOrganization('NBS')
nbsStatInfoGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 233, 1))
if mibBuilder.loadTexts: nbsStatInfoGrp.setStatus('current')
nbsStatInfoTable = MibTable((1, 3, 6, 1, 4, 1, 629, 233, 1, 10), )
if mibBuilder.loadTexts: nbsStatInfoTable.setStatus('current')
nbsStatInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1), ).setIndexNames((0, "NBS-STATS-MIB", "nbsStatInfoIndex"))
if mibBuilder.loadTexts: nbsStatInfoEntry.setStatus('current')
nbsStatInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsStatInfoIndex.setStatus('current')
nbsStatInfoCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoCounters.setStatus('current')
nbsStatInfoPmData = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoPmData.setStatus('current')
mibBuilder.exportSymbols("NBS-STATS-MIB", nbsStatInfoIndex=nbsStatInfoIndex, nbsStatsMib=nbsStatsMib, nbsStatInfoCounters=nbsStatInfoCounters, nbsStatInfoPmData=nbsStatInfoPmData, nbsStatInfoGrp=nbsStatInfoGrp, nbsStatInfoTable=nbsStatInfoTable, nbsStatInfoEntry=nbsStatInfoEntry, PYSNMP_MODULE_ID=nbsStatsMib)
