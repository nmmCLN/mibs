#
# PySNMP MIB module DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DVMRP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:33 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Counter32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, ModuleIdentity, Bits, Unsigned32, ObjectIdentity, NotificationType, TimeTicks, Counter64, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "ModuleIdentity", "Bits", "Unsigned32", "ObjectIdentity", "NotificationType", "TimeTicks", "Counter64", "experimental")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
dvmrpMIB = ModuleIdentity((1, 3, 6, 1, 3, 62))
if mibBuilder.loadTexts: dvmrpMIB.setLastUpdated('9804221900Z')
if mibBuilder.loadTexts: dvmrpMIB.setOrganization('IETF IDMR Working Group.')
dvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 62, 1))
dvmrp = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1))
dvmrpVersionString = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpVersionString.setStatus('current')
dvmrpGenerationId = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpGenerationId.setStatus('current')
dvmrpNumRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNumRoutes.setStatus('current')
dvmrpReachableRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpReachableRoutes.setStatus('current')
dvmrpInterfaceTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 3), )
if mibBuilder.loadTexts: dvmrpInterfaceTable.setStatus('current')
dvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 3, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpInterfaceIfIndex"))
if mibBuilder.loadTexts: dvmrpInterfaceEntry.setStatus('current')
dvmrpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: dvmrpInterfaceIfIndex.setStatus('current')
dvmrpInterfaceType = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tunnel", 1), ("srcrt", 2), ("querier", 3), ("subnet", 4))).clone('tunnel')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceType.setStatus('deprecated')
dvmrpInterfaceOperState = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceOperState.setStatus('deprecated')
dvmrpInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceLocalAddress.setStatus('current')
dvmrpInterfaceRemoteAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceRemoteAddress.setStatus('deprecated')
dvmrpInterfaceRemoteSubnetMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRemoteSubnetMask.setStatus('deprecated')
dvmrpInterfaceMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMetric.setStatus('current')
dvmrpInterfaceRateLimit = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceRateLimit.setStatus('deprecated')
dvmrpInterfaceInPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceInPkts.setStatus('deprecated')
dvmrpInterfaceOutPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceOutPkts.setStatus('deprecated')
dvmrpInterfaceInOctets = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceInOctets.setStatus('deprecated')
dvmrpInterfaceOutOctets = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceOutOctets.setStatus('deprecated')
dvmrpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceStatus.setStatus('current')
dvmrpInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadPkts.setStatus('current')
dvmrpInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadRoutes.setStatus('current')
dvmrpInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceSentRoutes.setStatus('current')
dvmrpInterfaceMasterKey = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 17), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMasterKey.setStatus('current')
dvmrpInterfaceMasterKeyVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 18), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMasterKeyVersion.setStatus('current')
dvmrpNeighborTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 4), )
if mibBuilder.loadTexts: dvmrpNeighborTable.setStatus('current')
dvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 4, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpNeighborIfIndex"), (0, "DVMRP-MIB", "dvmrpNeighborAddress"))
if mibBuilder.loadTexts: dvmrpNeighborEntry.setStatus('current')
dvmrpNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: dvmrpNeighborIfIndex.setStatus('current')
dvmrpNeighborAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpNeighborAddress.setStatus('current')
dvmrpNeighborUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborUpTime.setStatus('current')
dvmrpNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborExpiryTime.setStatus('current')
dvmrpNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborGenerationId.setStatus('current')
dvmrpNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMajorVersion.setStatus('current')
dvmrpNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMinorVersion.setStatus('current')
dvmrpNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 9), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborCapabilities.setStatus('current')
dvmrpNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvRoutes.setStatus('current')
dvmrpNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadPkts.setStatus('current')
dvmrpNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadRoutes.setStatus('current')
dvmrpNeighborState = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborState.setStatus('current')
dvmrpRouteTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 5), )
if mibBuilder.loadTexts: dvmrpRouteTable.setStatus('current')
dvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 5, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpRouteSource"), (0, "DVMRP-MIB", "dvmrpRouteSourceMask"))
if mibBuilder.loadTexts: dvmrpRouteEntry.setStatus('current')
dvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSource.setStatus('current')
dvmrpRouteSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSourceMask.setStatus('current')
dvmrpRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpstreamNeighbor.setStatus('current')
dvmrpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteIfIndex.setStatus('current')
dvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteMetric.setStatus('current')
dvmrpRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteExpiryTime.setStatus('current')
dvmrpRouteUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpTime.setStatus('current')
dvmrpRouteNextHopTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 6), )
if mibBuilder.loadTexts: dvmrpRouteNextHopTable.setStatus('current')
dvmrpRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 6, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpRouteNextHopSource"), (0, "DVMRP-MIB", "dvmrpRouteNextHopSourceMask"), (0, "DVMRP-MIB", "dvmrpRouteNextHopIfIndex"))
if mibBuilder.loadTexts: dvmrpRouteNextHopEntry.setStatus('current')
dvmrpRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSource.setStatus('current')
dvmrpRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSourceMask.setStatus('current')
dvmrpRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: dvmrpRouteNextHopIfIndex.setStatus('current')
dvmrpRouteNextHopType = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteNextHopType.setStatus('current')
dvmrpAltNetTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 8), )
if mibBuilder.loadTexts: dvmrpAltNetTable.setStatus('deprecated')
dvmrpAltNetEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 8, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpAltNetIfIndex"), (0, "DVMRP-MIB", "dvmrpAltNetAddress"), (0, "DVMRP-MIB", "dvmrpAltNetMask"))
if mibBuilder.loadTexts: dvmrpAltNetEntry.setStatus('deprecated')
dvmrpAltNetIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 1), Integer32())
if mibBuilder.loadTexts: dvmrpAltNetIfIndex.setStatus('deprecated')
dvmrpAltNetAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpAltNetAddress.setStatus('deprecated')
dvmrpAltNetMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 3), IpAddress())
if mibBuilder.loadTexts: dvmrpAltNetMask.setStatus('deprecated')
dvmrpAltNetStatus = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpAltNetStatus.setStatus('deprecated')
dvmrpTraps = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1, 11))
dvmrpNeighborLoss = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 11, 1)).setObjects(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpNeighborIfIndex"), ("DVMRP-MIB", "dvmrpNeighborAddress"), ("DVMRP-MIB", "dvmrpNeighborState"))
if mibBuilder.loadTexts: dvmrpNeighborLoss.setStatus('current')
dvmrpNeighborNotPruning = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 11, 2)).setObjects(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpNeighborIfIndex"), ("DVMRP-MIB", "dvmrpNeighborAddress"))
if mibBuilder.loadTexts: dvmrpNeighborNotPruning.setStatus('current')
dvmrpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 62, 2))
dvmrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 1))
dvmrpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 2))
dvmrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 62, 2, 1, 1)).setObjects(("DVMRP-MIB", "dvmrpGeneralGroup"), ("DVMRP-MIB", "dvmrpInterfaceGroup"), ("DVMRP-MIB", "dvmrpNeighborGroup"), ("DVMRP-MIB", "dvmrpRoutingGroup"), ("DVMRP-MIB", "dvmrpSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpMIBCompliance = dvmrpMIBCompliance.setStatus('current')
dvmrpMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 1)).setObjects(("DVMRP-MIB", "dvmrpVersionString"), ("DVMRP-MIB", "dvmrpGenerationId"), ("DVMRP-MIB", "dvmrpNumRoutes"), ("DVMRP-MIB", "dvmrpReachableRoutes"), ("DVMRP-MIB", "dvmrpInterfaceType"), ("DVMRP-MIB", "dvmrpInterfaceOperState"), ("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpInterfaceRemoteAddress"), ("DVMRP-MIB", "dvmrpInterfaceRemoteSubnetMask"), ("DVMRP-MIB", "dvmrpInterfaceMetric"), ("DVMRP-MIB", "dvmrpInterfaceRateLimit"), ("DVMRP-MIB", "dvmrpInterfaceInPkts"), ("DVMRP-MIB", "dvmrpInterfaceOutPkts"), ("DVMRP-MIB", "dvmrpInterfaceInOctets"), ("DVMRP-MIB", "dvmrpInterfaceOutOctets"), ("DVMRP-MIB", "dvmrpInterfaceStatus"), ("DVMRP-MIB", "dvmrpNeighborUpTime"), ("DVMRP-MIB", "dvmrpNeighborExpiryTime"), ("DVMRP-MIB", "dvmrpNeighborGenerationId"), ("DVMRP-MIB", "dvmrpNeighborMajorVersion"), ("DVMRP-MIB", "dvmrpNeighborMinorVersion"), ("DVMRP-MIB", "dvmrpNeighborCapabilities"), ("DVMRP-MIB", "dvmrpRouteUpstreamNeighbor"), ("DVMRP-MIB", "dvmrpRouteIfIndex"), ("DVMRP-MIB", "dvmrpRouteMetric"), ("DVMRP-MIB", "dvmrpRouteExpiryTime"), ("DVMRP-MIB", "dvmrpRouteNextHopType"), ("DVMRP-MIB", "dvmrpAltNetStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpMIBGroup = dvmrpMIBGroup.setStatus('deprecated')
dvmrpGeneralGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 2)).setObjects(("DVMRP-MIB", "dvmrpVersionString"), ("DVMRP-MIB", "dvmrpGenerationId"), ("DVMRP-MIB", "dvmrpNumRoutes"), ("DVMRP-MIB", "dvmrpReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpGeneralGroup = dvmrpGeneralGroup.setStatus('current')
dvmrpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 3)).setObjects(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpInterfaceMetric"), ("DVMRP-MIB", "dvmrpInterfaceStatus"), ("DVMRP-MIB", "dvmrpInterfaceRcvBadPkts"), ("DVMRP-MIB", "dvmrpInterfaceRcvBadRoutes"), ("DVMRP-MIB", "dvmrpInterfaceSentRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpInterfaceGroup = dvmrpInterfaceGroup.setStatus('current')
dvmrpNeighborGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 4)).setObjects(("DVMRP-MIB", "dvmrpNeighborUpTime"), ("DVMRP-MIB", "dvmrpNeighborExpiryTime"), ("DVMRP-MIB", "dvmrpNeighborGenerationId"), ("DVMRP-MIB", "dvmrpNeighborMajorVersion"), ("DVMRP-MIB", "dvmrpNeighborMinorVersion"), ("DVMRP-MIB", "dvmrpNeighborCapabilities"), ("DVMRP-MIB", "dvmrpNeighborRcvRoutes"), ("DVMRP-MIB", "dvmrpNeighborRcvBadPkts"), ("DVMRP-MIB", "dvmrpNeighborRcvBadRoutes"), ("DVMRP-MIB", "dvmrpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNeighborGroup = dvmrpNeighborGroup.setStatus('current')
dvmrpRoutingGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 5)).setObjects(("DVMRP-MIB", "dvmrpRouteUpstreamNeighbor"), ("DVMRP-MIB", "dvmrpRouteIfIndex"), ("DVMRP-MIB", "dvmrpRouteMetric"), ("DVMRP-MIB", "dvmrpRouteExpiryTime"), ("DVMRP-MIB", "dvmrpRouteUpTime"), ("DVMRP-MIB", "dvmrpRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpRoutingGroup = dvmrpRoutingGroup.setStatus('current')
dvmrpSecurityGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 6)).setObjects(("DVMRP-MIB", "dvmrpInterfaceMasterKey"), ("DVMRP-MIB", "dvmrpInterfaceMasterKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpSecurityGroup = dvmrpSecurityGroup.setStatus('current')
mibBuilder.exportSymbols("DVMRP-MIB", dvmrpRouteMetric=dvmrpRouteMetric, dvmrpRouteExpiryTime=dvmrpRouteExpiryTime, dvmrpNeighborMinorVersion=dvmrpNeighborMinorVersion, dvmrpMIBGroups=dvmrpMIBGroups, dvmrpRoutingGroup=dvmrpRoutingGroup, dvmrpAltNetTable=dvmrpAltNetTable, dvmrpInterfaceType=dvmrpInterfaceType, dvmrpAltNetStatus=dvmrpAltNetStatus, dvmrpRouteNextHopType=dvmrpRouteNextHopType, dvmrpNeighborRcvBadPkts=dvmrpNeighborRcvBadPkts, dvmrpNeighborState=dvmrpNeighborState, dvmrpInterfaceRcvBadRoutes=dvmrpInterfaceRcvBadRoutes, dvmrpMIBConformance=dvmrpMIBConformance, dvmrpNeighborGroup=dvmrpNeighborGroup, dvmrpRouteUpTime=dvmrpRouteUpTime, dvmrpNumRoutes=dvmrpNumRoutes, dvmrpNeighborRcvBadRoutes=dvmrpNeighborRcvBadRoutes, dvmrpInterfaceRcvBadPkts=dvmrpInterfaceRcvBadPkts, dvmrpVersionString=dvmrpVersionString, dvmrpNeighborRcvRoutes=dvmrpNeighborRcvRoutes, PYSNMP_MODULE_ID=dvmrpMIB, dvmrpInterfaceStatus=dvmrpInterfaceStatus, dvmrpNeighborExpiryTime=dvmrpNeighborExpiryTime, dvmrpInterfaceRemoteSubnetMask=dvmrpInterfaceRemoteSubnetMask, dvmrpInterfaceSentRoutes=dvmrpInterfaceSentRoutes, dvmrpAltNetEntry=dvmrpAltNetEntry, dvmrpTraps=dvmrpTraps, dvmrpMIB=dvmrpMIB, dvmrpRouteIfIndex=dvmrpRouteIfIndex, dvmrpMIBCompliances=dvmrpMIBCompliances, dvmrpMIBCompliance=dvmrpMIBCompliance, dvmrpInterfaceLocalAddress=dvmrpInterfaceLocalAddress, dvmrpAltNetIfIndex=dvmrpAltNetIfIndex, dvmrpRouteNextHopSourceMask=dvmrpRouteNextHopSourceMask, dvmrpInterfaceRemoteAddress=dvmrpInterfaceRemoteAddress, dvmrpRouteEntry=dvmrpRouteEntry, dvmrpRouteNextHopIfIndex=dvmrpRouteNextHopIfIndex, dvmrpNeighborUpTime=dvmrpNeighborUpTime, dvmrpInterfaceInOctets=dvmrpInterfaceInOctets, dvmrpRouteNextHopTable=dvmrpRouteNextHopTable, dvmrpAltNetMask=dvmrpAltNetMask, dvmrpNeighborCapabilities=dvmrpNeighborCapabilities, dvmrpNeighborEntry=dvmrpNeighborEntry, dvmrpInterfaceOutPkts=dvmrpInterfaceOutPkts, dvmrpRouteTable=dvmrpRouteTable, dvmrpRouteNextHopEntry=dvmrpRouteNextHopEntry, dvmrpRouteNextHopSource=dvmrpRouteNextHopSource, dvmrpInterfaceMasterKeyVersion=dvmrpInterfaceMasterKeyVersion, dvmrpGenerationId=dvmrpGenerationId, dvmrpNeighborGenerationId=dvmrpNeighborGenerationId, dvmrpInterfaceOutOctets=dvmrpInterfaceOutOctets, dvmrpSecurityGroup=dvmrpSecurityGroup, dvmrpNeighborIfIndex=dvmrpNeighborIfIndex, dvmrpNeighborAddress=dvmrpNeighborAddress, dvmrpInterfaceRateLimit=dvmrpInterfaceRateLimit, dvmrpAltNetAddress=dvmrpAltNetAddress, dvmrpInterfaceMasterKey=dvmrpInterfaceMasterKey, dvmrpInterfaceEntry=dvmrpInterfaceEntry, dvmrpNeighborMajorVersion=dvmrpNeighborMajorVersion, dvmrpRouteSource=dvmrpRouteSource, dvmrpInterfaceMetric=dvmrpInterfaceMetric, dvmrpMIBObjects=dvmrpMIBObjects, dvmrp=dvmrp, dvmrpInterfaceInPkts=dvmrpInterfaceInPkts, dvmrpNeighborLoss=dvmrpNeighborLoss, dvmrpMIBGroup=dvmrpMIBGroup, dvmrpGeneralGroup=dvmrpGeneralGroup, dvmrpInterfaceGroup=dvmrpInterfaceGroup, dvmrpInterfaceTable=dvmrpInterfaceTable, dvmrpRouteSourceMask=dvmrpRouteSourceMask, dvmrpRouteUpstreamNeighbor=dvmrpRouteUpstreamNeighbor, dvmrpNeighborNotPruning=dvmrpNeighborNotPruning, dvmrpInterfaceOperState=dvmrpInterfaceOperState, dvmrpInterfaceIfIndex=dvmrpInterfaceIfIndex, dvmrpNeighborTable=dvmrpNeighborTable, dvmrpReachableRoutes=dvmrpReachableRoutes)
