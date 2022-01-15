#
# PySNMP MIB module MDS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:20:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
mdsSystem, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsSystem")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, Integer32, Unsigned32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, NotificationType, Counter32, Gauge32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Unsigned32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "NotificationType", "Counter32", "Gauge32", "Bits", "IpAddress")
DateAndTime, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TruthValue")
mdsSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1))
mdsSystemMIB.setRevisions(('2019-11-18 00:00', '2018-05-16 00:00', '2014-02-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsSystemMIB.setRevisionsDescriptions(('Added boot and current time.', 'Updated conformance statments based on smilint.', 'Initial version.',))
if mibBuilder.loadTexts: mdsSystemMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsSystemMIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsSystemMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n         T 585-242-9600\n         F 585-242-9620\n\n         175 Science Parkway\n         Rochester, New York 14620\n         USA')
if mibBuilder.loadTexts: mdsSystemMIB.setDescription('The MIB module to describe the system.')
mSysMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1))
mSysConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 1))
mSysStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2))
class FirmwareLocation(TextualConvention, Unsigned32):
    description = 'FirmwareLocation'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

mSysSerialNumberCore = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysSerialNumberCore.setStatus('current')
if mibBuilder.loadTexts: mSysSerialNumberCore.setDescription('Core board serial number.')
mSysSerialNumberPlatform = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysSerialNumberPlatform.setStatus('current')
if mibBuilder.loadTexts: mSysSerialNumberPlatform.setDescription('Platform board serial number.')
mSysProductConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysProductConfiguration.setStatus('current')
if mibBuilder.loadTexts: mSysProductConfiguration.setDescription('Product configuration.')
mSysGuid = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysGuid.setStatus('current')
if mibBuilder.loadTexts: mSysGuid.setDescription('GUID of the unit.')
mSysUptime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysUptime.setStatus('current')
if mibBuilder.loadTexts: mSysUptime.setDescription('System uptime (in secs) since bootup.')
mSysTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysTemperature.setStatus('current')
if mibBuilder.loadTexts: mSysTemperature.setDescription('System temperature (in Celsius).')
mSysFirmwareVersionTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7), )
if mibBuilder.loadTexts: mSysFirmwareVersionTable.setStatus('current')
if mibBuilder.loadTexts: mSysFirmwareVersionTable.setDescription('This table contains status of system firmware.')
mSysPowerSupplyVoltage = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysPowerSupplyVoltage.setStatus('current')
if mibBuilder.loadTexts: mSysPowerSupplyVoltage.setDescription('Power Supply Voltage (in VDC).')
mSysCurrentDateTime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysCurrentDateTime.setStatus('current')
if mibBuilder.loadTexts: mSysCurrentDateTime.setDescription('Current system date and time.')
mSysBootDateTime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysBootDateTime.setStatus('current')
if mibBuilder.loadTexts: mSysBootDateTime.setDescription('system date and time on boot.')
mSysFirmwareVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1), ).setIndexNames((0, "MDS-SYSTEM-MIB", "mSysLocation"))
if mibBuilder.loadTexts: mSysFirmwareVersionEntry.setStatus('current')
if mibBuilder.loadTexts: mSysFirmwareVersionEntry.setDescription('Each entry contains information about the stored firmware image.')
mSysLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 1), FirmwareLocation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysLocation.setStatus('current')
if mibBuilder.loadTexts: mSysLocation.setDescription('Firmware location.')
mSysVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysVersion.setStatus('current')
if mibBuilder.loadTexts: mSysVersion.setDescription('Firmware version.')
mSysActive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysActive.setStatus('current')
if mibBuilder.loadTexts: mSysActive.setDescription('Firmware state.')
mSysAutoUpdateState = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysAutoUpdateState.setStatus('current')
if mibBuilder.loadTexts: mSysAutoUpdateState.setDescription('Current state of the auto-update daemon.')
mSysAutoUpdateDetails = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysAutoUpdateDetails.setStatus('current')
if mibBuilder.loadTexts: mSysAutoUpdateDetails.setDescription('Detailed information on auto-update state.')
mSysMprStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8))
mSysMprHeatsinkTemperature1 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprHeatsinkTemperature1.setStatus('current')
if mibBuilder.loadTexts: mSysMprHeatsinkTemperature1.setDescription('The current heatsink #1 temperature in degrees Celsius.')
mSysMprHeatsinkTemperature2 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprHeatsinkTemperature2.setStatus('current')
if mibBuilder.loadTexts: mSysMprHeatsinkTemperature2.setDescription('The current heatsink #2 temperature in degrees Celsius.')
mSysMprPowerSupplyVoltage1 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprPowerSupplyVoltage1.setStatus('current')
if mibBuilder.loadTexts: mSysMprPowerSupplyVoltage1.setDescription('The current output voltage of power supply #1.')
mSysMprPowerSupplyVoltage2 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprPowerSupplyVoltage2.setStatus('current')
if mibBuilder.loadTexts: mSysMprPowerSupplyVoltage2.setDescription('The current output voltage of power supply #2.')
mSysMprRelaySwitchPosition = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprRelaySwitchPosition.setStatus('current')
if mibBuilder.loadTexts: mSysMprRelaySwitchPosition.setDescription('The current state of the manual override switch on the relay card.')
mdsSysMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3))
mdsSysMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 1))
mdsSysMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2))
mSysCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 1, 1)).setObjects(("MDS-SYSTEM-MIB", "mSysStatusGroup"), ("MDS-SYSTEM-MIB", "mSysMprStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSysCompliance = mSysCompliance.setStatus('current')
if mibBuilder.loadTexts: mSysCompliance.setDescription('The compliance statement for SNMP entities that \n            implement the MDS-SYSTEM-MIB.')
mSysStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2, 1)).setObjects(("MDS-SYSTEM-MIB", "mSysSerialNumberCore"), ("MDS-SYSTEM-MIB", "mSysSerialNumberPlatform"), ("MDS-SYSTEM-MIB", "mSysProductConfiguration"), ("MDS-SYSTEM-MIB", "mSysGuid"), ("MDS-SYSTEM-MIB", "mSysUptime"), ("MDS-SYSTEM-MIB", "mSysTemperature"), ("MDS-SYSTEM-MIB", "mSysPowerSupplyVoltage"), ("MDS-SYSTEM-MIB", "mSysLocation"), ("MDS-SYSTEM-MIB", "mSysVersion"), ("MDS-SYSTEM-MIB", "mSysActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSysStatusGroup = mSysStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mSysStatusGroup.setDescription('A collection of objects providing information about\n        Orbit system status.')
mSysMprStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2, 2)).setObjects(("MDS-SYSTEM-MIB", "mSysMprHeatsinkTemperature1"), ("MDS-SYSTEM-MIB", "mSysMprHeatsinkTemperature2"), ("MDS-SYSTEM-MIB", "mSysMprPowerSupplyVoltage1"), ("MDS-SYSTEM-MIB", "mSysMprPowerSupplyVoltage2"), ("MDS-SYSTEM-MIB", "mSysMprRelaySwitchPosition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSysMprStatusGroup = mSysMprStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mSysMprStatusGroup.setDescription('A collection of objects providing information about\n        Orbit MPR system status.')
mibBuilder.exportSymbols("MDS-SYSTEM-MIB", mSysConfig=mSysConfig, mSysMprHeatsinkTemperature1=mSysMprHeatsinkTemperature1, mSysPowerSupplyVoltage=mSysPowerSupplyVoltage, mSysLocation=mSysLocation, mSysMprPowerSupplyVoltage2=mSysMprPowerSupplyVoltage2, mSysMIBObjects=mSysMIBObjects, PYSNMP_MODULE_ID=mdsSystemMIB, mSysMprStatus=mSysMprStatus, mSysActive=mSysActive, mSysTemperature=mSysTemperature, mSysFirmwareVersionEntry=mSysFirmwareVersionEntry, mSysMprStatusGroup=mSysMprStatusGroup, mSysCurrentDateTime=mSysCurrentDateTime, mSysBootDateTime=mSysBootDateTime, FirmwareLocation=FirmwareLocation, mdsSysMIBGroups=mdsSysMIBGroups, mSysSerialNumberPlatform=mSysSerialNumberPlatform, mSysFirmwareVersionTable=mSysFirmwareVersionTable, mSysAutoUpdateState=mSysAutoUpdateState, mSysVersion=mSysVersion, mSysMprRelaySwitchPosition=mSysMprRelaySwitchPosition, mSysCompliance=mSysCompliance, mSysGuid=mSysGuid, mSysAutoUpdateDetails=mSysAutoUpdateDetails, mSysStatusGroup=mSysStatusGroup, mSysMprHeatsinkTemperature2=mSysMprHeatsinkTemperature2, mdsSysMIBCompliances=mdsSysMIBCompliances, mSysUptime=mSysUptime, mdsSysMIBConformance=mdsSysMIBConformance, mSysMprPowerSupplyVoltage1=mSysMprPowerSupplyVoltage1, mSysSerialNumberCore=mSysSerialNumberCore, mdsSystemMIB=mdsSystemMIB, mSysProductConfiguration=mSysProductConfiguration, mSysStatus=mSysStatus)
