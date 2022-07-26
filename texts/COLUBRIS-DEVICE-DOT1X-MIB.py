#
# PySNMP MIB module COLUBRIS-DEVICE-DOT1X-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-DEVICE-DOT1X-MIB.my
# Produced by pysmi-1.1.8 at Tue Jul 26 15:28:57 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
coDevDisIndex, = mibBuilder.importSymbols("COLUBRIS-DEVICE-MIB", "coDevDisIndex")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, iso, IpAddress, MibIdentifier, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Counter64, Integer32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "iso", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Counter64", "Integer32", "NotificationType", "ObjectIdentity")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
colubrisDeviceDot1xMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 32))
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setDescription('Colubris Device IEEE 802.1x MIB.')
colubrisDeviceDot1xMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1))
coDeviceDot1xConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 1))
coDeviceDot1xStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2))
coDeviceDot1xStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3))
coDeviceDot1xStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceDot1xStatusTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatusTable.setDescription('Device IEEE 802.1x wireless station status attributes.')
coDeviceDot1xStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaIndex"))
if mibBuilder.loadTexts: coDeviceDot1xStatusEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatusEntry.setDescription('An entry in the coDeviceDot1xStatusTable.\n                 coDevDisIndex - Uniquely identifies a device on the\n                                 MultiService Controller.\n                 coDev1xStaIndex - Uniquely identifies a 802.1x station on\n                                   the device.')
coDev1xStaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDev1xStaIndex.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaIndex.setDescription('Specifies the index of a 802.1x station on the\n                 device.')
coDev1xStaMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaMacAddress.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaMacAddress.setDescription('Wireless MAC address of the 802.1x station.')
coDev1xStaUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaUserName.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaUserName.setDescription('The User-Name representing the identity of the\n                 Supplicant PAE.')
coDev1xStaPaeState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaPaeState.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaPaeState.setDescription('The current value of the Authenticator PAE state\n                 machine.')
coDev1xStaBackendAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthState.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendAuthState.setDescription('The current state of the Backend Authentication\n                 state machine.')
coDev1xStaPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authorized", 1), ("unauthorized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaPortStatus.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaPortStatus.setDescription('The current value of the controlled Port status\n                 parameter for the Port.')
coDev1xStaSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 7), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaSessionTime.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaSessionTime.setDescription('The duration of the session in seconds.')
coDev1xStaTerminateCause = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 999))).clone(namedValues=NamedValues(("supplicantLogoff", 1), ("portFailure", 2), ("supplicantRestart", 3), ("reauthFailed", 4), ("authControlForceUnauth", 5), ("portReInit", 6), ("portAdminDisabled", 7), ("notTerminatedYet", 999)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaTerminateCause.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaTerminateCause.setDescription('The reason for session termination.')
coDeviceDot1xStatsTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1), )
if mibBuilder.loadTexts: coDeviceDot1xStatsTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatsTable.setDescription('Device IEEE 802.1x wireless client statistic attributes.')
coDeviceDot1xStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1), )
coDeviceDot1xStatusEntry.registerAugmentions(("COLUBRIS-DEVICE-DOT1X-MIB", "coDeviceDot1xStatsEntry"))
coDeviceDot1xStatsEntry.setIndexNames(*coDeviceDot1xStatusEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceDot1xStatsEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatsEntry.setDescription('An entry in the coDeviceDot1xStatsTable.\n                 coDevDisIndex - Uniquely identify a device in the\n                                 MultiService Controller.\n                 coDev1xStaIndex - Uniquely identify a 802.1x station on\n                                   the device.')
coDev1xStaEapolRxFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaEapolRxFrame.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaEapolRxFrame.setDescription('The number of valid EAPOL frames of any type\n                 that have been received by this Authenticator.')
coDev1xStaEapolTxFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaEapolTxFrame.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaEapolTxFrame.setDescription('The number of EAPOL frames of any type that\n                 have been transmitted by this Authenticator.')
coDev1xStaBackendResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendResponses.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendResponses.setDescription('Counts the number of times that the state machine sends\n                 an initial Access-Request packet to the Authentication\n                 server (i.e., executes sendRespToServer on entry to the\n                 RESPONSE state). Indicates that the Authenticator\n                 attempted communication with the Authentication Server.')
coDev1xStaBackendChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendChallenges.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendChallenges.setDescription('Counts the number of times that the state machine\n                 receives an initial Access-Challenge packet from the\n                 Authentication server (i.e., aReq becomes TRUE,\n                 causing exit from the RESPONSE state). Indicates that\n                 the Authentication Server has communication with\n                 the Authenticator.')
coDev1xStaBackendAuthSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthSuccesses.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendAuthSuccesses.setDescription('Counts the number of times that the state machine\n                 receives an EAP-Success message from the Authentication\n                 Server (i.e., aSuccess becomes TRUE, causing a\n                 transition from RESPONSE to SUCCESS). Indicates that\n                 the Supplicant has successfully authenticated to\n                 the Authentication Server.')
coDev1xStaBackendAuthFails = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthFails.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendAuthFails.setDescription('Counts the number of times that the state machine\n                 receives an EAP-Failure message from the Authentication\n                 Server (i.e., aFail becomes TRUE, causing a transition\n                 from RESPONSE to FAIL). Indicates that the Supplicant\n                 has not authenticated to the Authentication Server.')
colubrisDeviceDot1xMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2))
colubrisDeviceDot1xMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 1))
colubrisDeviceDot1xMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2))
colubrisDeviceDot1xMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 1, 1)).setObjects(("COLUBRIS-DEVICE-DOT1X-MIB", "colubrisDeviceDot1xStatusMIBGroup"), ("COLUBRIS-DEVICE-DOT1X-MIB", "colubrisDeviceDot1xStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDot1xMIBCompliance = colubrisDeviceDot1xMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIBCompliance.setDescription('The compliance statement for the Device MIB.')
colubrisDeviceDot1xStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2, 1)).setObjects(("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaMacAddress"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaUserName"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaPaeState"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthState"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaPortStatus"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaSessionTime"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaTerminateCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDot1xStatusMIBGroup = colubrisDeviceDot1xStatusMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceDot1xStatusMIBGroup.setDescription('A collection of status objects for IEEE 802.1x\n                 stations connected to colubris devices.')
colubrisDeviceDot1xStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2, 2)).setObjects(("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaEapolRxFrame"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaEapolTxFrame"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendResponses"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendChallenges"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthSuccesses"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthFails"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDot1xStatsMIBGroup = colubrisDeviceDot1xStatsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceDot1xStatsMIBGroup.setDescription('A collection of statistical objects for IEEE 802.1x\n                 stations connected to colubris devices.')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-DOT1X-MIB", coDev1xStaBackendAuthState=coDev1xStaBackendAuthState, coDeviceDot1xStatusGroup=coDeviceDot1xStatusGroup, coDeviceDot1xStatusEntry=coDeviceDot1xStatusEntry, coDev1xStaIndex=coDev1xStaIndex, coDev1xStaTerminateCause=coDev1xStaTerminateCause, colubrisDeviceDot1xStatsMIBGroup=colubrisDeviceDot1xStatsMIBGroup, coDeviceDot1xStatsEntry=coDeviceDot1xStatsEntry, coDev1xStaBackendResponses=coDev1xStaBackendResponses, coDev1xStaUserName=coDev1xStaUserName, colubrisDeviceDot1xMIBCompliance=colubrisDeviceDot1xMIBCompliance, colubrisDeviceDot1xMIB=colubrisDeviceDot1xMIB, coDev1xStaEapolTxFrame=coDev1xStaEapolTxFrame, coDev1xStaBackendChallenges=coDev1xStaBackendChallenges, coDev1xStaMacAddress=coDev1xStaMacAddress, coDeviceDot1xStatsGroup=coDeviceDot1xStatsGroup, colubrisDeviceDot1xMIBConformance=colubrisDeviceDot1xMIBConformance, PYSNMP_MODULE_ID=colubrisDeviceDot1xMIB, colubrisDeviceDot1xMIBGroups=colubrisDeviceDot1xMIBGroups, coDev1xStaBackendAuthFails=coDev1xStaBackendAuthFails, coDev1xStaEapolRxFrame=coDev1xStaEapolRxFrame, coDeviceDot1xStatusTable=coDeviceDot1xStatusTable, coDeviceDot1xStatsTable=coDeviceDot1xStatsTable, coDeviceDot1xConfigGroup=coDeviceDot1xConfigGroup, colubrisDeviceDot1xStatusMIBGroup=colubrisDeviceDot1xStatusMIBGroup, coDev1xStaPaeState=coDev1xStaPaeState, colubrisDeviceDot1xMIBCompliances=colubrisDeviceDot1xMIBCompliances, coDev1xStaPortStatus=coDev1xStaPortStatus, coDev1xStaBackendAuthSuccesses=coDev1xStaBackendAuthSuccesses, coDev1xStaSessionTime=coDev1xStaSessionTime, colubrisDeviceDot1xMIBObjects=colubrisDeviceDot1xMIBObjects)
