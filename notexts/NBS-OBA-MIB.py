#
# PySNMP MIB module NBS-OBA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-OBA-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:22 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, NbsTcMHz = mibBuilder.importSymbols("NBS-MIB", "nbs", "NbsTcMHz")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, Unsigned32, IpAddress, Integer32, NotificationType, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
nbsObaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 240))
if mibBuilder.loadTexts: nbsObaMib.setLastUpdated('201503270000Z')
if mibBuilder.loadTexts: nbsObaMib.setOrganization('NBS')
nbsObaInfoGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 240, 1))
if mibBuilder.loadTexts: nbsObaInfoGrp.setStatus('current')
nbsObaDefineGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 240, 2))
if mibBuilder.loadTexts: nbsObaDefineGrp.setStatus('current')
nbsObaAlsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 240, 3))
if mibBuilder.loadTexts: nbsObaAlsGrp.setStatus('current')
nbsObaInfoTable = MibTable((1, 3, 6, 1, 4, 1, 629, 240, 1, 1), )
if mibBuilder.loadTexts: nbsObaInfoTable.setStatus('current')
nbsObaInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1), ).setIndexNames((0, "NBS-OBA-MIB", "nbsObaInfoLineIfIndex"))
if mibBuilder.loadTexts: nbsObaInfoEntry.setStatus('current')
nbsObaInfoLineIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoLineIfIndex.setStatus('current')
nbsObaInfoAvails = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoAvails.setStatus('current')
nbsObaInfoUnitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 3), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoUnitSize.setStatus('current')
nbsObaInfoMaxUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoMaxUnits.setStatus('current')
nbsObaInfoMaxUnitsPerClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoMaxUnitsPerClientPort.setStatus('current')
nbsObaDefineTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 240, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineTableSize.setStatus('current')
nbsObaDefineTable = MibTable((1, 3, 6, 1, 4, 1, 629, 240, 2, 2), )
if mibBuilder.loadTexts: nbsObaDefineTable.setStatus('current')
nbsObaDefineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1), ).setIndexNames((0, "NBS-OBA-MIB", "nbsObaDefineLinePort"), (0, "NBS-OBA-MIB", "nbsObaDefineOrdinalIndex"))
if mibBuilder.loadTexts: nbsObaDefineEntry.setStatus('current')
nbsObaDefineLinePort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineLinePort.setStatus('current')
nbsObaDefineOrdinalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineOrdinalIndex.setStatus('current')
nbsObaDefineLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineLabel.setStatus('current')
nbsObaDefineOduType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unconfigured", 1), ("odu0", 2))).clone('unconfigured')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineOduType.setStatus('current')
nbsObaDefineOduList = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineOduList.setStatus('current')
nbsObaDefineOduCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineOduCount.setStatus('current')
nbsObaDefineMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unconfigured", 1), ("express", 2), ("standAlone", 3), ("primary", 4), ("secondary", 5))).clone('unconfigured')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineMapType.setStatus('current')
nbsObaDefineClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 21), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineClientPort.setStatus('current')
nbsObaDefineCoupledWith = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineCoupledWith.setStatus('current')
nbsObaDefinePresentState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("down", 2), ("active", 3), ("standby", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefinePresentState.setStatus('current')
nbsObaDefineAllocationInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("unitsExceedProtocolSpec", 2), ("additionalUnitsNeededForProtocol", 3), ("unitsMatchProtocolSpec", 4), ("unitsExceedExpress", 5), ("additionalUnitsNeededForExpress", 6), ("unitsMatchExpress", 7))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineAllocationInfo.setStatus('current')
nbsObaDefineRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 99), RowStatus().clone('notInService')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineRowStatus.setStatus('current')
nbsObaAlsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 240, 3, 1), )
if mibBuilder.loadTexts: nbsObaAlsTable.setStatus('current')
nbsObaAlsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1), ).setIndexNames((0, "NBS-OBA-MIB", "nbsObaAlsIfIndex"))
if mibBuilder.loadTexts: nbsObaAlsEntry.setStatus('current')
nbsObaAlsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaAlsIfIndex.setStatus('current')
nbsObaAlsState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsObaAlsState.setStatus('current')
mibBuilder.exportSymbols("NBS-OBA-MIB", nbsObaDefineAllocationInfo=nbsObaDefineAllocationInfo, nbsObaDefineRowStatus=nbsObaDefineRowStatus, nbsObaDefineLabel=nbsObaDefineLabel, nbsObaMib=nbsObaMib, nbsObaAlsState=nbsObaAlsState, nbsObaInfoEntry=nbsObaInfoEntry, nbsObaDefineOduList=nbsObaDefineOduList, nbsObaInfoGrp=nbsObaInfoGrp, nbsObaDefineOduCount=nbsObaDefineOduCount, nbsObaInfoMaxUnits=nbsObaInfoMaxUnits, nbsObaAlsIfIndex=nbsObaAlsIfIndex, PYSNMP_MODULE_ID=nbsObaMib, nbsObaAlsGrp=nbsObaAlsGrp, nbsObaInfoUnitSize=nbsObaInfoUnitSize, nbsObaDefineClientPort=nbsObaDefineClientPort, nbsObaDefineTableSize=nbsObaDefineTableSize, nbsObaDefineTable=nbsObaDefineTable, nbsObaAlsEntry=nbsObaAlsEntry, nbsObaDefineCoupledWith=nbsObaDefineCoupledWith, nbsObaDefineLinePort=nbsObaDefineLinePort, nbsObaDefineMapType=nbsObaDefineMapType, nbsObaDefineOrdinalIndex=nbsObaDefineOrdinalIndex, nbsObaInfoLineIfIndex=nbsObaInfoLineIfIndex, nbsObaInfoMaxUnitsPerClientPort=nbsObaInfoMaxUnitsPerClientPort, nbsObaAlsTable=nbsObaAlsTable, nbsObaDefineEntry=nbsObaDefineEntry, nbsObaInfoTable=nbsObaInfoTable, nbsObaDefineGrp=nbsObaDefineGrp, nbsObaInfoAvails=nbsObaInfoAvails, nbsObaDefineOduType=nbsObaDefineOduType, nbsObaDefinePresentState=nbsObaDefinePresentState)
