#
# PySNMP MIB module SL-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RADIUS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:56 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, NotificationType, MibIdentifier, Counter64, Counter32, iso, Unsigned32, TimeTicks, Integer32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "NotificationType", "MibIdentifier", "Counter64", "Counter32", "iso", "Unsigned32", "TimeTicks", "Integer32", "ModuleIdentity", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
slRadiusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23))
if mibBuilder.loadTexts: slRadiusMIB.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: slRadiusMIB.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slRadiusMIB.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slRadiusMIB.setDescription('The MIB module for entities implementing the client side of\n         the Remote Access Dialin User Service (RADIUS) accounting\n         protocol.')
slRadiusClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1))
slRadiusClient = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1))
slRadiusTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 2))
class SharedSecret(TextualConvention, OctetString):
    description = 'Authentication Shared-Secret.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

slRadiusEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusEnabled.setStatus('current')
if mibBuilder.loadTexts: slRadiusEnabled.setDescription('true(1) - radius is enabled\n             false(2) - radius is disabled.')
slRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2), )
if mibBuilder.loadTexts: slRadiusServerTable.setStatus('current')
if mibBuilder.loadTexts: slRadiusServerTable.setDescription('The (conceptual) table listing the RADIUS accounting\n             servers with which the client shares a secret.')
slRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1), ).setIndexNames((0, "SL-RADIUS-MIB", "slRadiusServerIndex"))
if mibBuilder.loadTexts: slRadiusServerEntry.setStatus('current')
if mibBuilder.loadTexts: slRadiusServerEntry.setDescription('An entry (conceptual row) representing a RADIUS\n             accounting server with which the client shares a secret.')
slRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRadiusServerIndex.setStatus('current')
if mibBuilder.loadTexts: slRadiusServerIndex.setDescription('1 - Primary\n             2 - Secondary.')
slRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerAddress.setStatus('current')
if mibBuilder.loadTexts: slRadiusServerAddress.setDescription('The IP address of the RADIUS accounting server\n             referred to in this table entry.')
slRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerPort.setStatus('current')
if mibBuilder.loadTexts: slRadiusServerPort.setDescription('The port number of the server.')
slRadiusServerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerAdminStatus.setStatus('current')
if mibBuilder.loadTexts: slRadiusServerAdminStatus.setDescription('The admin status of the server.')
slRadiusTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusTimeout.setStatus('current')
if mibBuilder.loadTexts: slRadiusTimeout.setDescription('The server timeout specified in seconds. \n             The range is 1..30 seconds. The default is 15 seconds')
slRadiusSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 6), SharedSecret()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusSharedSecret.setStatus('current')
if mibBuilder.loadTexts: slRadiusSharedSecret.setDescription('The shared secret of the server.')
mibBuilder.exportSymbols("SL-RADIUS-MIB", PYSNMP_MODULE_ID=slRadiusMIB, slRadiusTimeout=slRadiusTimeout, slRadiusSharedSecret=slRadiusSharedSecret, slRadiusClient=slRadiusClient, slRadiusEnabled=slRadiusEnabled, slRadiusServerPort=slRadiusServerPort, slRadiusTraps=slRadiusTraps, slRadiusServerAddress=slRadiusServerAddress, slRadiusMIB=slRadiusMIB, slRadiusServerAdminStatus=slRadiusServerAdminStatus, slRadiusServerEntry=slRadiusServerEntry, slRadiusServerTable=slRadiusServerTable, slRadiusServerIndex=slRadiusServerIndex, slRadiusClientMIBObjects=slRadiusClientMIBObjects, SharedSecret=SharedSecret)
