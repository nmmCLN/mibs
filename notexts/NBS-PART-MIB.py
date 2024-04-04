#
# PySNMP MIB module NBS-PART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-PART-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:09 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NbsTcPartIndex, nbs = mibBuilder.importSymbols("NBS-MIB", "NbsTcPartIndex", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, Gauge32, Unsigned32, Integer32, TimeTicks, IpAddress, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "Gauge32", "Unsigned32", "Integer32", "TimeTicks", "IpAddress", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsPartMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 231))
if mibBuilder.loadTexts: nbsPartMib.setLastUpdated('201503090000Z')
if mibBuilder.loadTexts: nbsPartMib.setOrganization('NBS')
nbsPartHardGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 231, 1))
if mibBuilder.loadTexts: nbsPartHardGrp.setStatus('current')
nbsPartFirmGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 231, 2))
if mibBuilder.loadTexts: nbsPartFirmGrp.setStatus('current')
nbsPartProgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 231, 3))
if mibBuilder.loadTexts: nbsPartProgGrp.setStatus('current')
nbsPartHardTable = MibTable((1, 3, 6, 1, 4, 1, 629, 231, 1, 1), )
if mibBuilder.loadTexts: nbsPartHardTable.setStatus('current')
nbsPartHardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1), ).setIndexNames((0, "NBS-PART-MIB", "nbsPartHardIfIndex"), (0, "NBS-PART-MIB", "nbsPartHardPartIndex"))
if mibBuilder.loadTexts: nbsPartHardEntry.setStatus('current')
nbsPartHardIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsPartHardIfIndex.setStatus('current')
nbsPartHardPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 2), NbsTcPartIndex())
if mibBuilder.loadTexts: nbsPartHardPartIndex.setStatus('current')
nbsPartHardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardDescription.setStatus('current')
nbsPartHardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardSerialNumber.setStatus('current')
nbsPartHardProductionId = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardProductionId.setStatus('current')
nbsPartHardVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardVendor.setStatus('current')
nbsPartHardModel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardModel.setStatus('current')
nbsPartHardWareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardWareRev.setStatus('current')
nbsPartFirmTable = MibTable((1, 3, 6, 1, 4, 1, 629, 231, 2, 1), )
if mibBuilder.loadTexts: nbsPartFirmTable.setStatus('current')
nbsPartFirmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1), ).setIndexNames((0, "NBS-PART-MIB", "nbsPartFirmIfIndex"), (0, "NBS-PART-MIB", "nbsPartFirmPartIndex"))
if mibBuilder.loadTexts: nbsPartFirmEntry.setStatus('current')
nbsPartFirmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsPartFirmIfIndex.setStatus('current')
nbsPartFirmPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 2), NbsTcPartIndex())
if mibBuilder.loadTexts: nbsPartFirmPartIndex.setStatus('current')
nbsPartFirmFpgaRev = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmFpgaRev.setStatus('current')
nbsPartFirmSwMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmSwMajor.setStatus('current')
nbsPartFirmSwMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmSwMinor.setStatus('current')
nbsPartFirmSwBuild = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmSwBuild.setStatus('current')
nbsPartFirmWareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmWareIndex.setStatus('current')
nbsPartProgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 231, 3, 1), )
if mibBuilder.loadTexts: nbsPartProgTable.setStatus('current')
nbsPartProgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1), ).setIndexNames((0, "NBS-PART-MIB", "nbsPartProgIfIndex"), (0, "NBS-PART-MIB", "nbsPartProgPartIndex"))
if mibBuilder.loadTexts: nbsPartProgEntry.setStatus('current')
nbsPartProgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsPartProgIfIndex.setStatus('current')
nbsPartProgPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 2), NbsTcPartIndex())
if mibBuilder.loadTexts: nbsPartProgPartIndex.setStatus('current')
nbsPartProgFirmwareCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgFirmwareCaps.setStatus('current')
nbsPartProgFirmwareLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsPartProgFirmwareLoad.setStatus('current')
nbsPartProgLoader = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgLoader.setStatus('current')
nbsPartProgNVAreaAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsPartProgNVAreaAdmin.setStatus('current')
nbsPartProgNVAreaOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 23), Integer32().clone(-1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgNVAreaOper.setStatus('current')
nbsPartProgNVAreaStart = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgNVAreaStart.setStatus('current')
nbsPartProgNVAreaBanks = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgNVAreaBanks.setStatus('current')
mibBuilder.exportSymbols("NBS-PART-MIB", nbsPartHardDescription=nbsPartHardDescription, nbsPartFirmIfIndex=nbsPartFirmIfIndex, nbsPartFirmFpgaRev=nbsPartFirmFpgaRev, nbsPartFirmTable=nbsPartFirmTable, nbsPartFirmGrp=nbsPartFirmGrp, nbsPartFirmPartIndex=nbsPartFirmPartIndex, nbsPartHardProductionId=nbsPartHardProductionId, nbsPartProgGrp=nbsPartProgGrp, nbsPartFirmEntry=nbsPartFirmEntry, nbsPartHardVendor=nbsPartHardVendor, nbsPartProgPartIndex=nbsPartProgPartIndex, nbsPartProgNVAreaOper=nbsPartProgNVAreaOper, nbsPartHardEntry=nbsPartHardEntry, nbsPartProgNVAreaBanks=nbsPartProgNVAreaBanks, nbsPartFirmSwMinor=nbsPartFirmSwMinor, nbsPartHardTable=nbsPartHardTable, PYSNMP_MODULE_ID=nbsPartMib, nbsPartProgLoader=nbsPartProgLoader, nbsPartHardIfIndex=nbsPartHardIfIndex, nbsPartProgEntry=nbsPartProgEntry, nbsPartFirmWareIndex=nbsPartFirmWareIndex, nbsPartFirmSwMajor=nbsPartFirmSwMajor, nbsPartFirmSwBuild=nbsPartFirmSwBuild, nbsPartProgTable=nbsPartProgTable, nbsPartHardGrp=nbsPartHardGrp, nbsPartProgFirmwareCaps=nbsPartProgFirmwareCaps, nbsPartProgNVAreaAdmin=nbsPartProgNVAreaAdmin, nbsPartHardPartIndex=nbsPartHardPartIndex, nbsPartMib=nbsPartMib, nbsPartHardWareRev=nbsPartHardWareRev, nbsPartHardModel=nbsPartHardModel, nbsPartProgIfIndex=nbsPartProgIfIndex, nbsPartHardSerialNumber=nbsPartHardSerialNumber, nbsPartProgFirmwareLoad=nbsPartProgFirmwareLoad, nbsPartProgNVAreaStart=nbsPartProgNVAreaStart)
