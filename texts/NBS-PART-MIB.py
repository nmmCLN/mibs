#
# PySNMP MIB module NBS-PART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-PART-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:11 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, NbsTcPartIndex = mibBuilder.importSymbols("NBS-MIB", "nbs", "NbsTcPartIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, Bits, ObjectIdentity, TimeTicks, Counter64, Counter32, iso, IpAddress, MibIdentifier, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Bits", "ObjectIdentity", "TimeTicks", "Counter64", "Counter32", "iso", "IpAddress", "MibIdentifier", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsPartMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 231))
if mibBuilder.loadTexts: nbsPartMib.setLastUpdated('201503090000Z')
if mibBuilder.loadTexts: nbsPartMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsPartMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsPartMib.setDescription('Identification and programming of field-serviceable components.')
nbsPartHardGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 231, 1))
if mibBuilder.loadTexts: nbsPartHardGrp.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardGrp.setDescription('Information common to most system hardware components')
nbsPartFirmGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 231, 2))
if mibBuilder.loadTexts: nbsPartFirmGrp.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmGrp.setDescription('Firmware information for system components')
nbsPartProgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 231, 3))
if mibBuilder.loadTexts: nbsPartProgGrp.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgGrp.setDescription('Reprogrammable system components')
nbsPartHardTable = MibTable((1, 3, 6, 1, 4, 1, 629, 231, 1, 1), )
if mibBuilder.loadTexts: nbsPartHardTable.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardTable.setDescription('Attributes shared by most system hardware components.')
nbsPartHardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1), ).setIndexNames((0, "NBS-PART-MIB", "nbsPartHardIfIndex"), (0, "NBS-PART-MIB", "nbsPartHardPartIndex"))
if mibBuilder.loadTexts: nbsPartHardEntry.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardEntry.setDescription('Contains a description of a particular component')
nbsPartHardIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsPartHardIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardIfIndex.setDescription('If this part is a chassis, card, or port, this object is its\n        own mib2-like ifIndex.\n\n        If this is any other kind of part, this object is the ifIndex\n        of the chassis, card, or port of which it is a component.')
nbsPartHardPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 2), NbsTcPartIndex())
if mibBuilder.loadTexts: nbsPartHardPartIndex.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardPartIndex.setDescription('Unique ID of this component within scope of nbsPartHardIfIndex')
nbsPartHardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardDescription.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardDescription.setDescription('Human-readable identification of this part, including location')
nbsPartHardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardSerialNumber.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardSerialNumber.setDescription('Factory assigned unique identifier.')
nbsPartHardProductionId = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardProductionId.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardProductionId.setDescription("The 'Top Assembly Number' used in internal tracking")
nbsPartHardVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardVendor.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardVendor.setDescription('The manufacturer of this component')
nbsPartHardModel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardModel.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardModel.setDescription('Factory assigned model name/number.')
nbsPartHardWareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartHardWareRev.setStatus('current')
if mibBuilder.loadTexts: nbsPartHardWareRev.setDescription('The Hardware Revision number of this component.')
nbsPartFirmTable = MibTable((1, 3, 6, 1, 4, 1, 629, 231, 2, 1), )
if mibBuilder.loadTexts: nbsPartFirmTable.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmTable.setDescription('Firmware information for this part.')
nbsPartFirmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1), ).setIndexNames((0, "NBS-PART-MIB", "nbsPartFirmIfIndex"), (0, "NBS-PART-MIB", "nbsPartFirmPartIndex"))
if mibBuilder.loadTexts: nbsPartFirmEntry.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmEntry.setDescription('Contains a description of a particular entity')
nbsPartFirmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsPartFirmIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmIfIndex.setDescription('If this part is a chassis, card, or port, this object is its\n        own mib2-like ifIndex.\n\n        If this is any other kind of part, this object is the ifIndex\n        of the chassis, card, or port of which it is a component.')
nbsPartFirmPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 2), NbsTcPartIndex())
if mibBuilder.loadTexts: nbsPartFirmPartIndex.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmPartIndex.setDescription('Unique ID of this component within scope of nbsPartFirmIfIndex')
nbsPartFirmFpgaRev = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmFpgaRev.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmFpgaRev.setDescription('The Firmware/FPGA Revision running on this component.')
nbsPartFirmSwMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmSwMajor.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmSwMajor.setDescription('The Major Revision Number of the software running on this\n        component.\n\n        Not Supported value: -1')
nbsPartFirmSwMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmSwMinor.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmSwMinor.setDescription('The Minor Revision Number of the software running on this\n        component.\n\n        Not Supported value: -1')
nbsPartFirmSwBuild = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmSwBuild.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmSwBuild.setDescription('The Build Number of the software running on this component.\n\n        Not Supported value: -1')
nbsPartFirmWareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartFirmWareIndex.setStatus('current')
if mibBuilder.loadTexts: nbsPartFirmWareIndex.setDescription('The nbsCmmcSysFirmwareIndex of the firmware currently loaded.\n\n        Not Supported value: -1')
nbsPartProgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 231, 3, 1), )
if mibBuilder.loadTexts: nbsPartProgTable.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgTable.setDescription('A table that describes reprogrammable components.')
nbsPartProgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1), ).setIndexNames((0, "NBS-PART-MIB", "nbsPartProgIfIndex"), (0, "NBS-PART-MIB", "nbsPartProgPartIndex"))
if mibBuilder.loadTexts: nbsPartProgEntry.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgEntry.setDescription('Firmware of a particular reprogrammable component')
nbsPartProgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsPartProgIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgIfIndex.setDescription('If this part is a chassis, card, or port, this object is its\n        own mib2-like ifIndex.\n\n        If this is any other kind of part, this object is the ifIndex\n        of the chassis, card, or port of which it is a component.')
nbsPartProgPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 2), NbsTcPartIndex())
if mibBuilder.loadTexts: nbsPartProgPartIndex.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgPartIndex.setDescription('Unique ID of this component within scope of nbsPartProgIfIndex')
nbsPartProgFirmwareCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgFirmwareCaps.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgFirmwareCaps.setDescription('See nbsCmmcSlotFirmwareCaps.')
nbsPartProgFirmwareLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsPartProgFirmwareLoad.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgFirmwareLoad.setDescription('See nbsCmmcSlotFirmwareLoad')
nbsPartProgLoader = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgLoader.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgLoader.setDescription('See nbsCmmcSlotLoader')
nbsPartProgNVAreaAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsPartProgNVAreaAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgNVAreaAdmin.setDescription('See nbsCmmcSlotNVAreaAdmin')
nbsPartProgNVAreaOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 23), Integer32().clone(-1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgNVAreaOper.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgNVAreaOper.setDescription('See nbsCmmcSlotNVAreaOper')
nbsPartProgNVAreaStart = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgNVAreaStart.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgNVAreaStart.setDescription("The nbsCmmcSysNVAreaBank of this component's bank 1.")
nbsPartProgNVAreaBanks = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsPartProgNVAreaBanks.setStatus('current')
if mibBuilder.loadTexts: nbsPartProgNVAreaBanks.setDescription('The number of NVAreaBanks on this component.')
mibBuilder.exportSymbols("NBS-PART-MIB", nbsPartProgNVAreaOper=nbsPartProgNVAreaOper, nbsPartHardProductionId=nbsPartHardProductionId, nbsPartFirmWareIndex=nbsPartFirmWareIndex, nbsPartProgFirmwareLoad=nbsPartProgFirmwareLoad, nbsPartProgNVAreaStart=nbsPartProgNVAreaStart, nbsPartFirmSwBuild=nbsPartFirmSwBuild, nbsPartProgLoader=nbsPartProgLoader, nbsPartProgPartIndex=nbsPartProgPartIndex, nbsPartFirmGrp=nbsPartFirmGrp, nbsPartProgGrp=nbsPartProgGrp, nbsPartHardSerialNumber=nbsPartHardSerialNumber, nbsPartFirmEntry=nbsPartFirmEntry, nbsPartFirmTable=nbsPartFirmTable, nbsPartProgTable=nbsPartProgTable, nbsPartHardGrp=nbsPartHardGrp, nbsPartHardWareRev=nbsPartHardWareRev, nbsPartProgNVAreaAdmin=nbsPartProgNVAreaAdmin, nbsPartFirmIfIndex=nbsPartFirmIfIndex, PYSNMP_MODULE_ID=nbsPartMib, nbsPartMib=nbsPartMib, nbsPartFirmPartIndex=nbsPartFirmPartIndex, nbsPartFirmSwMajor=nbsPartFirmSwMajor, nbsPartProgEntry=nbsPartProgEntry, nbsPartProgNVAreaBanks=nbsPartProgNVAreaBanks, nbsPartFirmSwMinor=nbsPartFirmSwMinor, nbsPartProgIfIndex=nbsPartProgIfIndex, nbsPartHardModel=nbsPartHardModel, nbsPartHardEntry=nbsPartHardEntry, nbsPartHardIfIndex=nbsPartHardIfIndex, nbsPartFirmFpgaRev=nbsPartFirmFpgaRev, nbsPartHardPartIndex=nbsPartHardPartIndex, nbsPartHardVendor=nbsPartHardVendor, nbsPartHardDescription=nbsPartHardDescription, nbsPartProgFirmwareCaps=nbsPartProgFirmwareCaps, nbsPartHardTable=nbsPartHardTable)
