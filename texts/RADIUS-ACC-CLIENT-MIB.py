#
# PySNMP MIB module RADIUS-ACC-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RADIUS-ACC-CLIENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, mib_2, Integer32, iso, Counter32, Gauge32, Bits, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "mib-2", "Integer32", "iso", "Counter32", "Gauge32", "Bits", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
radiusAccClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 2, 2))
radiusAccClientMIB.setRevisions(('1999-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: radiusAccClientMIB.setRevisionsDescriptions(('Initial version as published in RFC 2620',))
if mibBuilder.loadTexts: radiusAccClientMIB.setLastUpdated('9906110000Z')
if mibBuilder.loadTexts: radiusAccClientMIB.setOrganization('IETF RADIUS Working Group.')
if mibBuilder.loadTexts: radiusAccClientMIB.setContactInfo(' Bernard Aboba\n            Microsoft\n            One Microsoft Way\n            Redmond, WA  98052\n            US\n\n            Phone: +1 425 936 6605\n            EMail: bernarda@microsoft.com')
if mibBuilder.loadTexts: radiusAccClientMIB.setDescription('The MIB module for entities implementing the client side of\n              the Remote Access Dialin User Service (RADIUS) accounting\n              protocol.')
radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setStatus('current')
if mibBuilder.loadTexts: radiusMIB.setDescription('The OID assigned to RADIUS MIB work by the IANA.')
radiusAccounting = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2))
radiusAccClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 1))
radiusAccClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1))
radiusAccClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientInvalidServerAddresses.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientInvalidServerAddresses.setDescription('The number of RADIUS Accounting-Response packets\n             received from unknown addresses.')
radiusAccClientIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientIdentifier.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientIdentifier.setDescription('The NAS-Identifier of the RADIUS accounting client. This\n             is not necessarily the same as sysName in MIB II.')
radiusAccServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3), )
if mibBuilder.loadTexts: radiusAccServerTable.setStatus('current')
if mibBuilder.loadTexts: radiusAccServerTable.setDescription('The (conceptual) table listing the RADIUS accounting\n             servers with which the client shares a secret.')
radiusAccServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1), ).setIndexNames((0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"))
if mibBuilder.loadTexts: radiusAccServerEntry.setStatus('current')
if mibBuilder.loadTexts: radiusAccServerEntry.setDescription('An entry (conceptual row) representing a RADIUS\n             accounting server with which the client shares a secret.')
radiusAccServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusAccServerIndex.setStatus('current')
if mibBuilder.loadTexts: radiusAccServerIndex.setDescription('A number uniquely identifying each RADIUS\n             Accounting server with which this client\n             communicates.')
radiusAccServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServerAddress.setStatus('current')
if mibBuilder.loadTexts: radiusAccServerAddress.setDescription('The IP address of the RADIUS accounting server\n             referred to in this table entry.')
radiusAccClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientServerPortNumber.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientServerPortNumber.setDescription('The UDP port the client is using to send requests to\n             this server.')
radiusAccClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientRoundTripTime.setDescription('The time interval between the most recent\n             Accounting-Response and the Accounting-Request that\n             matched it from this RADIUS accounting server.')
radiusAccClientRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientRequests.setDescription('The number of RADIUS Accounting-Request packets\n             sent. This does not include retransmissions.')
radiusAccClientRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientRetransmissions.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientRetransmissions.setDescription('The number of RADIUS Accounting-Request packets\n             retransmitted to this RADIUS accounting server.\n             Retransmissions include retries where the\n             Identifier and Acct-Delay have been updated, as\n             well as those in which they remain the same.')
radiusAccClientResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientResponses.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientResponses.setDescription('The number of RADIUS packets received on the\n             accounting port from this server.')
radiusAccClientMalformedResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientMalformedResponses.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientMalformedResponses.setDescription('The number of malformed RADIUS Accounting-Response\n              packets received from this server. Malformed packets\n             include packets with an invalid length. Bad\n             authenticators and unknown types are not included as\n             malformed accounting responses.')
radiusAccClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientBadAuthenticators.setDescription('The number of RADIUS Accounting-Response\n             packets which contained invalid authenticators\n             received from this server.')
radiusAccClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientPendingRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientPendingRequests.setDescription('The number of RADIUS Accounting-Request packets\n             sent to this server that have not yet timed out or\n             received a response. This variable is incremented when an\n             Accounting-Request is sent and decremented due to\n             receipt of an Accounting-Response, a timeout or\n             a retransmission.')
radiusAccClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientTimeouts.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientTimeouts.setDescription('The number of accounting timeouts to this server.\n           After a timeout the client may retry to the same\n           server, send to a different server, or give up.\n           A retry to the same server is counted as a\n           retransmit as well as a timeout. A send to a different\n           server is counted as an Accounting-Request as well as\n           a timeout.')
radiusAccClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientUnknownTypes.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientUnknownTypes.setDescription('The number of RADIUS packets of unknown type which\n             were received from this server on the accounting port.')
radiusAccClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientPacketsDropped.setDescription('The number of RADIUS packets which were received from\n             this server on the accounting port and dropped for some\n             other reason.')
radiusAccClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2))
radiusAccClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1))
radiusAccClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2))
radiusAccClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1, 1)).setObjects(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccClientMIBCompliance = radiusAccClientMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientMIBCompliance.setDescription('The compliance statement for accounting clients\n            implementing the RADIUS Accounting Client MIB.')
radiusAccClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 1)).setObjects(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientIdentifier"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientInvalidServerAddresses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRoundTripTime"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRequests"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRetransmissions"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientResponses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMalformedResponses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientBadAuthenticators"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPendingRequests"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientTimeouts"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientUnknownTypes"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccClientMIBGroup = radiusAccClientMIBGroup.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientMIBGroup.setDescription('The basic collection of objects providing management of\n            RADIUS Accounting Clients.')
mibBuilder.exportSymbols("RADIUS-ACC-CLIENT-MIB", radiusAccClientResponses=radiusAccClientResponses, radiusAccServerIndex=radiusAccServerIndex, radiusAccClientMIBCompliance=radiusAccClientMIBCompliance, radiusAccClientTimeouts=radiusAccClientTimeouts, radiusAccClientIdentifier=radiusAccClientIdentifier, PYSNMP_MODULE_ID=radiusAccClientMIB, radiusAccClientMIBGroups=radiusAccClientMIBGroups, radiusAccClientRetransmissions=radiusAccClientRetransmissions, radiusAccClientMIBObjects=radiusAccClientMIBObjects, radiusAccClientInvalidServerAddresses=radiusAccClientInvalidServerAddresses, radiusAccClientServerPortNumber=radiusAccClientServerPortNumber, radiusAccServerTable=radiusAccServerTable, radiusAccServerAddress=radiusAccServerAddress, radiusAccClientPendingRequests=radiusAccClientPendingRequests, radiusAccClientRoundTripTime=radiusAccClientRoundTripTime, radiusAccClientUnknownTypes=radiusAccClientUnknownTypes, radiusAccServerEntry=radiusAccServerEntry, radiusAccClientMIBGroup=radiusAccClientMIBGroup, radiusAccClientPacketsDropped=radiusAccClientPacketsDropped, radiusAccClient=radiusAccClient, radiusAccClientMIBCompliances=radiusAccClientMIBCompliances, radiusAccClientRequests=radiusAccClientRequests, radiusAccClientMIB=radiusAccClientMIB, radiusAccounting=radiusAccounting, radiusAccClientBadAuthenticators=radiusAccClientBadAuthenticators, radiusAccClientMIBConformance=radiusAccClientMIBConformance, radiusMIB=radiusMIB, radiusAccClientMalformedResponses=radiusAccClientMalformedResponses)
