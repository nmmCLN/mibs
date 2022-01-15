#
# PySNMP MIB module XF-SOFTWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/XF-SOFTWARE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:30 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, MibIdentifier, ModuleIdentity, iso, Integer32, Bits, Counter64, Unsigned32, NotificationType, Counter32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "MibIdentifier", "ModuleIdentity", "iso", "Integer32", "Bits", "Counter64", "Unsigned32", "NotificationType", "Counter32", "TimeTicks", "IpAddress")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
XfProductnumber, xfPlatform, XfProductRevision = mibBuilder.importSymbols("XF-TOP-MIB", "XfProductnumber", "xfPlatform", "XfProductRevision")
xfSoftwareMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 81, 2, 7))
xfSoftwareMIB.setRevisions(('2008-03-05 18:03', '2007-11-26 12:44', '2007-06-11 09:12', '2007-04-10 09:09', '2003-06-19 10:30', '2002-03-08 08:41', '2002-01-14 09:11', '2001-10-10 12:15', '2004-01-30 13:51', '2004-08-03 08:23', '2005-01-31 08:26', '2005-02-09 08:13',))
if mibBuilder.loadTexts: xfSoftwareMIB.setLastUpdated('200803060000Z')
if mibBuilder.loadTexts: xfSoftwareMIB.setOrganization('Ericsson-Norway')
class XfSwRelease(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2)

class XfSwEnableDisable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

xfSwObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1))
xfSwLoadModuleTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1), )
if mibBuilder.loadTexts: xfSwLoadModuleTable.setStatus('current')
xfSwLoadModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1), ).setIndexNames((0, "XF-SOFTWARE-MIB", "xfSwRelease"), (0, "XF-SOFTWARE-MIB", "xfSwLoadModuleIndex"))
if mibBuilder.loadTexts: xfSwLoadModuleEntry.setStatus('current')
xfSwRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 1), XfSwRelease()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwRelease.setStatus('current')
xfSwLoadModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLoadModuleIndex.setStatus('current')
xfSwLoadModuleProductNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 3), XfProductnumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLoadModuleProductNumber.setStatus('current')
xfSwLoadModuleRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 4), XfProductRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLoadModuleRevision.setStatus('current')
xfSwLoadModuleOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("passive", 1), ("upgradeStarted", 2), ("upgradeFinished", 3), ("upgradeFailed", 4), ("upgradeAborted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLoadModuleOperStatus.setStatus('current')
xfSwLoadModuleFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("downloadFailure", 1), ("programFailure", 2), ("noFailure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLoadModuleFailure.setStatus('current')
xfSwLoadModuleProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLoadModuleProgress.setStatus('current')
xfSwLoadModuleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLoadModuleDescription.setStatus('current')
xfSwReleaseTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2), )
if mibBuilder.loadTexts: xfSwReleaseTable.setStatus('current')
xfSwReleaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1), ).setIndexNames((0, "XF-SOFTWARE-MIB", "xfSwReleaseIndex"))
if mibBuilder.loadTexts: xfSwReleaseEntry.setStatus('current')
xfSwReleaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 1), XfSwRelease()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwReleaseIndex.setStatus('current')
xfSwReleaseProductNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 2), XfProductnumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwReleaseProductNumber.setStatus('current')
xfSwReleaseRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 3), XfProductRevision()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwReleaseRevision.setStatus('current')
xfSwReleaseAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5, 6))).clone(namedValues=NamedValues(("upgradeStarted", 1), ("upgradeAborted", 2), ("activeAndRunning", 5), ("upgradeTest", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwReleaseAdminStatus.setStatus('current')
xfSwReleaseOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 50, 51, 52, 53, 54, 55, 56, 57, 58, 421, 425, 426, 450, 451, 452, 501, 502, 503, 504, 530, 532, 550, 552, 553))).clone(namedValues=NamedValues(("passive", 1), ("upgradeStarted", 2), ("upgradeFinished", 3), ("testing", 4), ("upgradeFailed", 5), ("upgradeAborted", 6), ("running", 7), ("testingFromManual", 8), ("errorInternal", 50), ("errorFileStorage", 51), ("ftpPingFailed", 52), ("ftpNoAccess", 53), ("ftpConnectionDetailsMissing", 54), ("ftpConnectionDetailsInvalid", 55), ("ftpConnectionTimeout", 56), ("ftpNoSuchRemoteFile", 57), ("ftpNoSuchRemoteDir", 58), ("ftpServiceNotAvailable", 421), ("ftpUnableToOpenDataConnection", 425), ("ftpConnectionClosed", 426), ("ftpFileBusy", 450), ("ftpLocalError", 451), ("ftpInsufficientStorageSpace", 452), ("ftpSyntaxError", 501), ("ftpCommandNotImplemented", 502), ("ftpBadSequenceCommands", 503), ("ftpParameterNotImplemented", 504), ("ftpNoLoggedIn", 530), ("ftpNeedAccount", 532), ("ftpFileUnavailable", 550), ("ftpExceededStorageAllocation", 552), ("ftpFileNameNotAllowed", 553)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwReleaseOperStatus.setStatus('current')
xfSwReleaseSBLType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("definedByEricsson", 1), ("definedByOperator", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwReleaseSBLType.setStatus('current')
xfSwActiveRelease = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 3), XfSwRelease()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwActiveRelease.setStatus('current')
xfSwBootTime = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 4), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwBootTime.setStatus('current')
xfSwCommitType = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operatorCommit", 1), ("nodeCommit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwCommitType.setStatus('current')
xfSwBoardTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6), )
if mibBuilder.loadTexts: xfSwBoardTable.setStatus('current')
xfSwBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "XF-SOFTWARE-MIB", "xfSwLoadModuleIndex"))
if mibBuilder.loadTexts: xfSwBoardEntry.setStatus('current')
xfSwBoardLoadModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardLoadModuleIndex.setStatus('current')
xfSwBoardLoadModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardLoadModuleType.setStatus('obsolete')
xfSwBoardProductNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 3), XfProductnumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardProductNumber.setStatus('current')
xfSwBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 4), XfProductRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardRevision.setStatus('current')
xfSwBoardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("active", 2), ("upgrading", 3), ("wrongSoftware", 4), ("minSoftwareRevision", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardStatus.setStatus('current')
xfSwBoardSuProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardSuProgress.setStatus('current')
xfSwBoardMinProductNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 7), XfProductnumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardMinProductNumber.setStatus('current')
xfSwBoardMinRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 8), XfProductRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardMinRevision.setStatus('current')
xfSwBoardTrafficDisturbance = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disturbing", 2), ("notDisturbing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwBoardTrafficDisturbance.setStatus('current')
xfSwNpuObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7))
xfSwNpuPassiveProductNumber = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7, 1), XfProductnumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwNpuPassiveProductNumber.setStatus('current')
xfSwNpuPassiveRevision = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7, 2), XfProductRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwNpuPassiveRevision.setStatus('current')
xfSwNpuPassiveSwitch = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("switch", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwNpuPassiveSwitch.setStatus('current')
xfSwLoadModuleTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 8))
xfDeviceProcessorSoftware = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 8, 1))
if mibBuilder.loadTexts: xfDeviceProcessorSoftware.setStatus('obsolete')
xfPciFpgaCode = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 8, 2))
if mibBuilder.loadTexts: xfPciFpgaCode.setStatus('obsolete')
xfSwUpgradePreferences = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9))
xfSwVersionControl = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 1), XfSwEnableDisable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwVersionControl.setStatus('current')
xfSwAutoUpgrade = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 2), XfSwEnableDisable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwAutoUpgrade.setStatus('current')
xfSwAutoDowngrade = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 3), XfSwEnableDisable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwAutoDowngrade.setStatus('current')
xfSwAcceptFailure = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 4), XfSwEnableDisable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwAcceptFailure.setStatus('current')
xfSwLmUpgradeTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10), )
if mibBuilder.loadTexts: xfSwLmUpgradeTable.setStatus('current')
xfSwLmUpgradeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1), ).setIndexNames((0, "XF-SOFTWARE-MIB", "xfSwLmUpgradeIndex"))
if mibBuilder.loadTexts: xfSwLmUpgradeEntry.setStatus('current')
xfSwLmUpgradeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLmUpgradeIndex.setStatus('current')
xfSwLmUpgradeProductNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 3), XfProductnumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLmUpgradeProductNumber.setStatus('current')
xfSwLmUpgradeRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 4), XfProductRevision()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwLmUpgradeRevision.setStatus('current')
xfSwLmUpgradeAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("upgradeStarted", 1), ("upgradeAborted", 2), ("activeAndRunning", 3), ("upgradeTest", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfSwLmUpgradeAdminStatus.setStatus('current')
xfSwLmUpgradeOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 50, 51, 52, 53, 54, 55, 56, 57, 58, 421, 425, 426, 450, 451, 452, 501, 502, 503, 504, 530, 532, 550, 552, 553))).clone(namedValues=NamedValues(("active", 1), ("upgradeStarted", 2), ("upgradeFinished", 3), ("upgradeTested", 4), ("upgradeFailed", 5), ("upgradeAborted", 6), ("errorInternalError", 50), ("errorFileStorage", 51), ("ftpPingFailed", 52), ("ftpNoAccess", 53), ("ftpConnectionDetailsMissing", 54), ("ftpConnectionDetailsInvalid", 55), ("ftpConnectionTimeout", 56), ("ftpNoSuchRemoteFile", 57), ("ftpNoSuchRemoteDir", 58), ("ftpServiceNotAvailable", 421), ("ftpUnableToOpenDataConnection", 425), ("ftpConnectionClosed", 426), ("ftpFileBusy", 450), ("ftpLocalError", 451), ("ftpInsufficienStorageSpace", 452), ("ftpSyntaxError", 501), ("ftpCommandNotImplemented", 502), ("ftpBadSequenceCommands", 503), ("ftpParameterNotImplemented", 504), ("ftpNotLoggedIn", 530), ("ftpNeedAccount", 532), ("ftpFileUnavailable", 550), ("ftpExceededStorageAllocation", 552), ("ftpFileNameNotAllowed", 553)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLmUpgradeOperStatus.setStatus('current')
xfSwLmUpgradeProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLmUpgradeProgress.setStatus('current')
xfSwLmUpgradeFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("downloadFailure", 1), ("programFailure", 2), ("noFailure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLmUpgradeFailure.setStatus('current')
xfSwLmUpgradeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwLmUpgradeDescription.setStatus('current')
xfSwGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 11), Bits().clone(namedValues=NamedValues(("noUpgrade", 0), ("sblStarted", 1), ("sblWaitForActivate", 2), ("sblWaitForCommit", 3), ("manualStarted", 4), ("manualWaitForActivate", 5), ("manualWaitForCommit", 6), ("unitUpgrade", 7), ("cachingLoadModules", 8), ("preparingForTest", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfSwGlobalState.setStatus('current')
xfSwConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2))
xfSwCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 1))
xfSwFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 1, 1)).setObjects(("XF-SOFTWARE-MIB", "xfSwGroup"), ("XF-SOFTWARE-MIB", "xSwGroupR2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfSwFullCompliance = xfSwFullCompliance.setStatus('current')
xfSwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2))
xfSwGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2, 1)).setObjects(("XF-SOFTWARE-MIB", "xfSwRelease"), ("XF-SOFTWARE-MIB", "xfSwLoadModuleIndex"), ("XF-SOFTWARE-MIB", "xfSwLoadModuleProductNumber"), ("XF-SOFTWARE-MIB", "xfSwLoadModuleRevision"), ("XF-SOFTWARE-MIB", "xfSwLoadModuleOperStatus"), ("XF-SOFTWARE-MIB", "xfSwReleaseIndex"), ("XF-SOFTWARE-MIB", "xfSwReleaseProductNumber"), ("XF-SOFTWARE-MIB", "xfSwReleaseRevision"), ("XF-SOFTWARE-MIB", "xfSwReleaseAdminStatus"), ("XF-SOFTWARE-MIB", "xfSwReleaseOperStatus"), ("XF-SOFTWARE-MIB", "xfSwActiveRelease"), ("XF-SOFTWARE-MIB", "xfSwBootTime"), ("XF-SOFTWARE-MIB", "xfSwCommitType"), ("XF-SOFTWARE-MIB", "xfSwBoardProductNumber"), ("XF-SOFTWARE-MIB", "xfSwBoardRevision"), ("XF-SOFTWARE-MIB", "xfSwNpuPassiveProductNumber"), ("XF-SOFTWARE-MIB", "xfSwNpuPassiveSwitch"), ("XF-SOFTWARE-MIB", "xfSwLoadModuleFailure"), ("XF-SOFTWARE-MIB", "xfSwNpuPassiveRevision"), ("XF-SOFTWARE-MIB", "xfSwBoardStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfSwGroup = xfSwGroup.setStatus('current')
xSwGroupR2 = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2, 2)).setObjects(("XF-SOFTWARE-MIB", "xfSwBoardSuProgress"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeIndex"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeProductNumber"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeRevision"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeAdminStatus"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeOperStatus"), ("XF-SOFTWARE-MIB", "xfSwBoardMinProductNumber"), ("XF-SOFTWARE-MIB", "xfSwBoardMinRevision"), ("XF-SOFTWARE-MIB", "xfSwVersionControl"), ("XF-SOFTWARE-MIB", "xfSwLoadModuleProgress"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeFailure"), ("XF-SOFTWARE-MIB", "xfSwBoardTrafficDisturbance"), ("XF-SOFTWARE-MIB", "xfSwReleaseSBLType"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeProgress"), ("XF-SOFTWARE-MIB", "xfSwAutoUpgrade"), ("XF-SOFTWARE-MIB", "xfSwAutoDowngrade"), ("XF-SOFTWARE-MIB", "xfSwGlobalState"), ("XF-SOFTWARE-MIB", "xfSwAcceptFailure"), ("XF-SOFTWARE-MIB", "xfSwLoadModuleDescription"), ("XF-SOFTWARE-MIB", "xfSwLmUpgradeDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xSwGroupR2 = xSwGroupR2.setStatus('current')
xfSwObsoleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2, 3)).setObjects(("XF-SOFTWARE-MIB", "xfSwBoardLoadModuleIndex"), ("XF-SOFTWARE-MIB", "xfSwBoardLoadModuleType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfSwObsoleteGroup = xfSwObsoleteGroup.setStatus('obsolete')
mibBuilder.exportSymbols("XF-SOFTWARE-MIB", xfSwLoadModuleTable=xfSwLoadModuleTable, xfSwNpuPassiveProductNumber=xfSwNpuPassiveProductNumber, xfSwGroup=xfSwGroup, xfPciFpgaCode=xfPciFpgaCode, xfSwLmUpgradeProductNumber=xfSwLmUpgradeProductNumber, xfSwLmUpgradeAdminStatus=xfSwLmUpgradeAdminStatus, xfDeviceProcessorSoftware=xfDeviceProcessorSoftware, xfSwLmUpgradeEntry=xfSwLmUpgradeEntry, xfSwReleaseEntry=xfSwReleaseEntry, xfSwActiveRelease=xfSwActiveRelease, xfSwReleaseIndex=xfSwReleaseIndex, xfSwReleaseTable=xfSwReleaseTable, xfSwLoadModuleOperStatus=xfSwLoadModuleOperStatus, xfSwFullCompliance=xfSwFullCompliance, XfSwEnableDisable=XfSwEnableDisable, xfSwObsoleteGroup=xfSwObsoleteGroup, xfSwAutoDowngrade=xfSwAutoDowngrade, xfSwCompliances=xfSwCompliances, xfSwReleaseAdminStatus=xfSwReleaseAdminStatus, xfSwNpuPassiveRevision=xfSwNpuPassiveRevision, xfSwNpuObjects=xfSwNpuObjects, xfSwBoardLoadModuleIndex=xfSwBoardLoadModuleIndex, xfSwLoadModuleEntry=xfSwLoadModuleEntry, xfSoftwareMIB=xfSoftwareMIB, xfSwBoardProductNumber=xfSwBoardProductNumber, xfSwNpuPassiveSwitch=xfSwNpuPassiveSwitch, xfSwAcceptFailure=xfSwAcceptFailure, xfSwBoardSuProgress=xfSwBoardSuProgress, xfSwLmUpgradeTable=xfSwLmUpgradeTable, xfSwReleaseOperStatus=xfSwReleaseOperStatus, xfSwReleaseProductNumber=xfSwReleaseProductNumber, xfSwBoardMinProductNumber=xfSwBoardMinProductNumber, xfSwLmUpgradeProgress=xfSwLmUpgradeProgress, xfSwAutoUpgrade=xfSwAutoUpgrade, xfSwLoadModuleProgress=xfSwLoadModuleProgress, xfSwUpgradePreferences=xfSwUpgradePreferences, xfSwConformance=xfSwConformance, xfSwBoardEntry=xfSwBoardEntry, xfSwBoardRevision=xfSwBoardRevision, xfSwObjects=xfSwObjects, xSwGroupR2=xSwGroupR2, xfSwLoadModuleDescription=xfSwLoadModuleDescription, xfSwLoadModuleIndex=xfSwLoadModuleIndex, xfSwLmUpgradeFailure=xfSwLmUpgradeFailure, xfSwGroups=xfSwGroups, xfSwLoadModuleProductNumber=xfSwLoadModuleProductNumber, xfSwReleaseSBLType=xfSwReleaseSBLType, xfSwBoardMinRevision=xfSwBoardMinRevision, xfSwCommitType=xfSwCommitType, xfSwBootTime=xfSwBootTime, xfSwBoardTrafficDisturbance=xfSwBoardTrafficDisturbance, xfSwLmUpgradeRevision=xfSwLmUpgradeRevision, xfSwLmUpgradeOperStatus=xfSwLmUpgradeOperStatus, PYSNMP_MODULE_ID=xfSoftwareMIB, xfSwVersionControl=xfSwVersionControl, xfSwLmUpgradeDescription=xfSwLmUpgradeDescription, xfSwBoardTable=xfSwBoardTable, xfSwLoadModuleFailure=xfSwLoadModuleFailure, xfSwLmUpgradeIndex=xfSwLmUpgradeIndex, xfSwRelease=xfSwRelease, xfSwGlobalState=xfSwGlobalState, XfSwRelease=XfSwRelease, xfSwLoadModuleTypes=xfSwLoadModuleTypes, xfSwLoadModuleRevision=xfSwLoadModuleRevision, xfSwBoardLoadModuleType=xfSwBoardLoadModuleType, xfSwReleaseRevision=xfSwReleaseRevision, xfSwBoardStatus=xfSwBoardStatus)
