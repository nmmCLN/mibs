#
# PySNMP MIB module APRADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APRADIUS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, NotificationType, MibIdentifier, Unsigned32, iso, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "Unsigned32", "iso", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
apRadiusServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 18))
apRadiusServerModule.setRevisions(('2014-06-26 00:00',))
if mibBuilder.loadTexts: apRadiusServerModule.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apRadiusServerModule.setOrganization('Oracle Communications')
apRadiusServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1))
apRadiusServerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1), )
if mibBuilder.loadTexts: apRadiusServerStatsTable.setStatus('current')
apRadiusServerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1), ).setIndexNames((0, "APRADIUS-MIB", "apRadiusServerAddressType"), (0, "APRADIUS-MIB", "apRadiusServerAddress"))
if mibBuilder.loadTexts: apRadiusServerStatsEntry.setStatus('current')
apRadiusServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAddressType.setStatus('current')
apRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAddress.setStatus('current')
apRadiusServerRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerRoundTripTime.setStatus('current')
apRadiusServerMalformedAccessResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerMalformedAccessResponse.setStatus('current')
apRadiusServerAccessRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessRequests.setStatus('current')
apRadiusServerDisconnectRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerDisconnectRequests.setStatus('current')
apRadiusServerDisconnectACKs = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerDisconnectACKs.setStatus('current')
apRadiusServerDisconnectNACks = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerDisconnectNACks.setStatus('current')
apRadiusServerBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerBadAuthenticators.setStatus('current')
apRadiusServerAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessRetransmissions.setStatus('current')
apRadiusServerAccessAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessAccepts.setStatus('current')
apRadiusServerTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerTimeouts.setStatus('current')
apRadiusServerAccessRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessRejects.setStatus('current')
apRadiusServerUnknownPDUTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerUnknownPDUTypes.setStatus('current')
apRadiusServerAccessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessChallenges.setStatus('current')
apRadiusServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 18, 2))
apRadiusObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 18, 2, 1))
apRadiusInterfaceStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 18, 2, 1, 1)).setObjects(("APRADIUS-MIB", "apRadiusServerRoundTripTime"), ("APRADIUS-MIB", "apRadiusServerMalformedAccessResponse"), ("APRADIUS-MIB", "apRadiusServerAccessRequests"), ("APRADIUS-MIB", "apRadiusServerDisconnectRequests"), ("APRADIUS-MIB", "apRadiusServerDisconnectACKs"), ("APRADIUS-MIB", "apRadiusServerDisconnectNACks"), ("APRADIUS-MIB", "apRadiusServerBadAuthenticators"), ("APRADIUS-MIB", "apRadiusServerAccessRetransmissions"), ("APRADIUS-MIB", "apRadiusServerAccessAccepts"), ("APRADIUS-MIB", "apRadiusServerTimeouts"), ("APRADIUS-MIB", "apRadiusServerAccessRejects"), ("APRADIUS-MIB", "apRadiusServerUnknownPDUTypes"), ("APRADIUS-MIB", "apRadiusServerAccessChallenges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusInterfaceStatsGroup = apRadiusInterfaceStatsGroup.setStatus('current')
mibBuilder.exportSymbols("APRADIUS-MIB", apRadiusServerBadAuthenticators=apRadiusServerBadAuthenticators, apRadiusServerMIBObjects=apRadiusServerMIBObjects, apRadiusServerConformance=apRadiusServerConformance, apRadiusServerAccessChallenges=apRadiusServerAccessChallenges, apRadiusServerStatsEntry=apRadiusServerStatsEntry, apRadiusServerDisconnectRequests=apRadiusServerDisconnectRequests, apRadiusServerModule=apRadiusServerModule, apRadiusServerAccessRequests=apRadiusServerAccessRequests, apRadiusServerRoundTripTime=apRadiusServerRoundTripTime, apRadiusObjectGroups=apRadiusObjectGroups, apRadiusServerAccessAccepts=apRadiusServerAccessAccepts, apRadiusServerAccessRejects=apRadiusServerAccessRejects, apRadiusServerTimeouts=apRadiusServerTimeouts, apRadiusServerDisconnectACKs=apRadiusServerDisconnectACKs, apRadiusServerMalformedAccessResponse=apRadiusServerMalformedAccessResponse, apRadiusServerUnknownPDUTypes=apRadiusServerUnknownPDUTypes, apRadiusServerDisconnectNACks=apRadiusServerDisconnectNACks, apRadiusServerAddressType=apRadiusServerAddressType, apRadiusInterfaceStatsGroup=apRadiusInterfaceStatsGroup, apRadiusServerAccessRetransmissions=apRadiusServerAccessRetransmissions, PYSNMP_MODULE_ID=apRadiusServerModule, apRadiusServerAddress=apRadiusServerAddress, apRadiusServerStatsTable=apRadiusServerStatsTable)
