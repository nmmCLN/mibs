#
# PySNMP MIB module NBS-OBA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-OBA-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:31:34 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NbsTcMHz, nbs = mibBuilder.importSymbols("NBS-MIB", "NbsTcMHz", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Counter64, Unsigned32, IpAddress, Integer32, ModuleIdentity, MibIdentifier, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
nbsObaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 240))
if mibBuilder.loadTexts: nbsObaMib.setLastUpdated('201503270000Z')
if mibBuilder.loadTexts: nbsObaMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsObaMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsObaMib.setDescription('Optical bandwidth allocation (OBA) information.')
nbsObaInfoGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 240, 1))
if mibBuilder.loadTexts: nbsObaInfoGrp.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoGrp.setDescription('For users to know if OBA is accessible')
nbsObaDefineGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 240, 2))
if mibBuilder.loadTexts: nbsObaDefineGrp.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineGrp.setDescription('For users to configure OBAs')
nbsObaAlsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 240, 3))
if mibBuilder.loadTexts: nbsObaAlsGrp.setStatus('current')
if mibBuilder.loadTexts: nbsObaAlsGrp.setDescription('For users to configure the Automatic Laser Shut-down (ALS) feature')
nbsObaInfoTable = MibTable((1, 3, 6, 1, 4, 1, 629, 240, 1, 1), )
if mibBuilder.loadTexts: nbsObaInfoTable.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoTable.setDescription('Optical bandwidth allocation (OBA) definition(s); table entries\n       are expected to be configured and viewed from the port-level.')
nbsObaInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1), ).setIndexNames((0, "NBS-OBA-MIB", "nbsObaInfoLineIfIndex"))
if mibBuilder.loadTexts: nbsObaInfoEntry.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoEntry.setDescription('Optical bandwidth allocation (OBA) definition.')
nbsObaInfoLineIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoLineIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoLineIfIndex.setDescription('The trunk or line port ifindex.')
nbsObaInfoAvails = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoAvails.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoAvails.setDescription('The comma separated list of bandwidth units available to the\n        user')
nbsObaInfoUnitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 3), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoUnitSize.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoUnitSize.setDescription('Shows the unit size in MHz')
nbsObaInfoMaxUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoMaxUnits.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoMaxUnits.setDescription('Shows the maximum number of OBA units allowed on this port')
nbsObaInfoMaxUnitsPerClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaInfoMaxUnitsPerClientPort.setStatus('current')
if mibBuilder.loadTexts: nbsObaInfoMaxUnitsPerClientPort.setDescription('Shows the maximum number of OBA units allowed on client ports')
nbsObaDefineTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 240, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineTableSize.setDescription('The number of entries for the nbsObaDefineTable in this port ')
nbsObaDefineTable = MibTable((1, 3, 6, 1, 4, 1, 629, 240, 2, 2), )
if mibBuilder.loadTexts: nbsObaDefineTable.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineTable.setDescription('Optical bandwidth allocation (OBA) definition(s); table entries\n       are expected to be configured and viewed from the port-level.')
nbsObaDefineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1), ).setIndexNames((0, "NBS-OBA-MIB", "nbsObaDefineLinePort"), (0, "NBS-OBA-MIB", "nbsObaDefineOrdinalIndex"))
if mibBuilder.loadTexts: nbsObaDefineEntry.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineEntry.setDescription('Optical bandwidth allocation (OBA) definition.')
nbsObaDefineLinePort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineLinePort.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineLinePort.setDescription('The line port (aka trunk port) associated with this entry.')
nbsObaDefineOrdinalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineOrdinalIndex.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineOrdinalIndex.setDescription('Ordinal index for this entry; arbitrarily picked, starting from\n       1. It is hidden from the CLI.')
nbsObaDefineLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineLabel.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineLabel.setDescription('User defined label that uniquely identifies this OBA.')
nbsObaDefineOduType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unconfigured", 1), ("odu0", 2))).clone('unconfigured')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineOduType.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineOduType.setDescription('The information structure data unit (data rate):\n         * ODU0 (1.24416 Gb/s)')
nbsObaDefineOduList = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineOduList.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineOduList.setDescription('A comma separated list of data unit identifiers assigned to\n       this OBA; an identifier may be assigned to one OBA only. ODU0\n       identifiers are the letters a-h.\n\n        The count of identifiers determines the maximum bandwidth\n        available, based on nbsObaDefineOduType. Just enough should be\n        assigned to convey the desired protocol; an overly generous\n        assignment wastes a limited resource and reduces overall\n        service capacity.')
nbsObaDefineOduCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineOduCount.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineOduCount.setDescription('The count of identifiers found in nbsObaDefineOduList.')
nbsObaDefineMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unconfigured", 1), ("express", 2), ("standAlone", 3), ("primary", 4), ("secondary", 5))).clone('unconfigured')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineMapType.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineMapType.setDescription('Specifies the OBA traffic mapping type:\n         * an express OBA passes from one line port to the other;\n         * a standAlone OBA has no redundant backup;\n         * a primary OBA is the first choice for redundant service;\n         * a secondary OBA provides service when the primary OBA fails.')
nbsObaDefineClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 21), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineClientPort.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineClientPort.setDescription('The add/drop client port (aka user or access port) associated\n       with this entry.')
nbsObaDefineCoupledWith = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineCoupledWith.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineCoupledWith.setDescription("This object's content depends on the 'nbsObaDefineMapType'\n       value:\n         * express -- the associated OBA on the other line port;\n         * standAlone -- N/A\n         * primary -- label of the associated secondary OBA;\n         * secondary -- label of the associated primary OBA.\n\n        Using an OBA's label instead of its ordinal index avoids\n        unexpected and unintential associations after create/delete\n        activities.")
nbsObaDefinePresentState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("down", 2), ("active", 3), ("standby", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefinePresentState.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefinePresentState.setDescription('Current OBA status.')
nbsObaDefineAllocationInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("unitsExceedProtocolSpec", 2), ("additionalUnitsNeededForProtocol", 3), ("unitsMatchProtocolSpec", 4), ("unitsExceedExpress", 5), ("additionalUnitsNeededForExpress", 6), ("unitsMatchExpress", 7))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaDefineAllocationInfo.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineAllocationInfo.setDescription('Indicates if the number of units (ODUs) exceed, are under, or\n       match the port protocol specifications.')
nbsObaDefineRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 99), RowStatus().clone('notInService')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsObaDefineRowStatus.setStatus('current')
if mibBuilder.loadTexts: nbsObaDefineRowStatus.setDescription('Used to create and delete OBAs')
nbsObaAlsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 240, 3, 1), )
if mibBuilder.loadTexts: nbsObaAlsTable.setStatus('current')
if mibBuilder.loadTexts: nbsObaAlsTable.setDescription('The Automatic Laser Shutdown (ALS) setting for each port.')
nbsObaAlsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1), ).setIndexNames((0, "NBS-OBA-MIB", "nbsObaAlsIfIndex"))
if mibBuilder.loadTexts: nbsObaAlsEntry.setStatus('current')
if mibBuilder.loadTexts: nbsObaAlsEntry.setDescription('Optical bandwidth allocation (OBA) port.')
nbsObaAlsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsObaAlsIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsObaAlsIfIndex.setDescription('The ifindex associated with this entry.')
nbsObaAlsState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsObaAlsState.setStatus('current')
if mibBuilder.loadTexts: nbsObaAlsState.setDescription('Defines whether the Automatic Laser Shut-down (ALS) feature is enabled or disabled.')
mibBuilder.exportSymbols("NBS-OBA-MIB", nbsObaDefineOrdinalIndex=nbsObaDefineOrdinalIndex, nbsObaDefineOduList=nbsObaDefineOduList, nbsObaDefineGrp=nbsObaDefineGrp, nbsObaDefineCoupledWith=nbsObaDefineCoupledWith, nbsObaDefineEntry=nbsObaDefineEntry, nbsObaInfoTable=nbsObaInfoTable, nbsObaDefineOduType=nbsObaDefineOduType, nbsObaMib=nbsObaMib, nbsObaAlsIfIndex=nbsObaAlsIfIndex, nbsObaAlsEntry=nbsObaAlsEntry, PYSNMP_MODULE_ID=nbsObaMib, nbsObaInfoAvails=nbsObaInfoAvails, nbsObaInfoMaxUnits=nbsObaInfoMaxUnits, nbsObaDefineTable=nbsObaDefineTable, nbsObaAlsState=nbsObaAlsState, nbsObaDefineLinePort=nbsObaDefineLinePort, nbsObaInfoLineIfIndex=nbsObaInfoLineIfIndex, nbsObaAlsGrp=nbsObaAlsGrp, nbsObaInfoEntry=nbsObaInfoEntry, nbsObaDefinePresentState=nbsObaDefinePresentState, nbsObaDefineOduCount=nbsObaDefineOduCount, nbsObaDefineAllocationInfo=nbsObaDefineAllocationInfo, nbsObaInfoUnitSize=nbsObaInfoUnitSize, nbsObaAlsTable=nbsObaAlsTable, nbsObaDefineRowStatus=nbsObaDefineRowStatus, nbsObaDefineMapType=nbsObaDefineMapType, nbsObaInfoMaxUnitsPerClientPort=nbsObaInfoMaxUnitsPerClientPort, nbsObaInfoGrp=nbsObaInfoGrp, nbsObaDefineClientPort=nbsObaDefineClientPort, nbsObaDefineLabel=nbsObaDefineLabel, nbsObaDefineTableSize=nbsObaDefineTableSize)
