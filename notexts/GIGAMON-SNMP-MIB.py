#
# PySNMP MIB module GIGAMON-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gigamon/GIGAMON-SNMP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:19:39 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits, Unsigned32, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, enterprises, IpAddress, ModuleIdentity, NotificationType, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits", "Unsigned32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "enterprises", "IpAddress", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32")
TextualConvention, PhysAddress, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "TimeStamp", "DisplayString")
gigamonSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 26866))
gigamonSnmp.setRevisions(('2018-05-15 00:00', '2013-09-25 00:00', '2013-04-15 00:00', '2012-12-04 00:00', '2012-05-09 00:00', '2012-03-27 00:00', '2011-03-25 00:00', '2011-03-24 00:00', '2011-03-03 00:00', '2010-07-10 10:00',))
if mibBuilder.loadTexts: gigamonSnmp.setLastUpdated('201805150000Z')
if mibBuilder.loadTexts: gigamonSnmp.setOrganization('www.gigamon.com')
gigamonSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 1))
gigamonGigaVUE = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 1, 1))
gigamonSnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 1, 2))
gigamonSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 2))
manufacturer = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manufacturer.setStatus('current')
model = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: model.setStatus('current')
name = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: name.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
systemDescription = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDescription.setStatus('current')
version = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
chassisModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisModelNumber.setStatus('current')
chassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNumber.setStatus('current')
bladeSerialNumbers = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bladeSerialNumbers.setStatus('current')
firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
hardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareVersion.setStatus('current')
cpuRAMSize = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuRAMSize.setStatus('current')
cpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilization.setStatus('current')
fans = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fans.setStatus('current')
temperatureSensors = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureSensors.setStatus('current')
powerSupply = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupply.setStatus('current')
gigamonProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3))
gigamonGV2404 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 1))
gigamonGV420 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 2))
gigamonGV212 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 3))
gigamonGV216 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 4))
gigamonSnmpNotifLevel = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("information", 1), ("minor", 2), ("major", 3), ("critical", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifLevel.setStatus('current')
gigamonSnmpNotifDescription = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 2), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifDescription.setStatus('current')
gigamonSnmpNotifOpType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("delete", 3), ("validate", 4), ("change", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifOpType.setStatus('current')
gigamonSnmpNotifPortName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 4), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifPortName.setStatus('current')
gigamonSnmpNotifPortLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifPortLinkStatus.setStatus('current')
gigamonSnmpNotifTAPRelayStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("passive", 1), ("active", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifTAPRelayStatus.setStatus('current')
gigamonSnmpNotifRxTxType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("rx", 0), ("tx", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifRxTxType.setStatus('current')
gigamonSnmpNotifRxTxErrorType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("under-size", 0), ("fragments", 1), ("obsolete", 2), ("jabbers", 3), ("crc-align", 4), ("unknown", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifRxTxErrorType.setStatus('current')
gigamonSnmpNotifCounter = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 9), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifCounter.setStatus('current')
gigamonSnmpNotifFirmwareName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 10), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFirmwareName.setStatus('current')
gigamonSnmpNotifModuleOperationType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("removed", 0), ("inserted", 1), ("changed", 2), ("mismatch", 3), ("shutdown", 4), ("up", 5), ("license-mismatch", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifModuleOperationType.setStatus('current')
gigamonSnmpNotifModuleName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 12), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifModuleName.setStatus('current')
gigamonNotifSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("mid-plane", 0), ("slot-1", 1), ("slot-2", 2), ("slot-3", 3), ("gigaLink-Back", 4), ("daughter-Card", 5), ("slot-4", 10), ("slot-5", 11), ("slot-6", 12), ("slot-7", 13), ("slot-8", 14), ("slot-CC1", 15), ("slot-CC2", 16)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonNotifSlotNumber.setStatus('current')
gigamonSnmpNotifUserName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 14), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifUserName.setStatus('current')
gigamonSnmpNotifFileName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 15), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFileName.setStatus('current')
gigamonNotifPowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("failure", -1), ("abnormal", 0), ("normal", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonNotifPowerStatus.setStatus('current')
gigamonSnmpNotifHardWareName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 17), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifHardWareName.setStatus('current')
gigamonSnmpNotifGigaVUE420SlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("mid-plane", 0), ("expansion-slot-1", 1), ("expansion-slot-2", 2), ("expansion-slot-3", 3), ("expansion-slot-4", 4), ("expansion-slot-5", 5), ("x1-slot", 6), ("x2-slot", 7), ("x3-slot", 8), ("x4-slot", 9)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifGigaVUE420SlotNumber.setStatus('current')
gigamonSnmpNotifFanName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 19), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFanName.setStatus('current')
gigamonNotifFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("failure", -1), ("abnormal", 0), ("normal", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonNotifFanStatus.setStatus('current')
gigamonSnmpNotifUtilizationAlarm = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("below", 0), ("exceed", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifUtilizationAlarm.setStatus('current')
gigamonSnmpNotifUtilizationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 22), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifUtilizationThreshold.setStatus('current')
gigamonSnmpBatteryLevel = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("batteryChargeComplete", 0), ("downBelow75", 1), ("downBelow50", 2), ("downBelow25", 3), ("shutDownSystem", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gigamonSnmpBatteryLevel.setStatus('current')
gigamonSnmpPortLinkSpeed = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApply", 0), ("speed10", 1), ("speed100", 2), ("speed1000", 3), ("speed10000", 4), ("speed40000", 5), ("speed100000", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpPortLinkSpeed.setStatus('current')
gigamonSnmpPortLinkDuplex = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notApply", 0), ("full", 1), ("half", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpPortLinkDuplex.setStatus('current')
gigamonSnmpNotifCpuIndex = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 26), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifCpuIndex.setStatus('current')
gigamonSnmpNotifFsMountPoint = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 27), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFsMountPoint.setStatus('current')
gigamonSnmpPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mainPower", 0), ("poe", 1), ("power48V", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gigamonSnmpPowerSource.setStatus('current')
gigamonSnmpNotifBpsUnitName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 29), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifBpsUnitName.setStatus('current')
gigamonSnmpNotifBpsFailoverStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("primary", 0), ("secondary", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifBpsFailoverStatus.setStatus('current')
gigamonSnmpResetSystemNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 1)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
if mibBuilder.loadTexts: gigamonSnmpResetSystemNotification.setStatus('current')
gigamonSnmpUserAuthFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 2)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUserName"))
if mibBuilder.loadTexts: gigamonSnmpUserAuthFailNotification.setStatus('current')
gigamonSnmpFirmwareChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 3)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFirmwareName"))
if mibBuilder.loadTexts: gigamonSnmpFirmwareChangeNotification.setStatus('current')
gigamonSnmpConfigSaveNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 4)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFileName"))
if mibBuilder.loadTexts: gigamonSnmpConfigSaveNotification.setStatus('current')
gigamonSnmpModuleChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 5)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleOperationType"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleName"), ("GIGAMON-SNMP-MIB", "gigamonNotifSlotNumber"))
if mibBuilder.loadTexts: gigamonSnmpModuleChangeNotification.setStatus('current')
gigamonSnmpPacketDropNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 6)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
if mibBuilder.loadTexts: gigamonSnmpPacketDropNotification.setStatus('current')
gigamonSnmpTapRelayChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 7)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifTAPRelayStatus"))
if mibBuilder.loadTexts: gigamonSnmpTapRelayChangeNotification.setStatus('current')
gigamonSnmpPortLinkChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 8)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortLinkStatus"))
if mibBuilder.loadTexts: gigamonSnmpPortLinkChangeNotification.setStatus('current')
gigamonSnmpRxTxErrorNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 9)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxType"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxErrorType"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
if mibBuilder.loadTexts: gigamonSnmpRxTxErrorNotification.setStatus('current')
gigamonPowerChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 10)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonNotifPowerStatus"))
if mibBuilder.loadTexts: gigamonPowerChangeNotification.setStatus('current')
gigamonFanChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 11)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFanName"), ("GIGAMON-SNMP-MIB", "gigamonNotifFanStatus"))
if mibBuilder.loadTexts: gigamonFanChangeNotification.setStatus('current')
gigamonSnmpOverThresholdChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 12)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationAlarm"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationThreshold"))
if mibBuilder.loadTexts: gigamonSnmpOverThresholdChangeNotification.setStatus('current')
gigamonSnmpBatteryLevelChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 13)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpBatteryLevel"))
if mibBuilder.loadTexts: gigamonSnmpBatteryLevelChangeNotification.setStatus('current')
gigamonLinkSpeedStatusChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 14)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpPortLinkSpeed"), ("GIGAMON-SNMP-MIB", "gigamonSnmpPortLinkDuplex"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortLinkStatus"))
if mibBuilder.loadTexts: gigamonLinkSpeedStatusChangeNotification.setStatus('current')
gigamonPowerSourceChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 15)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpPowerSource"), ("GIGAMON-SNMP-MIB", "gigamonNotifPowerStatus"))
if mibBuilder.loadTexts: gigamonPowerSourceChangeNotification.setStatus('current')
gigamonSnmpCpuUtilHighNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 16)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCpuIndex"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationThreshold"))
if mibBuilder.loadTexts: gigamonSnmpCpuUtilHighNotification.setStatus('current')
gigamonSnmpUnexpectedShutdownNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 17)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
if mibBuilder.loadTexts: gigamonSnmpUnexpectedShutdownNotification.setStatus('current')
gigamonSnmpDiskSpaceLowNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 18)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFsMountPoint"))
if mibBuilder.loadTexts: gigamonSnmpDiskSpaceLowNotification.setStatus('current')
gigamonSnmpWatchdogResetNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 19)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
if mibBuilder.loadTexts: gigamonSnmpWatchdogResetNotification.setStatus('current')
gigamonSnmpBpsFailoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 20)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifBpsUnitName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifBpsFailoverStatus"))
if mibBuilder.loadTexts: gigamonSnmpBpsFailoverNotification.setStatus('current')
mibBuilder.exportSymbols("GIGAMON-SNMP-MIB", gigamonProducts=gigamonProducts, gigamonSnmpBatteryLevel=gigamonSnmpBatteryLevel, gigamonSnmpNotifLevel=gigamonSnmpNotifLevel, gigamonSnmpNotifBpsFailoverStatus=gigamonSnmpNotifBpsFailoverStatus, gigamonSnmpModuleChangeNotification=gigamonSnmpModuleChangeNotification, gigamonFanChangeNotification=gigamonFanChangeNotification, gigamonSnmpConfigSaveNotification=gigamonSnmpConfigSaveNotification, gigamonSnmpNotifOpType=gigamonSnmpNotifOpType, fans=fans, bladeSerialNumbers=bladeSerialNumbers, gigamonNotifSlotNumber=gigamonNotifSlotNumber, cpuUtilization=cpuUtilization, chassisModelNumber=chassisModelNumber, gigamonSnmp=gigamonSnmp, gigamonSnmpNotifBpsUnitName=gigamonSnmpNotifBpsUnitName, gigamonSnmpNotifFsMountPoint=gigamonSnmpNotifFsMountPoint, gigamonSnmpNotifUtilizationThreshold=gigamonSnmpNotifUtilizationThreshold, gigamonSnmpNotifFileName=gigamonSnmpNotifFileName, gigamonSnmpNotifications=gigamonSnmpNotifications, gigamonLinkSpeedStatusChangeNotification=gigamonLinkSpeedStatusChangeNotification, gigamonNotifFanStatus=gigamonNotifFanStatus, gigamonSnmpOverThresholdChangeNotification=gigamonSnmpOverThresholdChangeNotification, manufacturer=manufacturer, gigamonSnmpPowerSource=gigamonSnmpPowerSource, firmwareVersion=firmwareVersion, temperatureSensors=temperatureSensors, gigamonSnmpNotifGigaVUE420SlotNumber=gigamonSnmpNotifGigaVUE420SlotNumber, systemDescription=systemDescription, chassisSerialNumber=chassisSerialNumber, gigamonGV212=gigamonGV212, hardwareVersion=hardwareVersion, gigamonSnmpRxTxErrorNotification=gigamonSnmpRxTxErrorNotification, gigamonSnmpNotifUtilizationAlarm=gigamonSnmpNotifUtilizationAlarm, gigamonSnmpNotifPortName=gigamonSnmpNotifPortName, gigamonSnmpResetSystemNotification=gigamonSnmpResetSystemNotification, PYSNMP_MODULE_ID=gigamonSnmp, gigamonSnmpDiskSpaceLowNotification=gigamonSnmpDiskSpaceLowNotification, gigamonSnmpNotifDescription=gigamonSnmpNotifDescription, gigamonSnmpBatteryLevelChangeNotification=gigamonSnmpBatteryLevelChangeNotification, version=version, gigamonSnmpNotificationObjects=gigamonSnmpNotificationObjects, gigamonSnmpNotifPortLinkStatus=gigamonSnmpNotifPortLinkStatus, gigamonSnmpNotifTAPRelayStatus=gigamonSnmpNotifTAPRelayStatus, gigamonSnmpNotifUserName=gigamonSnmpNotifUserName, gigamonSnmpPortLinkSpeed=gigamonSnmpPortLinkSpeed, gigamonSnmpBpsFailoverNotification=gigamonSnmpBpsFailoverNotification, gigamonSnmpTapRelayChangeNotification=gigamonSnmpTapRelayChangeNotification, gigamonSnmpWatchdogResetNotification=gigamonSnmpWatchdogResetNotification, gigamonPowerSourceChangeNotification=gigamonPowerSourceChangeNotification, gigamonSnmpNotifCpuIndex=gigamonSnmpNotifCpuIndex, gigamonSnmpUserAuthFailNotification=gigamonSnmpUserAuthFailNotification, gigamonSnmpNotifCounter=gigamonSnmpNotifCounter, gigamonSnmpCpuUtilHighNotification=gigamonSnmpCpuUtilHighNotification, gigamonSnmpPortLinkChangeNotification=gigamonSnmpPortLinkChangeNotification, model=model, name=name, serialNumber=serialNumber, gigamonSystem=gigamonSystem, gigamonNotifPowerStatus=gigamonNotifPowerStatus, gigamonSnmpNotifRxTxType=gigamonSnmpNotifRxTxType, gigamonSnmpFirmwareChangeNotification=gigamonSnmpFirmwareChangeNotification, gigamonSnmpPacketDropNotification=gigamonSnmpPacketDropNotification, gigamonSnmpNotifModuleOperationType=gigamonSnmpNotifModuleOperationType, powerSupply=powerSupply, gigamonPowerChangeNotification=gigamonPowerChangeNotification, gigamonSnmpNotifModuleName=gigamonSnmpNotifModuleName, gigamonGigaVUE=gigamonGigaVUE, cpuRAMSize=cpuRAMSize, gigamonGV2404=gigamonGV2404, gigamonSnmpNotifRxTxErrorType=gigamonSnmpNotifRxTxErrorType, gigamonSnmpPortLinkDuplex=gigamonSnmpPortLinkDuplex, gigamonSnmpNotifHardWareName=gigamonSnmpNotifHardWareName, gigamonSnmpNotifFirmwareName=gigamonSnmpNotifFirmwareName, gigamonSnmpUnexpectedShutdownNotification=gigamonSnmpUnexpectedShutdownNotification, gigamonGV216=gigamonGV216, gigamonSnmpNotifFanName=gigamonSnmpNotifFanName, gigamonGV420=gigamonGV420)
