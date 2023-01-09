#
# PySNMP MIB module Argus-Power-System-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alpha/Argus-Power-System-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:54 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Counter64, ModuleIdentity, Integer32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Unsigned32, MibIdentifier, Counter32, TimeTicks, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter64", "ModuleIdentity", "Integer32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "TimeTicks", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
argus = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309))
argus.setRevisions(('2016-12-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: argus.setRevisionsDescriptions(('\n   Updated upsSecondsOnBattery to upsMinutesOnBattery to match unit value of the data.\n   ',))
if mibBuilder.loadTexts: argus.setLastUpdated('201612090000Z')
if mibBuilder.loadTexts: argus.setOrganization('Alpha Technologies Ltd.')
if mibBuilder.loadTexts: argus.setContactInfo('Alpha Technologies Ltd.\n     7700 Riverfront Gate\n     Burnaby, BC  V5J 5M4\n     Canada\n\n     Tel: 1-604-436-5900\n     Fax: 1-604-436-1233')
if mibBuilder.loadTexts: argus.setDescription('This MIB defines the information block(s) available in CXC RMU\n     as defined by the following list: \n    - upsDevice: the CXC-series of controllers')
class PositiveInteger(TextualConvention, Integer32):
    description = 'This data type is a non-zero and non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    description = 'This data type is a non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

upsPower = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6))
upsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1))
upsIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1))
upsBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2))
upsInput = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3))
upsOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4))
upsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5))
upsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6))
upsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7))
upsExtra = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8))
upsExtraCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraCount.setStatus('current')
if mibBuilder.loadTexts: upsExtraCount.setDescription('Number of extra variables')
upsExtraTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2), )
if mibBuilder.loadTexts: upsExtraTable.setStatus('current')
if mibBuilder.loadTexts: upsExtraTable.setDescription('A table of CXC upstem controller extra variables')
upsExtraEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsExtraIndex"))
if mibBuilder.loadTexts: upsExtraEntry.setStatus('current')
if mibBuilder.loadTexts: upsExtraEntry.setDescription('An entry into the CXC upstem controller extra variable table')
upsExtraIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraIndex.setStatus('current')
if mibBuilder.loadTexts: upsExtraIndex.setDescription('The index of the extra variable in the CXC upstem controller table')
upsExtraName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraName.setStatus('current')
if mibBuilder.loadTexts: upsExtraName.setDescription('The description of the extra variable as reported by the CXC upstem controller')
upsExtraIntegerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1000000000, 1000000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraIntegerValue.setStatus('current')
if mibBuilder.loadTexts: upsExtraIntegerValue.setDescription('The integer value of the extra variable as reported by the CXC upstem controller')
upsExtraStringValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraStringValue.setStatus('current')
if mibBuilder.loadTexts: upsExtraStringValue.setDescription('The string value of the extra variable as reported by the CXC upstem controller')
upsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0))
upsAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 1)).setObjects(("Argus-Power-System-MIB", "upsExtraIntegerValue"), ("Argus-Power-System-MIB", "upsExtraStringValue"), ("Argus-Power-System-MIB", "upsExtraIndex"), ("Argus-Power-System-MIB", "upsExtraName"))
if mibBuilder.loadTexts: upsAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: upsAlarmTrap.setDescription('A trap issued from a change in state in one of the Alarms on the Novus controller')
upsAgentStartupTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 2)).setObjects(("Argus-Power-System-MIB", "upsIdentSiteName"))
if mibBuilder.loadTexts: upsAgentStartupTrap.setStatus('current')
if mibBuilder.loadTexts: upsAgentStartupTrap.setDescription('A trap to indicate that the agent software has started up.')
upsAgentShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 3)).setObjects(("Argus-Power-System-MIB", "upsIdentSiteName"))
if mibBuilder.loadTexts: upsAgentShutdownTrap.setStatus('current')
if mibBuilder.loadTexts: upsAgentShutdownTrap.setDescription('A trap to indicate that the agent software has shutdown.')
upsAgentFaultTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 4)).setObjects(("Argus-Power-System-MIB", "upsExtraIntegerValue"), ("Argus-Power-System-MIB", "upsExtraStringValue"), ("Argus-Power-System-MIB", "upsExtraIndex"), ("Argus-Power-System-MIB", "upsExtraName"))
if mibBuilder.loadTexts: upsAgentFaultTrap.setStatus('current')
if mibBuilder.loadTexts: upsAgentFaultTrap.setDescription('A trap issued from a change in state in one of the Faults on the Novus controller')
upsAgentEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 5)).setObjects(("Argus-Power-System-MIB", "upsExtraIntegerValue"), ("Argus-Power-System-MIB", "upsExtraStringValue"), ("Argus-Power-System-MIB", "upsExtraIndex"), ("Argus-Power-System-MIB", "upsExtraName"))
if mibBuilder.loadTexts: upsAgentEventTrap.setStatus('current')
if mibBuilder.loadTexts: upsAgentEventTrap.setDescription('A trap issued from a change in state in one of the Events on the Novus controller')
upsIdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentManufacturer.setStatus('current')
if mibBuilder.loadTexts: upsIdentManufacturer.setDescription('The name of the UPS manufacturer.')
upsIdentProductCode = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentProductCode.setStatus('current')
if mibBuilder.loadTexts: upsIdentProductCode.setDescription('The UPS Model designation.')
upsIdentModel = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentModel.setStatus('current')
if mibBuilder.loadTexts: upsIdentModel.setDescription('The UPS Product code designation.')
upsIdentUPSSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentUPSSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: upsIdentUPSSoftwareVersion.setDescription('The UPS firmware/software version(s).  This variable\n               may or may not have the same value as\n               upsIdentAgentSoftwareVersion in some implementations.')
upsIdentAgentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentAgentSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: upsIdentAgentSoftwareVersion.setDescription('The UPS agent software version.  This variable may or\n               may not have the same value as\n               upsIdentUPSSoftwareVersion in some implementations.')
upsIdentName = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentName.setStatus('current')
if mibBuilder.loadTexts: upsIdentName.setDescription('A string identifying the UPS.  This object should be\n               set by the administrator.')
upsIdentAttachedDevices = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentAttachedDevices.setStatus('current')
if mibBuilder.loadTexts: upsIdentAttachedDevices.setDescription('A string identifying the devices attached to the\n               output(s) of the UPS.  This object should be set by\n               the administrator.')
upsIdentSiteName = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteName.setStatus('current')
if mibBuilder.loadTexts: upsIdentSiteName.setDescription('Site Name')
upsIdentSiteCity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteCity.setStatus('current')
if mibBuilder.loadTexts: upsIdentSiteCity.setDescription('Site City')
upsIdentSiteRegion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteRegion.setStatus('current')
if mibBuilder.loadTexts: upsIdentSiteRegion.setDescription('Site Region')
upsIdentSiteCountry = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteCountry.setStatus('current')
if mibBuilder.loadTexts: upsIdentSiteCountry.setDescription('Site Country')
upsIdentContactName = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentContactName.setStatus('current')
if mibBuilder.loadTexts: upsIdentContactName.setDescription('Contact Name')
upsIdentPhoneNumber = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentPhoneNumber.setStatus('current')
if mibBuilder.loadTexts: upsIdentPhoneNumber.setDescription('Phone Number')
upsIdentDate = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentDate.setStatus('current')
if mibBuilder.loadTexts: upsIdentDate.setDescription('Date of the RMU-Novus')
upsIdentTime = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentTime.setStatus('current')
if mibBuilder.loadTexts: upsIdentTime.setDescription('Time of the RMU-Novus')
upsBatteryStatus = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("batteryNormal", 2), ("batteryLow", 3), ("batteryDepleted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryStatus.setStatus('current')
if mibBuilder.loadTexts: upsBatteryStatus.setDescription("The indication of the capacity remaining in the UPS\n               system's batteries.   A value of batteryNormal\n               indicates that the remaining run-time is greater than\n               upsConfigLowBattTime.  A value of batteryLow indicates\n               that the remaining battery run-time is less than or\n               equal to upsConfigLowBattTime.  A value of\n               batteryDepleted indicates that the UPS will be unable\n               to sustain the present load when and if the utility\n               power is lost (including the possibility that the\n               utility power is currently absent and the UPS is\n               unable to sustain the output).")
upsMinutesOnBattery = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 2), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsMinutesOnBattery.setStatus('current')
if mibBuilder.loadTexts: upsMinutesOnBattery.setDescription('\n               The accumulated elapsed time that the UPS system have been on battery.\n               ')
upsBatteryVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 3), Integer32()).setUnits('0.1 Volt DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryVoltage.setStatus('current')
if mibBuilder.loadTexts: upsBatteryVoltage.setDescription('The magnitude of the present battery voltage.')
upsBatteryChargingCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 4), Integer32()).setUnits('0.1 Amp DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryChargingCurrent.setStatus('current')
if mibBuilder.loadTexts: upsBatteryChargingCurrent.setDescription('The present battery charging current.')
upsBatteryCapacity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 5), Integer32()).setUnits('0.1 Amp DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryCapacity.setStatus('current')
if mibBuilder.loadTexts: upsBatteryCapacity.setDescription('The present battery capacity.')
upsBatteryTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 6), Integer32()).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryTemperature.setStatus('current')
if mibBuilder.loadTexts: upsBatteryTemperature.setDescription('The ambient temperature at or near the UPS Battery\n               casing.')
upsBatteryLowWarning = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 7), Integer32()).setUnits('percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsBatteryLowWarning.setStatus('current')
if mibBuilder.loadTexts: upsBatteryLowWarning.setDescription('The set battery capacity percentage at which the unit will raise an alarm.')
upsInputNumLines = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputNumLines.setStatus('current')
if mibBuilder.loadTexts: upsInputNumLines.setDescription('The number of input lines utilized in this device.\n               This variable indicates the number of rows in the\n               input table.')
upsInputTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2), )
if mibBuilder.loadTexts: upsInputTable.setStatus('current')
if mibBuilder.loadTexts: upsInputTable.setDescription('A list of input table entries.  The number of entries\n               is given by the value of upsInputNumLines.')
upsInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsInputLineIndex"))
if mibBuilder.loadTexts: upsInputEntry.setStatus('current')
if mibBuilder.loadTexts: upsInputEntry.setDescription('An entry containing information applicable to a\n               particular input line.')
upsInputLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: upsInputLineIndex.setStatus('current')
if mibBuilder.loadTexts: upsInputLineIndex.setDescription('The input line identifier.')
upsInputFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 2), Integer32()).setUnits('Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputFrequency.setStatus('current')
if mibBuilder.loadTexts: upsInputFrequency.setDescription('The present input frequency.')
upsInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 3), Integer32()).setUnits('0.1 RMS Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputVoltage.setStatus('current')
if mibBuilder.loadTexts: upsInputVoltage.setDescription('The magnitude of the present input voltage.')
upsOutputSource = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("standby", 1), ("line", 2), ("boost2", 3), ("boost1", 4), ("buck1", 5), ("buck2", 6), ("inverter", 7), ("retransfer", 8), ("transfer", 9), ("shutdown", 10), ("bypass", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputSource.setStatus('current')
if mibBuilder.loadTexts: upsOutputSource.setDescription('The present source of output power.  The enumeration\n               line(2) indicates that the Novus is in line mode.')
upsOutputFrequency = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 2), Integer32()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputFrequency.setStatus('current')
if mibBuilder.loadTexts: upsOutputFrequency.setDescription('The present output frequency.')
upsOutputNumLines = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputNumLines.setStatus('current')
if mibBuilder.loadTexts: upsOutputNumLines.setDescription('The number of output lines utilized in this device.\n               This variable indicates the number of rows in the\n               output table.')
upsOutputTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4), )
if mibBuilder.loadTexts: upsOutputTable.setStatus('current')
if mibBuilder.loadTexts: upsOutputTable.setDescription('A list of output table entries.  The number of\n               entries is given by the value of upsOutputNumLines.')
upsOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsOutputLineIndex"))
if mibBuilder.loadTexts: upsOutputEntry.setStatus('current')
if mibBuilder.loadTexts: upsOutputEntry.setDescription('An entry containing information applicable to a\n               particular output line.')
upsOutputLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: upsOutputLineIndex.setStatus('current')
if mibBuilder.loadTexts: upsOutputLineIndex.setDescription('The output line identifier.')
upsOutputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 2), Integer32()).setUnits('0.1 RMS Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputVoltage.setStatus('current')
if mibBuilder.loadTexts: upsOutputVoltage.setDescription('The present output voltage.')
upsOutputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 3), Integer32()).setUnits('0.1 RMS Amp').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputCurrent.setStatus('current')
if mibBuilder.loadTexts: upsOutputCurrent.setDescription('The present output current.')
upsOutputPowerVA = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 4), Integer32()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPowerVA.setStatus('current')
if mibBuilder.loadTexts: upsOutputPowerVA.setDescription('The present output VA.')
upsOutputPowerWatt = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 5), Integer32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPowerWatt.setStatus('current')
if mibBuilder.loadTexts: upsOutputPowerWatt.setDescription('The present output true power.')
upsPowerFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 6), Integer32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsPowerFactor.setStatus('current')
if mibBuilder.loadTexts: upsPowerFactor.setDescription('The present power factor.')
upsOutputPercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPercentLoad.setStatus('current')
if mibBuilder.loadTexts: upsOutputPercentLoad.setDescription('The percentage of the UPS power capacity presently\n               being used on this output line, i.e., the greater of\n               the percent load of true power capacity and the\n               percent load of VA.')
upsAlarmsPresent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmsPresent.setStatus('current')
if mibBuilder.loadTexts: upsAlarmsPresent.setDescription('The present number of active alarm conditions.')
upsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2), )
if mibBuilder.loadTexts: upsAlarmTable.setStatus('current')
if mibBuilder.loadTexts: upsAlarmTable.setDescription('A list of alarm table entries. ')
upsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsAlarmId"))
if mibBuilder.loadTexts: upsAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: upsAlarmEntry.setDescription('An entry containing information applicable to a\n               particular alarm.')
upsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: upsAlarmId.setStatus('current')
if mibBuilder.loadTexts: upsAlarmId.setDescription('A unique identifier for an alarm condition.  This\n               value must remain constant.')
upsAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmDescr.setStatus('current')
if mibBuilder.loadTexts: upsAlarmDescr.setDescription('A unique description of the alarm. ')
upsAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: upsAlarmStatus.setDescription('1 - ON or 0 - OFF. ')
upsConfigLineQualifyTime = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 1), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigLineQualifyTime.setStatus('current')
if mibBuilder.loadTexts: upsConfigLineQualifyTime.setDescription('This objects displays the line qualify time.')
upsConfigLineOutputVoltageHighLimit = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 2), Integer32()).setUnits('volttenth').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigLineOutputVoltageHighLimit.setStatus('current')
if mibBuilder.loadTexts: upsConfigLineOutputVoltageHighLimit.setDescription('This object represents the Line output High Voltage Limit.')
upsConfigLineOutputVoltageLowLimit = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 3), Integer32()).setUnits('volttenth').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigLineOutputVoltageLowLimit.setStatus('current')
if mibBuilder.loadTexts: upsConfigLineOutputVoltageLowLimit.setDescription('This object represents the Line output Low Voltage Limit.')
upsConfigFanOnTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 4), Integer32()).setUnits('degreeC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigFanOnTemperature.setStatus('current')
if mibBuilder.loadTexts: upsConfigFanOnTemperature.setDescription('This object represents the Fan on temperature.')
upsShutdownStatus = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 5), Integer32()).setUnits('').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsShutdownStatus.setStatus('current')
if mibBuilder.loadTexts: upsShutdownStatus.setDescription('This object tells us if output is disabled or enabled.')
upsInverterOffDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 6), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsInverterOffDelayTime.setStatus('current')
if mibBuilder.loadTexts: upsInverterOffDelayTime.setDescription('This object represents the inverter off delay time.')
upsConfigIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigIPAddress.setStatus('current')
if mibBuilder.loadTexts: upsConfigIPAddress.setDescription('This objects displays the IP address of the RMU.')
upsConfigNetMask = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigNetMask.setStatus('current')
if mibBuilder.loadTexts: upsConfigNetMask.setDescription('This object displays the Net Mask of the RMU.')
upsConfigGateway = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigGateway.setStatus('current')
if mibBuilder.loadTexts: upsConfigGateway.setDescription('This object displays the Gateway of the RMU.')
upsConfigSnmpCommunity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigSnmpCommunity.setStatus('current')
if mibBuilder.loadTexts: upsConfigSnmpCommunity.setDescription('This object displays the SNMP community')
upsConfigSnmpTrapIPDestination = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigSnmpTrapIPDestination.setStatus('current')
if mibBuilder.loadTexts: upsConfigSnmpTrapIPDestination.setDescription('This object displays the SNMP Trap IP destination.')
mibBuilder.exportSymbols("Argus-Power-System-MIB", upsIdentSiteCountry=upsIdentSiteCountry, upsOutput=upsOutput, NonNegativeInteger=NonNegativeInteger, upsAlarmTable=upsAlarmTable, upsAgentEventTrap=upsAgentEventTrap, upsOutputPowerVA=upsOutputPowerVA, upsAlarmStatus=upsAlarmStatus, upsOutputSource=upsOutputSource, upsConfigNetMask=upsConfigNetMask, upsShutdownStatus=upsShutdownStatus, upsIdentProductCode=upsIdentProductCode, upsAgentShutdownTrap=upsAgentShutdownTrap, upsIdentSiteCity=upsIdentSiteCity, upsAlarmDescr=upsAlarmDescr, upsInputFrequency=upsInputFrequency, upsIdentContactName=upsIdentContactName, upsIdentAgentSoftwareVersion=upsIdentAgentSoftwareVersion, PhysAddress=PhysAddress, upsBatteryLowWarning=upsBatteryLowWarning, upsIdent=upsIdent, upsAgentStartupTrap=upsAgentStartupTrap, upsConfigSnmpTrapIPDestination=upsConfigSnmpTrapIPDestination, upsTrap=upsTrap, upsExtraIntegerValue=upsExtraIntegerValue, upsTraps=upsTraps, upsConfig=upsConfig, upsPowerFactor=upsPowerFactor, upsOutputPowerWatt=upsOutputPowerWatt, upsConfigLineOutputVoltageLowLimit=upsConfigLineOutputVoltageLowLimit, upsIdentAttachedDevices=upsIdentAttachedDevices, upsOutputVoltage=upsOutputVoltage, PositiveInteger=PositiveInteger, upsIdentPhoneNumber=upsIdentPhoneNumber, upsIdentName=upsIdentName, upsIdentManufacturer=upsIdentManufacturer, upsAlarmEntry=upsAlarmEntry, upsExtraEntry=upsExtraEntry, upsOutputTable=upsOutputTable, upsConfigSnmpCommunity=upsConfigSnmpCommunity, upsOutputEntry=upsOutputEntry, upsIdentUPSSoftwareVersion=upsIdentUPSSoftwareVersion, upsInputNumLines=upsInputNumLines, upsMinutesOnBattery=upsMinutesOnBattery, upsInputEntry=upsInputEntry, upsAlarm=upsAlarm, upsInverterOffDelayTime=upsInverterOffDelayTime, upsBattery=upsBattery, upsExtraTable=upsExtraTable, upsExtra=upsExtra, upsBatteryStatus=upsBatteryStatus, upsBatteryVoltage=upsBatteryVoltage, upsAlarmTrap=upsAlarmTrap, upsIdentTime=upsIdentTime, upsConfigGateway=upsConfigGateway, upsConfigLineOutputVoltageHighLimit=upsConfigLineOutputVoltageHighLimit, upsOutputFrequency=upsOutputFrequency, PYSNMP_MODULE_ID=argus, upsConfigLineQualifyTime=upsConfigLineQualifyTime, upsBatteryCapacity=upsBatteryCapacity, upsBatteryTemperature=upsBatteryTemperature, upsAlarmsPresent=upsAlarmsPresent, upsPower=upsPower, argus=argus, upsBatteryChargingCurrent=upsBatteryChargingCurrent, DisplayString=DisplayString, upsConfigIPAddress=upsConfigIPAddress, upsExtraIndex=upsExtraIndex, upsInputLineIndex=upsInputLineIndex, upsIdentModel=upsIdentModel, upsDevice=upsDevice, upsInputTable=upsInputTable, upsInputVoltage=upsInputVoltage, upsIdentSiteName=upsIdentSiteName, upsIdentSiteRegion=upsIdentSiteRegion, upsConfigFanOnTemperature=upsConfigFanOnTemperature, upsExtraCount=upsExtraCount, upsExtraStringValue=upsExtraStringValue, upsOutputNumLines=upsOutputNumLines, upsOutputCurrent=upsOutputCurrent, upsOutputLineIndex=upsOutputLineIndex, upsOutputPercentLoad=upsOutputPercentLoad, upsAgentFaultTrap=upsAgentFaultTrap, upsAlarmId=upsAlarmId, upsInput=upsInput, upsIdentDate=upsIdentDate, upsExtraName=upsExtraName)
