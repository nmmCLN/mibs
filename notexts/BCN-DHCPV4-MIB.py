#
# PySNMP MIB module BCN-DHCPV4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-DHCPV4-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:48 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, IpAddress, Unsigned32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, ModuleIdentity, Counter32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "IpAddress", "Unsigned32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "ModuleIdentity", "Counter32", "TimeTicks", "Integer32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
bcnDhcpv4MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 1))
bcnDhcpv4MIB.setRevisions(('2010-12-08 00:00',))
if mibBuilder.loadTexts: bcnDhcpv4MIB.setLastUpdated('201012080000Z')
if mibBuilder.loadTexts: bcnDhcpv4MIB.setOrganization('BlueCat Networks')
bcnDhcpv4 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1))
bcnDhcpv4Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2))
bcnDhcpv4Notification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3))
bcnDhcpv4Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4))
bcnDhcpv4ServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1))
if mibBuilder.loadTexts: bcnDhcpv4ServiceStatus.setStatus('current')
bcnDhcpv4SerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SerOperState.setStatus('current')
bcnDhcpv4FirstAlertIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4FirstAlertIpAddr.setStatus('current')
bcnDhcpv4LeaseStatsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseStatsSuccess.setStatus('current')
bcnDhcpv4ServiceStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2))
if mibBuilder.loadTexts: bcnDhcpv4ServiceStatistics.setStatus('current')
bcnDhcpv4LeaseTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1), )
if mibBuilder.loadTexts: bcnDhcpv4LeaseTable.setStatus('current')
bcnDhcpv4LeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4LeaseIP"))
if mibBuilder.loadTexts: bcnDhcpv4LeaseEntry.setStatus('current')
bcnDhcpv4LeaseIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: bcnDhcpv4LeaseIP.setStatus('current')
bcnDhcpv4LeaseStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseStartTime.setStatus('current')
bcnDhcpv4LeaseEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseEndTime.setStatus('current')
bcnDhcpv4LeaseTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseTimeStamp.setStatus('current')
bcnDhcpv4LeaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseMacAddress.setStatus('current')
bcnDhcpv4LeaseHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseHostname.setStatus('current')
bcnDhcpv4SubnetTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2), )
if mibBuilder.loadTexts: bcnDhcpv4SubnetTable.setStatus('current')
bcnDhcpv4SubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4SubnetIP"))
if mibBuilder.loadTexts: bcnDhcpv4SubnetEntry.setStatus('current')
bcnDhcpv4SubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: bcnDhcpv4SubnetIP.setStatus('current')
bcnDhcpv4SubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetMask.setStatus('current')
bcnDhcpv4SubnetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetSize.setStatus('current')
bcnDhcpv4SubnetFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetFreeAddresses.setStatus('current')
bcnDhcpv4SubnetLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetLowThreshold.setStatus('current')
bcnDhcpv4SubnetHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetHighThreshold.setStatus('current')
bcnDhcpv4PoolTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3), )
if mibBuilder.loadTexts: bcnDhcpv4PoolTable.setStatus('current')
bcnDhcpv4PoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4PoolStartIP"))
if mibBuilder.loadTexts: bcnDhcpv4PoolEntry.setStatus('current')
bcnDhcpv4PoolStartIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: bcnDhcpv4PoolStartIP.setStatus('current')
bcnDhcpv4PoolEndIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolEndIP.setStatus('current')
bcnDhcpv4PoolSubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolSubnetIP.setStatus('current')
bcnDhcpv4PoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolSize.setStatus('current')
bcnDhcpv4PoolFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolFreeAddresses.setStatus('current')
bcnDhcpv4FixedIPTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4), )
if mibBuilder.loadTexts: bcnDhcpv4FixedIPTable.setStatus('current')
bcnDhcpv4FixedIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4FixedIP"))
if mibBuilder.loadTexts: bcnDhcpv4FixedIPEntry.setStatus('current')
bcnDhcpv4FixedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4FixedIP.setStatus('current')
bcnDhcpv4NotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0))
bcnDhcpv4NotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1))
bcnDhcpv4AlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4AlarmSeverity.setStatus('current')
bcnDhcpv4AlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4AlarmInfo.setStatus('current')
bcnDhcpv4FailOverState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 254))).clone(namedValues=NamedValues(("startup", 1), ("normal", 2), ("communicationsInterrupted", 3), ("partnerDown", 4), ("potentialConflict", 5), ("recover", 6), ("paused", 7), ("shutdown", 8), ("recoverDone", 9), ("recoverWait", 254)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4FailOverState.setStatus('current')
bcnDhcpv4SubnetAlertIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4SubnetAlertIpAddr.setStatus('current')
bcnDhcpv4AlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 1)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SerOperState"), ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmSeverity"), ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmInfo"))
if mibBuilder.loadTexts: bcnDhcpv4AlarmNotif.setStatus('current')
bcnDhcpv4FailOverNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 2)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverState"))
if mibBuilder.loadTexts: bcnDhcpv4FailOverNotif.setStatus('current')
bcnDhcpv4SubnetLowNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 3)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowThreshold"))
if mibBuilder.loadTexts: bcnDhcpv4SubnetLowNotif.setStatus('current')
bcnDhcpv4SubnetHighNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 4)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighThreshold"))
if mibBuilder.loadTexts: bcnDhcpv4SubnetHighNotif.setStatus('current')
bcnDhcpv4ServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 1))
bcnDhcpv4ServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2))
bcnDhcpv4ServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 1)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SerOperState"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FirstAlertIpAddr"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseStatsSuccess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4ServiceStatusGroup = bcnDhcpv4ServiceStatusGroup.setStatus('current')
bcnDhcpv4StatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 2)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseStartTime"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseEndTime"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseTimeStamp"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseMacAddress"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseHostname"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetMask"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetSize"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowThreshold"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighThreshold"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolSubnetIP"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolEndIP"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolSize"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FixedIP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4StatisticsGroup = bcnDhcpv4StatisticsGroup.setStatus('current')
bcnDhcpv4NotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 3)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmNotif"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverNotif"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowNotif"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4NotificationEventGroup = bcnDhcpv4NotificationEventGroup.setStatus('current')
bcnDhcpv4NotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 4)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmSeverity"), ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmInfo"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverState"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4NotificationDataGroup = bcnDhcpv4NotificationDataGroup.setStatus('current')
bcnDhcpv4StatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 1, 1)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4ServiceStatusGroup"), ("BCN-DHCPV4-MIB", "bcnDhcpv4StatisticsGroup"), ("BCN-DHCPV4-MIB", "bcnDhcpv4NotificationEventGroup"), ("BCN-DHCPV4-MIB", "bcnDhcpv4NotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4StatusCompliance = bcnDhcpv4StatusCompliance.setStatus('current')
mibBuilder.exportSymbols("BCN-DHCPV4-MIB", bcnDhcpv4SubnetSize=bcnDhcpv4SubnetSize, bcnDhcpv4LeaseStatsSuccess=bcnDhcpv4LeaseStatsSuccess, bcnDhcpv4PoolSize=bcnDhcpv4PoolSize, bcnDhcpv4NotificationData=bcnDhcpv4NotificationData, bcnDhcpv4AlarmSeverity=bcnDhcpv4AlarmSeverity, bcnDhcpv4SubnetHighNotif=bcnDhcpv4SubnetHighNotif, bcnDhcpv4MIB=bcnDhcpv4MIB, bcnDhcpv4PoolEndIP=bcnDhcpv4PoolEndIP, bcnDhcpv4PoolStartIP=bcnDhcpv4PoolStartIP, bcnDhcpv4Notification=bcnDhcpv4Notification, bcnDhcpv4NotificationEventGroup=bcnDhcpv4NotificationEventGroup, bcnDhcpv4SubnetTable=bcnDhcpv4SubnetTable, bcnDhcpv4Objects=bcnDhcpv4Objects, bcnDhcpv4ServiceStatistics=bcnDhcpv4ServiceStatistics, bcnDhcpv4AlarmNotif=bcnDhcpv4AlarmNotif, bcnDhcpv4=bcnDhcpv4, bcnDhcpv4PoolSubnetIP=bcnDhcpv4PoolSubnetIP, bcnDhcpv4FailOverState=bcnDhcpv4FailOverState, bcnDhcpv4LeaseHostname=bcnDhcpv4LeaseHostname, bcnDhcpv4LeaseTimeStamp=bcnDhcpv4LeaseTimeStamp, bcnDhcpv4NotificationEvents=bcnDhcpv4NotificationEvents, bcnDhcpv4SubnetLowNotif=bcnDhcpv4SubnetLowNotif, bcnDhcpv4Conformance=bcnDhcpv4Conformance, bcnDhcpv4LeaseEntry=bcnDhcpv4LeaseEntry, bcnDhcpv4LeaseStartTime=bcnDhcpv4LeaseStartTime, bcnDhcpv4PoolTable=bcnDhcpv4PoolTable, bcnDhcpv4FailOverNotif=bcnDhcpv4FailOverNotif, bcnDhcpv4ServiceStatusGroup=bcnDhcpv4ServiceStatusGroup, bcnDhcpv4NotificationDataGroup=bcnDhcpv4NotificationDataGroup, bcnDhcpv4FirstAlertIpAddr=bcnDhcpv4FirstAlertIpAddr, bcnDhcpv4SubnetLowThreshold=bcnDhcpv4SubnetLowThreshold, bcnDhcpv4SubnetMask=bcnDhcpv4SubnetMask, bcnDhcpv4SubnetAlertIpAddr=bcnDhcpv4SubnetAlertIpAddr, bcnDhcpv4FixedIPEntry=bcnDhcpv4FixedIPEntry, bcnDhcpv4FixedIP=bcnDhcpv4FixedIP, bcnDhcpv4StatusCompliance=bcnDhcpv4StatusCompliance, bcnDhcpv4PoolFreeAddresses=bcnDhcpv4PoolFreeAddresses, bcnDhcpv4LeaseIP=bcnDhcpv4LeaseIP, bcnDhcpv4LeaseTable=bcnDhcpv4LeaseTable, bcnDhcpv4FixedIPTable=bcnDhcpv4FixedIPTable, bcnDhcpv4PoolEntry=bcnDhcpv4PoolEntry, bcnDhcpv4AlarmInfo=bcnDhcpv4AlarmInfo, bcnDhcpv4ServiceGroups=bcnDhcpv4ServiceGroups, bcnDhcpv4LeaseMacAddress=bcnDhcpv4LeaseMacAddress, bcnDhcpv4ServiceStatus=bcnDhcpv4ServiceStatus, bcnDhcpv4LeaseEndTime=bcnDhcpv4LeaseEndTime, bcnDhcpv4StatisticsGroup=bcnDhcpv4StatisticsGroup, PYSNMP_MODULE_ID=bcnDhcpv4MIB, bcnDhcpv4SubnetEntry=bcnDhcpv4SubnetEntry, bcnDhcpv4ServiceCompliances=bcnDhcpv4ServiceCompliances, bcnDhcpv4SerOperState=bcnDhcpv4SerOperState, bcnDhcpv4SubnetIP=bcnDhcpv4SubnetIP, bcnDhcpv4SubnetHighThreshold=bcnDhcpv4SubnetHighThreshold, bcnDhcpv4SubnetFreeAddresses=bcnDhcpv4SubnetFreeAddresses)
