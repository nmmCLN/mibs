#
# PySNMP MIB module NBS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-STATS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:23 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter32, ObjectIdentity, Counter64, Gauge32, IpAddress, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "Gauge32", "IpAddress", "ModuleIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsStatsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 233))
if mibBuilder.loadTexts: nbsStatsMib.setLastUpdated('201303130000Z')
if mibBuilder.loadTexts: nbsStatsMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsStatsMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsStatsMib.setDescription('For managing statistics')
nbsStatInfoGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 233, 1))
if mibBuilder.loadTexts: nbsStatInfoGrp.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoGrp.setDescription('')
nbsStatInfoTable = MibTable((1, 3, 6, 1, 4, 1, 629, 233, 1, 10), )
if mibBuilder.loadTexts: nbsStatInfoTable.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoTable.setDescription('A table that provides basic control information for entity\n        (typically ports) statistics.')
nbsStatInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1), ).setIndexNames((0, "NBS-STATS-MIB", "nbsStatInfoIndex"))
if mibBuilder.loadTexts: nbsStatInfoEntry.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoEntry.setDescription('Contains a description of a particular statistics entity')
nbsStatInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsStatInfoIndex.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoIndex.setDescription('ifIndex-like identifier of a component that has statistics.')
nbsStatInfoCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoCounters.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoCounters.setDescription('Used to clear all entity-specific counters to zero.\n        Aliased/Equivalent to NBS-CMMC-MIB CountersState objects.')
nbsStatInfoPmData = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoPmData.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoPmData.setDescription('Used to clear all entity-specific performance monitoring (PM) data\n        to zero. Examples include: nbsFecpmCurrentTable, nbsFecpmHistoricTable,\n        nbsFecpmRunningTable, nbsOtnpmCurrentTable, nbsOtnpmHistoricTable, and\n        nbsOtnpmRunningTable.')
mibBuilder.exportSymbols("NBS-STATS-MIB", nbsStatInfoEntry=nbsStatInfoEntry, nbsStatInfoPmData=nbsStatInfoPmData, nbsStatsMib=nbsStatsMib, nbsStatInfoIndex=nbsStatInfoIndex, nbsStatInfoCounters=nbsStatInfoCounters, nbsStatInfoTable=nbsStatInfoTable, nbsStatInfoGrp=nbsStatInfoGrp, PYSNMP_MODULE_ID=nbsStatsMib)
