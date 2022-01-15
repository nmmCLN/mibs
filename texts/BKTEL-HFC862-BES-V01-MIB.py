#
# PySNMP MIB module BKTEL-HFC862-BES-V01-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-BES-V01-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:10:07 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
modules, DisplayString, TruthValue, ModuleWidthValue, PerceivedSeverityValue, NESlotValue = mibBuilder.importSymbols("BKTEL-HFC862-BASE-MIB", "modules", "DisplayString", "TruthValue", "ModuleWidthValue", "PerceivedSeverityValue", "NESlotValue")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Unsigned32, experimental, Counter64, MibIdentifier, TimeTicks, ObjectIdentity, NotificationType, IpAddress, Gauge32, enterprises, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Unsigned32", "experimental", "Counter64", "MibIdentifier", "TimeTicks", "ObjectIdentity", "NotificationType", "IpAddress", "Gauge32", "enterprises", "NotificationType", "Bits")
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
if mibBuilder.loadTexts: besCommonNumberOfModules.setDescription('Number of modules in table.')
besCommonTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2), )
if mibBuilder.loadTexts: besCommonTable.setStatus('mandatory')
if mibBuilder.loadTexts: besCommonTable.setDescription('The table contains all modules of the BES-type in the NE')
besCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besCommonEntry.setStatus('mandatory')
if mibBuilder.loadTexts: besCommonEntry.setDescription('Common-Values for a module.')
besNESlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 1), NESlotValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besNESlot.setStatus('mandatory')
if mibBuilder.loadTexts: besNESlot.setDescription('The slot number of the chassis for which this\n        entry contains management information.')
besCommonType = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: besCommonType.setStatus('mandatory')
if mibBuilder.loadTexts: besCommonType.setDescription('The type of physical module. modSlotEmpty indicates\n         an empty slot.  A Value of modSlotUnknown indicates\n         that the type of module is unknown.')
besCommonDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besCommonDescr.setStatus('mandatory')
if mibBuilder.loadTexts: besCommonDescr.setDescription('A textual description of the module.\n        If not available, this Value should be\n        set to a zero length string.')
besCommonFirmwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: besCommonFirmwareId.setStatus('mandatory')
if mibBuilder.loadTexts: besCommonFirmwareId.setDescription('The firmware Id of the module.')
besCommonModuleWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 5), ModuleWidthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besCommonModuleWidth.setStatus('optional')
if mibBuilder.loadTexts: besCommonModuleWidth.setDescription('The width of the module in multiples of slots (1, 2, ...)')
besMeasuringValuesTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1), )
if mibBuilder.loadTexts: besMeasuringValuesTable.setStatus('mandatory')
if mibBuilder.loadTexts: besMeasuringValuesTable.setDescription('')
besMeasuringValuesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besMeasuringValuesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: besMeasuringValuesEntry.setDescription('Common-Values for a module.')
besTemperatureLoLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureLoLo.setStatus('mandatory')
if mibBuilder.loadTexts: besTemperatureLoLo.setDescription('Device temperature low alarm threshold in 0.1 celsius degrees.')
besTemperatureLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureLo.setStatus('mandatory')
if mibBuilder.loadTexts: besTemperatureLo.setDescription('Device temperature low warning threshold in 0.1 celsius degrees.')
besTemperatureValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureValue.setStatus('mandatory')
if mibBuilder.loadTexts: besTemperatureValue.setDescription('Device temperature in 0.1 celsius degrees.')
besTemperatureHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureHi.setStatus('mandatory')
if mibBuilder.loadTexts: besTemperatureHi.setDescription('Device temperature high warning threshold in 0.1 celsius degrees.')
besTemperatureHiHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besTemperatureHiHi.setStatus('mandatory')
if mibBuilder.loadTexts: besTemperatureHiHi.setDescription('Device temperature high alarm threshold in 0.1 celsius degrees.')
besInputVoltageLoLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageLoLo.setStatus('mandatory')
if mibBuilder.loadTexts: besInputVoltageLoLo.setDescription('The input supply voltage low alarm threshold in steps of 0.1 Volts.')
besInputVoltageLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageLo.setStatus('mandatory')
if mibBuilder.loadTexts: besInputVoltageLo.setDescription('The input supply voltage low warning threshold in steps of 0.1 Volts.')
besInputVoltageValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageValue.setStatus('mandatory')
if mibBuilder.loadTexts: besInputVoltageValue.setDescription("The input supply voltage in steps of 0.1 Volts.\n                     Input supply voltage nominal value, see 'besDisplayInputVoltageNominal'")
besInputVoltageHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageHi.setStatus('mandatory')
if mibBuilder.loadTexts: besInputVoltageHi.setDescription('The input supply voltage high warning threshold in steps of 0.1 Volts.')
besInputVoltageHiHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besInputVoltageHiHi.setStatus('mandatory')
if mibBuilder.loadTexts: besInputVoltageHiHi.setDescription('The input supply voltage high alarm threshold in steps of 0.1 Volts.')
besStatesTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1), )
if mibBuilder.loadTexts: besStatesTable.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesTable.setDescription('')
besStatesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besStatesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesEntry.setDescription('Alarms for a module.')
besStatesBootloader = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 1), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesBootloader.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesBootloader.setDescription('The device is running in bootloader mode\n             without a legal application software.')
besStatesCommLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 2), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesCommLoss.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesCommLoss.setDescription('The NEC has lost the connection to the device.\n             Reason may be a removed or defective device.\n             Note that this state is set by the NEC and not\n             by the device')
besStatesTemperatureLow = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 3), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesTemperatureLow.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesTemperatureLow.setDescription('Device temperature low')
besStatesTemperatureHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 4), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesTemperatureHigh.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesTemperatureHigh.setDescription('Device temperature high')
besStatesInputVoltageLow = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 5), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesInputVoltageLow.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesInputVoltageLow.setDescription('Input supply voltage low')
besStatesInputVoltageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 6), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besStatesInputVoltageHigh.setStatus('mandatory')
if mibBuilder.loadTexts: besStatesInputVoltageHigh.setDescription('Input supply voltage high')
besControlTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1), )
if mibBuilder.loadTexts: besControlTable.setStatus('mandatory')
if mibBuilder.loadTexts: besControlTable.setDescription('')
besControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besControlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: besControlEntry.setDescription('Alarms for a module.')
besControlReset = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besControlReset.setStatus('mandatory')
if mibBuilder.loadTexts: besControlReset.setDescription('Reset the module.')
besControlModuleLedBlink = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besControlModuleLedBlink.setStatus('mandatory')
if mibBuilder.loadTexts: besControlModuleLedBlink.setDescription("Writing this variable to true(1) lets the device's\n        modul LED blink green for 10 seconds.\n        Writing this variable to false(2) stbes blinking at once.\n        This variable always returns false(2) on read requests")
besConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1), )
if mibBuilder.loadTexts: besConfigurationTable.setStatus('mandatory')
if mibBuilder.loadTexts: besConfigurationTable.setDescription('')
besConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besConfigurationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: besConfigurationEntry.setDescription('')
besConfigNESlotWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 1), NESlotWriteValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besConfigNESlotWrite.setStatus('optional')
if mibBuilder.loadTexts: besConfigNESlotWrite.setDescription("By writing this variable a slot can be assigned\n            for devices that dont support hardware slot detection.\n            Reading '-1' means that the slot position is NOT writable.")
besConfigConfigurationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: besConfigConfigurationIndex.setStatus('mandatory')
if mibBuilder.loadTexts: besConfigConfigurationIndex.setDescription('Index of the active configuration (1..besDisplayNumberOfConfigs)')
besConfigConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besConfigConfiguration.setStatus('mandatory')
if mibBuilder.loadTexts: besConfigConfiguration.setDescription('Description of the active configuration')
besDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1), )
if mibBuilder.loadTexts: besDisplayTable.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayTable.setDescription('')
besDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"))
if mibBuilder.loadTexts: besDisplayEntry.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayEntry.setDescription('')
besDisplayNumberOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayNumberOfPorts.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayNumberOfPorts.setDescription('The number of ports')
besDisplayInputVoltageNominal = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayInputVoltageNominal.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayInputVoltageNominal.setDescription('The nominal value of input voltage in 0.1 V units.')
besDisplayNumberOfConfigs = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayNumberOfConfigs.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayNumberOfConfigs.setDescription('The number of different configurations supplied')
besDisplayConfiguration1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration1.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration1.setDescription('Description of configuration no. #1')
besDisplayConfiguration2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration2.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration2.setDescription('Description of configuration no. #2')
besDisplayConfiguration3 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration3.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration3.setDescription('Description of configuration no. #3')
besDisplayConfiguration4 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration4.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration4.setDescription('Description of configuration no. #4')
besDisplayConfiguration5 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration5.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration5.setDescription('Description of configuration no. #5')
besDisplayConfiguration6 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration6.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration6.setDescription('Description of configuration no. #6')
besDisplayConfiguration7 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration7.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration7.setDescription('Description of configuration no. #7')
besDisplayConfiguration8 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration8.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration8.setDescription('Description of configuration no. #8')
besDisplayConfiguration9 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration9.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration9.setDescription('Description of configuration no. #9')
besDisplayConfiguration10 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration10.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration10.setDescription('Description of configuration no. #10')
besDisplayConfiguration11 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration11.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration11.setDescription('Description of configuration no. #11')
besDisplayConfiguration12 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration12.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration12.setDescription('Description of configuration no. #12')
besDisplayConfiguration13 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration13.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration13.setDescription('Description of configuration no. #13')
besDisplayConfiguration14 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration14.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration14.setDescription('Description of configuration no. #14')
besDisplayConfiguration15 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration15.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration15.setDescription('Description of configuration no. #15')
besDisplayConfiguration16 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayConfiguration16.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayConfiguration16.setDescription('Description of configuration no. #16')
besDisplayPortsTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1), )
if mibBuilder.loadTexts: besDisplayPortsTable.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsTable.setDescription('')
besDisplayPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"), (0, "BKTEL-HFC862-BES-V01-MIB", "besDisplayPortsPortIndex"))
if mibBuilder.loadTexts: besDisplayPortsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsEntry.setDescription('')
besDisplayPortsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsPortIndex.setDescription('Port index (1..besDisplayNumberOfPorts)')
besDisplayPortsPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsPortName.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsPortName.setDescription('Port name')
besDisplayPortsType = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 3), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsType.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsType.setDescription('Port type')
besDisplayPortsLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 4), PortLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsLinkState.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsLinkState.setDescription('Port link status')
besDisplayPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 5), PortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsStatus.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsStatus.setDescription('Port status')
besDisplayPortsDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 6), PortDuplexMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsDuplexMode.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsDuplexMode.setDescription('Port duplex mode')
besDisplayPortsSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 7), PortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsSpeed.setDescription('Port speed')
besDisplayPortsFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 8), PortFlowControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFlowControl.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsFlowControl.setDescription('Port speed')
besDisplayPortsFiberTxDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberTxDistance.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsFiberTxDistance.setDescription('Port transmission distance in units of km (Fiber ports only)')
besDisplayPortsFiberTxWavelen = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberTxWavelen.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsFiberTxWavelen.setDescription('Port transmission wavelength in units of nm (Fiber ports only)')
besDisplayPortsFiberRxWavelenMin = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberRxWavelenMin.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsFiberRxWavelenMin.setDescription('Port minimum receive wavelength in units of nm (Fiber ports only)')
besDisplayPortsFiberRxWavelenMax = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberRxWavelenMax.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsFiberRxWavelenMax.setDescription('Port maximum receive wavelength in units of nm (Fiber ports only)')
besDisplayPortsFiberSfpData = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: besDisplayPortsFiberSfpData.setStatus('mandatory')
if mibBuilder.loadTexts: besDisplayPortsFiberSfpData.setDescription('Port SFP data text (Fiber ports only)')
mibBuilder.exportSymbols("BKTEL-HFC862-BES-V01-MIB", besDisplayEntry=besDisplayEntry, besDisplayConfiguration2=besDisplayConfiguration2, besDisplayConfiguration10=besDisplayConfiguration10, besDisplayConfiguration13=besDisplayConfiguration13, besDisplayPortsTable=besDisplayPortsTable, besMeasuringValuesEntry=besMeasuringValuesEntry, besControlTable=besControlTable, besMeasuringValues=besMeasuringValues, besDisplayConfiguration9=besDisplayConfiguration9, besTemperatureValue=besTemperatureValue, besStatesCommLoss=besStatesCommLoss, besConfigurationTable=besConfigurationTable, PortFlowControl=PortFlowControl, besDisplayConfiguration12=besDisplayConfiguration12, PortStatus=PortStatus, besInputVoltageHi=besInputVoltageHi, besTemperatureLo=besTemperatureLo, besDisplayPortsFiberTxWavelen=besDisplayPortsFiberTxWavelen, besCommon=besCommon, besConfigConfigurationIndex=besConfigConfigurationIndex, besStatesTemperatureHigh=besStatesTemperatureHigh, besStatesBootloader=besStatesBootloader, PortDuplexMode=PortDuplexMode, besConfigConfiguration=besConfigConfiguration, besDisplayConfiguration8=besDisplayConfiguration8, besDisplayPortsEntry=besDisplayPortsEntry, besDisplayConfiguration16=besDisplayConfiguration16, besDisplay=besDisplay, besStatesTable=besStatesTable, besInputVoltageLo=besInputVoltageLo, besDisplayConfiguration3=besDisplayConfiguration3, besStatesEntry=besStatesEntry, besDisplayConfiguration7=besDisplayConfiguration7, besCommonEntry=besCommonEntry, besStates=besStates, besDisplayConfiguration6=besDisplayConfiguration6, besCommonFirmwareId=besCommonFirmwareId, besDisplayPortsPortName=besDisplayPortsPortName, PortSpeed=PortSpeed, besStatesInputVoltageHigh=besStatesInputVoltageHigh, besControl=besControl, besInputVoltageLoLo=besInputVoltageLoLo, besDisplayPorts=besDisplayPorts, besDisplayPortsFiberSfpData=besDisplayPortsFiberSfpData, besTemperatureLoLo=besTemperatureLoLo, besDisplayTable=besDisplayTable, besDisplayConfiguration15=besDisplayConfiguration15, besDisplayPortsFiberRxWavelenMin=besDisplayPortsFiberRxWavelenMin, besCommonDescr=besCommonDescr, besTemperatureHiHi=besTemperatureHiHi, besDisplayConfiguration5=besDisplayConfiguration5, besInputVoltageValue=besInputVoltageValue, besMeasuringValuesTable=besMeasuringValuesTable, PortLinkState=PortLinkState, besDisplayNumberOfPorts=besDisplayNumberOfPorts, NESlotWriteValue=NESlotWriteValue, besConfigNESlotWrite=besConfigNESlotWrite, besDisplayPortsStatus=besDisplayPortsStatus, besNESlot=besNESlot, besDisplayConfiguration4=besDisplayConfiguration4, besDisplayPortsLinkState=besDisplayPortsLinkState, besDisplayInputVoltageNominal=besDisplayInputVoltageNominal, besConfiguration=besConfiguration, besConfigurationEntry=besConfigurationEntry, besDisplayPortsSpeed=besDisplayPortsSpeed, besDisplayConfiguration1=besDisplayConfiguration1, besDisplayNumberOfConfigs=besDisplayNumberOfConfigs, besCommonType=besCommonType, besControlEntry=besControlEntry, besDisplayConfiguration14=besDisplayConfiguration14, besDisplayPortsFiberTxDistance=besDisplayPortsFiberTxDistance, besDisplayConfiguration11=besDisplayConfiguration11, PortType=PortType, besControlReset=besControlReset, besCommonNumberOfModules=besCommonNumberOfModules, besDisplayPortsFlowControl=besDisplayPortsFlowControl, besDisplayPortsPortIndex=besDisplayPortsPortIndex, besTemperatureHi=besTemperatureHi, besDisplayPortsType=besDisplayPortsType, besControlModuleLedBlink=besControlModuleLedBlink, bes=bes, besCommonTable=besCommonTable, besDisplayPortsFiberRxWavelenMax=besDisplayPortsFiberRxWavelenMax, besStatesTemperatureLow=besStatesTemperatureLow, besInputVoltageHiHi=besInputVoltageHiHi, besStatesInputVoltageLow=besStatesInputVoltageLow, besDisplayPortsDuplexMode=besDisplayPortsDuplexMode, besCommonModuleWidth=besCommonModuleWidth)
