#
# PySNMP MIB module BLUECOAT-SG-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-AUTHENTICATION-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:10:15 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, Integer32, MibIdentifier, Counter32, Unsigned32, NotificationType, IpAddress, ObjectIdentity, iso, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "Integer32", "MibIdentifier", "Counter32", "Unsigned32", "NotificationType", "IpAddress", "ObjectIdentity", "iso", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecoatSGAuthentication = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 15))
bluecoatSGAuthentication.setRevisions(('2014-08-06 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecoatSGAuthentication.setRevisionsDescriptions(('Initial revision of this MIB.',))
if mibBuilder.loadTexts: bluecoatSGAuthentication.setLastUpdated('201408060300Z')
if mibBuilder.loadTexts: bluecoatSGAuthentication.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: bluecoatSGAuthentication.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: bluecoatSGAuthentication.setDescription('The BLUECOAT-SG-AUTHENTICATION-MIB provides authentication information\n                         and statistics for a BlueCoat SG proxy appliance.')
class ToggleState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

schannelStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2))
lsaDomainControllerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3))
schannelServerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4))
authNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 5))
authNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 5, 0))
schannelStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1), )
if mibBuilder.loadTexts: schannelStatsTable.setStatus('current')
if mibBuilder.loadTexts: schannelStatsTable.setDescription('This table lists the various statistics\n                         concerning the schannel.')
schannelStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-AUTHENTICATION-MIB", "schannelStatsIndex"))
if mibBuilder.loadTexts: schannelStatsEntry.setStatus('current')
if mibBuilder.loadTexts: schannelStatsEntry.setDescription('A schannelStats entry describes the\n                         present usage of a schannel.')
schannelStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: schannelStatsIndex.setStatus('current')
if mibBuilder.loadTexts: schannelStatsIndex.setDescription('An arbitrary value which uniquely identifies\n                         a resource.')
domainName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domainName.setStatus('current')
if mibBuilder.loadTexts: domainName.setDescription('The name of the domain.')
domainStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domainStatus.setStatus('current')
if mibBuilder.loadTexts: domainStatus.setDescription('The status of the domain.')
timeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 4), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: timeouts.setStatus('current')
if mibBuilder.loadTexts: timeouts.setDescription('Number of Schannel timeouts.')
transactions = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 5), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: transactions.setStatus('current')
if mibBuilder.loadTexts: transactions.setDescription('Number of Schannel transactions.')
currentWaiters = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 6), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: currentWaiters.setStatus('current')
if mibBuilder.loadTexts: currentWaiters.setDescription('Number of current waiters.')
maxWaiters = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 7), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxWaiters.setStatus('current')
if mibBuilder.loadTexts: maxWaiters.setDescription('Max number of waiters.')
resets = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 8), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: resets.setStatus('current')
if mibBuilder.loadTexts: resets.setDescription('Number of schannel resets.')
lsaDomainControllerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1), )
if mibBuilder.loadTexts: lsaDomainControllerStatsTable.setStatus('current')
if mibBuilder.loadTexts: lsaDomainControllerStatsTable.setDescription('This table lists the various lsa domain controller statistics.')
lsaDomainControllerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-AUTHENTICATION-MIB", "lsaDomainControllerStatsIndex"))
if mibBuilder.loadTexts: lsaDomainControllerStatsEntry.setStatus('current')
if mibBuilder.loadTexts: lsaDomainControllerStatsEntry.setDescription('Describe statistics of Domain controllers.')
lsaDomainControllerStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lsaDomainControllerStatsIndex.setStatus('current')
if mibBuilder.loadTexts: lsaDomainControllerStatsIndex.setDescription('An arbitrary value which uniquely identifies\n                         a resource.')
domainControllerName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domainControllerName.setStatus('current')
if mibBuilder.loadTexts: domainControllerName.setDescription('Name of domain controller.')
address = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: address.setStatus('current')
if mibBuilder.loadTexts: address.setDescription('Adress of Domain Controller.')
siteName = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: siteName.setStatus('current')
if mibBuilder.loadTexts: siteName.setDescription('Site name of domain controller.')
avgLDAPPingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLDAPPingTime.setStatus('current')
if mibBuilder.loadTexts: avgLDAPPingTime.setDescription('Average LDAP ping time in milliseconds.')
lastLDAPPingTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastLDAPPingTime.setStatus('current')
if mibBuilder.loadTexts: lastLDAPPingTime.setDescription('Last LDAP ping time in milliseconds.')
flags = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flags.setStatus('current')
if mibBuilder.loadTexts: flags.setDescription('Domain Controller flags.')
schannelServerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1), )
if mibBuilder.loadTexts: schannelServerStatsTable.setStatus('current')
if mibBuilder.loadTexts: schannelServerStatsTable.setDescription('This table lists the various statistics\n                         concerning the schannel server.')
schannelServerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-AUTHENTICATION-MIB", "schannelServerStatsIndex"))
if mibBuilder.loadTexts: schannelServerStatsEntry.setStatus('current')
if mibBuilder.loadTexts: schannelServerStatsEntry.setDescription('A schannelStats entry describes the\n                         present usage of a schannel server.')
schannelServerStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: schannelServerStatsIndex.setStatus('current')
if mibBuilder.loadTexts: schannelServerStatsIndex.setDescription('An arbitrary value which uniquely identifies\n                         a resource.')
serverName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverName.setStatus('current')
if mibBuilder.loadTexts: serverName.setDescription('The status of the domain.')
connectionsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsInUse.setStatus('current')
if mibBuilder.loadTexts: connectionsInUse.setDescription('Number of connections in use.')
availableConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availableConnections.setStatus('current')
if mibBuilder.loadTexts: availableConnections.setDescription('Number of available connections.')
averageTransactions = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: averageTransactions.setStatus('current')
if mibBuilder.loadTexts: averageTransactions.setDescription('Average transactions per second (last minute).')
authsByDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 6), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast1Minute.setStatus('current')
if mibBuilder.loadTexts: authsByDomainLast1Minute.setDescription('Auths by Domains Last 1 Minute.')
authsByDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 7), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast3Minutes.setStatus('current')
if mibBuilder.loadTexts: authsByDomainLast3Minutes.setDescription('Auths by Domains Last 3 Minutes.')
authsByDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 8), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast5Minutes.setStatus('current')
if mibBuilder.loadTexts: authsByDomainLast5Minutes.setDescription('Auths by Domains Last 5 Minutes.')
authsByDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 9), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast15Minutes.setStatus('current')
if mibBuilder.loadTexts: authsByDomainLast15Minutes.setDescription('Auths by Domains Last 15 Minutes.')
authsByDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 10), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast60Minutes.setStatus('current')
if mibBuilder.loadTexts: authsByDomainLast60Minutes.setDescription('Auths by Domains Last 60 Minutes.')
failedAuthsByDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 11), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast1Minute.setStatus('current')
if mibBuilder.loadTexts: failedAuthsByDomainLast1Minute.setDescription('Failed auths by Domains Last 1 Minute.')
failedAuthsByDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 12), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast3Minutes.setStatus('current')
if mibBuilder.loadTexts: failedAuthsByDomainLast3Minutes.setDescription('Failed auths by Domains Last 3 Minutes.')
failedAuthsByDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 13), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast5Minutes.setStatus('current')
if mibBuilder.loadTexts: failedAuthsByDomainLast5Minutes.setDescription('Failed auths by Domains Last 5 Minutes.')
failedAuthsByDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 14), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast15Minutes.setStatus('current')
if mibBuilder.loadTexts: failedAuthsByDomainLast15Minutes.setDescription('Failed auths by Domains Last 15 Minutes.')
failedAuthsByDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 15), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast60Minutes.setStatus('current')
if mibBuilder.loadTexts: failedAuthsByDomainLast60Minutes.setDescription('Failed auths by Domains Last 60 Minutes.')
avgLatencyPerDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 16), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast1Minute.setStatus('current')
if mibBuilder.loadTexts: avgLatencyPerDomainLast1Minute.setDescription('Average Latency Per Domains Last 1 Minute.')
avgLatencyPerDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 17), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast3Minutes.setStatus('current')
if mibBuilder.loadTexts: avgLatencyPerDomainLast3Minutes.setDescription('Average Latency Per Domain Last 3 Minutes.')
avgLatencyPerDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 18), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast5Minutes.setStatus('current')
if mibBuilder.loadTexts: avgLatencyPerDomainLast5Minutes.setDescription('Average Latency Per Last 5 Minutes.')
avgLatencyPerDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 19), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast15Minutes.setStatus('current')
if mibBuilder.loadTexts: avgLatencyPerDomainLast15Minutes.setDescription('Average Latency Per Domain Last 15 Minutes.')
avgLatencyPerDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 20), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast60Minutes.setStatus('current')
if mibBuilder.loadTexts: avgLatencyPerDomainLast60Minutes.setDescription('Average Latency Per Domain Last 60 Minutes.')
maxLatencyPerDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 21), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast1Minute.setStatus('current')
if mibBuilder.loadTexts: maxLatencyPerDomainLast1Minute.setDescription('Max Latency Per Domain Last 1 Minute.')
maxLatencyPerDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 22), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast3Minutes.setStatus('current')
if mibBuilder.loadTexts: maxLatencyPerDomainLast3Minutes.setDescription('Max Latency Per Domains Last 3 Minutes.')
maxLatencyPerDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 23), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast5Minutes.setStatus('current')
if mibBuilder.loadTexts: maxLatencyPerDomainLast5Minutes.setDescription('Max Latency Per Domains Last 5 Minutes.')
maxLatencyPerDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 24), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast15Minutes.setStatus('current')
if mibBuilder.loadTexts: maxLatencyPerDomainLast15Minutes.setDescription('Max Latency Per Domains Last 15 Minutes.')
maxLatencyPerDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 25), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast60Minutes.setStatus('current')
if mibBuilder.loadTexts: maxLatencyPerDomainLast60Minutes.setDescription('Max Latency Per Domains Last 60 Minutes.')
minLatencyPerDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 26), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast1Minute.setStatus('current')
if mibBuilder.loadTexts: minLatencyPerDomainLast1Minute.setDescription('Min Latency Per Domains Last 1 Minute.')
minLatencyPerDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 27), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast3Minutes.setStatus('current')
if mibBuilder.loadTexts: minLatencyPerDomainLast3Minutes.setDescription('Min Latency Per Domains Last 3 Minutes.')
minLatencyPerDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 28), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast5Minutes.setStatus('current')
if mibBuilder.loadTexts: minLatencyPerDomainLast5Minutes.setDescription('Min Latency Per Domains Last 5 Minutes.')
minLatencyPerDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 29), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast15Minutes.setStatus('current')
if mibBuilder.loadTexts: minLatencyPerDomainLast15Minutes.setDescription('Min Latency Per Domains Last 15 Minutes.')
minLatencyPerDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 30), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast60Minutes.setStatus('current')
if mibBuilder.loadTexts: minLatencyPerDomainLast60Minutes.setDescription('Min Latency Per Domains Last 60 Minutes.')
schannelLatencyTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 15, 5, 0, 1)).setObjects(("BLUECOAT-SG-AUTHENTICATION-MIB", "domainName"), ("BLUECOAT-SG-AUTHENTICATION-MIB", "latencyType"), ("BLUECOAT-SG-AUTHENTICATION-MIB", "latencyValue"))
if mibBuilder.loadTexts: schannelLatencyTrap.setStatus('current')
if mibBuilder.loadTexts: schannelLatencyTrap.setDescription('The domain that warrants a notification.')
mibBuilder.exportSymbols("BLUECOAT-SG-AUTHENTICATION-MIB", siteName=siteName, address=address, domainName=domainName, schannelStatsEntry=schannelStatsEntry, schannelServerStatsIndex=schannelServerStatsIndex, failedAuthsByDomainLast60Minutes=failedAuthsByDomainLast60Minutes, avgLatencyPerDomainLast60Minutes=avgLatencyPerDomainLast60Minutes, failedAuthsByDomainLast1Minute=failedAuthsByDomainLast1Minute, maxLatencyPerDomainLast5Minutes=maxLatencyPerDomainLast5Minutes, maxLatencyPerDomainLast60Minutes=maxLatencyPerDomainLast60Minutes, failedAuthsByDomainLast15Minutes=failedAuthsByDomainLast15Minutes, maxLatencyPerDomainLast3Minutes=maxLatencyPerDomainLast3Minutes, minLatencyPerDomainLast5Minutes=minLatencyPerDomainLast5Minutes, authNotificationsPrefix=authNotificationsPrefix, schannelStatsIndex=schannelStatsIndex, transactions=transactions, avgLDAPPingTime=avgLDAPPingTime, maxLatencyPerDomainLast15Minutes=maxLatencyPerDomainLast15Minutes, avgLatencyPerDomainLast1Minute=avgLatencyPerDomainLast1Minute, maxLatencyPerDomainLast1Minute=maxLatencyPerDomainLast1Minute, connectionsInUse=connectionsInUse, schannelLatencyTrap=schannelLatencyTrap, avgLatencyPerDomainLast3Minutes=avgLatencyPerDomainLast3Minutes, minLatencyPerDomainLast15Minutes=minLatencyPerDomainLast15Minutes, schannelStatsTable=schannelStatsTable, authsByDomainLast15Minutes=authsByDomainLast15Minutes, bluecoatSGAuthentication=bluecoatSGAuthentication, lsaDomainControllerStatsEntry=lsaDomainControllerStatsEntry, authsByDomainLast3Minutes=authsByDomainLast3Minutes, authsByDomainLast60Minutes=authsByDomainLast60Minutes, avgLatencyPerDomainLast5Minutes=avgLatencyPerDomainLast5Minutes, avgLatencyPerDomainLast15Minutes=avgLatencyPerDomainLast15Minutes, averageTransactions=averageTransactions, minLatencyPerDomainLast3Minutes=minLatencyPerDomainLast3Minutes, schannelStats=schannelStats, authNotifications=authNotifications, lsaDomainControllerStatsIndex=lsaDomainControllerStatsIndex, PYSNMP_MODULE_ID=bluecoatSGAuthentication, flags=flags, failedAuthsByDomainLast3Minutes=failedAuthsByDomainLast3Minutes, authsByDomainLast1Minute=authsByDomainLast1Minute, timeouts=timeouts, serverName=serverName, lsaDomainControllerStatsTable=lsaDomainControllerStatsTable, authsByDomainLast5Minutes=authsByDomainLast5Minutes, schannelServerStatsTable=schannelServerStatsTable, failedAuthsByDomainLast5Minutes=failedAuthsByDomainLast5Minutes, minLatencyPerDomainLast60Minutes=minLatencyPerDomainLast60Minutes, schannelServerStats=schannelServerStats, lsaDomainControllerStats=lsaDomainControllerStats, resets=resets, availableConnections=availableConnections, minLatencyPerDomainLast1Minute=minLatencyPerDomainLast1Minute, currentWaiters=currentWaiters, maxWaiters=maxWaiters, domainStatus=domainStatus, lastLDAPPingTime=lastLDAPPingTime, schannelServerStatsEntry=schannelServerStatsEntry, ToggleState=ToggleState, domainControllerName=domainControllerName)
