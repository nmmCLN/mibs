#
# PySNMP MIB module CTRON-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DHCP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
nwIpRouter, nwIpMibs, nwIpClientServices, nwIpComponents = mibBuilder.importSymbols("CTRON-IP-ROUTER-MIB", "nwIpRouter", "nwIpMibs", "nwIpClientServices", "nwIpComponents")
nwRtrProtoSuites, = mibBuilder.importSymbols("ROUTER-OIDS", "nwRtrProtoSuites")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CTRON-DHCP-MIB", ctDhcpReleases=ctDhcpReleases, ctDhcpIfDomainName=ctDhcpIfDomainName, ctDhcp=ctDhcp, ctDhcpDiscovers=ctDhcpDiscovers, ctDhcpIfSubnetMask=ctDhcpIfSubnetMask, ctDhcpIfLeasePeriod=ctDhcpIfLeasePeriod, ctDhcpNoOfActiveClients=ctDhcpNoOfActiveClients, ctDhcpReclaimIP=ctDhcpReclaimIP, ctDhcpIfAddressesFree=ctDhcpIfAddressesFree, ctDhcpIfHighestAddress=ctDhcpIfHighestAddress, ctDhcpDeclines=ctDhcpDeclines, ctDhcpClientStatsID=ctDhcpClientStatsID, ctDhcpClientStatsTable=ctDhcpClientStatsTable, ctDhcpServerTime=ctDhcpServerTime, ctDhcpServerIfTable=ctDhcpServerIfTable, ctDhcpIfAddressesUsed=ctDhcpIfAddressesUsed, ctDhcpClientStatusTable=ctDhcpClientStatusTable, ctDhcpEndOfLease=ctDhcpEndOfLease, ctDhcpAdminStatus=ctDhcpAdminStatus, ctDhcpInterfaceConfig=ctDhcpInterfaceConfig, ctDhcpServerStats=ctDhcpServerStats, ctDhcpIfWINServer=ctDhcpIfWINServer, ctDhcpIfNetworkAddress=ctDhcpIfNetworkAddress, ctDhcpClientStatsEntry=ctDhcpClientStatsEntry, ctDhcpClientName=ctDhcpClientName, ctDhcpOffers=ctDhcpOffers, ctDhcpIfIndex=ctDhcpIfIndex, ctDhcpIfDefaultGateway=ctDhcpIfDefaultGateway, ctDhcpProtocolErrors=ctDhcpProtocolErrors, ctDhcpAcks=ctDhcpAcks, ctDhcpIfServerAddress=ctDhcpIfServerAddress, ctDhcpRequests=ctDhcpRequests, ctDhcpIfLowestaddress=ctDhcpIfLowestaddress, ctDhcpOperStatus=ctDhcpOperStatus, ctDhcpOtherServers=ctDhcpOtherServers, ctDhcpIfOperStatus=ctDhcpIfOperStatus, ctDhcpServerIfEntry=ctDhcpServerIfEntry, ctDhcpIfDomainNameServer=ctDhcpIfDomainNameServer, ctDhcpIfAdminStatus=ctDhcpIfAdminStatus, ctDhcpNaks=ctDhcpNaks, ctDhcpClientID=ctDhcpClientID, ctDhcpClientIP=ctDhcpClientIP)
