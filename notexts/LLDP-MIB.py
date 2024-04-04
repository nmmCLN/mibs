#
# PySNMP MIB module LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/LLDP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:28 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
ZeroBasedCounter32, TimeFilter = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32", "TimeFilter")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, iso, Gauge32, MibIdentifier, ModuleIdentity, ObjectIdentity, Bits, Counter32, IpAddress, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "iso", "Gauge32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "IpAddress", "Unsigned32", "Integer32")
TimeStamp, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention", "TruthValue")
lldpMIB = ModuleIdentity((1, 0, 8802, 1, 1, 2))
lldpMIB.setRevisions(('2005-05-06 00:00',))
if mibBuilder.loadTexts: lldpMIB.setLastUpdated('200505060000Z')
if mibBuilder.loadTexts: lldpMIB.setOrganization('IEEE 802.1 Working Group')
lldpNotifications = MibIdentifier((1, 0, 8802, 1, 1, 2, 0))
lldpObjects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1))
lldpConformance = MibIdentifier((1, 0, 8802, 1, 1, 2, 2))
lldpConfiguration = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 1))
lldpStatistics = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 2))
lldpLocalSystemData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 3))
lldpRemoteSystemsData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 4))
lldpExtensions = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5))
class LldpChassisIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class LldpChassisId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpPortIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class LldpPortId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpManAddrIfSubtype(TextualConvention, Integer32):
    reference = 'IEEE 802.1AB-2005 9.5.9.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3))

class LldpManAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class LldpSystemCapabilitiesMap(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("other", 0), ("repeater", 1), ("bridge", 2), ("wlanAccessPoint", 3), ("router", 4), ("telephone", 5), ("docsisCableDevice", 6), ("stationOnly", 7))

class LldpPortNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4096)

class LldpPortList(TextualConvention, OctetString):
    reference = 'IETF RFC 2674 section 5'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

lldpMessageTxInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 32768)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpMessageTxInterval.setStatus('current')
lldpMessageTxHoldMultiplier = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpMessageTxHoldMultiplier.setStatus('current')
lldpReinitDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpReinitDelay.setStatus('current')
lldpTxDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)).clone(2)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpTxDelay.setStatus('current')
lldpNotificationInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpNotificationInterval.setStatus('current')
lldpPortConfigTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 6), )
if mibBuilder.loadTexts: lldpPortConfigTable.setStatus('current')
lldpPortConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1), ).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
if mibBuilder.loadTexts: lldpPortConfigEntry.setStatus('current')
lldpPortConfigPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpPortConfigPortNum.setStatus('current')
lldpPortConfigAdminStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4))).clone('txAndRx')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpPortConfigAdminStatus.setStatus('current')
lldpPortConfigNotificationEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpPortConfigNotificationEnable.setStatus('current')
lldpPortConfigTLVsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 4), Bits().clone(namedValues=NamedValues(("portDesc", 0), ("sysName", 1), ("sysDesc", 2), ("sysCap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpPortConfigTLVsTxEnable.setStatus('current')
lldpConfigManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 7), )
if mibBuilder.loadTexts: lldpConfigManAddrTable.setStatus('current')
lldpConfigManAddrPortsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1, 1), LldpPortList().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigManAddrPortsTxEnable.setStatus('current')
lldpStatsRemTablesLastChangeTime = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesLastChangeTime.setStatus('current')
lldpStatsRemTablesInserts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 2), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesInserts.setStatus('current')
lldpStatsRemTablesDeletes = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 3), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesDeletes.setStatus('current')
lldpStatsRemTablesDrops = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 4), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesDrops.setStatus('current')
lldpStatsRemTablesAgeouts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 5), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesAgeouts.setStatus('current')
lldpStatsTxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 6), )
if mibBuilder.loadTexts: lldpStatsTxPortTable.setStatus('current')
lldpStatsTxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1), ).setIndexNames((0, "LLDP-MIB", "lldpStatsTxPortNum"))
if mibBuilder.loadTexts: lldpStatsTxPortEntry.setStatus('current')
lldpStatsTxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpStatsTxPortNum.setStatus('current')
lldpStatsTxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsTxPortFramesTotal.setStatus('current')
lldpStatsRxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 7), )
if mibBuilder.loadTexts: lldpStatsRxPortTable.setStatus('current')
lldpStatsRxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1), ).setIndexNames((0, "LLDP-MIB", "lldpStatsRxPortNum"))
if mibBuilder.loadTexts: lldpStatsRxPortEntry.setStatus('current')
lldpStatsRxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpStatsRxPortNum.setStatus('current')
lldpStatsRxPortFramesDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortFramesDiscardedTotal.setStatus('current')
lldpStatsRxPortFramesErrors = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortFramesErrors.setStatus('current')
lldpStatsRxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortFramesTotal.setStatus('current')
lldpStatsRxPortTLVsDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortTLVsDiscardedTotal.setStatus('current')
lldpStatsRxPortTLVsUnrecognizedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortTLVsUnrecognizedTotal.setStatus('current')
lldpStatsRxPortAgeoutsTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortAgeoutsTotal.setStatus('current')
lldpLocChassisIdSubtype = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 1), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocChassisIdSubtype.setStatus('current')
lldpLocChassisId = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 2), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocChassisId.setStatus('current')
lldpLocSysName = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysName.setStatus('current')
lldpLocSysDesc = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysDesc.setStatus('current')
lldpLocSysCapSupported = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 5), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysCapSupported.setStatus('current')
lldpLocSysCapEnabled = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 6), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysCapEnabled.setStatus('current')
lldpLocPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 7), )
if mibBuilder.loadTexts: lldpLocPortTable.setStatus('current')
lldpLocPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpLocPortEntry.setStatus('current')
lldpLocPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpLocPortNum.setStatus('current')
lldpLocPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 2), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocPortIdSubtype.setStatus('current')
lldpLocPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 3), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocPortId.setStatus('current')
lldpLocPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocPortDesc.setStatus('current')
lldpLocManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 8), )
if mibBuilder.loadTexts: lldpLocManAddrTable.setStatus('current')
lldpLocManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocManAddrSubtype"), (0, "LLDP-MIB", "lldpLocManAddr"))
if mibBuilder.loadTexts: lldpLocManAddrEntry.setStatus('current')
lldpConfigManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1), )
lldpLocManAddrEntry.registerAugmentions(("LLDP-MIB", "lldpConfigManAddrEntry"))
lldpConfigManAddrEntry.setIndexNames(*lldpLocManAddrEntry.getIndexNames())
if mibBuilder.loadTexts: lldpConfigManAddrEntry.setStatus('current')
lldpLocManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: lldpLocManAddrSubtype.setStatus('current')
lldpLocManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 2), LldpManAddress())
if mibBuilder.loadTexts: lldpLocManAddr.setStatus('current')
lldpLocManAddrLen = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrLen.setStatus('current')
lldpLocManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 4), LldpManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrIfSubtype.setStatus('current')
lldpLocManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrIfId.setStatus('current')
lldpLocManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrOID.setStatus('current')
lldpRemTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 1), )
if mibBuilder.loadTexts: lldpRemTable.setStatus('current')
lldpRemEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpRemEntry.setStatus('current')
lldpRemTimeMark = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: lldpRemTimeMark.setStatus('current')
lldpRemLocalPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 2), LldpPortNumber())
if mibBuilder.loadTexts: lldpRemLocalPortNum.setStatus('current')
lldpRemIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpRemIndex.setStatus('current')
lldpRemChassisIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 4), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemChassisIdSubtype.setStatus('current')
lldpRemChassisId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 5), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemChassisId.setStatus('current')
lldpRemPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 6), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemPortIdSubtype.setStatus('current')
lldpRemPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 7), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemPortId.setStatus('current')
lldpRemPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemPortDesc.setStatus('current')
lldpRemSysName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysName.setStatus('current')
lldpRemSysDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysDesc.setStatus('current')
lldpRemSysCapSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 11), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysCapSupported.setStatus('current')
lldpRemSysCapEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 12), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysCapEnabled.setStatus('current')
lldpRemManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 2), )
if mibBuilder.loadTexts: lldpRemManAddrTable.setStatus('current')
lldpRemManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemManAddrSubtype"), (0, "LLDP-MIB", "lldpRemManAddr"))
if mibBuilder.loadTexts: lldpRemManAddrEntry.setStatus('current')
lldpRemManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: lldpRemManAddrSubtype.setStatus('current')
lldpRemManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 2), LldpManAddress())
if mibBuilder.loadTexts: lldpRemManAddr.setStatus('current')
lldpRemManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 3), LldpManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemManAddrIfSubtype.setStatus('current')
lldpRemManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemManAddrIfId.setStatus('current')
lldpRemManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemManAddrOID.setStatus('current')
lldpRemUnknownTLVTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 3), )
if mibBuilder.loadTexts: lldpRemUnknownTLVTable.setStatus('current')
lldpRemUnknownTLVEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemUnknownTLVType"))
if mibBuilder.loadTexts: lldpRemUnknownTLVEntry.setStatus('current')
lldpRemUnknownTLVType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(9, 126)))
if mibBuilder.loadTexts: lldpRemUnknownTLVType.setStatus('current')
lldpRemUnknownTLVInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemUnknownTLVInfo.setStatus('current')
lldpRemOrgDefInfoTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 4), )
if mibBuilder.loadTexts: lldpRemOrgDefInfoTable.setStatus('current')
lldpRemOrgDefInfoEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemOrgDefInfoOUI"), (0, "LLDP-MIB", "lldpRemOrgDefInfoSubtype"), (0, "LLDP-MIB", "lldpRemOrgDefInfoIndex"))
if mibBuilder.loadTexts: lldpRemOrgDefInfoEntry.setStatus('current')
lldpRemOrgDefInfoOUI = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3))
if mibBuilder.loadTexts: lldpRemOrgDefInfoOUI.setStatus('current')
lldpRemOrgDefInfoSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: lldpRemOrgDefInfoSubtype.setStatus('current')
lldpRemOrgDefInfoIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpRemOrgDefInfoIndex.setStatus('current')
lldpRemOrgDefInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 507))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemOrgDefInfo.setStatus('current')
lldpNotificationPrefix = MibIdentifier((1, 0, 8802, 1, 1, 2, 0, 0))
lldpRemTablesChange = NotificationType((1, 0, 8802, 1, 1, 2, 0, 0, 1)).setObjects(("LLDP-MIB", "lldpStatsRemTablesInserts"), ("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"))
if mibBuilder.loadTexts: lldpRemTablesChange.setStatus('current')
lldpCompliances = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 1))
lldpGroups = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 2))
lldpCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 2, 2, 1, 1)).setObjects(("LLDP-MIB", "lldpConfigGroup"), ("LLDP-MIB", "lldpConfigRxGroup"), ("LLDP-MIB", "lldpConfigTxGroup"), ("LLDP-MIB", "lldpStatsRxGroup"), ("LLDP-MIB", "lldpStatsTxGroup"), ("LLDP-MIB", "lldpLocSysGroup"), ("LLDP-MIB", "lldpRemSysGroup"), ("LLDP-MIB", "lldpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpCompliance = lldpCompliance.setStatus('current')
lldpConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 1)).setObjects(("LLDP-MIB", "lldpPortConfigAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpConfigGroup = lldpConfigGroup.setStatus('current')
lldpConfigRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 2)).setObjects(("LLDP-MIB", "lldpNotificationInterval"), ("LLDP-MIB", "lldpPortConfigNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpConfigRxGroup = lldpConfigRxGroup.setStatus('current')
lldpConfigTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 3)).setObjects(("LLDP-MIB", "lldpMessageTxInterval"), ("LLDP-MIB", "lldpMessageTxHoldMultiplier"), ("LLDP-MIB", "lldpReinitDelay"), ("LLDP-MIB", "lldpTxDelay"), ("LLDP-MIB", "lldpPortConfigTLVsTxEnable"), ("LLDP-MIB", "lldpConfigManAddrPortsTxEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpConfigTxGroup = lldpConfigTxGroup.setStatus('current')
lldpStatsRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 4)).setObjects(("LLDP-MIB", "lldpStatsRemTablesLastChangeTime"), ("LLDP-MIB", "lldpStatsRemTablesInserts"), ("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"), ("LLDP-MIB", "lldpStatsRxPortFramesDiscardedTotal"), ("LLDP-MIB", "lldpStatsRxPortFramesErrors"), ("LLDP-MIB", "lldpStatsRxPortFramesTotal"), ("LLDP-MIB", "lldpStatsRxPortTLVsDiscardedTotal"), ("LLDP-MIB", "lldpStatsRxPortTLVsUnrecognizedTotal"), ("LLDP-MIB", "lldpStatsRxPortAgeoutsTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpStatsRxGroup = lldpStatsRxGroup.setStatus('current')
lldpStatsTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 5)).setObjects(("LLDP-MIB", "lldpStatsTxPortFramesTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpStatsTxGroup = lldpStatsTxGroup.setStatus('current')
lldpLocSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 6)).setObjects(("LLDP-MIB", "lldpLocChassisIdSubtype"), ("LLDP-MIB", "lldpLocChassisId"), ("LLDP-MIB", "lldpLocPortIdSubtype"), ("LLDP-MIB", "lldpLocPortId"), ("LLDP-MIB", "lldpLocPortDesc"), ("LLDP-MIB", "lldpLocSysDesc"), ("LLDP-MIB", "lldpLocSysName"), ("LLDP-MIB", "lldpLocSysCapSupported"), ("LLDP-MIB", "lldpLocSysCapEnabled"), ("LLDP-MIB", "lldpLocManAddrLen"), ("LLDP-MIB", "lldpLocManAddrIfSubtype"), ("LLDP-MIB", "lldpLocManAddrIfId"), ("LLDP-MIB", "lldpLocManAddrOID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpLocSysGroup = lldpLocSysGroup.setStatus('current')
lldpRemSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 7)).setObjects(("LLDP-MIB", "lldpRemChassisIdSubtype"), ("LLDP-MIB", "lldpRemChassisId"), ("LLDP-MIB", "lldpRemPortIdSubtype"), ("LLDP-MIB", "lldpRemPortId"), ("LLDP-MIB", "lldpRemPortDesc"), ("LLDP-MIB", "lldpRemSysName"), ("LLDP-MIB", "lldpRemSysDesc"), ("LLDP-MIB", "lldpRemSysCapSupported"), ("LLDP-MIB", "lldpRemSysCapEnabled"), ("LLDP-MIB", "lldpRemManAddrIfSubtype"), ("LLDP-MIB", "lldpRemManAddrIfId"), ("LLDP-MIB", "lldpRemManAddrOID"), ("LLDP-MIB", "lldpRemUnknownTLVInfo"), ("LLDP-MIB", "lldpRemOrgDefInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpRemSysGroup = lldpRemSysGroup.setStatus('current')
lldpNotificationsGroup = NotificationGroup((1, 0, 8802, 1, 1, 2, 2, 2, 8)).setObjects(("LLDP-MIB", "lldpRemTablesChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpNotificationsGroup = lldpNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("LLDP-MIB", lldpRemUnknownTLVEntry=lldpRemUnknownTLVEntry, lldpLocManAddr=lldpLocManAddr, LldpPortList=LldpPortList, lldpRemIndex=lldpRemIndex, lldpRemSysName=lldpRemSysName, lldpStatsRxPortTable=lldpStatsRxPortTable, lldpRemSysCapEnabled=lldpRemSysCapEnabled, lldpNotifications=lldpNotifications, lldpStatsRxGroup=lldpStatsRxGroup, lldpRemOrgDefInfoEntry=lldpRemOrgDefInfoEntry, lldpGroups=lldpGroups, lldpObjects=lldpObjects, lldpLocalSystemData=lldpLocalSystemData, lldpConfigTxGroup=lldpConfigTxGroup, lldpConfigRxGroup=lldpConfigRxGroup, lldpLocManAddrLen=lldpLocManAddrLen, PYSNMP_MODULE_ID=lldpMIB, lldpStatistics=lldpStatistics, lldpRemPortIdSubtype=lldpRemPortIdSubtype, lldpPortConfigTLVsTxEnable=lldpPortConfigTLVsTxEnable, lldpRemOrgDefInfoIndex=lldpRemOrgDefInfoIndex, lldpStatsRxPortNum=lldpStatsRxPortNum, lldpRemManAddr=lldpRemManAddr, lldpNotificationsGroup=lldpNotificationsGroup, lldpRemManAddrIfId=lldpRemManAddrIfId, LldpChassisId=LldpChassisId, lldpStatsRxPortFramesTotal=lldpStatsRxPortFramesTotal, lldpRemOrgDefInfoTable=lldpRemOrgDefInfoTable, lldpRemManAddrEntry=lldpRemManAddrEntry, lldpRemManAddrSubtype=lldpRemManAddrSubtype, lldpStatsRemTablesAgeouts=lldpStatsRemTablesAgeouts, lldpStatsRxPortTLVsDiscardedTotal=lldpStatsRxPortTLVsDiscardedTotal, lldpStatsRxPortFramesDiscardedTotal=lldpStatsRxPortFramesDiscardedTotal, LldpManAddress=LldpManAddress, lldpMessageTxInterval=lldpMessageTxInterval, lldpRemOrgDefInfoSubtype=lldpRemOrgDefInfoSubtype, lldpRemUnknownTLVInfo=lldpRemUnknownTLVInfo, lldpLocPortNum=lldpLocPortNum, lldpRemTimeMark=lldpRemTimeMark, lldpCompliances=lldpCompliances, lldpLocManAddrIfId=lldpLocManAddrIfId, LldpSystemCapabilitiesMap=LldpSystemCapabilitiesMap, lldpRemManAddrOID=lldpRemManAddrOID, lldpStatsTxPortEntry=lldpStatsTxPortEntry, lldpReinitDelay=lldpReinitDelay, lldpLocPortTable=lldpLocPortTable, lldpRemOrgDefInfo=lldpRemOrgDefInfo, LldpPortNumber=LldpPortNumber, lldpLocManAddrIfSubtype=lldpLocManAddrIfSubtype, lldpStatsRemTablesDeletes=lldpStatsRemTablesDeletes, lldpConfigManAddrEntry=lldpConfigManAddrEntry, lldpStatsRxPortEntry=lldpStatsRxPortEntry, lldpConformance=lldpConformance, LldpChassisIdSubtype=LldpChassisIdSubtype, lldpLocManAddrOID=lldpLocManAddrOID, lldpStatsRxPortFramesErrors=lldpStatsRxPortFramesErrors, lldpPortConfigNotificationEnable=lldpPortConfigNotificationEnable, lldpStatsTxPortFramesTotal=lldpStatsTxPortFramesTotal, lldpStatsRemTablesInserts=lldpStatsRemTablesInserts, lldpLocPortIdSubtype=lldpLocPortIdSubtype, lldpRemSysCapSupported=lldpRemSysCapSupported, lldpStatsRemTablesLastChangeTime=lldpStatsRemTablesLastChangeTime, lldpRemPortDesc=lldpRemPortDesc, lldpStatsTxPortNum=lldpStatsTxPortNum, lldpRemTable=lldpRemTable, lldpRemManAddrIfSubtype=lldpRemManAddrIfSubtype, lldpRemChassisIdSubtype=lldpRemChassisIdSubtype, lldpMIB=lldpMIB, lldpLocManAddrSubtype=lldpLocManAddrSubtype, lldpStatsTxPortTable=lldpStatsTxPortTable, LldpPortIdSubtype=LldpPortIdSubtype, lldpRemTablesChange=lldpRemTablesChange, lldpPortConfigEntry=lldpPortConfigEntry, lldpConfigManAddrPortsTxEnable=lldpConfigManAddrPortsTxEnable, lldpStatsRxPortTLVsUnrecognizedTotal=lldpStatsRxPortTLVsUnrecognizedTotal, lldpRemEntry=lldpRemEntry, lldpStatsRxPortAgeoutsTotal=lldpStatsRxPortAgeoutsTotal, lldpPortConfigTable=lldpPortConfigTable, lldpLocSysDesc=lldpLocSysDesc, lldpLocChassisIdSubtype=lldpLocChassisIdSubtype, lldpLocPortDesc=lldpLocPortDesc, lldpConfiguration=lldpConfiguration, lldpStatsRemTablesDrops=lldpStatsRemTablesDrops, lldpLocSysName=lldpLocSysName, lldpLocPortId=lldpLocPortId, lldpLocChassisId=lldpLocChassisId, lldpRemUnknownTLVType=lldpRemUnknownTLVType, lldpPortConfigAdminStatus=lldpPortConfigAdminStatus, lldpPortConfigPortNum=lldpPortConfigPortNum, lldpRemPortId=lldpRemPortId, lldpRemChassisId=lldpRemChassisId, lldpRemSysDesc=lldpRemSysDesc, lldpLocPortEntry=lldpLocPortEntry, lldpConfigGroup=lldpConfigGroup, lldpRemLocalPortNum=lldpRemLocalPortNum, lldpMessageTxHoldMultiplier=lldpMessageTxHoldMultiplier, lldpRemOrgDefInfoOUI=lldpRemOrgDefInfoOUI, lldpRemSysGroup=lldpRemSysGroup, lldpStatsTxGroup=lldpStatsTxGroup, lldpConfigManAddrTable=lldpConfigManAddrTable, lldpNotificationInterval=lldpNotificationInterval, lldpLocSysGroup=lldpLocSysGroup, lldpLocSysCapSupported=lldpLocSysCapSupported, LldpPortId=LldpPortId, lldpExtensions=lldpExtensions, lldpCompliance=lldpCompliance, lldpRemManAddrTable=lldpRemManAddrTable, lldpRemoteSystemsData=lldpRemoteSystemsData, lldpLocSysCapEnabled=lldpLocSysCapEnabled, LldpManAddrIfSubtype=LldpManAddrIfSubtype, lldpLocManAddrTable=lldpLocManAddrTable, lldpRemUnknownTLVTable=lldpRemUnknownTLVTable, lldpTxDelay=lldpTxDelay, lldpNotificationPrefix=lldpNotificationPrefix, lldpLocManAddrEntry=lldpLocManAddrEntry)
