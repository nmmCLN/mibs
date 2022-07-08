#
# PySNMP MIB module F3-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-OSPF-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:21 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cmIpInterfaceEntry, ipManagementTunnelEntry = mibBuilder.importSymbols("CM-IP-MIB", "cmIpInterfaceEntry", "ipManagementTunnelEntry")
DesignatedRouterPriority, AreaID, ospfNbrEntry, RouterID, OspfAuthenticationType, HelloRange = mibBuilder.importSymbols("OSPF-MIB", "DesignatedRouterPriority", "AreaID", "ospfNbrEntry", "RouterID", "OspfAuthenticationType", "HelloRange")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Gauge32, Integer32, Counter64, TimeTicks, ObjectIdentity, IpAddress, Bits, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Integer32", "Counter64", "TimeTicks", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32")
TextualConvention, StorageType, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "DisplayString", "TruthValue", "RowStatus")
f3OspfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35))
f3OspfMIB.setRevisions(('2014-10-06 00:00',))
if mibBuilder.loadTexts: f3OspfMIB.setLastUpdated('201410060000Z')
if mibBuilder.loadTexts: f3OspfMIB.setOrganization('ADVA Optical Networking')
class OspfMetricType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("e1", 1), ("e2", 2))

class OspfRedistributionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("rip", 2))

class OspfState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("passive", 3))

class OspfAreaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("stub", 2))

class OspfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bdr", 1), ("dr", 2), ("drother", 3))

f3OspfConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1))
f3OspfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2))
f3OspfRouterTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1), )
if mibBuilder.loadTexts: f3OspfRouterTable.setStatus('current')
f3OspfRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1), ).setIndexNames((0, "F3-OSPF-MIB", "f3OspfRouterIndex"))
if mibBuilder.loadTexts: f3OspfRouterEntry.setStatus('current')
f3OspfRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 1), RouterID())
if mibBuilder.loadTexts: f3OspfRouterIndex.setStatus('current')
f3OspfRouterMetricType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 2), OspfMetricType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfRouterMetricType.setStatus('current')
f3OspfRouterMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777214))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfRouterMetric.setStatus('current')
f3OspfRouterRedistributionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 4), OspfRedistributionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfRouterRedistributionType.setStatus('current')
f3OspfRouterNumAttachedAreas = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OspfRouterNumAttachedAreas.setStatus('current')
f3OspfRouterAreaBdrRtrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfRouterAreaBdrRtrStatus.setStatus('current')
f3OspfRouterStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 7), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfRouterStorageType.setStatus('current')
f3OspfRouterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfRouterRowStatus.setStatus('current')
f3OspfAreaTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2), )
if mibBuilder.loadTexts: f3OspfAreaTable.setStatus('current')
f3OspfAreaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1), ).setIndexNames((0, "F3-OSPF-MIB", "f3OspfAreaId"))
if mibBuilder.loadTexts: f3OspfAreaEntry.setStatus('current')
f3OspfAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 1), AreaID())
if mibBuilder.loadTexts: f3OspfAreaId.setStatus('current')
f3OspfAreaType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 2), OspfAreaType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfAreaType.setStatus('current')
f3OspfAreaAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 3), OspfAuthenticationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfAreaAuthType.setStatus('current')
f3OspfAreaDefaultCost = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfAreaDefaultCost.setStatus('current')
f3OspfAreaSpfRuns = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OspfAreaSpfRuns.setStatus('current')
f3OspfAreaLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OspfAreaLsaCount.setStatus('current')
f3OspfAreaStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 7), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfAreaStorageType.setStatus('current')
f3OspfAreaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3OspfAreaRowStatus.setStatus('current')
f3OspfIpInterfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3), )
if mibBuilder.loadTexts: f3OspfIpInterfaceExtTable.setStatus('current')
f3OspfIpInterfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1), )
cmIpInterfaceEntry.registerAugmentions(("F3-OSPF-MIB", "f3OspfIpInterfaceExtEntry"))
f3OspfIpInterfaceExtEntry.setIndexNames(*cmIpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: f3OspfIpInterfaceExtEntry.setStatus('current')
f3OspfIpInterfaceExtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 1), OspfState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtStatus.setStatus('current')
f3OspfIpInterfaceExtAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 2), AreaID().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtAreaId.setStatus('current')
f3OspfIpInterfaceExtIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))).clone(namedValues=NamedValues(("broadcast", 1), ("nbma", 2), ("pointToPoint", 3), ("pointToMultipoint", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtIfType.setStatus('current')
f3OspfIpInterfaceExtHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 4), HelloRange().clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtHelloInterval.setStatus('current')
f3OspfIpInterfaceExtRtrDeadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(40)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtRtrDeadInterval.setStatus('current')
f3OspfIpInterfaceExtRetransInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtRetransInterval.setStatus('current')
f3OspfIpInterfaceExtRtrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 7), DesignatedRouterPriority().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtRtrPriority.setStatus('current')
f3OspfIpInterfaceExtCost = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtCost.setStatus('current')
f3OspfIpInterfaceExtAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 9), OspfAuthenticationType().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtAuthType.setStatus('current')
f3OspfIpInterfaceExtAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="0000000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpInterfaceExtAuthKey.setStatus('current')
f3OspfIpMgmtTunnelExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4), )
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtTable.setStatus('current')
f3OspfIpMgmtTunnelExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1), )
ipManagementTunnelEntry.registerAugmentions(("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtEntry"))
f3OspfIpMgmtTunnelExtEntry.setIndexNames(*ipManagementTunnelEntry.getIndexNames())
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtEntry.setStatus('current')
f3OspfIpMgmtTunnelExtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 1), OspfState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtStatus.setStatus('current')
f3OspfIpMgmtTunnelExtAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 2), AreaID().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtAreaId.setStatus('current')
f3OspfIpMgmtTunnelExtIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))).clone(namedValues=NamedValues(("broadcast", 1), ("nbma", 2), ("pointToPoint", 3), ("pointToMultipoint", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtIfType.setStatus('current')
f3OspfIpMgmtTunnelExtHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 4), HelloRange().clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtHelloInterval.setStatus('current')
f3OspfIpMgmtTunnelExtRtrDeadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(40)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtRtrDeadInterval.setStatus('current')
f3OspfIpMgmtTunnelExtRetransInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtRetransInterval.setStatus('current')
f3OspfIpMgmtTunnelExtRtrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 7), DesignatedRouterPriority().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtRtrPriority.setStatus('current')
f3OspfIpMgmtTunnelExtCost = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtCost.setStatus('current')
f3OspfIpMgmtTunnelExtAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 9), OspfAuthenticationType().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtAuthType.setStatus('current')
f3OspfIpMgmtTunnelExtAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="0000000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OspfIpMgmtTunnelExtAuthKey.setStatus('current')
f3OspfNbrExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 5), )
if mibBuilder.loadTexts: f3OspfNbrExtTable.setStatus('current')
f3OspfNbrExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 5, 1), )
ospfNbrEntry.registerAugmentions(("F3-OSPF-MIB", "f3OspfNbrExtEntry"))
f3OspfNbrExtEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
if mibBuilder.loadTexts: f3OspfNbrExtEntry.setStatus('current')
f3OspfNbrExtRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 5, 1, 1), OspfRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OspfNbrExtRole.setStatus('current')
f3OspfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 1))
f3OspfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2))
f3OspfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 1, 1)).setObjects(("F3-OSPF-MIB", "f3OspfRouterGroup"), ("F3-OSPF-MIB", "f3OspfAreaGroup"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtGroup"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtGroup"), ("F3-OSPF-MIB", "f3OspfNbrExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfCompliance = f3OspfCompliance.setStatus('current')
f3OspfRouterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 1)).setObjects(("F3-OSPF-MIB", "f3OspfRouterMetricType"), ("F3-OSPF-MIB", "f3OspfRouterMetric"), ("F3-OSPF-MIB", "f3OspfRouterRedistributionType"), ("F3-OSPF-MIB", "f3OspfRouterNumAttachedAreas"), ("F3-OSPF-MIB", "f3OspfRouterAreaBdrRtrStatus"), ("F3-OSPF-MIB", "f3OspfRouterStorageType"), ("F3-OSPF-MIB", "f3OspfRouterRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfRouterGroup = f3OspfRouterGroup.setStatus('current')
f3OspfAreaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 2)).setObjects(("F3-OSPF-MIB", "f3OspfAreaType"), ("F3-OSPF-MIB", "f3OspfAreaAuthType"), ("F3-OSPF-MIB", "f3OspfAreaDefaultCost"), ("F3-OSPF-MIB", "f3OspfAreaSpfRuns"), ("F3-OSPF-MIB", "f3OspfAreaLsaCount"), ("F3-OSPF-MIB", "f3OspfAreaStorageType"), ("F3-OSPF-MIB", "f3OspfAreaRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfAreaGroup = f3OspfAreaGroup.setStatus('current')
f3OspfIpInterfaceExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 3)).setObjects(("F3-OSPF-MIB", "f3OspfIpInterfaceExtStatus"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtAreaId"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtIfType"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtHelloInterval"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtRtrDeadInterval"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtRetransInterval"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtRtrPriority"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtCost"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtAuthType"), ("F3-OSPF-MIB", "f3OspfIpInterfaceExtAuthKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfIpInterfaceExtGroup = f3OspfIpInterfaceExtGroup.setStatus('current')
f3OspfIpMgmtTunnelExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 4)).setObjects(("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtStatus"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtAreaId"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtIfType"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtHelloInterval"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtRtrDeadInterval"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtRetransInterval"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtRtrPriority"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtCost"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtAuthType"), ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtAuthKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfIpMgmtTunnelExtGroup = f3OspfIpMgmtTunnelExtGroup.setStatus('current')
f3OspfNbrExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 5)).setObjects(("F3-OSPF-MIB", "f3OspfNbrExtRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfNbrExtGroup = f3OspfNbrExtGroup.setStatus('current')
mibBuilder.exportSymbols("F3-OSPF-MIB", f3OspfAreaId=f3OspfAreaId, f3OspfConfigObjects=f3OspfConfigObjects, f3OspfIpMgmtTunnelExtTable=f3OspfIpMgmtTunnelExtTable, f3OspfRouterRowStatus=f3OspfRouterRowStatus, f3OspfAreaRowStatus=f3OspfAreaRowStatus, OspfRole=OspfRole, f3OspfIpInterfaceExtRtrPriority=f3OspfIpInterfaceExtRtrPriority, f3OspfRouterMetric=f3OspfRouterMetric, f3OspfNbrExtTable=f3OspfNbrExtTable, f3OspfIpInterfaceExtStatus=f3OspfIpInterfaceExtStatus, OspfAreaType=OspfAreaType, f3OspfMIB=f3OspfMIB, f3OspfNbrExtEntry=f3OspfNbrExtEntry, f3OspfAreaAuthType=f3OspfAreaAuthType, f3OspfGroups=f3OspfGroups, f3OspfRouterAreaBdrRtrStatus=f3OspfRouterAreaBdrRtrStatus, f3OspfAreaStorageType=f3OspfAreaStorageType, f3OspfCompliances=f3OspfCompliances, f3OspfIpMgmtTunnelExtRtrDeadInterval=f3OspfIpMgmtTunnelExtRtrDeadInterval, f3OspfAreaTable=f3OspfAreaTable, f3OspfIpInterfaceExtEntry=f3OspfIpInterfaceExtEntry, f3OspfAreaGroup=f3OspfAreaGroup, f3OspfIpMgmtTunnelExtHelloInterval=f3OspfIpMgmtTunnelExtHelloInterval, f3OspfIpMgmtTunnelExtAuthKey=f3OspfIpMgmtTunnelExtAuthKey, f3OspfRouterIndex=f3OspfRouterIndex, OspfMetricType=OspfMetricType, f3OspfIpMgmtTunnelExtRetransInterval=f3OspfIpMgmtTunnelExtRetransInterval, f3OspfNbrExtGroup=f3OspfNbrExtGroup, OspfState=OspfState, f3OspfIpInterfaceExtRtrDeadInterval=f3OspfIpInterfaceExtRtrDeadInterval, f3OspfRouterNumAttachedAreas=f3OspfRouterNumAttachedAreas, f3OspfRouterTable=f3OspfRouterTable, f3OspfIpInterfaceExtIfType=f3OspfIpInterfaceExtIfType, f3OspfIpMgmtTunnelExtGroup=f3OspfIpMgmtTunnelExtGroup, f3OspfAreaType=f3OspfAreaType, f3OspfIpInterfaceExtAuthKey=f3OspfIpInterfaceExtAuthKey, f3OspfIpMgmtTunnelExtEntry=f3OspfIpMgmtTunnelExtEntry, f3OspfAreaDefaultCost=f3OspfAreaDefaultCost, f3OspfIpInterfaceExtRetransInterval=f3OspfIpInterfaceExtRetransInterval, f3OspfIpMgmtTunnelExtAreaId=f3OspfIpMgmtTunnelExtAreaId, f3OspfIpInterfaceExtGroup=f3OspfIpInterfaceExtGroup, f3OspfIpInterfaceExtAreaId=f3OspfIpInterfaceExtAreaId, f3OspfIpMgmtTunnelExtRtrPriority=f3OspfIpMgmtTunnelExtRtrPriority, f3OspfIpInterfaceExtHelloInterval=f3OspfIpInterfaceExtHelloInterval, f3OspfAreaEntry=f3OspfAreaEntry, f3OspfCompliance=f3OspfCompliance, f3OspfConformance=f3OspfConformance, f3OspfIpMgmtTunnelExtIfType=f3OspfIpMgmtTunnelExtIfType, OspfRedistributionType=OspfRedistributionType, f3OspfAreaSpfRuns=f3OspfAreaSpfRuns, f3OspfIpInterfaceExtAuthType=f3OspfIpInterfaceExtAuthType, f3OspfIpInterfaceExtCost=f3OspfIpInterfaceExtCost, f3OspfIpMgmtTunnelExtAuthType=f3OspfIpMgmtTunnelExtAuthType, f3OspfRouterRedistributionType=f3OspfRouterRedistributionType, f3OspfRouterStorageType=f3OspfRouterStorageType, f3OspfRouterEntry=f3OspfRouterEntry, f3OspfRouterMetricType=f3OspfRouterMetricType, f3OspfAreaLsaCount=f3OspfAreaLsaCount, f3OspfNbrExtRole=f3OspfNbrExtRole, f3OspfIpInterfaceExtTable=f3OspfIpInterfaceExtTable, f3OspfIpMgmtTunnelExtCost=f3OspfIpMgmtTunnelExtCost, f3OspfRouterGroup=f3OspfRouterGroup, PYSNMP_MODULE_ID=f3OspfMIB, f3OspfIpMgmtTunnelExtStatus=f3OspfIpMgmtTunnelExtStatus)
