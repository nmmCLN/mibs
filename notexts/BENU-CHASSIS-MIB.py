#
# PySNMP MIB module BENU-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:19 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ifOperStatus, ifDescr, ifAdminStatus, ifType, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifOperStatus", "ifDescr", "ifAdminStatus", "ifType", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, ObjectIdentity, TimeTicks, Gauge32, NotificationType, Counter32, iso, Bits, Unsigned32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Gauge32", "NotificationType", "Counter32", "iso", "Bits", "Unsigned32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 1))
benuChassisMIB.setRevisions(('2016-11-18 00:00', '2016-10-14 00:00', '2016-01-26 00:00', '2015-10-14 00:00', '2015-01-27 00:00', '2015-01-05 00:00', '2014-11-14 00:00', '2014-06-27 00:00', '2013-11-25 00:00', '2012-12-12 00:00',))
if mibBuilder.loadTexts: benuChassisMIB.setLastUpdated('201611180000Z')
if mibBuilder.loadTexts: benuChassisMIB.setOrganization('Benu Networks')
benuChassisMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1))
benuChassisNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0))
benuChassisNotifVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 2))
benuChassisInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1))
benuCardInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2))
benuCardIfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3))
benuSensorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4))
benuChassisGeneralInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 5))
benuFanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6))
benuPowerSupplyInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7))
benuChassisType = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meg100", 1), ("meg400", 2), ("meg1200", 3), ("meg50", 4), ("xMEG100", 5), ("xMEG10", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuChassisType.setStatus('current')
benuChassisHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuChassisHwVersion.setStatus('current')
benuChassisId = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuChassisId.setStatus('current')
benuChassisNumOfSlots = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuChassisNumOfSlots.setStatus('current')
benuChassisPowerTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: benuChassisPowerTrapEnable.setStatus('current')
benuChassisFanTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: benuChassisFanTrapEnable.setStatus('current')
benuChassisSensorTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: benuChassisSensorTrapEnable.setStatus('current')
benuSysUpTimeAtLastChassisChange = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSysUpTimeAtLastChassisChange.setStatus('current')
benuCardTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: benuCardTable.setStatus('current')
benuCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "BENU-CHASSIS-MIB", "benuCardIndex"))
if mibBuilder.loadTexts: benuCardEntry.setStatus('current')
benuCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: benuCardIndex.setStatus('current')
benuCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("rsm", 1), ("switchFabric", 2), ("shelfmgr", 3), ("seFP", 4), ("inputOutputCard", 5), ("switchMesh", 6), ("xmeg", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardType.setStatus('current')
benuCardDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardDescr.setStatus('current')
benuCardSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardSerial.setStatus('current')
benuCardPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardPartNumber.setStatus('current')
benuCardHwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardHwVersion.setStatus('current')
benuCardSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardSwVersion.setStatus('current')
benuCardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardSlotNumber.setStatus('current')
benuCardRamSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardRamSize.setStatus('current')
benuCardPrimaryDiskSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardPrimaryDiskSize.setStatus('current')
benuCardSecondaryDiskSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardSecondaryDiskSize.setStatus('current')
benuCardOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("notSpecified", 1), ("up", 2), ("down", 3), ("standby", 4), ("rom", 5), ("flash", 6), ("diag", 7), ("boot", 8), ("config", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardOperStatus.setStatus('current')
benuCardIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: benuCardIfIndexTable.setStatus('current')
benuCardIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "BENU-CHASSIS-MIB", "benuCardIfIndex"))
if mibBuilder.loadTexts: benuCardIfIndexEntry.setStatus('current')
benuCardIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: benuCardIfIndex.setStatus('current')
benuCardIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardIfName.setStatus('current')
benuCardIfPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardIfPortNumber.setStatus('current')
benuCardIfSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardIfSlotNumber.setStatus('current')
benuCardIfLinkUpDownEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: benuCardIfLinkUpDownEnable.setStatus('current')
benuCardIfPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("none", 0), ("ethernet", 1), ("fastEthernet", 2), ("gigaEthernet", 3), ("tunnel", 4), ("ipGre", 5), ("vlan", 6), ("l2tp", 7), ("cable", 8), ("bridge", 9), ("ip", 10), ("multiBind", 11), ("p2p", 12), ("loopback", 13), ("multiBindLastResort", 14), ("lag", 15), ("max", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardIfPortType.setStatus('current')
benuCardIfBindName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardIfBindName.setStatus('current')
benuCardIfEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardIfEncapsulation.setStatus('current')
benuCardIfVirtualType = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("physical", 1), ("virtual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuCardIfVirtualType.setStatus('current')
benuSensorTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1), )
if mibBuilder.loadTexts: benuSensorTable.setStatus('current')
benuSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1), ).setIndexNames((0, "BENU-CHASSIS-MIB", "benuSensorCardIndex"), (0, "BENU-CHASSIS-MIB", "benuSensorIndex"))
if mibBuilder.loadTexts: benuSensorEntry.setStatus('current')
benuSensorCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: benuSensorCardIndex.setStatus('current')
benuSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: benuSensorIndex.setStatus('current')
benuSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSensorName.setStatus('current')
benuSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 0), ("temparature", 1), ("voltage", 2), ("electicCurrent", 3), ("fan", 4), ("power", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSensorType.setStatus('current')
benuSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSensorValue.setStatus('current')
benuSensorMinThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSensorMinThresh.setStatus('current')
benuSensorMaxThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSensorMaxThresh.setStatus('current')
benuSensorState = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("other", 0), ("normal", 1), ("critical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSensorState.setStatus('current')
benuSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSensorId.setStatus('current')
benuFanTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1), )
if mibBuilder.loadTexts: benuFanTable.setStatus('current')
benuFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1), ).setIndexNames((0, "BENU-CHASSIS-MIB", "benuFanCardIndex"))
if mibBuilder.loadTexts: benuFanEntry.setStatus('current')
benuFanCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: benuFanCardIndex.setStatus('current')
benuFanMaxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuFanMaxSpeed.setStatus('current')
benuFanCurSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuFanCurSpeed.setStatus('current')
benuFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuFanStatus.setStatus('current')
benuPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1), )
if mibBuilder.loadTexts: benuPowerSupplyTable.setStatus('current')
benuPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1), ).setIndexNames((0, "BENU-CHASSIS-MIB", "benuPowerSupplyIndex"))
if mibBuilder.loadTexts: benuPowerSupplyEntry.setStatus('current')
benuPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerA", 1), ("powerB", 2))))
if mibBuilder.loadTexts: benuPowerSupplyIndex.setStatus('current')
benuPowerSupplyName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuPowerSupplyName.setStatus('current')
benuPowerSupplyPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuPowerSupplyPresent.setStatus('current')
benuPowerSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ac", 1), ("dc", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuPowerSupplyType.setStatus('current')
benuPowerSupplyPowered = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("powered", 1), ("notPowered", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuPowerSupplyPowered.setStatus('current')
benuSysUpTimeSinceLastConfigChange = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 5, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: benuSysUpTimeSinceLastConfigChange.setStatus('current')
benuChassisPowerFailureInfo = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("powerFailureA", 1), ("powerFailureB", 2), ("powerRestoredA", 3), ("powerRestoredB", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: benuChassisPowerFailureInfo.setStatus('obsolete')
benuChassisPowerFailure = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 1)).setObjects(("BENU-CHASSIS-MIB", "benuChassisPowerFailureCardInfo"), ("BENU-CHASSIS-MIB", "benuChassisPowerFailureInfo"))
if mibBuilder.loadTexts: benuChassisPowerFailure.setStatus('obsolete')
benuChassisFanFailureInfo = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: benuChassisFanFailureInfo.setStatus('current')
benuChassisFanFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 2)).setObjects(("BENU-CHASSIS-MIB", "benuChassisFanFailureInfo"))
if mibBuilder.loadTexts: benuChassisFanFailureTrap.setStatus('current')
benuLinkUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"))
if mibBuilder.loadTexts: benuLinkUpTrap.setStatus('current')
benuLinkDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"))
if mibBuilder.loadTexts: benuLinkDownTrap.setStatus('current')
benuChassisPowerFailureCardInfo = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: benuChassisPowerFailureCardInfo.setStatus('obsolete')
benuSensorCritical = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 5)).setObjects(("BENU-CHASSIS-MIB", "benuSensorName"), ("BENU-CHASSIS-MIB", "benuSensorType"), ("BENU-CHASSIS-MIB", "benuSensorValue"), ("BENU-CHASSIS-MIB", "benuSensorId"))
if mibBuilder.loadTexts: benuSensorCritical.setStatus('current')
benuSensorNormal = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 6)).setObjects(("BENU-CHASSIS-MIB", "benuSensorName"), ("BENU-CHASSIS-MIB", "benuSensorType"), ("BENU-CHASSIS-MIB", "benuSensorValue"), ("BENU-CHASSIS-MIB", "benuSensorId"))
if mibBuilder.loadTexts: benuSensorNormal.setStatus('current')
benuChassisPowerInfo = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerSupplyA", 1), ("powerSupplyB", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: benuChassisPowerInfo.setStatus('current')
benuChassisPowerFault = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 7)).setObjects(("BENU-CHASSIS-MIB", "benuChassisPowerInfo"))
if mibBuilder.loadTexts: benuChassisPowerFault.setStatus('current')
benuChassisPowerRecovery = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 8)).setObjects(("BENU-CHASSIS-MIB", "benuChassisPowerInfo"))
if mibBuilder.loadTexts: benuChassisPowerRecovery.setStatus('current')
benuChassisPowerPresent = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 9)).setObjects(("BENU-CHASSIS-MIB", "benuChassisPowerInfo"))
if mibBuilder.loadTexts: benuChassisPowerPresent.setStatus('current')
benuChassisPowerAbsent = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 10)).setObjects(("BENU-CHASSIS-MIB", "benuChassisPowerInfo"))
if mibBuilder.loadTexts: benuChassisPowerAbsent.setStatus('current')
mibBuilder.exportSymbols("BENU-CHASSIS-MIB", benuCardIfPortType=benuCardIfPortType, benuSensorEntry=benuSensorEntry, benuChassisFanTrapEnable=benuChassisFanTrapEnable, benuCardPartNumber=benuCardPartNumber, benuCardDescr=benuCardDescr, benuChassisMIB=benuChassisMIB, benuCardIfInfo=benuCardIfInfo, benuCardIfIndex=benuCardIfIndex, benuSensorId=benuSensorId, benuPowerSupplyEntry=benuPowerSupplyEntry, benuCardOperStatus=benuCardOperStatus, benuCardIfSlotNumber=benuCardIfSlotNumber, benuCardTable=benuCardTable, benuCardSlotNumber=benuCardSlotNumber, benuSensorCritical=benuSensorCritical, benuCardRamSize=benuCardRamSize, benuSysUpTimeSinceLastConfigChange=benuSysUpTimeSinceLastConfigChange, PYSNMP_MODULE_ID=benuChassisMIB, benuCardIndex=benuCardIndex, benuSensorMaxThresh=benuSensorMaxThresh, benuChassisMIBObjects=benuChassisMIBObjects, benuChassisHwVersion=benuChassisHwVersion, benuCardType=benuCardType, benuChassisFanFailureTrap=benuChassisFanFailureTrap, benuSensorState=benuSensorState, benuCardEntry=benuCardEntry, benuCardIfIndexEntry=benuCardIfIndexEntry, benuChassisSensorTrapEnable=benuChassisSensorTrapEnable, benuCardHwVersion=benuCardHwVersion, benuChassisNotifObjects=benuChassisNotifObjects, benuSensorInfo=benuSensorInfo, benuChassisPowerPresent=benuChassisPowerPresent, benuFanCurSpeed=benuFanCurSpeed, benuCardSecondaryDiskSize=benuCardSecondaryDiskSize, benuCardSwVersion=benuCardSwVersion, benuPowerSupplyIndex=benuPowerSupplyIndex, benuChassisPowerFailure=benuChassisPowerFailure, benuLinkDownTrap=benuLinkDownTrap, benuSensorNormal=benuSensorNormal, benuChassisPowerInfo=benuChassisPowerInfo, benuChassisType=benuChassisType, benuCardIfName=benuCardIfName, benuChassisPowerRecovery=benuChassisPowerRecovery, benuCardIfIndexTable=benuCardIfIndexTable, benuSensorMinThresh=benuSensorMinThresh, benuLinkUpTrap=benuLinkUpTrap, benuCardIfVirtualType=benuCardIfVirtualType, benuSensorCardIndex=benuSensorCardIndex, benuChassisPowerTrapEnable=benuChassisPowerTrapEnable, benuPowerSupplyPresent=benuPowerSupplyPresent, benuFanInfo=benuFanInfo, benuChassisNotifVariables=benuChassisNotifVariables, benuPowerSupplyTable=benuPowerSupplyTable, benuPowerSupplyName=benuPowerSupplyName, benuSysUpTimeAtLastChassisChange=benuSysUpTimeAtLastChassisChange, benuChassisId=benuChassisId, benuFanStatus=benuFanStatus, benuSensorType=benuSensorType, benuCardInfo=benuCardInfo, benuPowerSupplyPowered=benuPowerSupplyPowered, benuCardIfPortNumber=benuCardIfPortNumber, benuFanCardIndex=benuFanCardIndex, benuSensorValue=benuSensorValue, benuChassisPowerAbsent=benuChassisPowerAbsent, benuChassisInfo=benuChassisInfo, benuFanTable=benuFanTable, benuSensorTable=benuSensorTable, benuPowerSupplyType=benuPowerSupplyType, benuChassisPowerFailureCardInfo=benuChassisPowerFailureCardInfo, benuPowerSupplyInfo=benuPowerSupplyInfo, benuCardSerial=benuCardSerial, benuFanEntry=benuFanEntry, benuChassisPowerFault=benuChassisPowerFault, benuSensorName=benuSensorName, benuChassisFanFailureInfo=benuChassisFanFailureInfo, benuCardPrimaryDiskSize=benuCardPrimaryDiskSize, benuChassisNumOfSlots=benuChassisNumOfSlots, benuCardIfBindName=benuCardIfBindName, benuChassisPowerFailureInfo=benuChassisPowerFailureInfo, benuChassisGeneralInfo=benuChassisGeneralInfo, benuFanMaxSpeed=benuFanMaxSpeed, benuCardIfEncapsulation=benuCardIfEncapsulation, benuSensorIndex=benuSensorIndex, benuCardIfLinkUpDownEnable=benuCardIfLinkUpDownEnable)
