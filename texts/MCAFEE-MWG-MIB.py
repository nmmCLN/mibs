#
# PySNMP MIB module MCAFEE-MWG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-MWG-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:20:57 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
mcafeeGATEWAY, = mibBuilder.importSymbols("MCAFEE-SMI", "mcafeeGATEWAY")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, enterprises, Unsigned32, Counter32, NotificationType, ModuleIdentity, Counter64, mib_2, Gauge32, TimeTicks, MibIdentifier, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "Unsigned32", "Counter32", "NotificationType", "ModuleIdentity", "Counter64", "mib-2", "Gauge32", "TimeTicks", "MibIdentifier", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
mwg = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230, 2, 7))
mwg.setRevisions(('2014-11-10 00:00', '2014-10-07 00:00', '2013-05-21 00:00', '2011-12-01 00:00', '2011-01-11 00:00', '2010-04-26 00:00', '2010-02-19 00:00', '2009-10-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mwg.setRevisionsDescriptions(('Add memory consumption value', 'Fix trap notification enums', 'Add values for performance measurement', 'Mark stBadReputation as obsolete', 'Add some more statistical values and descriptions', 'Add build number to version information', 'Minor RFC related compatiblility changes in the mib', 'Initial version',))
if mibBuilder.loadTexts: mwg.setLastUpdated('201411100000Z')
if mibBuilder.loadTexts: mwg.setOrganization('McAfee Inc.')
if mibBuilder.loadTexts: mwg.setContactInfo('email: support@mcafee.com')
if mibBuilder.loadTexts: mwg.setDescription('McAfee Web Gateway 7.5 MIB definitions')
mwgInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1))
mwgStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2))
mwgTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4))
mwgContent = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1))
mwgHttp = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2))
mwgHttps = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3))
mwgFTP = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4))
mwgMiscellaneous = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5))
kProductName = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kProductName.setStatus('current')
if mibBuilder.loadTexts: kProductName.setDescription('Product name')
kCompanyName = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: kCompanyName.setStatus('current')
if mibBuilder.loadTexts: kCompanyName.setDescription('Company holding the copyright on this product')
kProductVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: kProductVersion.setStatus('current')
if mibBuilder.loadTexts: kProductVersion.setDescription('String representation of the product version')
kMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kMajorVersion.setStatus('current')
if mibBuilder.loadTexts: kMajorVersion.setDescription('Major version number')
kMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kMinorVersion.setStatus('current')
if mibBuilder.loadTexts: kMinorVersion.setDescription('Minor version number')
kMicroVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kMicroVersion.setStatus('current')
if mibBuilder.loadTexts: kMicroVersion.setDescription('Micro version number')
kHotfixVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kHotfixVersion.setStatus('current')
if mibBuilder.loadTexts: kHotfixVersion.setDescription('Hotfix version number')
kCustomVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kCustomVersion.setStatus('current')
if mibBuilder.loadTexts: kCustomVersion.setDescription('Custom  version number')
kRevision = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: kRevision.setStatus('current')
if mibBuilder.loadTexts: kRevision.setDescription('SVN revision number')
kBuildNumber = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kBuildNumber.setStatus('current')
if mibBuilder.loadTexts: kBuildNumber.setDescription('BUILD number')
mwgEngineVersions = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20))
pAMEngineVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pAMEngineVersion.setStatus('current')
if mibBuilder.loadTexts: pAMEngineVersion.setDescription('Version of the McAfee Anti-Malware Engine for Gateway')
pAMSignatureVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pAMSignatureVersion.setStatus('current')
if mibBuilder.loadTexts: pAMSignatureVersion.setDescription('Version of the McAfee Anti-Malware Signature File (obsolete)')
pMFEEngineVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pMFEEngineVersion.setStatus('current')
if mibBuilder.loadTexts: pMFEEngineVersion.setDescription('Version of the McAfee Anti-Malware Engine')
pMFEDATVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pMFEDATVersion.setStatus('current')
if mibBuilder.loadTexts: pMFEDATVersion.setDescription('Version of the McAfee DATs')
pAMProactiveVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pAMProactiveVersion.setStatus('current')
if mibBuilder.loadTexts: pAMProactiveVersion.setDescription('Version of the ProActive database')
pTSDBVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTSDBVersion.setStatus('current')
if mibBuilder.loadTexts: pTSDBVersion.setDescription('Version of McAfee TrustedSource')
stBadReputation = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBadReputation.setStatus('obsolete')
if mibBuilder.loadTexts: stBadReputation.setDescription('This statistic value is obsolete and should no longer be used')
stMalwareDetected = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stMalwareDetected.setStatus('current')
if mibBuilder.loadTexts: stMalwareDetected.setDescription('Number of infections detected by the McAfee Gateway Antimalware Engine')
stConnectionsLegitimate = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stConnectionsLegitimate.setStatus('current')
if mibBuilder.loadTexts: stConnectionsLegitimate.setDescription('Number of connections that not have been blocked')
stBlockedByAntiMalware = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBlockedByAntiMalware.setStatus('current')
if mibBuilder.loadTexts: stBlockedByAntiMalware.setDescription('Number of connections blocked by Anti-Malware')
stConnectionsBlocked = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stConnectionsBlocked.setStatus('current')
if mibBuilder.loadTexts: stConnectionsBlocked.setDescription('Number of blocked connections')
stBlockedByMediaFilter = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBlockedByMediaFilter.setStatus('current')
if mibBuilder.loadTexts: stBlockedByMediaFilter.setDescription('Number of connections that have been blocked by the Media-Type filter')
stBlockedByURLFilter = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBlockedByURLFilter.setStatus('current')
if mibBuilder.loadTexts: stBlockedByURLFilter.setDescription('Number of connection that have been blocked by the URL filter')
stMimeType = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stMimeType.setStatus('current')
if mibBuilder.loadTexts: stMimeType.setDescription('Number of media types detected by the Media Type filter')
stCategories = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCategories.setStatus('current')
if mibBuilder.loadTexts: stCategories.setDescription('Number of categories detected by the URL filter')
stCategoriesTable = MibTable((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10), )
if mibBuilder.loadTexts: stCategoriesTable.setStatus('current')
if mibBuilder.loadTexts: stCategoriesTable.setDescription('A table containing the categories detected by the URL filter')
stCategoriesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1), ).setIndexNames((0, "MCAFEE-MWG-MIB", "stCategoryName"))
if mibBuilder.loadTexts: stCategoriesEntry.setStatus('current')
if mibBuilder.loadTexts: stCategoriesEntry.setDescription('An entry containing information about a categorys name and counter.')
stCategoryName = MibTableColumn((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCategoryName.setStatus('current')
if mibBuilder.loadTexts: stCategoryName.setDescription('Name of the category')
stCategoryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCategoryCount.setStatus('current')
if mibBuilder.loadTexts: stCategoryCount.setDescription('Number of times the URL filter detected this category')
stHttpRequests = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpRequests.setStatus('current')
if mibBuilder.loadTexts: stHttpRequests.setDescription('Number of HTTP requests')
stHttpTraffic = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpTraffic.setStatus('current')
if mibBuilder.loadTexts: stHttpTraffic.setDescription('Number of bytes tranferred between proxy and server(s) using the HTTP protocol')
stHttpBytesFromClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesFromClient.setStatus('current')
if mibBuilder.loadTexts: stHttpBytesFromClient.setDescription('Number of bytes transferred from client to proxy using the HTTP protocol')
stHttpBytesFromServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesFromServer.setStatus('current')
if mibBuilder.loadTexts: stHttpBytesFromServer.setDescription('Number of bytes transferred from server to proxy using the HTTP protocol')
stHttpBytesToClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesToClient.setStatus('current')
if mibBuilder.loadTexts: stHttpBytesToClient.setDescription('Number of bytes transferred from proxy to client(s) using the HTTP protocol')
stHttpBytesToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesToServer.setStatus('current')
if mibBuilder.loadTexts: stHttpBytesToServer.setDescription('Number of bytes transferred from proxy to server(s) using the HTTP protocol')
stHttpsRequests = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsRequests.setStatus('current')
if mibBuilder.loadTexts: stHttpsRequests.setDescription('Number of HTTPS requests')
stHttpsTraffic = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsTraffic.setStatus('current')
if mibBuilder.loadTexts: stHttpsTraffic.setDescription('Number of bytes tranferred between proxy and server(s) using the HTTPS protocol')
stHttpsBytesFromClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesFromClient.setStatus('current')
if mibBuilder.loadTexts: stHttpsBytesFromClient.setDescription('Number of bytes tranferred from client(s) to proxy using the HTTPS protocol')
stHttpsBytesFromServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesFromServer.setStatus('current')
if mibBuilder.loadTexts: stHttpsBytesFromServer.setDescription('Number of bytes tranferred from server(s) to proxy using the HTTPS protocol')
stHttpsBytesToClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesToClient.setStatus('current')
if mibBuilder.loadTexts: stHttpsBytesToClient.setDescription('Number of bytes tranferred from proxy to client(s) and proxy using the HTTPS protocol')
stHttpsBytesToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesToServer.setStatus('current')
if mibBuilder.loadTexts: stHttpsBytesToServer.setDescription('Number of bytes tranferred from proxy to server(s) and proxy using the HTTPS protocol')
stFtpTraffic = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpTraffic.setStatus('current')
if mibBuilder.loadTexts: stFtpTraffic.setDescription('Number of bytes transmitted between proxy and server(s) using the FTP protocol')
stFtpBytesFromClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesFromClient.setStatus('current')
if mibBuilder.loadTexts: stFtpBytesFromClient.setDescription('Number of bytes tranferred from proxy to client(s) using the FTP protocol')
stFtpBytesFromServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesFromServer.setStatus('current')
if mibBuilder.loadTexts: stFtpBytesFromServer.setDescription('Number of bytes tranferred from server(s) to proxy using the FTP protocol')
stFtpBytesToClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesToClient.setStatus('current')
if mibBuilder.loadTexts: stFtpBytesToClient.setDescription('Number of bytes tranferred from proxy to client(s) using the FTP protocol')
stFtpBytesToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesToServer.setStatus('current')
if mibBuilder.loadTexts: stFtpBytesToServer.setDescription('Number of bytes tranferred from proxy to server(s) using the FTP protocol')
stCPULoad = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCPULoad.setStatus('current')
if mibBuilder.loadTexts: stCPULoad.setDescription('Current overall CPU usage in percent')
stClientCount = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stClientCount.setStatus('current')
if mibBuilder.loadTexts: stClientCount.setDescription('Currently connected clients')
stConnectedSockets = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stConnectedSockets.setStatus('current')
if mibBuilder.loadTexts: stConnectedSockets.setDescription('Number of open network sockets in use by the proxy')
stCPULoadRaw = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCPULoadRaw.setStatus('current')
if mibBuilder.loadTexts: stCPULoadRaw.setDescription('Load value 1 minute average')
stCPUIOWait = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCPUIOWait.setStatus('current')
if mibBuilder.loadTexts: stCPUIOWait.setDescription('I/O wait value in percent')
stResolveHostViaDNS = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stResolveHostViaDNS.setStatus('current')
if mibBuilder.loadTexts: stResolveHostViaDNS.setDescription('Time to resolve DNS in ms')
stTimeConsumedByRuleEngine = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stTimeConsumedByRuleEngine.setStatus('current')
if mibBuilder.loadTexts: stTimeConsumedByRuleEngine.setDescription('Average time used by the rule engine in ms')
stTimeForTransaction = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stTimeForTransaction.setStatus('current')
if mibBuilder.loadTexts: stTimeForTransaction.setDescription('Average time for transaction in ms')
stHandleConnectToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHandleConnectToServer.setStatus('current')
if mibBuilder.loadTexts: stHandleConnectToServer.setDescription('Connect to Server')
stFirstSentFirstReceivedClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFirstSentFirstReceivedClient.setStatus('current')
if mibBuilder.loadTexts: stFirstSentFirstReceivedClient.setDescription('First byte received from client until first byte sent back')
stLastSentLastReceivedClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stLastSentLastReceivedClient.setStatus('current')
if mibBuilder.loadTexts: stLastSentLastReceivedClient.setDescription('Last byte received from client until last byte sent back')
stFirstSentFirstReceivedServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFirstSentFirstReceivedServer.setStatus('current')
if mibBuilder.loadTexts: stFirstSentFirstReceivedServer.setDescription('First byte sent to server until first byte received')
stLastSentLastReceivedServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stLastSentLastReceivedServer.setStatus('current')
if mibBuilder.loadTexts: stLastSentLastReceivedServer.setDescription('Last byte sent to server until last byte received')
stLastSentFirstReceivedServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stLastSentFirstReceivedServer.setStatus('current')
if mibBuilder.loadTexts: stLastSentFirstReceivedServer.setDescription('Last byte sent to server until first byte received')
stMemConsumed = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stMemConsumed.setStatus('current')
if mibBuilder.loadTexts: stMemConsumed.setDescription('Virtual memory consumption of the main processes divided by RAM + half of SWAP space. Projected to 0-100.')
trSystem = NotificationType((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 1)).setObjects(("MCAFEE-MWG-MIB", "notifyOrigin"), ("MCAFEE-MWG-MIB", "notifyOriginName"), ("MCAFEE-MWG-MIB", "notifySeverity"), ("MCAFEE-MWG-MIB", "notifyReason"), ("MCAFEE-MWG-MIB", "notifyReasonString"), ("MCAFEE-MWG-MIB", "notifyAffectedHost"), ("MCAFEE-MWG-MIB", "notifyAdditional"))
if mibBuilder.loadTexts: trSystem.setStatus('current')
if mibBuilder.loadTexts: trSystem.setDescription('Traps that are generated by a system event')
trApplication = NotificationType((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 2)).setObjects(("MCAFEE-MWG-MIB", "notifyOrigin"), ("MCAFEE-MWG-MIB", "notifyOriginName"), ("MCAFEE-MWG-MIB", "notifySeverity"), ("MCAFEE-MWG-MIB", "notifyReason"), ("MCAFEE-MWG-MIB", "notifyReasonString"), ("MCAFEE-MWG-MIB", "notifyAffectedHost"), ("MCAFEE-MWG-MIB", "notifyAdditional"))
if mibBuilder.loadTexts: trApplication.setStatus('current')
if mibBuilder.loadTexts: trApplication.setDescription('Traps that are generated by an application system event')
trUser = NotificationType((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 3)).setObjects(("MCAFEE-MWG-MIB", "notifyReason"), ("MCAFEE-MWG-MIB", "notifyReasonString"), ("MCAFEE-MWG-MIB", "notifyAffectedHost"), ("MCAFEE-MWG-MIB", "notifyAdditional"))
if mibBuilder.loadTexts: trUser.setStatus('current')
if mibBuilder.loadTexts: trUser.setDescription('User defined trap that indicates an event connected to a client IP')
mwgTrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10))
notifyOrigin = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyOrigin.setStatus('current')
if mibBuilder.loadTexts: notifyOrigin.setDescription('Origin from where the notification has been send')
notifyOriginName = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyOriginName.setStatus('current')
if mibBuilder.loadTexts: notifyOriginName.setDescription('Name of the origin of the trap')
notifySeverity = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifySeverity.setStatus('current')
if mibBuilder.loadTexts: notifySeverity.setDescription('Severity of this notification')
notifyReason = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyReason.setStatus('current')
if mibBuilder.loadTexts: notifyReason.setDescription('Code to identify the notification')
notifyReasonString = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyReasonString.setStatus('current')
if mibBuilder.loadTexts: notifyReasonString.setDescription('Human readable string for the notification')
notifyAffectedHost = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyAffectedHost.setStatus('current')
if mibBuilder.loadTexts: notifyAffectedHost.setDescription('Additional information if a remote host was involved in this message')
notifyAdditional = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyAdditional.setStatus('current')
if mibBuilder.loadTexts: notifyAdditional.setDescription('Additional information string')
mibBuilder.exportSymbols("MCAFEE-MWG-MIB", stHttpsRequests=stHttpsRequests, trSystem=trSystem, notifyAdditional=notifyAdditional, stHttpsBytesToServer=stHttpsBytesToServer, stMalwareDetected=stMalwareDetected, stBadReputation=stBadReputation, stBlockedByMediaFilter=stBlockedByMediaFilter, mwgTraps=mwgTraps, stCategoriesEntry=stCategoriesEntry, kProductVersion=kProductVersion, stFtpBytesToServer=stFtpBytesToServer, notifyAffectedHost=notifyAffectedHost, stHttpBytesToClient=stHttpBytesToClient, stBlockedByAntiMalware=stBlockedByAntiMalware, kCompanyName=kCompanyName, kMajorVersion=kMajorVersion, mwgInfo=mwgInfo, stClientCount=stClientCount, pTSDBVersion=pTSDBVersion, notifyOrigin=notifyOrigin, stHttpsBytesFromServer=stHttpsBytesFromServer, stFirstSentFirstReceivedServer=stFirstSentFirstReceivedServer, mwgContent=mwgContent, kRevision=kRevision, stCategoryCount=stCategoryCount, stCPULoad=stCPULoad, notifyReasonString=notifyReasonString, stHttpsTraffic=stHttpsTraffic, stMimeType=stMimeType, stFtpBytesFromServer=stFtpBytesFromServer, stCPULoadRaw=stCPULoadRaw, kMinorVersion=kMinorVersion, kCustomVersion=kCustomVersion, mwgStatistics=mwgStatistics, pMFEDATVersion=pMFEDATVersion, stHttpRequests=stHttpRequests, stFtpTraffic=stFtpTraffic, stHttpBytesFromServer=stHttpBytesFromServer, notifyOriginName=notifyOriginName, stFtpBytesToClient=stFtpBytesToClient, mwgMiscellaneous=mwgMiscellaneous, stHandleConnectToServer=stHandleConnectToServer, pMFEEngineVersion=pMFEEngineVersion, stConnectionsBlocked=stConnectionsBlocked, mwgHttps=mwgHttps, stHttpsBytesFromClient=stHttpsBytesFromClient, stLastSentFirstReceivedServer=stLastSentFirstReceivedServer, stConnectionsLegitimate=stConnectionsLegitimate, stMemConsumed=stMemConsumed, stCategories=stCategories, kMicroVersion=kMicroVersion, stTimeConsumedByRuleEngine=stTimeConsumedByRuleEngine, stTimeForTransaction=stTimeForTransaction, trUser=trUser, stHttpTraffic=stHttpTraffic, notifyReason=notifyReason, mwg=mwg, pAMSignatureVersion=pAMSignatureVersion, stFtpBytesFromClient=stFtpBytesFromClient, trApplication=trApplication, stCategoriesTable=stCategoriesTable, kProductName=kProductName, mwgTrapVariables=mwgTrapVariables, stCPUIOWait=stCPUIOWait, pAMProactiveVersion=pAMProactiveVersion, stHttpBytesToServer=stHttpBytesToServer, stLastSentLastReceivedClient=stLastSentLastReceivedClient, stFirstSentFirstReceivedClient=stFirstSentFirstReceivedClient, stHttpBytesFromClient=stHttpBytesFromClient, mwgEngineVersions=mwgEngineVersions, stHttpsBytesToClient=stHttpsBytesToClient, notifySeverity=notifySeverity, kHotfixVersion=kHotfixVersion, stConnectedSockets=stConnectedSockets, kBuildNumber=kBuildNumber, PYSNMP_MODULE_ID=mwg, stBlockedByURLFilter=stBlockedByURLFilter, stLastSentLastReceivedServer=stLastSentLastReceivedServer, stCategoryName=stCategoryName, stResolveHostViaDNS=stResolveHostViaDNS, mwgHttp=mwgHttp, pAMEngineVersion=pAMEngineVersion, mwgFTP=mwgFTP)
