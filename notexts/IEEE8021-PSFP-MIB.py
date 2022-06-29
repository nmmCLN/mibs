#
# PySNMP MIB module IEEE8021-PSFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-PSFP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:08 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ieee8021BridgeBaseComponentId, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId")
IEEE8021STPTPtimeValue, = mibBuilder.importSymbols("IEEE8021-ST-MIB", "IEEE8021STPTPtimeValue")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Unsigned32, Counter64, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, Counter32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "Counter32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
ieee8021PSFPMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 31))
ieee8021PSFPMib.setRevisions(('2018-06-28 00:00', '2017-09-08 00:00',))
if mibBuilder.loadTexts: ieee8021PSFPMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021PSFPMib.setOrganization('IEEE 802.1 Working Group')
ieee8021PSFPNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 0))
ieee8021PSFPObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 1))
ieee8021PSFPConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 2))
ieee8021PSFPStreamFilterParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 1, 1))
ieee8021PSFPStreamGateParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 1, 2))
ieee8021PSFPFlowMeterParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 1, 3))
ieee8021PSFPStreamParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 1, 4))
ieee8021PSFPStreamFilterTable = MibTable((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021PSFPStreamFilterTable.setStatus('current')
ieee8021PSFPStreamFilterEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-PSFP-MIB", "ieee8021PSFPStreamFilterInstance"))
if mibBuilder.loadTexts: ieee8021PSFPStreamFilterEntry.setStatus('current')
ieee8021PSFPStreamFilterInstance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ieee8021PSFPStreamFilterInstance.setStatus('current')
ieee8021PSFPStreamHandleSpec = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPStreamHandleSpec.setStatus('current')
ieee8021PSFPPrioritySpec = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPPrioritySpec.setStatus('current')
ieee8021PSFPStreamGateInstanceID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPStreamGateInstanceID.setStatus('current')
ieee8021PSFPFilterSpecificationList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFilterSpecificationList.setStatus('current')
ieee8021PSFPMatchingFramesCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPMatchingFramesCount.setStatus('current')
ieee8021PSFPPassingFramesCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPPassingFramesCount.setStatus('current')
ieee8021PSFPNotPassingFramesCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPNotPassingFramesCount.setStatus('current')
ieee8021PSFPPassingSDUCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPPassingSDUCount.setStatus('current')
ieee8021PSFPNotPassingSDUCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPNotPassingSDUCount.setStatus('current')
ieee8021PSFPREDFramesCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPREDFramesCount.setStatus('current')
ieee8021PSFPStreamBlockedDueToOversizeFrameEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPStreamBlockedDueToOversizeFrameEnable.setStatus('current')
ieee8021PSFPStreamBlockedDueToOversizeFrame = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPStreamBlockedDueToOversizeFrame.setStatus('current')
ieee8021PSFPStreamFilterEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPStreamFilterEntryRowStatus.setStatus('current')
ieee8021PSFPStreamGateTable = MibTable((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021PSFPStreamGateTable.setStatus('current')
ieee8021PSFPStreamGateEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-PSFP-MIB", "ieee8021PSFPStreamGateInstance"))
if mibBuilder.loadTexts: ieee8021PSFPStreamGateEntry.setStatus('current')
ieee8021PSFPStreamGateInstance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ieee8021PSFPStreamGateInstance.setStatus('current')
ieee8021PSFPGateEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPGateEnabled.setStatus('current')
ieee8021PSFPAdminGateStates = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("closed", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminGateStates.setStatus('current')
ieee8021PSFPOperGateStates = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("closed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPOperGateStates.setStatus('current')
ieee8021PSFPAdminControlListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminControlListLength.setStatus('current')
ieee8021PSFPOperControlListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPOperControlListLength.setStatus('current')
ieee8021PSFPAdminControlList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 7), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminControlList.setStatus('current')
ieee8021PSFPOperControlList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPOperControlList.setStatus('current')
ieee8021PSFPAdminCycleTimeNumerator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminCycleTimeNumerator.setStatus('current')
ieee8021PSFPAdminCycleTimeDenominator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminCycleTimeDenominator.setStatus('current')
ieee8021PSFPOperCycleTimeNumerator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPOperCycleTimeNumerator.setStatus('current')
ieee8021PSFPOperCycleTimeDenominator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPOperCycleTimeDenominator.setStatus('current')
ieee8021PSFPAdminCycleTimeExtension = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 13), Unsigned32()).setUnits('nanoseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminCycleTimeExtension.setStatus('current')
ieee8021PSFPOperCycleTimeExtension = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 14), Unsigned32()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPOperCycleTimeExtension.setStatus('current')
ieee8021PSFPAdminBaseTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 15), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminBaseTime.setStatus('current')
ieee8021PSFPOperBaseTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 16), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPOperBaseTime.setStatus('current')
ieee8021PSFPConfigChange = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 17), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPConfigChange.setStatus('current')
ieee8021PSFPConfigChangeTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 18), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPConfigChangeTime.setStatus('current')
ieee8021PSFPTickGranularity = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPTickGranularity.setStatus('current')
ieee8021PSFPCurrentTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 20), IEEE8021STPTPtimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPCurrentTime.setStatus('current')
ieee8021PSFPConfigPending = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 21), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPConfigPending.setStatus('current')
ieee8021PSFPConfigChangeError = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPConfigChangeError.setStatus('current')
ieee8021PSFPAdminIPV = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPAdminIPV.setStatus('current')
ieee8021PSFPOperIPV = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPOperIPV.setStatus('current')
ieee8021PSFPGateClosedDueToInvalidRxEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 26), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPGateClosedDueToInvalidRxEnable.setStatus('current')
ieee8021PSFPGateClosedDueToInvalidRx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 27), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPGateClosedDueToInvalidRx.setStatus('current')
ieee8021PSFPGateClosedDueToOctetsExceededEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 28), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPGateClosedDueToOctetsExceededEnable.setStatus('current')
ieee8021PSFPGateClosedDueToOctetsExceeded = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 29), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPGateClosedDueToOctetsExceeded.setStatus('current')
ieee8021PSFPStreamGateEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 30), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPStreamGateEntryRowStatus.setStatus('current')
ieee8021PSFPFlowMeterTable = MibTable((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1), )
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterTable.setStatus('current')
ieee8021PSFPFlowMeterEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterInstance"))
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterEntry.setStatus('current')
ieee8021PSFPFlowMeterInstance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterInstance.setStatus('current')
ieee8021PSFPFlowMeterCIR = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterCIR.setStatus('current')
ieee8021PSFPFlowMeterCBS = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterCBS.setStatus('current')
ieee8021PSFPFlowMeterEIR = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterEIR.setStatus('current')
ieee8021PSFPFlowMeterEBS = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterEBS.setStatus('current')
ieee8021PSFPFlowMeterCF = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterCF.setStatus('current')
ieee8021PSFPFlowMeterCM = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("colorBlind", 1), ("colorAware", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterCM.setStatus('current')
ieee8021PSFPFlowMeterDropOnYellow = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterDropOnYellow.setStatus('current')
ieee8021PSFPFlowMeterMarkAllFramesRedEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterMarkAllFramesRedEnable.setStatus('current')
ieee8021PSFPFlowMeterMarkAllFramesRed = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterMarkAllFramesRed.setStatus('current')
ieee8021PSFPFlowMeterEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PSFPFlowMeterEntryRowStatus.setStatus('current')
ieee8021PSFPStreamParameterTable = MibTable((1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1), )
if mibBuilder.loadTexts: ieee8021PSFPStreamParameterTable.setStatus('current')
ieee8021PSFPStreamParameterEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"))
if mibBuilder.loadTexts: ieee8021PSFPStreamParameterEntry.setStatus('current')
ieee8021PSFPMaxStreamFilterInstances = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPMaxStreamFilterInstances.setStatus('current')
ieee8021PSFPMaxStreamGateInstances = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPMaxStreamGateInstances.setStatus('current')
ieee8021PSFPMaxFlowMeterInstances = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPMaxFlowMeterInstances.setStatus('current')
ieee8021PSFPSupportedListMax = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PSFPSupportedListMax.setStatus('current')
ieee8021PSFPCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 2, 1))
ieee8021PSFPGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 31, 2, 2))
ieee8021PSFPObjectsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 31, 2, 2, 1)).setObjects(("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamHandleSpec"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPPrioritySpec"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamGateInstanceID"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFilterSpecificationList"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPMatchingFramesCount"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPPassingFramesCount"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPNotPassingFramesCount"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPPassingSDUCount"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPNotPassingSDUCount"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPREDFramesCount"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamBlockedDueToOversizeFrameEnable"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamBlockedDueToOversizeFrame"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamFilterEntryRowStatus"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateEnabled"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminGateStates"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperGateStates"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminControlListLength"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperControlListLength"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminControlList"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperControlList"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminCycleTimeNumerator"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminCycleTimeDenominator"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperCycleTimeNumerator"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperCycleTimeDenominator"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminCycleTimeExtension"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperCycleTimeExtension"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminBaseTime"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperBaseTime"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigChange"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigChangeTime"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPTickGranularity"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPCurrentTime"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigPending"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigChangeError"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminIPV"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperIPV"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToInvalidRxEnable"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToInvalidRx"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToOctetsExceededEnable"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToOctetsExceeded"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamGateEntryRowStatus"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCIR"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCBS"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterEIR"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterEBS"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCF"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCM"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterDropOnYellow"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterMarkAllFramesRedEnable"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterMarkAllFramesRed"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterEntryRowStatus"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPMaxStreamFilterInstances"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPMaxStreamGateInstances"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPMaxFlowMeterInstances"), ("IEEE8021-PSFP-MIB", "ieee8021PSFPSupportedListMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PSFPObjectsGroup = ieee8021PSFPObjectsGroup.setStatus('current')
ieee8021PSFPCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 31, 2, 1, 1)).setObjects(("IEEE8021-PSFP-MIB", "ieee8021PSFPObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PSFPCompliance = ieee8021PSFPCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PSFP-MIB", ieee8021PSFPMaxFlowMeterInstances=ieee8021PSFPMaxFlowMeterInstances, ieee8021PSFPAdminBaseTime=ieee8021PSFPAdminBaseTime, ieee8021PSFPCompliance=ieee8021PSFPCompliance, ieee8021PSFPObjectsGroup=ieee8021PSFPObjectsGroup, ieee8021PSFPConfigPending=ieee8021PSFPConfigPending, ieee8021PSFPCurrentTime=ieee8021PSFPCurrentTime, ieee8021PSFPFlowMeterMarkAllFramesRed=ieee8021PSFPFlowMeterMarkAllFramesRed, ieee8021PSFPStreamGateInstance=ieee8021PSFPStreamGateInstance, ieee8021PSFPFlowMeterDropOnYellow=ieee8021PSFPFlowMeterDropOnYellow, ieee8021PSFPPassingFramesCount=ieee8021PSFPPassingFramesCount, ieee8021PSFPOperCycleTimeDenominator=ieee8021PSFPOperCycleTimeDenominator, ieee8021PSFPOperBaseTime=ieee8021PSFPOperBaseTime, ieee8021PSFPOperControlList=ieee8021PSFPOperControlList, PYSNMP_MODULE_ID=ieee8021PSFPMib, ieee8021PSFPFlowMeterCIR=ieee8021PSFPFlowMeterCIR, ieee8021PSFPConfigChangeTime=ieee8021PSFPConfigChangeTime, ieee8021PSFPStreamFilterTable=ieee8021PSFPStreamFilterTable, ieee8021PSFPNotPassingFramesCount=ieee8021PSFPNotPassingFramesCount, ieee8021PSFPStreamGateTable=ieee8021PSFPStreamGateTable, ieee8021PSFPAdminCycleTimeNumerator=ieee8021PSFPAdminCycleTimeNumerator, ieee8021PSFPAdminCycleTimeDenominator=ieee8021PSFPAdminCycleTimeDenominator, ieee8021PSFPConfigChange=ieee8021PSFPConfigChange, ieee8021PSFPFlowMeterEntryRowStatus=ieee8021PSFPFlowMeterEntryRowStatus, ieee8021PSFPFlowMeterCF=ieee8021PSFPFlowMeterCF, ieee8021PSFPGateClosedDueToInvalidRx=ieee8021PSFPGateClosedDueToInvalidRx, ieee8021PSFPOperCycleTimeExtension=ieee8021PSFPOperCycleTimeExtension, ieee8021PSFPStreamFilterParameters=ieee8021PSFPStreamFilterParameters, ieee8021PSFPStreamGateEntry=ieee8021PSFPStreamGateEntry, ieee8021PSFPOperCycleTimeNumerator=ieee8021PSFPOperCycleTimeNumerator, ieee8021PSFPFlowMeterCM=ieee8021PSFPFlowMeterCM, ieee8021PSFPPrioritySpec=ieee8021PSFPPrioritySpec, ieee8021PSFPCompliances=ieee8021PSFPCompliances, ieee8021PSFPStreamGateEntryRowStatus=ieee8021PSFPStreamGateEntryRowStatus, ieee8021PSFPFlowMeterParameters=ieee8021PSFPFlowMeterParameters, ieee8021PSFPStreamParameters=ieee8021PSFPStreamParameters, ieee8021PSFPNotPassingSDUCount=ieee8021PSFPNotPassingSDUCount, ieee8021PSFPAdminIPV=ieee8021PSFPAdminIPV, ieee8021PSFPStreamBlockedDueToOversizeFrame=ieee8021PSFPStreamBlockedDueToOversizeFrame, ieee8021PSFPPassingSDUCount=ieee8021PSFPPassingSDUCount, ieee8021PSFPStreamParameterTable=ieee8021PSFPStreamParameterTable, ieee8021PSFPStreamFilterEntry=ieee8021PSFPStreamFilterEntry, ieee8021PSFPStreamHandleSpec=ieee8021PSFPStreamHandleSpec, ieee8021PSFPOperGateStates=ieee8021PSFPOperGateStates, ieee8021PSFPNotifications=ieee8021PSFPNotifications, ieee8021PSFPStreamFilterInstance=ieee8021PSFPStreamFilterInstance, ieee8021PSFPStreamParameterEntry=ieee8021PSFPStreamParameterEntry, ieee8021PSFPStreamFilterEntryRowStatus=ieee8021PSFPStreamFilterEntryRowStatus, ieee8021PSFPFlowMeterTable=ieee8021PSFPFlowMeterTable, ieee8021PSFPOperIPV=ieee8021PSFPOperIPV, ieee8021PSFPAdminCycleTimeExtension=ieee8021PSFPAdminCycleTimeExtension, ieee8021PSFPStreamGateParameters=ieee8021PSFPStreamGateParameters, ieee8021PSFPMatchingFramesCount=ieee8021PSFPMatchingFramesCount, ieee8021PSFPFlowMeterCBS=ieee8021PSFPFlowMeterCBS, ieee8021PSFPStreamBlockedDueToOversizeFrameEnable=ieee8021PSFPStreamBlockedDueToOversizeFrameEnable, ieee8021PSFPConformance=ieee8021PSFPConformance, ieee8021PSFPFlowMeterEntry=ieee8021PSFPFlowMeterEntry, ieee8021PSFPAdminGateStates=ieee8021PSFPAdminGateStates, ieee8021PSFPConfigChangeError=ieee8021PSFPConfigChangeError, ieee8021PSFPGateClosedDueToInvalidRxEnable=ieee8021PSFPGateClosedDueToInvalidRxEnable, ieee8021PSFPGateEnabled=ieee8021PSFPGateEnabled, ieee8021PSFPAdminControlList=ieee8021PSFPAdminControlList, ieee8021PSFPREDFramesCount=ieee8021PSFPREDFramesCount, ieee8021PSFPMaxStreamGateInstances=ieee8021PSFPMaxStreamGateInstances, ieee8021PSFPGroups=ieee8021PSFPGroups, ieee8021PSFPSupportedListMax=ieee8021PSFPSupportedListMax, ieee8021PSFPFlowMeterInstance=ieee8021PSFPFlowMeterInstance, ieee8021PSFPTickGranularity=ieee8021PSFPTickGranularity, ieee8021PSFPOperControlListLength=ieee8021PSFPOperControlListLength, ieee8021PSFPFlowMeterEBS=ieee8021PSFPFlowMeterEBS, ieee8021PSFPStreamGateInstanceID=ieee8021PSFPStreamGateInstanceID, ieee8021PSFPMib=ieee8021PSFPMib, ieee8021PSFPObjects=ieee8021PSFPObjects, ieee8021PSFPAdminControlListLength=ieee8021PSFPAdminControlListLength, ieee8021PSFPFlowMeterMarkAllFramesRedEnable=ieee8021PSFPFlowMeterMarkAllFramesRedEnable, ieee8021PSFPGateClosedDueToOctetsExceeded=ieee8021PSFPGateClosedDueToOctetsExceeded, ieee8021PSFPMaxStreamFilterInstances=ieee8021PSFPMaxStreamFilterInstances, ieee8021PSFPFilterSpecificationList=ieee8021PSFPFilterSpecificationList, ieee8021PSFPFlowMeterEIR=ieee8021PSFPFlowMeterEIR, ieee8021PSFPGateClosedDueToOctetsExceededEnable=ieee8021PSFPGateClosedDueToOctetsExceededEnable)
