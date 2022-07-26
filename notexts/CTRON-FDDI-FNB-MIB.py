#
# PySNMP MIB module CTRON-FDDI-FNB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-FDDI-FNB-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:41 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ctFDDIFnb, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFDDIFnb")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ObjectIdentity, Counter64, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, TimeTicks, Gauge32, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Bits", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFDDIResource = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1))
ctFDDINonMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2))
ctFDDIMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3))
ctFDDISerialConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4))
ctFDDIResourceTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1), )
if mibBuilder.loadTexts: ctFDDIResourceTable.setStatus('mandatory')
ctFDDIResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIResourceSlotID"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIResourceID"))
if mibBuilder.loadTexts: ctFDDIResourceEntry.setStatus('mandatory')
ctFDDIResourceSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceSlotID.setStatus('mandatory')
ctFDDIResourceID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceID.setStatus('mandatory')
ctFDDIResourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceType.setStatus('mandatory')
ctFDDIResourceNumbInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceNumbInstance.setStatus('mandatory')
ctFDDINonMuxCapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1), )
if mibBuilder.loadTexts: ctFDDINonMuxCapTable.setStatus('mandatory')
ctFDDINonMuxCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConfigID"))
if mibBuilder.loadTexts: ctFDDINonMuxCapEntry.setStatus('mandatory')
ctFDDINMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMSlot.setStatus('mandatory')
ctFDDINMConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConfigID.setStatus('mandatory')
ctFDDINMConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConfig.setStatus('mandatory')
ctFDDINMConfigDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConfigDesc.setStatus('mandatory')
ctFDDINonMuxCapEnableTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2), )
if mibBuilder.loadTexts: ctFDDINonMuxCapEnableTable.setStatus('mandatory')
ctFDDINonMuxCapEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMEnableSlot"))
if mibBuilder.loadTexts: ctFDDINonMuxCapEnableEntry.setStatus('mandatory')
ctFDDINMEnableSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMEnableSlot.setStatus('mandatory')
ctFDDINMCapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDINMCapEnable.setStatus('mandatory')
ctFDDINonMuxConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3), )
if mibBuilder.loadTexts: ctFDDINonMuxConnectionTable.setStatus('mandatory')
ctFDDINonMuxConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConnectionSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConnectionID"))
if mibBuilder.loadTexts: ctFDDINonMuxConnectionEntry.setStatus('mandatory')
ctFDDINMConnectionSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConnectionSlot.setStatus('mandatory')
ctFDDINMConnectionID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConnectionID.setStatus('mandatory')
ctFDDINMSMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMSMT.setStatus('mandatory')
ctFDDINMMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMMAC.setStatus('mandatory')
ctFDDINMBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMBytes.setStatus('mandatory')
ctFDDINMFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMFrames.setStatus('mandatory')
ctFDDINonMuxInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4), )
if mibBuilder.loadTexts: ctFDDINonMuxInterfaceTable.setStatus('mandatory')
ctFDDINonMuxInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMInterSlot"))
if mibBuilder.loadTexts: ctFDDINonMuxInterfaceEntry.setStatus('mandatory')
ctFDDINMInterSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMInterSlot.setStatus('mandatory')
ctFDDINMNumbInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMNumbInterfaces.setStatus('mandatory')
ctFDDIMuxCapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1), )
if mibBuilder.loadTexts: ctFDDIMuxCapTable.setStatus('mandatory')
ctFDDIMuxCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxConfig"))
if mibBuilder.loadTexts: ctFDDIMuxCapEntry.setStatus('mandatory')
ctFDDIMuxSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxSlot.setStatus('mandatory')
ctFDDIMuxConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxConfigID.setStatus('mandatory')
ctFDDIMuxConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxConfig.setStatus('mandatory')
ctFDDIMuxConfigDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxConfigDesc.setStatus('mandatory')
ctFDDIMuxCapEnableTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2), )
if mibBuilder.loadTexts: ctFDDIMuxCapEnableTable.setStatus('mandatory')
ctFDDIMuxCapEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxEnableSlot"))
if mibBuilder.loadTexts: ctFDDIMuxCapEnableEntry.setStatus('mandatory')
ctFDDIMuxEnableSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxEnableSlot.setStatus('mandatory')
ctFDDIMuxCapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDIMuxCapEnable.setStatus('mandatory')
ctFDDIMuxMasterPortAssignmentChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortAssignmentChange.setStatus('mandatory')
ctFDDIMuxOutTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3), )
if mibBuilder.loadTexts: ctFDDIMuxOutTable.setStatus('mandatory')
ctFDDIMuxOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxOutSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxOutID"))
if mibBuilder.loadTexts: ctFDDIMuxOutEntry.setStatus('mandatory')
ctFDDIMuxOutSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutSlot.setStatus('mandatory')
ctFDDIMuxOutID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutID.setStatus('mandatory')
ctFDDIMuxOutMACIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutMACIndex.setStatus('mandatory')
ctFDDIMuxOutSMTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutSMTIndex.setStatus('mandatory')
ctFDDIMuxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxBytes.setStatus('mandatory')
ctFDDIMuxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxFrames.setStatus('mandatory')
ctFDDIMuxMasterPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4), )
if mibBuilder.loadTexts: ctFDDIMuxMasterPortTable.setStatus('mandatory')
ctFDDIMuxMasterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxMasterPortSlotID"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxMasterPortID"))
if mibBuilder.loadTexts: ctFDDIMuxMasterPortEntry.setStatus('mandatory')
ctFDDIMuxMasterPortSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortSlotID.setStatus('mandatory')
ctFDDIMuxMasterPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortID.setStatus('mandatory')
ctFDDIMuxMasterPortAssignment = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortAssignment.setStatus('mandatory')
ctFDDIMuxMasterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortIndex.setStatus('mandatory')
ctFDDINumbModules = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINumbModules.setStatus('mandatory')
ctFDDISerialConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2), )
if mibBuilder.loadTexts: ctFDDISerialConfigTable.setStatus('mandatory')
ctFDDISerialConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDISerialSlotID"))
if mibBuilder.loadTexts: ctFDDISerialConfigEntry.setStatus('mandatory')
ctFDDISerialSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISerialSlotID.setStatus('mandatory')
ctFDDISerialAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("insertFNB1", 1), ("insertFNB2", 2), ("insertFNB1FNB2", 3), ("bypass", 4), ("hwControlFNB1", 5), ("hwControlFNB2", 6), ("hwControl", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDISerialAdminStatus.setStatus('mandatory')
ctFDDISerialOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("insertFNB1", 1), ("insertFNB2", 2), ("insertFNB1FNB2", 3), ("bypass", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISerialOperStatus.setStatus('mandatory')
ctFDDIModuleFPIMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3), )
if mibBuilder.loadTexts: ctFDDIModuleFPIMTable.setStatus('mandatory')
ctFDDIModuleFPIMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFddiFPIMSlotID"), (0, "CTRON-FDDI-FNB-MIB", "ctFddiFPIM"))
if mibBuilder.loadTexts: ctFDDIModuleFPIMEntry.setStatus('mandatory')
ctFddiFPIMSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIMSlotID.setStatus('mandatory')
ctFddiFPIM = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIM.setStatus('mandatory')
ctFddiFPIMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("link", 1), ("noLink", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIMStatus.setStatus('mandatory')
ctFddiFPIMType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIMType.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-FDDI-FNB-MIB", ctFDDIMuxCapTable=ctFDDIMuxCapTable, ctFddiFPIM=ctFddiFPIM, ctFDDINMInterSlot=ctFDDINMInterSlot, ctFDDIMuxConfigDesc=ctFDDIMuxConfigDesc, ctFDDIMuxOutEntry=ctFDDIMuxOutEntry, ctFDDIMuxMasterPortSlotID=ctFDDIMuxMasterPortSlotID, ctFDDIMuxOutID=ctFDDIMuxOutID, ctFDDIMuxMasterPortAssignment=ctFDDIMuxMasterPortAssignment, ctFDDINMConfigID=ctFDDINMConfigID, ctFDDIMuxSlot=ctFDDIMuxSlot, ctFDDINonMuxConnectionEntry=ctFDDINonMuxConnectionEntry, ctFDDIMuxConfigID=ctFDDIMuxConfigID, ctFDDIMuxMasterPortID=ctFDDIMuxMasterPortID, ctFDDIResourceNumbInstance=ctFDDIResourceNumbInstance, ctFDDIMuxOutTable=ctFDDIMuxOutTable, ctFDDIMuxBytes=ctFDDIMuxBytes, ctFDDISerialOperStatus=ctFDDISerialOperStatus, ctFDDIMuxMasterPortTable=ctFDDIMuxMasterPortTable, ctFDDIMux=ctFDDIMux, ctFDDINonMuxCapEnableEntry=ctFDDINonMuxCapEnableEntry, ctFDDINMEnableSlot=ctFDDINMEnableSlot, ctFDDINMFrames=ctFDDINMFrames, ctFDDIResourceSlotID=ctFDDIResourceSlotID, ctFDDIResourceType=ctFDDIResourceType, ctFDDIResourceID=ctFDDIResourceID, ctFDDINonMuxCapEntry=ctFDDINonMuxCapEntry, ctFDDIResourceTable=ctFDDIResourceTable, ctFDDINMNumbInterfaces=ctFDDINMNumbInterfaces, ctFDDINonMux=ctFDDINonMux, ctFDDINumbModules=ctFDDINumbModules, ctFDDINMConnectionSlot=ctFDDINMConnectionSlot, ctFDDIMuxMasterPortIndex=ctFDDIMuxMasterPortIndex, ctFDDIMuxOutSMTIndex=ctFDDIMuxOutSMTIndex, ctFDDINMMAC=ctFDDINMMAC, ctFDDIMuxEnableSlot=ctFDDIMuxEnableSlot, ctFDDIResource=ctFDDIResource, ctFDDIModuleFPIMEntry=ctFDDIModuleFPIMEntry, ctFDDIMuxCapEntry=ctFDDIMuxCapEntry, ctFDDIMuxConfig=ctFDDIMuxConfig, ctFDDINonMuxCapEnableTable=ctFDDINonMuxCapEnableTable, ctFDDIMuxOutMACIndex=ctFDDIMuxOutMACIndex, ctFDDIMuxMasterPortAssignmentChange=ctFDDIMuxMasterPortAssignmentChange, ctFDDISerialSlotID=ctFDDISerialSlotID, ctFDDISerialConfig=ctFDDISerialConfig, ctFDDIMuxCapEnableEntry=ctFDDIMuxCapEnableEntry, ctFDDIMuxMasterPortEntry=ctFDDIMuxMasterPortEntry, ctFDDISerialConfigEntry=ctFDDISerialConfigEntry, ctFddiFPIMType=ctFddiFPIMType, ctFDDINonMuxConnectionTable=ctFDDINonMuxConnectionTable, ctFDDINMConnectionID=ctFDDINMConnectionID, ctFDDINonMuxInterfaceEntry=ctFDDINonMuxInterfaceEntry, ctFddiFPIMStatus=ctFddiFPIMStatus, ctFDDIMuxCapEnableTable=ctFDDIMuxCapEnableTable, ctFDDINMConfigDesc=ctFDDINMConfigDesc, ctFDDIResourceEntry=ctFDDIResourceEntry, ctFDDINMSMT=ctFDDINMSMT, ctFDDIMuxOutSlot=ctFDDIMuxOutSlot, ctFddiFPIMSlotID=ctFddiFPIMSlotID, ctFDDISerialAdminStatus=ctFDDISerialAdminStatus, ctFDDINMBytes=ctFDDINMBytes, ctFDDINMCapEnable=ctFDDINMCapEnable, ctFDDINonMuxInterfaceTable=ctFDDINonMuxInterfaceTable, ctFDDIModuleFPIMTable=ctFDDIModuleFPIMTable, ctFDDIMuxCapEnable=ctFDDIMuxCapEnable, ctFDDISerialConfigTable=ctFDDISerialConfigTable, ctFDDIMuxFrames=ctFDDIMuxFrames, ctFDDINonMuxCapTable=ctFDDINonMuxCapTable, ctFDDINMConfig=ctFDDINMConfig, ctFDDINMSlot=ctFDDINMSlot)
