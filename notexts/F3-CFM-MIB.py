#
# PySNMP MIB module F3-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-CFM-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:29 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
CmPmBinAction, AdminState, VlanPriority, OperationalState, PerfCounter64, SecondaryState = mibBuilder.importSymbols("CM-COMMON-MIB", "CmPmBinAction", "AdminState", "VlanPriority", "OperationalState", "PerfCounter64", "SecondaryState")
shelfIndex, neIndex, slotIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "shelfIndex", "neIndex", "slotIndex")
cmEthernetAccPortIndex, cmEthernetTrafficPortIndex, cmEthernetNetPortIndex = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmEthernetAccPortIndex", "cmEthernetTrafficPortIndex", "cmEthernetNetPortIndex")
dot1agCfmMaCompEntry, dot1agCfmMaNetEntry, dot1agCfmMepEntry, dot1agCfmMepIdentifier, dot1agCfmMdIndex, Dot1agCfmMDLevel, Dot1agCfmMepId, dot1agCfmMaIndex = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMaCompEntry", "dot1agCfmMaNetEntry", "dot1agCfmMepEntry", "dot1agCfmMepIdentifier", "dot1agCfmMdIndex", "Dot1agCfmMDLevel", "Dot1agCfmMepId", "dot1agCfmMaIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Counter64, iso, Integer32, Bits, ObjectIdentity, IpAddress, Counter32, Unsigned32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "iso", "Integer32", "Bits", "ObjectIdentity", "IpAddress", "Counter32", "Unsigned32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity")
DisplayString, StorageType, VariablePointer, MacAddress, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "VariablePointer", "MacAddress", "TextualConvention", "RowStatus", "TruthValue")
f3CfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13))
f3CfmMIB.setRevisions(('2021-01-28 00:00',))
if mibBuilder.loadTexts: f3CfmMIB.setLastUpdated('202101280000Z')
if mibBuilder.loadTexts: f3CfmMIB.setOrganization('ADVA Optical Networking SE')
cfmExtSvc = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1))
cfmExtSvcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1))
cfmExtSvcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2))
class CfmAisGenTriggerTypes(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bAisDefRemoteCCM", 0), ("bAisDefErrorCCM", 1), ("bAisDefXconCCM", 2), ("bAisDefAis", 3))

class CfmAisInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("aisInterval1sec", 1), ("aisInterval1min", 2))

class CfmLmmDmmInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("interval10msec", 1), ("interval100msec", 2), ("interval1sec", 3), ("interval10sec", 4), ("interval1min", 5))

class CfmMepDefects(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bDefAIS", 0))

class CfmLLFTriggerTypes(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bAis", 0), ("bCcmIfStatusTlv", 1), ("bRemoteCCM", 2), ("bRDI", 3))

class CfmSignalFailTriggers(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rdiCcm", 0), ("remoteCcm", 1), ("erroredCcm", 2), ("xconCcm", 3), ("ais", 4))

class CfmSlmEnabledTypes(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cos0", 0), ("cos1", 1), ("cos2", 2), ("cos3", 3), ("cos4", 4), ("cos5", 5), ("cos6", 6), ("cos7", 7))

class CfmPduVersionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("y1731-2008", 1), ("y1731-2011", 2))

cfmExtScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1))
cfmEthType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmEthType.setStatus('current')
cfmMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMacAddress.setStatus('current')
slmMulticastMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmMulticastMacAddress.setStatus('current')
slmOpcode = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmOpcode.setStatus('current')
slrOpcode = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slrOpcode.setStatus('current')
cfmSignalFailTriggers = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 6), CfmSignalFailTriggers()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmSignalFailTriggers.setStatus('current')
cfmMepTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2), )
if mibBuilder.loadTexts: cfmMepTable.setStatus('current')
cfmMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1), )
dot1agCfmMepEntry.registerAugmentions(("F3-CFM-MIB", "cfmMepEntry"))
cfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: cfmMepEntry.setStatus('current')
cfmMepAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 1), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepAdminState.setStatus('current')
cfmMepAisGenTriggerTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 2), CfmAisGenTriggerTypes()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepAisGenTriggerTypes.setStatus('current')
cfmMepAisClientMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 3), Dot1agCfmMDLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepAisClientMdLevel.setStatus('current')
cfmMepAisInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 4), CfmAisInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepAisInterval.setStatus('current')
cfmMepAisGenEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepAisGenEnabled.setStatus('current')
cfmMepAisPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 6), VlanPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepAisPriority.setStatus('current')
cfmMepLmTxCountAllPriosEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepLmTxCountAllPriosEnabled.setStatus('current')
cfmMepLmRxCountAllPriosEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepLmRxCountAllPriosEnabled.setStatus('current')
cfmMepLmDualEndedCountAllPriosEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepLmDualEndedCountAllPriosEnabled.setStatus('current')
cfmMepLmCountInProfileEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 10), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepLmCountInProfileEnabled.setStatus('current')
cfmMepLmTxPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 11), VlanPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepLmTxPriority.setStatus('current')
cfmMepDmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 12), VlanPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepDmPriority.setStatus('current')
cfmMepRxCCMs = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 13), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepRxCCMs.setStatus('current')
cfmMepErrCCMs = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 14), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepErrCCMs.setStatus('current')
cfmMepLLFTriggerTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 15), CfmLLFTriggerTypes()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepLLFTriggerTypes.setStatus('current')
cfmMepDefects = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 16), CfmMepDefects()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepDefects.setStatus('current')
cfmMepTagEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 17), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepTagEtherType.setStatus('current')
cfmMepStatsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 18), CmPmBinAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepStatsAction.setStatus('current')
cfmMepLbmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 19), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepLbmInterval.setStatus('current')
cfmMepOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 20), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepOperationalState.setStatus('current')
cfmMepSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 21), SecondaryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepSecondaryState.setStatus('current')
cfmMepSlmEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 22), CfmSlmEnabledTypes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepSlmEnabled.setStatus('current')
cfmMepAssociatedObject = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 23), VariablePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepAssociatedObject.setStatus('current')
cfmMepPduVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 24), CfmPduVersionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepPduVersion.setStatus('current')
cfmMepLlbResponderEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 25), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepLlbResponderEnabled.setStatus('current')
cfmMepLlbPortLLEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 26), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepLlbPortLLEnabled.setStatus('current')
cfmMepLlbVidList = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepLlbVidList.setStatus('current')
cfmMepCcmInterfaceStatusTLVControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 28), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMepCcmInterfaceStatusTLVControl.setStatus('current')
cfmAccPortQosShaperTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3), )
if mibBuilder.loadTexts: cfmAccPortQosShaperTable.setStatus('current')
cfmAccPortQosShaperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"), (0, "F3-CFM-MIB", "cfmAccPortQosShaperIndex"))
if mibBuilder.loadTexts: cfmAccPortQosShaperEntry.setStatus('current')
cfmAccPortQosShaperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: cfmAccPortQosShaperIndex.setStatus('current')
cfmAccPortQosShaperCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmAccPortQosShaperCIR.setStatus('current')
cfmAccPortQosShaperBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmAccPortQosShaperBufSize.setStatus('current')
cfmAccPortQosShaperAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 4), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmAccPortQosShaperAdminState.setStatus('current')
cfmNetPortQosShaperTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4), )
if mibBuilder.loadTexts: cfmNetPortQosShaperTable.setStatus('current')
cfmNetPortQosShaperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"), (0, "F3-CFM-MIB", "cfmNetPortQosShaperTypeIndex"))
if mibBuilder.loadTexts: cfmNetPortQosShaperEntry.setStatus('current')
cfmNetPortQosShaperTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: cfmNetPortQosShaperTypeIndex.setStatus('current')
cfmNetPortQosShaperCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmNetPortQosShaperCIR.setStatus('current')
cfmNetPortQosShaperBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmNetPortQosShaperBufSize.setStatus('current')
cfmNetPortQosShaperAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 4), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmNetPortQosShaperAdminState.setStatus('current')
cfmServerMepTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5), )
if mibBuilder.loadTexts: cfmServerMepTable.setStatus('current')
cfmServerMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1), ).setIndexNames((0, "F3-CFM-MIB", "cfmServerMepIndex"))
if mibBuilder.loadTexts: cfmServerMepEntry.setStatus('current')
cfmServerMepIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepIndex.setStatus('current')
cfmServerMepAssociatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 2), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepAssociatedPort.setStatus('current')
cfmServerMepAisClientMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 3), Dot1agCfmMDLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepAisClientMdLevel.setStatus('current')
cfmServerMepAisInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 4), CfmAisInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepAisInterval.setStatus('current')
cfmServerMepAisGenEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepAisGenEnabled.setStatus('current')
cfmServerMepAisPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 6), VlanPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepAisPriority.setStatus('current')
cfmServerMepStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 7), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepStorageType.setStatus('current')
cfmServerMepRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmServerMepRowStatus.setStatus('current')
cfmServerMepAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 9), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmServerMepAdminState.setStatus('current')
cfmServerMepOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 10), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmServerMepOperationalState.setStatus('current')
cfmServerMepSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 11), SecondaryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmServerMepSecondaryState.setStatus('current')
cfmDownMEPQosShaperTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6), )
if mibBuilder.loadTexts: cfmDownMEPQosShaperTable.setStatus('current')
cfmDownMEPQosShaperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"), (0, "F3-CFM-MIB", "cfmDownMEPQosShaperType"), (0, "F3-CFM-MIB", "cfmDownMEPQosShaperIndex"))
if mibBuilder.loadTexts: cfmDownMEPQosShaperEntry.setStatus('current')
cfmDownMEPQosShaperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: cfmDownMEPQosShaperIndex.setStatus('current')
cfmDownMEPQosShaperType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmDownMEPQosShaperType.setStatus('current')
cfmDownMEPQosShaperCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmDownMEPQosShaperCIR.setStatus('current')
cfmDownMEPQosShaperProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 4), VariablePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmDownMEPQosShaperProfile.setStatus('current')
cfmDownMEPQosShaperAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 5), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmDownMEPQosShaperAdminState.setStatus('current')
cfmMepExcludedMepListTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7), )
if mibBuilder.loadTexts: cfmMepExcludedMepListTable.setStatus('current')
cfmMepExcludedMepListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "F3-CFM-MIB", "cfmMepExcludedMepListIdentifier"))
if mibBuilder.loadTexts: cfmMepExcludedMepListEntry.setStatus('current')
cfmMepExcludedMepListIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191)))
if mibBuilder.loadTexts: cfmMepExcludedMepListIdentifier.setStatus('current')
cfmMepExcludedMepListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMepExcludedMepListRowStatus.setStatus('current')
cfmMepLbrTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8), )
if mibBuilder.loadTexts: cfmMepLbrTable.setStatus('current')
cfmMepLbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "F3-CFM-MIB", "cfmMepLbrMacAddress"))
if mibBuilder.loadTexts: cfmMepLbrEntry.setStatus('current')
cfmMepLbrMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepLbrMacAddress.setStatus('current')
cfmMepLbrMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepLbrMepId.setStatus('current')
cfmMepLbrInOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 3), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepLbrInOrder.setStatus('current')
cfmMepLbrOutOfOder = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 4), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMepLbrOutOfOder.setStatus('current')
cfmMaCompTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9), )
if mibBuilder.loadTexts: cfmMaCompTable.setStatus('current')
cfmMaCompEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9, 1), )
dot1agCfmMaCompEntry.registerAugmentions(("F3-CFM-MIB", "cfmMaCompEntry"))
cfmMaCompEntry.setIndexNames(*dot1agCfmMaCompEntry.getIndexNames())
if mibBuilder.loadTexts: cfmMaCompEntry.setStatus('current')
cfmMaCompIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMaCompIndex.setStatus('current')
cfmMaCompEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9, 1, 2), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMaCompEntity.setStatus('current')
cfmMaNetTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10), )
if mibBuilder.loadTexts: cfmMaNetTable.setStatus('current')
cfmMaNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10, 1), )
dot1agCfmMaNetEntry.registerAugmentions(("F3-CFM-MIB", "cfmMaNetEntry"))
cfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
if mibBuilder.loadTexts: cfmMaNetEntry.setStatus('current')
cfmMaNetRemoteMepAutoDiscovery = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMaNetRemoteMepAutoDiscovery.setStatus('current')
cfmMaNetMepNumbers = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmMaNetMepNumbers.setStatus('current')
cfmTrafficPortQosShaperTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11), )
if mibBuilder.loadTexts: cfmTrafficPortQosShaperTable.setStatus('current')
cfmTrafficPortQosShaperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"), (0, "F3-CFM-MIB", "cfmTrafficPortQosShaperIndex"))
if mibBuilder.loadTexts: cfmTrafficPortQosShaperEntry.setStatus('current')
cfmTrafficPortQosShaperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 1), Integer32())
if mibBuilder.loadTexts: cfmTrafficPortQosShaperIndex.setStatus('current')
cfmTrafficPortQosShaperCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmTrafficPortQosShaperCIR.setStatus('current')
cfmTrafficPortQosShaperBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmTrafficPortQosShaperBufSize.setStatus('current')
cfmTrafficPortQosShaperAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 4), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfmTrafficPortQosShaperAdminState.setStatus('current')
cfmMepLlbMacAddressTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12), )
if mibBuilder.loadTexts: cfmMepLlbMacAddressTable.setStatus('current')
cfmLlbMacAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "F3-CFM-MIB", "cfmLlbMacAddress"))
if mibBuilder.loadTexts: cfmLlbMacAddressEntry.setStatus('current')
cfmLlbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12, 1, 1), MacAddress())
if mibBuilder.loadTexts: cfmLlbMacAddress.setStatus('current')
cfmLlbMacAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmLlbMacAddressRowStatus.setStatus('current')
cfmExtSvcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 1))
cfmExtSvcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2))
cfmExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 1, 1)).setObjects(("F3-CFM-MIB", "cfmExtGroup"), ("F3-CFM-MIB", "cfmGenGroup"), ("F3-CFM-MIB", "cfmMepGroup"), ("F3-CFM-MIB", "cfmPortShaperGroup"), ("F3-CFM-MIB", "cfmServerMepGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtCompliance = cfmExtCompliance.setStatus('current')
cfmExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 1)).setObjects(("F3-CFM-MIB", "cfmEthType"), ("F3-CFM-MIB", "cfmMacAddress"), ("F3-CFM-MIB", "slmMulticastMacAddress"), ("F3-CFM-MIB", "slmOpcode"), ("F3-CFM-MIB", "slrOpcode"), ("F3-CFM-MIB", "cfmMepAdminState"), ("F3-CFM-MIB", "cfmMepAisGenTriggerTypes"), ("F3-CFM-MIB", "cfmMepAisClientMdLevel"), ("F3-CFM-MIB", "cfmMepAisInterval"), ("F3-CFM-MIB", "cfmMepAisGenEnabled"), ("F3-CFM-MIB", "cfmMepAisPriority"), ("F3-CFM-MIB", "cfmMepLmTxCountAllPriosEnabled"), ("F3-CFM-MIB", "cfmMepLmRxCountAllPriosEnabled"), ("F3-CFM-MIB", "cfmMepLmDualEndedCountAllPriosEnabled"), ("F3-CFM-MIB", "cfmMepLmCountInProfileEnabled"), ("F3-CFM-MIB", "cfmMepLmTxPriority"), ("F3-CFM-MIB", "cfmMepDmPriority"), ("F3-CFM-MIB", "cfmMepRxCCMs"), ("F3-CFM-MIB", "cfmMepErrCCMs"), ("F3-CFM-MIB", "cfmMepLLFTriggerTypes"), ("F3-CFM-MIB", "cfmMepDefects"), ("F3-CFM-MIB", "cfmMepTagEtherType"), ("F3-CFM-MIB", "cfmMepStatsAction"), ("F3-CFM-MIB", "cfmMepLbmInterval"), ("F3-CFM-MIB", "cfmAccPortQosShaperIndex"), ("F3-CFM-MIB", "cfmAccPortQosShaperCIR"), ("F3-CFM-MIB", "cfmAccPortQosShaperBufSize"), ("F3-CFM-MIB", "cfmAccPortQosShaperAdminState"), ("F3-CFM-MIB", "cfmNetPortQosShaperTypeIndex"), ("F3-CFM-MIB", "cfmNetPortQosShaperCIR"), ("F3-CFM-MIB", "cfmNetPortQosShaperBufSize"), ("F3-CFM-MIB", "cfmNetPortQosShaperAdminState"), ("F3-CFM-MIB", "cfmServerMepIndex"), ("F3-CFM-MIB", "cfmServerMepAssociatedPort"), ("F3-CFM-MIB", "cfmServerMepAisClientMdLevel"), ("F3-CFM-MIB", "cfmServerMepAisInterval"), ("F3-CFM-MIB", "cfmServerMepAisGenEnabled"), ("F3-CFM-MIB", "cfmServerMepAisPriority"), ("F3-CFM-MIB", "cfmServerMepStorageType"), ("F3-CFM-MIB", "cfmServerMepRowStatus"), ("F3-CFM-MIB", "cfmDownMEPQosShaperIndex"), ("F3-CFM-MIB", "cfmDownMEPQosShaperType"), ("F3-CFM-MIB", "cfmDownMEPQosShaperCIR"), ("F3-CFM-MIB", "cfmDownMEPQosShaperProfile"), ("F3-CFM-MIB", "cfmDownMEPQosShaperAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtGroup = cfmExtGroup.setStatus('deprecated')
cfmGenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 2)).setObjects(("F3-CFM-MIB", "cfmEthType"), ("F3-CFM-MIB", "cfmMacAddress"), ("F3-CFM-MIB", "slmMulticastMacAddress"), ("F3-CFM-MIB", "slmOpcode"), ("F3-CFM-MIB", "slrOpcode"), ("F3-CFM-MIB", "cfmSignalFailTriggers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmGenGroup = cfmGenGroup.setStatus('current')
cfmMepGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 3)).setObjects(("F3-CFM-MIB", "cfmMepAdminState"), ("F3-CFM-MIB", "cfmMepAisGenTriggerTypes"), ("F3-CFM-MIB", "cfmMepAisClientMdLevel"), ("F3-CFM-MIB", "cfmMepAisInterval"), ("F3-CFM-MIB", "cfmMepAisGenEnabled"), ("F3-CFM-MIB", "cfmMepAisPriority"), ("F3-CFM-MIB", "cfmMepLmTxCountAllPriosEnabled"), ("F3-CFM-MIB", "cfmMepLmRxCountAllPriosEnabled"), ("F3-CFM-MIB", "cfmMepLmDualEndedCountAllPriosEnabled"), ("F3-CFM-MIB", "cfmMepLmCountInProfileEnabled"), ("F3-CFM-MIB", "cfmMepLmTxPriority"), ("F3-CFM-MIB", "cfmMepDmPriority"), ("F3-CFM-MIB", "cfmMepRxCCMs"), ("F3-CFM-MIB", "cfmMepErrCCMs"), ("F3-CFM-MIB", "cfmMepLLFTriggerTypes"), ("F3-CFM-MIB", "cfmMepDefects"), ("F3-CFM-MIB", "cfmMepTagEtherType"), ("F3-CFM-MIB", "cfmMepStatsAction"), ("F3-CFM-MIB", "cfmMepOperationalState"), ("F3-CFM-MIB", "cfmMepSecondaryState"), ("F3-CFM-MIB", "cfmMepSlmEnabled"), ("F3-CFM-MIB", "cfmMepExcludedMepListIdentifier"), ("F3-CFM-MIB", "cfmMepExcludedMepListRowStatus"), ("F3-CFM-MIB", "cfmMepLbrMacAddress"), ("F3-CFM-MIB", "cfmMepLbrMepId"), ("F3-CFM-MIB", "cfmMepLbrInOrder"), ("F3-CFM-MIB", "cfmMepLbrOutOfOder"), ("F3-CFM-MIB", "cfmMepAssociatedObject"), ("F3-CFM-MIB", "cfmMepPduVersion"), ("F3-CFM-MIB", "cfmMepLlbResponderEnabled"), ("F3-CFM-MIB", "cfmMepLlbPortLLEnabled"), ("F3-CFM-MIB", "cfmMepLlbVidList"), ("F3-CFM-MIB", "cfmLlbMacAddress"), ("F3-CFM-MIB", "cfmMepCcmInterfaceStatusTLVControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMepGroup = cfmMepGroup.setStatus('current')
cfmPortShaperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 4)).setObjects(("F3-CFM-MIB", "cfmAccPortQosShaperIndex"), ("F3-CFM-MIB", "cfmAccPortQosShaperCIR"), ("F3-CFM-MIB", "cfmAccPortQosShaperBufSize"), ("F3-CFM-MIB", "cfmAccPortQosShaperAdminState"), ("F3-CFM-MIB", "cfmNetPortQosShaperTypeIndex"), ("F3-CFM-MIB", "cfmNetPortQosShaperCIR"), ("F3-CFM-MIB", "cfmNetPortQosShaperBufSize"), ("F3-CFM-MIB", "cfmNetPortQosShaperAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmPortShaperGroup = cfmPortShaperGroup.setStatus('current')
cfmServerMepGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 5)).setObjects(("F3-CFM-MIB", "cfmServerMepIndex"), ("F3-CFM-MIB", "cfmServerMepAssociatedPort"), ("F3-CFM-MIB", "cfmServerMepAisClientMdLevel"), ("F3-CFM-MIB", "cfmServerMepAisInterval"), ("F3-CFM-MIB", "cfmServerMepAisGenEnabled"), ("F3-CFM-MIB", "cfmServerMepAisPriority"), ("F3-CFM-MIB", "cfmServerMepStorageType"), ("F3-CFM-MIB", "cfmServerMepRowStatus"), ("F3-CFM-MIB", "cfmServerMepAdminState"), ("F3-CFM-MIB", "cfmServerMepOperationalState"), ("F3-CFM-MIB", "cfmServerMepSecondaryState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmServerMepGroup = cfmServerMepGroup.setStatus('current')
cfmMaCompGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 6)).setObjects(("F3-CFM-MIB", "cfmMaCompIndex"), ("F3-CFM-MIB", "cfmMaCompEntity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMaCompGroup = cfmMaCompGroup.setStatus('current')
mibBuilder.exportSymbols("F3-CFM-MIB", cfmMepLmTxCountAllPriosEnabled=cfmMepLmTxCountAllPriosEnabled, cfmExtCompliance=cfmExtCompliance, cfmMepCcmInterfaceStatusTLVControl=cfmMepCcmInterfaceStatusTLVControl, cfmMepExcludedMepListTable=cfmMepExcludedMepListTable, cfmAccPortQosShaperCIR=cfmAccPortQosShaperCIR, slmOpcode=slmOpcode, cfmPortShaperGroup=cfmPortShaperGroup, cfmMaNetTable=cfmMaNetTable, cfmMepExcludedMepListRowStatus=cfmMepExcludedMepListRowStatus, cfmMepLbrMacAddress=cfmMepLbrMacAddress, cfmMacAddress=cfmMacAddress, CfmMepDefects=CfmMepDefects, cfmMaNetEntry=cfmMaNetEntry, slmMulticastMacAddress=slmMulticastMacAddress, cfmNetPortQosShaperCIR=cfmNetPortQosShaperCIR, cfmServerMepAisClientMdLevel=cfmServerMepAisClientMdLevel, cfmAccPortQosShaperIndex=cfmAccPortQosShaperIndex, cfmEthType=cfmEthType, cfmTrafficPortQosShaperTable=cfmTrafficPortQosShaperTable, cfmExtSvcCompliances=cfmExtSvcCompliances, cfmMepTable=cfmMepTable, cfmServerMepRowStatus=cfmServerMepRowStatus, cfmMepLmRxCountAllPriosEnabled=cfmMepLmRxCountAllPriosEnabled, cfmServerMepAisInterval=cfmServerMepAisInterval, cfmServerMepAdminState=cfmServerMepAdminState, cfmDownMEPQosShaperType=cfmDownMEPQosShaperType, cfmMepLbrTable=cfmMepLbrTable, cfmSignalFailTriggers=cfmSignalFailTriggers, cfmTrafficPortQosShaperAdminState=cfmTrafficPortQosShaperAdminState, cfmMepLlbResponderEnabled=cfmMepLlbResponderEnabled, CfmAisInterval=CfmAisInterval, slrOpcode=slrOpcode, cfmNetPortQosShaperTable=cfmNetPortQosShaperTable, cfmMepLbrEntry=cfmMepLbrEntry, cfmExtSvc=cfmExtSvc, PYSNMP_MODULE_ID=f3CfmMIB, cfmServerMepAssociatedPort=cfmServerMepAssociatedPort, cfmMepStatsAction=cfmMepStatsAction, cfmMepLlbMacAddressTable=cfmMepLlbMacAddressTable, cfmServerMepIndex=cfmServerMepIndex, cfmNetPortQosShaperAdminState=cfmNetPortQosShaperAdminState, cfmNetPortQosShaperTypeIndex=cfmNetPortQosShaperTypeIndex, cfmExtGroup=cfmExtGroup, cfmMepGroup=cfmMepGroup, cfmExtScalars=cfmExtScalars, cfmMaCompTable=cfmMaCompTable, cfmMaCompIndex=cfmMaCompIndex, cfmMepLmTxPriority=cfmMepLmTxPriority, cfmMepLmCountInProfileEnabled=cfmMepLmCountInProfileEnabled, CfmLmmDmmInterval=CfmLmmDmmInterval, cfmServerMepEntry=cfmServerMepEntry, cfmExtSvcConformance=cfmExtSvcConformance, CfmPduVersionType=CfmPduVersionType, cfmMepDmPriority=cfmMepDmPriority, cfmMepExcludedMepListIdentifier=cfmMepExcludedMepListIdentifier, cfmMepLlbPortLLEnabled=cfmMepLlbPortLLEnabled, CfmSignalFailTriggers=CfmSignalFailTriggers, cfmTrafficPortQosShaperIndex=cfmTrafficPortQosShaperIndex, cfmMaNetMepNumbers=cfmMaNetMepNumbers, cfmGenGroup=cfmGenGroup, cfmServerMepTable=cfmServerMepTable, cfmMepLbrOutOfOder=cfmMepLbrOutOfOder, cfmDownMEPQosShaperCIR=cfmDownMEPQosShaperCIR, cfmAccPortQosShaperTable=cfmAccPortQosShaperTable, cfmMepAdminState=cfmMepAdminState, cfmMaCompGroup=cfmMaCompGroup, cfmMepLlbVidList=cfmMepLlbVidList, cfmMepRxCCMs=cfmMepRxCCMs, f3CfmMIB=f3CfmMIB, cfmMepAssociatedObject=cfmMepAssociatedObject, cfmMepLbrMepId=cfmMepLbrMepId, cfmAccPortQosShaperBufSize=cfmAccPortQosShaperBufSize, cfmLlbMacAddressRowStatus=cfmLlbMacAddressRowStatus, cfmMepLbmInterval=cfmMepLbmInterval, cfmMepAisGenEnabled=cfmMepAisGenEnabled, cfmMepAisGenTriggerTypes=cfmMepAisGenTriggerTypes, cfmExtSvcGroups=cfmExtSvcGroups, cfmLlbMacAddressEntry=cfmLlbMacAddressEntry, cfmExtSvcObjects=cfmExtSvcObjects, cfmLlbMacAddress=cfmLlbMacAddress, cfmMaCompEntity=cfmMaCompEntity, CfmLLFTriggerTypes=CfmLLFTriggerTypes, cfmMepDefects=cfmMepDefects, cfmTrafficPortQosShaperEntry=cfmTrafficPortQosShaperEntry, cfmAccPortQosShaperEntry=cfmAccPortQosShaperEntry, cfmMepSecondaryState=cfmMepSecondaryState, cfmMepEntry=cfmMepEntry, cfmMepOperationalState=cfmMepOperationalState, cfmDownMEPQosShaperIndex=cfmDownMEPQosShaperIndex, cfmMepTagEtherType=cfmMepTagEtherType, cfmNetPortQosShaperBufSize=cfmNetPortQosShaperBufSize, cfmTrafficPortQosShaperBufSize=cfmTrafficPortQosShaperBufSize, cfmServerMepAisGenEnabled=cfmServerMepAisGenEnabled, CfmAisGenTriggerTypes=CfmAisGenTriggerTypes, cfmNetPortQosShaperEntry=cfmNetPortQosShaperEntry, CfmSlmEnabledTypes=CfmSlmEnabledTypes, cfmMepAisInterval=cfmMepAisInterval, cfmServerMepSecondaryState=cfmServerMepSecondaryState, cfmMepErrCCMs=cfmMepErrCCMs, cfmMepAisPriority=cfmMepAisPriority, cfmMepPduVersion=cfmMepPduVersion, cfmServerMepOperationalState=cfmServerMepOperationalState, cfmDownMEPQosShaperProfile=cfmDownMEPQosShaperProfile, cfmServerMepAisPriority=cfmServerMepAisPriority, cfmMaCompEntry=cfmMaCompEntry, cfmTrafficPortQosShaperCIR=cfmTrafficPortQosShaperCIR, cfmMepSlmEnabled=cfmMepSlmEnabled, cfmDownMEPQosShaperAdminState=cfmDownMEPQosShaperAdminState, cfmMepExcludedMepListEntry=cfmMepExcludedMepListEntry, cfmDownMEPQosShaperTable=cfmDownMEPQosShaperTable, cfmMepAisClientMdLevel=cfmMepAisClientMdLevel, cfmDownMEPQosShaperEntry=cfmDownMEPQosShaperEntry, cfmMepLLFTriggerTypes=cfmMepLLFTriggerTypes, cfmAccPortQosShaperAdminState=cfmAccPortQosShaperAdminState, cfmMaNetRemoteMepAutoDiscovery=cfmMaNetRemoteMepAutoDiscovery, cfmMepLmDualEndedCountAllPriosEnabled=cfmMepLmDualEndedCountAllPriosEnabled, cfmMepLbrInOrder=cfmMepLbrInOrder, cfmServerMepGroup=cfmServerMepGroup, cfmServerMepStorageType=cfmServerMepStorageType)
