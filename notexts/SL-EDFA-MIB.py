#
# PySNMP MIB module SL-EDFA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-EDFA.mib
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:39 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, MibIdentifier, Gauge32, Unsigned32, Counter32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Integer32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "MibIdentifier", "Gauge32", "Unsigned32", "Counter32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Integer32", "iso", "Counter64")
TimeStamp, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention", "TruthValue")
slEdfa = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 9))
if mibBuilder.loadTexts: slEdfa.setLastUpdated('200202040000Z')
if mibBuilder.loadTexts: slEdfa.setOrganization('PacketLight Networks Ltd.')
edfaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1))
edfaTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 9, 2))
edfaTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 0))
edfaConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1), )
if mibBuilder.loadTexts: edfaConfigTable.setStatus('current')
edfaConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1), ).setIndexNames((0, "SL-EDFA-MIB", "edfaIfIndex"))
if mibBuilder.loadTexts: edfaConfigEntry.setStatus('current')
edfaIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaIfIndex.setStatus('current')
edfaPumpTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaPumpTemp.setStatus('current')
edfaRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaRxPower.setStatus('current')
edfaPumpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("restart", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaPumpAdminStatus.setStatus('current')
edfaPumpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("restart", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaPumpOperStatus.setStatus('current')
edfaStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191))).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaStatus.setStatus('current')
edfaVoa = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaVoa.setStatus('current')
edfaAutomaticMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaAutomaticMode.setStatus('current')
edfaAdminControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("apc", 1), ("agc", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaAdminControlMode.setStatus('current')
edfaOperControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("apc", 1), ("agc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaOperControlMode.setStatus('current')
edfaAdminGain = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaAdminGain.setStatus('current')
edfaOperGain = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaOperGain.setStatus('current')
edfaAdminOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaAdminOutputPower.setStatus('current')
edfaOperOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaOperOutputPower.setStatus('current')
edfaChannelsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaChannelsNumber.setStatus('current')
edfaTotalChannelsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaTotalChannelsNumber.setStatus('current')
edfaEyeSafetyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaEyeSafetyMode.setStatus('current')
edfaShutDownLipEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaShutDownLipEnable.setStatus('current')
edfaAutoPowerUpLipEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaAutoPowerUpLipEnable.setStatus('current')
edfaMaxGain = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaMaxGain.setStatus('current')
edfaGainInFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaGainInFrom.setStatus('current')
edfaGainInTo = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaGainInTo.setStatus('current')
edfaGainOutFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaGainOutFrom.setStatus('current')
edfaGainOutTo = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaGainOutTo.setStatus('current')
edfaPowerInFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaPowerInFrom.setStatus('current')
edfaPowerInTo = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaPowerInTo.setStatus('current')
edfaPowerOutFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaPowerOutFrom.setStatus('current')
edfaPowerOutTo = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaPowerOutTo.setStatus('current')
edfaFromChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaFromChannel.setStatus('current')
edfaToChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaToChannel.setStatus('current')
edfaOscChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaOscChannel.setStatus('current')
edfaRedBlueType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("red", 1), ("blue", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaRedBlueType.setStatus('current')
edfaRole = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("booster", 1), ("boosterInline", 2), ("preamp", 3), ("inline", 4), ("raman", 5), ("other", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaRole.setStatus('current')
edfaFreeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 34), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: edfaFreeDescription.setStatus('current')
edfaConfigSafetyThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 35), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: edfaConfigSafetyThreshold.setStatus('current')
edfaStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 1)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaStatus"))
if mibBuilder.loadTexts: edfaStatusChange.setStatus('current')
edfaControlModeChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 2)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaOperControlMode"))
if mibBuilder.loadTexts: edfaControlModeChange.setStatus('current')
edfaStatusChange0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 0, 1)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaStatus"))
if mibBuilder.loadTexts: edfaStatusChange0.setStatus('current')
edfaControlModeChange0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 0, 2)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaOperControlMode"))
if mibBuilder.loadTexts: edfaControlModeChange0.setStatus('current')
mibBuilder.exportSymbols("SL-EDFA-MIB", edfaChannelsNumber=edfaChannelsNumber, PYSNMP_MODULE_ID=slEdfa, edfaConfigTable=edfaConfigTable, edfaEyeSafetyMode=edfaEyeSafetyMode, edfaIfIndex=edfaIfIndex, edfaPumpAdminStatus=edfaPumpAdminStatus, edfaMaxGain=edfaMaxGain, edfaGainOutFrom=edfaGainOutFrom, edfaOscChannel=edfaOscChannel, edfaRxPower=edfaRxPower, edfaFreeDescription=edfaFreeDescription, edfaConfigSafetyThreshold=edfaConfigSafetyThreshold, edfaPumpOperStatus=edfaPumpOperStatus, edfaPowerInFrom=edfaPowerInFrom, edfaPowerOutFrom=edfaPowerOutFrom, edfaTraps=edfaTraps, edfaStatus=edfaStatus, edfaToChannel=edfaToChannel, edfaPumpTemp=edfaPumpTemp, edfaOperOutputPower=edfaOperOutputPower, edfaTotalChannelsNumber=edfaTotalChannelsNumber, edfaOperGain=edfaOperGain, edfaConfig=edfaConfig, edfaFromChannel=edfaFromChannel, edfaOperControlMode=edfaOperControlMode, edfaControlModeChange=edfaControlModeChange, edfaAutomaticMode=edfaAutomaticMode, edfaStatusChange=edfaStatusChange, edfaRole=edfaRole, edfaShutDownLipEnable=edfaShutDownLipEnable, edfaPowerOutTo=edfaPowerOutTo, edfaAutoPowerUpLipEnable=edfaAutoPowerUpLipEnable, edfaPowerInTo=edfaPowerInTo, edfaAdminGain=edfaAdminGain, edfaControlModeChange0=edfaControlModeChange0, edfaAdminOutputPower=edfaAdminOutputPower, edfaVoa=edfaVoa, edfaGainOutTo=edfaGainOutTo, edfaGainInTo=edfaGainInTo, edfaStatusChange0=edfaStatusChange0, edfaGainInFrom=edfaGainInFrom, edfaConfigEntry=edfaConfigEntry, edfaRedBlueType=edfaRedBlueType, edfaTraps0=edfaTraps0, slEdfa=slEdfa, edfaAdminControlMode=edfaAdminControlMode)
