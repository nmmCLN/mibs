#
# PySNMP MIB module EQLCONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLCONTROLLER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:24 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, MibIdentifier, NotificationType, Bits, iso, ObjectIdentity, IpAddress, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "MibIdentifier", "NotificationType", "Bits", "iso", "ObjectIdentity", "IpAddress", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eqlcontrollerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 4))
eqlcontrollerModule.setRevisions(('2002-09-06 00:00',))
if mibBuilder.loadTexts: eqlcontrollerModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlcontrollerModule.setOrganization('EqualLogic Inc.')
eqlcontrollerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 1))
eqlcontrollerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 2))
eqlcontrollerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 3))
eqlbackplaneObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 4))
eqlbackplaneNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 5))
eqlbackplaneConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 6))
eqlemmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 7))
eqlemmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 8))
eqlemmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 9))
eqldaughtercardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 10))
eqldaughtercardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 11))
eqldaughtercardConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 12))
eqlchannelcardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 13))
eqlsfpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 4, 14))
eqlControllerTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1), )
if mibBuilder.loadTexts: eqlControllerTable.setStatus('current')
eqlControllerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLCONTROLLER-MIB", "eqlControllerIndex"))
if mibBuilder.loadTexts: eqlControllerEntry.setStatus('current')
eqlControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1))
if mibBuilder.loadTexts: eqlControllerIndex.setStatus('current')
eqlControllerModel = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('unknown model')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerModel.setStatus('current')
eqlControllerCMRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone('unknown rev')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerCMRevision.setStatus('current')
eqlControllerSwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 96)).clone('unknown sw rev')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerSwRevision.setStatus('current')
eqlControllerBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("ok", 1), ("failed", 2), ("good-battery-is-charging", 3), ("low-voltage-status", 4), ("low-voltage-is-charging", 5), ("missing-battery", 6), ("high-temp", 7), ("low-temp", 8), ("end-of-life", 9), ("end-of-life-warning", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerBatteryStatus.setStatus('current')
eqlControllerUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 6), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerUpTime.setStatus('current')
eqlControllerProcessorTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerProcessorTemp.setStatus('current')
eqlControllerChipsetTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerChipsetTemp.setStatus('current')
eqlControllerPrimaryOrSecondary = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerPrimaryOrSecondary.setStatus('current')
eqlControllerPrimaryFlashImageRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerPrimaryFlashImageRev.setStatus('current')
eqlControllerSecondaryFlashImageRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerSecondaryFlashImageRev.setStatus('current')
eqlControllerSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerSerialNumber.setStatus('current')
eqlControllerDate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerDate.setStatus('current')
eqlControllerECO = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerECO.setStatus('current')
eqlControllerEEprom = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerEEprom.setStatus('current')
eqlControllerPLDrev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerPLDrev.setStatus('current')
eqlControllerPlatformType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerPlatformType.setStatus('current')
eqlControllerPlatformVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerPlatformVersion.setStatus('current')
eqlControllerCPUPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerCPUPass.setStatus('current')
eqlControllerCPUrev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerCPUrev.setStatus('current')
eqlControllerCPUfreq = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerCPUfreq.setStatus('current')
eqlControllerPhysRam = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerPhysRam.setStatus('current')
eqlControllerBootRomVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerBootRomVersion.setStatus('current')
eqlControllerBootRomBuildDate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerBootRomBuildDate.setStatus('current')
eqlControllerInfoMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 25), DisplayString().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerInfoMsg.setStatus('current')
eqlControllerAthenaSataVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 26), DisplayString().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerAthenaSataVersion.setStatus('current')
eqlControllerMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 27), Unsigned32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerMajorVersion.setStatus('current')
eqlControllerMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 28), Unsigned32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerMinorVersion.setStatus('current')
eqlControllerMaintenanceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 29), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerMaintenanceVersion.setStatus('current')
eqlControllerSWCompatibilityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 30), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerSWCompatibilityLevel.setStatus('current')
eqlControllerFullSwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 96)).clone('unknown sw rev')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerFullSwRevision.setStatus('current')
eqlControllerNVRAMBattery = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("not-present", 0), ("good", 1), ("bad", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerNVRAMBattery.setStatus('current')
eqlControllerSerialNumber2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 33), DisplayString().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerSerialNumber2.setStatus('current')
eqlControllerType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 34), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerType.setStatus('current')
eqlControllerBootTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 35), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlControllerBootTime.setStatus('current')
eqlBackplaneTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1), )
if mibBuilder.loadTexts: eqlBackplaneTable.setStatus('current')
eqlBackplaneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLCONTROLLER-MIB", "eqlBackplaneIndex"))
if mibBuilder.loadTexts: eqlBackplaneEntry.setStatus('current')
eqlBackplaneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1))
if mibBuilder.loadTexts: eqlBackplaneIndex.setStatus('current')
eqlBackplanePartNum = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplanePartNum.setStatus('current')
eqlBackplaneRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneRev.setStatus('current')
eqlBackplaneDate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneDate.setStatus('current')
eqlBackplaneSN = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneSN.setStatus('current')
eqlBackplaneECO = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneECO.setStatus('current')
eqlBackplaneEEprom = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneEEprom.setStatus('current')
eqlBackplaneSN2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 8), DisplayString().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneSN2.setStatus('current')
eqlBackplaneType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneType.setStatus('current')
eqlBackplaneTypeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlBackplaneTypeId.setStatus('current')
eqlEMMTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1), )
if mibBuilder.loadTexts: eqlEMMTable.setStatus('current')
eqlEMMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLCONTROLLER-MIB", "eqlEMMIndex"))
if mibBuilder.loadTexts: eqlEMMEntry.setStatus('current')
eqlEMMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(1))
if mibBuilder.loadTexts: eqlEMMIndex.setStatus('current')
eqlEMMModel = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('unknown model')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMModel.setStatus('current')
eqlEMMPartNum = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMPartNum.setStatus('current')
eqlEMMRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMRev.setStatus('current')
eqlEMMDate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMDate.setStatus('current')
eqlEMMSN = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMSN.setStatus('current')
eqlEMMECO = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMECO.setStatus('current')
eqlEMMEEprom = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMEEprom.setStatus('current')
eqlEMMSN2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 9), DisplayString().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlEMMSN2.setStatus('current')
eqlDaughterCardTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1), )
if mibBuilder.loadTexts: eqlDaughterCardTable.setStatus('current')
eqlDaughterCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLCONTROLLER-MIB", "eqlDaughterCardIndex"))
if mibBuilder.loadTexts: eqlDaughterCardEntry.setStatus('current')
eqlDaughterCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1))
if mibBuilder.loadTexts: eqlDaughterCardIndex.setStatus('current')
eqlDaughterCardModel = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('unknown model')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDaughterCardModel.setStatus('current')
eqlDaughterCardPartNum = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDaughterCardPartNum.setStatus('current')
eqlDaughterCardRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDaughterCardRev.setStatus('current')
eqlDaughterCardDate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDaughterCardDate.setStatus('current')
eqlDaughterCardSN = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDaughterCardSN.setStatus('current')
eqlDaughterCardECO = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDaughterCardECO.setStatus('current')
eqlDaughterCardEEprom = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlDaughterCardEEprom.setStatus('current')
eqlChannelCardTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 4, 13, 1), )
if mibBuilder.loadTexts: eqlChannelCardTable.setStatus('current')
eqlChannelCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLCONTROLLER-MIB", "eqlChannelCardIndex"))
if mibBuilder.loadTexts: eqlChannelCardEntry.setStatus('current')
eqlChannelCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: eqlChannelCardIndex.setStatus('current')
eqlChannelCardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlChannelCardSerialNumber.setStatus('current')
eqlChannelCardFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlChannelCardFirmwareRev.setStatus('current')
eqlChannelCardInitRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlChannelCardInitRev.setStatus('current')
eqlChannelCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("not-present", 1), ("failed", 2), ("good", 3))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlChannelCardStatus.setStatus('current')
eqlSFPTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1), )
if mibBuilder.loadTexts: eqlSFPTable.setStatus('current')
eqlSFPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLCONTROLLER-MIB", "eqlSFPIndex"))
if mibBuilder.loadTexts: eqlSFPEntry.setStatus('current')
eqlSFPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: eqlSFPIndex.setStatus('current')
eqlSFPMode = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("single-mode", 1), ("multi-mode", 2), ("copper", 3), ("not-present", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPMode.setStatus('current')
eqlSFPIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPIfIndex.setStatus('current')
eqlSFPIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3))).clone(namedValues=NamedValues(("unknown", 0), ("sfp-transceiver", 3))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPIdentifier.setStatus('current')
eqlSFPConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 7, 33))).clone(namedValues=NamedValues(("unknown", 0), ("lc", 7), ("copper", 33))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPConnector.setStatus('current')
eqlSFPBitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPBitrate.setStatus('current')
eqlSFPLength1 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPLength1.setStatus('current')
eqlSFPLength2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPLength2.setStatus('current')
eqlSFPVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPVendorName.setStatus('current')
eqlSFPPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPPartNumber.setStatus('current')
eqlSFPFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPFirmwareRev.setStatus('current')
eqlSFPSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPSerialNumber.setStatus('current')
eqlSFPDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPDateCode.setStatus('current')
eqlSFPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("not-present", 1), ("failed", 2), ("good", 3))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSFPStatus.setStatus('current')
mibBuilder.exportSymbols("EQLCONTROLLER-MIB", eqlSFPFirmwareRev=eqlSFPFirmwareRev, eqlControllerEntry=eqlControllerEntry, eqlDaughterCardTable=eqlDaughterCardTable, eqlControllerPlatformType=eqlControllerPlatformType, eqlSFPVendorName=eqlSFPVendorName, PYSNMP_MODULE_ID=eqlcontrollerModule, eqlControllerSWCompatibilityLevel=eqlControllerSWCompatibilityLevel, eqlemmObjects=eqlemmObjects, eqlcontrollerModule=eqlcontrollerModule, eqlBackplaneEEprom=eqlBackplaneEEprom, eqlChannelCardStatus=eqlChannelCardStatus, eqlControllerBootRomVersion=eqlControllerBootRomVersion, eqlControllerPrimaryOrSecondary=eqlControllerPrimaryOrSecondary, eqlbackplaneConformance=eqlbackplaneConformance, eqlControllerModel=eqlControllerModel, eqlSFPPartNumber=eqlSFPPartNumber, eqlControllerIndex=eqlControllerIndex, eqlEMMModel=eqlEMMModel, eqlControllerCPUPass=eqlControllerCPUPass, eqlControllerCMRevision=eqlControllerCMRevision, eqlChannelCardFirmwareRev=eqlChannelCardFirmwareRev, eqldaughtercardConformance=eqldaughtercardConformance, eqlcontrollerObjects=eqlcontrollerObjects, eqlEMMSN=eqlEMMSN, eqlControllerNVRAMBattery=eqlControllerNVRAMBattery, eqlSFPIdentifier=eqlSFPIdentifier, eqlEMMRev=eqlEMMRev, eqlBackplaneSN=eqlBackplaneSN, eqlControllerTable=eqlControllerTable, eqlDaughterCardECO=eqlDaughterCardECO, eqlControllerInfoMsg=eqlControllerInfoMsg, eqlBackplaneSN2=eqlBackplaneSN2, eqlDaughterCardEEprom=eqlDaughterCardEEprom, eqlSFPTable=eqlSFPTable, eqlEMMDate=eqlEMMDate, eqlControllerSerialNumber=eqlControllerSerialNumber, eqlControllerDate=eqlControllerDate, eqlchannelcardObjects=eqlchannelcardObjects, eqlControllerBatteryStatus=eqlControllerBatteryStatus, eqlDaughterCardEntry=eqlDaughterCardEntry, eqlEMMEntry=eqlEMMEntry, eqlSFPSerialNumber=eqlSFPSerialNumber, eqlSFPMode=eqlSFPMode, eqlControllerChipsetTemp=eqlControllerChipsetTemp, eqlBackplanePartNum=eqlBackplanePartNum, eqlControllerSwRevision=eqlControllerSwRevision, eqlControllerBootRomBuildDate=eqlControllerBootRomBuildDate, eqlChannelCardInitRev=eqlChannelCardInitRev, eqlChannelCardSerialNumber=eqlChannelCardSerialNumber, eqlControllerAthenaSataVersion=eqlControllerAthenaSataVersion, eqlSFPConnector=eqlSFPConnector, eqlEMMECO=eqlEMMECO, eqlSFPLength2=eqlSFPLength2, eqlBackplaneType=eqlBackplaneType, eqlbackplaneNotifications=eqlbackplaneNotifications, eqlEMMTable=eqlEMMTable, eqlChannelCardIndex=eqlChannelCardIndex, eqlControllerCPUfreq=eqlControllerCPUfreq, eqlControllerProcessorTemp=eqlControllerProcessorTemp, eqlBackplaneDate=eqlBackplaneDate, eqlSFPStatus=eqlSFPStatus, eqlControllerType=eqlControllerType, eqlcontrollerConformance=eqlcontrollerConformance, eqlSFPDateCode=eqlSFPDateCode, eqlDaughterCardSN=eqlDaughterCardSN, eqlControllerFullSwRevision=eqlControllerFullSwRevision, eqldaughtercardObjects=eqldaughtercardObjects, eqlBackplaneRev=eqlBackplaneRev, eqlEMMSN2=eqlEMMSN2, eqlSFPEntry=eqlSFPEntry, eqlcontrollerNotifications=eqlcontrollerNotifications, eqlControllerPhysRam=eqlControllerPhysRam, eqlbackplaneObjects=eqlbackplaneObjects, eqlChannelCardTable=eqlChannelCardTable, eqlBackplaneTypeId=eqlBackplaneTypeId, eqlControllerBootTime=eqlControllerBootTime, eqlDaughterCardDate=eqlDaughterCardDate, eqlemmConformance=eqlemmConformance, eqlSFPIfIndex=eqlSFPIfIndex, eqlBackplaneTable=eqlBackplaneTable, eqlControllerMaintenanceVersion=eqlControllerMaintenanceVersion, eqlControllerPlatformVersion=eqlControllerPlatformVersion, eqlControllerUpTime=eqlControllerUpTime, eqlControllerSerialNumber2=eqlControllerSerialNumber2, eqlDaughterCardIndex=eqlDaughterCardIndex, eqlSFPIndex=eqlSFPIndex, eqlControllerMajorVersion=eqlControllerMajorVersion, eqlEMMPartNum=eqlEMMPartNum, eqlBackplaneEntry=eqlBackplaneEntry, eqlChannelCardEntry=eqlChannelCardEntry, eqlBackplaneIndex=eqlBackplaneIndex, eqlBackplaneECO=eqlBackplaneECO, eqlEMMEEprom=eqlEMMEEprom, eqlDaughterCardPartNum=eqlDaughterCardPartNum, eqlDaughterCardModel=eqlDaughterCardModel, eqlControllerPLDrev=eqlControllerPLDrev, eqlControllerSecondaryFlashImageRev=eqlControllerSecondaryFlashImageRev, eqlSFPBitrate=eqlSFPBitrate, eqlEMMIndex=eqlEMMIndex, eqlControllerMinorVersion=eqlControllerMinorVersion, eqlSFPLength1=eqlSFPLength1, eqlControllerEEprom=eqlControllerEEprom, eqlemmNotifications=eqlemmNotifications, eqlControllerECO=eqlControllerECO, eqlControllerCPUrev=eqlControllerCPUrev, eqldaughtercardNotifications=eqldaughtercardNotifications, eqlDaughterCardRev=eqlDaughterCardRev, eqlControllerPrimaryFlashImageRev=eqlControllerPrimaryFlashImageRev, eqlsfpObjects=eqlsfpObjects)
