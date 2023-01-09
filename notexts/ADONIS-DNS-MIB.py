#
# PySNMP MIB module ADONIS-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/ADONIS-DNS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:46 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
appliances, = mibBuilder.importSymbols("BLUECATNETWORKS-MIB", "appliances")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso, MibIdentifier, IpAddress, Integer32, Counter32, Gauge32, Unsigned32, ObjectIdentity, Bits, NotificationType, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso", "MibIdentifier", "IpAddress", "Integer32", "Counter32", "Gauge32", "Unsigned32", "ObjectIdentity", "Bits", "NotificationType", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adonis = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 100, 101))
if mibBuilder.loadTexts: adonis.setLastUpdated('200810010000Z')
if mibBuilder.loadTexts: adonis.setOrganization('BlueCat Networks Inc.')
adonisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1))
dns = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1))
dnsDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1))
dnsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2))
dhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2))
dhcpDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1))
dhcpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2))
dhcpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3))
ha = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3))
haService = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1))
commandServer = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4))
commandServerDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4, 1))
lcd = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5))
lcdDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1))
tftp = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6))
tftpDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6, 1))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7))
systemDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7, 1))
adonisTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2))
trapDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 1))
trapHA = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 2))
trapCommandServer = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 3))
trapDHCP = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 4))
trapReplication = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 5))
trapTFTP = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 6))
trapSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 7))
dnsDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonRunning.setStatus('current')
dnsDaemonNumberOfZones = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonNumberOfZones.setStatus('current')
dnsDaemonDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonDebugLevel.setStatus('current')
dnsDaemonZoneTransfersInProgress = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonZoneTransfersInProgress.setStatus('current')
dnsDaemonZoneTransfersDeferred = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonZoneTransfersDeferred.setStatus('current')
dnsDaemonSOAQueriesInProgress = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonSOAQueriesInProgress.setStatus('current')
dnsDaemonQueryLoggingState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonQueryLoggingState.setStatus('current')
dnsDaemonZoneTransferFailure = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonZoneTransferFailure.setStatus('current')
dnsStatsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsSuccess.setStatus('current')
dnsStatsReferral = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsReferral.setStatus('current')
dnsStatsNXRRSet = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsNXRRSet.setStatus('current')
dnsStatsNXDomain = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsNXDomain.setStatus('current')
dnsStatsRecursion = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsRecursion.setStatus('current')
dnsStatsFailure = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsFailure.setStatus('current')
dhcpDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDaemonRunning.setStatus('current')
dhcpDaemonSubnetAlert = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDaemonSubnetAlert.setStatus('current')
dhcpDaemonLeaseStatsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDaemonLeaseStatsSuccess.setStatus('current')
dhcpFailOverState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpFailOverState.setStatus('current')
dhcpLeaseTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseTable.setStatus('current')
dhcpLeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpIP"))
if mibBuilder.loadTexts: dhcpLeaseEntry.setStatus('current')
dhcpIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpIP.setStatus('current')
dhcpLeaseStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseStartTime.setStatus('current')
dhcpLeaseEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseEndTime.setStatus('current')
dhcpLeaseTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseTimeStamp.setStatus('current')
dhcpLeaseBindState = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("free", 0), ("active", 1), ("fixed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseBindState.setStatus('current')
dhcpLeaseHardwareAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseHardwareAddress.setStatus('current')
dhcpLeaseHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseHostname.setStatus('current')
dhcpSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetTable.setStatus('current')
dhcpSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpSubnetIP"))
if mibBuilder.loadTexts: dhcpSubnetEntry.setStatus('current')
dhcpSubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetIP.setStatus('current')
dhcpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetMask.setStatus('current')
dhcpSubnetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetSize.setStatus('current')
dhcpSubnetUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetUsed.setStatus('current')
dhcpSubnetAlert = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetAlert.setStatus('current')
dhcpPoolTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolTable.setStatus('current')
dhcpPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpPoolStartIP"))
if mibBuilder.loadTexts: dhcpPoolEntry.setStatus('current')
dhcpPoolSubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolSubnetIP.setStatus('current')
dhcpPoolStartIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolStartIP.setStatus('current')
dhcpPoolEndIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolEndIP.setStatus('current')
dhcpPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolSize.setStatus('current')
dhcpPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolUsed.setStatus('current')
dhcpPoolAlert = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolAlert.setStatus('current')
dhcpFixedIPTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpFixedIPTable.setStatus('current')
dhcpFixedIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpFixedIP"))
if mibBuilder.loadTexts: dhcpFixedIPEntry.setStatus('current')
dhcpFixedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpFixedIP.setStatus('current')
haServiceRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haServiceRunning.setStatus('current')
haServiceNodeType = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haServiceNodeType.setStatus('current')
haReplicationBinding = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haReplicationBinding.setStatus('current')
commandServerDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandServerDaemonRunning.setStatus('current')
systemState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemState.setStatus('current')
tftpDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpDaemonRunning.setStatus('current')
licenseValid = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseValid.setStatus('current')
licenseExpiry = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseExpiry.setStatus('current')
trapDNSDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 1, 1)).setObjects(("ADONIS-DNS-MIB", "dnsDaemonRunning"), ("ADONIS-DNS-MIB", "dnsDaemonZoneTransferFailure"))
if mibBuilder.loadTexts: trapDNSDaemon.setStatus('current')
trapDHCPDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 4, 1)).setObjects(("ADONIS-DNS-MIB", "dhcpDaemonRunning"), ("ADONIS-DNS-MIB", "dhcpDaemonSubnetAlert"), ("ADONIS-DNS-MIB", "dhcpFailOverState"))
if mibBuilder.loadTexts: trapDHCPDaemon.setStatus('current')
trapHAServiceFailOver = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 2, 1)).setObjects(("ADONIS-DNS-MIB", "haServiceNodeType"))
if mibBuilder.loadTexts: trapHAServiceFailOver.setStatus('current')
trapCommandServerDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 3, 1)).setObjects(("ADONIS-DNS-MIB", "commandServerDaemonRunning"))
if mibBuilder.loadTexts: trapCommandServerDaemon.setStatus('current')
trapSystemDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 7, 1)).setObjects(("ADONIS-DNS-MIB", "systemState"))
if mibBuilder.loadTexts: trapSystemDaemon.setStatus('current')
trapReplicationFailure = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 5, 1))
if mibBuilder.loadTexts: trapReplicationFailure.setStatus('current')
trapTFTPDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 6, 1)).setObjects(("ADONIS-DNS-MIB", "tftpDaemonRunning"))
if mibBuilder.loadTexts: trapTFTPDaemon.setStatus('current')
mibBuilder.exportSymbols("ADONIS-DNS-MIB", dhcpLeaseStartTime=dhcpLeaseStartTime, systemState=systemState, dhcpPoolAlert=dhcpPoolAlert, trapCommandServerDaemon=trapCommandServerDaemon, adonis=adonis, dnsDaemonQueryLoggingState=dnsDaemonQueryLoggingState, dnsDaemonDebugLevel=dnsDaemonDebugLevel, dhcpPoolUsed=dhcpPoolUsed, dhcp=dhcp, dnsDaemonZoneTransfersInProgress=dnsDaemonZoneTransfersInProgress, licenseExpiry=licenseExpiry, dhcpFailOverState=dhcpFailOverState, dhcpSubnetMask=dhcpSubnetMask, dnsStatsNXDomain=dnsStatsNXDomain, dhcpFixedIPEntry=dhcpFixedIPEntry, dhcpDaemonLeaseStatsSuccess=dhcpDaemonLeaseStatsSuccess, dnsStatsSuccess=dnsStatsSuccess, licenseValid=licenseValid, dnsDaemonZoneTransferFailure=dnsDaemonZoneTransferFailure, lcd=lcd, trapDHCPDaemon=trapDHCPDaemon, dhcpSubnetUsed=dhcpSubnetUsed, trapHAServiceFailOver=trapHAServiceFailOver, tftpDaemonRunning=tftpDaemonRunning, dnsDaemonSOAQueriesInProgress=dnsDaemonSOAQueriesInProgress, commandServerDaemon=commandServerDaemon, dhcpStats=dhcpStats, dhcpSubnetEntry=dhcpSubnetEntry, dnsDaemonZoneTransfersDeferred=dnsDaemonZoneTransfersDeferred, trapDNS=trapDNS, haService=haService, adonisTraps=adonisTraps, dhcpFixedIPTable=dhcpFixedIPTable, trapDHCP=trapDHCP, trapSystemDaemon=trapSystemDaemon, tftp=tftp, dhcpLeaseEndTime=dhcpLeaseEndTime, dhcpPoolTable=dhcpPoolTable, tftpDaemon=tftpDaemon, dhcpFixedIP=dhcpFixedIP, dhcpDaemonRunning=dhcpDaemonRunning, dnsDaemonRunning=dnsDaemonRunning, trapReplication=trapReplication, trapCommandServer=trapCommandServer, dnsStatsFailure=dnsStatsFailure, haServiceRunning=haServiceRunning, system=system, dns=dns, dhcpLeaseTimeStamp=dhcpLeaseTimeStamp, PYSNMP_MODULE_ID=adonis, dnsStatsRecursion=dnsStatsRecursion, commandServer=commandServer, dhcpSubnetAlert=dhcpSubnetAlert, haReplicationBinding=haReplicationBinding, dhcpSubnetIP=dhcpSubnetIP, dhcpSubnetSize=dhcpSubnetSize, trapReplicationFailure=trapReplicationFailure, dhcpLeaseTable=dhcpLeaseTable, dhcpDaemon=dhcpDaemon, trapTFTPDaemon=trapTFTPDaemon, dhcpLeaseEntry=dhcpLeaseEntry, dhcpPoolSubnetIP=dhcpPoolSubnetIP, trapDNSDaemon=trapDNSDaemon, dhcpLeaseBindState=dhcpLeaseBindState, dhcpPoolSize=dhcpPoolSize, dnsStatsReferral=dnsStatsReferral, haServiceNodeType=haServiceNodeType, dhcpSubnetTable=dhcpSubnetTable, commandServerDaemonRunning=commandServerDaemonRunning, systemDaemon=systemDaemon, dnsStats=dnsStats, dhcpLeaseHardwareAddress=dhcpLeaseHardwareAddress, ha=ha, dnsDaemonNumberOfZones=dnsDaemonNumberOfZones, trapSystem=trapSystem, dhcpConfig=dhcpConfig, trapHA=trapHA, dnsStatsNXRRSet=dnsStatsNXRRSet, dhcpDaemonSubnetAlert=dhcpDaemonSubnetAlert, dhcpIP=dhcpIP, dhcpPoolEntry=dhcpPoolEntry, trapTFTP=trapTFTP, dnsDaemon=dnsDaemon, dhcpLeaseHostname=dhcpLeaseHostname, dhcpPoolStartIP=dhcpPoolStartIP, adonisObjects=adonisObjects, dhcpPoolEndIP=dhcpPoolEndIP, lcdDaemon=lcdDaemon)
