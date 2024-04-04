#
# PySNMP MIB module BKTEL-HFC862-BES-V01-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-BES-V01-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:22 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleWidthValue, PerceivedSeverityValue, TruthValue, DisplayString, modules, NESlotValue = mibBuilder.importSymbols("BKTEL-HFC862-BASE-MIB", "ModuleWidthValue", "PerceivedSeverityValue", "TruthValue", "DisplayString", "modules", "NESlotValue")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Unsigned32, TimeTicks, Gauge32, enterprises, IpAddress, Integer32, Bits, experimental, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Unsigned32", "TimeTicks", "Gauge32", "enterprises", "IpAddress", "Integer32", "Bits", "experimental", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bes = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114))
besCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1))
besStates = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2))
besConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3))
besControl = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4))
besMeasuringValues = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5))
besDisplay = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6))
besDisplayPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56))
class PortType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("typeCopper", 1), ("typeFiber", 2))

class PortLinkState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("linkDown", 1), ("linkUp", 2))

class PortStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("statusUnknown", 1), ("statusInit", 2), ("statusValid", 3), ("statusBusy", 4), ("statusEmpty", 5), ("statusInvalid", 6), ("statusLossOfSignal", 7))

class PortDuplexMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("duplexFull", 1), ("duplexHalf", 2))

class PortSpeed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10, 100, 1000))
    namedValues = NamedValues(("speedUnknown", 0), ("speed10Mbps", 10), ("speed100Mbps", 100), ("speed1000Mbps", 1000))

class PortFlowControl(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("flowControlDisabled", 1), ("flowControlEnabled", 2))

class NESlotWriteValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 99)

besCommonNumberOfModules = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: besCommonNumberOfModules.setStatus('mandatory')
besCommonTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2), )
if mibBuilder.loadTexts: besCommonTable.setStatus('mandatory')
besCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besCommonEntry.setStatus('mandatory')
besNESlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 1), NESlotValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besNESlot.setStatus('mandatory')
besCommonType = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: besCommonType.setStatus('mandatory')
besCommonDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besCommonDescr.setStatus('mandatory')
besCommonFirmwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: besCommonFirmwareId.setStatus('mandatory')
besCommonModuleWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 5), ModuleWidthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besCommonModuleWidth.setStatus('optional')
besMeasuringValuesTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1), )
if mibBuilder.loadTexts: besMeasuringValuesTable.setStatus('mandatory')
besMeasuringValuesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besMeasuringValuesEntry.setStatus('mandatory')
besTemperatureLoLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureLoLo.setStatus('mandatory')
besTemperatureLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureLo.setStatus('mandatory')
besTemperatureValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureValue.setStatus('mandatory')
besTemperatureHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureHi.setStatus('mandatory')
besTemperatureHiHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureHiHi.setStatus('mandatory')
besInputVoltageLoLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageLoLo.setStatus('mandatory')
besInputVoltageLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageLo.setStatus('mandatory')
besInputVoltageValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageValue.setStatus('mandatory')
besInputVoltageHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageHi.setStatus('mandatory')
besInputVoltageHiHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageHiHi.setStatus('mandatory')
besStatesTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1), )
if mibBuilder.loadTexts: besStatesTable.setStatus('mandatory')
besStatesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besStatesEntry.setStatus('mandatory')
besStatesBootloader = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 1), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesBootloader.setStatus('mandatory')
besStatesCommLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 2), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesCommLoss.setStatus('mandatory')
besStatesTemperatureLow = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 3), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesTemperatureLow.setStatus('mandatory')
besStatesTemperatureHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 4), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesTemperatureHigh.setStatus('mandatory')
besStatesInputVoltageLow = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 5), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesInputVoltageLow.setStatus('mandatory')
besStatesInputVoltageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 6), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesInputVoltageHigh.setStatus('mandatory')
besControlTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1), )
if mibBuilder.loadTexts: besControlTable.setStatus('mandatory')
besControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besControlEntry.setStatus('mandatory')
besControlReset = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besControlReset.setStatus('mandatory')
besControlModuleLedBlink = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besControlModuleLedBlink.setStatus('mandatory')
besConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1), )
if mibBuilder.loadTexts: besConfigurationTable.setStatus('mandatory')
besConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besConfigurationEntry.setStatus('mandatory')
besConfigNESlotWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 1), NESlotWriteValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besConfigNESlotWrite.setStatus('optional')
besConfigConfigurationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besConfigConfigurationIndex.setStatus('mandatory')
besConfigConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besConfigConfiguration.setStatus('mandatory')
besDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1), )
if mibBuilder.loadTexts: besDisplayTable.setStatus('mandatory')
besDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besDisplayEntry.setStatus('mandatory')
besDisplayNumberOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayNumberOfPorts.setStatus('mandatory')
besDisplayInputVoltageNominal = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayInputVoltageNominal.setStatus('mandatory')
besDisplayNumberOfConfigs = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayNumberOfConfigs.setStatus('mandatory')
besDisplayConfiguration1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration1.setStatus('mandatory')
besDisplayConfiguration2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration2.setStatus('mandatory')
besDisplayConfiguration3 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration3.setStatus('mandatory')
besDisplayConfiguration4 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration4.setStatus('mandatory')
besDisplayConfiguration5 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration5.setStatus('mandatory')
besDisplayConfiguration6 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration6.setStatus('mandatory')
besDisplayConfiguration7 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration7.setStatus('mandatory')
besDisplayConfiguration8 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration8.setStatus('mandatory')
besDisplayConfiguration9 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration9.setStatus('mandatory')
besDisplayConfiguration10 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration10.setStatus('mandatory')
besDisplayConfiguration11 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration11.setStatus('mandatory')
besDisplayConfiguration12 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration12.setStatus('mandatory')
besDisplayConfiguration13 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration13.setStatus('mandatory')
besDisplayConfiguration14 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration14.setStatus('mandatory')
besDisplayConfiguration15 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration15.setStatus('mandatory')
besDisplayConfiguration16 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration16.setStatus('mandatory')
besDisplayPortsTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1), )
if mibBuilder.loadTexts: besDisplayPortsTable.setStatus('mandatory')
besDisplayPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"), (0, "BKTEL-HFC862-BES-V01-MIB", "besDisplayPortsPortIndex"))
if mibBuilder.loadTexts: besDisplayPortsEntry.setStatus('mandatory')
besDisplayPortsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsPortIndex.setStatus('mandatory')
besDisplayPortsPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsPortName.setStatus('mandatory')
besDisplayPortsType = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 3), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsType.setStatus('mandatory')
besDisplayPortsLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 4), PortLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsLinkState.setStatus('mandatory')
besDisplayPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 5), PortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsStatus.setStatus('mandatory')
besDisplayPortsDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 6), PortDuplexMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsDuplexMode.setStatus('mandatory')
besDisplayPortsSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 7), PortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsSpeed.setStatus('mandatory')
besDisplayPortsFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 8), PortFlowControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFlowControl.setStatus('mandatory')
besDisplayPortsFiberTxDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberTxDistance.setStatus('mandatory')
besDisplayPortsFiberTxWavelen = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberTxWavelen.setStatus('mandatory')
besDisplayPortsFiberRxWavelenMin = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberRxWavelenMin.setStatus('mandatory')
besDisplayPortsFiberRxWavelenMax = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberRxWavelenMax.setStatus('mandatory')
besDisplayPortsFiberSfpData = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberSfpData.setStatus('mandatory')
mibBuilder.exportSymbols("BKTEL-HFC862-BES-V01-MIB", besInputVoltageLo=besInputVoltageLo, besCommonEntry=besCommonEntry, besDisplayConfiguration13=besDisplayConfiguration13, besMeasuringValues=besMeasuringValues, besTemperatureHiHi=besTemperatureHiHi, besCommonNumberOfModules=besCommonNumberOfModules, besDisplayConfiguration10=besDisplayConfiguration10, PortSpeed=PortSpeed, besStatesInputVoltageHigh=besStatesInputVoltageHigh, besDisplayNumberOfPorts=besDisplayNumberOfPorts, besDisplayConfiguration1=besDisplayConfiguration1, besDisplayPortsSpeed=besDisplayPortsSpeed, besDisplayConfiguration4=besDisplayConfiguration4, besDisplay=besDisplay, PortFlowControl=PortFlowControl, besMeasuringValuesTable=besMeasuringValuesTable, besStatesTable=besStatesTable, besDisplayConfiguration12=besDisplayConfiguration12, besDisplayPortsFiberRxWavelenMin=besDisplayPortsFiberRxWavelenMin, besDisplayEntry=besDisplayEntry, besNESlot=besNESlot, besDisplayPortsTable=besDisplayPortsTable, besConfigConfiguration=besConfigConfiguration, besDisplayInputVoltageNominal=besDisplayInputVoltageNominal, besDisplayConfiguration14=besDisplayConfiguration14, besInputVoltageLoLo=besInputVoltageLoLo, besConfigurationTable=besConfigurationTable, besDisplayPortsFiberTxDistance=besDisplayPortsFiberTxDistance, besInputVoltageHi=besInputVoltageHi, besStatesTemperatureHigh=besStatesTemperatureHigh, besDisplayPortsFlowControl=besDisplayPortsFlowControl, besDisplayPortsLinkState=besDisplayPortsLinkState, besDisplayPortsFiberTxWavelen=besDisplayPortsFiberTxWavelen, besDisplayPortsPortIndex=besDisplayPortsPortIndex, besDisplayConfiguration15=besDisplayConfiguration15, besDisplayConfiguration6=besDisplayConfiguration6, besTemperatureLoLo=besTemperatureLoLo, besDisplayPortsEntry=besDisplayPortsEntry, besMeasuringValuesEntry=besMeasuringValuesEntry, besDisplayConfiguration9=besDisplayConfiguration9, bes=bes, besDisplayConfiguration16=besDisplayConfiguration16, besDisplayPortsPortName=besDisplayPortsPortName, besStatesInputVoltageLow=besStatesInputVoltageLow, besInputVoltageValue=besInputVoltageValue, besStatesTemperatureLow=besStatesTemperatureLow, besStates=besStates, besCommonType=besCommonType, PortDuplexMode=PortDuplexMode, besControl=besControl, besCommonModuleWidth=besCommonModuleWidth, besControlModuleLedBlink=besControlModuleLedBlink, besDisplayPorts=besDisplayPorts, besDisplayPortsType=besDisplayPortsType, besDisplayPortsDuplexMode=besDisplayPortsDuplexMode, besStatesBootloader=besStatesBootloader, besInputVoltageHiHi=besInputVoltageHiHi, besConfigNESlotWrite=besConfigNESlotWrite, besCommonDescr=besCommonDescr, besDisplayTable=besDisplayTable, PortStatus=PortStatus, besCommonTable=besCommonTable, besConfigConfigurationIndex=besConfigConfigurationIndex, besDisplayConfiguration5=besDisplayConfiguration5, besTemperatureValue=besTemperatureValue, besStatesCommLoss=besStatesCommLoss, besDisplayPortsFiberRxWavelenMax=besDisplayPortsFiberRxWavelenMax, besDisplayConfiguration2=besDisplayConfiguration2, besControlTable=besControlTable, besDisplayPortsStatus=besDisplayPortsStatus, NESlotWriteValue=NESlotWriteValue, besControlEntry=besControlEntry, besDisplayNumberOfConfigs=besDisplayNumberOfConfigs, besControlReset=besControlReset, besDisplayConfiguration8=besDisplayConfiguration8, besConfiguration=besConfiguration, besDisplayConfiguration7=besDisplayConfiguration7, besTemperatureLo=besTemperatureLo, PortType=PortType, besDisplayConfiguration11=besDisplayConfiguration11, PortLinkState=PortLinkState, besStatesEntry=besStatesEntry, besTemperatureHi=besTemperatureHi, besDisplayConfiguration3=besDisplayConfiguration3, besDisplayPortsFiberSfpData=besDisplayPortsFiberSfpData, besCommonFirmwareId=besCommonFirmwareId, besConfigurationEntry=besConfigurationEntry, besCommon=besCommon)
