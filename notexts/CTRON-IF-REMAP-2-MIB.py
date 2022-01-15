#
# PySNMP MIB module CTRON-IF-REMAP-2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-IF-REMAP-2-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:12 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctIFRemap2, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctIFRemap2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctIFRemap2Config = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1))
ctIFRemap2Table = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1), )
if mibBuilder.loadTexts: ctIFRemap2Table.setStatus('mandatory')
ctIFRemap2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SourceSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SourcePort"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2DestSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2DestPort"))
if mibBuilder.loadTexts: ctIFRemap2Entry.setStatus('mandatory')
ctIFRemap2SourceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SourceSlot.setStatus('mandatory')
ctIFRemap2SourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SourcePort.setStatus('mandatory')
ctIFRemap2DestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2DestSlot.setStatus('mandatory')
ctIFRemap2DestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2DestPort.setStatus('mandatory')
ctIFRemap2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2Status.setStatus('mandatory')
ctIFRemap2PhysicalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("unsupported", 3))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2PhysicalErrors.setStatus('mandatory')
ctIFRemap2EgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("alwaysTagged", 2), ("alwaysUntagged", 3))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2EgressType.setStatus('mandatory')
ctIFRemap2PortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2), )
if mibBuilder.loadTexts: ctIFRemap2PortTable.setStatus('mandatory')
ctIFRemap2PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2PortSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2PortIndex"))
if mibBuilder.loadTexts: ctIFRemap2PortEntry.setStatus('mandatory')
ctIFRemap2PortSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PortSlot.setStatus('mandatory')
ctIFRemap2PortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PortIndex.setStatus('mandatory')
ctIFRemap2PortReference = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PortReference.setStatus('mandatory')
ctIFRemap2PhysErrsCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("unsupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PhysErrsCapable.setStatus('mandatory')
ctIFRemap2SlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3), )
if mibBuilder.loadTexts: ctIFRemap2SlotTable.setStatus('mandatory')
ctIFRemap2SlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SlotIndex"))
if mibBuilder.loadTexts: ctIFRemap2SlotEntry.setStatus('mandatory')
ctIFRemap2SlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SlotIndex.setStatus('mandatory')
ctIFRemap2SlotMaxRemaps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SlotMaxRemaps.setStatus('mandatory')
ctIFRemap2SlotMaxRemoteDests = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SlotMaxRemoteDests.setStatus('mandatory')
ctIFRemap2VlanTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4), )
if mibBuilder.loadTexts: ctIFRemap2VlanTable.setStatus('mandatory')
ctIFRemap2VlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanSourceSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanSourceVlan"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanDestSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanDestPort"))
if mibBuilder.loadTexts: ctIFRemap2VlanEntry.setStatus('mandatory')
ctIFRemap2VlanSourceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanSourceSlot.setStatus('mandatory')
ctIFRemap2VlanSourceVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanSourceVlan.setStatus('mandatory')
ctIFRemap2VlanDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanDestSlot.setStatus('mandatory')
ctIFRemap2VlanDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanDestPort.setStatus('mandatory')
ctIFRemap2VlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2VlanStatus.setStatus('mandatory')
ctIFRemap2VlanEgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("received", 1), ("alwaysTagged", 2), ("alwaysUntagged", 3))).clone('received')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2VlanEgressType.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-IF-REMAP-2-MIB", ctIFRemap2VlanEntry=ctIFRemap2VlanEntry, ctIFRemap2PortReference=ctIFRemap2PortReference, ctIFRemap2Config=ctIFRemap2Config, ctIFRemap2DestPort=ctIFRemap2DestPort, ctIFRemap2VlanDestSlot=ctIFRemap2VlanDestSlot, ctIFRemap2VlanTable=ctIFRemap2VlanTable, ctIFRemap2VlanDestPort=ctIFRemap2VlanDestPort, ctIFRemap2SlotIndex=ctIFRemap2SlotIndex, ctIFRemap2PortSlot=ctIFRemap2PortSlot, ctIFRemap2VlanSourceVlan=ctIFRemap2VlanSourceVlan, ctIFRemap2VlanEgressType=ctIFRemap2VlanEgressType, ctIFRemap2VlanStatus=ctIFRemap2VlanStatus, ctIFRemap2SourcePort=ctIFRemap2SourcePort, ctIFRemap2Table=ctIFRemap2Table, ctIFRemap2VlanSourceSlot=ctIFRemap2VlanSourceSlot, ctIFRemap2PortEntry=ctIFRemap2PortEntry, ctIFRemap2SlotEntry=ctIFRemap2SlotEntry, ctIFRemap2EgressType=ctIFRemap2EgressType, ctIFRemap2SlotMaxRemoteDests=ctIFRemap2SlotMaxRemoteDests, ctIFRemap2SlotMaxRemaps=ctIFRemap2SlotMaxRemaps, ctIFRemap2PortTable=ctIFRemap2PortTable, ctIFRemap2SlotTable=ctIFRemap2SlotTable, ctIFRemap2Status=ctIFRemap2Status, ctIFRemap2PhysErrsCapable=ctIFRemap2PhysErrsCapable, ctIFRemap2PortIndex=ctIFRemap2PortIndex, ctIFRemap2SourceSlot=ctIFRemap2SourceSlot, ctIFRemap2Entry=ctIFRemap2Entry, ctIFRemap2PhysicalErrors=ctIFRemap2PhysicalErrors, ctIFRemap2DestSlot=ctIFRemap2DestSlot)
