#
# PySNMP MIB module PEAKFLOW-TMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-PEAKFLOW-TMS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:00 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
arbornetworksProducts, = mibBuilder.importSymbols("ARBOR-SMI", "arbornetworksProducts")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ifName, = mibBuilder.importSymbols("IF-MIB", "ifName")
Ipv6Address, Ipv6AddressPrefix = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address", "Ipv6AddressPrefix")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ObjectIdentity, TimeTicks, Unsigned32, iso, Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, Counter64, IpAddress, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Unsigned32", "iso", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter64", "IpAddress", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
peakflowTmsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9694, 1, 5))
peakflowTmsMIB.setRevisions(('2014-03-12 00:00', '2013-09-19 00:00', '2013-08-19 00:00', '2012-03-29 12:00', '2012-01-12 12:00', '2011-06-14 16:00', '2011-06-03 16:00', '2011-06-03 00:00', '2011-05-23 00:00', '2011-01-21 00:00', '2010-10-28 00:00', '2010-09-07 00:00', '2009-05-27 00:00', '2009-05-08 00:00', '2009-03-11 00:00', '2009-02-13 00:00', '2008-11-13 00:00', '2008-04-07 00:00', '2007-11-20 00:00', '2007-04-27 00:00',))
if mibBuilder.loadTexts: peakflowTmsMIB.setLastUpdated('201403120000Z')
if mibBuilder.loadTexts: peakflowTmsMIB.setOrganization('Arbor Networks, Inc.')
class TmsTableIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class TmsTableIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class TmsPercentage(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TmsHundredths(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

peakflowTmsMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2))
tmsHostFault = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsHostFault.setStatus('current')
tmsHostUpTime = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsHostUpTime.setStatus('current')
deviceCpuLoadAvg1min = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 3), TmsHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceCpuLoadAvg1min.setStatus('current')
deviceCpuLoadAvg5min = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 4), TmsHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceCpuLoadAvg5min.setStatus('current')
deviceCpuLoadAvg15min = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 5), TmsHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceCpuLoadAvg15min.setStatus('current')
deviceDiskUsage = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 6), TmsPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskUsage.setStatus('current')
devicePhysicalMemoryUsage = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 7), TmsPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devicePhysicalMemoryUsage.setStatus('current')
deviceSwapSpaceUsage = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 8), TmsPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSwapSpaceUsage.setStatus('current')
tmsTrapString = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapString.setStatus('current')
tmsTrapDetail = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapDetail.setStatus('current')
tmsTrapSubhostName = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapSubhostName.setStatus('current')
tmsTrapComponentName = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapComponentName.setStatus('current')
tmsTrapBgpPeer = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapBgpPeer.setStatus('current')
tmsTrapGreSource = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapGreSource.setStatus('current')
tmsTrapGreDestination = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapGreDestination.setStatus('current')
tmsTrapNexthop = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapNexthop.setStatus('current')
tmsTrapIpv6BgpPeer = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 17), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapIpv6BgpPeer.setStatus('current')
tmsTrapIpv6GreSource = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 18), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapIpv6GreSource.setStatus('current')
tmsTrapIpv6GreDestination = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 19), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapIpv6GreDestination.setStatus('current')
tmsTrapIpv6Nexthop = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 20), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapIpv6Nexthop.setStatus('current')
tmsTrapGreName = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsTrapGreName.setStatus('current')
peakflowTmsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3))
peakflowTmsTrapsEnumerate = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0))
hostFault = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsHostFault"))
if mibBuilder.loadTexts: hostFault.setStatus('obsolete')
greTunnelDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 2)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapGreSource"), ("PEAKFLOW-TMS-MIB", "tmsTrapGreDestination"))
if mibBuilder.loadTexts: greTunnelDown.setStatus('current')
greTunnelUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 3)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapGreSource"), ("PEAKFLOW-TMS-MIB", "tmsTrapGreDestination"))
if mibBuilder.loadTexts: greTunnelUp.setStatus('current')
tmsLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 4)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"))
if mibBuilder.loadTexts: tmsLinkUp.setStatus('obsolete')
tmsLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 5)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"))
if mibBuilder.loadTexts: tmsLinkDown.setStatus('obsolete')
subHostUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 6)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"))
if mibBuilder.loadTexts: subHostUp.setStatus('current')
subHostDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 7)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"))
if mibBuilder.loadTexts: subHostDown.setStatus('current')
tmsBgpNeighborDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 8)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapBgpPeer"))
if mibBuilder.loadTexts: tmsBgpNeighborDown.setStatus('current')
tmsBgpNeighborUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 9)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapBgpPeer"))
if mibBuilder.loadTexts: tmsBgpNeighborUp.setStatus('current')
tmsNexthopDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 10)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapNexthop"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: tmsNexthopDown.setStatus('current')
tmsNexthopUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 11)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapNexthop"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: tmsNexthopUp.setStatus('current')
tmsMitigationError = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 12)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsMitigationIndex"), ("PEAKFLOW-TMS-MIB", "tmsMitigationName"))
if mibBuilder.loadTexts: tmsMitigationError.setStatus('current')
tmsMitigationSuspended = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 13)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsMitigationIndex"), ("PEAKFLOW-TMS-MIB", "tmsMitigationName"))
if mibBuilder.loadTexts: tmsMitigationSuspended.setStatus('current')
tmsMitigationRunning = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 14)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsMitigationIndex"), ("PEAKFLOW-TMS-MIB", "tmsMitigationName"))
if mibBuilder.loadTexts: tmsMitigationRunning.setStatus('current')
tmsConfigMissing = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 15)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsConfigMissing.setStatus('current')
tmsConfigError = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 16)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsConfigError.setStatus('current')
tmsConfigOk = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 17)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsConfigOk.setStatus('current')
tmsHwDeviceDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 18)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsHwDeviceDown.setStatus('current')
tmsHwDeviceUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 19)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsHwDeviceUp.setStatus('current')
tmsHwSensorCritical = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 20)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsHwSensorCritical.setStatus('current')
tmsHwSensorOk = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 21)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsHwSensorOk.setStatus('current')
tmsSwComponentDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 22)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSwComponentDown.setStatus('current')
tmsSwComponentUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 23)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSwComponentUp.setStatus('current')
tmsSystemStatusCritical = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 24)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSystemStatusCritical.setStatus('current')
tmsSystemStatusDegraded = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 25)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSystemStatusDegraded.setStatus('current')
tmsSystemStatusNominal = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 26)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSystemStatusNominal.setStatus('current')
tmsFilesystemCritical = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 27)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsFilesystemCritical.setStatus('current')
tmsFilesystemNominal = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 28)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsFilesystemNominal.setStatus('current')
tmsHwSensorUnknown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 29)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsHwSensorUnknown.setStatus('current')
tmsSpCommunicationUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 30)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSpCommunicationUp.setStatus('current')
tmsSpCommunicationDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 31)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSpCommunicationDown.setStatus('current')
tmsSystemStatusError = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 32)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSystemStatusError.setStatus('current')
tmsAutomitigationBgpEnabled = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 33)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsAutomitigationBgpEnabled.setStatus('current')
tmsAutomitigationBgpDisabled = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 34)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsAutomitigationBgpDisabled.setStatus('current')
tmsAutomitigationBgpSuspended = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 35)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsAutomitigationBgpSuspended.setStatus('current')
tmsIpv6GreTunnelDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 36)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreSource"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreDestination"))
if mibBuilder.loadTexts: tmsIpv6GreTunnelDown.setStatus('current')
tmsIpv6GreTunnelUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 37)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreSource"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreDestination"))
if mibBuilder.loadTexts: tmsIpv6GreTunnelUp.setStatus('current')
tmsIpv6BgpNeighborDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 38)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6BgpPeer"))
if mibBuilder.loadTexts: tmsIpv6BgpNeighborDown.setStatus('current')
tmsIpv6BgpNeighborUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 39)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6BgpPeer"))
if mibBuilder.loadTexts: tmsIpv6BgpNeighborUp.setStatus('current')
tmsIpv6NexthopDown = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 40)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6Nexthop"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: tmsIpv6NexthopDown.setStatus('current')
tmsIpv6NexthopUp = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 41)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6Nexthop"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: tmsIpv6NexthopUp.setStatus('current')
tmsPerformanceOk = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 42)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsPerformanceOk.setStatus('current')
tmsPerformanceLossy = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 43)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsPerformanceLossy.setStatus('current')
tmsSystemPrefixesOk = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 44)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSystemPrefixesOk.setStatus('current')
tmsSystemPrefixesMissing = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 45)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSystemPrefixesMissing.setStatus('current')
tmsSpCommunicationDegraded = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 46)).setObjects(("SNMPv2-MIB", "sysName"), ("PEAKFLOW-TMS-MIB", "tmsTrapString"), ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"), ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
if mibBuilder.loadTexts: tmsSpCommunicationDegraded.setStatus('current')
peakflowTmsObj = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5))
tmsDpiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 1))
tmsVersion = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsVersion.setStatus('current')
tmsLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsLastUpdate.setStatus('current')
tmsMitigationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2))
tmsMitigationLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsMitigationLastUpdate.setStatus('current')
tmsMitigationNumber = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 2), TmsTableIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsMitigationNumber.setStatus('current')
tmsMitigationTable = MibTable((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3), )
if mibBuilder.loadTexts: tmsMitigationTable.setStatus('current')
tmsMitigationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1), ).setIndexNames((0, "PEAKFLOW-TMS-MIB", "tmsMitigationIndex"))
if mibBuilder.loadTexts: tmsMitigationEntry.setStatus('current')
tmsMitigationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 1), TmsTableIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsMitigationIndex.setStatus('current')
tmsMitigationId = MibTableColumn((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsMitigationId.setStatus('current')
tmsDestinationPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsDestinationPrefix.setStatus('current')
tmsDestinationPrefixMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsDestinationPrefixMask.setStatus('current')
tmsMitigationName = MibTableColumn((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsMitigationName.setStatus('current')
tmsIpv6DestinationPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 6), Ipv6AddressPrefix()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsIpv6DestinationPrefix.setStatus('current')
tmsIpv6DestinationPrefixMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsIpv6DestinationPrefixMask.setStatus('current')
mibBuilder.exportSymbols("PEAKFLOW-TMS-MIB", peakflowTmsMIB=peakflowTmsMIB, subHostUp=subHostUp, tmsSystemPrefixesOk=tmsSystemPrefixesOk, tmsHostUpTime=tmsHostUpTime, tmsSwComponentUp=tmsSwComponentUp, tmsTrapGreSource=tmsTrapGreSource, tmsVersion=tmsVersion, tmsPerformanceOk=tmsPerformanceOk, tmsTrapNexthop=tmsTrapNexthop, tmsHwSensorUnknown=tmsHwSensorUnknown, tmsSwComponentDown=tmsSwComponentDown, tmsIpv6NexthopUp=tmsIpv6NexthopUp, tmsIpv6GreTunnelUp=tmsIpv6GreTunnelUp, tmsMitigationRunning=tmsMitigationRunning, deviceCpuLoadAvg15min=deviceCpuLoadAvg15min, tmsMitigationTable=tmsMitigationTable, tmsConfigOk=tmsConfigOk, tmsMitigationNumber=tmsMitigationNumber, deviceCpuLoadAvg5min=deviceCpuLoadAvg5min, tmsMitigationId=tmsMitigationId, peakflowTmsMgr=peakflowTmsMgr, tmsAutomitigationBgpEnabled=tmsAutomitigationBgpEnabled, tmsSystemStatusNominal=tmsSystemStatusNominal, deviceCpuLoadAvg1min=deviceCpuLoadAvg1min, tmsIpv6BgpNeighborUp=tmsIpv6BgpNeighborUp, tmsTrapGreName=tmsTrapGreName, tmsMitigationIndex=tmsMitigationIndex, tmsTrapGreDestination=tmsTrapGreDestination, tmsBgpNeighborUp=tmsBgpNeighborUp, tmsLinkDown=tmsLinkDown, tmsHwDeviceDown=tmsHwDeviceDown, subHostDown=subHostDown, tmsTrapBgpPeer=tmsTrapBgpPeer, tmsDestinationPrefixMask=tmsDestinationPrefixMask, tmsHwSensorOk=tmsHwSensorOk, peakflowTmsTraps=peakflowTmsTraps, tmsAutomitigationBgpSuspended=tmsAutomitigationBgpSuspended, TmsHundredths=TmsHundredths, tmsSpCommunicationDown=tmsSpCommunicationDown, peakflowTmsTrapsEnumerate=peakflowTmsTrapsEnumerate, tmsTrapDetail=tmsTrapDetail, tmsFilesystemCritical=tmsFilesystemCritical, tmsMitigationName=tmsMitigationName, tmsTrapString=tmsTrapString, tmsBgpNeighborDown=tmsBgpNeighborDown, tmsMitigationError=tmsMitigationError, tmsMitigationSuspended=tmsMitigationSuspended, tmsHostFault=tmsHostFault, tmsHwDeviceUp=tmsHwDeviceUp, tmsConfigMissing=tmsConfigMissing, TmsTableIndexOrZero=TmsTableIndexOrZero, tmsNexthopDown=tmsNexthopDown, tmsMitigationEntry=tmsMitigationEntry, tmsIpv6BgpNeighborDown=tmsIpv6BgpNeighborDown, tmsSystemStatusDegraded=tmsSystemStatusDegraded, tmsIpv6DestinationPrefixMask=tmsIpv6DestinationPrefixMask, devicePhysicalMemoryUsage=devicePhysicalMemoryUsage, tmsSystemStatusError=tmsSystemStatusError, deviceSwapSpaceUsage=deviceSwapSpaceUsage, tmsPerformanceLossy=tmsPerformanceLossy, tmsConfigError=tmsConfigError, tmsMitigationLastUpdate=tmsMitigationLastUpdate, tmsTrapIpv6GreDestination=tmsTrapIpv6GreDestination, greTunnelUp=greTunnelUp, tmsSpCommunicationDegraded=tmsSpCommunicationDegraded, tmsIpv6NexthopDown=tmsIpv6NexthopDown, tmsTrapIpv6GreSource=tmsTrapIpv6GreSource, tmsSpCommunicationUp=tmsSpCommunicationUp, tmsLinkUp=tmsLinkUp, tmsIpv6DestinationPrefix=tmsIpv6DestinationPrefix, tmsNexthopUp=tmsNexthopUp, deviceDiskUsage=deviceDiskUsage, tmsSystemPrefixesMissing=tmsSystemPrefixesMissing, tmsLastUpdate=tmsLastUpdate, PYSNMP_MODULE_ID=peakflowTmsMIB, tmsTrapIpv6Nexthop=tmsTrapIpv6Nexthop, TmsPercentage=TmsPercentage, tmsHwSensorCritical=tmsHwSensorCritical, tmsTrapSubhostName=tmsTrapSubhostName, tmsTrapIpv6BgpPeer=tmsTrapIpv6BgpPeer, tmsMitigationConfig=tmsMitigationConfig, tmsDpiConfig=tmsDpiConfig, tmsAutomitigationBgpDisabled=tmsAutomitigationBgpDisabled, tmsFilesystemNominal=tmsFilesystemNominal, TmsTableIndex=TmsTableIndex, greTunnelDown=greTunnelDown, tmsIpv6GreTunnelDown=tmsIpv6GreTunnelDown, peakflowTmsObj=peakflowTmsObj, tmsTrapComponentName=tmsTrapComponentName, hostFault=hostFault, tmsDestinationPrefix=tmsDestinationPrefix, tmsSystemStatusCritical=tmsSystemStatusCritical)
