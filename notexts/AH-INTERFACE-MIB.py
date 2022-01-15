#
# PySNMP MIB module AH-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-INTERFACE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:06 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
AhNodeID, AhString, AhMACProtocol, AhInterfaceType, AhInterfaceMode, ahAPInterface = mibBuilder.importSymbols("AH-SMI-MIB", "AhNodeID", "AhString", "AhMACProtocol", "AhInterfaceType", "AhInterfaceMode", "ahAPInterface")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Counter64, MibIdentifier, Bits, Gauge32, iso, IpAddress, Unsigned32, ObjectIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Counter64", "MibIdentifier", "Bits", "Gauge32", "iso", "IpAddress", "Unsigned32", "ObjectIdentity", "NotificationType", "TimeTicks")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ahInterface = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: ahInterface.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: ahInterface.setOrganization('Aerohive Networks, Inc')
class AhAuthenticationMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("cwp", 0), ("open", 1), ("wep-open", 2), ("wep-shared", 3), ("wpa-psk", 4), ("wpa2-psk", 5), ("wpa-8021x", 6), ("wpa2-8021X", 7), ("wpa-auto-psk", 8), ("wpa-auto-8021x", 9), ("dynamic-wep", 10))

class AhEncrytionMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("AES", 0), ("TKIP", 1), ("WEP", 2), ("Non", 3))

ahXIfTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: ahXIfTable.setStatus('current')
ahXIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1), )
ifEntry.registerAugmentions(("AH-INTERFACE-MIB", "ahXIfEntry"))
ahXIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: ahXIfEntry.setStatus('current')
ahIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 1), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfName.setStatus('current')
ahSSIDName = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 2), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSSIDName.setStatus('current')
ahIfPromiscuous = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfPromiscuous.setStatus('current')
ahIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 4), AhInterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfType.setStatus('current')
ahIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 5), AhInterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfMode.setStatus('current')
ahIfConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 6), AhInterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfConfMode.setStatus('current')
ahAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2), )
if mibBuilder.loadTexts: ahAssociationTable.setStatus('current')
ahAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "AH-INTERFACE-MIB", "ahClientMac"))
if mibBuilder.loadTexts: ahAssociationEntry.setStatus('current')
ahClientMac = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 1), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientMac.setStatus('current')
ahClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientIP.setStatus('current')
ahClientHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 3), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientHostname.setStatus('current')
ahClientRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRSSI.setStatus('current')
ahClientLinkUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLinkUptime.setStatus('current')
ahClientCWPUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientCWPUsed.setStatus('current')
ahClientAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 7), AhAuthenticationMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientAuthMethod.setStatus('current')
ahClientEncryptionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 8), AhEncrytionMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientEncryptionMethod.setStatus('current')
ahClientMACProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 9), AhMACProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientMACProtocol.setStatus('current')
ahClientSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 10), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientSSID.setStatus('current')
ahClientVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientVLAN.setStatus('current')
ahClientUserProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientUserProfId.setStatus('current')
ahClientChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientChannel.setStatus('current')
ahClientLastTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLastTxRate.setStatus('current')
ahClientUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 15), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientUsername.setStatus('current')
ahClientRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxDataFrames.setStatus('current')
ahClientRxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxDataOctets.setStatus('current')
ahClientRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMgtFrames.setStatus('current')
ahClientRxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxUnicastFrames.setStatus('current')
ahClientRxMulticastFrames = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMulticastFrames.setStatus('current')
ahClientRxBroadcastFrames = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxBroadcastFrames.setStatus('current')
ahClientRxMICFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMICFailures.setStatus('current')
ahClientTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxDataFrames.setStatus('current')
ahClientTxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxMgtFrames.setStatus('current')
ahClientTxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxDataOctets.setStatus('current')
ahClientTxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxUnicastFrames.setStatus('current')
ahClientTxMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxMulticastFrames.setStatus('current')
ahClientTxBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBroadcastFrames.setStatus('current')
ahClientLastRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLastRxRate.setStatus('current')
ahClientTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBeDataFrames.setStatus('current')
ahClientTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBgDataFrames.setStatus('current')
ahClientTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxViDataFrames.setStatus('current')
ahClientTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxVoDataFrames.setStatus('current')
ahClientTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxAirtime.setStatus('current')
ahClientRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxAirtime.setStatus('current')
ahClientAssociationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientAssociationTime.setStatus('current')
ahClientBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 37), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientBSSID.setStatus('current')
ahRadioStatsTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3), )
if mibBuilder.loadTexts: ahRadioStatsTable.setStatus('current')
ahRadioStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahRadioStatsEntry.setStatus('current')
ahRadioTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxDataFrames.setStatus('current')
ahRadioTxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxUnicastDataFrames.setStatus('current')
ahRadioTxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxMulticastDataFrames.setStatus('current')
ahRadioTxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBroadcastDataFrames.setStatus('current')
ahRadioTxNonBeaconMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxNonBeaconMgtFrames.setStatus('current')
ahRadioTxBeaconFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBeaconFrames.setStatus('current')
ahRadioTxTotalRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalRetries.setStatus('current')
ahRadioTxTotalFramesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalFramesDropped.setStatus('current')
ahRadioTxTotalFrameErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalFrameErrors.setStatus('current')
ahRadioTxFEForExcessiveHWRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxFEForExcessiveHWRetries.setStatus('current')
ahRadioRxTotalDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxTotalDataFrames.setStatus('current')
ahRadioRxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxUnicastDataFrames.setStatus('current')
ahRadioRxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxMulticastDataFrames.setStatus('current')
ahRadioRxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxBroadcastDataFrames.setStatus('current')
ahRadioRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxMgtFrames.setStatus('current')
ahRadioRxTotalFrameDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxTotalFrameDropped.setStatus('current')
ahRadioTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBeDataFrames.setStatus('current')
ahRadioTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBgDataFrames.setStatus('current')
ahRadioTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxViDataFrames.setStatus('current')
ahRadioTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxVoDataFrames.setStatus('current')
ahRadioTXRTSFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTXRTSFailures.setStatus('current')
ahRadioTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxAirtime.setStatus('current')
ahRadioRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxAirtime.setStatus('current')
ahVIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4), )
if mibBuilder.loadTexts: ahVIfStatsTable.setStatus('current')
ahVIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahVIfStatsEntry.setStatus('current')
ahVIfRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxDataFrames.setStatus('current')
ahVIfRxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxUnicastDataFrames.setStatus('current')
ahVIfRxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxMulticastDataFrames.setStatus('current')
ahVIfRxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxBroadcastDataFrames.setStatus('current')
ahVIfRxErrorFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxErrorFrames.setStatus('current')
ahVIfRxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxDroppedFrames.setStatus('current')
ahVIfTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxDataFrames.setStatus('current')
ahVIfTxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxUnicastDataFrames.setStatus('current')
ahVIfTxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxMulticastDataFrames.setStatus('current')
ahVIfTxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBroadcastDataFrames.setStatus('current')
ahVIfTxErrorFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxErrorFrames.setStatus('current')
ahVIfTxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxDroppedFrames.setStatus('current')
ahVIfTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBeDataFrames.setStatus('current')
ahVIfTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBgDataFrames.setStatus('current')
ahVIfTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxViDataFrames.setStatus('current')
ahVIfTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxVoDataFrames.setStatus('current')
ahVifTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVifTxAirtime.setStatus('current')
ahVifRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVifRxAirtime.setStatus('current')
ahRadioAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5), )
if mibBuilder.loadTexts: ahRadioAttributeTable.setStatus('current')
ahRadioAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahRadioAttributeEntry.setStatus('current')
ahRadioChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioChannel.setStatus('current')
ahRadioTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxPower.setStatus('current')
ahRadioNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioNoiseFloor.setStatus('current')
mibBuilder.exportSymbols("AH-INTERFACE-MIB", ahClientEncryptionMethod=ahClientEncryptionMethod, ahVIfTxMulticastDataFrames=ahVIfTxMulticastDataFrames, ahRadioTxFEForExcessiveHWRetries=ahRadioTxFEForExcessiveHWRetries, ahVIfTxDataFrames=ahVIfTxDataFrames, ahClientRSSI=ahClientRSSI, ahClientMac=ahClientMac, ahVIfRxErrorFrames=ahVIfRxErrorFrames, ahRadioTxBroadcastDataFrames=ahRadioTxBroadcastDataFrames, ahRadioStatsTable=ahRadioStatsTable, ahRadioTxDataFrames=ahRadioTxDataFrames, ahRadioRxMulticastDataFrames=ahRadioRxMulticastDataFrames, ahRadioAttributeEntry=ahRadioAttributeEntry, ahClientTxBgDataFrames=ahClientTxBgDataFrames, ahVIfTxViDataFrames=ahVIfTxViDataFrames, ahRadioTxPower=ahRadioTxPower, ahIfConfMode=ahIfConfMode, ahVIfTxDroppedFrames=ahVIfTxDroppedFrames, ahRadioTxBeDataFrames=ahRadioTxBeDataFrames, ahVIfRxDroppedFrames=ahVIfRxDroppedFrames, ahClientTxMgtFrames=ahClientTxMgtFrames, ahIfPromiscuous=ahIfPromiscuous, ahXIfTable=ahXIfTable, ahVIfStatsEntry=ahVIfStatsEntry, ahRadioTxAirtime=ahRadioTxAirtime, ahRadioNoiseFloor=ahRadioNoiseFloor, ahRadioChannel=ahRadioChannel, ahVIfRxDataFrames=ahVIfRxDataFrames, ahVIfRxUnicastDataFrames=ahVIfRxUnicastDataFrames, ahClientLastRxRate=ahClientLastRxRate, ahRadioRxBroadcastDataFrames=ahRadioRxBroadcastDataFrames, ahVifTxAirtime=ahVifTxAirtime, ahRadioRxUnicastDataFrames=ahRadioRxUnicastDataFrames, ahXIfEntry=ahXIfEntry, ahAssociationTable=ahAssociationTable, ahClientLastTxRate=ahClientLastTxRate, ahClientAssociationTime=ahClientAssociationTime, ahRadioRxMgtFrames=ahRadioRxMgtFrames, ahRadioTxBgDataFrames=ahRadioTxBgDataFrames, ahClientCWPUsed=ahClientCWPUsed, ahClientRxMulticastFrames=ahClientRxMulticastFrames, ahIfType=ahIfType, ahRadioTxTotalFramesDropped=ahRadioTxTotalFramesDropped, ahVIfTxUnicastDataFrames=ahVIfTxUnicastDataFrames, ahClientTxViDataFrames=ahClientTxViDataFrames, ahVIfRxMulticastDataFrames=ahVIfRxMulticastDataFrames, ahSSIDName=ahSSIDName, ahClientRxBroadcastFrames=ahClientRxBroadcastFrames, AhEncrytionMethod=AhEncrytionMethod, ahClientRxAirtime=ahClientRxAirtime, ahClientRxDataOctets=ahClientRxDataOctets, ahRadioTxVoDataFrames=ahRadioTxVoDataFrames, ahIfName=ahIfName, ahRadioTxViDataFrames=ahRadioTxViDataFrames, ahClientTxDataFrames=ahClientTxDataFrames, ahRadioTxBeaconFrames=ahRadioTxBeaconFrames, ahRadioTxNonBeaconMgtFrames=ahRadioTxNonBeaconMgtFrames, ahRadioTxTotalRetries=ahRadioTxTotalRetries, ahClientSSID=ahClientSSID, ahAssociationEntry=ahAssociationEntry, ahClientUsername=ahClientUsername, ahClientRxMgtFrames=ahClientRxMgtFrames, ahClientRxMICFailures=ahClientRxMICFailures, ahClientTxMulticastFrames=ahClientTxMulticastFrames, ahRadioTXRTSFailures=ahRadioTXRTSFailures, ahVifRxAirtime=ahVifRxAirtime, ahClientAuthMethod=ahClientAuthMethod, ahClientRxUnicastFrames=ahClientRxUnicastFrames, ahClientVLAN=ahClientVLAN, ahRadioTxUnicastDataFrames=ahRadioTxUnicastDataFrames, ahVIfRxBroadcastDataFrames=ahVIfRxBroadcastDataFrames, ahClientTxVoDataFrames=ahClientTxVoDataFrames, ahVIfTxBeDataFrames=ahVIfTxBeDataFrames, ahVIfTxErrorFrames=ahVIfTxErrorFrames, ahRadioAttributeTable=ahRadioAttributeTable, ahClientHostname=ahClientHostname, ahClientTxBroadcastFrames=ahClientTxBroadcastFrames, ahRadioStatsEntry=ahRadioStatsEntry, ahRadioTxTotalFrameErrors=ahRadioTxTotalFrameErrors, ahRadioTxMulticastDataFrames=ahRadioTxMulticastDataFrames, ahClientTxDataOctets=ahClientTxDataOctets, ahVIfTxVoDataFrames=ahVIfTxVoDataFrames, ahRadioRxAirtime=ahRadioRxAirtime, ahVIfTxBroadcastDataFrames=ahVIfTxBroadcastDataFrames, ahVIfStatsTable=ahVIfStatsTable, ahRadioRxTotalFrameDropped=ahRadioRxTotalFrameDropped, PYSNMP_MODULE_ID=ahInterface, ahIfMode=ahIfMode, ahClientChannel=ahClientChannel, ahRadioRxTotalDataFrames=ahRadioRxTotalDataFrames, ahClientTxAirtime=ahClientTxAirtime, ahClientBSSID=ahClientBSSID, AhAuthenticationMethod=AhAuthenticationMethod, ahClientIP=ahClientIP, ahClientUserProfId=ahClientUserProfId, ahVIfTxBgDataFrames=ahVIfTxBgDataFrames, ahClientRxDataFrames=ahClientRxDataFrames, ahInterface=ahInterface, ahClientMACProtocol=ahClientMACProtocol, ahClientTxBeDataFrames=ahClientTxBeDataFrames, ahClientTxUnicastFrames=ahClientTxUnicastFrames, ahClientLinkUptime=ahClientLinkUptime)
