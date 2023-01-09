#
# PySNMP MIB module HM800MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hitachi/HM800MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:31:07 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, Gauge32, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, IpAddress, enterprises, iso, Integer32, Unsigned32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Gauge32", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "IpAddress", "enterprises", "iso", "Integer32", "Unsigned32", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hitachi = MibIdentifier((1, 3, 6, 1, 4, 1, 116))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3))
storage = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3, 11))
raid = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3, 11, 4))
raidDummy = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1))
raidRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1))
systemExMib = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5))
storageExMib = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11))
raidExMib = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 4))
raidExMibDummy = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1))
raidExMibDummyX = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2))
raidExMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1))
raidExMibName = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidExMibName.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibName.setDescription('Product name of the SVP.')
raidExMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidExMibVersion.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibVersion.setDescription('SVP micro-program version.')
raidExMibAgentVersion = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidExMibAgentVersion.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibAgentVersion.setDescription('Extension Agent version.')
raidExMibDkcCount = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidExMibDkcCount.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibDkcCount.setDescription('Number of DKC which is registered on the SVP.')
raidExMibRaidListTable = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5), )
if mibBuilder.loadTexts: raidExMibRaidListTable.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibRaidListTable.setDescription('List of DKC which is registered on the SVP.')
raidExMibRaidListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1), ).setIndexNames((0, "HM800MIB", "raidlistSerialNumber"))
if mibBuilder.loadTexts: raidExMibRaidListEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibRaidListEntry.setDescription('Entry of DKC list.')
raidlistSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidlistSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: raidlistSerialNumber.setDescription('Serial Number of the DKC.')
raidlistMibNickName = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidlistMibNickName.setStatus('mandatory')
if mibBuilder.loadTexts: raidlistMibNickName.setDescription('Nickname of the DKC.')
raidlistDKCMainVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidlistDKCMainVersion.setStatus('mandatory')
if mibBuilder.loadTexts: raidlistDKCMainVersion.setDescription('DKC Firmware Version.')
raidlistDKCProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidlistDKCProductName.setStatus('mandatory')
if mibBuilder.loadTexts: raidlistDKCProductName.setDescription('DKC Product Name.')
raidExMibDKCHWTable = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6), )
if mibBuilder.loadTexts: raidExMibDKCHWTable.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibDKCHWTable.setDescription('Error information of the DKC.')
raidExMibDKCHWEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1), ).setIndexNames((0, "HM800MIB", "dkcRaidListIndexSerialNumber"))
if mibBuilder.loadTexts: raidExMibDKCHWEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibDKCHWEntry.setDescription('Entry of DKC information.')
dkcRaidListIndexSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcRaidListIndexSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dkcRaidListIndexSerialNumber.setDescription('Serial Number the DKC.')
dkcHWProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWProcessor.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWProcessor.setDescription('Information of processor.')
dkcHWCSW = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWCSW.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWCSW.setDescription('Information of internal bus.')
dkcHWCache = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWCache.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWCache.setDescription('Information of cache.')
dkcHWSM = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWSM.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWSM.setDescription('Information of shared memory.')
dkcHWPS = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWPS.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWPS.setDescription('Information of power supply.')
dkcHWBattery = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWBattery.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWBattery.setDescription('Information of battery.')
dkcHWFan = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWFan.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWFan.setDescription('Information of fan.')
dkcHWEnvironment = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkcHWEnvironment.setStatus('mandatory')
if mibBuilder.loadTexts: dkcHWEnvironment.setDescription('Information of Environment.')
raidExMibDKUHWTable = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7), )
if mibBuilder.loadTexts: raidExMibDKUHWTable.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibDKUHWTable.setDescription('Error information of the DKU.')
raidExMibDKUHWEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1), ).setIndexNames((0, "HM800MIB", "dkuRaidListIndexSerialNumber"))
if mibBuilder.loadTexts: raidExMibDKUHWEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibDKUHWEntry.setDescription('Entry of DKU information.')
dkuRaidListIndexSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkuRaidListIndexSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dkuRaidListIndexSerialNumber.setDescription('Serial Number of the DKC.')
dkuHWPS = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkuHWPS.setStatus('mandatory')
if mibBuilder.loadTexts: dkuHWPS.setDescription('Information of DKU power supply.')
dkuHWFan = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkuHWFan.setStatus('mandatory')
if mibBuilder.loadTexts: dkuHWFan.setDescription('Information of DKU fan.')
dkuHWEnvironment = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkuHWEnvironment.setStatus('mandatory')
if mibBuilder.loadTexts: dkuHWEnvironment.setDescription('Information of DKU Environment.')
dkuHWDrive = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noError", 1), ("acute", 2), ("serious", 3), ("moderate", 4), ("service", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dkuHWDrive.setStatus('mandatory')
if mibBuilder.loadTexts: dkuHWDrive.setDescription('Information of Drive.')
raidExMibTrapListTable = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8), )
if mibBuilder.loadTexts: raidExMibTrapListTable.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibTrapListTable.setDescription('Trap list Table.')
raidExMibTrapListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1), ).setIndexNames((0, "HM800MIB", "eventListIndexSerialNumber"), (0, "HM800MIB", "eventListIndexRecordNo"))
if mibBuilder.loadTexts: raidExMibTrapListEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raidExMibTrapListEntry.setDescription('Trap list Table index.')
eventListIndexSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventListIndexSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: eventListIndexSerialNumber.setDescription('Serial Number of the DKC.')
eventListNickname = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventListNickname.setStatus('mandatory')
if mibBuilder.loadTexts: eventListNickname.setDescription('Nickname of the DKC.')
eventListIndexRecordNo = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventListIndexRecordNo.setStatus('mandatory')
if mibBuilder.loadTexts: eventListIndexRecordNo.setDescription('The record number of the event trap list.')
eventListREFCODE = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventListREFCODE.setStatus('mandatory')
if mibBuilder.loadTexts: eventListREFCODE.setDescription('The Reference code of the event trap. ')
eventListDate = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventListDate.setStatus('mandatory')
if mibBuilder.loadTexts: eventListDate.setDescription('The Date of the event trap. ')
eventListTime = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventListTime.setStatus('mandatory')
if mibBuilder.loadTexts: eventListTime.setDescription('The Time of the event trap. ')
eventListDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventListDescription.setStatus('mandatory')
if mibBuilder.loadTexts: eventListDescription.setDescription('Detail information of reference code. ')
eventTrapSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 1), Integer32())
if mibBuilder.loadTexts: eventTrapSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: eventTrapSerialNumber.setDescription('Serial Number of HM800 where an error occurred.')
eventTrapNickname = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 2), DisplayString())
if mibBuilder.loadTexts: eventTrapNickname.setStatus('mandatory')
if mibBuilder.loadTexts: eventTrapNickname.setDescription('Nickname of HM800 where an error occurred.')
eventTrapREFCODE = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 3), DisplayString())
if mibBuilder.loadTexts: eventTrapREFCODE.setStatus('mandatory')
if mibBuilder.loadTexts: eventTrapREFCODE.setDescription('Error reference code.')
eventTrapPartsID = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 4), ObjectIdentifier())
if mibBuilder.loadTexts: eventTrapPartsID.setStatus('mandatory')
if mibBuilder.loadTexts: eventTrapPartsID.setDescription('Error parts code of HM800 where an error occurred.')
eventTrapDate = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 5), DisplayString())
if mibBuilder.loadTexts: eventTrapDate.setStatus('mandatory')
if mibBuilder.loadTexts: eventTrapDate.setDescription('Date of HM800 where an error occurred.')
eventTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 6), DisplayString())
if mibBuilder.loadTexts: eventTrapTime.setStatus('mandatory')
if mibBuilder.loadTexts: eventTrapTime.setDescription('Time of HM800 where an error occurred.')
eventTrapDescription = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256)))
if mibBuilder.loadTexts: eventTrapDescription.setStatus('mandatory')
if mibBuilder.loadTexts: eventTrapDescription.setDescription(' Detail information of an error. ')
raideventUseracute = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1) + (0,1)).setObjects(("HM800MIB", "eventTrapSerialNumber"), ("HM800MIB", "eventTrapNickname"), ("HM800MIB", "eventTrapREFCODE"), ("HM800MIB", "eventTrapPartsID"), ("HM800MIB", "eventTrapDate"), ("HM800MIB", "eventTrapTime"), ("HM800MIB", "eventTrapDescription"))
if mibBuilder.loadTexts: raideventUseracute.setDescription('The impact of this event on the subsystem is acute.')
raideventUserserious = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1) + (0,2)).setObjects(("HM800MIB", "eventTrapSerialNumber"), ("HM800MIB", "eventTrapNickname"), ("HM800MIB", "eventTrapREFCODE"), ("HM800MIB", "eventTrapPartsID"), ("HM800MIB", "eventTrapDate"), ("HM800MIB", "eventTrapTime"), ("HM800MIB", "eventTrapDescription"))
if mibBuilder.loadTexts: raideventUserserious.setDescription('The impact of this event on the subsystem is serious.')
raideventUsermoderate = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1) + (0,3)).setObjects(("HM800MIB", "eventTrapSerialNumber"), ("HM800MIB", "eventTrapNickname"), ("HM800MIB", "eventTrapREFCODE"), ("HM800MIB", "eventTrapPartsID"), ("HM800MIB", "eventTrapDate"), ("HM800MIB", "eventTrapTime"), ("HM800MIB", "eventTrapDescription"))
if mibBuilder.loadTexts: raideventUsermoderate.setDescription('The impact of this event on the subsystem is moderate.')
raideventUserservice = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1) + (0,4)).setObjects(("HM800MIB", "eventTrapSerialNumber"), ("HM800MIB", "eventTrapNickname"), ("HM800MIB", "eventTrapREFCODE"), ("HM800MIB", "eventTrapPartsID"), ("HM800MIB", "eventTrapDate"), ("HM800MIB", "eventTrapTime"), ("HM800MIB", "eventTrapDescription"))
if mibBuilder.loadTexts: raideventUserservice.setDescription('The impact of this event on the subsystem is low.')
mibBuilder.exportSymbols("HM800MIB", eventTrapREFCODE=eventTrapREFCODE, raidExMibDKUHWTable=raidExMibDKUHWTable, dkcRaidListIndexSerialNumber=dkcRaidListIndexSerialNumber, raidRoot=raidRoot, raidExMibDummyX=raidExMibDummyX, eventListDescription=eventListDescription, eventTrapSerialNumber=eventTrapSerialNumber, dkcHWSM=dkcHWSM, raid=raid, raidlistMibNickName=raidlistMibNickName, raidExMibTrapListTable=raidExMibTrapListTable, storageExMib=storageExMib, raidExMib=raidExMib, raidExMibRaidListTable=raidExMibRaidListTable, dkcHWFan=dkcHWFan, raidDummy=raidDummy, dkcHWEnvironment=dkcHWEnvironment, raidExMibAgentVersion=raidExMibAgentVersion, dkuHWPS=dkuHWPS, storage=storage, raidExMibRaidListEntry=raidExMibRaidListEntry, dkuHWDrive=dkuHWDrive, raideventUseracute=raideventUseracute, raideventUserserious=raideventUserserious, eventTrapTime=eventTrapTime, raidExMibRoot=raidExMibRoot, system=system, eventListIndexSerialNumber=eventListIndexSerialNumber, eventListIndexRecordNo=eventListIndexRecordNo, raidlistDKCMainVersion=raidlistDKCMainVersion, eventListNickname=eventListNickname, eventTrapNickname=eventTrapNickname, raideventUsermoderate=raideventUsermoderate, eventTrapDescription=eventTrapDescription, dkuRaidListIndexSerialNumber=dkuRaidListIndexSerialNumber, hitachi=hitachi, raidExMibDkcCount=raidExMibDkcCount, raidExMibDKCHWEntry=raidExMibDKCHWEntry, eventListREFCODE=eventListREFCODE, dkcHWCache=dkcHWCache, dkuHWFan=dkuHWFan, raidExMibName=raidExMibName, eventListTime=eventListTime, dkcHWBattery=dkcHWBattery, dkcHWPS=dkcHWPS, raidlistDKCProductName=raidlistDKCProductName, raidlistSerialNumber=raidlistSerialNumber, raidExMibDKUHWEntry=raidExMibDKUHWEntry, raidExMibVersion=raidExMibVersion, dkuHWEnvironment=dkuHWEnvironment, raidExMibTrapListEntry=raidExMibTrapListEntry, raideventUserservice=raideventUserservice, eventTrapDate=eventTrapDate, raidExMibDummy=raidExMibDummy, eventListDate=eventListDate, eventTrapPartsID=eventTrapPartsID, dkcHWCSW=dkcHWCSW, dkcHWProcessor=dkcHWProcessor, raidExMibDKCHWTable=raidExMibDKCHWTable, systemExMib=systemExMib)
