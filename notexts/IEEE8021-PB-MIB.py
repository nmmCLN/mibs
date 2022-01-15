#
# PySNMP MIB module IEEE8021-PB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-PB-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ieee8021BridgeBasePort, ieee8021BridgeBasePortComponentId = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort", "ieee8021BridgeBasePortComponentId")
IEEE8021PbbComponentIdentifierOrZero, IEEE8021BridgePortType, IEEE8021PriorityValue, ieee802dot1mibs, IEEE8021BridgePortNumberOrZero, IEEE8021PortAcceptableFrameTypes = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PbbComponentIdentifierOrZero", "IEEE8021BridgePortType", "IEEE8021PriorityValue", "ieee802dot1mibs", "IEEE8021BridgePortNumberOrZero", "IEEE8021PortAcceptableFrameTypes")
VlanId, VlanIdOrNone = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "VlanIdOrNone")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
ieee8021PbMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 5))
ieee8021PbMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2012-02-10 00:00', '2011-04-06 00:00', '2011-02-27 00:00', '2010-08-26 00:00', '2008-10-15 00:00',))
if mibBuilder.loadTexts: ieee8021PbMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021PbMib.setOrganization('IEEE 802.1 Working Group')
ieee8021PbNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 5, 0))
ieee8021PbObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 5, 1))
ieee8021PbConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 5, 2))
ieee8021PbVidTranslationTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 1), )
if mibBuilder.loadTexts: ieee8021PbVidTranslationTable.setStatus('deprecated')
ieee8021PbVidTranslationEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-PB-MIB", "ieee8021PbVidTranslationLocalVid"))
if mibBuilder.loadTexts: ieee8021PbVidTranslationEntry.setStatus('deprecated')
ieee8021PbVidTranslationLocalVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: ieee8021PbVidTranslationLocalVid.setStatus('deprecated')
ieee8021PbVidTranslationRelayVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1, 2), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbVidTranslationRelayVid.setStatus('deprecated')
ieee8021PbVidTranslationRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbVidTranslationRowStatus.setStatus('deprecated')
ieee8021PbCVidRegistrationTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 2), )
if mibBuilder.loadTexts: ieee8021PbCVidRegistrationTable.setStatus('current')
ieee8021PbCVidRegistrationEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationCVid"))
if mibBuilder.loadTexts: ieee8021PbCVidRegistrationEntry.setStatus('current')
ieee8021PbCVidRegistrationCVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: ieee8021PbCVidRegistrationCVid.setStatus('current')
ieee8021PbCVidRegistrationSVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 2), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCVidRegistrationSVid.setStatus('current')
ieee8021PbCVidRegistrationUntaggedPep = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCVidRegistrationUntaggedPep.setStatus('current')
ieee8021PbCVidRegistrationUntaggedCep = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCVidRegistrationUntaggedCep.setStatus('current')
ieee8021PbCVidRegistrationRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCVidRegistrationRowStatus.setStatus('current')
ieee8021PbEdgePortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 3), )
if mibBuilder.loadTexts: ieee8021PbEdgePortTable.setStatus('current')
ieee8021PbEdgePortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-PB-MIB", "ieee8021PbEdgePortSVid"))
if mibBuilder.loadTexts: ieee8021PbEdgePortEntry.setStatus('current')
ieee8021PbEdgePortSVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 1), VlanId())
if mibBuilder.loadTexts: ieee8021PbEdgePortSVid.setStatus('current')
ieee8021PbEdgePortPVID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbEdgePortPVID.setStatus('current')
ieee8021PbEdgePortDefaultUserPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 3), IEEE8021PriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbEdgePortDefaultUserPriority.setStatus('current')
ieee8021PbEdgePortAcceptableFrameTypes = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 4), IEEE8021PortAcceptableFrameTypes().clone('admitAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbEdgePortAcceptableFrameTypes.setStatus('current')
ieee8021PbEdgePortEnableIngressFiltering = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbEdgePortEnableIngressFiltering.setStatus('current')
ieee8021PbServicePriorityRegenerationTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 4), )
if mibBuilder.loadTexts: ieee8021PbServicePriorityRegenerationTable.setStatus('current')
ieee8021PbServicePriorityRegenerationEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationSVid"), (0, "IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationReceivedPriority"))
if mibBuilder.loadTexts: ieee8021PbServicePriorityRegenerationEntry.setStatus('current')
ieee8021PbServicePriorityRegenerationSVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1, 1), VlanId())
if mibBuilder.loadTexts: ieee8021PbServicePriorityRegenerationSVid.setStatus('current')
ieee8021PbServicePriorityRegenerationReceivedPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1, 2), IEEE8021PriorityValue())
if mibBuilder.loadTexts: ieee8021PbServicePriorityRegenerationReceivedPriority.setStatus('current')
ieee8021PbServicePriorityRegenerationRegeneratedPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1, 3), IEEE8021PriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbServicePriorityRegenerationRegeneratedPriority.setStatus('current')
ieee8021PbCnpTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 5), )
if mibBuilder.loadTexts: ieee8021PbCnpTable.setStatus('current')
ieee8021PbCnpEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PbCnpEntry.setStatus('current')
ieee8021PbCnpCComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1, 1), IEEE8021PbbComponentIdentifierOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCnpCComponentId.setStatus('current')
ieee8021PbCnpSVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1, 2), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCnpSVid.setStatus('current')
ieee8021PbCnpRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCnpRowStatus.setStatus('current')
ieee8021PbPnpTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 6), )
if mibBuilder.loadTexts: ieee8021PbPnpTable.setStatus('current')
ieee8021PbPnpEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 6, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PbPnpEntry.setStatus('current')
ieee8021PbPnpRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 6, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbPnpRowStatus.setStatus('current')
ieee8021PbCepTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 7), )
if mibBuilder.loadTexts: ieee8021PbCepTable.setStatus('current')
ieee8021PbCepEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PbCepEntry.setStatus('current')
ieee8021PbCepCComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1, 1), IEEE8021PbbComponentIdentifierOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbCepCComponentId.setStatus('current')
ieee8021PbCepCepPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1, 2), IEEE8021BridgePortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbCepCepPortNumber.setStatus('current')
ieee8021PbCepRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbCepRowStatus.setStatus('current')
ieee8021PbRcapTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 8), )
if mibBuilder.loadTexts: ieee8021PbRcapTable.setStatus('current')
ieee8021PbRcapEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PbRcapEntry.setStatus('current')
ieee8021PbRcapSComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1, 1), IEEE8021PbbComponentIdentifierOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbRcapSComponentId.setStatus('current')
ieee8021PbRcapRcapPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1, 2), IEEE8021BridgePortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbRcapRcapPortNumber.setStatus('current')
ieee8021PbRcapRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbRcapRowStatus.setStatus('current')
ieee8021PbInternalInterfaceTable = MibTable((1, 3, 111, 2, 802, 1, 1, 5, 1, 9), )
if mibBuilder.loadTexts: ieee8021PbInternalInterfaceTable.setStatus('current')
ieee8021PbIiEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-PB-MIB", "ieee8021PbIiExternalSVid"))
if mibBuilder.loadTexts: ieee8021PbIiEntry.setStatus('current')
ieee8021PbIiExternalSVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 1), VlanId())
if mibBuilder.loadTexts: ieee8021PbIiExternalSVid.setStatus('current')
ieee8021PbIiInternalPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 2), IEEE8021BridgePortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbIiInternalPortNumber.setStatus('current')
ieee8021PbIiInternalPortType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 3), IEEE8021BridgePortType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbIiInternalPortType.setStatus('current')
ieee8021PbIiInternalSVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 4), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbIiInternalSVid.setStatus('current')
ieee8021PbIiRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbIiRowStatus.setStatus('current')
ieee8021PbGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 5, 2, 1))
ieee8021PbCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 5, 2, 2))
ieee8021PbVidTranslationGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 1)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbVidTranslationRelayVid"), ("IEEE8021-PB-MIB", "ieee8021PbVidTranslationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbVidTranslationGroup = ieee8021PbVidTranslationGroup.setStatus('deprecated')
ieee8021PbCVidRegistrationGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 2)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationSVid"), ("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationUntaggedPep"), ("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationUntaggedCep"), ("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbCVidRegistrationGroup = ieee8021PbCVidRegistrationGroup.setStatus('current')
ieee8021PbEdgePortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 3)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbEdgePortPVID"), ("IEEE8021-PB-MIB", "ieee8021PbEdgePortDefaultUserPriority"), ("IEEE8021-PB-MIB", "ieee8021PbEdgePortAcceptableFrameTypes"), ("IEEE8021-PB-MIB", "ieee8021PbEdgePortEnableIngressFiltering"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbEdgePortGroup = ieee8021PbEdgePortGroup.setStatus('current')
ieee8021PbServicePriorityRegenerationGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 4)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationRegeneratedPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbServicePriorityRegenerationGroup = ieee8021PbServicePriorityRegenerationGroup.setStatus('current')
ieee8021PbDynamicCnpGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 5)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbCnpCComponentId"), ("IEEE8021-PB-MIB", "ieee8021PbCnpSVid"), ("IEEE8021-PB-MIB", "ieee8021PbCnpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbDynamicCnpGroup = ieee8021PbDynamicCnpGroup.setStatus('current')
ieee8021PbDynamicPnpGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 6)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbPnpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbDynamicPnpGroup = ieee8021PbDynamicPnpGroup.setStatus('current')
ieee8021PbDynamicCepGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 7)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbCepCComponentId"), ("IEEE8021-PB-MIB", "ieee8021PbCepCepPortNumber"), ("IEEE8021-PB-MIB", "ieee8021PbCepRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbDynamicCepGroup = ieee8021PbDynamicCepGroup.setStatus('current')
ieee8021PbDynamicRcapGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 8)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbRcapSComponentId"), ("IEEE8021-PB-MIB", "ieee8021PbRcapRcapPortNumber"), ("IEEE8021-PB-MIB", "ieee8021PbCepRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbDynamicRcapGroup = ieee8021PbDynamicRcapGroup.setStatus('deprecated')
ieee8021PbInternalInterfaceGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 9)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbIiInternalPortNumber"), ("IEEE8021-PB-MIB", "ieee8021PbIiInternalPortType"), ("IEEE8021-PB-MIB", "ieee8021PbIiInternalSVid"), ("IEEE8021-PB-MIB", "ieee8021PbIiRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbInternalInterfaceGroup = ieee8021PbInternalInterfaceGroup.setStatus('current')
ieee8021PbDynamicRcapV2Group = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 10)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbRcapSComponentId"), ("IEEE8021-PB-MIB", "ieee8021PbRcapRcapPortNumber"), ("IEEE8021-PB-MIB", "ieee8021PbRcapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbDynamicRcapV2Group = ieee8021PbDynamicRcapV2Group.setStatus('current')
ieee8021PbCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 5, 2, 2, 1)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbVidTranslationGroup"), ("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationGroup"), ("IEEE8021-PB-MIB", "ieee8021PbEdgePortGroup"), ("IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicCnpGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicPnpGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicCepGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicRcapGroup"), ("IEEE8021-PB-MIB", "ieee8021PbInternalInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbCompliance = ieee8021PbCompliance.setStatus('deprecated')
ieee8021PbComplianceV2 = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 5, 2, 2, 2)).setObjects(("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationGroup"), ("IEEE8021-PB-MIB", "ieee8021PbEdgePortGroup"), ("IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicCnpGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicPnpGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicCepGroup"), ("IEEE8021-PB-MIB", "ieee8021PbDynamicRcapV2Group"), ("IEEE8021-PB-MIB", "ieee8021PbInternalInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbComplianceV2 = ieee8021PbComplianceV2.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PB-MIB", ieee8021PbMib=ieee8021PbMib, ieee8021PbPnpRowStatus=ieee8021PbPnpRowStatus, ieee8021PbServicePriorityRegenerationGroup=ieee8021PbServicePriorityRegenerationGroup, ieee8021PbEdgePortEnableIngressFiltering=ieee8021PbEdgePortEnableIngressFiltering, ieee8021PbCompliance=ieee8021PbCompliance, ieee8021PbCnpRowStatus=ieee8021PbCnpRowStatus, ieee8021PbGroups=ieee8021PbGroups, ieee8021PbCnpTable=ieee8021PbCnpTable, ieee8021PbCVidRegistrationGroup=ieee8021PbCVidRegistrationGroup, PYSNMP_MODULE_ID=ieee8021PbMib, ieee8021PbServicePriorityRegenerationEntry=ieee8021PbServicePriorityRegenerationEntry, ieee8021PbCnpCComponentId=ieee8021PbCnpCComponentId, ieee8021PbCVidRegistrationCVid=ieee8021PbCVidRegistrationCVid, ieee8021PbCVidRegistrationEntry=ieee8021PbCVidRegistrationEntry, ieee8021PbRcapRcapPortNumber=ieee8021PbRcapRcapPortNumber, ieee8021PbEdgePortDefaultUserPriority=ieee8021PbEdgePortDefaultUserPriority, ieee8021PbIiRowStatus=ieee8021PbIiRowStatus, ieee8021PbIiEntry=ieee8021PbIiEntry, ieee8021PbCnpEntry=ieee8021PbCnpEntry, ieee8021PbVidTranslationRowStatus=ieee8021PbVidTranslationRowStatus, ieee8021PbEdgePortAcceptableFrameTypes=ieee8021PbEdgePortAcceptableFrameTypes, ieee8021PbRcapTable=ieee8021PbRcapTable, ieee8021PbCepCepPortNumber=ieee8021PbCepCepPortNumber, ieee8021PbInternalInterfaceGroup=ieee8021PbInternalInterfaceGroup, ieee8021PbRcapSComponentId=ieee8021PbRcapSComponentId, ieee8021PbIiInternalSVid=ieee8021PbIiInternalSVid, ieee8021PbVidTranslationLocalVid=ieee8021PbVidTranslationLocalVid, ieee8021PbEdgePortEntry=ieee8021PbEdgePortEntry, ieee8021PbServicePriorityRegenerationTable=ieee8021PbServicePriorityRegenerationTable, ieee8021PbDynamicRcapGroup=ieee8021PbDynamicRcapGroup, ieee8021PbVidTranslationEntry=ieee8021PbVidTranslationEntry, ieee8021PbRcapEntry=ieee8021PbRcapEntry, ieee8021PbServicePriorityRegenerationSVid=ieee8021PbServicePriorityRegenerationSVid, ieee8021PbEdgePortSVid=ieee8021PbEdgePortSVid, ieee8021PbDynamicPnpGroup=ieee8021PbDynamicPnpGroup, ieee8021PbCepEntry=ieee8021PbCepEntry, ieee8021PbRcapRowStatus=ieee8021PbRcapRowStatus, ieee8021PbIiExternalSVid=ieee8021PbIiExternalSVid, ieee8021PbEdgePortGroup=ieee8021PbEdgePortGroup, ieee8021PbEdgePortPVID=ieee8021PbEdgePortPVID, ieee8021PbPnpTable=ieee8021PbPnpTable, ieee8021PbIiInternalPortNumber=ieee8021PbIiInternalPortNumber, ieee8021PbCompliances=ieee8021PbCompliances, ieee8021PbNotifications=ieee8021PbNotifications, ieee8021PbCVidRegistrationRowStatus=ieee8021PbCVidRegistrationRowStatus, ieee8021PbCepRowStatus=ieee8021PbCepRowStatus, ieee8021PbPnpEntry=ieee8021PbPnpEntry, ieee8021PbServicePriorityRegenerationRegeneratedPriority=ieee8021PbServicePriorityRegenerationRegeneratedPriority, ieee8021PbCVidRegistrationTable=ieee8021PbCVidRegistrationTable, ieee8021PbServicePriorityRegenerationReceivedPriority=ieee8021PbServicePriorityRegenerationReceivedPriority, ieee8021PbDynamicCnpGroup=ieee8021PbDynamicCnpGroup, ieee8021PbInternalInterfaceTable=ieee8021PbInternalInterfaceTable, ieee8021PbIiInternalPortType=ieee8021PbIiInternalPortType, ieee8021PbDynamicRcapV2Group=ieee8021PbDynamicRcapV2Group, ieee8021PbCepCComponentId=ieee8021PbCepCComponentId, ieee8021PbEdgePortTable=ieee8021PbEdgePortTable, ieee8021PbVidTranslationGroup=ieee8021PbVidTranslationGroup, ieee8021PbComplianceV2=ieee8021PbComplianceV2, ieee8021PbCnpSVid=ieee8021PbCnpSVid, ieee8021PbObjects=ieee8021PbObjects, ieee8021PbVidTranslationTable=ieee8021PbVidTranslationTable, ieee8021PbCepTable=ieee8021PbCepTable, ieee8021PbCVidRegistrationUntaggedPep=ieee8021PbCVidRegistrationUntaggedPep, ieee8021PbCVidRegistrationUntaggedCep=ieee8021PbCVidRegistrationUntaggedCep, ieee8021PbDynamicCepGroup=ieee8021PbDynamicCepGroup, ieee8021PbVidTranslationRelayVid=ieee8021PbVidTranslationRelayVid, ieee8021PbConformance=ieee8021PbConformance, ieee8021PbCVidRegistrationSVid=ieee8021PbCVidRegistrationSVid)
