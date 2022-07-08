#
# PySNMP MIB module IEEE8021-MSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-MSTP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:11:34 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
BridgeId, = mibBuilder.importSymbols("BRIDGE-MIB", "BridgeId")
IEEE8021VlanIndex, IEEE8021BridgePortNumber, IEEE8021MstIdentifier, IEEE8021PbbComponentIdentifier, ieee802dot1mibs = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021VlanIndex", "IEEE8021BridgePortNumber", "IEEE8021MstIdentifier", "IEEE8021PbbComponentIdentifier", "ieee802dot1mibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Bits, iso, ObjectIdentity, MibIdentifier, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, ModuleIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Bits", "iso", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "ModuleIdentity", "NotificationType", "Integer32")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
ieee8021MstpMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 6))
ieee8021MstpMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2012-08-10 00:00', '2011-12-12 00:00', '2011-03-23 00:00', '2008-10-15 00:00',))
if mibBuilder.loadTexts: ieee8021MstpMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021MstpMib.setOrganization('IEEE 802.1 Working Group')
ieee8021MstpNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 6, 0))
ieee8021MstpObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 6, 1))
ieee8021MstpConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 6, 2))
ieee8021MstpCistTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 1), )
if mibBuilder.loadTexts: ieee8021MstpCistTable.setStatus('current')
ieee8021MstpCistEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpCistComponentId"))
if mibBuilder.loadTexts: ieee8021MstpCistEntry.setStatus('current')
ieee8021MstpCistComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpCistComponentId.setStatus('current')
ieee8021MstpCistBridgeIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 2), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistBridgeIdentifier.setStatus('current')
ieee8021MstpCistTopologyChange = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistTopologyChange.setStatus('current')
ieee8021MstpCistRegionalRootIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 4), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistRegionalRootIdentifier.setStatus('current')
ieee8021MstpCistPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPathCost.setStatus('current')
ieee8021MstpCistMaxHops = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistMaxHops.setStatus('current')
ieee8021MstpTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 2), )
if mibBuilder.loadTexts: ieee8021MstpTable.setStatus('current')
ieee8021MstpEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpComponentId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpId"))
if mibBuilder.loadTexts: ieee8021MstpEntry.setStatus('current')
ieee8021MstpComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpComponentId.setStatus('current')
ieee8021MstpId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 2), IEEE8021MstIdentifier())
if mibBuilder.loadTexts: ieee8021MstpId.setStatus('current')
ieee8021MstpBridgeId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 3), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpBridgeId.setStatus('current')
ieee8021MstpTimeSinceTopologyChange = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 4), TimeTicks()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpTimeSinceTopologyChange.setStatus('current')
ieee8021MstpTopologyChanges = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 5), Counter64()).setUnits('topology changes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpTopologyChanges.setStatus('current')
ieee8021MstpTopologyChange = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpTopologyChange.setStatus('current')
ieee8021MstpDesignatedRoot = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 7), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpDesignatedRoot.setStatus('current')
ieee8021MstpRootPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpRootPathCost.setStatus('current')
ieee8021MstpRootPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 9), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpRootPort.setStatus('current')
ieee8021MstpBridgePriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MstpBridgePriority.setStatus('current')
ieee8021MstpVids0 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpVids0.setStatus('current')
ieee8021MstpVids1 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpVids1.setStatus('current')
ieee8021MstpVids2 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpVids2.setStatus('current')
ieee8021MstpVids3 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpVids3.setStatus('current')
ieee8021MstpRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MstpRowStatus.setStatus('current')
ieee8021MstpCistPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 3), )
if mibBuilder.loadTexts: ieee8021MstpCistPortTable.setStatus('current')
ieee8021MstpCistPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpCistPortComponentId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpCistPortNum"))
if mibBuilder.loadTexts: ieee8021MstpCistPortEntry.setStatus('current')
ieee8021MstpCistPortComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpCistPortComponentId.setStatus('current')
ieee8021MstpCistPortNum = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 2), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: ieee8021MstpCistPortNum.setStatus('current')
ieee8021MstpCistPortUptime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 3), TimeTicks()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortUptime.setStatus('current')
ieee8021MstpCistPortAdminPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortAdminPathCost.setStatus('current')
ieee8021MstpCistPortDesignatedRoot = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortDesignatedRoot.setStatus('current')
ieee8021MstpCistPortTopologyChangeAck = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortTopologyChangeAck.setStatus('current')
ieee8021MstpCistPortHelloTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortHelloTime.setStatus('current')
ieee8021MstpCistPortAdminEdgePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortAdminEdgePort.setStatus('current')
ieee8021MstpCistPortOperEdgePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortOperEdgePort.setStatus('current')
ieee8021MstpCistPortMacEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortMacEnabled.setStatus('current')
ieee8021MstpCistPortMacOperational = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortMacOperational.setStatus('current')
ieee8021MstpCistPortRestrictedRole = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortRestrictedRole.setStatus('current')
ieee8021MstpCistPortRestrictedTcn = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortRestrictedTcn.setStatus('current')
ieee8021MstpCistPortRole = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("root", 1), ("alternate", 2), ("designated", 3), ("backup", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortRole.setStatus('current')
ieee8021MstpCistPortDisputed = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortDisputed.setStatus('current')
ieee8021MstpCistPortCistRegionalRootId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 16), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortCistRegionalRootId.setStatus('current')
ieee8021MstpCistPortCistPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortCistPathCost.setStatus('current')
ieee8021MstpCistPortProtocolMigration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortProtocolMigration.setStatus('current')
ieee8021MstpCistPortEnableBPDURx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 19), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortEnableBPDURx.setStatus('current')
ieee8021MstpCistPortEnableBPDUTx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 20), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortEnableBPDUTx.setStatus('current')
ieee8021MstpCistPortPseudoRootId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 21), BridgeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortPseudoRootId.setStatus('current')
ieee8021MstpCistPortIsL2Gp = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 22), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortIsL2Gp.setStatus('current')
ieee8021MstpPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 4), )
if mibBuilder.loadTexts: ieee8021MstpPortTable.setStatus('current')
ieee8021MstpPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpPortComponentId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpPortMstId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpPortNum"))
if mibBuilder.loadTexts: ieee8021MstpPortEntry.setStatus('current')
ieee8021MstpPortComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpPortComponentId.setStatus('current')
ieee8021MstpPortMstId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 2), IEEE8021MstIdentifier())
if mibBuilder.loadTexts: ieee8021MstpPortMstId.setStatus('current')
ieee8021MstpPortNum = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 3), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: ieee8021MstpPortNum.setStatus('current')
ieee8021MstpPortUptime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 4), TimeTicks()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortUptime.setStatus('current')
ieee8021MstpPortState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("listening", 2), ("learning", 3), ("forwarding", 4), ("blocking", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortState.setStatus('current')
ieee8021MstpPortPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpPortPriority.setStatus('current')
ieee8021MstpPortPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpPortPathCost.setStatus('current')
ieee8021MstpPortDesignatedRoot = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 8), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortDesignatedRoot.setStatus('current')
ieee8021MstpPortDesignatedCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortDesignatedCost.setStatus('current')
ieee8021MstpPortDesignatedBridge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 10), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortDesignatedBridge.setStatus('current')
ieee8021MstpPortDesignatedPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 11), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortDesignatedPort.setStatus('current')
ieee8021MstpPortRole = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("root", 1), ("alternate", 2), ("designated", 3), ("backup", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortRole.setStatus('current')
ieee8021MstpPortDisputed = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpPortDisputed.setStatus('current')
ieee8021MstpPortAdminPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpPortAdminPathCost.setStatus('current')
ieee8021MstpFidToMstiTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 5), )
if mibBuilder.loadTexts: ieee8021MstpFidToMstiTable.setStatus('deprecated')
ieee8021MstpFidToMstiEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiComponentId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiFid"))
if mibBuilder.loadTexts: ieee8021MstpFidToMstiEntry.setStatus('deprecated')
ieee8021MstpFidToMstiComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpFidToMstiComponentId.setStatus('deprecated')
ieee8021MstpFidToMstiFid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: ieee8021MstpFidToMstiFid.setStatus('deprecated')
ieee8021MstpFidToMstiMstId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1, 3), IEEE8021MstIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpFidToMstiMstId.setStatus('deprecated')
ieee8021MstpFidToMstiV2Table = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 9), )
if mibBuilder.loadTexts: ieee8021MstpFidToMstiV2Table.setStatus('current')
ieee8021MstpFidToMstiV2Entry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiV2ComponentId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiV2Fid"))
if mibBuilder.loadTexts: ieee8021MstpFidToMstiV2Entry.setStatus('current')
ieee8021MstpFidToMstiV2ComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpFidToMstiV2ComponentId.setStatus('current')
ieee8021MstpFidToMstiV2Fid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: ieee8021MstpFidToMstiV2Fid.setStatus('current')
ieee8021MstpFidToMstiV2MstId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpFidToMstiV2MstId.setStatus('current')
ieee8021MstpVlanTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 6), )
if mibBuilder.loadTexts: ieee8021MstpVlanTable.setStatus('deprecated')
ieee8021MstpVlanEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanComponentId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanId"))
if mibBuilder.loadTexts: ieee8021MstpVlanEntry.setStatus('deprecated')
ieee8021MstpVlanComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpVlanComponentId.setStatus('deprecated')
ieee8021MstpVlanId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1, 2), IEEE8021VlanIndex())
if mibBuilder.loadTexts: ieee8021MstpVlanId.setStatus('deprecated')
ieee8021MstpVlanMstId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1, 3), IEEE8021MstIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpVlanMstId.setStatus('deprecated')
ieee8021MstpVlanV2Table = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 10), )
if mibBuilder.loadTexts: ieee8021MstpVlanV2Table.setStatus('current')
ieee8021MstpVlanV2Entry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanV2ComponentId"), (0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanV2Id"))
if mibBuilder.loadTexts: ieee8021MstpVlanV2Entry.setStatus('current')
ieee8021MstpVlanV2ComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpVlanV2ComponentId.setStatus('current')
ieee8021MstpVlanV2Id = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1, 2), IEEE8021VlanIndex())
if mibBuilder.loadTexts: ieee8021MstpVlanV2Id.setStatus('current')
ieee8021MstpVlanV2MstId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpVlanV2MstId.setStatus('current')
ieee8021MstpConfigIdTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 7), )
if mibBuilder.loadTexts: ieee8021MstpConfigIdTable.setStatus('current')
ieee8021MstpConfigIdEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1), ).setIndexNames((0, "IEEE8021-MSTP-MIB", "ieee8021MstpConfigIdComponentId"))
if mibBuilder.loadTexts: ieee8021MstpConfigIdEntry.setStatus('current')
ieee8021MstpConfigIdComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021MstpConfigIdComponentId.setStatus('current')
ieee8021MstpConfigIdFormatSelector = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpConfigIdFormatSelector.setStatus('current')
ieee8021MstpConfigurationName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpConfigurationName.setStatus('current')
ieee8021MstpRevisionLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpRevisionLevel.setStatus('current')
ieee8021MstpConfigurationDigest = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpConfigurationDigest.setStatus('current')
ieee8021MstpCistPortExtensionTable = MibTable((1, 3, 111, 2, 802, 1, 1, 6, 1, 8), )
if mibBuilder.loadTexts: ieee8021MstpCistPortExtensionTable.setStatus('current')
ieee8021MstpCistPortExtensionEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 6, 1, 8, 1), )
ieee8021MstpCistPortEntry.registerAugmentions(("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortExtensionEntry"))
ieee8021MstpCistPortExtensionEntry.setIndexNames(*ieee8021MstpCistPortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021MstpCistPortExtensionEntry.setStatus('current')
ieee8021MstpCistPortAutoEdgePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 8, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021MstpCistPortAutoEdgePort.setStatus('current')
ieee8021MstpCistPortAutoIsolatePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 6, 1, 8, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021MstpCistPortAutoIsolatePort.setStatus('current')
ieee8021MstpGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 6, 2, 1))
ieee8021MstpCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 6, 2, 2))
ieee8021MstpCistGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 1)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpCistBridgeIdentifier"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistTopologyChange"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistRegionalRootIdentifier"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPathCost"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistMaxHops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpCistGroup = ieee8021MstpCistGroup.setStatus('current')
ieee8021MstpGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 2)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpBridgeId"), ("IEEE8021-MSTP-MIB", "ieee8021MstpTimeSinceTopologyChange"), ("IEEE8021-MSTP-MIB", "ieee8021MstpTopologyChanges"), ("IEEE8021-MSTP-MIB", "ieee8021MstpTopologyChange"), ("IEEE8021-MSTP-MIB", "ieee8021MstpDesignatedRoot"), ("IEEE8021-MSTP-MIB", "ieee8021MstpRootPathCost"), ("IEEE8021-MSTP-MIB", "ieee8021MstpRootPort"), ("IEEE8021-MSTP-MIB", "ieee8021MstpBridgePriority"), ("IEEE8021-MSTP-MIB", "ieee8021MstpVids0"), ("IEEE8021-MSTP-MIB", "ieee8021MstpVids1"), ("IEEE8021-MSTP-MIB", "ieee8021MstpVids2"), ("IEEE8021-MSTP-MIB", "ieee8021MstpVids3"), ("IEEE8021-MSTP-MIB", "ieee8021MstpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpGroup = ieee8021MstpGroup.setStatus('current')
ieee8021MstpCistPortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 3)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortUptime"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAdminPathCost"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortDesignatedRoot"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortTopologyChangeAck"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortHelloTime"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAdminEdgePort"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortOperEdgePort"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortMacEnabled"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortMacOperational"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortRestrictedRole"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortRestrictedTcn"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortRole"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortDisputed"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortCistRegionalRootId"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortCistPathCost"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortProtocolMigration"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortEnableBPDURx"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortEnableBPDUTx"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortPseudoRootId"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortIsL2Gp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpCistPortGroup = ieee8021MstpCistPortGroup.setStatus('current')
ieee8021MstpPortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 4)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpPortUptime"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortState"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortPriority"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortPathCost"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedRoot"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedCost"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedBridge"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedPort"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortRole"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDisputed"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortAdminPathCost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpPortGroup = ieee8021MstpPortGroup.setStatus('current')
ieee8021MstpFidToMstiGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 5)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiMstId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpFidToMstiGroup = ieee8021MstpFidToMstiGroup.setStatus('deprecated')
ieee8021MstpVlanGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 6)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpVlanMstId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpVlanGroup = ieee8021MstpVlanGroup.setStatus('deprecated')
ieee8021MstpConfigIdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 7)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpConfigIdFormatSelector"), ("IEEE8021-MSTP-MIB", "ieee8021MstpConfigurationName"), ("IEEE8021-MSTP-MIB", "ieee8021MstpRevisionLevel"), ("IEEE8021-MSTP-MIB", "ieee8021MstpConfigurationDigest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpConfigIdGroup = ieee8021MstpConfigIdGroup.setStatus('current')
ieee8021MstpCistPortExtensionGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 8)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAutoEdgePort"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAutoIsolatePort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpCistPortExtensionGroup = ieee8021MstpCistPortExtensionGroup.setStatus('current')
ieee8021MstpFidToMstiV2Group = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 9)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiV2MstId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpFidToMstiV2Group = ieee8021MstpFidToMstiV2Group.setStatus('current')
ieee8021MstpVlanV2Group = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 10)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpVlanV2MstId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpVlanV2Group = ieee8021MstpVlanV2Group.setStatus('current')
ieee8021MstpCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 6, 2, 2, 1)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpCistGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpVlanGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpConfigIdGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortExtensionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpCompliance = ieee8021MstpCompliance.setStatus('deprecated')
ieee8021MstpComplianceV2 = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 6, 2, 2, 2)).setObjects(("IEEE8021-MSTP-MIB", "ieee8021MstpCistGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpPortGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiV2Group"), ("IEEE8021-MSTP-MIB", "ieee8021MstpVlanV2Group"), ("IEEE8021-MSTP-MIB", "ieee8021MstpConfigIdGroup"), ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortExtensionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MstpComplianceV2 = ieee8021MstpComplianceV2.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-MSTP-MIB", ieee8021MstpCistPortExtensionEntry=ieee8021MstpCistPortExtensionEntry, ieee8021MstpCistPortEnableBPDUTx=ieee8021MstpCistPortEnableBPDUTx, ieee8021MstpTable=ieee8021MstpTable, ieee8021MstpFidToMstiGroup=ieee8021MstpFidToMstiGroup, ieee8021MstpTopologyChange=ieee8021MstpTopologyChange, ieee8021MstpPortNum=ieee8021MstpPortNum, ieee8021MstpConfigIdFormatSelector=ieee8021MstpConfigIdFormatSelector, ieee8021MstpCistPortTopologyChangeAck=ieee8021MstpCistPortTopologyChangeAck, ieee8021MstpConfigIdTable=ieee8021MstpConfigIdTable, ieee8021MstpVlanV2Table=ieee8021MstpVlanV2Table, ieee8021MstpPortState=ieee8021MstpPortState, ieee8021MstpCistPortComponentId=ieee8021MstpCistPortComponentId, ieee8021MstpEntry=ieee8021MstpEntry, ieee8021MstpConfigIdComponentId=ieee8021MstpConfigIdComponentId, ieee8021MstpVlanV2Id=ieee8021MstpVlanV2Id, ieee8021MstpPortPriority=ieee8021MstpPortPriority, ieee8021MstpCistPortDisputed=ieee8021MstpCistPortDisputed, ieee8021MstpVlanGroup=ieee8021MstpVlanGroup, ieee8021MstpPortComponentId=ieee8021MstpPortComponentId, ieee8021MstpPortDesignatedPort=ieee8021MstpPortDesignatedPort, ieee8021MstpRevisionLevel=ieee8021MstpRevisionLevel, ieee8021MstpVlanTable=ieee8021MstpVlanTable, ieee8021MstpFidToMstiTable=ieee8021MstpFidToMstiTable, ieee8021MstpTopologyChanges=ieee8021MstpTopologyChanges, ieee8021MstpVlanEntry=ieee8021MstpVlanEntry, ieee8021MstpConfigurationName=ieee8021MstpConfigurationName, ieee8021MstpVlanV2ComponentId=ieee8021MstpVlanV2ComponentId, ieee8021MstpCistTable=ieee8021MstpCistTable, PYSNMP_MODULE_ID=ieee8021MstpMib, ieee8021MstpFidToMstiComponentId=ieee8021MstpFidToMstiComponentId, ieee8021MstpConfigIdEntry=ieee8021MstpConfigIdEntry, ieee8021MstpCistPortPseudoRootId=ieee8021MstpCistPortPseudoRootId, ieee8021MstpCistMaxHops=ieee8021MstpCistMaxHops, ieee8021MstpCistPortProtocolMigration=ieee8021MstpCistPortProtocolMigration, ieee8021MstpCistTopologyChange=ieee8021MstpCistTopologyChange, ieee8021MstpPortDesignatedCost=ieee8021MstpPortDesignatedCost, ieee8021MstpCistBridgeIdentifier=ieee8021MstpCistBridgeIdentifier, ieee8021MstpMib=ieee8021MstpMib, ieee8021MstpVlanComponentId=ieee8021MstpVlanComponentId, ieee8021MstpCompliances=ieee8021MstpCompliances, ieee8021MstpCompliance=ieee8021MstpCompliance, ieee8021MstpCistPortCistRegionalRootId=ieee8021MstpCistPortCistRegionalRootId, ieee8021MstpVids1=ieee8021MstpVids1, ieee8021MstpFidToMstiV2Entry=ieee8021MstpFidToMstiV2Entry, ieee8021MstpCistPortExtensionGroup=ieee8021MstpCistPortExtensionGroup, ieee8021MstpDesignatedRoot=ieee8021MstpDesignatedRoot, ieee8021MstpVlanV2Group=ieee8021MstpVlanV2Group, ieee8021MstpCistPortUptime=ieee8021MstpCistPortUptime, ieee8021MstpBridgeId=ieee8021MstpBridgeId, ieee8021MstpCistPortGroup=ieee8021MstpCistPortGroup, ieee8021MstpPortDesignatedBridge=ieee8021MstpPortDesignatedBridge, ieee8021MstpPortEntry=ieee8021MstpPortEntry, ieee8021MstpCistPortEntry=ieee8021MstpCistPortEntry, ieee8021MstpCistPortCistPathCost=ieee8021MstpCistPortCistPathCost, ieee8021MstpCistPortIsL2Gp=ieee8021MstpCistPortIsL2Gp, ieee8021MstpCistPortOperEdgePort=ieee8021MstpCistPortOperEdgePort, ieee8021MstpRowStatus=ieee8021MstpRowStatus, ieee8021MstpRootPathCost=ieee8021MstpRootPathCost, ieee8021MstpCistEntry=ieee8021MstpCistEntry, ieee8021MstpPortMstId=ieee8021MstpPortMstId, ieee8021MstpVids0=ieee8021MstpVids0, ieee8021MstpFidToMstiV2Fid=ieee8021MstpFidToMstiV2Fid, ieee8021MstpFidToMstiV2MstId=ieee8021MstpFidToMstiV2MstId, ieee8021MstpFidToMstiEntry=ieee8021MstpFidToMstiEntry, ieee8021MstpGroup=ieee8021MstpGroup, ieee8021MstpCistPathCost=ieee8021MstpCistPathCost, ieee8021MstpCistRegionalRootIdentifier=ieee8021MstpCistRegionalRootIdentifier, ieee8021MstpCistPortEnableBPDURx=ieee8021MstpCistPortEnableBPDURx, ieee8021MstpCistPortAutoIsolatePort=ieee8021MstpCistPortAutoIsolatePort, ieee8021MstpCistComponentId=ieee8021MstpCistComponentId, ieee8021MstpPortAdminPathCost=ieee8021MstpPortAdminPathCost, ieee8021MstpGroups=ieee8021MstpGroups, ieee8021MstpCistPortRestrictedTcn=ieee8021MstpCistPortRestrictedTcn, ieee8021MstpVlanV2Entry=ieee8021MstpVlanV2Entry, ieee8021MstpVlanMstId=ieee8021MstpVlanMstId, ieee8021MstpConformance=ieee8021MstpConformance, ieee8021MstpCistPortRestrictedRole=ieee8021MstpCistPortRestrictedRole, ieee8021MstpTimeSinceTopologyChange=ieee8021MstpTimeSinceTopologyChange, ieee8021MstpVlanV2MstId=ieee8021MstpVlanV2MstId, ieee8021MstpCistPortAutoEdgePort=ieee8021MstpCistPortAutoEdgePort, ieee8021MstpId=ieee8021MstpId, ieee8021MstpPortDisputed=ieee8021MstpPortDisputed, ieee8021MstpCistPortTable=ieee8021MstpCistPortTable, ieee8021MstpObjects=ieee8021MstpObjects, ieee8021MstpCistPortMacEnabled=ieee8021MstpCistPortMacEnabled, ieee8021MstpFidToMstiFid=ieee8021MstpFidToMstiFid, ieee8021MstpComponentId=ieee8021MstpComponentId, ieee8021MstpPortUptime=ieee8021MstpPortUptime, ieee8021MstpPortDesignatedRoot=ieee8021MstpPortDesignatedRoot, ieee8021MstpCistPortDesignatedRoot=ieee8021MstpCistPortDesignatedRoot, ieee8021MstpPortGroup=ieee8021MstpPortGroup, ieee8021MstpFidToMstiV2Table=ieee8021MstpFidToMstiV2Table, ieee8021MstpCistGroup=ieee8021MstpCistGroup, ieee8021MstpFidToMstiV2Group=ieee8021MstpFidToMstiV2Group, ieee8021MstpPortPathCost=ieee8021MstpPortPathCost, ieee8021MstpCistPortMacOperational=ieee8021MstpCistPortMacOperational, ieee8021MstpBridgePriority=ieee8021MstpBridgePriority, ieee8021MstpCistPortNum=ieee8021MstpCistPortNum, ieee8021MstpPortRole=ieee8021MstpPortRole, ieee8021MstpCistPortAdminPathCost=ieee8021MstpCistPortAdminPathCost, ieee8021MstpVids3=ieee8021MstpVids3, ieee8021MstpComplianceV2=ieee8021MstpComplianceV2, ieee8021MstpFidToMstiMstId=ieee8021MstpFidToMstiMstId, ieee8021MstpFidToMstiV2ComponentId=ieee8021MstpFidToMstiV2ComponentId, ieee8021MstpPortTable=ieee8021MstpPortTable, ieee8021MstpConfigurationDigest=ieee8021MstpConfigurationDigest, ieee8021MstpCistPortExtensionTable=ieee8021MstpCistPortExtensionTable, ieee8021MstpNotifications=ieee8021MstpNotifications, ieee8021MstpVids2=ieee8021MstpVids2, ieee8021MstpCistPortRole=ieee8021MstpCistPortRole, ieee8021MstpCistPortAdminEdgePort=ieee8021MstpCistPortAdminEdgePort, ieee8021MstpConfigIdGroup=ieee8021MstpConfigIdGroup, ieee8021MstpVlanId=ieee8021MstpVlanId, ieee8021MstpCistPortHelloTime=ieee8021MstpCistPortHelloTime, ieee8021MstpRootPort=ieee8021MstpRootPort)
