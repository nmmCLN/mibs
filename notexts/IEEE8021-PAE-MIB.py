#
# PySNMP MIB module IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IEEE8021-PAE-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:23 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, Counter32, Counter64, ObjectIdentity, iso, Bits, Gauge32, TimeTicks, NotificationType, ModuleIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Counter64", "ObjectIdentity", "iso", "Bits", "Gauge32", "TimeTicks", "NotificationType", "ModuleIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "TruthValue")
ieee8021paeMIB = ModuleIdentity((1, 0, 8802, 1, 1, 1))
ieee8021paeMIB.setRevisions(('2004-06-22 00:00', '2001-01-16 00:00',))
if mibBuilder.loadTexts: ieee8021paeMIB.setLastUpdated('200406220000Z')
if mibBuilder.loadTexts: ieee8021paeMIB.setOrganization('IEEE 802.1 Working Group')
paeMIBObjects = MibIdentifier((1, 0, 8802, 1, 1, 1, 1))
class PaeControlledDirections(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("both", 0), ("in", 1))

class PaeControlledPortStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("authorized", 1), ("unauthorized", 2))

class PaeControlledPortControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forceUnauthorized", 1), ("auto", 2), ("forceAuthorized", 3))

dot1xPaeSystem = MibIdentifier((1, 0, 8802, 1, 1, 1, 1, 1))
dot1xPaeAuthenticator = MibIdentifier((1, 0, 8802, 1, 1, 1, 1, 2))
dot1xPaeSupplicant = MibIdentifier((1, 0, 8802, 1, 1, 1, 1, 3))
dot1xPaeSystemAuthControl = MibScalar((1, 0, 8802, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPaeSystemAuthControl.setStatus('current')
dot1xPaePortTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: dot1xPaePortTable.setStatus('current')
dot1xPaePortEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xPaePortEntry.setStatus('current')
dot1xPaePortNumber = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot1xPaePortNumber.setStatus('current')
dot1xPaePortProtocolVersion = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xPaePortProtocolVersion.setStatus('current')
dot1xPaePortCapabilities = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 3), Bits().clone(namedValues=NamedValues(("dot1xPaePortAuthCapable", 0), ("dot1xPaePortSuppCapable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xPaePortCapabilities.setStatus('current')
dot1xPaePortInitialize = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPaePortInitialize.setStatus('current')
dot1xPaePortReauthenticate = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPaePortReauthenticate.setStatus('current')
dot1xAuthConfigTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: dot1xAuthConfigTable.setStatus('current')
dot1xAuthConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthConfigEntry.setStatus('current')
dot1xAuthPaeState = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9), ("restart", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthPaeState.setStatus('current')
dot1xAuthBackendAuthState = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7), ("ignore", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAuthState.setStatus('current')
dot1xAuthAdminControlledDirections = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 3), PaeControlledDirections()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthAdminControlledDirections.setStatus('current')
dot1xAuthOperControlledDirections = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 4), PaeControlledDirections()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthOperControlledDirections.setStatus('current')
dot1xAuthAuthControlledPortStatus = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 5), PaeControlledPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthControlledPortStatus.setStatus('current')
dot1xAuthAuthControlledPortControl = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 6), PaeControlledPortControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthAuthControlledPortControl.setStatus('current')
dot1xAuthQuietPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 7), Unsigned32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthQuietPeriod.setStatus('current')
dot1xAuthTxPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 8), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthTxPeriod.setStatus('deprecated')
dot1xAuthSuppTimeout = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 9), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthSuppTimeout.setStatus('deprecated')
dot1xAuthServerTimeout = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 10), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthServerTimeout.setStatus('current')
dot1xAuthMaxReq = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 11), Unsigned32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthMaxReq.setStatus('deprecated')
dot1xAuthReAuthPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 12), Unsigned32().clone(3600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthReAuthPeriod.setStatus('current')
dot1xAuthReAuthEnabled = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthReAuthEnabled.setStatus('current')
dot1xAuthKeyTxEnabled = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthKeyTxEnabled.setStatus('current')
dot1xAuthStatsTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 2), )
if mibBuilder.loadTexts: dot1xAuthStatsTable.setStatus('current')
dot1xAuthStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthStatsEntry.setStatus('current')
dot1xAuthEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolFramesRx.setStatus('current')
dot1xAuthEapolFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolFramesTx.setStatus('current')
dot1xAuthEapolStartFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolStartFramesRx.setStatus('current')
dot1xAuthEapolLogoffFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolLogoffFramesRx.setStatus('current')
dot1xAuthEapolRespIdFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolRespIdFramesRx.setStatus('current')
dot1xAuthEapolRespFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolRespFramesRx.setStatus('current')
dot1xAuthEapolReqIdFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolReqIdFramesTx.setStatus('current')
dot1xAuthEapolReqFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolReqFramesTx.setStatus('current')
dot1xAuthInvalidEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthInvalidEapolFramesRx.setStatus('current')
dot1xAuthEapLengthErrorFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapLengthErrorFramesRx.setStatus('current')
dot1xAuthLastEapolFrameVersion = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthLastEapolFrameVersion.setStatus('current')
dot1xAuthLastEapolFrameSource = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthLastEapolFrameSource.setStatus('current')
dot1xAuthDiagTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 3), )
if mibBuilder.loadTexts: dot1xAuthDiagTable.setStatus('deprecated')
dot1xAuthDiagEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthDiagEntry.setStatus('deprecated')
dot1xAuthEntersConnecting = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEntersConnecting.setStatus('deprecated')
dot1xAuthEapLogoffsWhileConnecting = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapLogoffsWhileConnecting.setStatus('deprecated')
dot1xAuthEntersAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEntersAuthenticating.setStatus('deprecated')
dot1xAuthAuthSuccessWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthSuccessWhileAuthenticating.setStatus('deprecated')
dot1xAuthAuthTimeoutsWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthTimeoutsWhileAuthenticating.setStatus('deprecated')
dot1xAuthAuthFailWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthFailWhileAuthenticating.setStatus('deprecated')
dot1xAuthAuthReauthsWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthReauthsWhileAuthenticating.setStatus('deprecated')
dot1xAuthAuthEapStartsWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapStartsWhileAuthenticating.setStatus('deprecated')
dot1xAuthAuthEapLogoffWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapLogoffWhileAuthenticating.setStatus('deprecated')
dot1xAuthAuthReauthsWhileAuthenticated = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthReauthsWhileAuthenticated.setStatus('deprecated')
dot1xAuthAuthEapStartsWhileAuthenticated = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapStartsWhileAuthenticated.setStatus('deprecated')
dot1xAuthAuthEapLogoffWhileAuthenticated = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapLogoffWhileAuthenticated.setStatus('deprecated')
dot1xAuthBackendResponses = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendResponses.setStatus('deprecated')
dot1xAuthBackendAccessChallenges = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAccessChallenges.setStatus('deprecated')
dot1xAuthBackendOtherRequestsToSupplicant = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendOtherRequestsToSupplicant.setStatus('deprecated')
dot1xAuthBackendNonNakResponsesFromSupplicant = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendNonNakResponsesFromSupplicant.setStatus('deprecated')
dot1xAuthBackendAuthSuccesses = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAuthSuccesses.setStatus('deprecated')
dot1xAuthBackendAuthFails = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAuthFails.setStatus('deprecated')
dot1xAuthSessionStatsTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 4), )
if mibBuilder.loadTexts: dot1xAuthSessionStatsTable.setStatus('current')
dot1xAuthSessionStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthSessionStatsEntry.setStatus('current')
dot1xAuthSessionOctetsRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionOctetsRx.setStatus('current')
dot1xAuthSessionOctetsTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionOctetsTx.setStatus('current')
dot1xAuthSessionFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionFramesRx.setStatus('current')
dot1xAuthSessionFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionFramesTx.setStatus('current')
dot1xAuthSessionId = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionId.setStatus('current')
dot1xAuthSessionAuthenticMethod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("remoteAuthServer", 1), ("localAuthServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionAuthenticMethod.setStatus('current')
dot1xAuthSessionTime = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionTime.setStatus('current')
dot1xAuthSessionTerminateCause = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 999))).clone(namedValues=NamedValues(("supplicantLogoff", 1), ("portFailure", 2), ("supplicantRestart", 3), ("reauthFailed", 4), ("authControlForceUnauth", 5), ("portReInit", 6), ("portAdminDisabled", 7), ("notTerminatedYet", 999)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionTerminateCause.setStatus('current')
dot1xAuthSessionUserName = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionUserName.setStatus('current')
dot1xSuppConfigTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: dot1xSuppConfigTable.setStatus('current')
dot1xSuppConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xSuppConfigEntry.setStatus('current')
dot1xSuppPaeState = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("disconnected", 1), ("logoff", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("acquired", 6), ("held", 7), ("restart", 8), ("sForceAuth", 9), ("sForceUnauth", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppPaeState.setStatus('current')
dot1xSuppHeldPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 2), Unsigned32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppHeldPeriod.setStatus('current')
dot1xSuppAuthPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 3), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppAuthPeriod.setStatus('current')
dot1xSuppStartPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 4), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppStartPeriod.setStatus('current')
dot1xSuppMaxStart = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 5), Unsigned32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppMaxStart.setStatus('current')
dot1xSuppControlledPortStatus = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 6), PaeControlledPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppControlledPortStatus.setStatus('current')
dot1xSuppAccessCtrlWithAuth = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppAccessCtrlWithAuth.setStatus('current')
dot1xSuppBackendState = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("initialize", 1), ("idle", 2), ("request", 3), ("response", 4), ("receive", 5), ("fail", 6), ("success", 7), ("timeout", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppBackendState.setStatus('current')
dot1xSuppStatsTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: dot1xSuppStatsTable.setStatus('current')
dot1xSuppStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xSuppStatsEntry.setStatus('current')
dot1xSuppEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolFramesRx.setStatus('current')
dot1xSuppEapolFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolFramesTx.setStatus('current')
dot1xSuppEapolStartFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolStartFramesTx.setStatus('current')
dot1xSuppEapolLogoffFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolLogoffFramesTx.setStatus('current')
dot1xSuppEapolRespIdFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolRespIdFramesTx.setStatus('deprecated')
dot1xSuppEapolRespFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolRespFramesTx.setStatus('deprecated')
dot1xSuppEapolReqIdFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolReqIdFramesRx.setStatus('deprecated')
dot1xSuppEapolReqFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolReqFramesRx.setStatus('deprecated')
dot1xSuppInvalidEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppInvalidEapolFramesRx.setStatus('current')
dot1xSuppEapLengthErrorFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapLengthErrorFramesRx.setStatus('current')
dot1xSuppLastEapolFrameVersion = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppLastEapolFrameVersion.setStatus('current')
dot1xSuppLastEapolFrameSource = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppLastEapolFrameSource.setStatus('current')
dot1xPaeConformance = MibIdentifier((1, 0, 8802, 1, 1, 1, 2))
dot1xPaeGroups = MibIdentifier((1, 0, 8802, 1, 1, 1, 2, 1))
dot1xPaeCompliances = MibIdentifier((1, 0, 8802, 1, 1, 1, 2, 2))
dot1xPaeSystemGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 1)).setObjects(("IEEE8021-PAE-MIB", "dot1xPaeSystemAuthControl"), ("IEEE8021-PAE-MIB", "dot1xPaePortProtocolVersion"), ("IEEE8021-PAE-MIB", "dot1xPaePortCapabilities"), ("IEEE8021-PAE-MIB", "dot1xPaePortInitialize"), ("IEEE8021-PAE-MIB", "dot1xPaePortReauthenticate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSystemGroup = dot1xPaeSystemGroup.setStatus('current')
dot1xPaeAuthConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 2)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"), ("IEEE8021-PAE-MIB", "dot1xAuthAdminControlledDirections"), ("IEEE8021-PAE-MIB", "dot1xAuthOperControlledDirections"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortStatus"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortControl"), ("IEEE8021-PAE-MIB", "dot1xAuthQuietPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthTxPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthSuppTimeout"), ("IEEE8021-PAE-MIB", "dot1xAuthServerTimeout"), ("IEEE8021-PAE-MIB", "dot1xAuthMaxReq"), ("IEEE8021-PAE-MIB", "dot1xAuthReAuthPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthReAuthEnabled"), ("IEEE8021-PAE-MIB", "dot1xAuthKeyTxEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthConfigGroup = dot1xPaeAuthConfigGroup.setStatus('deprecated')
dot1xPaeAuthStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 3)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolStartFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolLogoffFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolRespIdFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolRespFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolReqIdFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolReqFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthInvalidEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapLengthErrorFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthLastEapolFrameVersion"), ("IEEE8021-PAE-MIB", "dot1xAuthLastEapolFrameSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthStatsGroup = dot1xPaeAuthStatsGroup.setStatus('current')
dot1xPaeAuthDiagGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 4)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthEntersConnecting"), ("IEEE8021-PAE-MIB", "dot1xAuthEapLogoffsWhileConnecting"), ("IEEE8021-PAE-MIB", "dot1xAuthEntersAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthSuccessWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthTimeoutsWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthFailWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthReauthsWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapStartsWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthReauthsWhileAuthenticated"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapStartsWhileAuthenticated"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticated"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendResponses"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAccessChallenges"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendOtherRequestsToSupplicant"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendNonNakResponsesFromSupplicant"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthSuccesses"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthFails"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthDiagGroup = dot1xPaeAuthDiagGroup.setStatus('deprecated')
dot1xPaeAuthSessionStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 5)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthSessionOctetsRx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionOctetsTx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionId"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionAuthenticMethod"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionTime"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthSessionStatsGroup = dot1xPaeAuthSessionStatsGroup.setStatus('current')
dot1xPaeSuppConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 6)).setObjects(("IEEE8021-PAE-MIB", "dot1xSuppPaeState"), ("IEEE8021-PAE-MIB", "dot1xSuppHeldPeriod"), ("IEEE8021-PAE-MIB", "dot1xSuppAuthPeriod"), ("IEEE8021-PAE-MIB", "dot1xSuppStartPeriod"), ("IEEE8021-PAE-MIB", "dot1xSuppMaxStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSuppConfigGroup = dot1xPaeSuppConfigGroup.setStatus('current')
dot1xPaeSuppStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 7)).setObjects(("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolStartFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolLogoffFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolRespIdFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolRespFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolReqIdFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolReqFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppInvalidEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapLengthErrorFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameVersion"), ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSuppStatsGroup = dot1xPaeSuppStatsGroup.setStatus('deprecated')
dot1xPaeAuthConfigGroup2 = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 8)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"), ("IEEE8021-PAE-MIB", "dot1xAuthAdminControlledDirections"), ("IEEE8021-PAE-MIB", "dot1xAuthOperControlledDirections"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortStatus"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortControl"), ("IEEE8021-PAE-MIB", "dot1xAuthQuietPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthServerTimeout"), ("IEEE8021-PAE-MIB", "dot1xAuthReAuthPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthReAuthEnabled"), ("IEEE8021-PAE-MIB", "dot1xAuthKeyTxEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthConfigGroup2 = dot1xPaeAuthConfigGroup2.setStatus('current')
dot1xPaeSuppConfigGroup2 = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 9)).setObjects(("IEEE8021-PAE-MIB", "dot1xSuppControlledPortStatus"), ("IEEE8021-PAE-MIB", "dot1xSuppAccessCtrlWithAuth"), ("IEEE8021-PAE-MIB", "dot1xSuppBackendState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSuppConfigGroup2 = dot1xPaeSuppConfigGroup2.setStatus('current')
dot1xPaeSuppStatsGroup2 = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 10)).setObjects(("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolStartFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolLogoffFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppInvalidEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapLengthErrorFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameVersion"), ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSuppStatsGroup2 = dot1xPaeSuppStatsGroup2.setStatus('current')
dot1xPaeCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 1, 2, 2, 1)).setObjects(("IEEE8021-PAE-MIB", "dot1xPaeSystemGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthConfigGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthStatsGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthDiagGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthSessionStatsGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeSuppConfigGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeSuppStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeCompliance = dot1xPaeCompliance.setStatus('deprecated')
dot1xPaeCompliance2 = ModuleCompliance((1, 0, 8802, 1, 1, 1, 2, 2, 2)).setObjects(("IEEE8021-PAE-MIB", "dot1xPaeSystemGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthConfigGroup2"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthStatsGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthSessionStatsGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeSuppConfigGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeSuppStatsGroup2"), ("IEEE8021-PAE-MIB", "dot1xPaeSuppConfigGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeCompliance2 = dot1xPaeCompliance2.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PAE-MIB", dot1xAuthBackendOtherRequestsToSupplicant=dot1xAuthBackendOtherRequestsToSupplicant, dot1xPaeAuthConfigGroup=dot1xPaeAuthConfigGroup, dot1xPaeSuppConfigGroup2=dot1xPaeSuppConfigGroup2, dot1xAuthServerTimeout=dot1xAuthServerTimeout, dot1xAuthBackendNonNakResponsesFromSupplicant=dot1xAuthBackendNonNakResponsesFromSupplicant, dot1xSuppHeldPeriod=dot1xSuppHeldPeriod, PaeControlledPortControl=PaeControlledPortControl, dot1xAuthMaxReq=dot1xAuthMaxReq, dot1xAuthEntersAuthenticating=dot1xAuthEntersAuthenticating, dot1xAuthQuietPeriod=dot1xAuthQuietPeriod, dot1xAuthEntersConnecting=dot1xAuthEntersConnecting, dot1xPaeConformance=dot1xPaeConformance, dot1xAuthSessionStatsTable=dot1xAuthSessionStatsTable, dot1xSuppEapLengthErrorFramesRx=dot1xSuppEapLengthErrorFramesRx, dot1xPaePortProtocolVersion=dot1xPaePortProtocolVersion, dot1xSuppControlledPortStatus=dot1xSuppControlledPortStatus, PYSNMP_MODULE_ID=ieee8021paeMIB, dot1xPaeAuthenticator=dot1xPaeAuthenticator, dot1xAuthSuppTimeout=dot1xAuthSuppTimeout, dot1xAuthAuthEapStartsWhileAuthenticating=dot1xAuthAuthEapStartsWhileAuthenticating, dot1xPaePortNumber=dot1xPaePortNumber, dot1xAuthBackendAuthSuccesses=dot1xAuthBackendAuthSuccesses, PaeControlledPortStatus=PaeControlledPortStatus, dot1xSuppAccessCtrlWithAuth=dot1xSuppAccessCtrlWithAuth, dot1xSuppEapolFramesTx=dot1xSuppEapolFramesTx, dot1xSuppConfigTable=dot1xSuppConfigTable, dot1xSuppEapolFramesRx=dot1xSuppEapolFramesRx, dot1xPaePortTable=dot1xPaePortTable, dot1xPaeGroups=dot1xPaeGroups, dot1xAuthTxPeriod=dot1xAuthTxPeriod, dot1xAuthBackendAuthFails=dot1xAuthBackendAuthFails, dot1xPaeAuthSessionStatsGroup=dot1xPaeAuthSessionStatsGroup, dot1xPaePortEntry=dot1xPaePortEntry, dot1xSuppAuthPeriod=dot1xSuppAuthPeriod, dot1xSuppEapolReqFramesRx=dot1xSuppEapolReqFramesRx, dot1xAuthSessionFramesTx=dot1xAuthSessionFramesTx, dot1xSuppStatsTable=dot1xSuppStatsTable, dot1xSuppStartPeriod=dot1xSuppStartPeriod, dot1xPaeSystemGroup=dot1xPaeSystemGroup, dot1xAuthStatsEntry=dot1xAuthStatsEntry, dot1xAuthAuthTimeoutsWhileAuthenticating=dot1xAuthAuthTimeoutsWhileAuthenticating, dot1xAuthEapLengthErrorFramesRx=dot1xAuthEapLengthErrorFramesRx, dot1xAuthEapolFramesTx=dot1xAuthEapolFramesTx, dot1xAuthEapLogoffsWhileConnecting=dot1xAuthEapLogoffsWhileConnecting, dot1xAuthEapolFramesRx=dot1xAuthEapolFramesRx, dot1xPaeSystemAuthControl=dot1xPaeSystemAuthControl, dot1xPaeSuppConfigGroup=dot1xPaeSuppConfigGroup, dot1xAuthEapolRespIdFramesRx=dot1xAuthEapolRespIdFramesRx, dot1xPaeAuthConfigGroup2=dot1xPaeAuthConfigGroup2, dot1xAuthSessionAuthenticMethod=dot1xAuthSessionAuthenticMethod, dot1xAuthBackendAccessChallenges=dot1xAuthBackendAccessChallenges, dot1xPaeSuppStatsGroup=dot1xPaeSuppStatsGroup, dot1xAuthBackendAuthState=dot1xAuthBackendAuthState, dot1xPaePortReauthenticate=dot1xPaePortReauthenticate, dot1xAuthSessionId=dot1xAuthSessionId, dot1xAuthEapolRespFramesRx=dot1xAuthEapolRespFramesRx, dot1xPaeSystem=dot1xPaeSystem, dot1xPaeCompliances=dot1xPaeCompliances, dot1xPaeSuppStatsGroup2=dot1xPaeSuppStatsGroup2, dot1xPaeAuthDiagGroup=dot1xPaeAuthDiagGroup, dot1xSuppConfigEntry=dot1xSuppConfigEntry, dot1xSuppStatsEntry=dot1xSuppStatsEntry, dot1xSuppEapolReqIdFramesRx=dot1xSuppEapolReqIdFramesRx, dot1xPaeSupplicant=dot1xPaeSupplicant, dot1xAuthAuthSuccessWhileAuthenticating=dot1xAuthAuthSuccessWhileAuthenticating, dot1xAuthBackendResponses=dot1xAuthBackendResponses, dot1xAuthAuthControlledPortStatus=dot1xAuthAuthControlledPortStatus, dot1xSuppPaeState=dot1xSuppPaeState, dot1xAuthSessionTime=dot1xAuthSessionTime, dot1xSuppLastEapolFrameVersion=dot1xSuppLastEapolFrameVersion, dot1xAuthInvalidEapolFramesRx=dot1xAuthInvalidEapolFramesRx, dot1xAuthDiagEntry=dot1xAuthDiagEntry, dot1xAuthReAuthPeriod=dot1xAuthReAuthPeriod, dot1xAuthSessionTerminateCause=dot1xAuthSessionTerminateCause, dot1xAuthSessionOctetsTx=dot1xAuthSessionOctetsTx, dot1xAuthReAuthEnabled=dot1xAuthReAuthEnabled, dot1xAuthLastEapolFrameVersion=dot1xAuthLastEapolFrameVersion, dot1xAuthAuthControlledPortControl=dot1xAuthAuthControlledPortControl, dot1xAuthStatsTable=dot1xAuthStatsTable, dot1xAuthKeyTxEnabled=dot1xAuthKeyTxEnabled, dot1xAuthConfigTable=dot1xAuthConfigTable, dot1xAuthOperControlledDirections=dot1xAuthOperControlledDirections, dot1xAuthDiagTable=dot1xAuthDiagTable, dot1xPaeCompliance=dot1xPaeCompliance, dot1xAuthAuthReauthsWhileAuthenticated=dot1xAuthAuthReauthsWhileAuthenticated, dot1xSuppMaxStart=dot1xSuppMaxStart, dot1xAuthEapolStartFramesRx=dot1xAuthEapolStartFramesRx, PaeControlledDirections=PaeControlledDirections, dot1xAuthAuthEapLogoffWhileAuthenticated=dot1xAuthAuthEapLogoffWhileAuthenticated, dot1xAuthSessionStatsEntry=dot1xAuthSessionStatsEntry, dot1xSuppEapolStartFramesTx=dot1xSuppEapolStartFramesTx, dot1xSuppEapolRespIdFramesTx=dot1xSuppEapolRespIdFramesTx, dot1xAuthEapolReqFramesTx=dot1xAuthEapolReqFramesTx, dot1xPaeAuthStatsGroup=dot1xPaeAuthStatsGroup, dot1xSuppLastEapolFrameSource=dot1xSuppLastEapolFrameSource, dot1xAuthAdminControlledDirections=dot1xAuthAdminControlledDirections, dot1xAuthEapolLogoffFramesRx=dot1xAuthEapolLogoffFramesRx, dot1xAuthLastEapolFrameSource=dot1xAuthLastEapolFrameSource, dot1xAuthAuthFailWhileAuthenticating=dot1xAuthAuthFailWhileAuthenticating, dot1xPaePortCapabilities=dot1xPaePortCapabilities, dot1xAuthAuthReauthsWhileAuthenticating=dot1xAuthAuthReauthsWhileAuthenticating, dot1xAuthAuthEapStartsWhileAuthenticated=dot1xAuthAuthEapStartsWhileAuthenticated, dot1xAuthSessionUserName=dot1xAuthSessionUserName, dot1xPaeCompliance2=dot1xPaeCompliance2, ieee8021paeMIB=ieee8021paeMIB, dot1xSuppEapolRespFramesTx=dot1xSuppEapolRespFramesTx, dot1xSuppInvalidEapolFramesRx=dot1xSuppInvalidEapolFramesRx, dot1xPaePortInitialize=dot1xPaePortInitialize, dot1xAuthPaeState=dot1xAuthPaeState, dot1xAuthEapolReqIdFramesTx=dot1xAuthEapolReqIdFramesTx, dot1xSuppEapolLogoffFramesTx=dot1xSuppEapolLogoffFramesTx, dot1xAuthAuthEapLogoffWhileAuthenticating=dot1xAuthAuthEapLogoffWhileAuthenticating, dot1xSuppBackendState=dot1xSuppBackendState, dot1xAuthConfigEntry=dot1xAuthConfigEntry, paeMIBObjects=paeMIBObjects, dot1xAuthSessionOctetsRx=dot1xAuthSessionOctetsRx, dot1xAuthSessionFramesRx=dot1xAuthSessionFramesRx)
