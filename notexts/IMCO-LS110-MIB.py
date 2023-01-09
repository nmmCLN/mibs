#
# PySNMP MIB module IMCO-LS110-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/imco/IMCO-LS110-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:32:48 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Bits, NotificationType, ObjectIdentity, MibIdentifier, ModuleIdentity, enterprises, Unsigned32, IpAddress, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "enterprises", "Unsigned32", "IpAddress", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mib_AN_Dcz_SDS = ModuleIdentity((1, 3, 6, 1, 4, 1, 33283)).setLabel("mib-AN-Dcz-SDS")
mib_AN_Dcz_SDS.setRevisions(('2017-02-09 00:00',))
if mibBuilder.loadTexts: mib_AN_Dcz_SDS.setLastUpdated('201702090000Z')
if mibBuilder.loadTexts: mib_AN_Dcz_SDS.setOrganization('ViaNet.sk')
sdsxpublic = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1))
sdsBIGandSTSW = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30))
sdsOptoInput = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2))
opto1 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 32768))).clone(namedValues=NamedValues(("activeSignalPresent", 0), ("noSignal", 32768)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: opto1.setStatus('current')
opto2 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("activeSignalPresent", 0), ("noSignal", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: opto2.setStatus('current')
opto3 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("activeSignalPresent", 0), ("noSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: opto3.setStatus('current')
sdsOutputRelays = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3))
sdsOutputRelay1 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 1))
sdsRE1state = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 255))).clone(namedValues=NamedValues(("off", 0), ("activated", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdsRE1state.setStatus('current')
sdsOutputRelay2 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 2))
sdsRE2state = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 255))).clone(namedValues=NamedValues(("off", 0), ("activated", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdsRE2state.setStatus('current')
sdsOutputRelay3 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 3))
sdsRE3state = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 255))).clone(namedValues=NamedValues(("off", 0), ("activated", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdsRE3state.setStatus('current')
sdsADCinputs = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5))
sdsADCitem0 = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1))
sdsTempSensValue = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsTempSensValue.setStatus('current')
sdsTempSensName = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsTempSensName.setStatus('current')
sdsADCvalues = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7))
sdsMaximumLoad = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsMaximumLoad.setStatus('current')
sdsAlarmText = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsAlarmText.setStatus('current')
sdsOutputVoltage1 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsOutputVoltage1.setStatus('current')
sdsOutputVoltage2 = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsOutputVoltage2.setStatus('current')
sdsOutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsOutputCurrent.setStatus('current')
sdsBatteryCapacity = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsBatteryCapacity.setStatus('current')
sdsLoad = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsLoad.setStatus('current')
sdsCapTestTime = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsCapTestTime.setStatus('current')
sdsGeneralInfoEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8))
sdsManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 80), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsManufacturer.setStatus('current')
sdsModel = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 81), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsModel.setStatus('current')
sdsName = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 82), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsName.setStatus('current')
sdsSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 83), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsSerialNumber.setStatus('current')
sdsSoftware = MibScalar((1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 84), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdsSoftware.setStatus('current')
opto1_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,100)).setLabel("opto1-trap").setObjects(("IMCO-LS110-MIB", "opto1"))
opto2_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,101)).setLabel("opto2-trap").setObjects(("IMCO-LS110-MIB", "opto2"))
opto3_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,102)).setLabel("opto3-trap").setObjects(("IMCO-LS110-MIB", "opto3"))
sdsRE1state_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,150)).setLabel("sdsRE1state-trap").setObjects(("IMCO-LS110-MIB", "sdsRE1state"))
sdsRE2state_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,153)).setLabel("sdsRE2state-trap").setObjects(("IMCO-LS110-MIB", "sdsRE2state"))
sdsTempSensValue_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,222)).setLabel("sdsTempSensValue-trap").setObjects(("IMCO-LS110-MIB", "sdsTempSensValue"))
sdsTempSensName_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,223)).setLabel("sdsTempSensName-trap").setObjects(("IMCO-LS110-MIB", "sdsTempSensName"))
sdsMaximumLoad_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,401)).setLabel("sdsMaximumLoad-trap").setObjects(("IMCO-LS110-MIB", "sdsMaximumLoad"))
sdsAlarmText_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,402)).setLabel("sdsAlarmText-trap").setObjects(("IMCO-LS110-MIB", "sdsAlarmText"))
sdsOutputVoltage1_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,403)).setLabel("sdsOutputVoltage1-trap").setObjects(("IMCO-LS110-MIB", "sdsOutputVoltage1"))
sdsOutputVoltage2_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,404)).setLabel("sdsOutputVoltage2-trap").setObjects(("IMCO-LS110-MIB", "sdsOutputVoltage2"))
sdsOutputCurrent_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,405)).setLabel("sdsOutputCurrent-trap").setObjects(("IMCO-LS110-MIB", "sdsOutputCurrent"))
sdsBatteryCapacity_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,406)).setLabel("sdsBatteryCapacity-trap").setObjects(("IMCO-LS110-MIB", "sdsBatteryCapacity"))
sdsLoad_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,407)).setLabel("sdsLoad-trap").setObjects(("IMCO-LS110-MIB", "sdsLoad"))
sdsCapTestTime_trap = NotificationType((1, 3, 6, 1, 4, 1, 33283) + (0,408)).setLabel("sdsCapTestTime-trap").setObjects(("IMCO-LS110-MIB", "sdsCapTestTime"))
mibBuilder.exportSymbols("IMCO-LS110-MIB", sdsManufacturer=sdsManufacturer, mib_AN_Dcz_SDS=mib_AN_Dcz_SDS, opto1=opto1, sdsSoftware=sdsSoftware, sdsCapTestTime=sdsCapTestTime, sdsRE1state_trap=sdsRE1state_trap, sdsOutputVoltage1_trap=sdsOutputVoltage1_trap, sdsTempSensValue_trap=sdsTempSensValue_trap, sdsMaximumLoad_trap=sdsMaximumLoad_trap, sdsRE2state_trap=sdsRE2state_trap, sdsOutputRelays=sdsOutputRelays, sdsOutputVoltage2_trap=sdsOutputVoltage2_trap, sdsModel=sdsModel, sdsxpublic=sdsxpublic, sdsRE3state=sdsRE3state, sdsTempSensValue=sdsTempSensValue, sdsOutputCurrent_trap=sdsOutputCurrent_trap, sdsTempSensName=sdsTempSensName, sdsOutputRelay1=sdsOutputRelay1, sdsOutputRelay2=sdsOutputRelay2, sdsMaximumLoad=sdsMaximumLoad, opto3_trap=opto3_trap, sdsBIGandSTSW=sdsBIGandSTSW, sdsADCvalues=sdsADCvalues, sdsRE2state=sdsRE2state, sdsAlarmText_trap=sdsAlarmText_trap, sdsSerialNumber=sdsSerialNumber, sdsADCitem0=sdsADCitem0, PYSNMP_MODULE_ID=mib_AN_Dcz_SDS, sdsRE1state=sdsRE1state, sdsTempSensName_trap=sdsTempSensName_trap, sdsADCinputs=sdsADCinputs, opto2_trap=opto2_trap, sdsGeneralInfoEntry=sdsGeneralInfoEntry, sdsOptoInput=sdsOptoInput, sdsName=sdsName, sdsBatteryCapacity=sdsBatteryCapacity, opto1_trap=opto1_trap, opto2=opto2, sdsLoad_trap=sdsLoad_trap, sdsCapTestTime_trap=sdsCapTestTime_trap, sdsOutputVoltage1=sdsOutputVoltage1, sdsOutputRelay3=sdsOutputRelay3, sdsOutputCurrent=sdsOutputCurrent, sdsBatteryCapacity_trap=sdsBatteryCapacity_trap, sdsOutputVoltage2=sdsOutputVoltage2, opto3=opto3, sdsAlarmText=sdsAlarmText, sdsLoad=sdsLoad)
