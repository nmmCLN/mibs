#
# PySNMP MIB module SL-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RADIUS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:33:08 2022
# On host fv-az130-744 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ModuleIdentity, iso, MibIdentifier, Gauge32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, TimeTicks, Unsigned32, NotificationType, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "iso", "MibIdentifier", "Gauge32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "TimeTicks", "Unsigned32", "NotificationType", "mib-2", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
slRadiusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23))
if mibBuilder.loadTexts: slRadiusMIB.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: slRadiusMIB.setOrganization('PacketLight Networks Ltd.')
slRadiusClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1))
slRadiusClient = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1))
slRadiusTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 2))
class SharedSecret(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

slRadiusEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusEnabled.setStatus('current')
slRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2), )
if mibBuilder.loadTexts: slRadiusServerTable.setStatus('current')
slRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1), ).setIndexNames((0, "SL-RADIUS-MIB", "slRadiusServerIndex"))
if mibBuilder.loadTexts: slRadiusServerEntry.setStatus('current')
slRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRadiusServerIndex.setStatus('current')
slRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerAddress.setStatus('current')
slRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerPort.setStatus('current')
slRadiusServerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerAdminStatus.setStatus('current')
slRadiusTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusTimeout.setStatus('current')
slRadiusSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 6), SharedSecret()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusSharedSecret.setStatus('current')
mibBuilder.exportSymbols("SL-RADIUS-MIB", slRadiusServerTable=slRadiusServerTable, slRadiusClientMIBObjects=slRadiusClientMIBObjects, slRadiusServerPort=slRadiusServerPort, slRadiusClient=slRadiusClient, SharedSecret=SharedSecret, slRadiusSharedSecret=slRadiusSharedSecret, slRadiusServerAddress=slRadiusServerAddress, slRadiusServerAdminStatus=slRadiusServerAdminStatus, PYSNMP_MODULE_ID=slRadiusMIB, slRadiusServerEntry=slRadiusServerEntry, slRadiusTimeout=slRadiusTimeout, slRadiusServerIndex=slRadiusServerIndex, slRadiusEnabled=slRadiusEnabled, slRadiusMIB=slRadiusMIB, slRadiusTraps=slRadiusTraps)
