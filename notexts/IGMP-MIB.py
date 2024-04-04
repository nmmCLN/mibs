#
# PySNMP MIB module IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IGMP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:33 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Counter32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, ModuleIdentity, Bits, Unsigned32, ObjectIdentity, Counter64, TimeTicks, NotificationType, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "ModuleIdentity", "Bits", "Unsigned32", "ObjectIdentity", "Counter64", "TimeTicks", "NotificationType", "experimental")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
igmpMIB = ModuleIdentity((1, 3, 6, 1, 3, 59))
igmpMIB.setRevisions(('1995-08-15 00:00', '1997-01-06 00:00', '1997-12-18 00:00',))
if mibBuilder.loadTexts: igmpMIB.setLastUpdated('9712180000Z')
if mibBuilder.loadTexts: igmpMIB.setOrganization('IETF IDMR Working Group.')
igmpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 59, 1))
igmp = MibIdentifier((1, 3, 6, 1, 3, 59, 1, 1))
igmpInterfaceTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 1), )
if mibBuilder.loadTexts: igmpInterfaceTable.setStatus('current')
igmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 1, 1), ).setIndexNames((0, "IGMP-MIB", "igmpInterfaceIfIndex"))
if mibBuilder.loadTexts: igmpInterfaceEntry.setStatus('current')
igmpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setStatus('current')
igmpInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 2), Integer32().clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setStatus('current')
igmpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceStatus.setStatus('current')
igmpInterfaceVersion = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2))).clone('version2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceVersion.setStatus('current')
igmpInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerier.setStatus('current')
igmpInterfaceQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 6), Integer32().clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setStatus('current')
igmpInterfaceQuerierPresentTimeout = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 7), Integer32().clone(255)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQuerierPresentTimeout.setStatus('deprecated')
igmpInterfaceLeaveEnabled = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceLeaveEnabled.setStatus('deprecated')
igmpInterfaceVersion1QuerierTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 9), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setStatus('current')
igmpInterfaceWrongVersionQueries = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setStatus('current')
igmpInterfaceJoins = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceJoins.setStatus('current')
igmpInterfaceLeaves = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceLeaves.setStatus('deprecated')
igmpInterfaceGroups = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceGroups.setStatus('current')
igmpInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 14), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceRobustness.setStatus('current')
igmpCacheTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 2), )
if mibBuilder.loadTexts: igmpCacheTable.setStatus('current')
igmpCacheEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 2, 1), ).setIndexNames((0, "IGMP-MIB", "igmpCacheAddress"), (0, "IGMP-MIB", "igmpCacheIfIndex"))
if mibBuilder.loadTexts: igmpCacheEntry.setStatus('current')
igmpCacheAddress = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: igmpCacheAddress.setStatus('current')
igmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: igmpCacheIfIndex.setStatus('current')
igmpCacheSelf = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpCacheSelf.setStatus('current')
igmpCacheLastReporter = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheLastReporter.setStatus('current')
igmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheUpTime.setStatus('current')
igmpCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheExpiryTime.setStatus('current')
igmpCacheStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpCacheStatus.setStatus('current')
igmpCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 8), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setStatus('current')
igmpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 59, 2))
igmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 1))
igmpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 2))
igmpV1HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 1)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1HostMIBCompliance = igmpV1HostMIBCompliance.setStatus('current')
igmpV1RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 2)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"), ("IGMP-MIB", "igmpRouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1RouterMIBCompliance = igmpV1RouterMIBCompliance.setStatus('current')
igmpV2HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 3)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"), ("IGMP-MIB", "igmpV2HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBCompliance = igmpV2HostMIBCompliance.setStatus('current')
igmpV2RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 4)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"), ("IGMP-MIB", "igmpRouterMIBGroup"), ("IGMP-MIB", "igmpV2RouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBCompliance = igmpV2RouterMIBCompliance.setStatus('current')
igmpBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 1)).setObjects(("IGMP-MIB", "igmpCacheSelf"), ("IGMP-MIB", "igmpCacheLastReporter"), ("IGMP-MIB", "igmpCacheStatus"), ("IGMP-MIB", "igmpInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpBaseMIBGroup = igmpBaseMIBGroup.setStatus('current')
igmpRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 2)).setObjects(("IGMP-MIB", "igmpCacheUpTime"), ("IGMP-MIB", "igmpCacheExpiryTime"), ("IGMP-MIB", "igmpInterfaceQueryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpRouterMIBGroup = igmpRouterMIBGroup.setStatus('current')
igmpV2HostMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 3)).setObjects(("IGMP-MIB", "igmpInterfaceQuerier"), ("IGMP-MIB", "igmpInterfaceVersion1QuerierTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBGroup = igmpV2HostMIBGroup.setStatus('current')
igmpRouterVersion2MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 4)).setObjects(("IGMP-MIB", "igmpInterfaceVersion"), ("IGMP-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-MIB", "igmpInterfaceQuerierPresentTimeout"), ("IGMP-MIB", "igmpInterfaceLeaveEnabled"), ("IGMP-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-MIB", "igmpInterfaceJoins"), ("IGMP-MIB", "igmpInterfaceLeaves"), ("IGMP-MIB", "igmpCacheVersion1HostTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpRouterVersion2MIBGroup = igmpRouterVersion2MIBGroup.setStatus('deprecated')
igmpV2RouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 5)).setObjects(("IGMP-MIB", "igmpInterfaceVersion"), ("IGMP-MIB", "igmpInterfaceQuerier"), ("IGMP-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-MIB", "igmpInterfaceRobustness"), ("IGMP-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-MIB", "igmpInterfaceJoins"), ("IGMP-MIB", "igmpInterfaceGroups"), ("IGMP-MIB", "igmpCacheVersion1HostTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBGroup = igmpV2RouterMIBGroup.setStatus('current')
mibBuilder.exportSymbols("IGMP-MIB", igmpInterfaceStatus=igmpInterfaceStatus, igmpInterfaceGroups=igmpInterfaceGroups, igmpInterfaceQueryInterval=igmpInterfaceQueryInterval, igmpInterfaceWrongVersionQueries=igmpInterfaceWrongVersionQueries, igmpCacheStatus=igmpCacheStatus, igmpCacheAddress=igmpCacheAddress, igmpInterfaceIfIndex=igmpInterfaceIfIndex, igmpMIBObjects=igmpMIBObjects, igmpV2HostMIBCompliance=igmpV2HostMIBCompliance, igmpRouterVersion2MIBGroup=igmpRouterVersion2MIBGroup, igmpInterfaceQuerierPresentTimeout=igmpInterfaceQuerierPresentTimeout, igmpCacheSelf=igmpCacheSelf, igmpV1HostMIBCompliance=igmpV1HostMIBCompliance, igmpMIB=igmpMIB, igmpInterfaceRobustness=igmpInterfaceRobustness, igmpMIBConformance=igmpMIBConformance, igmpInterfaceJoins=igmpInterfaceJoins, igmpCacheExpiryTime=igmpCacheExpiryTime, igmp=igmp, igmpCacheUpTime=igmpCacheUpTime, igmpInterfaceVersion=igmpInterfaceVersion, igmpV2RouterMIBCompliance=igmpV2RouterMIBCompliance, igmpCacheLastReporter=igmpCacheLastReporter, igmpCacheTable=igmpCacheTable, igmpInterfaceQuerier=igmpInterfaceQuerier, PYSNMP_MODULE_ID=igmpMIB, igmpInterfaceVersion1QuerierTimer=igmpInterfaceVersion1QuerierTimer, igmpInterfaceLeaves=igmpInterfaceLeaves, igmpMIBGroups=igmpMIBGroups, igmpMIBCompliances=igmpMIBCompliances, igmpV2HostMIBGroup=igmpV2HostMIBGroup, igmpInterfaceQueryMaxResponseTime=igmpInterfaceQueryMaxResponseTime, igmpRouterMIBGroup=igmpRouterMIBGroup, igmpBaseMIBGroup=igmpBaseMIBGroup, igmpCacheIfIndex=igmpCacheIfIndex, igmpV1RouterMIBCompliance=igmpV1RouterMIBCompliance, igmpInterfaceEntry=igmpInterfaceEntry, igmpCacheVersion1HostTimer=igmpCacheVersion1HostTimer, igmpV2RouterMIBGroup=igmpV2RouterMIBGroup, igmpInterfaceLeaveEnabled=igmpInterfaceLeaveEnabled, igmpInterfaceTable=igmpInterfaceTable, igmpCacheEntry=igmpCacheEntry)
