#
# PySNMP MIB module AT-SETUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-SETUP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ObjectIdentity, Counter32, ModuleIdentity, Gauge32, Unsigned32, NotificationType, iso, Bits, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ObjectIdentity", "Counter32", "ModuleIdentity", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "Counter64", "MibIdentifier")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
setup = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500))
setup.setRevisions(('2014-04-30 00:00', '2013-10-14 00:00', '2012-09-21 00:00', '2010-11-20 00:00', '2010-10-08 00:00', '2010-09-10 00:00', '2010-09-08 00:00', '2010-06-15 00:15', '2010-04-09 00:00', '2008-10-02 00:00', '2008-09-30 00:00', '2008-09-24 00:00', '2008-05-21 00:00',))
if mibBuilder.loadTexts: setup.setLastUpdated('201404300000Z')
if mibBuilder.loadTexts: setup.setOrganization('Allied Telesis, Inc.')
class SystemFileOperationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("success", 2), ("failure", 3), ("saving", 4), ("syncing", 5))

restartDevice = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartDevice.setStatus('deprecated')
restartStkMemberDevice = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartStkMemberDevice.setStatus('current')
firmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2))
currentFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1))
currSoftVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftVersion.setStatus('current')
currSoftName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftName.setStatus('current')
currSoftSaveAs = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currSoftSaveAs.setStatus('deprecated')
currSoftSaveToFile = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currSoftSaveToFile.setStatus('current')
currSoftSaveStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 5), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftSaveStatus.setStatus('current')
currSoftLastSaveResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftLastSaveResult.setStatus('current')
nextBootFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2))
nextBootVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextBootVersion.setStatus('current')
nextBootPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nextBootPath.setStatus('current')
nextBootSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextBootSetStatus.setStatus('current')
nextBootLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextBootLastSetResult.setStatus('current')
backupFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3))
backupVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupVersion.setStatus('current')
backupPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupPath.setStatus('current')
backupSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSetStatus.setStatus('current')
backupLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupLastSetResult.setStatus('current')
deviceConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3))
runningConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1))
runCnfgSaveAs = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: runCnfgSaveAs.setStatus('current')
runCnfgSaveAsStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 2), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: runCnfgSaveAsStatus.setStatus('current')
runCnfgLastSaveResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: runCnfgLastSaveResult.setStatus('current')
nextBootConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2))
bootCnfgPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bootCnfgPath.setStatus('current')
bootCnfgExists = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootCnfgExists.setStatus('current')
bootCnfgSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootCnfgSetStatus.setStatus('current')
bootCnfgLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootCnfgLastSetResult.setStatus('current')
defaultConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3))
dfltCnfgPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfltCnfgPath.setStatus('current')
dfltCnfgExists = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfltCnfgExists.setStatus('current')
backupConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4))
backupCnfgPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupCnfgPath.setStatus('current')
backupCnfgExists = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupCnfgExists.setStatus('current')
backupCnfgSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupCnfgSetStatus.setStatus('current')
backupCnfgLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupCnfgLastSetResult.setStatus('current')
serviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5))
srvcTelnetEnable = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srvcTelnetEnable.setStatus('current')
srvcSshEnable = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srvcSshEnable.setStatus('current')
guiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6))
guiAppletConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1))
guiAppletSysSwVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: guiAppletSysSwVer.setStatus('current')
guiAppletSwVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: guiAppletSwVer.setStatus('current')
mibBuilder.exportSymbols("AT-SETUP-MIB", srvcSshEnable=srvcSshEnable, restartDevice=restartDevice, currSoftSaveStatus=currSoftSaveStatus, nextBootPath=nextBootPath, runCnfgSaveAs=runCnfgSaveAs, backupFirmware=backupFirmware, bootCnfgPath=bootCnfgPath, bootCnfgExists=bootCnfgExists, PYSNMP_MODULE_ID=setup, currSoftLastSaveResult=currSoftLastSaveResult, guiAppletConfig=guiAppletConfig, bootCnfgLastSetResult=bootCnfgLastSetResult, SystemFileOperationType=SystemFileOperationType, backupSetStatus=backupSetStatus, currSoftName=currSoftName, backupVersion=backupVersion, setup=setup, nextBootSetStatus=nextBootSetStatus, currSoftVersion=currSoftVersion, defaultConfig=defaultConfig, backupCnfgSetStatus=backupCnfgSetStatus, backupCnfgExists=backupCnfgExists, guiAppletSysSwVer=guiAppletSysSwVer, backupPath=backupPath, firmware=firmware, runCnfgSaveAsStatus=runCnfgSaveAsStatus, nextBootVersion=nextBootVersion, backupCnfgLastSetResult=backupCnfgLastSetResult, nextBootFirmware=nextBootFirmware, runCnfgLastSaveResult=runCnfgLastSaveResult, runningConfig=runningConfig, currSoftSaveToFile=currSoftSaveToFile, dfltCnfgExists=dfltCnfgExists, backupCnfgPath=backupCnfgPath, srvcTelnetEnable=srvcTelnetEnable, deviceConfiguration=deviceConfiguration, currSoftSaveAs=currSoftSaveAs, bootCnfgSetStatus=bootCnfgSetStatus, guiAppletSwVer=guiAppletSwVer, guiConfig=guiConfig, nextBootConfig=nextBootConfig, serviceConfig=serviceConfig, restartStkMemberDevice=restartStkMemberDevice, currentFirmware=currentFirmware, backupLastSetResult=backupLastSetResult, dfltCnfgPath=dfltCnfgPath, backupConfig=backupConfig, nextBootLastSetResult=nextBootLastSetResult)
