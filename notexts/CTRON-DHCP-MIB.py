#
# PySNMP MIB module CTRON-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DHCP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:47 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
nwIpComponents, nwIpRouter, nwIpMibs, nwIpClientServices = mibBuilder.importSymbols("CTRON-IP-ROUTER-MIB", "nwIpComponents", "nwIpRouter", "nwIpMibs", "nwIpClientServices")
nwRtrProtoSuites, = mibBuilder.importSymbols("ROUTER-OIDS", "nwRtrProtoSuites")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, iso, Counter64, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "Counter64", "Gauge32", "NotificationType")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
ctDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2))
ctDhcpServerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1))
ctDhcpInterfaceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2))
ctDhcpClientStatusTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3))
ctDhcpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpAdminStatus.setStatus('mandatory')
ctDhcpOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOperStatus.setStatus('mandatory')
ctDhcpDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDiscovers.setStatus('mandatory')
ctDhcpOffers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOffers.setStatus('mandatory')
ctDhcpRequests = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpRequests.setStatus('mandatory')
ctDhcpDeclines = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDeclines.setStatus('mandatory')
ctDhcpReleases = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpReleases.setStatus('mandatory')
ctDhcpAcks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpAcks.setStatus('mandatory')
ctDhcpNaks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNaks.setStatus('mandatory')
ctDhcpOtherServers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOtherServers.setStatus('mandatory')
ctDhcpProtocolErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpProtocolErrors.setStatus('mandatory')
ctDhcpServerTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpServerTime.setStatus('mandatory')
ctDhcpNoOfActiveClients = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNoOfActiveClients.setStatus('mandatory')
ctDhcpReclaimIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpReclaimIP.setStatus('mandatory')
ctDhcpServerIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1), )
if mibBuilder.loadTexts: ctDhcpServerIfTable.setStatus('mandatory')
ctDhcpServerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpIfIndex"))
if mibBuilder.loadTexts: ctDhcpServerIfEntry.setStatus('mandatory')
ctDhcpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfIndex.setStatus('mandatory')
ctDhcpIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfAdminStatus.setStatus('mandatory')
ctDhcpIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("invalid-config", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfOperStatus.setStatus('mandatory')
ctDhcpIfServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfServerAddress.setStatus('mandatory')
ctDhcpIfNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfNetworkAddress.setStatus('mandatory')
ctDhcpIfSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfSubnetMask.setStatus('mandatory')
ctDhcpIfLowestaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLowestaddress.setStatus('mandatory')
ctDhcpIfHighestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfHighestAddress.setStatus('mandatory')
ctDhcpIfAddressesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesUsed.setStatus('mandatory')
ctDhcpIfAddressesFree = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesFree.setStatus('mandatory')
ctDhcpIfLeasePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLeasePeriod.setStatus('mandatory')
ctDhcpIfDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDefaultGateway.setStatus('mandatory')
ctDhcpIfDomainNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainNameServer.setStatus('mandatory')
ctDhcpIfDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 14), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainName.setStatus('mandatory')
ctDhcpIfWINServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfWINServer.setStatus('mandatory')
ctDhcpClientStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1), )
if mibBuilder.loadTexts: ctDhcpClientStatsTable.setStatus('mandatory')
ctDhcpClientStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpClientStatsID"))
if mibBuilder.loadTexts: ctDhcpClientStatsEntry.setStatus('mandatory')
ctDhcpClientStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientStatsID.setStatus('mandatory')
ctDhcpClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientName.setStatus('mandatory')
ctDhcpClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientIP.setStatus('mandatory')
ctDhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientID.setStatus('mandatory')
ctDhcpEndOfLease = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpEndOfLease.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-DHCP-MIB", ctDhcpAdminStatus=ctDhcpAdminStatus, ctDhcpIfWINServer=ctDhcpIfWINServer, ctDhcpIfServerAddress=ctDhcpIfServerAddress, ctDhcpIfLowestaddress=ctDhcpIfLowestaddress, ctDhcpReleases=ctDhcpReleases, ctDhcpServerTime=ctDhcpServerTime, ctDhcpEndOfLease=ctDhcpEndOfLease, ctDhcpIfDomainNameServer=ctDhcpIfDomainNameServer, ctDhcpServerIfEntry=ctDhcpServerIfEntry, ctDhcpIfSubnetMask=ctDhcpIfSubnetMask, ctDhcpOperStatus=ctDhcpOperStatus, ctDhcpNoOfActiveClients=ctDhcpNoOfActiveClients, ctDhcpIfDomainName=ctDhcpIfDomainName, ctDhcpIfOperStatus=ctDhcpIfOperStatus, ctDhcpServerStats=ctDhcpServerStats, ctDhcpClientStatusTable=ctDhcpClientStatusTable, ctDhcpClientName=ctDhcpClientName, ctDhcpDiscovers=ctDhcpDiscovers, ctDhcpAcks=ctDhcpAcks, ctDhcp=ctDhcp, ctDhcpOffers=ctDhcpOffers, ctDhcpClientIP=ctDhcpClientIP, ctDhcpIfAdminStatus=ctDhcpIfAdminStatus, ctDhcpOtherServers=ctDhcpOtherServers, ctDhcpProtocolErrors=ctDhcpProtocolErrors, ctDhcpIfNetworkAddress=ctDhcpIfNetworkAddress, ctDhcpIfAddressesUsed=ctDhcpIfAddressesUsed, ctDhcpClientStatsID=ctDhcpClientStatsID, ctDhcpInterfaceConfig=ctDhcpInterfaceConfig, ctDhcpIfAddressesFree=ctDhcpIfAddressesFree, ctDhcpClientStatsTable=ctDhcpClientStatsTable, ctDhcpIfDefaultGateway=ctDhcpIfDefaultGateway, ctDhcpReclaimIP=ctDhcpReclaimIP, ctDhcpDeclines=ctDhcpDeclines, ctDhcpNaks=ctDhcpNaks, ctDhcpIfLeasePeriod=ctDhcpIfLeasePeriod, ctDhcpIfHighestAddress=ctDhcpIfHighestAddress, ctDhcpClientStatsEntry=ctDhcpClientStatsEntry, ctDhcpClientID=ctDhcpClientID, ctDhcpIfIndex=ctDhcpIfIndex, ctDhcpServerIfTable=ctDhcpServerIfTable, ctDhcpRequests=ctDhcpRequests)
