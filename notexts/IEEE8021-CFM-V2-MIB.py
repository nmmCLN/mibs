#
# PySNMP MIB module IEEE8021-CFM-V2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-CFM-V2-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
Dot1agCfmMDLevelOrNone, dot1agCfmStack, dot1agCfmConfigErrorList, ieee8021CfmDefaultMdDefGroup, Dot1agCfmConfigErrors, Dot1agCfmMhfCreation, dot1agCfmVlan, dot1agCfmMepGroup, ieee8021CfmMaNetGroup, ieee8021CfmPbbTeExtensionGroup, dot1agCfmMepRowStatus, dot1agCfmNotificationsGroup, Dot1agCfmMDLevel, Dot1agCfmMpDirection, Dot1agCfmMepIdOrZero, dot1agCfmCompliances, Dot1agCfmIdPermission, dot1agCfmMaMepListRowStatus, dot1agCfmMdRowStatus, dot1agCfmMdIndex, dot1agCfmDefaultMd, dot1agCfmMa, dot1agCfmMdGroup, dot1agCfmGroups, dot1agCfmMaIndex, dot1agCfmMaNetRowStatus, ieee8021CfmPbbTeTrafficBitGroup, dot1agCfmMepDbGroup, dot1agCfmMepLbrBadMsdu = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMDLevelOrNone", "dot1agCfmStack", "dot1agCfmConfigErrorList", "ieee8021CfmDefaultMdDefGroup", "Dot1agCfmConfigErrors", "Dot1agCfmMhfCreation", "dot1agCfmVlan", "dot1agCfmMepGroup", "ieee8021CfmMaNetGroup", "ieee8021CfmPbbTeExtensionGroup", "dot1agCfmMepRowStatus", "dot1agCfmNotificationsGroup", "Dot1agCfmMDLevel", "Dot1agCfmMpDirection", "Dot1agCfmMepIdOrZero", "dot1agCfmCompliances", "Dot1agCfmIdPermission", "dot1agCfmMaMepListRowStatus", "dot1agCfmMdRowStatus", "dot1agCfmMdIndex", "dot1agCfmDefaultMd", "dot1agCfmMa", "dot1agCfmMdGroup", "dot1agCfmGroups", "dot1agCfmMaIndex", "dot1agCfmMaNetRowStatus", "ieee8021CfmPbbTeTrafficBitGroup", "dot1agCfmMepDbGroup", "dot1agCfmMepLbrBadMsdu")
IEEE8021ServiceSelectorType, IEEE8021ServiceSelectorValue, ieee802dot1mibs, IEEE8021PbbComponentIdentifier, IEEE8021ServiceSelectorValueOrNone = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021ServiceSelectorType", "IEEE8021ServiceSelectorValue", "ieee802dot1mibs", "IEEE8021PbbComponentIdentifier", "IEEE8021ServiceSelectorValueOrNone")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TruthValue, TextualConvention, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus", "MacAddress")
ieee8021CfmV2Mib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 7))
ieee8021CfmV2Mib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2011-02-27 00:00', '2008-11-18 00:00', '2008-10-15 00:00',))
if mibBuilder.loadTexts: ieee8021CfmV2Mib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021CfmV2Mib.setOrganization('IEEE 802.1 Working Group')
ieee8021CfmStackTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2), )
if mibBuilder.loadTexts: ieee8021CfmStackTable.setStatus('current')
ieee8021CfmStackEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackifIndex"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackServiceSelectorType"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackServiceSelectorOrNone"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMdLevel"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackDirection"))
if mibBuilder.loadTexts: ieee8021CfmStackEntry.setStatus('current')
ieee8021CfmStackifIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021CfmStackifIndex.setStatus('current')
ieee8021CfmStackServiceSelectorType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 2), IEEE8021ServiceSelectorType())
if mibBuilder.loadTexts: ieee8021CfmStackServiceSelectorType.setStatus('current')
ieee8021CfmStackServiceSelectorOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 3), IEEE8021ServiceSelectorValueOrNone())
if mibBuilder.loadTexts: ieee8021CfmStackServiceSelectorOrNone.setStatus('current')
ieee8021CfmStackMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 4), Dot1agCfmMDLevel())
if mibBuilder.loadTexts: ieee8021CfmStackMdLevel.setStatus('current')
ieee8021CfmStackDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 5), Dot1agCfmMpDirection())
if mibBuilder.loadTexts: ieee8021CfmStackDirection.setStatus('current')
ieee8021CfmStackMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021CfmStackMdIndex.setStatus('current')
ieee8021CfmStackMaIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021CfmStackMaIndex.setStatus('current')
ieee8021CfmStackMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 8), Dot1agCfmMepIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021CfmStackMepId.setStatus('current')
ieee8021CfmStackMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021CfmStackMacAddress.setStatus('current')
ieee8021CfmVlanTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2), )
if mibBuilder.loadTexts: ieee8021CfmVlanTable.setStatus('current')
ieee8021CfmVlanEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanComponentId"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanSelector"))
if mibBuilder.loadTexts: ieee8021CfmVlanEntry.setStatus('current')
ieee8021CfmVlanComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021CfmVlanComponentId.setStatus('current')
ieee8021CfmVlanSelector = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 3), IEEE8021ServiceSelectorValue())
if mibBuilder.loadTexts: ieee8021CfmVlanSelector.setStatus('current')
ieee8021CfmVlanPrimarySelector = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 5), IEEE8021ServiceSelectorValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmVlanPrimarySelector.setStatus('current')
ieee8021CfmVlanRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmVlanRowStatus.setStatus('current')
ieee8021CfmDefaultMdTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5), )
if mibBuilder.loadTexts: ieee8021CfmDefaultMdTable.setStatus('current')
ieee8021CfmDefaultMdEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1), ).setIndexNames((0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdComponentId"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdPrimarySelectorType"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdPrimarySelector"))
if mibBuilder.loadTexts: ieee8021CfmDefaultMdEntry.setStatus('current')
ieee8021CfmDefaultMdComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021CfmDefaultMdComponentId.setStatus('current')
ieee8021CfmDefaultMdPrimarySelectorType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 2), IEEE8021ServiceSelectorType())
if mibBuilder.loadTexts: ieee8021CfmDefaultMdPrimarySelectorType.setStatus('current')
ieee8021CfmDefaultMdPrimarySelector = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 3), IEEE8021ServiceSelectorValue())
if mibBuilder.loadTexts: ieee8021CfmDefaultMdPrimarySelector.setStatus('current')
ieee8021CfmDefaultMdStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021CfmDefaultMdStatus.setStatus('current')
ieee8021CfmDefaultMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 5), Dot1agCfmMDLevelOrNone().clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021CfmDefaultMdLevel.setStatus('current')
ieee8021CfmDefaultMdMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 6), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021CfmDefaultMdMhfCreation.setStatus('current')
ieee8021CfmDefaultMdIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 7), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021CfmDefaultMdIdPermission.setStatus('current')
ieee8021CfmConfigErrorListTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2), )
if mibBuilder.loadTexts: ieee8021CfmConfigErrorListTable.setStatus('current')
ieee8021CfmConfigErrorListEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListSelectorType"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListSelector"), (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListIfIndex"))
if mibBuilder.loadTexts: ieee8021CfmConfigErrorListEntry.setStatus('current')
ieee8021CfmConfigErrorListSelectorType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 1), IEEE8021ServiceSelectorType())
if mibBuilder.loadTexts: ieee8021CfmConfigErrorListSelectorType.setStatus('current')
ieee8021CfmConfigErrorListSelector = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 2), IEEE8021ServiceSelectorValue())
if mibBuilder.loadTexts: ieee8021CfmConfigErrorListSelector.setStatus('current')
ieee8021CfmConfigErrorListIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021CfmConfigErrorListIfIndex.setStatus('current')
ieee8021CfmConfigErrorListErrorType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 4), Dot1agCfmConfigErrors()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021CfmConfigErrorListErrorType.setStatus('current')
ieee8021CfmMaCompTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4), )
if mibBuilder.loadTexts: ieee8021CfmMaCompTable.setStatus('current')
ieee8021CfmMaCompEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1), ).setIndexNames((0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmMaComponentId"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"))
if mibBuilder.loadTexts: ieee8021CfmMaCompEntry.setStatus('current')
ieee8021CfmMaComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021CfmMaComponentId.setStatus('current')
ieee8021CfmMaCompPrimarySelectorType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 2), IEEE8021ServiceSelectorType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmMaCompPrimarySelectorType.setStatus('current')
ieee8021CfmMaCompPrimarySelectorOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 3), IEEE8021ServiceSelectorValueOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmMaCompPrimarySelectorOrNone.setStatus('current')
ieee8021CfmMaCompMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 4), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmMaCompMhfCreation.setStatus('current')
ieee8021CfmMaCompIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 5), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmMaCompIdPermission.setStatus('current')
ieee8021CfmMaCompNumberOfVids = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmMaCompNumberOfVids.setStatus('current')
ieee8021CfmMaCompRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021CfmMaCompRowStatus.setStatus('current')
ieee8021CfmStackGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 12)).setObjects(("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMdIndex"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMaIndex"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMepId"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmStackGroup = ieee8021CfmStackGroup.setStatus('current')
ieee8021CfmMaGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 13)).setObjects(("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompPrimarySelectorType"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompPrimarySelectorOrNone"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompMhfCreation"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompIdPermission"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompRowStatus"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompNumberOfVids"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmMaGroup = ieee8021CfmMaGroup.setStatus('current')
ieee8021CfmDefaultMdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 14)).setObjects(("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdStatus"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdLevel"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdMhfCreation"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdIdPermission"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmDefaultMdGroup = ieee8021CfmDefaultMdGroup.setStatus('current')
ieee8021CfmVlanIdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 15)).setObjects(("IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanPrimarySelector"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmVlanIdGroup = ieee8021CfmVlanIdGroup.setStatus('current')
ieee8021CfmConfigErrorListGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 16)).setObjects(("IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListErrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmConfigErrorListGroup = ieee8021CfmConfigErrorListGroup.setStatus('current')
ieee8021CfmComplianceV2 = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 8, 2, 1, 2)).setObjects(("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanIdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmNotificationsGroup"), ("IEEE8021-CFM-MIB", "ieee8021CfmDefaultMdDefGroup"), ("IEEE8021-CFM-MIB", "ieee8021CfmMaNetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmComplianceV2 = ieee8021CfmComplianceV2.setStatus('current')
dot1agCfmWithPbbTeCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 8, 2, 1, 3)).setObjects(("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListGroup"), ("IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanIdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmNotificationsGroup"), ("IEEE8021-CFM-MIB", "ieee8021CfmDefaultMdDefGroup"), ("IEEE8021-CFM-MIB", "ieee8021CfmMaNetGroup"), ("IEEE8021-CFM-MIB", "ieee8021CfmPbbTeExtensionGroup"), ("IEEE8021-CFM-MIB", "ieee8021CfmPbbTeTrafficBitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmWithPbbTeCompliance = dot1agCfmWithPbbTeCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-CFM-V2-MIB", ieee8021CfmVlanEntry=ieee8021CfmVlanEntry, ieee8021CfmMaCompIdPermission=ieee8021CfmMaCompIdPermission, ieee8021CfmDefaultMdIdPermission=ieee8021CfmDefaultMdIdPermission, ieee8021CfmConfigErrorListGroup=ieee8021CfmConfigErrorListGroup, ieee8021CfmDefaultMdPrimarySelectorType=ieee8021CfmDefaultMdPrimarySelectorType, ieee8021CfmMaGroup=ieee8021CfmMaGroup, ieee8021CfmConfigErrorListTable=ieee8021CfmConfigErrorListTable, ieee8021CfmComplianceV2=ieee8021CfmComplianceV2, ieee8021CfmStackTable=ieee8021CfmStackTable, ieee8021CfmDefaultMdStatus=ieee8021CfmDefaultMdStatus, ieee8021CfmStackMdIndex=ieee8021CfmStackMdIndex, ieee8021CfmVlanComponentId=ieee8021CfmVlanComponentId, ieee8021CfmMaCompRowStatus=ieee8021CfmMaCompRowStatus, ieee8021CfmStackGroup=ieee8021CfmStackGroup, ieee8021CfmMaCompEntry=ieee8021CfmMaCompEntry, ieee8021CfmVlanIdGroup=ieee8021CfmVlanIdGroup, ieee8021CfmMaCompNumberOfVids=ieee8021CfmMaCompNumberOfVids, ieee8021CfmConfigErrorListSelectorType=ieee8021CfmConfigErrorListSelectorType, ieee8021CfmDefaultMdPrimarySelector=ieee8021CfmDefaultMdPrimarySelector, ieee8021CfmConfigErrorListIfIndex=ieee8021CfmConfigErrorListIfIndex, ieee8021CfmStackEntry=ieee8021CfmStackEntry, ieee8021CfmVlanTable=ieee8021CfmVlanTable, ieee8021CfmStackServiceSelectorType=ieee8021CfmStackServiceSelectorType, PYSNMP_MODULE_ID=ieee8021CfmV2Mib, ieee8021CfmStackMacAddress=ieee8021CfmStackMacAddress, ieee8021CfmVlanRowStatus=ieee8021CfmVlanRowStatus, ieee8021CfmMaCompTable=ieee8021CfmMaCompTable, ieee8021CfmMaComponentId=ieee8021CfmMaComponentId, ieee8021CfmDefaultMdGroup=ieee8021CfmDefaultMdGroup, ieee8021CfmMaCompMhfCreation=ieee8021CfmMaCompMhfCreation, ieee8021CfmVlanPrimarySelector=ieee8021CfmVlanPrimarySelector, ieee8021CfmStackMaIndex=ieee8021CfmStackMaIndex, ieee8021CfmConfigErrorListErrorType=ieee8021CfmConfigErrorListErrorType, ieee8021CfmMaCompPrimarySelectorType=ieee8021CfmMaCompPrimarySelectorType, ieee8021CfmStackDirection=ieee8021CfmStackDirection, ieee8021CfmStackServiceSelectorOrNone=ieee8021CfmStackServiceSelectorOrNone, ieee8021CfmDefaultMdMhfCreation=ieee8021CfmDefaultMdMhfCreation, ieee8021CfmDefaultMdLevel=ieee8021CfmDefaultMdLevel, ieee8021CfmDefaultMdComponentId=ieee8021CfmDefaultMdComponentId, ieee8021CfmVlanSelector=ieee8021CfmVlanSelector, ieee8021CfmStackifIndex=ieee8021CfmStackifIndex, ieee8021CfmV2Mib=ieee8021CfmV2Mib, ieee8021CfmConfigErrorListEntry=ieee8021CfmConfigErrorListEntry, ieee8021CfmMaCompPrimarySelectorOrNone=ieee8021CfmMaCompPrimarySelectorOrNone, ieee8021CfmStackMdLevel=ieee8021CfmStackMdLevel, dot1agCfmWithPbbTeCompliance=dot1agCfmWithPbbTeCompliance, ieee8021CfmDefaultMdEntry=ieee8021CfmDefaultMdEntry, ieee8021CfmStackMepId=ieee8021CfmStackMepId, ieee8021CfmDefaultMdTable=ieee8021CfmDefaultMdTable, ieee8021CfmConfigErrorListSelector=ieee8021CfmConfigErrorListSelector)
