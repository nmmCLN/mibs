#
# PySNMP MIB module PHION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/PHION-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:09:49 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Gauge32, ModuleIdentity, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, enterprises, Counter32, Counter64, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Gauge32", "ModuleIdentity", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "enterprises", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
phion = ModuleIdentity((1, 3, 6, 1, 4, 1, 10704))
phion.setRevisions(('2014-01-08 00:00', '2014-01-07 00:00', '2013-12-03 00:00',))
if mibBuilder.loadTexts: phion.setLastUpdated('201401080000Z')
if mibBuilder.loadTexts: phion.setOrganization('Barracuda Networks')
event = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 10))
firewall = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 1))
fwCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 20))
fwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21))
fwCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10704, 20, 1)).setObjects(("PHION-MIB", "boxGroup"), ("PHION-MIB", "serverGroup"), ("PHION-MIB", "releaseGroup"), ("PHION-MIB", "hotfixGroup"), ("PHION-MIB", "hwGroup"), ("PHION-MIB", "raidGroup"), ("PHION-MIB", "vpnGroup"), ("PHION-MIB", "bgpGroup"), ("PHION-MIB", "ospfGroup"), ("PHION-MIB", "ripGroup"), ("PHION-MIB", "fwstatsGroup"), ("PHION-MIB", "vpnusersGroup"), ("PHION-MIB", "trafficshapeGroup"), ("PHION-MIB", "diskspaceGroup"), ("PHION-MIB", "eventGroup"), ("PHION-MIB", "notificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fwCompliance = fwCompliance.setStatus('current')
serviceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 1))
firmwareGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 2))
hwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 3))
netGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 4))
eventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10704, 21, 5))
class ServiceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 4))
    namedValues = NamedValues(("unknown", -1), ("stopped", 0), ("started", 1), ("blocked", 2), ("removed", 4))

class SensorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3))
    namedValues = NamedValues(("unknown", -1), ("voltage", 0), ("fan", 1), ("temperature", 2), ("psu-status", 3))

class RaidEventSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("error", 1), ("warning", 2), ("information", 3), ("debug", 4))

class VpnStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1))
    namedValues = NamedValues(("down", -1), ("down-disabled", 0), ("active", 1))

boxServices = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 0), )
if mibBuilder.loadTexts: boxServices.setStatus('current')
boxServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 0, 1), ).setIndexNames((0, "PHION-MIB", "boxServiceName"))
if mibBuilder.loadTexts: boxServicesEntry.setStatus('current')
boxServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 0, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServiceName.setStatus('current')
boxServiceState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 0, 1, 2), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServiceState.setStatus('current')
boxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 1, 1)).setObjects(("PHION-MIB", "boxServiceName"), ("PHION-MIB", "boxServiceState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boxGroup = boxGroup.setStatus('current')
serverServices = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 1), )
if mibBuilder.loadTexts: serverServices.setStatus('current')
serverServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 1, 1), ).setIndexNames((0, "PHION-MIB", "serverServiceName"))
if mibBuilder.loadTexts: serverServicesEntry.setStatus('current')
serverServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverServiceName.setStatus('current')
serverServiceState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 1, 1, 2), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverServiceState.setStatus('current')
serverGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 1, 2)).setObjects(("PHION-MIB", "serverServiceName"), ("PHION-MIB", "serverServiceState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    serverGroup = serverGroup.setStatus('current')
phionRelease = MibScalar((1, 3, 6, 1, 4, 1, 10704, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phionRelease.setStatus('current')
releaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 2, 1)).setObjects(("PHION-MIB", "phionRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    releaseGroup = releaseGroup.setStatus('current')
phionHotfixes = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 3), )
if mibBuilder.loadTexts: phionHotfixes.setStatus('current')
phionHotfixesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 3, 1), ).setIndexNames((0, "PHION-MIB", "hotfixName"))
if mibBuilder.loadTexts: phionHotfixesEntry.setStatus('current')
hotfixName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hotfixName.setStatus('current')
hotfixInstallTime = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hotfixInstallTime.setStatus('current')
hotfixGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 2, 2)).setObjects(("PHION-MIB", "hotfixName"), ("PHION-MIB", "hotfixInstallTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hotfixGroup = hotfixGroup.setStatus('current')
hwSensors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 4), )
if mibBuilder.loadTexts: hwSensors.setStatus('current')
hwSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1), ).setIndexNames((0, "PHION-MIB", "hwSensorName"))
if mibBuilder.loadTexts: hwSensorsEntry.setStatus('current')
hwSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSensorName.setStatus('current')
hwSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 2), SensorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSensorType.setStatus('current')
hwSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSensorValue.setStatus('current')
hwGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 1)).setObjects(("PHION-MIB", "hwSensorName"), ("PHION-MIB", "hwSensorType"), ("PHION-MIB", "hwSensorValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGroup = hwGroup.setStatus('current')
raidEvents = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 5), )
if mibBuilder.loadTexts: raidEvents.setStatus('current')
raidEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1), ).setIndexNames((0, "PHION-MIB", "raidEventIndex"))
if mibBuilder.loadTexts: raidEventsEntry.setStatus('current')
raidEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventIndex.setStatus('current')
raidEventSev = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 2), RaidEventSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventSev.setStatus('current')
raidEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventTime.setStatus('current')
raidEventText = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventText.setStatus('current')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 2)).setObjects(("PHION-MIB", "raidEventIndex"), ("PHION-MIB", "raidEventSev"), ("PHION-MIB", "raidEventTime"), ("PHION-MIB", "raidEventText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
vpnTunnels = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 6), )
if mibBuilder.loadTexts: vpnTunnels.setStatus('current')
vpnTunnelsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 6, 1), ).setIndexNames((0, "PHION-MIB", "vpnName"))
if mibBuilder.loadTexts: vpnTunnelsEntry.setStatus('current')
vpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnName.setStatus('current')
vpnState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 6, 1, 2), VpnStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnState.setStatus('current')
vpnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 1)).setObjects(("PHION-MIB", "vpnName"), ("PHION-MIB", "vpnState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vpnGroup = vpnGroup.setStatus('current')
bgpNeighbors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 7), )
if mibBuilder.loadTexts: bgpNeighbors.setStatus('current')
bgpNeighborsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 7, 1), ).setIndexNames((0, "PHION-MIB", "bgpNeighborAddress"))
if mibBuilder.loadTexts: bgpNeighborsEntry.setStatus('current')
bgpNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 7, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpNeighborAddress.setStatus('current')
bgpNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpNeighborState.setStatus('current')
bgpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 2)).setObjects(("PHION-MIB", "bgpNeighborAddress"), ("PHION-MIB", "bgpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgpGroup = bgpGroup.setStatus('current')
ospfNeighbors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 8), )
if mibBuilder.loadTexts: ospfNeighbors.setStatus('current')
ospfNeighborsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1), ).setIndexNames((0, "PHION-MIB", "ospfNeighborId"))
if mibBuilder.loadTexts: ospfNeighborsEntry.setStatus('current')
ospfNeighborId = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborId.setStatus('current')
ospfNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborAddress.setStatus('current')
ospfNeighborInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborInterface.setStatus('current')
ospfNeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNeighborStatus.setStatus('current')
ospfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 3)).setObjects(("PHION-MIB", "ospfNeighborId"), ("PHION-MIB", "ospfNeighborAddress"), ("PHION-MIB", "ospfNeighborInterface"), ("PHION-MIB", "ospfNeighborStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfGroup = ospfGroup.setStatus('current')
ripNeighbors = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 9), )
if mibBuilder.loadTexts: ripNeighbors.setStatus('current')
ripNeighborsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 9, 1), ).setIndexNames((0, "PHION-MIB", "ripNeighborAddress"))
if mibBuilder.loadTexts: ripNeighborsEntry.setStatus('current')
ripNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ripNeighborAddress.setStatus('current')
ripNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ripNeighborState.setStatus('current')
ripGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 4)).setObjects(("PHION-MIB", "ripNeighborAddress"), ("PHION-MIB", "ripNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ripGroup = ripGroup.setStatus('current')
fwStats = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 10), )
if mibBuilder.loadTexts: fwStats.setStatus('current')
fwStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1), ).setIndexNames((0, "PHION-MIB", "firewallSessions"))
if mibBuilder.loadTexts: fwStatsEntry.setStatus('current')
firewallSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firewallSessions.setStatus('current')
packetThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packetThroughput.setStatus('current')
dataThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataThroughput.setStatus('current')
firewallSessions64 = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firewallSessions64.setStatus('current')
packetThroughput64 = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packetThroughput64.setStatus('current')
dataThroughput64 = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataThroughput64.setStatus('current')
fwstatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 3)).setObjects(("PHION-MIB", "firewallSessions"), ("PHION-MIB", "packetThroughput"), ("PHION-MIB", "dataThroughput"), ("PHION-MIB", "firewallSessions64"), ("PHION-MIB", "packetThroughput64"), ("PHION-MIB", "dataThroughput64"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fwstatsGroup = fwstatsGroup.setStatus('current')
vpnUsers = MibScalar((1, 3, 6, 1, 4, 1, 10704, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnUsers.setStatus('current')
vpnusersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 4, 5)).setObjects(("PHION-MIB", "vpnUsers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vpnusersGroup = vpnusersGroup.setStatus('current')
trafficShape = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 12), )
if mibBuilder.loadTexts: trafficShape.setStatus('current')
trafficShapeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1), ).setIndexNames((0, "PHION-MIB", "connectorName"))
if mibBuilder.loadTexts: trafficShapeEntry.setStatus('current')
connectorName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectorName.setStatus('current')
rate = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rate.setStatus('current')
sessions = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessions.setStatus('current')
class1Total = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class1Total.setStatus('current')
class1Pakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class1Pakets.setStatus('current')
class1Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class1Drop.setStatus('current')
class2Total = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class2Total.setStatus('current')
class2Pakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class2Pakets.setStatus('current')
class2Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class2Drop.setStatus('current')
class3Total = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class3Total.setStatus('current')
class3Pakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class3Pakets.setStatus('current')
class3Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: class3Drop.setStatus('current')
noDelayTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noDelayTotal.setStatus('current')
noDelayPakets = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noDelayPakets.setStatus('current')
noDelayDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noDelayDrop.setStatus('current')
trafficshapeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 4)).setObjects(("PHION-MIB", "connectorName"), ("PHION-MIB", "rate"), ("PHION-MIB", "sessions"), ("PHION-MIB", "class1Total"), ("PHION-MIB", "class1Pakets"), ("PHION-MIB", "class1Drop"), ("PHION-MIB", "class2Total"), ("PHION-MIB", "class2Pakets"), ("PHION-MIB", "class2Drop"), ("PHION-MIB", "class3Total"), ("PHION-MIB", "class3Pakets"), ("PHION-MIB", "class3Drop"), ("PHION-MIB", "noDelayTotal"), ("PHION-MIB", "noDelayPakets"), ("PHION-MIB", "noDelayDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trafficshapeGroup = trafficshapeGroup.setStatus('current')
diskSpace = MibTable((1, 3, 6, 1, 4, 1, 10704, 1, 13), )
if mibBuilder.loadTexts: diskSpace.setStatus('current')
diskSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1), ).setIndexNames((0, "PHION-MIB", "partitionName"))
if mibBuilder.loadTexts: diskSpaceEntry.setStatus('current')
partitionName = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionName.setStatus('current')
partitionMaxSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionMaxSpace.setStatus('current')
partitionFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionFreeSpace.setStatus('current')
partitionUsedSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionUsedSpace.setStatus('current')
partitionUsedSpacePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 10704, 1, 13, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: partitionUsedSpacePercent.setStatus('current')
diskspaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 3, 5)).setObjects(("PHION-MIB", "partitionName"), ("PHION-MIB", "partitionMaxSpace"), ("PHION-MIB", "partitionFreeSpace"), ("PHION-MIB", "partitionUsedSpace"), ("PHION-MIB", "partitionUsedSpacePercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diskspaceGroup = diskspaceGroup.setStatus('current')
eventID = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventID.setStatus('current')
eventIDDescription = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventIDDescription.setStatus('current')
eventType = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('current')
eventAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmTime.setStatus('current')
eventLayerDescription = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLayerDescription.setStatus('current')
eventClassification = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClassification.setStatus('current')
eventRepresentation = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventRepresentation.setStatus('current')
eventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 10704, 10, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
eventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10704, 21, 5, 1)).setObjects(("PHION-MIB", "eventID"), ("PHION-MIB", "eventIDDescription"), ("PHION-MIB", "eventType"), ("PHION-MIB", "eventAlarmTime"), ("PHION-MIB", "eventLayerDescription"), ("PHION-MIB", "eventClassification"), ("PHION-MIB", "eventRepresentation"), ("PHION-MIB", "eventSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventGroup = eventGroup.setStatus('current')
eventTrap = NotificationType((1, 3, 6, 1, 4, 1, 10704, 11)).setObjects(("PHION-MIB", "eventID"), ("PHION-MIB", "eventIDDescription"), ("PHION-MIB", "eventType"), ("PHION-MIB", "eventAlarmTime"), ("PHION-MIB", "eventLayerDescription"), ("PHION-MIB", "eventClassification"), ("PHION-MIB", "eventRepresentation"), ("PHION-MIB", "eventSeverity"))
if mibBuilder.loadTexts: eventTrap.setStatus('current')
notificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10704, 21, 5, 2)).setObjects(("PHION-MIB", "eventTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationGroup = notificationGroup.setStatus('current')
mibBuilder.exportSymbols("PHION-MIB", hotfixName=hotfixName, eventRepresentation=eventRepresentation, raidGroup=raidGroup, class2Pakets=class2Pakets, firmwareGroups=firmwareGroups, raidEventsEntry=raidEventsEntry, raidEventIndex=raidEventIndex, connectorName=connectorName, serverGroup=serverGroup, phionHotfixesEntry=phionHotfixesEntry, partitionFreeSpace=partitionFreeSpace, vpnTunnelsEntry=vpnTunnelsEntry, class3Pakets=class3Pakets, SensorType=SensorType, vpnState=vpnState, serverServicesEntry=serverServicesEntry, eventLayerDescription=eventLayerDescription, fwGroups=fwGroups, boxServiceName=boxServiceName, diskspaceGroup=diskspaceGroup, eventClassification=eventClassification, ospfNeighborInterface=ospfNeighborInterface, hwGroup=hwGroup, eventType=eventType, eventGroups=eventGroups, vpnGroup=vpnGroup, fwCompliance=fwCompliance, trafficShapeEntry=trafficShapeEntry, dataThroughput=dataThroughput, raidEvents=raidEvents, serviceGroups=serviceGroups, trafficshapeGroup=trafficshapeGroup, phionRelease=phionRelease, netGroups=netGroups, serverServiceName=serverServiceName, hotfixGroup=hotfixGroup, partitionMaxSpace=partitionMaxSpace, ripNeighbors=ripNeighbors, class1Drop=class1Drop, raidEventText=raidEventText, ripNeighborState=ripNeighborState, eventTrap=eventTrap, event=event, ospfNeighborId=ospfNeighborId, class1Pakets=class1Pakets, ServiceState=ServiceState, class1Total=class1Total, PYSNMP_MODULE_ID=phion, vpnName=vpnName, ospfNeighbors=ospfNeighbors, trafficShape=trafficShape, firewall=firewall, hwGroups=hwGroups, rate=rate, hwSensorName=hwSensorName, hotfixInstallTime=hotfixInstallTime, phion=phion, vpnusersGroup=vpnusersGroup, serverServices=serverServices, class3Drop=class3Drop, partitionName=partitionName, class2Drop=class2Drop, noDelayTotal=noDelayTotal, eventID=eventID, ripNeighborAddress=ripNeighborAddress, hwSensorType=hwSensorType, vpnUsers=vpnUsers, notificationGroup=notificationGroup, RaidEventSeverity=RaidEventSeverity, fwCompliances=fwCompliances, boxServices=boxServices, boxServicesEntry=boxServicesEntry, diskSpace=diskSpace, bgpNeighborState=bgpNeighborState, noDelayDrop=noDelayDrop, eventAlarmTime=eventAlarmTime, ripGroup=ripGroup, eventGroup=eventGroup, VpnStates=VpnStates, class3Total=class3Total, phionHotfixes=phionHotfixes, eventSeverity=eventSeverity, noDelayPakets=noDelayPakets, hwSensors=hwSensors, eventIDDescription=eventIDDescription, packetThroughput64=packetThroughput64, vpnTunnels=vpnTunnels, raidEventTime=raidEventTime, partitionUsedSpace=partitionUsedSpace, releaseGroup=releaseGroup, bgpNeighborAddress=bgpNeighborAddress, diskSpaceEntry=diskSpaceEntry, fwstatsGroup=fwstatsGroup, dataThroughput64=dataThroughput64, hwSensorValue=hwSensorValue, boxServiceState=boxServiceState, ospfNeighborsEntry=ospfNeighborsEntry, sessions=sessions, firewallSessions64=firewallSessions64, serverServiceState=serverServiceState, partitionUsedSpacePercent=partitionUsedSpacePercent, packetThroughput=packetThroughput, ospfNeighborStatus=ospfNeighborStatus, raidEventSev=raidEventSev, boxGroup=boxGroup, bgpGroup=bgpGroup, bgpNeighborsEntry=bgpNeighborsEntry, fwStats=fwStats, class2Total=class2Total, hwSensorsEntry=hwSensorsEntry, fwStatsEntry=fwStatsEntry, ospfNeighborAddress=ospfNeighborAddress, ospfGroup=ospfGroup, ripNeighborsEntry=ripNeighborsEntry, firewallSessions=firewallSessions, bgpNeighbors=bgpNeighbors)
