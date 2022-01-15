#
# PySNMP MIB module NBS-JUMPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-JUMPER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:28:03 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, Counter64, TimeTicks, Counter32, ModuleIdentity, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, ObjectIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "ObjectIdentity", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NBS-JUMPER-MIB", nbsJumperTable=nbsJumperTable, nbsJumperInterpret=nbsJumperInterpret, nbsJumperMib=nbsJumperMib, nbsJumperIndex=nbsJumperIndex, nbsJumperSilkScreen=nbsJumperSilkScreen, PYSNMP_MODULE_ID=nbsJumperMib, nbsJumperTableSize=nbsJumperTableSize, nbsJumperIfIndex=nbsJumperIfIndex, nbsJumperGrp=nbsJumperGrp, nbsJumperDescription=nbsJumperDescription, nbsJumperEntry=nbsJumperEntry, nbsJumperPosition=nbsJumperPosition)
