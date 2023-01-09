#
# PySNMP MIB module AH-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-TRAP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:28 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
AhMACProtocol, AhNodeID, AhString, ahAPTrap = mibBuilder.importSymbols("AH-SMI-MIB", "AhMACProtocol", "AhNodeID", "AhString", "ahAPTrap")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Gauge32, MibIdentifier, IpAddress, Integer32, Counter32, TimeTicks, ObjectIdentity, Bits, ModuleIdentity, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TruthValue = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Gauge32", "MibIdentifier", "IpAddress", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity", "Bits", "ModuleIdentity", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TruthValue")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class AhAuthenticationMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11))
    namedValues = NamedValues(("cwp", 0), ("open", 1), ("wep-open", 2), ("wep-shared", 3), ("wpa-psk", 4), ("wpa2-psk", 5), ("wpa-8021x", 6), ("wpa2-8021X", 7), ("wpa-auto-psk", 8), ("dynamic-wep", 10), ("x8021x", 11))

class AhEncrytionMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("aes", 0), ("tkip", 1), ("wep", 2), ("non", 3))

ahTrapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1))
if mibBuilder.loadTexts: ahTrapModule.setLastUpdated('200612140000Z')
if mibBuilder.loadTexts: ahTrapModule.setOrganization('Aerohive Networks, Inc.')
ahNotificationVarBind = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2))
class AhState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ahUp", 1), ("ahDown", 2))

class AhProbableCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("ahClear", 0), ("ahUnknown", 1), ("ahFlashFailure", 2), ("ahFanFailure", 3), ("ahPowerSupplyFailure", 4), ("ahSoftwareUpgradeFailure", 5), ("ahRadioFailure", 6), ("ahConfFailure", 7))

ahFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 1)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahSeverity"), ("AH-TRAP-MIB", "ahProbableCause"), ("AH-TRAP-MIB", "ahFailureSet"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahFailureTrap.setStatus('current')
ahThresholdCrossingEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 2)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahCurValue"), ("AH-TRAP-MIB", "ahThresholdHigh"), ("AH-TRAP-MIB", "ahThresholdLow"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahThresholdCrossingEvent.setStatus('current')
ahStateChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 3)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahPreviousState"), ("AH-TRAP-MIB", "ahCurrentState"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahStateChangeEvent.setStatus('current')
ahConnectionChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 4)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahIfIndex"), ("AH-TRAP-MIB", "ahObjectType"), ("AH-TRAP-MIB", "ahRemoteId"), ("AH-TRAP-MIB", "ahCurrentState"), ("AH-TRAP-MIB", "ahSSID"), ("AH-TRAP-MIB", "ahCLientIP"), ("AH-TRAP-MIB", "ahClientHostName"), ("AH-TRAP-MIB", "ahClientUserName"), ("AH-TRAP-MIB", "ahClientAuthMethod"), ("AH-TRAP-MIB", "ahClientEncryptionMethod"), ("AH-TRAP-MIB", "ahClientMACProtocol"), ("AH-TRAP-MIB", "ahClientVLAN"), ("AH-TRAP-MIB", "ahClientUserProfId"), ("AH-TRAP-MIB", "ahClientChannel"), ("AH-TRAP-MIB", "ahClientCWPUsed"), ("AH-TRAP-MIB", "ahBSSID"), ("AH-TRAP-MIB", "ahAssociationTime"), ("AH-TRAP-MIB", "ahIfName"), ("AH-TRAP-MIB", "ahIDPRSSI"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahConnectionChangeEvent.setStatus('current')
ahIDPStationEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 5)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahIfIndex"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahStationType"), ("AH-TRAP-MIB", "ahRemoteId"), ("AH-TRAP-MIB", "ahIDPType"), ("AH-TRAP-MIB", "ahIDPChannel"), ("AH-TRAP-MIB", "ahIDPRSSI"), ("AH-TRAP-MIB", "ahIDPStationData"), ("AH-TRAP-MIB", "ahIDPCompliance"), ("AH-TRAP-MIB", "ahSSID"), ("AH-TRAP-MIB", "ahRemoved"), ("AH-TRAP-MIB", "ahIDPInNet"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahIDPStationEvent.setStatus('current')
ahClientInfoEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 6)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahSSID"), ("AH-TRAP-MIB", "ahClientMAC"), ("AH-TRAP-MIB", "ahCLientIP"), ("AH-TRAP-MIB", "ahClientHostName"), ("AH-TRAP-MIB", "ahClientUserName"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahClientInfoEvent.setStatus('current')
ahPoEEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 7)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahPowerSrc"), ("AH-TRAP-MIB", "ahPoEEth0On"), ("AH-TRAP-MIB", "ahPoEEth0Pwr"), ("AH-TRAP-MIB", "ahPoEEth0MaxSpeed"), ("AH-TRAP-MIB", "ahPoEWifi0Setting"), ("AH-TRAP-MIB", "ahPoEEth1On"), ("AH-TRAP-MIB", "ahPoEEth1Pwr"), ("AH-TRAP-MIB", "ahPoEEth1MaxSpeed"), ("AH-TRAP-MIB", "ahPoEWifi1Setting"), ("AH-TRAP-MIB", "ahPoEWifi2Setting"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahPoEEvent.setStatus('current')
ahChannelPowerChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 8)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahIfIndex"), ("AH-TRAP-MIB", "ahRadioChannel"), ("AH-TRAP-MIB", "ahRadioTxPower"), ("AH-TRAP-MIB", "ahBeaconInterval"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahChannelPowerChangeEvent.setStatus('current')
ahIDPMitigateEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 9)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahIfIndex"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahRemoteId"), ("AH-TRAP-MIB", "ahBSSID"), ("AH-TRAP-MIB", "ahDiscoverAge"), ("AH-TRAP-MIB", "ahUpdateAge"), ("AH-TRAP-MIB", "ahRemoved"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahIDPMitigateEvent.setStatus('current')
ahInterferenceMapAlertEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 10)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahIfIndex"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahInterferenceThreshold"), ("AH-TRAP-MIB", "ahRunningAverageInterference"), ("AH-TRAP-MIB", "ahShortTermInterference"), ("AH-TRAP-MIB", "ahSnapshotInterference"), ("AH-TRAP-MIB", "ahCRCErrRateThreshold"), ("AH-TRAP-MIB", "ahCRCErrRate"), ("AH-TRAP-MIB", "ahSeverity"), ("AH-TRAP-MIB", "ahFailureSet"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahInterferenceMapAlertEvent.setStatus('current')
ahBandwidthSentinelEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 11)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahIfIndex"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahClientMAC"), ("AH-TRAP-MIB", "ahBandwidthSentinelStatus"), ("AH-TRAP-MIB", "ahGuaranteedBandwidth"), ("AH-TRAP-MIB", "ahActualBandwidth"), ("AH-TRAP-MIB", "ahBandwidthSentinelAction"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahBandwidthSentinelEvent.setStatus('current')
ahAlarmMsgMapAlertEvent = NotificationType((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 12)).setObjects(("AH-TRAP-MIB", "ahAPId"), ("AH-TRAP-MIB", "ahAPName"), ("AH-TRAP-MIB", "ahIfIndex"), ("AH-TRAP-MIB", "ahObjectName"), ("AH-TRAP-MIB", "ahLevel"), ("AH-TRAP-MIB", "ahClientMAC"), ("AH-TRAP-MIB", "ahSSID"), ("AH-TRAP-MIB", "ahAlarmAlertType"), ("AH-TRAP-MIB", "ahThresholdValue"), ("AH-TRAP-MIB", "ahShortTermValue"), ("AH-TRAP-MIB", "ahSnapshotValue"), ("AH-TRAP-MIB", "ahFailureSet"), ("AH-TRAP-MIB", "ahCode"), ("AH-TRAP-MIB", "ahTrapDesc"))
if mibBuilder.loadTexts: ahAlarmMsgMapAlertEvent.setStatus('current')
ahAPId = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 1), AhNodeID())
if mibBuilder.loadTexts: ahAPId.setStatus('current')
ahAPName = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 2), AhString())
if mibBuilder.loadTexts: ahAPName.setStatus('current')
ahSeverity = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 4, 3, 2, 1))).clone(namedValues=NamedValues(("critical", 5), ("major", 4), ("minor", 3), ("info", 2), ("undetermined", 1))))
if mibBuilder.loadTexts: ahSeverity.setStatus('current')
ahObjectName = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: ahObjectName.setStatus('current')
ahProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 5), AhProbableCause())
if mibBuilder.loadTexts: ahProbableCause.setStatus('current')
ahCurValue = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 6), Integer32())
if mibBuilder.loadTexts: ahCurValue.setStatus('current')
ahThresholdHigh = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 7), Integer32())
if mibBuilder.loadTexts: ahThresholdHigh.setStatus('current')
ahThresholdLow = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 8), Integer32())
if mibBuilder.loadTexts: ahThresholdLow.setStatus('current')
ahPreviousState = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 9), AhState())
if mibBuilder.loadTexts: ahPreviousState.setStatus('current')
ahCurrentState = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 10), AhState())
if mibBuilder.loadTexts: ahCurrentState.setStatus('current')
ahTrapDesc = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 11), DisplayString())
if mibBuilder.loadTexts: ahTrapDesc.setStatus('current')
ahCode = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 12), Integer32())
if mibBuilder.loadTexts: ahCode.setStatus('current')
ahIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 13), Integer32())
if mibBuilder.loadTexts: ahIfIndex.setStatus('current')
ahObjectType = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clientLink", 1), ("neighborLink", 2))))
if mibBuilder.loadTexts: ahObjectType.setStatus('current')
ahRemoteId = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 15), AhNodeID())
if mibBuilder.loadTexts: ahRemoteId.setStatus('current')
ahIDPType = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rogue", 1), ("valid", 2), ("external", 3))))
if mibBuilder.loadTexts: ahIDPType.setStatus('current')
ahIDPChannel = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 17), Integer32())
if mibBuilder.loadTexts: ahIDPChannel.setStatus('current')
ahIDPRSSI = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 18), Integer32())
if mibBuilder.loadTexts: ahIDPRSSI.setStatus('current')
ahIDPCompliance = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64, 128, 256))).clone(namedValues=NamedValues(("open-policy", 1), ("wep-policy", 2), ("wpa-policy", 4), ("wmm-policy", 8), ("oui-policy", 16), ("ssid-policy", 32), ("short-preamble-policy", 64), ("short-beacon-policy", 128), ("ad-hoc-policy", 256))))
if mibBuilder.loadTexts: ahIDPCompliance.setStatus('current')
ahSSID = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: ahSSID.setStatus('current')
ahStationType = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("station-ap", 1), ("station-client", 2))))
if mibBuilder.loadTexts: ahStationType.setStatus('current')
ahIDPStationData = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 64, 128, 256))).clone(namedValues=NamedValues(("open-policy", 1), ("wep-policy", 2), ("wpa-policy", 4), ("wmm-policy", 8), ("short-preamble-policy", 64), ("short-beacon-policy", 128), ("ad-hoc-policy", 256))))
if mibBuilder.loadTexts: ahIDPStationData.setStatus('current')
ahRemoved = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("removed-false", 0), ("removed-true", 1))))
if mibBuilder.loadTexts: ahRemoved.setStatus('current')
ahClientMAC = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 24), AhNodeID())
if mibBuilder.loadTexts: ahClientMAC.setStatus('current')
ahCLientIP = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 25), DisplayString())
if mibBuilder.loadTexts: ahCLientIP.setStatus('current')
ahClientHostName = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 26), DisplayString())
if mibBuilder.loadTexts: ahClientHostName.setStatus('current')
ahClientUserName = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 27), DisplayString())
if mibBuilder.loadTexts: ahClientUserName.setStatus('current')
ahPowerSrc = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("adaptor", 0), ("poe", 1))))
if mibBuilder.loadTexts: ahPowerSrc.setStatus('current')
ahPoEEth0On = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 29), TruthValue())
if mibBuilder.loadTexts: ahPoEEth0On.setStatus('current')
ahPoEEth0Pwr = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 30), Integer32())
if mibBuilder.loadTexts: ahPoEEth0Pwr.setStatus('current')
ahPoEEth1On = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 31), TruthValue())
if mibBuilder.loadTexts: ahPoEEth1On.setStatus('current')
ahPoEEth1Pwr = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 32), Integer32())
if mibBuilder.loadTexts: ahPoEEth1Pwr.setStatus('current')
ahRadioChannel = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioChannel.setStatus('current')
ahRadioTxPower = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxPower.setStatus('current')
ahClientAuthMethod = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 35), AhAuthenticationMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientAuthMethod.setStatus('current')
ahClientEncryptionMethod = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 36), AhEncrytionMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientEncryptionMethod.setStatus('current')
ahClientMACProtocol = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 37), AhMACProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientMACProtocol.setStatus('current')
ahClientVLAN = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientVLAN.setStatus('current')
ahClientUserProfId = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientUserProfId.setStatus('current')
ahClientChannel = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientChannel.setStatus('current')
ahClientCWPUsed = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 41), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientCWPUsed.setStatus('current')
ahBSSID = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 42), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahBSSID.setStatus('current')
ahPoEEth0MaxSpeed = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("linkdown", 1), ("eth10", 2), ("eth100", 3), ("eth1000", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahPoEEth0MaxSpeed.setStatus('current')
ahPoEEth1MaxSpeed = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("linkdown", 1), ("eth10", 2), ("eth100", 3), ("eth1000", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahPoEEth1MaxSpeed.setStatus('current')
ahPoEWifi0Setting = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("invalid", 0), ("linkdown", 1), ("config", 2), ("tx2rx3", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahPoEWifi0Setting.setStatus('current')
ahPoEWifi1Setting = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 46), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("invalid", 0), ("linkdown", 1), ("config", 2), ("tx2rx3", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahPoEWifi1Setting.setStatus('current')
ahPoEWifi2Setting = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 47), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("invalid", 0), ("linkdown", 1), ("config", 2), ("tx2rx3", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahPoEWifi2Setting.setStatus('current')
ahAssociationTime = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahAssociationTime.setStatus('current')
ahIDPInNet = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 49), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIDPInNet.setStatus('current')
ahDiscoverAge = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahDiscoverAge.setStatus('current')
ahUpdateAge = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahUpdateAge.setStatus('current')
ahRunningAverageInterference = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRunningAverageInterference.setStatus('current')
ahShortTermInterference = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahShortTermInterference.setStatus('current')
ahSnapshotInterference = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSnapshotInterference.setStatus('current')
ahFailureSet = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 55), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahFailureSet.setStatus('current')
ahInterferenceThreshold = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahInterferenceThreshold.setStatus('current')
ahCRCErrRateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahCRCErrRateThreshold.setStatus('current')
ahCRCErrRate = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahCRCErrRate.setStatus('current')
ahBandwidthSentinelStatus = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 59), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("alert", 0), ("clear", 1), ("bad", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahBandwidthSentinelStatus.setStatus('current')
ahGuaranteedBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 60), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahGuaranteedBandwidth.setStatus('current')
ahActualBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 61), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahActualBandwidth.setStatus('current')
ahBandwidthSentinelAction = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahBandwidthSentinelAction.setStatus('current')
ahBeaconInterval = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahBeaconInterval.setStatus('current')
ahLevel = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 64), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("interface", 1), ("client", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahLevel.setStatus('current')
ahAlarmAlertType = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 65), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("crcrate", 0), ("txdroprate", 1), ("txretryrate", 2), ("rxdroprate", 3), ("airtime", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahAlarmAlertType.setStatus('current')
ahThresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 66), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahThresholdValue.setStatus('current')
ahShortTermValue = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 67), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahShortTermValue.setStatus('current')
ahSnapshotValue = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 68), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSnapshotValue.setStatus('current')
ahIfName = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 69), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfName.setStatus('current')
mibBuilder.exportSymbols("AH-TRAP-MIB", ahIDPStationEvent=ahIDPStationEvent, ahNotificationVarBind=ahNotificationVarBind, ahPoEWifi2Setting=ahPoEWifi2Setting, ahShortTermInterference=ahShortTermInterference, ahAPId=ahAPId, ahAssociationTime=ahAssociationTime, ahThresholdCrossingEvent=ahThresholdCrossingEvent, ahClientInfoEvent=ahClientInfoEvent, ahConnectionChangeEvent=ahConnectionChangeEvent, AhEncrytionMethod=AhEncrytionMethod, ahIDPRSSI=ahIDPRSSI, ahCLientIP=ahCLientIP, ahPoEWifi1Setting=ahPoEWifi1Setting, ahAPName=ahAPName, ahIDPCompliance=ahIDPCompliance, ahRemoteId=ahRemoteId, ahIfName=ahIfName, ahRunningAverageInterference=ahRunningAverageInterference, ahPoEEvent=ahPoEEvent, ahClientHostName=ahClientHostName, ahIDPInNet=ahIDPInNet, ahClientEncryptionMethod=ahClientEncryptionMethod, ahFailureTrap=ahFailureTrap, ahShortTermValue=ahShortTermValue, ahClientVLAN=ahClientVLAN, ahIDPMitigateEvent=ahIDPMitigateEvent, ahClientUserName=ahClientUserName, ahSSID=ahSSID, ahStationType=ahStationType, ahPoEWifi0Setting=ahPoEWifi0Setting, PYSNMP_MODULE_ID=ahTrapModule, ahChannelPowerChangeEvent=ahChannelPowerChangeEvent, ahCRCErrRate=ahCRCErrRate, ahCode=ahCode, AhAuthenticationMethod=AhAuthenticationMethod, ahThresholdHigh=ahThresholdHigh, ahPoEEth0Pwr=ahPoEEth0Pwr, ahRadioTxPower=ahRadioTxPower, ahBandwidthSentinelEvent=ahBandwidthSentinelEvent, ahAlarmMsgMapAlertEvent=ahAlarmMsgMapAlertEvent, ahSnapshotInterference=ahSnapshotInterference, AhState=AhState, ahTrapDesc=ahTrapDesc, ahClientAuthMethod=ahClientAuthMethod, ahClientChannel=ahClientChannel, ahInterferenceMapAlertEvent=ahInterferenceMapAlertEvent, ahBandwidthSentinelStatus=ahBandwidthSentinelStatus, ahClientCWPUsed=ahClientCWPUsed, ahLevel=ahLevel, ahPoEEth1MaxSpeed=ahPoEEth1MaxSpeed, ahIfIndex=ahIfIndex, ahBSSID=ahBSSID, ahIDPChannel=ahIDPChannel, ahBandwidthSentinelAction=ahBandwidthSentinelAction, ahActualBandwidth=ahActualBandwidth, AhProbableCause=AhProbableCause, ahClientMACProtocol=ahClientMACProtocol, ahClientUserProfId=ahClientUserProfId, ahFailureSet=ahFailureSet, ahIDPType=ahIDPType, ahPowerSrc=ahPowerSrc, ahPoEEth0On=ahPoEEth0On, ahSnapshotValue=ahSnapshotValue, ahDiscoverAge=ahDiscoverAge, ahStateChangeEvent=ahStateChangeEvent, ahInterferenceThreshold=ahInterferenceThreshold, ahPoEEth0MaxSpeed=ahPoEEth0MaxSpeed, ahPoEEth1On=ahPoEEth1On, ahUpdateAge=ahUpdateAge, ahCRCErrRateThreshold=ahCRCErrRateThreshold, ahRadioChannel=ahRadioChannel, ahThresholdLow=ahThresholdLow, ahObjectType=ahObjectType, ahAlarmAlertType=ahAlarmAlertType, ahThresholdValue=ahThresholdValue, ahCurValue=ahCurValue, ahProbableCause=ahProbableCause, ahRemoved=ahRemoved, ahPoEEth1Pwr=ahPoEEth1Pwr, ahCurrentState=ahCurrentState, ahGuaranteedBandwidth=ahGuaranteedBandwidth, ahPreviousState=ahPreviousState, ahSeverity=ahSeverity, ahClientMAC=ahClientMAC, ahBeaconInterval=ahBeaconInterval, ahObjectName=ahObjectName, ahTrapModule=ahTrapModule, ahIDPStationData=ahIDPStationData)
