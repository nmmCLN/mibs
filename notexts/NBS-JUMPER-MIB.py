#
# PySNMP MIB module NBS-JUMPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-JUMPER-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:31:32 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ModuleIdentity, TimeTicks, iso, Unsigned32, Integer32, IpAddress, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ModuleIdentity", "TimeTicks", "iso", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsJumperMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 210))
if mibBuilder.loadTexts: nbsJumperMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsJumperMib.setOrganization('NBS')
nbsJumperGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 210, 1))
if mibBuilder.loadTexts: nbsJumperGrp.setStatus('current')
nbsJumperTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 210, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperTableSize.setStatus('current')
nbsJumperTable = MibTable((1, 3, 6, 1, 4, 1, 629, 210, 1, 2), )
if mibBuilder.loadTexts: nbsJumperTable.setStatus('current')
nbsJumperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1), ).setIndexNames((0, "NBS-JUMPER-MIB", "nbsJumperIfIndex"), (0, "NBS-JUMPER-MIB", "nbsJumperIndex"))
if mibBuilder.loadTexts: nbsJumperEntry.setStatus('current')
nbsJumperIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsJumperIfIndex.setStatus('current')
nbsJumperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsJumperIndex.setStatus('current')
nbsJumperPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("off", 2), ("on", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperPosition.setStatus('current')
nbsJumperInterpret = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperInterpret.setStatus('current')
nbsJumperSilkScreen = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperSilkScreen.setStatus('current')
nbsJumperDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperDescription.setStatus('current')
mibBuilder.exportSymbols("NBS-JUMPER-MIB", nbsJumperDescription=nbsJumperDescription, nbsJumperInterpret=nbsJumperInterpret, nbsJumperIfIndex=nbsJumperIfIndex, nbsJumperMib=nbsJumperMib, nbsJumperPosition=nbsJumperPosition, PYSNMP_MODULE_ID=nbsJumperMib, nbsJumperSilkScreen=nbsJumperSilkScreen, nbsJumperEntry=nbsJumperEntry, nbsJumperIndex=nbsJumperIndex, nbsJumperTableSize=nbsJumperTableSize, nbsJumperTable=nbsJumperTable, nbsJumperGrp=nbsJumperGrp)
