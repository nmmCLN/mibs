#
# PySNMP MIB module EQL-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQL-LLDP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ObjectIdentity, IpAddress, Counter64, Counter32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, MibIdentifier, NotificationType, iso, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "IpAddress", "Counter64", "Counter32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "MibIdentifier", "NotificationType", "iso", "Bits", "ModuleIdentity")
TruthValue, DisplayString, MacAddress, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "MacAddress", "TextualConvention", "TimeInterval")
eqlLldpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 21))
eqlLldpMib.setRevisions(('2010-07-23 00:00',))
if mibBuilder.loadTexts: eqlLldpMib.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlLldpMib.setOrganization('EqualLogic Inc.')
eqlLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 21, 1))
class EqlLldpV2ChassisIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class EqlLldpV2ChassisId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(255, 255)
    fixedLength = 255

class EqlLldpV2PortIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class EqlLldpV2PortId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class EqlLldpV2State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("off", 0), ("noPeer", 1), ("active", 2), ("multiplePeers", 3))

eqlLldpDynamicIfTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1), )
if mibBuilder.loadTexts: eqlLldpDynamicIfTable.setStatus('current')
eqlLldpDynamicIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eqlLldpDynamicIfEntry.setStatus('current')
eqlLldpRemMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpRemMacAddress.setStatus('current')
eqlLldpV2RemChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 2), EqlLldpV2ChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisIdSubtype.setStatus('current')
eqlLldpV2RemChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 3), EqlLldpV2ChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisId.setStatus('current')
eqlLldpV2RemPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 4), EqlLldpV2PortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortIdSubtype.setStatus('current')
eqlLldpV2RemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 5), EqlLldpV2PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortId.setStatus('current')
eqlLldpV2RemPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortDesc.setStatus('current')
eqlLldpV2RemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysName.setStatus('current')
eqlLldpV2RemSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysDesc.setStatus('current')
eqlLldpV2State = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 9), EqlLldpV2State()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2State.setStatus('current')
eqlLldpV2RemMgmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemMgmtAddr.setStatus('current')
mibBuilder.exportSymbols("EQL-LLDP-MIB", eqlLldpDynamicIfEntry=eqlLldpDynamicIfEntry, EqlLldpV2State=EqlLldpV2State, eqlLldpV2RemPortId=eqlLldpV2RemPortId, eqlLldpDynamicIfTable=eqlLldpDynamicIfTable, eqlLldpMIBObjects=eqlLldpMIBObjects, eqlLldpV2RemChassisIdSubtype=eqlLldpV2RemChassisIdSubtype, PYSNMP_MODULE_ID=eqlLldpMib, eqlLldpV2RemSysDesc=eqlLldpV2RemSysDesc, eqlLldpV2RemMgmtAddr=eqlLldpV2RemMgmtAddr, eqlLldpV2RemSysName=eqlLldpV2RemSysName, EqlLldpV2ChassisId=EqlLldpV2ChassisId, eqlLldpV2RemPortIdSubtype=eqlLldpV2RemPortIdSubtype, eqlLldpV2State=eqlLldpV2State, eqlLldpMib=eqlLldpMib, EqlLldpV2PortIdSubtype=EqlLldpV2PortIdSubtype, eqlLldpRemMacAddress=eqlLldpRemMacAddress, EqlLldpV2ChassisIdSubtype=EqlLldpV2ChassisIdSubtype, EqlLldpV2PortId=EqlLldpV2PortId, eqlLldpV2RemChassisId=eqlLldpV2RemChassisId, eqlLldpV2RemPortDesc=eqlLldpV2RemPortDesc)
