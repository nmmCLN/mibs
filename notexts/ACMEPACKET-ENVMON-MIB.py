#
# PySNMP MIB module ACMEPACKET-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-ENVMON-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ApPhyPortType, ApHardwareModuleFamily, ApRedundancyState, ApPresence = mibBuilder.importSymbols("ACMEPACKET-TC", "ApPhyPortType", "ApHardwareModuleFamily", "ApRedundancyState", "ApPresence")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, NotificationType, Counter64, MibIdentifier, iso, Unsigned32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Gauge32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "iso", "Unsigned32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Gauge32", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
apEnvMonModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 3))
apEnvMonModule.setRevisions(('2012-07-16 00:00', '2014-06-26 00:00', '2018-11-19 00:00',))
if mibBuilder.loadTexts: apEnvMonModule.setLastUpdated('201811190000Z')
if mibBuilder.loadTexts: apEnvMonModule.setOrganization('Oracle Communications')
class ApEnvMonState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("initial", 1), ("normal", 2), ("minor", 3), ("major", 4), ("critical", 5), ("shutdown", 6), ("notPresent", 7), ("notFunctioning", 8), ("unknown", 9))

apEnvMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1))
apEnvMonI2CState = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 1), ApEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonI2CState.setStatus('current')
apEnvMonVoltageObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2))
apEnvMonVoltageStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1), )
if mibBuilder.loadTexts: apEnvMonVoltageStatusTable.setStatus('current')
apEnvMonVoltageStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1), ).setIndexNames((0, "ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusIndex"))
if mibBuilder.loadTexts: apEnvMonVoltageStatusEntry.setStatus('current')
apEnvMonVoltageStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apEnvMonVoltageStatusIndex.setStatus('current')
apEnvMonVoltageStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43, 50, 51, 52, 53, 60, 61, 62, 70, 71, 72, 80, 81, 82, 83, 84, 85))).clone(namedValues=NamedValues(("unknown", 0), ("v2p5", 1), ("v3p3", 2), ("v5", 3), ("cpu", 4), ("v1", 5), ("v1p1", 6), ("v1p15", 7), ("v1p2", 8), ("v1p212", 9), ("v1p25", 10), ("v1p3", 11), ("v1p5", 12), ("v1p8", 13), ("v2p6", 14), ("v3p3aux", 15), ("sd5MainV0p9", 20), ("sd5MainV1p0", 21), ("sd5MainV1p2", 22), ("sd5MainV1p5", 23), ("sd5MainV1p8", 24), ("sd5MainV2p5", 25), ("sd5MainV3p3", 26), ("sd5MainV5p0", 27), ("sd5PhyV0p9", 30), ("sd5PhyV1p0", 31), ("sd5PhyV1p1", 32), ("sd5PhyV1p2", 33), ("sd5PhyV1p5", 34), ("sd5PhyV1p8", 35), ("sd5PhyV2p5", 36), ("sd5PhyV3p3", 37), ("sd5MgmtV1p0", 40), ("sd5MgmtV1p8", 41), ("sd5MgmtV3p3", 42), ("sd5MgmtV5p0", 43), ("sd5Cav0Pol0", 50), ("sd5Cav0Pol1", 51), ("sd5Cav1Pol0", 52), ("sd5Cav1Pol1", 53), ("sd5FlexV1p0", 60), ("sd5FlexV1p2", 61), ("sd5FlexV1p8", 62), ("sd5TighV1p2", 70), ("sd5TighV3p3", 71), ("sd5TighV1p05", 72), ("sd5TcmPol0", 80), ("sd5TcmPol1", 81), ("sd5TcmPol2", 82), ("sd5TcmPol3", 83), ("sd5TcmPol4", 84), ("sd5TcmPol5", 85)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonVoltageStatusType.setStatus('current')
apEnvMonVoltageStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonVoltageStatusDescr.setStatus('current')
apEnvMonVoltageStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 4), Integer32()).setUnits('millivolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonVoltageStatusValue.setStatus('current')
apEnvMonVoltageState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 5), ApEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonVoltageState.setStatus('current')
apEnvMonVoltageSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonVoltageSlotID.setStatus('current')
apEnvMonVoltageSlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 7), ApHardwareModuleFamily()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonVoltageSlotType.setStatus('current')
apEnvMonTemperatureObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3))
apEnvMonTemperatureStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1), )
if mibBuilder.loadTexts: apEnvMonTemperatureStatusTable.setStatus('current')
apEnvMonTemperatureStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1), ).setIndexNames((0, "ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusIndex"))
if mibBuilder.loadTexts: apEnvMonTemperatureStatusEntry.setStatus('current')
apEnvMonTemperatureStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apEnvMonTemperatureStatusIndex.setStatus('current')
apEnvMonTemperatureStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78))).clone(namedValues=NamedValues(("ds1624sMain", 1), ("ds1624sCPU", 2), ("lm84", 3), ("lm75", 4), ("lm75Main", 5), ("lm75Cpu", 6), ("lm75Phy", 7), ("sd5MainCpu", 10), ("sd5MainLI", 11), ("sd5MainRI", 12), ("sd5MainLE", 13), ("sd5MainRE", 14), ("sd5MainPlx", 15), ("sd5MainPcie", 16), ("sd5MainPsa", 17), ("sd5MainPsb", 18), ("sd5Tigh", 20), ("sd5Flex", 21), ("sd5Mgmt", 22), ("sd5PhyCav0", 30), ("sd5PhyCav1", 31), ("sd5PhyTemp0", 32), ("sd5PhyTemp1", 33), ("sd5PhyTemp2", 34), ("sd5PhyTemp3", 35), ("sd5PhyTemp4", 36), ("sd5PhyTemp5", 37), ("sd5PhyTcm0", 40), ("sd5PhyTcm1", 41), ("sd5PhyTcm2", 42), ("sd5PhyTcm3", 43), ("sd5PhyTcm4", 44), ("sd5PhyTcm5", 45), ("sd5PhyTcm6", 46), ("sd5PhyTcm7", 47), ("sd5PhyTcm8", 48), ("sd5PhyTcm9", 49), ("sd5PhyTcm10", 50), ("sd5PhyTcm11", 51), ("sd5PhyTcm12", 52), ("sd5PhyTcm13", 53), ("sd5PhyTcm14", 54), ("sd5PhyTcm15", 55), ("sd5PhyTcm16", 56), ("sd5PhyTcm17", 57), ("sd5PhyTcm18", 58), ("sd5PhyTcm19", 59), ("sd5PhyTcm20", 60), ("sd5PhyTcm21", 61), ("sd5PhyTcm22", 62), ("sd5PhyTcm23", 63), ("sd6MainBoard1", 71), ("sd6MainBoard2", 72), ("sd6MgmtI350", 73), ("sd6MediaI350", 74), ("sd6DSPI350", 75), ("sd6MainTCM0", 76), ("sd6MainTCM1", 77), ("sd6CPU", 78)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonTemperatureStatusType.setStatus('current')
apEnvMonTemperatureStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonTemperatureStatusDescr.setStatus('current')
apEnvMonTemperatureStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 4), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonTemperatureStatusValue.setStatus('current')
apEnvMonTemperatureState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 5), ApEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonTemperatureState.setStatus('current')
apEnvMonTemperatureSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonTemperatureSlotID.setStatus('current')
apEnvMonTemperatureSlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 7), ApHardwareModuleFamily()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonTemperatureSlotType.setStatus('current')
apEnvMonFanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4))
apEnvMonFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1), )
if mibBuilder.loadTexts: apEnvMonFanStatusTable.setStatus('current')
apEnvMonFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1), ).setIndexNames((0, "ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusIndex"))
if mibBuilder.loadTexts: apEnvMonFanStatusEntry.setStatus('current')
apEnvMonFanStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apEnvMonFanStatusIndex.setStatus('current')
apEnvMonFanStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 11, 12, 13, 14, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35))).clone(namedValues=NamedValues(("left", 0), ("middle", 1), ("right", 2), ("slot", 3), ("fan1", 11), ("fan2", 12), ("fan3", 13), ("fan4", 14), ("mainFan1", 21), ("mainFan2", 22), ("mainFan3", 23), ("mainFan4", 24), ("mainFan5", 25), ("flx1Fan1", 26), ("flx1Fan2", 27), ("flx1Fan3", 28), ("flx1Fan4", 29), ("flx1Fan5", 30), ("flx2Fan1", 31), ("flx2Fan2", 32), ("flx2Fan3", 33), ("flx2Fan4", 34), ("flx2Fan5", 35)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonFanStatusType.setStatus('current')
apEnvMonFanStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonFanStatusDescr.setStatus('current')
apEnvMonFanStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 4), Gauge32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonFanStatusValue.setStatus('current')
apEnvMonFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 5), ApEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonFanState.setStatus('current')
apEnvMonFanSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonFanSlotID.setStatus('current')
apEnvMonPowerSupplyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5))
apEnvMonPowerSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1), )
if mibBuilder.loadTexts: apEnvMonPowerSupplyStatusTable.setStatus('current')
apEnvMonPowerSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1), ).setIndexNames((0, "ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyStatusIndex"))
if mibBuilder.loadTexts: apEnvMonPowerSupplyStatusEntry.setStatus('current')
apEnvMonPowerSupplyStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apEnvMonPowerSupplyStatusIndex.setStatus('current')
apEnvMonPowerSupplyStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("left", 0), ("right", 1), ("slot", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonPowerSupplyStatusType.setStatus('current')
apEnvMonPowerSupplyStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonPowerSupplyStatusDescr.setStatus('current')
apEnvMonPowerSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 4), ApEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonPowerSupplyState.setStatus('current')
apEnvMonPhyCardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6))
apEnvMonPhyCardStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1), )
if mibBuilder.loadTexts: apEnvMonPhyCardStatusTable.setStatus('deprecated')
apEnvMonPhyCardStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1), ).setIndexNames((0, "ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardStatusIndex"))
if mibBuilder.loadTexts: apEnvMonPhyCardStatusEntry.setStatus('deprecated')
apEnvMonPhyCardStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apEnvMonPhyCardStatusIndex.setStatus('deprecated')
apEnvMonPhyCardStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("left", 0), ("right", 1), ("slot", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonPhyCardStatusType.setStatus('deprecated')
apEnvMonPhyCardStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonPhyCardStatusDescr.setStatus('deprecated')
apEnvMonPhyCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 4), ApEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonPhyCardState.setStatus('deprecated')
apEnvMonCardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7))
apEnvMonCardTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1), )
if mibBuilder.loadTexts: apEnvMonCardTable.setStatus('current')
apEnvMonCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1), ).setIndexNames((0, "ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"))
if mibBuilder.loadTexts: apEnvMonCardEntry.setStatus('current')
apEnvMonCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCardSlot.setStatus('current')
apEnvMonCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 2), ApHardwareModuleFamily()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCardType.setStatus('current')
apEnvMonCardDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCardDescr.setStatus('current')
apEnvMonCardHealthScore = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCardHealthScore.setStatus('current')
apEnvMonCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 5), ApEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCardState.setStatus('current')
apEnvMonCardRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 6), ApRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCardRedundancy.setStatus('current')
apEnvMonCpuCoreTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2), )
if mibBuilder.loadTexts: apEnvMonCpuCoreTable.setStatus('current')
apEnvMonCpuCoreEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1), ).setIndexNames((0, "ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"), (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreIndex"))
if mibBuilder.loadTexts: apEnvMonCpuCoreEntry.setStatus('current')
apEnvMonCpuCoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCpuCoreIndex.setStatus('current')
apEnvMonCpuCoreDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCpuCoreDescr.setStatus('current')
apEnvMonCpuCoreUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 3), Gauge32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCpuCoreUsage.setStatus('current')
apEnvMonCpuCoreState = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 101, 102, 201, 202, 203, 204, 205, 206, 207, 208, 209, 401, 402, 403, 404, 405, 406))).clone(namedValues=NamedValues(("unknown", 0), ("present", 1), ("booting", 2), ("registered", 3), ("readywait", 4), ("ready", 5), ("bootTimeout", 6), ("registerTimeout", 7), ("manifestTimeout", 8), ("readyTimeout", 9), ("healthWait", 101), ("healthRcvd", 102), ("becomingActive", 201), ("becomingStandby", 202), ("becomingOOS", 203), ("active", 204), ("standby", 205), ("oos", 206), ("activeTimeout", 207), ("standbyTimeout", 208), ("oosTimeout", 209), ("resetting", 401), ("reset", 402), ("resetTimeout", 403), ("shuttingDown", 404), ("shutOff", 405), ("shutdownTimeout", 406)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCpuCoreState.setStatus('current')
apEnvMonCpuCoreRamDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCpuCoreRamDescr.setStatus('current')
apEnvMonCpuCoreRamUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 6), Gauge32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonCpuCoreRamUsage.setStatus('current')
apEnvMonMIBNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 2))
apEnvMonEnableStatChangeNotif = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apEnvMonEnableStatChangeNotif.setStatus('current')
apEnvMonNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3))
apEnvMonTrapInstance = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapInstance.setStatus('current')
apEnvMonTrapPreviousState = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 2), ApEnvMonState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapPreviousState.setStatus('current')
apEnvMonTrapCurrentState = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 3), ApEnvMonState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapCurrentState.setStatus('current')
apEnvMonTrapSlotID = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapSlotID.setStatus('current')
apEnvMonTrapSlotType = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 5), ApHardwareModuleFamily()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapSlotType.setStatus('current')
apEnvMonTrapPortType = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 6), ApPhyPortType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapPortType.setStatus('current')
apEnvMonTrapPresence = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 7), ApPresence()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapPresence.setStatus('current')
apEnvMonTrapPortID = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 8), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apEnvMonTrapPortID.setStatus('current')
apEnvMonMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 4))
apEnvMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0))
apEnvMonI2CFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 1))
if mibBuilder.loadTexts: apEnvMonI2CFailNotification.setStatus('current')
apEnvMonStatusChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 2)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapInstance"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPreviousState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapCurrentState"))
if mibBuilder.loadTexts: apEnvMonStatusChangeNotification.setStatus('current')
apEnvMonTempChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 3)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotID"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPreviousState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapCurrentState"))
if mibBuilder.loadTexts: apEnvMonTempChangeNotification.setStatus('current')
apEnvMonVoltageChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 4)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotID"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPreviousState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapCurrentState"))
if mibBuilder.loadTexts: apEnvMonVoltageChangeNotification.setStatus('current')
apEnvMonPortChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 5)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPortType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPresence"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotID"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPortID"))
if mibBuilder.loadTexts: apEnvMonPortChangeNotification.setStatus('current')
apEnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5))
apEnvMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 1))
apEnvMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2))
apEnvMonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 1)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonI2CState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusValue"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusValue"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusValue"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyStatusType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyStatusDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardStatusType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardStatusDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonEnableStatChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonGroup = apEnvMonGroup.setStatus('current')
apEnvMonNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 3)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonStatusChangeNotification"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonI2CFailNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonNotifyGroup = apEnvMonNotifyGroup.setStatus('current')
apEnvMonExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 4)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageSlotID"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageSlotType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureSlotID"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureSlotType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanSlotID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonExtGroup = apEnvMonExtGroup.setStatus('current')
apEnvMonCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 5)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardHealthScore"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardRedundancy"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreIndex"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreUsage"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreRamDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreRamUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCardGroup = apEnvMonCardGroup.setStatus('current')
apEnvMonExtNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 6)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonTempChangeNotification"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonExtNotifyGroup = apEnvMonExtNotifyGroup.setStatus('current')
apEnvMonPortNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 7)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonPortChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortNotifyGroup = apEnvMonPortNotifyGroup.setStatus('current')
apEnvMonTempNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 8)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonTempChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonTempNotifyGroup = apEnvMonTempNotifyGroup.setStatus('current')
apEnvMonCardOnlyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 9)).setObjects(("ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardType"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardDescr"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardHealthScore"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardState"), ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardRedundancy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCardOnlyGroup = apEnvMonCardOnlyGroup.setStatus('current')
mibBuilder.exportSymbols("ACMEPACKET-ENVMON-MIB", apEnvMonCpuCoreEntry=apEnvMonCpuCoreEntry, apEnvMonTrapInstance=apEnvMonTrapInstance, apEnvMonCpuCoreUsage=apEnvMonCpuCoreUsage, apEnvMonVoltageStatusTable=apEnvMonVoltageStatusTable, apEnvMonVoltageStatusDescr=apEnvMonVoltageStatusDescr, apEnvMonObjects=apEnvMonObjects, apEnvMonI2CFailNotification=apEnvMonI2CFailNotification, apEnvMonPowerSupplyStatusIndex=apEnvMonPowerSupplyStatusIndex, apEnvMonGroup=apEnvMonGroup, apEnvMonMIBNotificationPrefix=apEnvMonMIBNotificationPrefix, apEnvMonPhyCardStatusDescr=apEnvMonPhyCardStatusDescr, apEnvMonVoltageStatusValue=apEnvMonVoltageStatusValue, apEnvMonVoltageObjects=apEnvMonVoltageObjects, apEnvMonPhyCardStatusIndex=apEnvMonPhyCardStatusIndex, apEnvMonTrapSlotID=apEnvMonTrapSlotID, apEnvMonExtGroup=apEnvMonExtGroup, apEnvMonVoltageChangeNotification=apEnvMonVoltageChangeNotification, apEnvMonFanStatusEntry=apEnvMonFanStatusEntry, apEnvMonTemperatureSlotID=apEnvMonTemperatureSlotID, apEnvMonPowerSupplyObjects=apEnvMonPowerSupplyObjects, apEnvMonTrapPreviousState=apEnvMonTrapPreviousState, apEnvMonPowerSupplyStatusTable=apEnvMonPowerSupplyStatusTable, apEnvMonFanStatusDescr=apEnvMonFanStatusDescr, apEnvMonPhyCardStatusTable=apEnvMonPhyCardStatusTable, apEnvMonTemperatureStatusIndex=apEnvMonTemperatureStatusIndex, apEnvMonMIBConformance=apEnvMonMIBConformance, ApEnvMonState=ApEnvMonState, apEnvMonCardOnlyGroup=apEnvMonCardOnlyGroup, apEnvMonCardSlot=apEnvMonCardSlot, apEnvMonMIBNotifications=apEnvMonMIBNotifications, apEnvMonTemperatureStatusEntry=apEnvMonTemperatureStatusEntry, apEnvMonCpuCoreIndex=apEnvMonCpuCoreIndex, apEnvMonI2CState=apEnvMonI2CState, apEnvMonFanSlotID=apEnvMonFanSlotID, apEnvMonCardObjects=apEnvMonCardObjects, apEnvMonPortNotifyGroup=apEnvMonPortNotifyGroup, apEnvMonCpuCoreState=apEnvMonCpuCoreState, apEnvMonVoltageStatusEntry=apEnvMonVoltageStatusEntry, apEnvMonNotificationObjects=apEnvMonNotificationObjects, apEnvMonPhyCardStatusEntry=apEnvMonPhyCardStatusEntry, apEnvMonCardTable=apEnvMonCardTable, apEnvMonCardType=apEnvMonCardType, apEnvMonNotifyGroup=apEnvMonNotifyGroup, apEnvMonFanObjects=apEnvMonFanObjects, apEnvMonPortChangeNotification=apEnvMonPortChangeNotification, apEnvMonTrapCurrentState=apEnvMonTrapCurrentState, apEnvMonFanStatusTable=apEnvMonFanStatusTable, apEnvMonVoltageSlotType=apEnvMonVoltageSlotType, apEnvMonPowerSupplyState=apEnvMonPowerSupplyState, apEnvMonTemperatureState=apEnvMonTemperatureState, apEnvMonExtNotifyGroup=apEnvMonExtNotifyGroup, apEnvMonCardEntry=apEnvMonCardEntry, apEnvMonTrapPortID=apEnvMonTrapPortID, apEnvMonTemperatureSlotType=apEnvMonTemperatureSlotType, apEnvMonPowerSupplyStatusType=apEnvMonPowerSupplyStatusType, apEnvMonTrapSlotType=apEnvMonTrapSlotType, apEnvMonCardDescr=apEnvMonCardDescr, apEnvMonFanStatusType=apEnvMonFanStatusType, apEnvMonCpuCoreRamDescr=apEnvMonCpuCoreRamDescr, apEnvMonEnableStatChangeNotif=apEnvMonEnableStatChangeNotif, apEnvMonVoltageState=apEnvMonVoltageState, apEnvMonTemperatureStatusValue=apEnvMonTemperatureStatusValue, apEnvMonCpuCoreDescr=apEnvMonCpuCoreDescr, apEnvMonFanStatusValue=apEnvMonFanStatusValue, apEnvMonMIBNotificationEnables=apEnvMonMIBNotificationEnables, apEnvMonStatusChangeNotification=apEnvMonStatusChangeNotification, apEnvMonVoltageStatusType=apEnvMonVoltageStatusType, apEnvMonCardState=apEnvMonCardState, apEnvMonMIBCompliances=apEnvMonMIBCompliances, apEnvMonTemperatureStatusType=apEnvMonTemperatureStatusType, apEnvMonTempNotifyGroup=apEnvMonTempNotifyGroup, apEnvMonModule=apEnvMonModule, apEnvMonCardGroup=apEnvMonCardGroup, apEnvMonPowerSupplyStatusDescr=apEnvMonPowerSupplyStatusDescr, PYSNMP_MODULE_ID=apEnvMonModule, apEnvMonMIBGroups=apEnvMonMIBGroups, apEnvMonPhyCardStatusType=apEnvMonPhyCardStatusType, apEnvMonPowerSupplyStatusEntry=apEnvMonPowerSupplyStatusEntry, apEnvMonTemperatureObjects=apEnvMonTemperatureObjects, apEnvMonCpuCoreTable=apEnvMonCpuCoreTable, apEnvMonCardRedundancy=apEnvMonCardRedundancy, apEnvMonTrapPresence=apEnvMonTrapPresence, apEnvMonPhyCardObjects=apEnvMonPhyCardObjects, apEnvMonTemperatureStatusDescr=apEnvMonTemperatureStatusDescr, apEnvMonCpuCoreRamUsage=apEnvMonCpuCoreRamUsage, apEnvMonTemperatureStatusTable=apEnvMonTemperatureStatusTable, apEnvMonCardHealthScore=apEnvMonCardHealthScore, apEnvMonTempChangeNotification=apEnvMonTempChangeNotification, apEnvMonFanState=apEnvMonFanState, apEnvMonFanStatusIndex=apEnvMonFanStatusIndex, apEnvMonTrapPortType=apEnvMonTrapPortType, apEnvMonPhyCardState=apEnvMonPhyCardState, apEnvMonVoltageStatusIndex=apEnvMonVoltageStatusIndex, apEnvMonVoltageSlotID=apEnvMonVoltageSlotID)
