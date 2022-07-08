#
# PySNMP MIB module HIRSCHMANN-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/hmDVMRP.mib
# Produced by pysmi-1.1.8 at Fri Jul  8 09:20:19 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hmPlatform4Multicast, = mibBuilder.importSymbols("HIRSCHMANN-MULTICAST-MIB", "hmPlatform4Multicast")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, ModuleIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, NotificationType, Unsigned32, IpAddress, TimeTicks, Bits, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "TimeTicks", "Bits", "Gauge32", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hmDVMRPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 15, 4, 100))
hmDVMRPMIB.setRevisions(('2010-04-12 12:00',))
if mibBuilder.loadTexts: hmDVMRPMIB.setLastUpdated('201004121200Z')
if mibBuilder.loadTexts: hmDVMRPMIB.setOrganization('Hirschmann Automation and Control GmbH')
hmDVMRPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1))
hmDVMRP = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1))
hmDVMRPScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1))
hmDVMRPVersionString = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPVersionString.setStatus('current')
hmDVMRPGenerationId = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPGenerationId.setStatus('obsolete')
hmDVMRPNumRoutes = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNumRoutes.setStatus('current')
hmDVMRPReachableRoutes = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPReachableRoutes.setStatus('current')
hmDVMRPUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDVMRPUpdateInterval.setStatus('current')
hmDVMRPPruneLifetime = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 64800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDVMRPPruneLifetime.setStatus('current')
hmDVMRPInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2), )
if mibBuilder.loadTexts: hmDVMRPInterfaceTable.setStatus('current')
hmDVMRPInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceIfIndex"))
if mibBuilder.loadTexts: hmDVMRPInterfaceEntry.setStatus('current')
hmDVMRPInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hmDVMRPInterfaceIfIndex.setStatus('current')
hmDVMRPInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceLocalAddress.setStatus('current')
hmDVMRPInterfaceMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceMetric.setStatus('current')
hmDVMRPInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceStatus.setStatus('current')
hmDVMRPInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceRcvBadPkts.setStatus('current')
hmDVMRPInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceRcvBadRoutes.setStatus('current')
hmDVMRPInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceSentRoutes.setStatus('current')
hmDVMRPInterfaceInterfaceKey = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceInterfaceKey.setStatus('current')
hmDVMRPInterfaceInterfaceKeyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceInterfaceKeyVersion.setStatus('current')
hmDVMRPInterfaceGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceGenerationId.setStatus('current')
hmDVMRPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3), )
if mibBuilder.loadTexts: hmDVMRPNeighborTable.setStatus('current')
hmDVMRPNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborIfIndex"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborAddress"))
if mibBuilder.loadTexts: hmDVMRPNeighborEntry.setStatus('current')
hmDVMRPNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hmDVMRPNeighborIfIndex.setStatus('current')
hmDVMRPNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPNeighborAddress.setStatus('current')
hmDVMRPNeighborUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborUpTime.setStatus('current')
hmDVMRPNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborExpiryTime.setStatus('current')
hmDVMRPNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborGenerationId.setStatus('current')
hmDVMRPNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborMajorVersion.setStatus('current')
hmDVMRPNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborMinorVersion.setStatus('current')
hmDVMRPNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborCapabilities.setStatus('current')
hmDVMRPNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborRcvRoutes.setStatus('current')
hmDVMRPNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborRcvBadPkts.setStatus('current')
hmDVMRPNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborRcvBadRoutes.setStatus('current')
hmDVMRPNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborState.setStatus('current')
hmDVMRPRouteTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4), )
if mibBuilder.loadTexts: hmDVMRPRouteTable.setStatus('current')
hmDVMRPRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteSource"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteSourceMask"))
if mibBuilder.loadTexts: hmDVMRPRouteEntry.setStatus('current')
hmDVMRPRouteSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteSource.setStatus('current')
hmDVMRPRouteSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteSourceMask.setStatus('current')
hmDVMRPRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteUpstreamNeighbor.setStatus('current')
hmDVMRPRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteIfIndex.setStatus('current')
hmDVMRPRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteMetric.setStatus('current')
hmDVMRPRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteExpiryTime.setStatus('current')
hmDVMRPRouteUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteUpTime.setStatus('current')
hmDVMRPRouteNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5), )
if mibBuilder.loadTexts: hmDVMRPRouteNextHopTable.setStatus('current')
hmDVMRPRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopSource"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopSourceMask"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopIfIndex"))
if mibBuilder.loadTexts: hmDVMRPRouteNextHopEntry.setStatus('current')
hmDVMRPRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteNextHopSource.setStatus('current')
hmDVMRPRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteNextHopSourceMask.setStatus('current')
hmDVMRPRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: hmDVMRPRouteNextHopIfIndex.setStatus('current')
hmDVMRPRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteNextHopType.setStatus('current')
hmDVMRPPruneTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6), )
if mibBuilder.loadTexts: hmDVMRPPruneTable.setStatus('current')
hmDVMRPPruneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneGroup"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneSource"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneSourceMask"))
if mibBuilder.loadTexts: hmDVMRPPruneEntry.setStatus('current')
hmDVMRPPruneGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmDVMRPPruneGroup.setStatus('current')
hmDVMRPPruneSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPPruneSource.setStatus('current')
hmDVMRPPruneSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: hmDVMRPPruneSourceMask.setStatus('current')
hmDVMRPPruneExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPPruneExpiryTime.setStatus('current')
hmDVMRPTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7))
hmDVMRPNeighborLoss = NotificationType((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7, 1)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborState"))
if mibBuilder.loadTexts: hmDVMRPNeighborLoss.setStatus('current')
hmDVMRPNeighborNotPruning = NotificationType((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7, 2)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborCapabilities"))
if mibBuilder.loadTexts: hmDVMRPNeighborNotPruning.setStatus('current')
hmDVMRPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2))
hmDVMRPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 1))
hmDVMRPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2))
hmDVMRPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 1, 1)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPGeneralGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRoutingGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPTreeGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPMIBCompliance = hmDVMRPMIBCompliance.setStatus('current')
hmDVMRPGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 2)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPVersionString"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPGenerationId"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNumRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPGeneralGroup = hmDVMRPGeneralGroup.setStatus('current')
hmDVMRPInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 3)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceMetric"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceStatus"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceRcvBadPkts"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceRcvBadRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceSentRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceGenerationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPInterfaceGroup = hmDVMRPInterfaceGroup.setStatus('current')
hmDVMRPNeighborGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 4)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborUpTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborExpiryTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborGenerationId"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborMajorVersion"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborMinorVersion"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborCapabilities"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvBadPkts"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvBadRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPNeighborGroup = hmDVMRPNeighborGroup.setStatus('current')
hmDVMRPRoutingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 5)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteUpstreamNeighbor"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteIfIndex"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteMetric"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteExpiryTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteUpTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPRoutingGroup = hmDVMRPRoutingGroup.setStatus('current')
hmDVMRPSecurityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 6)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceInterfaceKey"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceInterfaceKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPSecurityGroup = hmDVMRPSecurityGroup.setStatus('current')
hmDVMRPTreeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 7)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPTreeGroup = hmDVMRPTreeGroup.setStatus('current')
hmDVMRPNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 8)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborLoss"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborNotPruning"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPNotificationGroup = hmDVMRPNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-DVMRP-MIB", hmDVMRPPruneEntry=hmDVMRPPruneEntry, hmDVMRPNeighborMinorVersion=hmDVMRPNeighborMinorVersion, hmDVMRPTreeGroup=hmDVMRPTreeGroup, hmDVMRPTraps=hmDVMRPTraps, hmDVMRPRouteNextHopTable=hmDVMRPRouteNextHopTable, hmDVMRP=hmDVMRP, hmDVMRPNeighborAddress=hmDVMRPNeighborAddress, hmDVMRPPruneLifetime=hmDVMRPPruneLifetime, hmDVMRPRouteNextHopType=hmDVMRPRouteNextHopType, hmDVMRPRouteExpiryTime=hmDVMRPRouteExpiryTime, hmDVMRPMIBCompliance=hmDVMRPMIBCompliance, hmDVMRPRouteNextHopSource=hmDVMRPRouteNextHopSource, hmDVMRPMIBObjects=hmDVMRPMIBObjects, hmDVMRPUpdateInterval=hmDVMRPUpdateInterval, hmDVMRPVersionString=hmDVMRPVersionString, hmDVMRPNeighborNotPruning=hmDVMRPNeighborNotPruning, hmDVMRPNeighborRcvRoutes=hmDVMRPNeighborRcvRoutes, hmDVMRPInterfaceSentRoutes=hmDVMRPInterfaceSentRoutes, hmDVMRPGeneralGroup=hmDVMRPGeneralGroup, hmDVMRPNotificationGroup=hmDVMRPNotificationGroup, hmDVMRPInterfaceIfIndex=hmDVMRPInterfaceIfIndex, hmDVMRPMIB=hmDVMRPMIB, hmDVMRPRouteNextHopSourceMask=hmDVMRPRouteNextHopSourceMask, hmDVMRPRouteMetric=hmDVMRPRouteMetric, hmDVMRPGenerationId=hmDVMRPGenerationId, hmDVMRPInterfaceInterfaceKeyVersion=hmDVMRPInterfaceInterfaceKeyVersion, PYSNMP_MODULE_ID=hmDVMRPMIB, hmDVMRPNeighborEntry=hmDVMRPNeighborEntry, hmDVMRPRouteUpstreamNeighbor=hmDVMRPRouteUpstreamNeighbor, hmDVMRPInterfaceGroup=hmDVMRPInterfaceGroup, hmDVMRPNeighborGroup=hmDVMRPNeighborGroup, hmDVMRPNeighborExpiryTime=hmDVMRPNeighborExpiryTime, hmDVMRPPruneGroup=hmDVMRPPruneGroup, hmDVMRPInterfaceInterfaceKey=hmDVMRPInterfaceInterfaceKey, hmDVMRPInterfaceRcvBadPkts=hmDVMRPInterfaceRcvBadPkts, hmDVMRPNeighborLoss=hmDVMRPNeighborLoss, hmDVMRPInterfaceEntry=hmDVMRPInterfaceEntry, hmDVMRPInterfaceTable=hmDVMRPInterfaceTable, hmDVMRPInterfaceMetric=hmDVMRPInterfaceMetric, hmDVMRPInterfaceGenerationId=hmDVMRPInterfaceGenerationId, hmDVMRPMIBCompliances=hmDVMRPMIBCompliances, hmDVMRPRouteNextHopEntry=hmDVMRPRouteNextHopEntry, hmDVMRPRouteNextHopIfIndex=hmDVMRPRouteNextHopIfIndex, hmDVMRPNeighborRcvBadRoutes=hmDVMRPNeighborRcvBadRoutes, hmDVMRPRouteSource=hmDVMRPRouteSource, hmDVMRPNeighborGenerationId=hmDVMRPNeighborGenerationId, hmDVMRPNeighborState=hmDVMRPNeighborState, hmDVMRPRouteIfIndex=hmDVMRPRouteIfIndex, hmDVMRPScalar=hmDVMRPScalar, hmDVMRPInterfaceRcvBadRoutes=hmDVMRPInterfaceRcvBadRoutes, hmDVMRPInterfaceStatus=hmDVMRPInterfaceStatus, hmDVMRPNeighborMajorVersion=hmDVMRPNeighborMajorVersion, hmDVMRPSecurityGroup=hmDVMRPSecurityGroup, hmDVMRPNeighborTable=hmDVMRPNeighborTable, hmDVMRPPruneTable=hmDVMRPPruneTable, hmDVMRPNeighborIfIndex=hmDVMRPNeighborIfIndex, hmDVMRPRouteSourceMask=hmDVMRPRouteSourceMask, hmDVMRPNumRoutes=hmDVMRPNumRoutes, hmDVMRPRouteUpTime=hmDVMRPRouteUpTime, hmDVMRPRouteTable=hmDVMRPRouteTable, hmDVMRPNeighborRcvBadPkts=hmDVMRPNeighborRcvBadPkts, hmDVMRPPruneSourceMask=hmDVMRPPruneSourceMask, hmDVMRPInterfaceLocalAddress=hmDVMRPInterfaceLocalAddress, hmDVMRPPruneSource=hmDVMRPPruneSource, hmDVMRPMIBGroups=hmDVMRPMIBGroups, hmDVMRPReachableRoutes=hmDVMRPReachableRoutes, hmDVMRPMIBConformance=hmDVMRPMIBConformance, hmDVMRPRoutingGroup=hmDVMRPRoutingGroup, hmDVMRPNeighborCapabilities=hmDVMRPNeighborCapabilities, hmDVMRPRouteEntry=hmDVMRPRouteEntry, hmDVMRPPruneExpiryTime=hmDVMRPPruneExpiryTime, hmDVMRPNeighborUpTime=hmDVMRPNeighborUpTime)
