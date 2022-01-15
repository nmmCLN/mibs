#
# PySNMP MIB module BKTEL-HFC862-HMSNE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-HMSNE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:10:06 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
DisplayString, PerceivedSeverityValue, ne, TruthValue, NESlotValue = mibBuilder.importSymbols("BKTEL-HFC862-BASE-MIB", "DisplayString", "PerceivedSeverityValue", "ne", "TruthValue", "NESlotValue")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, iso, ModuleIdentity, Integer32, NotificationType, Gauge32, Bits, MibIdentifier, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "iso", "ModuleIdentity", "Integer32", "NotificationType", "Gauge32", "Bits", "MibIdentifier", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
neCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1))
neType = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neType.setStatus('mandatory')
neDescription = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neDescription.setStatus('mandatory')
neLocationStreet = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neLocationStreet.setStatus('mandatory')
neLocationCity = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neLocationCity.setStatus('mandatory')
neObsolete_UsingAPS = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_UsingAPS.setStatus('obsolete')
neObsolete_APSMode = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_APSMode.setStatus('obsolete')
neObsolete_CommonSubrackWidth = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_CommonSubrackWidth.setStatus('obsolete')
neObsolete_CommonSubrackNumber = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_CommonSubrackNumber.setStatus('obsolete')
neObsolete_NumberModul = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 61))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_NumberModul.setStatus('obsolete')
neObsolete_UsingRevertiveMode = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_UsingRevertiveMode.setStatus('obsolete')
neObsolete_RevertiveMode = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_RevertiveMode.setStatus('obsolete')
neObsolete_InitPhase = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_InitPhase.setStatus('obsolete')
neObsolete_PredecessorRedundantPath = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_PredecessorRedundantPath.setStatus('obsolete')
neObsolete_PredecessorNominalPath = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_PredecessorNominalPath.setStatus('obsolete')
neModuleTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16), )
if mibBuilder.loadTexts: neModuleTable.setStatus('mandatory')
neModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1), ).setIndexNames((0, "BKTEL-HFC862-HMSNE-MIB", "neModuleNESlot"))
if mibBuilder.loadTexts: neModuleEntry.setStatus('mandatory')
neModuleNESlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 1), NESlotValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleNESlot.setStatus('mandatory')
neModuleSubrack = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSubrack.setStatus('mandatory')
neModuleModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleModelName.setStatus('mandatory')
neModuleMibLink = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleMibLink.setStatus('mandatory')
neModuleSubrackSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSubrackSlot.setStatus('mandatory')
neModuleSlotUnitsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSlotUnitsUsed.setStatus('mandatory')
neModuleSlotRackDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2), ("detectionError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSlotRackDetection.setStatus('mandatory')
neModuleHousingType = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("housingUnknownOrDefault", 1), ("housingBk", 2), ("housing2G6", 3), ("housing19inch", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleHousingType.setStatus('mandatory')
neModuleFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleFirmwareVersion.setStatus('mandatory')
neModuleHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleHardwareVersion.setStatus('mandatory')
neModuleDateOfProduction = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleDateOfProduction.setStatus('mandatory')
neModuleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSerialNumber.setStatus('mandatory')
neModuleArticleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleArticleNumber.setStatus('mandatory')
neModuleCustomerCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleCustomerCode.setStatus('mandatory')
neModuleAliasName = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleAliasName.setStatus('mandatory')
neModuleUserdata = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleUserdata.setStatus('mandatory')
neModuleReset = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleReset.setStatus('mandatory')
neModuleLedBlink = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleLedBlink.setStatus('mandatory')
neStates = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2))
neStatesObsolete_TrapDisable = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 1), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_TrapDisable.setStatus('obsolete')
neStatesObsolete_TerminalConnected = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 2), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_TerminalConnected.setStatus('obsolete')
neStatesObsolete_Isolated = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 4), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_Isolated.setStatus('obsolete')
neStatesObsolete_ResetModullist = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 5), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_ResetModullist.setStatus('obsolete')
neStatesObsolete_Redundant = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 6), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_Redundant.setStatus('obsolete')
neStatesObsolete_ActivateRedundantPath = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 7), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_ActivateRedundantPath.setStatus('obsolete')
neStatesObsolete_AutoOff = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 8), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_AutoOff.setStatus('obsolete')
neConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3))
neConfigObsolete_NEtype = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigObsolete_NEtype.setStatus('obsolete')
neConfigObsolete_IPaddress = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigObsolete_IPaddress.setStatus('obsolete')
neConfigObsolete_Alarmdelay = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigObsolete_Alarmdelay.setStatus('obsolete')
neConfigDeprecated_MinTrapInterval = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigDeprecated_MinTrapInterval.setStatus('optional')
neConfigDeprecated_MaxTrapLifetime = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigDeprecated_MaxTrapLifetime.setStatus('optional')
neControl = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4))
neControlTrapDisable = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neControlTrapDisable.setStatus('mandatory')
neControlResetModullist = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neControlResetModullist.setStatus('mandatory')
neControlObsolete_SetDefaultAPS = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neControlObsolete_SetDefaultAPS.setStatus('obsolete')
neSynchronizeEvent = NotificationType((1, 3, 6, 1, 4, 1, 7501, 1, 1) + (0,1))
mibBuilder.exportSymbols("BKTEL-HFC862-HMSNE-MIB", neStatesObsolete_ActivateRedundantPath=neStatesObsolete_ActivateRedundantPath, neModuleReset=neModuleReset, neModuleMibLink=neModuleMibLink, neObsolete_CommonSubrackNumber=neObsolete_CommonSubrackNumber, neModuleSubrackSlot=neModuleSubrackSlot, neStatesObsolete_ResetModullist=neStatesObsolete_ResetModullist, neStatesObsolete_Isolated=neStatesObsolete_Isolated, neConfigObsolete_Alarmdelay=neConfigObsolete_Alarmdelay, neConfig=neConfig, neType=neType, neModuleDateOfProduction=neModuleDateOfProduction, neControlResetModullist=neControlResetModullist, neModuleTable=neModuleTable, neObsolete_CommonSubrackWidth=neObsolete_CommonSubrackWidth, neConfigObsolete_IPaddress=neConfigObsolete_IPaddress, neModuleHousingType=neModuleHousingType, neModuleSlotUnitsUsed=neModuleSlotUnitsUsed, neSynchronizeEvent=neSynchronizeEvent, neObsolete_RevertiveMode=neObsolete_RevertiveMode, neModuleNESlot=neModuleNESlot, neModuleAliasName=neModuleAliasName, neStatesObsolete_Redundant=neStatesObsolete_Redundant, neObsolete_PredecessorNominalPath=neObsolete_PredecessorNominalPath, neModuleFirmwareVersion=neModuleFirmwareVersion, neLocationStreet=neLocationStreet, neStatesObsolete_TrapDisable=neStatesObsolete_TrapDisable, neLocationCity=neLocationCity, neModuleHardwareVersion=neModuleHardwareVersion, neConfigDeprecated_MinTrapInterval=neConfigDeprecated_MinTrapInterval, neObsolete_PredecessorRedundantPath=neObsolete_PredecessorRedundantPath, neModuleArticleNumber=neModuleArticleNumber, neModuleModelName=neModuleModelName, neConfigObsolete_NEtype=neConfigObsolete_NEtype, neModuleSlotRackDetection=neModuleSlotRackDetection, neStatesObsolete_AutoOff=neStatesObsolete_AutoOff, neControlObsolete_SetDefaultAPS=neControlObsolete_SetDefaultAPS, neModuleUserdata=neModuleUserdata, neObsolete_NumberModul=neObsolete_NumberModul, neObsolete_UsingRevertiveMode=neObsolete_UsingRevertiveMode, neControl=neControl, neStates=neStates, neStatesObsolete_TerminalConnected=neStatesObsolete_TerminalConnected, neCommon=neCommon, neConfigDeprecated_MaxTrapLifetime=neConfigDeprecated_MaxTrapLifetime, neControlTrapDisable=neControlTrapDisable, neDescription=neDescription, neModuleSerialNumber=neModuleSerialNumber, neObsolete_UsingAPS=neObsolete_UsingAPS, neModuleCustomerCode=neModuleCustomerCode, neModuleLedBlink=neModuleLedBlink, neObsolete_APSMode=neObsolete_APSMode, neModuleEntry=neModuleEntry, neModuleSubrack=neModuleSubrack, neObsolete_InitPhase=neObsolete_InitPhase)
