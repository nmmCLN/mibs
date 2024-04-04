#
# PySNMP MIB module MCAFEE-MWG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-MWG-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:20:56 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
mcafeeGATEWAY, = mibBuilder.importSymbols("MCAFEE-SMI", "mcafeeGATEWAY")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Gauge32, Integer32, ObjectIdentity, Bits, Unsigned32, Counter32, IpAddress, iso, mib_2, MibIdentifier, NotificationType, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Gauge32", "Integer32", "ObjectIdentity", "Bits", "Unsigned32", "Counter32", "IpAddress", "iso", "mib-2", "MibIdentifier", "NotificationType", "NotificationType")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
mwg = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230, 2, 7))
mwg.setRevisions(('2014-11-10 00:00', '2014-10-07 00:00', '2013-05-21 00:00', '2011-12-01 00:00', '2011-01-11 00:00', '2010-04-26 00:00', '2010-02-19 00:00', '2009-10-13 00:00',))
if mibBuilder.loadTexts: mwg.setLastUpdated('201411100000Z')
if mibBuilder.loadTexts: mwg.setOrganization('McAfee Inc.')
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
kCompanyName = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: kCompanyName.setStatus('current')
kProductVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: kProductVersion.setStatus('current')
kMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kMajorVersion.setStatus('current')
kMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kMinorVersion.setStatus('current')
kMicroVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kMicroVersion.setStatus('current')
kHotfixVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kHotfixVersion.setStatus('current')
kCustomVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kCustomVersion.setStatus('current')
kRevision = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: kRevision.setStatus('current')
kBuildNumber = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: kBuildNumber.setStatus('current')
mwgEngineVersions = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20))
pAMEngineVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pAMEngineVersion.setStatus('current')
pAMSignatureVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pAMSignatureVersion.setStatus('current')
pMFEEngineVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pMFEEngineVersion.setStatus('current')
pMFEDATVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pMFEDATVersion.setStatus('current')
pAMProactiveVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pAMProactiveVersion.setStatus('current')
pTSDBVersion = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTSDBVersion.setStatus('current')
stBadReputation = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBadReputation.setStatus('obsolete')
stMalwareDetected = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stMalwareDetected.setStatus('current')
stConnectionsLegitimate = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stConnectionsLegitimate.setStatus('current')
stBlockedByAntiMalware = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBlockedByAntiMalware.setStatus('current')
stConnectionsBlocked = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stConnectionsBlocked.setStatus('current')
stBlockedByMediaFilter = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBlockedByMediaFilter.setStatus('current')
stBlockedByURLFilter = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stBlockedByURLFilter.setStatus('current')
stMimeType = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stMimeType.setStatus('current')
stCategories = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCategories.setStatus('current')
stCategoriesTable = MibTable((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10), )
if mibBuilder.loadTexts: stCategoriesTable.setStatus('current')
stCategoriesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1), ).setIndexNames((0, "MCAFEE-MWG-MIB", "stCategoryName"))
if mibBuilder.loadTexts: stCategoriesEntry.setStatus('current')
stCategoryName = MibTableColumn((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCategoryName.setStatus('current')
stCategoryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCategoryCount.setStatus('current')
stHttpRequests = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpRequests.setStatus('current')
stHttpTraffic = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpTraffic.setStatus('current')
stHttpBytesFromClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesFromClient.setStatus('current')
stHttpBytesFromServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesFromServer.setStatus('current')
stHttpBytesToClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesToClient.setStatus('current')
stHttpBytesToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpBytesToServer.setStatus('current')
stHttpsRequests = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsRequests.setStatus('current')
stHttpsTraffic = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsTraffic.setStatus('current')
stHttpsBytesFromClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesFromClient.setStatus('current')
stHttpsBytesFromServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesFromServer.setStatus('current')
stHttpsBytesToClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesToClient.setStatus('current')
stHttpsBytesToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHttpsBytesToServer.setStatus('current')
stFtpTraffic = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpTraffic.setStatus('current')
stFtpBytesFromClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesFromClient.setStatus('current')
stFtpBytesFromServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesFromServer.setStatus('current')
stFtpBytesToClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesToClient.setStatus('current')
stFtpBytesToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFtpBytesToServer.setStatus('current')
stCPULoad = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCPULoad.setStatus('current')
stClientCount = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stClientCount.setStatus('current')
stConnectedSockets = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stConnectedSockets.setStatus('current')
stCPULoadRaw = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCPULoadRaw.setStatus('current')
stCPUIOWait = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stCPUIOWait.setStatus('current')
stResolveHostViaDNS = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stResolveHostViaDNS.setStatus('current')
stTimeConsumedByRuleEngine = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stTimeConsumedByRuleEngine.setStatus('current')
stTimeForTransaction = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stTimeForTransaction.setStatus('current')
stHandleConnectToServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stHandleConnectToServer.setStatus('current')
stFirstSentFirstReceivedClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFirstSentFirstReceivedClient.setStatus('current')
stLastSentLastReceivedClient = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stLastSentLastReceivedClient.setStatus('current')
stFirstSentFirstReceivedServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFirstSentFirstReceivedServer.setStatus('current')
stLastSentLastReceivedServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stLastSentLastReceivedServer.setStatus('current')
stLastSentFirstReceivedServer = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stLastSentFirstReceivedServer.setStatus('current')
stMemConsumed = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stMemConsumed.setStatus('current')
trSystem = NotificationType((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 1)).setObjects(("MCAFEE-MWG-MIB", "notifyOrigin"), ("MCAFEE-MWG-MIB", "notifyOriginName"), ("MCAFEE-MWG-MIB", "notifySeverity"), ("MCAFEE-MWG-MIB", "notifyReason"), ("MCAFEE-MWG-MIB", "notifyReasonString"), ("MCAFEE-MWG-MIB", "notifyAffectedHost"), ("MCAFEE-MWG-MIB", "notifyAdditional"))
if mibBuilder.loadTexts: trSystem.setStatus('current')
trApplication = NotificationType((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 2)).setObjects(("MCAFEE-MWG-MIB", "notifyOrigin"), ("MCAFEE-MWG-MIB", "notifyOriginName"), ("MCAFEE-MWG-MIB", "notifySeverity"), ("MCAFEE-MWG-MIB", "notifyReason"), ("MCAFEE-MWG-MIB", "notifyReasonString"), ("MCAFEE-MWG-MIB", "notifyAffectedHost"), ("MCAFEE-MWG-MIB", "notifyAdditional"))
if mibBuilder.loadTexts: trApplication.setStatus('current')
trUser = NotificationType((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 3)).setObjects(("MCAFEE-MWG-MIB", "notifyReason"), ("MCAFEE-MWG-MIB", "notifyReasonString"), ("MCAFEE-MWG-MIB", "notifyAffectedHost"), ("MCAFEE-MWG-MIB", "notifyAdditional"))
if mibBuilder.loadTexts: trUser.setStatus('current')
mwgTrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10))
notifyOrigin = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyOrigin.setStatus('current')
notifyOriginName = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyOriginName.setStatus('current')
notifySeverity = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifySeverity.setStatus('current')
notifyReason = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyReason.setStatus('current')
notifyReasonString = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyReasonString.setStatus('current')
notifyAffectedHost = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyAffectedHost.setStatus('current')
notifyAdditional = MibScalar((1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notifyAdditional.setStatus('current')
mibBuilder.exportSymbols("MCAFEE-MWG-MIB", pMFEDATVersion=pMFEDATVersion, stHttpsBytesFromClient=stHttpsBytesFromClient, stLastSentFirstReceivedServer=stLastSentFirstReceivedServer, stLastSentLastReceivedServer=stLastSentLastReceivedServer, kBuildNumber=kBuildNumber, trApplication=trApplication, stConnectionsLegitimate=stConnectionsLegitimate, stHttpTraffic=stHttpTraffic, stLastSentLastReceivedClient=stLastSentLastReceivedClient, stCPUIOWait=stCPUIOWait, stBlockedByAntiMalware=stBlockedByAntiMalware, mwgFTP=mwgFTP, stFirstSentFirstReceivedClient=stFirstSentFirstReceivedClient, kCustomVersion=kCustomVersion, mwgHttps=mwgHttps, stHttpsBytesToServer=stHttpsBytesToServer, PYSNMP_MODULE_ID=mwg, stHttpsBytesToClient=stHttpsBytesToClient, notifySeverity=notifySeverity, stBadReputation=stBadReputation, kProductVersion=kProductVersion, stClientCount=stClientCount, stHttpBytesToClient=stHttpBytesToClient, mwgStatistics=mwgStatistics, stCPULoad=stCPULoad, mwg=mwg, stConnectedSockets=stConnectedSockets, stCategoriesEntry=stCategoriesEntry, pTSDBVersion=pTSDBVersion, trSystem=trSystem, kHotfixVersion=kHotfixVersion, stMimeType=stMimeType, pMFEEngineVersion=pMFEEngineVersion, stFtpBytesFromServer=stFtpBytesFromServer, kProductName=kProductName, notifyAffectedHost=notifyAffectedHost, notifyReasonString=notifyReasonString, mwgHttp=mwgHttp, stFtpBytesToClient=stFtpBytesToClient, mwgInfo=mwgInfo, stHttpsBytesFromServer=stHttpsBytesFromServer, pAMEngineVersion=pAMEngineVersion, stConnectionsBlocked=stConnectionsBlocked, kCompanyName=kCompanyName, stHttpBytesFromClient=stHttpBytesFromClient, stCategories=stCategories, mwgContent=mwgContent, stHttpBytesToServer=stHttpBytesToServer, stFtpBytesFromClient=stFtpBytesFromClient, stMemConsumed=stMemConsumed, notifyOriginName=notifyOriginName, stFtpTraffic=stFtpTraffic, stTimeConsumedByRuleEngine=stTimeConsumedByRuleEngine, mwgTrapVariables=mwgTrapVariables, stHttpRequests=stHttpRequests, mwgEngineVersions=mwgEngineVersions, notifyAdditional=notifyAdditional, stFtpBytesToServer=stFtpBytesToServer, stResolveHostViaDNS=stResolveHostViaDNS, stCategoriesTable=stCategoriesTable, notifyReason=notifyReason, notifyOrigin=notifyOrigin, pAMProactiveVersion=pAMProactiveVersion, stCategoryCount=stCategoryCount, stBlockedByMediaFilter=stBlockedByMediaFilter, stMalwareDetected=stMalwareDetected, stHttpsRequests=stHttpsRequests, stBlockedByURLFilter=stBlockedByURLFilter, mwgTraps=mwgTraps, kMajorVersion=kMajorVersion, kMicroVersion=kMicroVersion, trUser=trUser, stTimeForTransaction=stTimeForTransaction, stFirstSentFirstReceivedServer=stFirstSentFirstReceivedServer, pAMSignatureVersion=pAMSignatureVersion, stCategoryName=stCategoryName, stHandleConnectToServer=stHandleConnectToServer, stHttpBytesFromServer=stHttpBytesFromServer, kMinorVersion=kMinorVersion, kRevision=kRevision, stHttpsTraffic=stHttpsTraffic, stCPULoadRaw=stCPULoadRaw, mwgMiscellaneous=mwgMiscellaneous)
