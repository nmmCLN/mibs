#
# PySNMP MIB module APDNSALG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APDNSALG-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:45 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ApRedundancyState, ApTransportType, ApHardwareModuleFamily = mibBuilder.importSymbols("ACMEPACKET-TC", "ApRedundancyState", "ApTransportType", "ApHardwareModuleFamily")
SysMgmtPercentage, = mibBuilder.importSymbols("APSYSMGMT-MIB", "SysMgmtPercentage")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifIndex")
InetVersion, InetAddressPrefixLength, InetAddress, InetZoneIndex, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetVersion", "InetAddressPrefixLength", "InetAddress", "InetZoneIndex", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Counter64, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, IpAddress, Unsigned32, iso, Integer32, Gauge32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Integer32", "Gauge32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apDNSALGModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 14))
apDNSALGModule.setRevisions(('2014-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apDNSALGModule.setRevisionsDescriptions(('Updated Organization and Contact info.',))
if mibBuilder.loadTexts: apDNSALGModule.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apDNSALGModule.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apDNSALGModule.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apDNSALGModule.setDescription('The Dns Alg MIB for Oracle Communications Acme Packet SBCs')
apDNSALGMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1))
apDNSALGMIBGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 1))
apDNSALGMIBTabularObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2))
apDNSALGNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2))
apDNSALGNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 1))
apDNSALGNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2))
apDNSALGNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0))
apDNSALGConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 3))
apDNSALGObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 1))
apDNSALGNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 2))
apDNSALGServerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1), )
if mibBuilder.loadTexts: apDNSALGServerStatusTable.setStatus('current')
if mibBuilder.loadTexts: apDNSALGServerStatusTable.setDescription('A read-only table to hold the status of configured DNSALG servers,\n            indexed by the name of the Dns alg config name, \n\t    server realm and server IP.')
apDNSALGServerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1), ).setIndexNames((0, "APDNSALG-MIB", "apDNSALGConfigIndex"), (0, "APDNSALG-MIB", "apDNSALGServerIndex"), (0, "APDNSALG-MIB", "apDNSALGServerIpAddress"))
if mibBuilder.loadTexts: apDNSALGServerStatusEntry.setStatus('current')
if mibBuilder.loadTexts: apDNSALGServerStatusEntry.setDescription('An entry designed to hold the status of a single DNSALG server')
apDNSALGConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDNSALGConfigIndex.setStatus('current')
if mibBuilder.loadTexts: apDNSALGConfigIndex.setDescription('An integer for the sole purpose of indexing the DNS-ALG configuration.Only one \n            DNS-ALG configuration is allowed per a realm.')
apDNSALGServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDNSALGServerIndex.setStatus('current')
if mibBuilder.loadTexts: apDNSALGServerIndex.setDescription('An integer for the sole purpose of indexing the Dns Server Attributes in a DNS-ALG config.\n            Each DNS-ALG config can have multiple Dns Server Attributes.')
apDNSALGConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDNSALGConfigName.setStatus('current')
if mibBuilder.loadTexts: apDNSALGConfigName.setDescription('The name of the dns-alg-config element that contains this\n            DNS-ALG server.')
apDNSALGServerRealm = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDNSALGServerRealm.setStatus('current')
if mibBuilder.loadTexts: apDNSALGServerRealm.setDescription('The name of the server realm element that contains this\n            DNSALG server.')
apDNSALGDomainSuffix = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDNSALGDomainSuffix.setStatus('current')
if mibBuilder.loadTexts: apDNSALGDomainSuffix.setDescription('The name of the domain suffix element that contains this\n            DNSALG server.')
apDNSALGServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDNSALGServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: apDNSALGServerIpAddress.setDescription('The IP address of this DNSALG server.')
apDNSALGServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inservice", 0), ("lowerpriority", 1), ("oosunreachable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDNSALGServerStatus.setStatus('current')
if mibBuilder.loadTexts: apDNSALGServerStatus.setDescription('The status of this DNSALG server.')
apDNSALGStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2), )
if mibBuilder.loadTexts: apDNSALGStatsTable.setStatus('current')
if mibBuilder.loadTexts: apDNSALGStatsTable.setDescription('per DNS-ALG config(i.e.client realm)stats.')
apDnsALGStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1), ).setIndexNames((0, "APDNSALG-MIB", "apDnsAlgClientRealmIndex"))
if mibBuilder.loadTexts: apDnsALGStatsEntry.setStatus('current')
if mibBuilder.loadTexts: apDnsALGStatsEntry.setDescription('A table entry designed to hold DNS-ALG stats data')
apDnsAlgClientRealmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDnsAlgClientRealmIndex.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgClientRealmIndex.setDescription('An integer for the sole purpose of indexing the DNS-ALG configuration.Only one \n            DNS-ALG configuration is allowed per a realm.')
apDnsAlgClientRealmName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgClientRealmName.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgClientRealmName.setDescription('DNS-ALG Config realm name')
apDnsAlgCurrentQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgCurrentQueries.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgCurrentQueries.setDescription('Number of queries sent in recent period received on DNS-ALG config realm.')
apDnsAlgTotalQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgTotalQueries.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgTotalQueries.setDescription('Total number of queries sent in life time received on DNS-ALG config realm.')
apDnsAlgCurrentSucess = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgCurrentSucess.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgCurrentSucess.setDescription('Number of success responses in recent period received on DNS-ALG config realm.')
apDnsAlgTotalSucess = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgTotalSucess.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgTotalSucess.setDescription('Total number of success responses in life time received on DNS-ALG config realm.')
apDnsAlgCurrentNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgCurrentNotFound.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgCurrentNotFound.setDescription('Number of not-found responses in recent period received on DNS-ALG config realm.')
apDnsAlgTotalNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgTotalNotFound.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgTotalNotFound.setDescription('Total number of not-found responses in life time received on DNS-ALG config realm.')
apDnsAlgCurrentTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgCurrentTimeOut.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgCurrentTimeOut.setDescription('Number of time out responses in recent period received on DNS-ALG config realm.')
apDnsAlgTotalTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgTotalTimeOut.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgTotalTimeOut.setDescription('Total number of time out responses in life time received on DNS-ALG config realm')
apDnsAlgCurrentBadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgCurrentBadStatus.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgCurrentBadStatus.setDescription('Number of bad status responses in recent period received on DNS-ALG config realm.')
apDnsAlgTotalBadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgTotalBadStatus.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgTotalBadStatus.setDescription('Total number of bad status responses in life time received on DNS-ALG config realm.')
apDnsAlgCurrentOtherFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgCurrentOtherFailures.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgCurrentOtherFailures.setDescription('Number of other failure responses in recent period received on DNS-ALG config realm.')
apDnsAlgTotalOtherFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgTotalOtherFailures.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgTotalOtherFailures.setDescription('Total number of other failure responses in life time received on DNS-ALG config realm.')
apDnsAlgAvgLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgAvgLatency.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgAvgLatency.setDescription('Average observed one-way signalling latency during the period\n                in milliseconds')
apDnsAlgMaxLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgMaxLatency.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgMaxLatency.setDescription('Maximum observed one-way signalling latency during the period\n                in milliseconds')
apDnsAlgMaxBurstRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgMaxBurstRate.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgMaxBurstRate.setDescription('Maximum burst rate of traffic measured during the\n                period (combined inbound and outbound)')
apDnsAlgConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 3), )
if mibBuilder.loadTexts: apDnsAlgConfigTable.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgConfigTable.setDescription('DNS Config info.')
apDnsAlgConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 3, 1), ).setIndexNames((0, "APDNSALG-MIB", "apDnsAlgConfigIndex"))
if mibBuilder.loadTexts: apDnsAlgConfigEntry.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgConfigEntry.setDescription('DNS ALG config and client realm info.')
apDnsAlgConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apDnsAlgConfigIndex.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgConfigIndex.setDescription('An integer for the sole purpose of indexing the DNS-ALG configuration.Only one \n            DNS-ALG configuration is allowed per a realm.')
apDnsAlgConfigClientRealm = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgConfigClientRealm.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgConfigClientRealm.setDescription('client realm name.')
apDnsAlgServerTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 4), )
if mibBuilder.loadTexts: apDnsAlgServerTable.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerTable.setDescription('DNS Alg Server table.')
apDnsAlgServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 4, 1), ).setIndexNames((0, "APDNSALG-MIB", "apDnsAlgConfigIndex"), (0, "APDNSALG-MIB", "apDnsAlgServerIndex"))
if mibBuilder.loadTexts: apDnsAlgServerEntry.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerEntry.setDescription('DNS ALG server entry.')
apDnsAlgServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apDnsAlgServerIndex.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerIndex.setDescription('An integer for the sole purpose of indexing the Dns Server.')
apDnsAlgServerRealm = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerRealm.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRealm.setDescription('The name of the server realm element that contains this\n            DnsAlg server.')
apDnsAlgServerRateStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5), )
if mibBuilder.loadTexts: apDnsAlgServerRateStatsTable.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateStatsTable.setDescription('DNS Alg Server message rate stats.')
apDnsAlgServerRateStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1), ).setIndexNames((0, "APDNSALG-MIB", "apDnsAlgConfigIndex"), (0, "APDNSALG-MIB", "apDnsAlgServerIndex"), (0, "APDNSALG-MIB", "apDnsAlgServerInetAddressType"), (0, "APDNSALG-MIB", "apDnsAlgServerInetAddress"))
if mibBuilder.loadTexts: apDnsAlgServerRateStatsEntry.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateStatsEntry.setDescription('DNS ALG server message rate statistics.')
apDnsAlgServerInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerInetAddressType.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerInetAddressType.setDescription('The IP address of this DnsAlg server.')
apDnsAlgServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerInetAddress.setDescription('The IP address of this DnsAlg server.')
apDnsAlgServerRateMsgRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 5), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerRateMsgRcvd.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateMsgRcvd.setDescription('The rate of messages received.')
apDnsAlgServerRateMsgSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 6), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerRateMsgSent.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateMsgSent.setDescription('The rate of messages sent.')
apDnsAlgServerRateReqRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 7), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerRateReqRcvd.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateReqRcvd.setDescription('The rate of request messages received.')
apDnsAlgServerRateReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 8), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerRateReqSent.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateReqSent.setDescription('The rate of request messages sent.')
apDnsAlgServerRateRspRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 9), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerRateRspRcvd.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateRspRcvd.setDescription('The rate of response messages received.')
apDnsAlgServerRateRspSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 5, 1, 10), Gauge32()).setUnits('messages per 10 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: apDnsAlgServerRateRspSent.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateRspSent.setDescription('The rate of response messages sent.')
apDNSALGConstraintsStatus = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inservice", 0), ("constraintsExceeded", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDNSALGConstraintsStatus.setStatus('current')
if mibBuilder.loadTexts: apDNSALGConstraintsStatus.setDescription('The status of this DNS-ALG config realm for constraints.')
apDnsAlgStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 1)).setObjects(("APDNSALG-MIB", "apDNSALGConfigName"), ("APDNSALG-MIB", "apDNSALGServerRealm"), ("APDNSALG-MIB", "apDNSALGServerIpAddress"), ("APDNSALG-MIB", "apDNSALGServerStatus"))
if mibBuilder.loadTexts: apDnsAlgStatusChangeTrap.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgStatusChangeTrap.setDescription(' The trap will be generated if the reachability status of an DNS-ALG\n        server changes from In-Service to either Timed out or Out of Service.')
apDnsAlgStatusChangeClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 2)).setObjects(("APDNSALG-MIB", "apDNSALGConfigName"), ("APDNSALG-MIB", "apDNSALGServerRealm"), ("APDNSALG-MIB", "apDNSALGServerIpAddress"), ("APDNSALG-MIB", "apDNSALGServerStatus"))
if mibBuilder.loadTexts: apDnsAlgStatusChangeClearTrap.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgStatusChangeClearTrap.setDescription(' The trap will be generated if the reachability status of an DNS-ALG\n        server changes from either Timed out or Out of Service to In-Service')
apDnsAlgConstraintStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 3)).setObjects(("APDNSALG-MIB", "apDNSALGConfigName"), ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
if mibBuilder.loadTexts: apDnsAlgConstraintStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgConstraintStateChangeTrap.setDescription(" The trap will be generated if an DNS-ALG config's constriants state changed \n        from inservice to constraintsExceeded.")
apDnsAlgConstraintStateChangeClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 4)).setObjects(("APDNSALG-MIB", "apDNSALGConfigName"), ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
if mibBuilder.loadTexts: apDnsAlgConstraintStateChangeClearTrap.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgConstraintStateChangeClearTrap.setDescription(" The trap will be generated if an DNS-ALG config's constriants state changed \n        from constraintsExceeded to inservice.")
apDnsAlgSvrConstraintStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 5)).setObjects(("APDNSALG-MIB", "apDNSALGConfigName"), ("APDNSALG-MIB", "apDNSALGServerRealm"), ("APDNSALG-MIB", "apDNSALGServerIpAddress"), ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
if mibBuilder.loadTexts: apDnsAlgSvrConstraintStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgSvrConstraintStateChangeTrap.setDescription(' The trap will be generated if an Dns Server(i.e.IP-Address) constriants state changed \n        from inservice to constraintsExceeded.')
apDnsAlgSvrConstraintStateChangeClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 6)).setObjects(("APDNSALG-MIB", "apDNSALGConfigName"), ("APDNSALG-MIB", "apDNSALGServerRealm"), ("APDNSALG-MIB", "apDNSALGServerIpAddress"), ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
if mibBuilder.loadTexts: apDnsAlgSvrConstraintStateChangeClearTrap.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgSvrConstraintStateChangeClearTrap.setDescription(' The trap will be generated if an Dns Server(i.e.IP-Address) constriants state changed \n        from constraintsExceeded to inservice.')
apDnsAlgServerStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 1, 1)).setObjects(("APDNSALG-MIB", "apDNSALGConfigName"), ("APDNSALG-MIB", "apDNSALGServerRealm"), ("APDNSALG-MIB", "apDNSALGDomainSuffix"), ("APDNSALG-MIB", "apDNSALGServerIpAddress"), ("APDNSALG-MIB", "apDNSALGServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDnsAlgServerStatusGroup = apDnsAlgServerStatusGroup.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerStatusGroup.setDescription('A collection of statistics for DNS-ALG server status.')
apDnsAlgStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 1, 2)).setObjects(("APDNSALG-MIB", "apDnsAlgClientRealmIndex"), ("APDNSALG-MIB", "apDnsAlgClientRealmName"), ("APDNSALG-MIB", "apDnsAlgCurrentQueries"), ("APDNSALG-MIB", "apDnsAlgTotalQueries"), ("APDNSALG-MIB", "apDnsAlgCurrentSucess"), ("APDNSALG-MIB", "apDnsAlgTotalSucess"), ("APDNSALG-MIB", "apDnsAlgCurrentNotFound"), ("APDNSALG-MIB", "apDnsAlgTotalNotFound"), ("APDNSALG-MIB", "apDnsAlgCurrentTimeOut"), ("APDNSALG-MIB", "apDnsAlgTotalTimeOut"), ("APDNSALG-MIB", "apDnsAlgCurrentBadStatus"), ("APDNSALG-MIB", "apDnsAlgTotalBadStatus"), ("APDNSALG-MIB", "apDnsAlgCurrentOtherFailures"), ("APDNSALG-MIB", "apDnsAlgTotalOtherFailures"), ("APDNSALG-MIB", "apDnsAlgAvgLatency"), ("APDNSALG-MIB", "apDnsAlgMaxLatency"), ("APDNSALG-MIB", "apDnsAlgMaxBurstRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDnsAlgStatsGroup = apDnsAlgStatsGroup.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgStatsGroup.setDescription('Report the stats of configured DNSALG config objects.')
apDnsAlgServerRateStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 1, 3)).setObjects(("APDNSALG-MIB", "apDnsAlgServerInetAddressType"), ("APDNSALG-MIB", "apDnsAlgServerInetAddress"), ("APDNSALG-MIB", "apDnsAlgConfigClientRealm"), ("APDNSALG-MIB", "apDnsAlgServerRealm"), ("APDNSALG-MIB", "apDnsAlgServerRateMsgRcvd"), ("APDNSALG-MIB", "apDnsAlgServerRateMsgSent"), ("APDNSALG-MIB", "apDnsAlgServerRateReqRcvd"), ("APDNSALG-MIB", "apDnsAlgServerRateReqSent"), ("APDNSALG-MIB", "apDnsAlgServerRateRspRcvd"), ("APDNSALG-MIB", "apDnsAlgServerRateRspSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDnsAlgServerRateStatsGroup = apDnsAlgServerRateStatsGroup.setStatus('current')
if mibBuilder.loadTexts: apDnsAlgServerRateStatsGroup.setDescription('Report the status of configured DNS servers.')
apDNSALGNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 2, 1)).setObjects(("APDNSALG-MIB", "apDnsAlgStatusChangeTrap"), ("APDNSALG-MIB", "apDnsAlgStatusChangeClearTrap"), ("APDNSALG-MIB", "apDnsAlgConstraintStateChangeTrap"), ("APDNSALG-MIB", "apDnsAlgConstraintStateChangeClearTrap"), ("APDNSALG-MIB", "apDnsAlgSvrConstraintStateChangeTrap"), ("APDNSALG-MIB", "apDnsAlgSvrConstraintStateChangeClearTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotificationsGroup = apDNSALGNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: apDNSALGNotificationsGroup.setDescription('A collection of mib objects accessible only to traps.')
mibBuilder.exportSymbols("APDNSALG-MIB", apDnsAlgStatsGroup=apDnsAlgStatsGroup, apDnsAlgTotalNotFound=apDnsAlgTotalNotFound, apDNSALGNotificationsGroup=apDNSALGNotificationsGroup, apDnsAlgServerRateMsgSent=apDnsAlgServerRateMsgSent, apDNSALGServerStatus=apDNSALGServerStatus, apDNSALGNotificationObjects=apDNSALGNotificationObjects, apDnsAlgClientRealmIndex=apDnsAlgClientRealmIndex, apDnsAlgServerRateMsgRcvd=apDnsAlgServerRateMsgRcvd, apDnsAlgServerRateRspSent=apDnsAlgServerRateRspSent, apDNSALGConformance=apDNSALGConformance, apDnsAlgConstraintStateChangeClearTrap=apDnsAlgConstraintStateChangeClearTrap, apDnsAlgServerInetAddress=apDnsAlgServerInetAddress, apDNSALGModule=apDNSALGModule, apDnsAlgTotalSucess=apDnsAlgTotalSucess, apDNSALGServerIpAddress=apDNSALGServerIpAddress, apDnsAlgConfigEntry=apDnsAlgConfigEntry, apDnsAlgCurrentNotFound=apDnsAlgCurrentNotFound, apDnsAlgServerEntry=apDnsAlgServerEntry, apDnsAlgCurrentBadStatus=apDnsAlgCurrentBadStatus, apDnsAlgCurrentSucess=apDnsAlgCurrentSucess, apDNSALGConfigName=apDNSALGConfigName, apDnsAlgTotalQueries=apDnsAlgTotalQueries, apDnsAlgConfigIndex=apDnsAlgConfigIndex, apDNSALGObjectGroups=apDNSALGObjectGroups, apDnsAlgClientRealmName=apDnsAlgClientRealmName, apDnsAlgCurrentQueries=apDnsAlgCurrentQueries, apDnsAlgServerRealm=apDnsAlgServerRealm, apDnsAlgServerRateReqRcvd=apDnsAlgServerRateReqRcvd, apDnsAlgServerRateStatsTable=apDnsAlgServerRateStatsTable, apDnsAlgServerStatusGroup=apDnsAlgServerStatusGroup, apDnsAlgStatusChangeClearTrap=apDnsAlgStatusChangeClearTrap, apDNSALGServerStatusTable=apDNSALGServerStatusTable, apDnsALGStatsEntry=apDnsALGStatsEntry, apDnsAlgServerTable=apDnsAlgServerTable, apDnsAlgCurrentTimeOut=apDnsAlgCurrentTimeOut, apDnsAlgServerIndex=apDnsAlgServerIndex, apDnsAlgServerRateStatsEntry=apDnsAlgServerRateStatsEntry, apDnsAlgConstraintStateChangeTrap=apDnsAlgConstraintStateChangeTrap, apDnsAlgTotalOtherFailures=apDnsAlgTotalOtherFailures, apDnsAlgAvgLatency=apDnsAlgAvgLatency, apDNSALGDomainSuffix=apDNSALGDomainSuffix, apDNSALGNotifObjects=apDNSALGNotifObjects, apDNSALGMIBGeneralObjects=apDNSALGMIBGeneralObjects, apDNSALGServerRealm=apDNSALGServerRealm, apDNSALGNotifPrefix=apDNSALGNotifPrefix, apDnsAlgSvrConstraintStateChangeClearTrap=apDnsAlgSvrConstraintStateChangeClearTrap, apDNSALGNotificationGroups=apDNSALGNotificationGroups, apDNSALGServerStatusEntry=apDNSALGServerStatusEntry, apDnsAlgMaxBurstRate=apDnsAlgMaxBurstRate, apDnsAlgStatusChangeTrap=apDnsAlgStatusChangeTrap, apDNSALGServerIndex=apDNSALGServerIndex, apDnsAlgTotalTimeOut=apDnsAlgTotalTimeOut, apDnsAlgServerRateRspRcvd=apDnsAlgServerRateRspRcvd, apDnsAlgServerRateStatsGroup=apDnsAlgServerRateStatsGroup, apDnsAlgServerRateReqSent=apDnsAlgServerRateReqSent, apDnsAlgCurrentOtherFailures=apDnsAlgCurrentOtherFailures, apDnsAlgServerInetAddressType=apDnsAlgServerInetAddressType, apDnsAlgConfigClientRealm=apDnsAlgConfigClientRealm, apDNSALGMIBTabularObjects=apDNSALGMIBTabularObjects, PYSNMP_MODULE_ID=apDNSALGModule, apDNSALGMIBObjects=apDNSALGMIBObjects, apDnsAlgTotalBadStatus=apDnsAlgTotalBadStatus, apDnsAlgConfigTable=apDnsAlgConfigTable, apDNSALGConstraintsStatus=apDNSALGConstraintsStatus, apDnsAlgSvrConstraintStateChangeTrap=apDnsAlgSvrConstraintStateChangeTrap, apDNSALGNotifications=apDNSALGNotifications, apDNSALGConfigIndex=apDNSALGConfigIndex, apDNSALGStatsTable=apDNSALGStatsTable, apDnsAlgMaxLatency=apDnsAlgMaxLatency)
