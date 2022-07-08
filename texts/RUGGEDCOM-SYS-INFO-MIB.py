#
# PySNMP MIB module RUGGEDCOM-SYS-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ros/RUGGEDCOM-SYS-INFO-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:27:52 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ruggedcomMgmt, = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Counter64, TimeTicks, Counter32, Integer32, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Counter64", "TimeTicks", "Counter32", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rcSysInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 2))
rcSysInfo.setRevisions(('2014-10-08 17:00', '2012-08-30 17:00', '2012-06-01 17:00', '2011-04-05 10:00', '2010-09-16 13:00', '2009-05-17 13:00', '2008-12-17 13:00', '2008-10-09 10:00', '2008-09-12 14:00', '2008-02-15 14:00', '2006-09-06 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rcSysInfo.setRevisionsDescriptions(('Added new board IDs in RcMainBoard TEXTUAL-CONVENTION.', 'Added new objects: rcDeviceStsKeysDflt and rcDeviceInfoMinBootSwVer\n         related to the device security in the group \n         rcSysDeviceSecurityGroup01.', 'Added new objects rcDeviceStsPwdsWeak related to the device\n        security in the group rcSysDeviceSecurityGroup.', "Extended RcHardwareStatus textual convention. Added\n         'notConnected(4)' value.", 'Added Fan Bank Module hardware status elements.\n         Added new objects:\n        \trcDeviceStsFanBank1 and rcDeviceStsFanBank2\n         Added new types related to module Slot and state change.', 'Fixed description for object rcDeviceCommClearSyslog.\n         Added new object:\n        \trcDeviceCommClearLogs\n         Removed statement about mandatory groups from groups descriptions.', 'Fixed mistyped object name for rcDeviceStsErrorAlarm in \n         rcSysStsObjectsGroup objects list.\n         Added new object:\n        \trcDeviceCommIdentify.', 'Added new objects:\n        \trcDeviceStsErrorAlarm,\n        \trcDeviceStsFailSafeRelay,\n        \trcDeviceStsNoOfActiveAlarms.', 'Adde new enumeration labels for rcDeviceInfoMainBoardType\n        for new hardware platform support.', "Removed '_' characters from enumeration labels.\n        Added new objects:\n           rcDeviceInfoPendingBootSwVersion\n           rcDeviceInfoPendingMainSwVersion\n           rcDeviceInfoCfgRevision\n\t\t   rcDeviceCommReset           \n           rcDeviceCommLoadDefaultCfg,\n\t\t   rcDeviceCommClearAlarms,\n\t\t   rcDeviceCommClearSyslog\n        ", 'The initial version of RuggedCom system information MIB.',))
if mibBuilder.loadTexts: rcSysInfo.setLastUpdated('201410081700Z')
if mibBuilder.loadTexts: rcSysInfo.setOrganization('RuggedCom')
if mibBuilder.loadTexts: rcSysInfo.setContactInfo('Postal: RuggedCom Inc.\n                300 Applewood Crescent\n                Concord, Ontario, \n                L4K 5C7 Canada\n        Tel:    1-905-856-5288\n        E-Mail: support@ruggedcom.com')
if mibBuilder.loadTexts: rcSysInfo.setDescription('RuggedCom system information MIB.')
class RcHardwareStatus(TextualConvention, Integer32):
    description = 'A status of a hardware module in the RuggedCom device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notPresent", 1), ("functional", 2), ("notFunctional", 3), ("notConnected", 4))

class RcFanStatus(TextualConvention, Integer32):
    description = 'The status of a fan-bank.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notPresent", 1), ("failed", 2), ("standby", 3), ("off", 4), ("on", 5))

class RcHotswapModuleSlot(TextualConvention, Integer32):
    description = 'A physical slot holding the hotswapable module (ROX 2 specific).\n\t\t As the value 0 is forbidden in SNMP enumerations, this value is the \n\t\t value 1 higher than some other ROX 2 slot values'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("pm1", 1), ("lm1", 2), ("lm2", 3), ("lm3", 4), ("cm", 5), ("sm", 6), ("lm4", 7), ("lm5", 8), ("lm6", 9), ("pm2", 10), ("main", 11), ("em", 12))

class RcHotswapModuleState(TextualConvention, Integer32):
    description = 'A status of a hardware module in the RuggedCom device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("empty", 1), ("disabled", 2), ("resetting", 3), ("operating", 4), ("failed", 5), ("unknown", 255))

class RcMainBoard(TextualConvention, Integer32):
    description = 'A main board type code. This textual convention will be updated\n\t\tany time when new main board type is developed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 61, 62, 63, 64, 65, 66, 67, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265))
    namedValues = NamedValues(("rsMCPU2", 1), ("rs400revB2", 2), ("rmc30", 3), ("rs900revB1F", 4), ("rs900revB1noF", 5), ("rs1600M", 6), ("rs400revC1", 7), ("rsG2100", 8), ("rs900G", 9), ("rsG2200", 10), ("rs969", 11), ("rs900v2F", 12), ("rs900v2noF", 13), ("rs416", 15), ("rsRMC30Ksz80001", 16), ("rs930", 17), ("rs969v2", 18), ("rs910", 19), ("rs920", 20), ("rs940G", 21), ("rsi80x", 22), ("rsG2300", 23), ("rs416v2", 24), ("rsg2288", 25), ("rp110", 26), ("rs900GP", 27), ("rs900M", 28), ("rs950G", 29), ("rsG2488", 61), ("rsG2488v2", 62), ("rsG2488v3", 63), ("rmc8388A", 64), ("rmc8388B", 65), ("rmc8388C", 66), ("rsG920P", 67), ("rsMCPU", 255), ("rx1000", 256), ("rx1100", 257), ("rx1500", 258), ("rx1501", 259), ("rx1510", 260), ("rx1511", 261), ("rx1512", 262), ("rx5000", 263), ("mx5000", 264), ("rx1400", 265))

rcSysInfoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5))
rcSysInfoGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2))
rcDeviceError = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1))
if mibBuilder.loadTexts: rcDeviceError.setStatus('current')
if mibBuilder.loadTexts: rcDeviceError.setDescription('The main subtree for various errors detected in RuggedCom devices.')
rcDeviceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2))
if mibBuilder.loadTexts: rcDeviceStatus.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStatus.setDescription('The main subtree for various status information detected in \n        RuggedCom devices.')
rcDeviceInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3))
if mibBuilder.loadTexts: rcDeviceInfo.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfo.setDescription('The main subtree for RuggedCom devices manufacturing information.')
rcDeviceCommands = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 2, 4))
if mibBuilder.loadTexts: rcDeviceCommands.setStatus('current')
if mibBuilder.loadTexts: rcDeviceCommands.setDescription('The main subtree for device control commands.')
rcDeviceErrBootupError = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrBootupError.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrBootupError.setDescription('The error discovered during bootup process.\n         If there was no error during device bootup, zero length string\n         will be retreived.')
rcDeviceErrWatchdogReset = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrWatchdogReset.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrWatchdogReset.setDescription('Indicates whether the last device reboot was caused by wachdog.')
rcDeviceErrConfigurationFailure = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrConfigurationFailure.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrConfigurationFailure.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrConfigurationFailure.setDescription('Indicates whether errors were detected while applying configuration \n         settings from configuration file.  \n         Configuration is updated from the configureation file at bootup time \n         when file is loaded from nonvolatile memory, or when new file is \n         downloaded to the device.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrCrashLogCreated = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrCrashLogCreated.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrCrashLogCreated.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrCrashLogCreated.setDescription('Indicates whether the device error that caused creation of an \n         entry in crashlog.txt file was detected.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrStackOverflow = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrStackOverflow.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrStackOverflow.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrStackOverflow.setDescription('Indicates whether the stack of any of the system tasks is used\n         over the system threshold.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrHeapError = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrHeapError.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrHeapError.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrHeapError.setDescription('Indicates whether the system memory corruption was detected.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrDateAndTimeSetFailed = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrDateAndTimeSetFailed.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrDateAndTimeSetFailed.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrDateAndTimeSetFailed.setDescription('Indicates whether the date and time setting in the device falied.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrNtpServerUnreachable = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrNtpServerUnreachable.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrNtpServerUnreachable.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrNtpServerUnreachable.setDescription('Indicates whether the NTP server (if required) can be reached.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrBootPTftpTrFailed = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrBootPTftpTrFailed.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrBootPTftpTrFailed.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrBootPTftpTrFailed.setDescription('Indicates whether the the file was transfered properly after \n         obtaining IP address from the BootP server.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrRadiusServerUnreachable = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrRadiusServerUnreachable.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrRadiusServerUnreachable.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrRadiusServerUnreachable.setDescription('Indicates whether the RADIUS server (if required) can be reached.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceErrTacacsServerUnreachable = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceErrTacacsServerUnreachable.setReference('genericTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceErrTacacsServerUnreachable.setStatus('current')
if mibBuilder.loadTexts: rcDeviceErrTacacsServerUnreachable.setDescription('Indicates whether the TACACS+ server (if required) can be reached.\n         Whenever the value of this object changes from false(2) to true(1),\n         the device will generate genericTrap notification.')
rcDeviceStsCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 1), Integer32()).setUnits('tenths of percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsCpuUsage.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsCpuUsage.setDescription('The percentage in tenths of percent of available CPU cycles used \n         for device operation as measured over the last second when \n         object was retreived.')
rcDeviceStsAvailableRam = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsAvailableRam.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsAvailableRam.setDescription('The total number of bytes of RAM still available in the system\n         control CPU.')
rcDeviceStsTemperature = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 3), Integer32()).setUnits('Celsius degrees').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsTemperature.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsTemperature.setDescription('The temperature measured in the device.')
rcDeviceStsPowerSupply1 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 4), RcHardwareStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsPowerSupply1.setReference('powerSupplyTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceStsPowerSupply1.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsPowerSupply1.setDescription('Indicates the status of Power Supply Module 1.\n         Whenever the value of this object changes from functional(2) to \n         notFunctional(3), or from notFunctionl(3) to functional(2),\n         the device will generate powerSupplyTrap notification.')
rcDeviceStsPowerSupply2 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 5), RcHardwareStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsPowerSupply2.setReference('powerSupplyTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceStsPowerSupply2.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsPowerSupply2.setDescription('Indicates the status of Power Supply Module 2.\n         Whenever the value of this object changes from functional(2) to \n         notFunctional(3), or from notFunctionl(3) to functional(2),\n         the device will generate powerSupplyTrap notification.')
rcDeviceStsCpuUsagePercent = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 6), Integer32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsCpuUsagePercent.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsCpuUsagePercent.setDescription('The percentage of available CPU cycles used for device operation\n         as measured over the last second when object was retreived.')
rcDeviceStsFailSafeRelay = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("energized", 1), ("deEnergized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsFailSafeRelay.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsFailSafeRelay.setDescription('Indicates status of fail safe relay in the device.\n         Fail safe relay is deEnergized(2) if there is at least one active\n         alarm recorded in the device.')
rcDeviceStsErrorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsErrorAlarm.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsErrorAlarm.setDescription('Indicates that at least one alarm of level ERROR, ALERT or CRITICAL\n         is active in the device.')
rcDeviceStsNoOfActiveAlarms = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsNoOfActiveAlarms.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsNoOfActiveAlarms.setDescription('Number of active alarms currently recorded in device.')
rcDeviceStsFanBank1 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 10), RcFanStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsFanBank1.setReference('fanBankTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceStsFanBank1.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsFanBank1.setDescription('Indicates the status of Fan Bank Module 1.')
rcDeviceStsFanBank2 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 11), RcFanStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsFanBank2.setReference('fanBankTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceStsFanBank2.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsFanBank2.setDescription('Indicates the status of Fan Bank Module 2.')
rcDeviceStsPwdsWeak = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 12), Bits().clone(namedValues=NamedValues(("adminPwd", 0), ("operPwd", 1), ("guestPwd", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsPwdsWeak.setReference('weakPasswordTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceStsPwdsWeak.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsPwdsWeak.setDescription("Indicates if any of passwords is configured as 'weak'.\n         Change in the value of the bit in this object from '0' to  '1' \n         will generate weakPasswordTrap.")
rcDeviceStsKeysDflt = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 2, 13), Bits().clone(namedValues=NamedValues(("sshDfltKeys", 0), ("sslDfltKeys", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceStsKeysDflt.setReference('defaultKeysTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceStsKeysDflt.setStatus('current')
if mibBuilder.loadTexts: rcDeviceStsKeysDflt.setDescription("Indicates if any of secure services uses default keys and/or \n         certificates. Customer is advised to update keys for secure\n         services if defaults are used.\n         Change in the value of the bit in this object from '0' to  '1' \n         will generate defaultKeysTrap notification.")
rcDeviceInfoSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoSerialNumber.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoSerialNumber.setDescription('The manufacturing serial number of the device.')
rcDeviceInfoBootSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoBootSwVersion.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoBootSwVersion.setDescription('The version and the build date of the boot loader software.')
rcDeviceInfoMainSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoMainSwVersion.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoMainSwVersion.setDescription('The version and the build date of the main operating system \n         software.')
rcDeviceInfoMainBoardType = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 4), RcMainBoard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoMainBoardType.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoMainBoardType.setDescription('The identification code of the device main board.')
rcDeviceInfoTotalRam = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoTotalRam.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoTotalRam.setDescription('The total number of bytes of RAM in the system control CPU.')
rcDeviceInfoPendingBootSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoPendingBootSwVersion.setReference('swUpgradeTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceInfoPendingBootSwVersion.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoPendingBootSwVersion.setDescription('The version and the build date of the boot loader software\n         that has been loaded to the device and is pending reboot.\n         Whenever the value of this object changes from zero-length string\n         to any string of non-zero length, the device will generate \n         swUpgradeTrap notification.')
rcDeviceInfoPendingMainSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoPendingMainSwVersion.setReference('swUpgradeTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceInfoPendingMainSwVersion.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoPendingMainSwVersion.setDescription('The version and the build date of the main operating system\n         software that has been loaded to the device and is pending reboot.\n         Whenever the value of this object changes from zero-length string\n         to any string of non-zero length, the device will generate \n         swUpgradeTrap notification.')
rcDeviceInfoCfgRevision = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoCfgRevision.setReference('cfgChangeTrap notification is defined in ruggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceInfoCfgRevision.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoCfgRevision.setDescription('The configuration file revision. \n         The revision number will be updated whenever file is saved to the \n         flash memory. This number is recorded in config.csv at the time file\n         is uploaded from the device.\n         Whenever the value of this object changes the device will generate \n         cfgChangeTrap notification.')
rcDeviceInfoMinBootSwVer = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 3, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcDeviceInfoMinBootSwVer.setReference('bootVersionMismatchTrap notification is defined in \n    \truggedcomTrapsModule.')
if mibBuilder.loadTexts: rcDeviceInfoMinBootSwVer.setStatus('current')
if mibBuilder.loadTexts: rcDeviceInfoMinBootSwVer.setDescription('The minimum version of the boot loader software required by \n         ROS device. If this version is not newer than the version\n         retreived as a value of object rcDeviceInfoBootSwVersion, trap\n         bootVersionMismatchTrap will be generated.')
rcDeviceCommReset = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDeviceCommReset.setStatus('current')
if mibBuilder.loadTexts: rcDeviceCommReset.setDescription("Setting the value of this object to 'true(1)' will cause device \n          to reboot.\n          As a result of Read request the agent will return value 'false(2)'.")
rcDeviceCommLoadDefaultCfg = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 4, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDeviceCommLoadDefaultCfg.setStatus('current')
if mibBuilder.loadTexts: rcDeviceCommLoadDefaultCfg.setDescription("Setting the value of this object to 'true(1)' will force device \n          to load default configuration to all tables.\n          As a result of Read request the agent will return value 'false(2)'.")
rcDeviceCommClearAlarms = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDeviceCommClearAlarms.setStatus('current')
if mibBuilder.loadTexts: rcDeviceCommClearAlarms.setDescription("Setting the value of this object to 'true(1)' will cause device \n         to clear all alarms.\n         As a result of Read request the agent will return value 'false(2)'.")
rcDeviceCommClearSyslog = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 4, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDeviceCommClearSyslog.setStatus('current')
if mibBuilder.loadTexts: rcDeviceCommClearSyslog.setDescription("Setting the value of this object to 'true(1)' will cause device \n         to clear syslog.txt file.\n         As a result of Read request the agent will return value 'false(2)'.")
rcDeviceCommClearLogs = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 4, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDeviceCommClearLogs.setStatus('current')
if mibBuilder.loadTexts: rcDeviceCommClearLogs.setDescription("Setting the value of this object to 'true(1)' will cause device \n         to clear syslog.txt and crashlog.txt files.\n         As a result of Read request the agent will return value 'false(2)'.")
rcDeviceCommIdentify = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 2, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDeviceCommIdentify.setStatus('current')
if mibBuilder.loadTexts: rcDeviceCommIdentify.setDescription('Time Period in seconds for which the device should continue flashing\n         the LEDs when possible so that device is visually recognized.\n         Setting this value to any value greater than 0 will start LED flash\n         timer on the device.Setting the value to 0 will stop the LED flash\n         timer. On Read request agent always sends back the existing Timeout \n         value for LED flash Timer.')
rcSysErrObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 1)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrBootupError"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrWatchdogReset"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrConfigurationFailure"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrCrashLogCreated"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrStackOverflow"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrHeapError"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrDateAndTimeSetFailed"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrNtpServerUnreachable"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrBootPTftpTrFailed"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrRadiusServerUnreachable"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceErrTacacsServerUnreachable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysErrObjectsGroup = rcSysErrObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysErrObjectsGroup.setDescription('A group of objects providing information about irregularities\n        in the device.')
rcSysStsObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 2)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsCpuUsage"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsCpuUsagePercent"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsAvailableRam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysStsObjectsGroup = rcSysStsObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysStsObjectsGroup.setDescription('A group of objects providing information device resources.')
rcSysStsObjectsTemperatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 3)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsTemperature"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysStsObjectsTemperatureGroup = rcSysStsObjectsTemperatureGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysStsObjectsTemperatureGroup.setDescription('This group is created to allow MIBs for products that do not have\n        temperature sensore installed to exclude rcDeviceStsTemperature \n        object.')
rcSysStsPowerSupplyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 4)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsPowerSupply1"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsPowerSupply2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysStsPowerSupplyGroup = rcSysStsPowerSupplyGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysStsPowerSupplyGroup.setDescription('A group of objects providing information about power supply modules\n        in the device. This group is mandatory for products with redundant\n        power supply.')
rcSysInfoDeviceInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 5)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoMainBoardType"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoTotalRam"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoBootSwVersion"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoMainSwVersion"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoPendingBootSwVersion"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoPendingMainSwVersion"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoCfgRevision"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysInfoDeviceInfoGroup = rcSysInfoDeviceInfoGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysInfoDeviceInfoGroup.setDescription("A group of object providing manufacturer's information about \n        product's main board hardware, software, identification.")
rcSysDeviceCommGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 6)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceCommReset"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceCommLoadDefaultCfg"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceCommClearAlarms"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceCommClearSyslog"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceCommClearLogs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysDeviceCommGroup = rcSysDeviceCommGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysDeviceCommGroup.setDescription('A group of object providing device control commands.')
rcSysDeviceCommIdentifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 7)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceCommIdentify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysDeviceCommIdentifyGroup = rcSysDeviceCommIdentifyGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysDeviceCommIdentifyGroup.setDescription('A group of object providing device control commands for \n        visual recognisation of the device (LED flashing).')
rcSysStsObjectsGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 8)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsCpuUsage"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsCpuUsagePercent"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsAvailableRam"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsErrorAlarm"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsFailSafeRelay"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsNoOfActiveAlarms"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysStsObjectsGroup1 = rcSysStsObjectsGroup1.setStatus('current')
if mibBuilder.loadTexts: rcSysStsObjectsGroup1.setDescription('A group of objects providing information device resources.')
rcSysStsFanBankGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 9)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsFanBank1"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsFanBank2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysStsFanBankGroup = rcSysStsFanBankGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysStsFanBankGroup.setDescription('A group of objects providing information about fan bank modules\n        in the device. This group is mandatory for products with redundant\n        fan banks.')
rcSysDeviceSecurityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 10)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsPwdsWeak"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysDeviceSecurityGroup = rcSysDeviceSecurityGroup.setStatus('current')
if mibBuilder.loadTexts: rcSysDeviceSecurityGroup.setDescription('A group of object providing device control commands.')
rcSysDeviceSecurityGroup01 = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 2, 5, 2, 11)).setObjects(("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsPwdsWeak"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceStsKeysDflt"), ("RUGGEDCOM-SYS-INFO-MIB", "rcDeviceInfoMinBootSwVer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcSysDeviceSecurityGroup01 = rcSysDeviceSecurityGroup01.setStatus('current')
if mibBuilder.loadTexts: rcSysDeviceSecurityGroup01.setDescription('A group of object providing device control commands.')
mibBuilder.exportSymbols("RUGGEDCOM-SYS-INFO-MIB", rcDeviceInfoBootSwVersion=rcDeviceInfoBootSwVersion, RcMainBoard=RcMainBoard, rcDeviceStsFanBank1=rcDeviceStsFanBank1, rcDeviceStsPowerSupply1=rcDeviceStsPowerSupply1, rcDeviceInfoCfgRevision=rcDeviceInfoCfgRevision, rcSysStsFanBankGroup=rcSysStsFanBankGroup, rcDeviceStsErrorAlarm=rcDeviceStsErrorAlarm, rcDeviceErrRadiusServerUnreachable=rcDeviceErrRadiusServerUnreachable, rcDeviceStsKeysDflt=rcDeviceStsKeysDflt, rcDeviceErrConfigurationFailure=rcDeviceErrConfigurationFailure, rcDeviceStsPwdsWeak=rcDeviceStsPwdsWeak, rcDeviceStsTemperature=rcDeviceStsTemperature, rcDeviceInfoSerialNumber=rcDeviceInfoSerialNumber, rcDeviceInfoTotalRam=rcDeviceInfoTotalRam, RcHardwareStatus=RcHardwareStatus, rcDeviceInfoPendingBootSwVersion=rcDeviceInfoPendingBootSwVersion, rcDeviceInfoPendingMainSwVersion=rcDeviceInfoPendingMainSwVersion, rcSysStsPowerSupplyGroup=rcSysStsPowerSupplyGroup, rcDeviceInfoMainBoardType=rcDeviceInfoMainBoardType, RcHotswapModuleState=RcHotswapModuleState, rcSysStsObjectsGroup1=rcSysStsObjectsGroup1, rcSysInfoGroups=rcSysInfoGroups, rcDeviceErrStackOverflow=rcDeviceErrStackOverflow, RcFanStatus=RcFanStatus, rcDeviceStsAvailableRam=rcDeviceStsAvailableRam, rcDeviceStsFanBank2=rcDeviceStsFanBank2, rcDeviceErrDateAndTimeSetFailed=rcDeviceErrDateAndTimeSetFailed, rcDeviceCommReset=rcDeviceCommReset, rcDeviceCommLoadDefaultCfg=rcDeviceCommLoadDefaultCfg, rcDeviceCommClearLogs=rcDeviceCommClearLogs, rcDeviceStsCpuUsage=rcDeviceStsCpuUsage, rcSysStsObjectsGroup=rcSysStsObjectsGroup, rcSysDeviceCommIdentifyGroup=rcSysDeviceCommIdentifyGroup, RcHotswapModuleSlot=RcHotswapModuleSlot, rcDeviceErrWatchdogReset=rcDeviceErrWatchdogReset, rcDeviceStsPowerSupply2=rcDeviceStsPowerSupply2, rcDeviceErrBootPTftpTrFailed=rcDeviceErrBootPTftpTrFailed, rcDeviceInfoMainSwVersion=rcDeviceInfoMainSwVersion, rcDeviceInfoMinBootSwVer=rcDeviceInfoMinBootSwVer, rcDeviceError=rcDeviceError, rcDeviceStsNoOfActiveAlarms=rcDeviceStsNoOfActiveAlarms, rcDeviceErrBootupError=rcDeviceErrBootupError, rcDeviceErrTacacsServerUnreachable=rcDeviceErrTacacsServerUnreachable, rcDeviceErrCrashLogCreated=rcDeviceErrCrashLogCreated, rcDeviceCommClearSyslog=rcDeviceCommClearSyslog, rcDeviceCommClearAlarms=rcDeviceCommClearAlarms, PYSNMP_MODULE_ID=rcSysInfo, rcDeviceStatus=rcDeviceStatus, rcDeviceErrHeapError=rcDeviceErrHeapError, rcSysDeviceSecurityGroup=rcSysDeviceSecurityGroup, rcDeviceErrNtpServerUnreachable=rcDeviceErrNtpServerUnreachable, rcSysInfoConformance=rcSysInfoConformance, rcDeviceCommIdentify=rcDeviceCommIdentify, rcSysDeviceSecurityGroup01=rcSysDeviceSecurityGroup01, rcSysDeviceCommGroup=rcSysDeviceCommGroup, rcSysInfo=rcSysInfo, rcDeviceInfo=rcDeviceInfo, rcDeviceCommands=rcDeviceCommands, rcDeviceStsFailSafeRelay=rcDeviceStsFailSafeRelay, rcDeviceStsCpuUsagePercent=rcDeviceStsCpuUsagePercent, rcSysStsObjectsTemperatureGroup=rcSysStsObjectsTemperatureGroup, rcSysErrObjectsGroup=rcSysErrObjectsGroup, rcSysInfoDeviceInfoGroup=rcSysInfoDeviceInfoGroup)
