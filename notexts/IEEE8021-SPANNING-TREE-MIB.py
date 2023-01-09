#
# PySNMP MIB module IEEE8021-SPANNING-TREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-SPANNING-TREE-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:23:45 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
Timeout, BridgeId = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "BridgeId")
IEEE8021BridgePortNumber, IEEE8021PbbComponentIdentifier, ieee802dot1mibs = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber", "IEEE8021PbbComponentIdentifier", "ieee802dot1mibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Integer32, ObjectIdentity, MibIdentifier, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "Unsigned32", "TimeTicks", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ieee8021SpanningTreeMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 3))
ieee8021SpanningTreeMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2011-03-24 00:00', '2008-10-15 00:00',))
if mibBuilder.loadTexts: ieee8021SpanningTreeMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021SpanningTreeMib.setOrganization('IEEE 802.1 Working Group')
ieee8021SpanningTreeNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 3, 0))
ieee8021SpanningTreeObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 3, 1))
ieee8021SpanningTreeConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 3, 2))
ieee8021SpanningTreeTable = MibTable((1, 3, 111, 2, 802, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: ieee8021SpanningTreeTable.setStatus('current')
ieee8021SpanningTreeEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeComponentId"))
if mibBuilder.loadTexts: ieee8021SpanningTreeEntry.setStatus('current')
ieee8021SpanningTreeComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021SpanningTreeComponentId.setStatus('current')
ieee8021SpanningTreeProtocolSpecification = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3), ("ieee8021q", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeProtocolSpecification.setStatus('current')
ieee8021SpanningTreePriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreePriority.setStatus('current')
ieee8021SpanningTreeTimeSinceTopologyChange = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 4), TimeTicks()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeTimeSinceTopologyChange.setStatus('current')
ieee8021SpanningTreeTopChanges = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 5), Counter64()).setUnits('topology changes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeTopChanges.setStatus('current')
ieee8021SpanningTreeDesignatedRoot = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeDesignatedRoot.setStatus('current')
ieee8021SpanningTreeRootCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeRootCost.setStatus('current')
ieee8021SpanningTreeRootPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 8), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeRootPort.setStatus('current')
ieee8021SpanningTreeMaxAge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 9), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeMaxAge.setStatus('current')
ieee8021SpanningTreeHelloTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 10), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeHelloTime.setStatus('current')
ieee8021SpanningTreeHoldTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 11), Integer32()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeHoldTime.setStatus('current')
ieee8021SpanningTreeForwardDelay = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 12), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeForwardDelay.setStatus('current')
ieee8021SpanningTreeBridgeMaxAge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeBridgeMaxAge.setStatus('current')
ieee8021SpanningTreeBridgeHelloTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeBridgeHelloTime.setStatus('current')
ieee8021SpanningTreeBridgeForwardDelay = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 15), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeBridgeForwardDelay.setStatus('current')
ieee8021SpanningTreeVersion = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2), ("mstp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeVersion.setStatus('current')
ieee8021SpanningTreeRstpTxHoldCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpTxHoldCount.setStatus('current')
ieee8021SpanningTreePortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 3, 1, 2), )
if mibBuilder.loadTexts: ieee8021SpanningTreePortTable.setStatus('current')
ieee8021SpanningTreePortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1), ).setIndexNames((0, "IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortComponentId"), (0, "IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePort"))
if mibBuilder.loadTexts: ieee8021SpanningTreePortEntry.setStatus('current')
ieee8021SpanningTreePortComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021SpanningTreePortComponentId.setStatus('current')
ieee8021SpanningTreePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 2), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: ieee8021SpanningTreePort.setStatus('current')
ieee8021SpanningTreePortPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreePortPriority.setStatus('current')
ieee8021SpanningTreePortState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreePortState.setStatus('current')
ieee8021SpanningTreePortEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreePortEnabled.setStatus('current')
ieee8021SpanningTreePortPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreePortPathCost.setStatus('current')
ieee8021SpanningTreePortDesignatedRoot = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 7), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreePortDesignatedRoot.setStatus('current')
ieee8021SpanningTreePortDesignatedCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreePortDesignatedCost.setStatus('current')
ieee8021SpanningTreePortDesignatedBridge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 9), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreePortDesignatedBridge.setStatus('current')
ieee8021SpanningTreePortDesignatedPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreePortDesignatedPort.setStatus('current')
ieee8021SpanningTreePortForwardTransitions = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 11), Counter64()).setUnits('forwarding transitions').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreePortForwardTransitions.setStatus('current')
ieee8021SpanningTreeRstpPortProtocolMigration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpPortProtocolMigration.setStatus('current')
ieee8021SpanningTreeRstpPortAdminEdgePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpPortAdminEdgePort.setStatus('current')
ieee8021SpanningTreeRstpPortOperEdgePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpPortOperEdgePort.setStatus('current')
ieee8021SpanningTreeRstpPortAdminPathCost = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpPortAdminPathCost.setStatus('current')
ieee8021SpanningTreePortExtensionTable = MibTable((1, 3, 111, 2, 802, 1, 1, 3, 1, 3), )
if mibBuilder.loadTexts: ieee8021SpanningTreePortExtensionTable.setStatus('current')
ieee8021SpanningTreePortExtensionEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1), )
ieee8021SpanningTreePortEntry.registerAugmentions(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortExtensionEntry"))
ieee8021SpanningTreePortExtensionEntry.setIndexNames(*ieee8021SpanningTreePortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021SpanningTreePortExtensionEntry.setStatus('current')
ieee8021SpanningTreeRstpPortAutoEdgePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpPortAutoEdgePort.setStatus('current')
ieee8021SpanningTreeRstpPortAutoIsolatePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpPortAutoIsolatePort.setStatus('current')
ieee8021SpanningTreeRstpPortIsolatePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpanningTreeRstpPortIsolatePort.setStatus('current')
ieee8021SpanningTreeNewRoot = NotificationType((1, 3, 111, 2, 802, 1, 1, 3, 0, 1))
if mibBuilder.loadTexts: ieee8021SpanningTreeNewRoot.setStatus('current')
ieee8021SpanningTreeTopologyChange = NotificationType((1, 3, 111, 2, 802, 1, 1, 3, 0, 2))
if mibBuilder.loadTexts: ieee8021SpanningTreeTopologyChange.setStatus('current')
ieee8021SpanningTreeCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 3, 2, 1))
ieee8021SpanningTreeGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 3, 2, 2))
ieee8021SpanningTreeGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 1)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeProtocolSpecification"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePriority"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeTimeSinceTopologyChange"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeTopChanges"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeDesignatedRoot"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRootCost"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRootPort"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeMaxAge"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeHelloTime"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeHoldTime"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeForwardDelay"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeBridgeMaxAge"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeBridgeHelloTime"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeBridgeForwardDelay"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreeGroup = ieee8021SpanningTreeGroup.setStatus('current')
ieee8021SpanningTreeRstpGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 2)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpTxHoldCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreeRstpGroup = ieee8021SpanningTreeRstpGroup.setStatus('current')
ieee8021SpanningTreePortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 3)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortPriority"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortState"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortEnabled"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortPathCost"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedRoot"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedCost"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedBridge"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedPort"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortForwardTransitions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreePortGroup = ieee8021SpanningTreePortGroup.setStatus('current')
ieee8021SpanningTreeRstpPortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 4)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortProtocolMigration"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAdminEdgePort"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortOperEdgePort"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAdminPathCost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreeRstpPortGroup = ieee8021SpanningTreeRstpPortGroup.setStatus('current')
ieee8021SpanningTreeRstpFragileGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 6)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAutoEdgePort"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAutoIsolatePort"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortIsolatePort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreeRstpFragileGroup = ieee8021SpanningTreeRstpFragileGroup.setStatus('current')
ieee8021SpanningTreeNotificationGroup = NotificationGroup((1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 5)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeNewRoot"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeTopologyChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreeNotificationGroup = ieee8021SpanningTreeNotificationGroup.setStatus('current')
ieee8021SpanningTreeCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 3, 2, 1, 1)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeGroup"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreeCompliance = ieee8021SpanningTreeCompliance.setStatus('current')
ieee8021SpanningTreeRstpCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 3, 2, 1, 2)).setObjects(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeGroup"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpGroup"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortGroup"), ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpanningTreeRstpCompliance = ieee8021SpanningTreeRstpCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-SPANNING-TREE-MIB", ieee8021SpanningTreeBridgeHelloTime=ieee8021SpanningTreeBridgeHelloTime, ieee8021SpanningTreeMib=ieee8021SpanningTreeMib, ieee8021SpanningTreeObjects=ieee8021SpanningTreeObjects, ieee8021SpanningTreeRootPort=ieee8021SpanningTreeRootPort, ieee8021SpanningTreePortDesignatedPort=ieee8021SpanningTreePortDesignatedPort, ieee8021SpanningTreeRstpPortAdminEdgePort=ieee8021SpanningTreeRstpPortAdminEdgePort, ieee8021SpanningTreeRstpPortAutoIsolatePort=ieee8021SpanningTreeRstpPortAutoIsolatePort, ieee8021SpanningTreePortState=ieee8021SpanningTreePortState, ieee8021SpanningTreeRstpPortOperEdgePort=ieee8021SpanningTreeRstpPortOperEdgePort, ieee8021SpanningTreeRstpCompliance=ieee8021SpanningTreeRstpCompliance, ieee8021SpanningTreeBridgeForwardDelay=ieee8021SpanningTreeBridgeForwardDelay, ieee8021SpanningTreeRstpPortGroup=ieee8021SpanningTreeRstpPortGroup, ieee8021SpanningTreeRstpTxHoldCount=ieee8021SpanningTreeRstpTxHoldCount, ieee8021SpanningTreeNotifications=ieee8021SpanningTreeNotifications, ieee8021SpanningTreeRootCost=ieee8021SpanningTreeRootCost, ieee8021SpanningTreeTopologyChange=ieee8021SpanningTreeTopologyChange, ieee8021SpanningTreeGroups=ieee8021SpanningTreeGroups, ieee8021SpanningTreeVersion=ieee8021SpanningTreeVersion, ieee8021SpanningTreePortExtensionTable=ieee8021SpanningTreePortExtensionTable, ieee8021SpanningTreePortPathCost=ieee8021SpanningTreePortPathCost, ieee8021SpanningTreeRstpPortAutoEdgePort=ieee8021SpanningTreeRstpPortAutoEdgePort, ieee8021SpanningTreeHoldTime=ieee8021SpanningTreeHoldTime, ieee8021SpanningTreeNewRoot=ieee8021SpanningTreeNewRoot, ieee8021SpanningTreeRstpPortProtocolMigration=ieee8021SpanningTreeRstpPortProtocolMigration, ieee8021SpanningTreePort=ieee8021SpanningTreePort, ieee8021SpanningTreePortDesignatedBridge=ieee8021SpanningTreePortDesignatedBridge, ieee8021SpanningTreePortDesignatedCost=ieee8021SpanningTreePortDesignatedCost, ieee8021SpanningTreeCompliances=ieee8021SpanningTreeCompliances, ieee8021SpanningTreeGroup=ieee8021SpanningTreeGroup, ieee8021SpanningTreeBridgeMaxAge=ieee8021SpanningTreeBridgeMaxAge, ieee8021SpanningTreePortEntry=ieee8021SpanningTreePortEntry, ieee8021SpanningTreeRstpGroup=ieee8021SpanningTreeRstpGroup, ieee8021SpanningTreePriority=ieee8021SpanningTreePriority, ieee8021SpanningTreeForwardDelay=ieee8021SpanningTreeForwardDelay, ieee8021SpanningTreeRstpPortAdminPathCost=ieee8021SpanningTreeRstpPortAdminPathCost, ieee8021SpanningTreeCompliance=ieee8021SpanningTreeCompliance, ieee8021SpanningTreePortTable=ieee8021SpanningTreePortTable, ieee8021SpanningTreePortPriority=ieee8021SpanningTreePortPriority, ieee8021SpanningTreeComponentId=ieee8021SpanningTreeComponentId, ieee8021SpanningTreeHelloTime=ieee8021SpanningTreeHelloTime, ieee8021SpanningTreeEntry=ieee8021SpanningTreeEntry, ieee8021SpanningTreeProtocolSpecification=ieee8021SpanningTreeProtocolSpecification, ieee8021SpanningTreeMaxAge=ieee8021SpanningTreeMaxAge, PYSNMP_MODULE_ID=ieee8021SpanningTreeMib, ieee8021SpanningTreePortForwardTransitions=ieee8021SpanningTreePortForwardTransitions, ieee8021SpanningTreeRstpFragileGroup=ieee8021SpanningTreeRstpFragileGroup, ieee8021SpanningTreePortComponentId=ieee8021SpanningTreePortComponentId, ieee8021SpanningTreePortGroup=ieee8021SpanningTreePortGroup, ieee8021SpanningTreePortExtensionEntry=ieee8021SpanningTreePortExtensionEntry, ieee8021SpanningTreeConformance=ieee8021SpanningTreeConformance, ieee8021SpanningTreeRstpPortIsolatePort=ieee8021SpanningTreeRstpPortIsolatePort, ieee8021SpanningTreePortEnabled=ieee8021SpanningTreePortEnabled, ieee8021SpanningTreeTopChanges=ieee8021SpanningTreeTopChanges, ieee8021SpanningTreeDesignatedRoot=ieee8021SpanningTreeDesignatedRoot, ieee8021SpanningTreePortDesignatedRoot=ieee8021SpanningTreePortDesignatedRoot, ieee8021SpanningTreeNotificationGroup=ieee8021SpanningTreeNotificationGroup, ieee8021SpanningTreeTable=ieee8021SpanningTreeTable, ieee8021SpanningTreeTimeSinceTopologyChange=ieee8021SpanningTreeTimeSinceTopologyChange)
