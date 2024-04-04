#
# PySNMP MIB module IMCO-LS110-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/imco/IMCO-LS110-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:20:08 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, IpAddress, iso, NotificationType, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Bits, MibIdentifier, ModuleIdentity, TimeTicks, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "IpAddress", "iso", "NotificationType", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mib_AN_Dcz_SDS = ModuleIdentity((1, 3, 6, 1, 4, 1, 33283)).setLabel("mib-AN-Dcz-SDS")
mib_AN_Dcz_SDS.setRevisions(('2017-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mib_AN_Dcz_SDS.setRevisionsDescriptions(('PSMSmicro, by ViaNet.sk.',))
if mibBuilder.loadTexts: mib_AN_Dcz_SDS.setLastUpdated('201702090000Z')
if mibBuilder.loadTexts: mib_AN_Dcz_SDS.setOrganization('ViaNet.sk')
if mibBuilder.loadTexts: mib_AN_Dcz_SDS.setContactInfo('   Ivan Mochnac\n                ViaNet\n                -\n                -\n                SK EUROPE\n\n                -\n                vianet@vianet.sk')
if mibBuilder.loadTexts: mib_AN_Dcz_SDS.setDescription('The MIB module to describe PSMSmicro version of SDS.')
sdsxpublic = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1))
sdsBIGandSTSW = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30))
sdsOptoInput = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2))
opto1 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 32768))).clone(namedValues=NamedValues(("activeSignalPresent", 0), ("noSignal", 32768)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: opto1.setStatus('current')
if mibBuilder.loadTexts: opto1.setDescription('Current OPTO1 binary input status.')
opto2 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("activeSignalPresent", 0), ("noSignal", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: opto2.setStatus('current')
if mibBuilder.loadTexts: opto2.setDescription('Current OPTO2 binary input status.')
opto3 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("activeSignalPresent", 0), ("noSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: opto3.setStatus('current')
if mibBuilder.loadTexts: opto3.setDescription('Current Mains (OPTO3) binary input status.')
sdsOutputRelays = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3))
sdsOutputRelay1 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 1))
sdsRE1state = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 255))).clone(namedValues=NamedValues(("off", 0), ("activated", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdsRE1state.setStatus('current')
if mibBuilder.loadTexts: sdsRE1state.setDescription('Current RELAY 1 output status.')
sdsOutputRelay2 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 2))
sdsRE2state = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 255))).clone(namedValues=NamedValues(("off", 0), ("activated", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdsRE2state.setStatus('current')
if mibBuilder.loadTexts: sdsRE2state.setDescription('Current RELAY 2 output status.')
sdsOutputRelay3 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 3))
sdsRE3state = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 255))).clone(namedValues=NamedValues(("off", 0), ("activated", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdsRE3state.setStatus('current')
if mibBuilder.loadTexts: sdsRE3state.setDescription('Current RELAY 3 output status.')
sdsADCinputs = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5))
sdsADCitem0 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1))
sdsTempSensValue = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsTempSensValue.setStatus('current')
if mibBuilder.loadTexts: sdsTempSensValue.setDescription('Temperature Sensor (C) multiplied by 100.')
sdsTempSensName = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsTempSensName.setStatus('current')
if mibBuilder.loadTexts: sdsTempSensName.setDescription('User name for the analog temperature sensor.')
sdsADCvalues = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7))
sdsMaximumLoad = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsMaximumLoad.setStatus('current')
if mibBuilder.loadTexts: sdsMaximumLoad.setDescription('Maximum Load (W) multiplied by 10.')
sdsAlarmText = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsAlarmText.setStatus('current')
if mibBuilder.loadTexts: sdsAlarmText.setDescription('SDS Alarm Text.')
sdsOutputVoltage1 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsOutputVoltage1.setStatus('current')
if mibBuilder.loadTexts: sdsOutputVoltage1.setDescription('Output voltage U1 (V) multiplied by 100.')
sdsOutputVoltage2 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsOutputVoltage2.setStatus('current')
if mibBuilder.loadTexts: sdsOutputVoltage2.setDescription('Output voltage U2 (V) multiplied by 100.')
sdsOutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsOutputCurrent.setStatus('current')
if mibBuilder.loadTexts: sdsOutputCurrent.setDescription('Output current I (A) multiplied by 10.')
sdsBatteryCapacity = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsBatteryCapacity.setStatus('current')
if mibBuilder.loadTexts: sdsBatteryCapacity.setDescription('Battery Capacity (%) multiplied by 10.')
sdsLoad = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsLoad.setStatus('current')
if mibBuilder.loadTexts: sdsLoad.setDescription('Load (%) multiplied by 10.')
sdsCapTestTime = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsCapTestTime.setStatus('current')
if mibBuilder.loadTexts: sdsCapTestTime.setDescription('Time (min) of last Capacity Test.')
sdsGeneralInfoEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8))
sdsManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 80), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsManufacturer.setStatus('current')
if mibBuilder.loadTexts: sdsManufacturer.setDescription('Manufacturer of the device.')
sdsModel = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 81), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsModel.setStatus('current')
if mibBuilder.loadTexts: sdsModel.setDescription('Model (type) of the device.')
sdsName = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 82), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsName.setStatus('current')
if mibBuilder.loadTexts: sdsName.setDescription('Name/Location of the device.')
sdsSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 83), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsSerialNumber.setStatus('current')
if mibBuilder.loadTexts: sdsSerialNumber.setDescription('Serial number of the device.')
sdsSoftware = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 84), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsSoftware.setStatus('current')
if mibBuilder.loadTexts: sdsSoftware.setDescription('Software version of the device.')
opto1_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,100)).setLabel("opto1-trap").setObjects(("IMCO-LS110-MIB", "opto1"))
if mibBuilder.loadTexts: opto1_trap.setDescription('TRAP: optical input 1 status.')
opto2_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,101)).setLabel("opto2-trap").setObjects(("IMCO-LS110-MIB", "opto2"))
if mibBuilder.loadTexts: opto2_trap.setDescription('TRAP: optical input 2 status.')
opto3_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,102)).setLabel("opto3-trap").setObjects(("IMCO-LS110-MIB", "opto3"))
if mibBuilder.loadTexts: opto3_trap.setDescription('TRAP: optical input 3 status.')
sdsRE1state_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,150)).setLabel("sdsRE1state-trap").setObjects(("IMCO-LS110-MIB", "sdsRE1state"))
if mibBuilder.loadTexts: sdsRE1state_trap.setDescription('TRAP: Current RELAY 1 output status.')
sdsRE2state_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,153)).setLabel("sdsRE2state-trap").setObjects(("IMCO-LS110-MIB", "sdsRE2state"))
if mibBuilder.loadTexts: sdsRE2state_trap.setDescription('TRAP: Current RELAY 2 output status.')
sdsTempSensValue_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,222)).setLabel("sdsTempSensValue-trap").setObjects(("IMCO-LS110-MIB", "sdsTempSensValue"))
if mibBuilder.loadTexts: sdsTempSensValue_trap.setDescription('TRAP: Temperature Sensor (C) multiplied by 100.')
sdsTempSensName_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,223)).setLabel("sdsTempSensName-trap").setObjects(("IMCO-LS110-MIB", "sdsTempSensName"))
if mibBuilder.loadTexts: sdsTempSensName_trap.setDescription('TRAP: User name for analog temperature sensor.')
sdsMaximumLoad_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,401)).setLabel("sdsMaximumLoad-trap").setObjects(("IMCO-LS110-MIB", "sdsMaximumLoad"))
if mibBuilder.loadTexts: sdsMaximumLoad_trap.setDescription('TRAP: SDS Maximum Load-trap.')
sdsAlarmText_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,402)).setLabel("sdsAlarmText-trap").setObjects(("IMCO-LS110-MIB", "sdsAlarmText"))
if mibBuilder.loadTexts: sdsAlarmText_trap.setDescription('TRAP: SDS Alarm Text.')
sdsOutputVoltage1_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,403)).setLabel("sdsOutputVoltage1-trap").setObjects(("IMCO-LS110-MIB", "sdsOutputVoltage1"))
if mibBuilder.loadTexts: sdsOutputVoltage1_trap.setDescription('TRAP: SDS Output Voltage1-trap.')
sdsOutputVoltage2_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,404)).setLabel("sdsOutputVoltage2-trap").setObjects(("IMCO-LS110-MIB", "sdsOutputVoltage2"))
if mibBuilder.loadTexts: sdsOutputVoltage2_trap.setDescription('TRAP: SDS Outpur Voltage2-trap.')
sdsOutputCurrent_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,405)).setLabel("sdsOutputCurrent-trap").setObjects(("IMCO-LS110-MIB", "sdsOutputCurrent"))
if mibBuilder.loadTexts: sdsOutputCurrent_trap.setDescription('TRAP: SDS Output current-trap.')
sdsBatteryCapacity_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,406)).setLabel("sdsBatteryCapacity-trap").setObjects(("IMCO-LS110-MIB", "sdsBatteryCapacity"))
if mibBuilder.loadTexts: sdsBatteryCapacity_trap.setDescription('TRAP: SDS Battery Capacity-trap.')
sdsLoad_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,407)).setLabel("sdsLoad-trap").setObjects(("IMCO-LS110-MIB", "sdsLoad"))
if mibBuilder.loadTexts: sdsLoad_trap.setDescription('TRAP: SDS Load-trap.')
sdsCapTestTime_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,408)).setLabel("sdsCapTestTime-trap").setObjects(("IMCO-LS110-MIB", "sdsCapTestTime"))
if mibBuilder.loadTexts: sdsCapTestTime_trap.setDescription('TRAP: SDS CapTestTime-trap.')
mibBuilder.exportSymbols("IMCO-LS110-MIB", sdsCapTestTime=sdsCapTestTime, sdsCapTestTime_trap=sdsCapTestTime_trap, sdsRE1state=sdsRE1state, sdsRE2state_trap=sdsRE2state_trap, sdsTempSensValue=sdsTempSensValue, sdsOutputRelay1=sdsOutputRelay1, sdsOutputRelay2=sdsOutputRelay2, sdsLoad_trap=sdsLoad_trap, sdsADCitem0=sdsADCitem0, opto2=opto2, sdsBatteryCapacity_trap=sdsBatteryCapacity_trap, sdsManufacturer=sdsManufacturer, sdsOutputVoltage1_trap=sdsOutputVoltage1_trap, sdsAlarmText=sdsAlarmText, opto2_trap=opto2_trap, sdsBIGandSTSW=sdsBIGandSTSW, sdsTempSensName_trap=sdsTempSensName_trap, sdsOutputRelays=sdsOutputRelays, sdsTempSensName=sdsTempSensName, opto3=opto3, sdsSerialNumber=sdsSerialNumber, opto3_trap=opto3_trap, sdsOutputCurrent=sdsOutputCurrent, sdsName=sdsName, sdsOutputVoltage2=sdsOutputVoltage2, sdsRE1state_trap=sdsRE1state_trap, sdsGeneralInfoEntry=sdsGeneralInfoEntry, sdsMaximumLoad_trap=sdsMaximumLoad_trap, sdsMaximumLoad=sdsMaximumLoad, sdsAlarmText_trap=sdsAlarmText_trap, sdsModel=sdsModel, sdsADCinputs=sdsADCinputs, sdsOutputCurrent_trap=sdsOutputCurrent_trap, sdsOptoInput=sdsOptoInput, sdsOutputVoltage2_trap=sdsOutputVoltage2_trap, opto1=opto1, mib_AN_Dcz_SDS=mib_AN_Dcz_SDS, sdsBatteryCapacity=sdsBatteryCapacity, sdsLoad=sdsLoad, sdsSoftware=sdsSoftware, sdsTempSensValue_trap=sdsTempSensValue_trap, sdsxpublic=sdsxpublic, sdsRE3state=sdsRE3state, sdsOutputRelay3=sdsOutputRelay3, sdsADCvalues=sdsADCvalues, sdsOutputVoltage1=sdsOutputVoltage1, opto1_trap=opto1_trap, PYSNMP_MODULE_ID=mib_AN_Dcz_SDS, sdsRE2state=sdsRE2state)
