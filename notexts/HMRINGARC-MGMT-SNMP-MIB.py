#
# PySNMP MIB module HMRINGARC-MGMT-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/hmARC
# Produced by pysmi-1.1.8 at Fri Jul  8 09:20:19 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hmRingRedundancy, = mibBuilder.importSymbols("HMRING-MGMT-SNMP-MIB", "hmRingRedundancy")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, NotificationType, IpAddress, Unsigned32, TimeTicks, Bits, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "NotificationType", "IpAddress", "Unsigned32", "TimeTicks", "Bits", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmARC = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 14, 5, 7))
hmARC.setRevisions(('2010-09-01 12:00',))
if mibBuilder.loadTexts: hmARC.setLastUpdated('201009011200Z')
if mibBuilder.loadTexts: hmARC.setOrganization('Hirschmann Automation and Control GmbH')
hmArcManagerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1))
hmArcManagerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2))
hmArcClientConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 3))
hmArcClientStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4))
hmArcManagerAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcManagerAdminStatus.setStatus('current')
hmArcManagerRedProtocol = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("mrp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcManagerRedProtocol.setStatus('current')
hmArcManagerPrimGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerPrimGroupID.setStatus('current')
hmArcManagerPrimIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerPrimIfIndex.setStatus('current')
hmArcManagerRedGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerRedGroupID.setStatus('current')
hmArcManagerRedIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerRedIfIndex.setStatus('current')
hmArcManagerVlanID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerVlanID.setStatus('current')
hmArcManagerAction = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("checkTopology", 2), ("configureRing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcManagerAction.setStatus('current')
hmArcManagerActionResult = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noAction", 1), ("pending", 2), ("closedRing", 3), ("configuredRing", 4), ("openRing", 5), ("invalidTopology", 6), ("configFailed", 7), ("configSuccessful", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerActionResult.setStatus('current')
hmArcCheckResultTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1), )
if mibBuilder.loadTexts: hmArcCheckResultTable.setStatus('current')
hmArcCheckResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1), ).setIndexNames((0, "HMRINGARC-MGMT-SNMP-MIB", "hmArcCheckStatusIndex"), (0, "HMRINGARC-MGMT-SNMP-MIB", "hmArcCheckStatusDeviceMac"))
if mibBuilder.loadTexts: hmArcCheckResultEntry.setStatus('current')
hmArcCheckStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusIndex.setStatus('current')
hmArcCheckStatusDeviceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusDeviceMac.setStatus('current')
hmArcCheckStatusDeviceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusDeviceIp.setStatus('current')
hmArcCheckStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("otherRm", 1), ("loop", 2), ("alreadyConfigured", 3), ("unsupportedOption", 4), ("openRing", 5), ("configFailed", 6), ("duplexMode", 7), ("noArcDevices", 8), ("portState", 9), ("info", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusType.setStatus('current')
hmArcCheckStatusInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusInfo.setStatus('current')
hmArcCheckStatusClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("ok", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusClassification.setStatus('current')
hmArcClientAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("checkOnly", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcClientAdminStatus.setStatus('current')
hmArcClientManagerDeviceMac = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientManagerDeviceMac.setStatus('current')
hmArcClientManagerDeviceIp = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientManagerDeviceIp.setStatus('current')
hmArcClientPrimGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientPrimGroupID.setStatus('current')
hmArcClientPrimIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientPrimIfIndex.setStatus('current')
hmArcClientRedGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientRedGroupID.setStatus('current')
hmArcClientRedIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientRedIfIndex.setStatus('current')
mibBuilder.exportSymbols("HMRINGARC-MGMT-SNMP-MIB", hmArcClientManagerDeviceIp=hmArcClientManagerDeviceIp, hmArcClientRedGroupID=hmArcClientRedGroupID, hmArcCheckStatusDeviceIp=hmArcCheckStatusDeviceIp, hmArcCheckStatusDeviceMac=hmArcCheckStatusDeviceMac, hmArcClientConfig=hmArcClientConfig, hmArcManagerConfig=hmArcManagerConfig, hmArcManagerPrimIfIndex=hmArcManagerPrimIfIndex, hmArcManagerAction=hmArcManagerAction, hmArcManagerActionResult=hmArcManagerActionResult, hmArcClientPrimIfIndex=hmArcClientPrimIfIndex, hmArcManagerAdminStatus=hmArcManagerAdminStatus, hmArcManagerRedProtocol=hmArcManagerRedProtocol, hmArcCheckStatusType=hmArcCheckStatusType, hmArcClientRedIfIndex=hmArcClientRedIfIndex, hmARC=hmARC, hmArcManagerPrimGroupID=hmArcManagerPrimGroupID, PYSNMP_MODULE_ID=hmARC, hmArcClientAdminStatus=hmArcClientAdminStatus, hmArcClientPrimGroupID=hmArcClientPrimGroupID, hmArcManagerVlanID=hmArcManagerVlanID, hmArcManagerRedGroupID=hmArcManagerRedGroupID, hmArcCheckStatusIndex=hmArcCheckStatusIndex, hmArcCheckStatusClassification=hmArcCheckStatusClassification, hmArcCheckStatusInfo=hmArcCheckStatusInfo, hmArcClientManagerDeviceMac=hmArcClientManagerDeviceMac, hmArcManagerStatus=hmArcManagerStatus, hmArcCheckResultEntry=hmArcCheckResultEntry, hmArcClientStatus=hmArcClientStatus, hmArcManagerRedIfIndex=hmArcManagerRedIfIndex, hmArcCheckResultTable=hmArcCheckResultTable)
