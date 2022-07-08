#
# PySNMP MIB module SOCOMECPDU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/socomec/SOCOMECPDU-MIB.mib
# Produced by pysmi-1.1.8 at Fri Jul  8 09:28:34 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, enterprises, Counter32, ModuleIdentity, Bits, ObjectIdentity, Gauge32, NotificationType, iso, Unsigned32, Counter64, IpAddress, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "enterprises", "Counter32", "ModuleIdentity", "Bits", "ObjectIdentity", "Gauge32", "NotificationType", "iso", "Unsigned32", "Counter64", "IpAddress", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
socomec = MibIdentifier((1, 3, 6, 1, 4, 1, 4555))
ups = MibIdentifier((1, 3, 6, 1, 4, 1, 4555, 2))
pdu = MibIdentifier((1, 3, 6, 1, 4, 1, 4555, 2, 30))
dpduIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1))
dpduOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2))
dpduAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3))
dpduEnvironment = MibIdentifier((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4))
dpduTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20))
dpduIdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduIdentManufacturer.setStatus('mandatory')
if mibBuilder.loadTexts: dpduIdentManufacturer.setDescription('The EnviroStation Vendor.')
dpduIdentModel = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduIdentModel.setStatus('mandatory')
if mibBuilder.loadTexts: dpduIdentModel.setDescription('The PDU Model designation.')
dpduIdentSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduIdentSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dpduIdentSerialNumber.setDescription('The PDU serial number')
dpduIdentPDUFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduIdentPDUFirmwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: dpduIdentPDUFirmwareVersion.setDescription('The PDU firmware version')
dpduIdentAgentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduIdentAgentSoftwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: dpduIdentAgentSoftwareVersion.setDescription('The PDU NMC software version')
dpduIdentName = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduIdentName.setStatus('mandatory')
if mibBuilder.loadTexts: dpduIdentName.setDescription('A string identifying the PDU. This object should be\n               set by the administrator.')
dpduAttachedDevices = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduAttachedDevices.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAttachedDevices.setDescription('A string identifying the devices attached to the\n               output(s) of the PDU. This object should be set by\n               the administrator.')
dpduOutputFrequency = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2, 1), Integer32()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduOutputFrequency.setStatus('mandatory')
if mibBuilder.loadTexts: dpduOutputFrequency.setDescription('The present output frequency in 1/10 Hz.')
dpduOutputVoltage1 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2, 2), Integer32()).setUnits('0.1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduOutputVoltage1.setStatus('mandatory')
if mibBuilder.loadTexts: dpduOutputVoltage1.setDescription('The Output line 1 voltage of the PDU system in 1/10 V.')
dpduOutputCurrent1 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2, 3), Integer32()).setUnits('0.1 A').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduOutputCurrent1.setStatus('mandatory')
if mibBuilder.loadTexts: dpduOutputCurrent1.setDescription('The Output line 1 current of the PDU system in 1/10 A.')
dpduOutputVoltage2 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2, 4), Integer32()).setUnits('0.1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduOutputVoltage2.setStatus('mandatory')
if mibBuilder.loadTexts: dpduOutputVoltage2.setDescription('The Output line 2 voltage of the PDU system in 1/10 V.')
dpduOutputCurrent2 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2, 5), Integer32()).setUnits('0.1 A').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduOutputCurrent2.setStatus('mandatory')
if mibBuilder.loadTexts: dpduOutputCurrent2.setDescription('The Output line 2 current of the PDU system in 1/10 A.')
dpduOutputVoltage3 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2, 6), Integer32()).setUnits('0.1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduOutputVoltage3.setStatus('mandatory')
if mibBuilder.loadTexts: dpduOutputVoltage3.setDescription('The Output line 3 voltage of the PDU system in 1/10 V.')
dpduOutputCurrent3 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 2, 7), Integer32()).setUnits('0.1 A').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduOutputCurrent3.setStatus('mandatory')
if mibBuilder.loadTexts: dpduOutputCurrent3.setDescription('The Output line 3 current of the PDU system in 1/10 A.')
dpduAlarmDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmDisconnect.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmDisconnect.setDescription('Does the PDU disconnect?')
dpduAlarmL1LoadMajor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL1LoadMajor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL1LoadMajor.setDescription('L1 load major alarm')
dpduAlarmL1LoadMinor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL1LoadMinor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL1LoadMinor.setDescription('L1 load minor alarm')
dpduAlarmL1OutVoltMajor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL1OutVoltMajor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL1OutVoltMajor.setDescription('L1 output votage major alarm')
dpduAlarmL1OutVoltMinor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL1OutVoltMinor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL1OutVoltMinor.setDescription('L1 output voltage minor alarm')
dpduAlarmL2LoadMajor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL2LoadMajor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL2LoadMajor.setDescription('L2 load major alarm')
dpduAlarmL2LoadMinor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL2LoadMinor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL2LoadMinor.setDescription('L2 load minor alarm')
dpduAlarmL2OutVoltMajor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL2OutVoltMajor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL2OutVoltMajor.setDescription('L2 output votage major alarm')
dpduAlarmL2OutVoltMinor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL2OutVoltMinor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL2OutVoltMinor.setDescription('L2 output voltage minor alarm')
dpduAlarmL3LoadMajor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL3LoadMajor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL3LoadMajor.setDescription('L3 load major alarm')
dpduAlarmL3LoadMinor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL3LoadMinor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL3LoadMinor.setDescription('L3 load minor alarm')
dpduAlarmL3OutVoltMajor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL3OutVoltMajor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL3OutVoltMajor.setDescription('L3 output votage major alarm')
dpduAlarmL3OutVoltMinor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL3OutVoltMinor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL3OutVoltMinor.setDescription('L3 output voltage minor alarm')
dpduAlarmL12LoadMajor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL12LoadMajor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL12LoadMajor.setDescription('L1, L2 load major alarm')
dpduAlarmL12LoadMinor = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 3, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmL12LoadMinor.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmL12LoadMinor.setDescription('L1, L2 load minor alarm')
dpduEnvTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 1), Integer32()).setUnits('0.1 Degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduEnvTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvTemperature.setDescription('The ambient environmental temperature.')
dpduEnvHumidity = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 2), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduEnvHumidity.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvHumidity.setDescription('The environmental humidity.')
dpduEnvSetTemperatureWarnLimit = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 3), Integer32()).setUnits('Degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetTemperatureWarnLimit.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetTemperatureWarnLimit.setDescription('Alarm dpduEnvOverWarnTemperature on when the environmental\n\t\ttemperature over the value.')
dpduEnvSetTemperatureAlarmLimit = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 4), Integer32()).setUnits('Degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetTemperatureAlarmLimit.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetTemperatureAlarmLimit.setDescription('Alarm dpduEnvOverAlarmTemperature on when the environmental\n\t\ttemperature over the value.')
dpduEnvSetHumidityWarnLimit = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 5), Integer32()).setUnits('percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetHumidityWarnLimit.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetHumidityWarnLimit.setDescription('Alarm dpduEnvOverWarnHumidity on when the environmental\n\t\thumidity over the value.')
dpduEnvSetHumidityAlarmLimit = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 6), Integer32()).setUnits('percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetHumidityAlarmLimit.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetHumidityAlarmLimit.setDescription('Alarm dpduEnvOverAlarmHumidity on when the environmental\n\t\thumidity over the value.')
dpduEnvSetEnvRelay1 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOpen", 0), ("normalClose", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetEnvRelay1.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetEnvRelay1.setDescription('')
dpduEnvSetEnvRelay2 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOpen", 0), ("normalClose", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetEnvRelay2.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetEnvRelay2.setDescription('')
dpduEnvSetEnvRelay3 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOpen", 0), ("normalClose", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetEnvRelay3.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetEnvRelay3.setDescription('')
dpduEnvSetEnvRelay4 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOpen", 0), ("normalClose", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpduEnvSetEnvRelay4.setStatus('mandatory')
if mibBuilder.loadTexts: dpduEnvSetEnvRelay4.setDescription('')
dpduWarnOverEnvTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduWarnOverEnvTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: dpduWarnOverEnvTemperature.setDescription('Does the environment over warning temperature?')
dpduAlarmOverEnvTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmOverEnvTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmOverEnvTemperature.setDescription('Does the environment over alarm temperature?')
dpduWarnmOverEnvHumidity = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduWarnmOverEnvHumidity.setStatus('mandatory')
if mibBuilder.loadTexts: dpduWarnmOverEnvHumidity.setDescription('Does the environment over warn humidity?')
dpduAlarmOverEnvHumidity = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmOverEnvHumidity.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmOverEnvHumidity.setDescription('Does the environment over alarm humidity?')
dpduAlarmEnvRelay1 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmEnvRelay1.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmEnvRelay1.setDescription('The alarm status of relay1.')
dpduAlarmEnvRelay2 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmEnvRelay2.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmEnvRelay2.setDescription(' The alarm status of relay2.')
dpduAlarmEnvRelay3 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmEnvRelay3.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmEnvRelay3.setDescription(' The alarm status of relay3.')
dpduAlarmEnvRelay4 = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmEnvRelay4.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmEnvRelay4.setDescription(' The alarm status of relay4.')
dpduAlarmEnvDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 4555, 2, 30, 4, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpduAlarmEnvDisconnect.setStatus('mandatory')
if mibBuilder.loadTexts: dpduAlarmEnvDisconnect.setDescription(' To indicate the communication status of EnviroProbe.')
dpduCommunicationLost = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,1))
if mibBuilder.loadTexts: dpduCommunicationLost.setDescription('Communication with the PDU failed.')
dpduCommunicationEstablished = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,2))
if mibBuilder.loadTexts: dpduCommunicationEstablished.setDescription('Communication with the PDU reestablished.')
dpduL1LoadMajorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,3))
if mibBuilder.loadTexts: dpduL1LoadMajorAlarm.setDescription('L1 load major alarm.')
dpduL1LoadMajorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,4))
if mibBuilder.loadTexts: dpduL1LoadMajorAlarmRecover.setDescription('Recover from L1 load major alarm.')
dpduL1LoadMinorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,5))
if mibBuilder.loadTexts: dpduL1LoadMinorAlarm.setDescription('L1 load minor alarm.')
dpduL1LoadMinorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,6))
if mibBuilder.loadTexts: dpduL1LoadMinorAlarmRecover.setDescription('Recover from L1 load minor alarm.')
dpduL1OutVoltMajorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,7))
if mibBuilder.loadTexts: dpduL1OutVoltMajorAlarm.setDescription('L1 output voltage major alarm.')
dpduL1OutVoltMajorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,8))
if mibBuilder.loadTexts: dpduL1OutVoltMajorAlarmRecover.setDescription('Recover from L1 output voltage major alarm.')
dpduL1OutVoltMinorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,9))
if mibBuilder.loadTexts: dpduL1OutVoltMinorAlarm.setDescription('L1 output voltage minor alarm.')
dpduL1OutVoltMinorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,10))
if mibBuilder.loadTexts: dpduL1OutVoltMinorAlarmRecover.setDescription('Recover from L1 output voltage minor alarm.')
dpduL2LoadMajorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,11))
if mibBuilder.loadTexts: dpduL2LoadMajorAlarm.setDescription('L2 load major alarm.')
dpduL2LoadMajorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,12))
if mibBuilder.loadTexts: dpduL2LoadMajorAlarmRecover.setDescription('Recover from L2 load major alarm.')
dpduL2LoadMinorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,13))
if mibBuilder.loadTexts: dpduL2LoadMinorAlarm.setDescription('L2 load minor alarm.')
dpduL2LoadMinorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,14))
if mibBuilder.loadTexts: dpduL2LoadMinorAlarmRecover.setDescription('Recover from L2 load minor alarm.')
dpduL2OutVoltMajorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,15))
if mibBuilder.loadTexts: dpduL2OutVoltMajorAlarm.setDescription('L2 output voltage major alarm.')
dpduL2OutVoltMajorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,16))
if mibBuilder.loadTexts: dpduL2OutVoltMajorAlarmRecover.setDescription('Recover from L2 output voltage major alarm.')
dpduL2OutVoltMinorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,17))
if mibBuilder.loadTexts: dpduL2OutVoltMinorAlarm.setDescription('L2 output voltage minor alarm.')
dpduL2OutVoltMinorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,18))
if mibBuilder.loadTexts: dpduL2OutVoltMinorAlarmRecover.setDescription('Recover from L2 output voltage minor alarm.')
dpduL3LoadMajorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,19))
if mibBuilder.loadTexts: dpduL3LoadMajorAlarm.setDescription('L3 load major alarm.')
dpduL3LoadMajorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,20))
if mibBuilder.loadTexts: dpduL3LoadMajorAlarmRecover.setDescription('Recover from L3 load major alarm.')
dpduL3LoadMinorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,21))
if mibBuilder.loadTexts: dpduL3LoadMinorAlarm.setDescription('L3 load minor alarm.')
dpduL3LoadMinorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,22))
if mibBuilder.loadTexts: dpduL3LoadMinorAlarmRecover.setDescription('Recover from L3 load minor alarm.')
dpduL3OutVoltMajorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,23))
if mibBuilder.loadTexts: dpduL3OutVoltMajorAlarm.setDescription('L3 output voltage major alarm.')
dpduL3OutVoltMajorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,24))
if mibBuilder.loadTexts: dpduL3OutVoltMajorAlarmRecover.setDescription('Recover from L3 output voltage major alarm.')
dpduL3OutVoltMinorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,25))
if mibBuilder.loadTexts: dpduL3OutVoltMinorAlarm.setDescription('L3 output voltage minor alarm.')
dpduL3OutVoltMinorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,26))
if mibBuilder.loadTexts: dpduL3OutVoltMinorAlarmRecover.setDescription('Recover from L3 output voltage minor alarm.')
dpduL12LoadMajorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,27))
if mibBuilder.loadTexts: dpduL12LoadMajorAlarm.setDescription('L1 L2 load major alarm.')
dpduL12LoadMajorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,28))
if mibBuilder.loadTexts: dpduL12LoadMajorAlarmRecover.setDescription('Recover from L1 L2 load major alarm.')
dpduL12LoadMinorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,29))
if mibBuilder.loadTexts: dpduL12LoadMinorAlarm.setDescription('L1 L2 load minor alarm.')
dpduL12LoadMinorAlarmRecover = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,30))
if mibBuilder.loadTexts: dpduL12LoadMinorAlarmRecover.setDescription('Recover from L1 L2 load minor alarm.')
dpduEnvCommunicationLost = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,31))
if mibBuilder.loadTexts: dpduEnvCommunicationLost.setDescription('Communication with the environmental sensor failed.')
dpduEnvCommunicationEstablished = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,32))
if mibBuilder.loadTexts: dpduEnvCommunicationEstablished.setDescription('Communication with the environmental sensor reestablished.')
dpduEnvOverWarnTemperature = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,33))
if mibBuilder.loadTexts: dpduEnvOverWarnTemperature.setDescription('The environment over warning temperature.')
dpduNoLongerEnvOverWarnTemperature = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,34))
if mibBuilder.loadTexts: dpduNoLongerEnvOverWarnTemperature.setDescription('The environment recovered from over warning temperature.')
dpduEnvOverWarnHumidity = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,35))
if mibBuilder.loadTexts: dpduEnvOverWarnHumidity.setDescription('The environment over warning humidity.')
dpduNoLongerEnvOverWarnHumidity = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,36))
if mibBuilder.loadTexts: dpduNoLongerEnvOverWarnHumidity.setDescription('The environment recovered from over warning humidity.')
dpduEnvOverAlarmTemperature = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,37))
if mibBuilder.loadTexts: dpduEnvOverAlarmTemperature.setDescription('The environment over alarm temperature.')
dpduNoLongerEnvOverAlarmTemperature = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,38))
if mibBuilder.loadTexts: dpduNoLongerEnvOverAlarmTemperature.setDescription('The environment recovered from over alarm temperature.')
dpduEnvOverAlarmHumidity = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,39))
if mibBuilder.loadTexts: dpduEnvOverAlarmHumidity.setDescription('The environment over alarm humidity.')
dpduNoLongerEnvOverAlarmHumidity = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,40))
if mibBuilder.loadTexts: dpduNoLongerEnvOverAlarmHumidity.setDescription('The environment recovered from over alarm humidity.')
dpduEnvRelay1Alarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,41))
if mibBuilder.loadTexts: dpduEnvRelay1Alarm.setDescription('The environment relay1 is not in normal state.')
dpduEnvRelay1Normal = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,42))
if mibBuilder.loadTexts: dpduEnvRelay1Normal.setDescription('The environment relay1 is in normal state.')
dpduEnvRelay2Alarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,43))
if mibBuilder.loadTexts: dpduEnvRelay2Alarm.setDescription('The environment relay2 is not in normal state.')
dpduEnvRelay2Normal = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,44))
if mibBuilder.loadTexts: dpduEnvRelay2Normal.setDescription('The environment relay2 is in normal state.')
dpduEnvRelay3Alarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,45))
if mibBuilder.loadTexts: dpduEnvRelay3Alarm.setDescription('The environment relay3 is not in normal state.')
dpduEnvRelay3Normal = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,46))
if mibBuilder.loadTexts: dpduEnvRelay3Normal.setDescription('The environment relay3 is in normal state.')
dpduEnvRelay4Alarm = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,47))
if mibBuilder.loadTexts: dpduEnvRelay4Alarm.setDescription('The environment relay4 is not in normal state.')
dpduEnvRelay4Normal = NotificationType((1, 3, 6, 1, 4, 1, 4555, 2, 30, 20) + (0,48))
if mibBuilder.loadTexts: dpduEnvRelay4Normal.setDescription('The environment relay4 is in normal state.')
mibBuilder.exportSymbols("SOCOMECPDU-MIB", dpduL1OutVoltMajorAlarm=dpduL1OutVoltMajorAlarm, dpduL12LoadMinorAlarm=dpduL12LoadMinorAlarm, dpduL2LoadMinorAlarmRecover=dpduL2LoadMinorAlarmRecover, dpduIdentAgentSoftwareVersion=dpduIdentAgentSoftwareVersion, dpduAlarmEnvRelay1=dpduAlarmEnvRelay1, dpduEnvTemperature=dpduEnvTemperature, dpduAlarmEnvRelay3=dpduAlarmEnvRelay3, dpduNoLongerEnvOverWarnHumidity=dpduNoLongerEnvOverWarnHumidity, dpduIdentManufacturer=dpduIdentManufacturer, dpduL2OutVoltMinorAlarmRecover=dpduL2OutVoltMinorAlarmRecover, dpduL2LoadMinorAlarm=dpduL2LoadMinorAlarm, dpduAlarmDisconnect=dpduAlarmDisconnect, dpduL3LoadMajorAlarm=dpduL3LoadMajorAlarm, dpduAlarmL12LoadMajor=dpduAlarmL12LoadMajor, dpduAlarm=dpduAlarm, dpduIdentPDUFirmwareVersion=dpduIdentPDUFirmwareVersion, dpduAlarmL1LoadMinor=dpduAlarmL1LoadMinor, dpduL1OutVoltMajorAlarmRecover=dpduL1OutVoltMajorAlarmRecover, dpduEnvCommunicationLost=dpduEnvCommunicationLost, pdu=pdu, dpduAlarmL2OutVoltMajor=dpduAlarmL2OutVoltMajor, dpduL3OutVoltMajorAlarm=dpduL3OutVoltMajorAlarm, dpduL3OutVoltMajorAlarmRecover=dpduL3OutVoltMajorAlarmRecover, dpduEnvSetTemperatureAlarmLimit=dpduEnvSetTemperatureAlarmLimit, dpduAlarmEnvDisconnect=dpduAlarmEnvDisconnect, dpduIdentSerialNumber=dpduIdentSerialNumber, dpduOutputFrequency=dpduOutputFrequency, dpduL2OutVoltMajorAlarmRecover=dpduL2OutVoltMajorAlarmRecover, dpduEnvRelay3Normal=dpduEnvRelay3Normal, dpduEnvRelay4Normal=dpduEnvRelay4Normal, dpduAlarmL3OutVoltMajor=dpduAlarmL3OutVoltMajor, dpduAlarmOverEnvHumidity=dpduAlarmOverEnvHumidity, dpduEnvSetTemperatureWarnLimit=dpduEnvSetTemperatureWarnLimit, dpduEnvOverAlarmTemperature=dpduEnvOverAlarmTemperature, dpduAlarmL1LoadMajor=dpduAlarmL1LoadMajor, dpduOutputCurrent1=dpduOutputCurrent1, dpduL3LoadMinorAlarmRecover=dpduL3LoadMinorAlarmRecover, dpduEnvCommunicationEstablished=dpduEnvCommunicationEstablished, dpduL1LoadMinorAlarmRecover=dpduL1LoadMinorAlarmRecover, dpduL1LoadMajorAlarm=dpduL1LoadMajorAlarm, dpduNoLongerEnvOverWarnTemperature=dpduNoLongerEnvOverWarnTemperature, dpduL1LoadMinorAlarm=dpduL1LoadMinorAlarm, dpduWarnmOverEnvHumidity=dpduWarnmOverEnvHumidity, dpduEnvSetEnvRelay2=dpduEnvSetEnvRelay2, dpduOutputCurrent3=dpduOutputCurrent3, dpduEnvHumidity=dpduEnvHumidity, dpduCommunicationLost=dpduCommunicationLost, dpduAlarmL3OutVoltMinor=dpduAlarmL3OutVoltMinor, dpduL3OutVoltMinorAlarm=dpduL3OutVoltMinorAlarm, dpduEnvSetEnvRelay1=dpduEnvSetEnvRelay1, dpduAttachedDevices=dpduAttachedDevices, dpduL1OutVoltMinorAlarm=dpduL1OutVoltMinorAlarm, dpduL12LoadMajorAlarm=dpduL12LoadMajorAlarm, dpduAlarmL12LoadMinor=dpduAlarmL12LoadMinor, dpduIdent=dpduIdent, dpduEnvironment=dpduEnvironment, dpduL12LoadMinorAlarmRecover=dpduL12LoadMinorAlarmRecover, dpduIdentModel=dpduIdentModel, dpduAlarmL3LoadMajor=dpduAlarmL3LoadMajor, dpduEnvOverWarnTemperature=dpduEnvOverWarnTemperature, dpduAlarmL2LoadMinor=dpduAlarmL2LoadMinor, dpduOutputVoltage1=dpduOutputVoltage1, dpduEnvRelay2Normal=dpduEnvRelay2Normal, dpduIdentName=dpduIdentName, dpduNoLongerEnvOverAlarmTemperature=dpduNoLongerEnvOverAlarmTemperature, dpduEnvRelay3Alarm=dpduEnvRelay3Alarm, dpduL3LoadMajorAlarmRecover=dpduL3LoadMajorAlarmRecover, dpduEnvSetEnvRelay3=dpduEnvSetEnvRelay3, dpduL1OutVoltMinorAlarmRecover=dpduL1OutVoltMinorAlarmRecover, dpduL1LoadMajorAlarmRecover=dpduL1LoadMajorAlarmRecover, dpduEnvRelay4Alarm=dpduEnvRelay4Alarm, dpduNoLongerEnvOverAlarmHumidity=dpduNoLongerEnvOverAlarmHumidity, dpduAlarmOverEnvTemperature=dpduAlarmOverEnvTemperature, dpduOutput=dpduOutput, dpduTraps=dpduTraps, dpduAlarmEnvRelay2=dpduAlarmEnvRelay2, dpduAlarmL2LoadMajor=dpduAlarmL2LoadMajor, dpduCommunicationEstablished=dpduCommunicationEstablished, dpduEnvRelay2Alarm=dpduEnvRelay2Alarm, dpduEnvSetHumidityWarnLimit=dpduEnvSetHumidityWarnLimit, dpduL12LoadMajorAlarmRecover=dpduL12LoadMajorAlarmRecover, dpduAlarmL1OutVoltMajor=dpduAlarmL1OutVoltMajor, dpduAlarmL3LoadMinor=dpduAlarmL3LoadMinor, dpduL3OutVoltMinorAlarmRecover=dpduL3OutVoltMinorAlarmRecover, dpduEnvOverAlarmHumidity=dpduEnvOverAlarmHumidity, dpduEnvSetHumidityAlarmLimit=dpduEnvSetHumidityAlarmLimit, dpduOutputVoltage3=dpduOutputVoltage3, dpduL3LoadMinorAlarm=dpduL3LoadMinorAlarm, dpduL2LoadMajorAlarmRecover=dpduL2LoadMajorAlarmRecover, dpduAlarmL2OutVoltMinor=dpduAlarmL2OutVoltMinor, dpduEnvRelay1Normal=dpduEnvRelay1Normal, dpduEnvSetEnvRelay4=dpduEnvSetEnvRelay4, dpduL2OutVoltMajorAlarm=dpduL2OutVoltMajorAlarm, dpduEnvOverWarnHumidity=dpduEnvOverWarnHumidity, dpduOutputVoltage2=dpduOutputVoltage2, dpduAlarmL1OutVoltMinor=dpduAlarmL1OutVoltMinor, dpduWarnOverEnvTemperature=dpduWarnOverEnvTemperature, dpduL2LoadMajorAlarm=dpduL2LoadMajorAlarm, dpduEnvRelay1Alarm=dpduEnvRelay1Alarm, socomec=socomec, dpduOutputCurrent2=dpduOutputCurrent2, dpduAlarmEnvRelay4=dpduAlarmEnvRelay4, ups=ups, dpduL2OutVoltMinorAlarm=dpduL2OutVoltMinorAlarm)
