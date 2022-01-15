#
# PySNMP MIB module RADIUS-ACC-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RADIUS-ACC-CLIENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
radiusAccClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 2, 2))
radiusAccClientMIB.setRevisions(('1999-06-11 00:00',))
if mibBuilder.loadTexts: radiusAccClientMIB.setLastUpdated('9906110000Z')
if mibBuilder.loadTexts: radiusAccClientMIB.setOrganization('IETF RADIUS Working Group.')
radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setStatus('current')
radiusAccounting = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2))
radiusAccClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 1))
radiusAccClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1))
radiusAccClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientInvalidServerAddresses.setStatus('current')
radiusAccClientIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientIdentifier.setStatus('current')
radiusAccServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3), )
if mibBuilder.loadTexts: radiusAccServerTable.setStatus('current')
radiusAccServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1), ).setIndexNames((0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"))
if mibBuilder.loadTexts: radiusAccServerEntry.setStatus('current')
radiusAccServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusAccServerIndex.setStatus('current')
radiusAccServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServerAddress.setStatus('current')
radiusAccClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientServerPortNumber.setStatus('current')
radiusAccClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientRoundTripTime.setStatus('current')
radiusAccClientRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientRequests.setStatus('current')
radiusAccClientRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientRetransmissions.setStatus('current')
radiusAccClientResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientResponses.setStatus('current')
radiusAccClientMalformedResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientMalformedResponses.setStatus('current')
radiusAccClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientBadAuthenticators.setStatus('current')
radiusAccClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientPendingRequests.setStatus('current')
radiusAccClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientTimeouts.setStatus('current')
radiusAccClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientUnknownTypes.setStatus('current')
radiusAccClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientPacketsDropped.setStatus('current')
radiusAccClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2))
radiusAccClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1))
radiusAccClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2))
radiusAccClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1, 1)).setObjects(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccClientMIBCompliance = radiusAccClientMIBCompliance.setStatus('current')
radiusAccClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 1)).setObjects(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientIdentifier"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientInvalidServerAddresses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRoundTripTime"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRequests"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRetransmissions"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientResponses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMalformedResponses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientBadAuthenticators"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPendingRequests"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientTimeouts"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientUnknownTypes"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccClientMIBGroup = radiusAccClientMIBGroup.setStatus('current')
mibBuilder.exportSymbols("RADIUS-ACC-CLIENT-MIB", radiusAccounting=radiusAccounting, radiusAccClientUnknownTypes=radiusAccClientUnknownTypes, radiusAccServerEntry=radiusAccServerEntry, radiusAccClientMIBGroups=radiusAccClientMIBGroups, radiusAccClientIdentifier=radiusAccClientIdentifier, radiusAccClientMIBObjects=radiusAccClientMIBObjects, radiusAccClientPacketsDropped=radiusAccClientPacketsDropped, radiusAccServerIndex=radiusAccServerIndex, radiusAccClientPendingRequests=radiusAccClientPendingRequests, radiusAccClientServerPortNumber=radiusAccClientServerPortNumber, radiusAccClientRequests=radiusAccClientRequests, radiusAccClientResponses=radiusAccClientResponses, radiusAccServerAddress=radiusAccServerAddress, radiusAccClientMIBCompliance=radiusAccClientMIBCompliance, radiusAccClientRetransmissions=radiusAccClientRetransmissions, radiusAccClientMIBConformance=radiusAccClientMIBConformance, radiusAccClientRoundTripTime=radiusAccClientRoundTripTime, radiusAccClient=radiusAccClient, radiusAccClientMIB=radiusAccClientMIB, radiusAccServerTable=radiusAccServerTable, PYSNMP_MODULE_ID=radiusAccClientMIB, radiusAccClientTimeouts=radiusAccClientTimeouts, radiusMIB=radiusMIB, radiusAccClientBadAuthenticators=radiusAccClientBadAuthenticators, radiusAccClientMIBGroup=radiusAccClientMIBGroup, radiusAccClientMIBCompliances=radiusAccClientMIBCompliances, radiusAccClientMalformedResponses=radiusAccClientMalformedResponses, radiusAccClientInvalidServerAddresses=radiusAccClientInvalidServerAddresses)
