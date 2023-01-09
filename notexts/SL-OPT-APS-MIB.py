#
# PySNMP MIB module SL-OPT-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-OPT-APS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:39 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
slmTrapLogId, = mibBuilder.importSymbols("SL-MAIN-MIB", "slmTrapLogId")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, MibIdentifier, Gauge32, Unsigned32, Counter32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Opaque, Integer32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "MibIdentifier", "Gauge32", "Unsigned32", "Counter32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Opaque", "Integer32", "iso", "Counter64")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
slOptApsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 11))
if mibBuilder.loadTexts: slOptApsMib.setLastUpdated('200201140000Z')
if mibBuilder.loadTexts: slOptApsMib.setOrganization('PacketLight Networks Ltd.')
slOptApsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1))
slOptApsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2))
slOptApsTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0))
optApsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1), )
if mibBuilder.loadTexts: optApsConfigTable.setStatus('current')
optApsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1), ).setIndexNames((0, "SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"))
if mibBuilder.loadTexts: optApsConfigEntry.setStatus('current')
optApsConfigUserWorkingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigUserWorkingIndex.setStatus('current')
optApsConfigNetWorkingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigNetWorkingIndex.setStatus('current')
optApsConfigUserProtectingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigUserProtectingIndex.setStatus('current')
optApsConfigNetProtectingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigNetProtectingIndex.setStatus('current')
optApsConfigScheme = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equipment", 1), ("facility", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigScheme.setStatus('current')
optApsConfigEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("optApsDisabled", 1), ("optApsEnabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigEnable.setStatus('current')
optApsConfigArchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onePlusOne", 1), ("oneToOne", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigArchMode.setStatus('current')
optApsConfigActiveConnectionRx = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("optApsWorkingConnection", 1), ("optApsProtectionConnection", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigActiveConnectionRx.setStatus('current')
optApsConfigActiveConnectionTx = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("optApsWorkingConnection", 1), ("optApsProtectionConnection", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigActiveConnectionTx.setStatus('current')
optApsConfigWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigWaitToRestore.setStatus('current')
optApsConfigDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uniDirectional", 1), ("biDirectional", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigDirection.setStatus('current')
optApsConfigRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonrevertive", 1), ("revertive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigRevertive.setStatus('current')
optApsConfigChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 13), Bits().clone(namedValues=NamedValues(("lockedOut", 0), ("sfWorking", 1), ("sfProtecting", 2), ("switched", 3), ("lockedOutRemote", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanStatus.setStatus('current')
optApsConfigChanSignalFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanSignalFailures.setStatus('current')
optApsConfigChanSwitchovers = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanSwitchovers.setStatus('current')
optApsConfigChanLastSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanLastSwitchover.setStatus('current')
optApsConfigSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("clear", 1), ("lockoutOfProtection", 2), ("forcedSwitchOfWorking", 3), ("forcedSwitchOfProtection", 4), ("manualSwitchOfWorking", 5), ("manualSwitchOfProtection", 6))).clone('clear')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigSwitchCommand.setStatus('current')
optApsConfigSwitchReason = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("optApsOther", 1), ("optApsRevertive", 2), ("optApsManual", 3), ("optApsSignalFailure", 4), ("optApsForceSwitch", 5), ("optApsLockOut", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigSwitchReason.setStatus('current')
optApsConfigResetCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigResetCounters.setStatus('current')
optApsConfigActiveRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("optApsOther", 1), ("optApsRevertive", 2), ("optApsManual", 3), ("optApsSignalFailure", 4), ("optApsForceSwitch", 5), ("optApsLockOut", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigActiveRequest.setStatus('current')
optApsConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 21), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigStatus.setStatus('current')
optApsConfigLosThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optApsConfigLosThreshold.setStatus('current')
eqptApsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2), )
if mibBuilder.loadTexts: eqptApsConfigTable.setStatus('current')
eqptApsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1), ).setIndexNames((0, "SL-OPT-APS-MIB", "eqptApsConfigDummyIndex"))
if mibBuilder.loadTexts: eqptApsConfigEntry.setStatus('current')
eqptApsConfigDummyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqptApsConfigDummyIndex.setStatus('current')
eqptApsConfigRole = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eqptApsWorkingRole", 1), ("eqptApsProtectionRole", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqptApsConfigRole.setStatus('current')
eqptApsConfigMate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqptApsConfigMate.setStatus('current')
eqptApsConfigLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eqptApsLinkUp", 1), ("eqptApsLinkDown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqptApsConfigLinkStatus.setStatus('current')
optApsTrapSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 1)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
if mibBuilder.loadTexts: optApsTrapSwitchover.setStatus('current')
optApsConfigTableChanged = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 2)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"))
if mibBuilder.loadTexts: optApsConfigTableChanged.setStatus('current')
optApsTrapSwitchover0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0, 1)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"), ("SL-MAIN-MIB", "slmTrapLogId"))
if mibBuilder.loadTexts: optApsTrapSwitchover0.setStatus('current')
optApsConfigTableChanged0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0, 2)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"), ("SL-MAIN-MIB", "slmTrapLogId"))
if mibBuilder.loadTexts: optApsConfigTableChanged0.setStatus('current')
mibBuilder.exportSymbols("SL-OPT-APS-MIB", optApsConfigResetCounters=optApsConfigResetCounters, optApsConfigTableChanged=optApsConfigTableChanged, eqptApsConfigMate=eqptApsConfigMate, optApsConfigRevertive=optApsConfigRevertive, optApsConfigActiveConnectionRx=optApsConfigActiveConnectionRx, optApsConfigActiveRequest=optApsConfigActiveRequest, optApsConfigTable=optApsConfigTable, slOptApsTraps=slOptApsTraps, optApsConfigStatus=optApsConfigStatus, optApsConfigScheme=optApsConfigScheme, optApsConfigEntry=optApsConfigEntry, optApsConfigNetWorkingIndex=optApsConfigNetWorkingIndex, optApsConfigSwitchCommand=optApsConfigSwitchCommand, eqptApsConfigLinkStatus=eqptApsConfigLinkStatus, optApsConfigDirection=optApsConfigDirection, slOptApsConfig=slOptApsConfig, optApsConfigUserProtectingIndex=optApsConfigUserProtectingIndex, optApsConfigChanLastSwitchover=optApsConfigChanLastSwitchover, optApsConfigTableChanged0=optApsConfigTableChanged0, eqptApsConfigTable=eqptApsConfigTable, optApsTrapSwitchover0=optApsTrapSwitchover0, optApsConfigChanStatus=optApsConfigChanStatus, eqptApsConfigEntry=eqptApsConfigEntry, optApsConfigNetProtectingIndex=optApsConfigNetProtectingIndex, optApsConfigLosThreshold=optApsConfigLosThreshold, slOptApsTraps0=slOptApsTraps0, eqptApsConfigDummyIndex=eqptApsConfigDummyIndex, optApsTrapSwitchover=optApsTrapSwitchover, optApsConfigChanSignalFailures=optApsConfigChanSignalFailures, optApsConfigSwitchReason=optApsConfigSwitchReason, optApsConfigArchMode=optApsConfigArchMode, optApsConfigActiveConnectionTx=optApsConfigActiveConnectionTx, optApsConfigChanSwitchovers=optApsConfigChanSwitchovers, slOptApsMib=slOptApsMib, PYSNMP_MODULE_ID=slOptApsMib, optApsConfigEnable=optApsConfigEnable, eqptApsConfigRole=eqptApsConfigRole, optApsConfigUserWorkingIndex=optApsConfigUserWorkingIndex, optApsConfigWaitToRestore=optApsConfigWaitToRestore)
