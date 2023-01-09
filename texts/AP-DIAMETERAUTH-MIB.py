#
# PySNMP MIB module AP-DIAMETERAUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/AP-DIAMETERAUTH-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:23 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ApTransportType, = mibBuilder.importSymbols("ACMEPACKET-TC", "ApTransportType")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, IpAddress, TimeTicks, NotificationType, Counter32, Unsigned32, Bits, MibIdentifier, ModuleIdentity, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "TimeTicks", "NotificationType", "Counter32", "Unsigned32", "Bits", "MibIdentifier", "ModuleIdentity", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
apDiameterAuthServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 20))
apDiameterAuthServerModule.setRevisions(('2017-01-19 00:00', '2017-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apDiameterAuthServerModule.setRevisionsDescriptions(('Updated Organization and Contact info.', 'Included mib objects related to traps.',))
if mibBuilder.loadTexts: apDiameterAuthServerModule.setLastUpdated('201702090000Z')
if mibBuilder.loadTexts: apDiameterAuthServerModule.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apDiameterAuthServerModule.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apDiameterAuthServerModule.setDescription('The Net-Net Diameter Authentication MIB for Oracle Communications Acme Packet MSG')
apDiamAuthServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1))
apDiamAuthStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1), )
if mibBuilder.loadTexts: apDiamAuthStatsTable.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthStatsTable.setDescription('The table of authentication statistics per diameter authentication server.')
apDiamAuthStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1), ).setIndexNames((0, "AP-DIAMETERAUTH-MIB", "apDiamAuthInterfaceType"), (0, "AP-DIAMETERAUTH-MIB", "apDiamAuthServerAddress"))
if mibBuilder.loadTexts: apDiamAuthStatsEntry.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthStatsEntry.setDescription('A table entry designed to hold authentication statistics per server.')
apDiamAuthInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthInterfaceType.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthInterfaceType.setDescription('IPAddress type of the diameter authentication server')
apDiamAuthServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthServerAddress.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthServerAddress.setDescription('IPAddress of the diameter authentication server')
apDiamAuthCapExchReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthCapExchReqSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthCapExchReqSent.setDescription('The count of diameter capability exchange messages sent.')
apDiamAuthCapExchReqTimedout = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthCapExchReqTimedout.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthCapExchReqTimedout.setDescription('The count of diameter capability exchange request messages timedout.')
apDiamAuthCapExchAnsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthCapExchAnsRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthCapExchAnsRcvd.setDescription('The count of diameter capability exchange answer messages received.')
apDiamAuthCapExchReqRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthCapExchReqRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthCapExchReqRcvd.setDescription('The count of diameter capability exchange request messages received.')
apDiamAuthCapExchAnsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthCapExchAnsSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthCapExchAnsSent.setDescription('The count of diameter capability exchange answer messages sent.')
apDiamAuthDWDReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDWDReqSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDWDReqSent.setDescription('The count of diameter device watch dog request messages sent.')
apDiamAuthDWDReqTimedout = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDWDReqTimedout.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDWDReqTimedout.setDescription('The count of diameter device watch dog request messages timedout.')
apDiamAuthDWDAnsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDWDAnsRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDWDAnsRcvd.setDescription('The count of diameter device watch dog answer messages received.')
apDiamAuthDWDReqRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDWDReqRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDWDReqRcvd.setDescription('The count of diameter device watch dog request messages received.')
apDiamAuthDWDAnsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDWDAnsSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDWDAnsSent.setDescription('The count of diameter device watch dog answer messages sent.')
apDiamAuthDisconPeerReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDisconPeerReqSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDisconPeerReqSent.setDescription('The count of diameter disconnect-peer request messages sent.')
apDiamAuthDisconPeerReqTimedout = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDisconPeerReqTimedout.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDisconPeerReqTimedout.setDescription('The count of diameter disconnect-peer request messages timedout.')
apDiamAuthDisconPeerAnsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDisconPeerAnsRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDisconPeerAnsRcvd.setDescription('The count of diameter disconnect-peer answer messages received.')
apDiamAuthDisconPeerReqRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDisconPeerReqRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDisconPeerReqRcvd.setDescription('The count of diameter disconnect-peer request messages received.')
apDiamAuthDisconPeerAnsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthDisconPeerAnsSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthDisconPeerAnsSent.setDescription('The count of diameter disconnect-peer answer messages sent.')
apDiamAuthSessTermReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthSessTermReqSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthSessTermReqSent.setDescription('The count of diameter session termination request messages sent.')
apDiamAuthSessTermReqTimedout = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthSessTermReqTimedout.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthSessTermReqTimedout.setDescription('The count of diameter session termination request messages timedout.')
apDiamAuthSessTermAnsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthSessTermAnsRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthSessTermAnsRcvd.setDescription('The count of diameter session termination answer messages received.')
apDiamAuthAbortSessReqRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthAbortSessReqRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthAbortSessReqRcvd.setDescription('The count of diameter abort session request messages received.')
apDiamAuthAbortSessAnsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthAbortSessAnsSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthAbortSessAnsSent.setDescription('The count of diameter abort session answer messages sent.')
apDiamAuthEapReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthEapReqSent.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthEapReqSent.setDescription('The count of diameter eap request messages sent.')
apDiamAuthEapReqTimedout = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthEapReqTimedout.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthEapReqTimedout.setDescription('The count of diameter eap request messages timedout.')
apDiamAuthEapAnsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthEapAnsRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthEapAnsRcvd.setDescription('The count of diameter eap answer messages received.')
apDiamAuthEapAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthEapAccepts.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthEapAccepts.setDescription('The count of  eap accept messages recived.')
apDiamAuthEapRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthEapRejects.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthEapRejects.setDescription('The count of eap reject messages received.')
apDiamAuthActiveSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthActiveSessions.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthActiveSessions.setDescription('The number of active sessions on this server')
apDiamAuthServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("initial", 0), ("tcpConInProgress", 1), ("tcpConnComplete", 2), ("capexInProgress", 3), ("inService", 4), ("outOfService", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthServerStatus.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthServerStatus.setDescription('The current state of the the diameter authentication server')
apDiamAuthErrorStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2), )
if mibBuilder.loadTexts: apDiamAuthErrorStatsTable.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthErrorStatsTable.setDescription('The table of diameter authentication error statistics per diameter authentication server.')
apDiamAuthErrorStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1), )
apDiamAuthStatsEntry.registerAugmentions(("AP-DIAMETERAUTH-MIB", "apDiamAuthErrorStatsEntry"))
apDiamAuthErrorStatsEntry.setIndexNames(*apDiamAuthStatsEntry.getIndexNames())
if mibBuilder.loadTexts: apDiamAuthErrorStatsEntry.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthErrorStatsEntry.setDescription('A table entry designed to hold error authentication statistics per server.')
apDiamAuthUnknownVersionRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthUnknownVersionRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthUnknownVersionRcvd.setDescription('The count of diameter unknown version messages received.')
apDiamAuthUnknownExchRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthUnknownExchRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthUnknownExchRcvd.setDescription('The count of diameter unknown exchange messages received.')
apDiamAuthNoCommonAppRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthNoCommonAppRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthNoCommonAppRcvd.setDescription('The count of diameter No common application messages received.')
apDiamAuthAppUnsuppRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthAppUnsuppRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthAppUnsuppRcvd.setDescription('The count of diameter application unsupported messages received.')
apDiamAuthCommandUnsuppRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthCommandUnsuppRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthCommandUnsuppRcvd.setDescription('The count of diameter command unsupported messages received.')
apDiamAuthUnkownPeerRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthUnkownPeerRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthUnkownPeerRcvd.setDescription('The count of diameter unknown peer messages received.')
apDiamAuthUnkownSessIdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthUnkownSessIdRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthUnkownSessIdRcvd.setDescription('The count of diameter unknown session-id messages received.')
apDiamAuthUnableToComplyRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthUnableToComplyRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthUnableToComplyRcvd.setDescription('The count of diameter unable to comply  messages received.')
apDiamAuthAvpsUnsupportedRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthAvpsUnsupportedRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthAvpsUnsupportedRcvd.setDescription("The count of diameter unsupported AVP's messages received.")
apDiamAuthMissingAvpRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthMissingAvpRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthMissingAvpRcvd.setDescription("The count of diameter missing AVP's messages received.")
apDiamAuthUnknownUsersRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthUnknownUsersRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthUnknownUsersRcvd.setDescription('The count of diameter unknown users messages received.')
apDiamAuthAuthorizationRejectedRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthAuthorizationRejectedRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthAuthorizationRejectedRcvd.setDescription('The count of diameter authorization rejected messages received.')
apDiamAuthRoamingNotAllowedRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthRoamingNotAllowedRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthRoamingNotAllowedRcvd.setDescription('The count of diameter roaming not allowed rejected messages received.')
apDiamAuthNoNon3gppSubscriptionRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthNoNon3gppSubscriptionRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthNoNon3gppSubscriptionRcvd.setDescription('The count of diameter roaming no non 3gpp subcription rejected messages received.')
apDiamAuthNoApnSubscriptionRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthNoApnSubscriptionRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthNoApnSubscriptionRcvd.setDescription('The count of diameter no apn subcription rejected messages received.')
apDiamAuthRatTypeNotAllowedRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 20, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthRatTypeNotAllowedRcvd.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthRatTypeNotAllowedRcvd.setDescription('The count of diameter rat type not allowed rejected messages received.')
apDiamAuthNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3))
apDiamAuthNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 1))
apDiamAuthNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 2))
apDiamAuthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 2, 0))
apDiamAuthServerType = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAuthServerType.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthServerType.setDescription('Address type of diameter authentication server.')
apDiamAuthServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAuthServerAddr.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthServerAddr.setDescription('Address of diameter authentication server.')
apDiamAuthOriginHostType = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 1, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAuthOriginHostType.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthOriginHostType.setDescription('Address type of origin host(MSG).')
apDiamAuthOriginHostAddr = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 1, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAuthOriginHostAddr.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthOriginHostAddr.setDescription('Address of the origin host(MSG)')
apDiamAuthServerPort = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 1, 5), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAuthServerPort.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthServerPort.setDescription('The authentication port of the diameter authentication sever')
apDiamAuthOriginRealm = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAuthOriginRealm.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthOriginRealm.setDescription('The realm of the origin host.')
apDiamAuthSrvrEstTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 2, 0, 1)).setObjects(("AP-DIAMETERAUTH-MIB", "apDiamAuthServerType"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthServerAddr"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginHostType"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginHostAddr"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthServerPort"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginRealm"))
if mibBuilder.loadTexts: apDiamAuthSrvrEstTrap.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthSrvrEstTrap.setDescription(' The trap will be generated when the connection gets established successfully with diameter authentication server')
apDiamAuthSrvrDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 20, 3, 2, 0, 2)).setObjects(("AP-DIAMETERAUTH-MIB", "apDiamAuthServerType"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthServerAddr"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginHostType"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginHostAddr"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthServerPort"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginRealm"))
if mibBuilder.loadTexts: apDiamAuthSrvrDownTrap.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthSrvrDownTrap.setDescription(' The trap will be generated when the diameter authentication server goes down')
apDiamAuthServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 20, 2))
apDiamAuthObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 20, 2, 1))
apDiamAuthStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 20, 2, 1, 1)).setObjects(("AP-DIAMETERAUTH-MIB", "apDiamAuthCapExchReqSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthCapExchReqTimedout"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthCapExchAnsRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthCapExchReqRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthCapExchAnsSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDWDReqSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDWDReqTimedout"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDWDAnsRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDWDReqRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDWDAnsSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDisconPeerReqSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDisconPeerReqTimedout"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDisconPeerAnsRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDisconPeerReqRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthDisconPeerAnsSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthSessTermReqSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthSessTermReqTimedout"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthSessTermAnsRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthAbortSessReqRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthAbortSessAnsSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthEapReqSent"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthEapReqTimedout"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthEapAnsRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthEapAccepts"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthEapRejects"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthServerStatus"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthActiveSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthStatsGroup = apDiamAuthStatsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthStatsGroup.setDescription('A collection of authentication statistics for diameter authentication server.')
apDiamAuthErrorStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 20, 2, 1, 2)).setObjects(("AP-DIAMETERAUTH-MIB", "apDiamAuthUnknownVersionRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthUnknownExchRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthNoCommonAppRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthAppUnsuppRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthCommandUnsuppRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthUnkownPeerRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthUnkownSessIdRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthUnableToComplyRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthAvpsUnsupportedRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthMissingAvpRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthUnknownUsersRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthAuthorizationRejectedRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthRoamingNotAllowedRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthNoNon3gppSubscriptionRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthNoApnSubscriptionRcvd"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthRatTypeNotAllowedRcvd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthErrorStatsGroup = apDiamAuthErrorStatsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthErrorStatsGroup.setDescription('A collection of authentication statistics for diameter authentication server.')
apDiamAuthNotificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 20, 2, 1, 3)).setObjects(("AP-DIAMETERAUTH-MIB", "apDiamAuthServerType"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthServerAddr"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginHostType"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginHostAddr"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthServerPort"), ("AP-DIAMETERAUTH-MIB", "apDiamAuthOriginRealm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthNotificationGroup = apDiamAuthNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthNotificationGroup.setDescription('A collection of notification objects for diameter authentication server.')
mibBuilder.exportSymbols("AP-DIAMETERAUTH-MIB", apDiameterAuthServerModule=apDiameterAuthServerModule, apDiamAuthDisconPeerAnsRcvd=apDiamAuthDisconPeerAnsRcvd, apDiamAuthErrorStatsTable=apDiamAuthErrorStatsTable, apDiamAuthDisconPeerAnsSent=apDiamAuthDisconPeerAnsSent, apDiamAuthEapAccepts=apDiamAuthEapAccepts, apDiamAuthNotificationObjects=apDiamAuthNotificationObjects, apDiamAuthSrvrDownTrap=apDiamAuthSrvrDownTrap, apDiamAuthCapExchReqSent=apDiamAuthCapExchReqSent, apDiamAuthErrorStatsEntry=apDiamAuthErrorStatsEntry, apDiamAuthServerMIBObjects=apDiamAuthServerMIBObjects, apDiamAuthNotificationGroup=apDiamAuthNotificationGroup, apDiamAuthEapReqSent=apDiamAuthEapReqSent, apDiamAuthCapExchReqRcvd=apDiamAuthCapExchReqRcvd, apDiamAuthMissingAvpRcvd=apDiamAuthMissingAvpRcvd, apDiamAuthStatsTable=apDiamAuthStatsTable, apDiamAuthServerAddr=apDiamAuthServerAddr, apDiamAuthDWDReqTimedout=apDiamAuthDWDReqTimedout, apDiamAuthUnableToComplyRcvd=apDiamAuthUnableToComplyRcvd, apDiamAuthServerPort=apDiamAuthServerPort, apDiamAuthEapRejects=apDiamAuthEapRejects, apDiamAuthServerStatus=apDiamAuthServerStatus, apDiamAuthSessTermAnsRcvd=apDiamAuthSessTermAnsRcvd, apDiamAuthSessTermReqSent=apDiamAuthSessTermReqSent, apDiamAuthUnkownSessIdRcvd=apDiamAuthUnkownSessIdRcvd, apDiamAuthCapExchAnsSent=apDiamAuthCapExchAnsSent, apDiamAuthDWDAnsRcvd=apDiamAuthDWDAnsRcvd, apDiamAuthDWDReqSent=apDiamAuthDWDReqSent, apDiamAuthAuthorizationRejectedRcvd=apDiamAuthAuthorizationRejectedRcvd, apDiamAuthEapAnsRcvd=apDiamAuthEapAnsRcvd, apDiamAuthCapExchReqTimedout=apDiamAuthCapExchReqTimedout, apDiamAuthInterfaceType=apDiamAuthInterfaceType, apDiamAuthDisconPeerReqSent=apDiamAuthDisconPeerReqSent, apDiamAuthNotifObjects=apDiamAuthNotifObjects, apDiamAuthActiveSessions=apDiamAuthActiveSessions, apDiamAuthAbortSessAnsSent=apDiamAuthAbortSessAnsSent, apDiamAuthOriginHostType=apDiamAuthOriginHostType, apDiamAuthOriginRealm=apDiamAuthOriginRealm, apDiamAuthStatsGroup=apDiamAuthStatsGroup, apDiamAuthStatsEntry=apDiamAuthStatsEntry, apDiamAuthCommandUnsuppRcvd=apDiamAuthCommandUnsuppRcvd, apDiamAuthDWDReqRcvd=apDiamAuthDWDReqRcvd, apDiamAuthCapExchAnsRcvd=apDiamAuthCapExchAnsRcvd, apDiamAuthNoCommonAppRcvd=apDiamAuthNoCommonAppRcvd, apDiamAuthSrvrEstTrap=apDiamAuthSrvrEstTrap, apDiamAuthNoNon3gppSubscriptionRcvd=apDiamAuthNoNon3gppSubscriptionRcvd, apDiamAuthServerAddress=apDiamAuthServerAddress, apDiamAuthErrorStatsGroup=apDiamAuthErrorStatsGroup, apDiamAuthOriginHostAddr=apDiamAuthOriginHostAddr, apDiamAuthServerType=apDiamAuthServerType, apDiamAuthAvpsUnsupportedRcvd=apDiamAuthAvpsUnsupportedRcvd, apDiamAuthSessTermReqTimedout=apDiamAuthSessTermReqTimedout, apDiamAuthAppUnsuppRcvd=apDiamAuthAppUnsuppRcvd, apDiamAuthDisconPeerReqTimedout=apDiamAuthDisconPeerReqTimedout, apDiamAuthEapReqTimedout=apDiamAuthEapReqTimedout, apDiamAuthUnkownPeerRcvd=apDiamAuthUnkownPeerRcvd, apDiamAuthUnknownExchRcvd=apDiamAuthUnknownExchRcvd, apDiamAuthNotifPrefix=apDiamAuthNotifPrefix, apDiamAuthDWDAnsSent=apDiamAuthDWDAnsSent, apDiamAuthUnknownUsersRcvd=apDiamAuthUnknownUsersRcvd, apDiamAuthDisconPeerReqRcvd=apDiamAuthDisconPeerReqRcvd, apDiamAuthObjectGroups=apDiamAuthObjectGroups, apDiamAuthNoApnSubscriptionRcvd=apDiamAuthNoApnSubscriptionRcvd, apDiamAuthRatTypeNotAllowedRcvd=apDiamAuthRatTypeNotAllowedRcvd, apDiamAuthRoamingNotAllowedRcvd=apDiamAuthRoamingNotAllowedRcvd, apDiamAuthUnknownVersionRcvd=apDiamAuthUnknownVersionRcvd, apDiamAuthServerConformance=apDiamAuthServerConformance, PYSNMP_MODULE_ID=apDiameterAuthServerModule, apDiamAuthNotifications=apDiamAuthNotifications, apDiamAuthAbortSessReqRcvd=apDiamAuthAbortSessReqRcvd)
