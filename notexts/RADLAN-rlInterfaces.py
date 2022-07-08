#
# PySNMP MIB module RADLAN-rlInterfaces (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-rlInterfaces
# Produced by pysmi-1.1.8 at Fri Jul  8 09:27:00 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rlIfInterfaces, swInterfaces = mibBuilder.importSymbols("RADLAN-MIB", "rlIfInterfaces", "swInterfaces")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, MibIdentifier, Counter32, Integer32, Bits, Unsigned32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "Bits", "Unsigned32", "IpAddress", "ModuleIdentity")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
class AutoNegCapabilitiesBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("default", 0), ("unknown", 1), ("tenHalf", 2), ("tenFull", 3), ("fastHalf", 4), ("fastFull", 5), ("gigaHalf", 6), ("gigaFull", 7))

swIfTable = MibTable((1, 3, 6, 1, 4, 1, 89, 43, 1), )
if mibBuilder.loadTexts: swIfTable.setStatus('current')
swIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 43, 1, 1), ).setIndexNames((0, "RADLAN-rlInterfaces", "swIfIndex"))
if mibBuilder.loadTexts: swIfEntry.setStatus('current')
swIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfIndex.setStatus('current')
swIfPhysAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("reserve", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPhysAddressType.setStatus('obsolete')
swIfDuplexAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("half", 2), ("full", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfDuplexAdminMode.setStatus('current')
swIfDuplexOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("hybrid", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfDuplexOperMode.setStatus('current')
swIfBackPressureMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfBackPressureMode.setStatus('current')
swIfTaggedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfTaggedMode.setStatus('current')
swIfTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("regular", 1), ("fiberOptics", 2), ("comboRegular", 3), ("comboFiberOptics", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfTransceiverType.setStatus('current')
swIfLockAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2))).clone('unlocked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockAdminStatus.setStatus('current')
swIfLockOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfLockOperStatus.setStatus('current')
swIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("eth10M", 1), ("eth100M", 2), ("eth1000M", 3), ("eth10G", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfType.setStatus('current')
swIfDefaultTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfDefaultTag.setStatus('current')
swIfDefaultPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfDefaultPriority.setStatus('current')
swIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfStatus.setStatus('current')
swIfFlowControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("autoNegotiation", 3), ("enabledRx", 4), ("enabledTx", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfFlowControlMode.setStatus('current')
swIfSpeedAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSpeedAdminMode.setStatus('current')
swIfSpeedDuplexAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSpeedDuplexAutoNegotiation.setStatus('current')
swIfOperFlowControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("enabledRx", 3), ("enabledTx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperFlowControlMode.setStatus('current')
swIfOperSpeedDuplexAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("hybrid", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperSpeedDuplexAutoNegotiation.setStatus('current')
swIfOperBackPressureMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("hybrid", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperBackPressureMode.setStatus('current')
swIfAdminLockAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminLockAction.setStatus('current')
swIfOperLockAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperLockAction.setStatus('current')
swIfAdminLockTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 22), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminLockTrapEnable.setStatus('current')
swIfOperLockTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 23), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperLockTrapEnable.setStatus('current')
swIfOperSuspendedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperSuspendedStatus.setStatus('current')
swIfLockOperTrapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfLockOperTrapCount.setStatus('current')
swIfLockAdminTrapFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockAdminTrapFrequency.setStatus('current')
swIfReActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 27), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfReActivate.setStatus('current')
swIfAdminMdix = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cross", 1), ("normal", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminMdix.setStatus('current')
swIfOperMdix = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cross", 1), ("normal", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperMdix.setStatus('current')
swIfHostMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("single", 1), ("multiple", 2))).clone('single')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfHostMode.setStatus('current')
swIfSingleHostViolationAdminAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSingleHostViolationAdminAction.setStatus('current')
swIfSingleHostViolationOperAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3))).clone('discard')).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSingleHostViolationOperAction.setStatus('current')
swIfSingleHostViolationAdminTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 33), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSingleHostViolationAdminTrapEnable.setStatus('current')
swIfSingleHostViolationOperTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 34), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSingleHostViolationOperTrapEnable.setStatus('current')
swIfSingleHostViolationOperTrapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 35), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSingleHostViolationOperTrapCount.setStatus('current')
swIfSingleHostViolationAdminTrapFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSingleHostViolationAdminTrapFrequency.setStatus('current')
swIfLockLimitationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("dynamic", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockLimitationMode.setStatus('current')
swIfLockMaxMacAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockMaxMacAddresses.setStatus('current')
swIfLockMacAddressesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 39), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfLockMacAddressesCount.setStatus('current')
swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 40), AutoNegCapabilitiesBits().clone(namedValues=NamedValues(("default", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities.setStatus('current')
swIfOperSpeedDuplexAutoNegotiationLocalCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 41), AutoNegCapabilitiesBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperSpeedDuplexAutoNegotiationLocalCapabilities.setStatus('current')
swIfSpeedDuplexNegotiationRemoteCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 42), AutoNegCapabilitiesBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSpeedDuplexNegotiationRemoteCapabilities.setStatus('current')
swIfAdminComboMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("force-fiber", 1), ("force-copper", 2), ("prefer-fiber", 3), ("prefer-copper", 4))).clone('prefer-fiber')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminComboMode.setStatus('current')
swIfOperComboMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 1, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fiber", 1), ("copper", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperComboMode.setStatus('current')
swIfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 43, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfMibVersion.setStatus('current')
swIfPortLockSupport = MibScalar((1, 3, 6, 1, 4, 1, 89, 43, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockSupport.setStatus('current')
swIfPortLockActionSupport = MibScalar((1, 3, 6, 1, 4, 1, 89, 43, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockActionSupport.setStatus('current')
swIfPortLockTrapSupport = MibScalar((1, 3, 6, 1, 4, 1, 89, 43, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockTrapSupport.setStatus('current')
swIfPortLockIfRangeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 43, 6), )
if mibBuilder.loadTexts: swIfPortLockIfRangeTable.setStatus('current')
swIfPortLockIfRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 43, 6, 1), ).setIndexNames((0, "RADLAN-rlInterfaces", "swIfPortLockIfRangeIndex"))
if mibBuilder.loadTexts: swIfPortLockIfRangeEntry.setStatus('current')
swIfPortLockIfRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockIfRangeIndex.setStatus('current')
swIfPortLockIfRange = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 6, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRange.setStatus('current')
swIfPortLockIfRangeLockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2))).clone('unlocked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeLockStatus.setStatus('current')
swIfPortLockIfRangeAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeAction.setStatus('current')
swIfPortLockIfRangeTrapEn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 6, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeTrapEn.setStatus('current')
swIfPortLockIfRangeTrapFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeTrapFreq.setStatus('current')
swIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 43, 7), )
if mibBuilder.loadTexts: swIfExtTable.setStatus('current')
swIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 43, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: swIfExtEntry.setStatus('current')
swIfExtSFPSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 43, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("eth100M", 2), ("eth1G", 3))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfExtSFPSpeed.setStatus('current')
rlIfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfMibVersion.setStatus('current')
rlIfNumOfPhPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfNumOfPhPorts.setStatus('current')
rlIfMapOfOnPhPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfMapOfOnPhPorts.setStatus('current')
rlIfClearPortMibCounters = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfClearPortMibCounters.setStatus('current')
rlIfNumOfUserDefinedPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfNumOfUserDefinedPorts.setStatus('current')
rlIfFirstOutOfBandIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfFirstOutOfBandIfIndex.setStatus('current')
rlIfNumOfLoopbackPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfNumOfLoopbackPorts.setStatus('current')
rlIfFirstLoopbackIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfFirstLoopbackIfIndex.setStatus('current')
rlIfExistingPortList = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 9), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfExistingPortList.setStatus('current')
rlIfBaseMACAddressPerIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfBaseMACAddressPerIfIndex.setStatus('current')
rlFlowControlCascadeMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFlowControlCascadeMode.setStatus('current')
rlFlowControlCascadeType = MibScalar((1, 3, 6, 1, 4, 1, 89, 54, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internalonly", 1), ("internalexternal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFlowControlCascadeType.setStatus('current')
mibBuilder.exportSymbols("RADLAN-rlInterfaces", swIfAdminMdix=swIfAdminMdix, rlIfFirstOutOfBandIfIndex=rlIfFirstOutOfBandIfIndex, swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities=swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities, swIfPortLockActionSupport=swIfPortLockActionSupport, swIfOperLockAction=swIfOperLockAction, swIfSingleHostViolationOperAction=swIfSingleHostViolationOperAction, swIfSpeedDuplexAutoNegotiation=swIfSpeedDuplexAutoNegotiation, AutoNegCapabilitiesBits=AutoNegCapabilitiesBits, swIfTaggedMode=swIfTaggedMode, rlIfClearPortMibCounters=rlIfClearPortMibCounters, swIfAdminLockTrapEnable=swIfAdminLockTrapEnable, rlIfNumOfLoopbackPorts=rlIfNumOfLoopbackPorts, swIfSingleHostViolationAdminAction=swIfSingleHostViolationAdminAction, swIfPortLockIfRange=swIfPortLockIfRange, swIfType=swIfType, rlIfMibVersion=rlIfMibVersion, swIfLockMaxMacAddresses=swIfLockMaxMacAddresses, swIfDuplexAdminMode=swIfDuplexAdminMode, swIfTransceiverType=swIfTransceiverType, swIfPortLockSupport=swIfPortLockSupport, swIfPortLockIfRangeTable=swIfPortLockIfRangeTable, rlIfNumOfUserDefinedPorts=rlIfNumOfUserDefinedPorts, swIfStatus=swIfStatus, swIfAdminLockAction=swIfAdminLockAction, swIfOperMdix=swIfOperMdix, swIfOperFlowControlMode=swIfOperFlowControlMode, swIfOperSpeedDuplexAutoNegotiationLocalCapabilities=swIfOperSpeedDuplexAutoNegotiationLocalCapabilities, swIfPortLockIfRangeIndex=swIfPortLockIfRangeIndex, swIfPortLockIfRangeAction=swIfPortLockIfRangeAction, swIfLockAdminStatus=swIfLockAdminStatus, swIfReActivate=swIfReActivate, swIfLockAdminTrapFrequency=swIfLockAdminTrapFrequency, swIfDuplexOperMode=swIfDuplexOperMode, swIfPortLockTrapSupport=swIfPortLockTrapSupport, swIfSingleHostViolationAdminTrapFrequency=swIfSingleHostViolationAdminTrapFrequency, swIfOperLockTrapEnable=swIfOperLockTrapEnable, swIfOperComboMode=swIfOperComboMode, swIfAdminComboMode=swIfAdminComboMode, swIfPortLockIfRangeTrapEn=swIfPortLockIfRangeTrapEn, swIfMibVersion=swIfMibVersion, rlIfMapOfOnPhPorts=rlIfMapOfOnPhPorts, swIfTable=swIfTable, swIfLockOperStatus=swIfLockOperStatus, swIfExtEntry=swIfExtEntry, rlFlowControlCascadeMode=rlFlowControlCascadeMode, swIfLockOperTrapCount=swIfLockOperTrapCount, swIfIndex=swIfIndex, swIfSpeedAdminMode=swIfSpeedAdminMode, swIfDefaultPriority=swIfDefaultPriority, swIfLockLimitationMode=swIfLockLimitationMode, swIfPortLockIfRangeLockStatus=swIfPortLockIfRangeLockStatus, rlIfBaseMACAddressPerIfIndex=rlIfBaseMACAddressPerIfIndex, swIfDefaultTag=swIfDefaultTag, swIfEntry=swIfEntry, swIfOperSpeedDuplexAutoNegotiation=swIfOperSpeedDuplexAutoNegotiation, swIfExtTable=swIfExtTable, swIfBackPressureMode=swIfBackPressureMode, swIfHostMode=swIfHostMode, swIfPhysAddressType=swIfPhysAddressType, swIfSingleHostViolationAdminTrapEnable=swIfSingleHostViolationAdminTrapEnable, swIfSingleHostViolationOperTrapEnable=swIfSingleHostViolationOperTrapEnable, swIfPortLockIfRangeEntry=swIfPortLockIfRangeEntry, swIfSpeedDuplexNegotiationRemoteCapabilities=swIfSpeedDuplexNegotiationRemoteCapabilities, swIfSingleHostViolationOperTrapCount=swIfSingleHostViolationOperTrapCount, swIfOperBackPressureMode=swIfOperBackPressureMode, rlFlowControlCascadeType=rlFlowControlCascadeType, swIfOperSuspendedStatus=swIfOperSuspendedStatus, swIfPortLockIfRangeTrapFreq=swIfPortLockIfRangeTrapFreq, swIfExtSFPSpeed=swIfExtSFPSpeed, rlIfNumOfPhPorts=rlIfNumOfPhPorts, rlIfExistingPortList=rlIfExistingPortList, swIfLockMacAddressesCount=swIfLockMacAddressesCount, swIfFlowControlMode=swIfFlowControlMode, rlIfFirstLoopbackIfIndex=rlIfFirstLoopbackIfIndex)
