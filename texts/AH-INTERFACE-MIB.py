#
# PySNMP MIB module AH-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-INTERFACE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:07 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
AhInterfaceType, AhString, AhMACProtocol, AhNodeID, ahAPInterface, AhInterfaceMode = mibBuilder.importSymbols("AH-SMI-MIB", "AhInterfaceType", "AhString", "AhMACProtocol", "AhNodeID", "ahAPInterface", "AhInterfaceMode")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, ObjectIdentity, iso, Bits, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ObjectIdentity", "iso", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ahInterface = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: ahInterface.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: ahInterface.setOrganization('Aerohive Networks, Inc')
if mibBuilder.loadTexts: ahInterface.setContactInfo('info@aerohive.com\r\n                        1011 McCarthy Boulevard\r                        \r                        Milpitas, CA 95035')
if mibBuilder.loadTexts: ahInterface.setDescription('This module contains the MIB definition of \r\n\t\t\tinterface related information.')
class AhAuthenticationMethod(TextualConvention, Integer32):
    description = 'Authentication method supported within Aerohive AP'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("cwp", 0), ("open", 1), ("wep-open", 2), ("wep-shared", 3), ("wpa-psk", 4), ("wpa2-psk", 5), ("wpa-8021x", 6), ("wpa2-8021X", 7), ("wpa-auto-psk", 8), ("wpa-auto-8021x", 9), ("dynamic-wep", 10))

class AhEncrytionMethod(TextualConvention, Integer32):
    description = 'Encryption method supported within Aerohive AP'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("AES", 0), ("TKIP", 1), ("WEP", 2), ("Non", 3))

ahXIfTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: ahXIfTable.setStatus('current')
if mibBuilder.loadTexts: ahXIfTable.setDescription('Table of all the Interface/SSID info \r\n\t\t\tnot covered by the rfc 2863')
ahXIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1), )
ifEntry.registerAugmentions(("AH-INTERFACE-MIB", "ahXIfEntry"))
ahXIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: ahXIfEntry.setStatus('current')
if mibBuilder.loadTexts: ahXIfEntry.setDescription('Individual entry of Interface/SSID table')
ahIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 1), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfName.setStatus('current')
if mibBuilder.loadTexts: ahIfName.setDescription('Name - uniquely identifies an AP Interface.')
ahSSIDName = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 2), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSSIDName.setStatus('current')
if mibBuilder.loadTexts: ahSSIDName.setDescription('Name - identifies a wireless interface with Access mode.\r\n\t\t\tIf the interface is not a wireless interface with Access mode, the \r\n\t\t\tSSIDName should be set N/A')
ahIfPromiscuous = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfPromiscuous.setStatus('current')
if mibBuilder.loadTexts: ahIfPromiscuous.setDescription('Indicates whether an interface is in promiscuous \r\n\t\t\tmode or not.')
ahIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 4), AhInterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfType.setStatus('current')
if mibBuilder.loadTexts: ahIfType.setDescription('Indicates whether an interface is a physical \r\n\t\t\tor virtual one.')
ahIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 5), AhInterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfMode.setStatus('current')
if mibBuilder.loadTexts: ahIfMode.setDescription('Indicates whether an interface is used for Access\r\n\t\t\tor Backhaul currently.')
ahIfConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 6), AhInterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfConfMode.setStatus('current')
if mibBuilder.loadTexts: ahIfConfMode.setDescription('Indicates whether an interface is configured for Access\r\n\t\t\tor Backhaul.')
ahAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2), )
if mibBuilder.loadTexts: ahAssociationTable.setStatus('current')
if mibBuilder.loadTexts: ahAssociationTable.setDescription('Table of directly connected APs')
ahAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "AH-INTERFACE-MIB", "ahClientMac"))
if mibBuilder.loadTexts: ahAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: ahAssociationEntry.setDescription('Individual entry of client table')
ahClientMac = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 1), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientMac.setStatus('current')
if mibBuilder.loadTexts: ahClientMac.setDescription('Uniquely identifies a client.')
ahClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientIP.setStatus('current')
if mibBuilder.loadTexts: ahClientIP.setDescription('The IP address of the client if known. Otherwise, this\r\n\t\t\tfield should be 0')
ahClientHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 3), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientHostname.setStatus('current')
if mibBuilder.loadTexts: ahClientHostname.setDescription('The host name of the client if known. Otherwise, this\r\n\t\t\tfield should be empty')
ahClientRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRSSI.setStatus('current')
if mibBuilder.loadTexts: ahClientRSSI.setDescription('An indicator for the RSSI of the client \r\n\t\t\tderived from last communication')
ahClientLinkUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLinkUptime.setStatus('current')
if mibBuilder.loadTexts: ahClientLinkUptime.setDescription('Link up time in second')
ahClientCWPUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientCWPUsed.setStatus('current')
if mibBuilder.loadTexts: ahClientCWPUsed.setDescription('The boolean indicating whether Captive Web Portal\r\n\t\t\tis used.')
ahClientAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 7), AhAuthenticationMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientAuthMethod.setStatus('current')
if mibBuilder.loadTexts: ahClientAuthMethod.setDescription('The authentication method the client uses to communicated\r\n\t\t\twith AP')
ahClientEncryptionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 8), AhEncrytionMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientEncryptionMethod.setStatus('current')
if mibBuilder.loadTexts: ahClientEncryptionMethod.setDescription('The encryption method the client uses to communicated\r\n\t\t\twith AP')
ahClientMACProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 9), AhMACProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientMACProtocol.setStatus('current')
if mibBuilder.loadTexts: ahClientMACProtocol.setDescription('The radio mode the client uses to communicated\r\n\t\t\twith AP')
ahClientSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 10), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientSSID.setStatus('current')
if mibBuilder.loadTexts: ahClientSSID.setDescription('The SSID used by client to communicated\r\n\t\t\twith AP')
ahClientVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientVLAN.setStatus('current')
if mibBuilder.loadTexts: ahClientVLAN.setDescription('The VLAN used by client to communicated\r\n\t\t\twith AP')
ahClientUserProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientUserProfId.setStatus('current')
if mibBuilder.loadTexts: ahClientUserProfId.setDescription('The user profile id used by client to communicated\r\n\t\t\twith AP')
ahClientChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientChannel.setStatus('current')
if mibBuilder.loadTexts: ahClientChannel.setDescription('The radio channel used by client to communicated\r\n\t\t\twith AP')
ahClientLastTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLastTxRate.setStatus('current')
if mibBuilder.loadTexts: ahClientLastTxRate.setDescription('The rate (KBPS) of last transmitting frame to the client.')
ahClientUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 15), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientUsername.setStatus('current')
if mibBuilder.loadTexts: ahClientUsername.setDescription('The client user name to login to the network.\r\n\t\t\tIt contain empty string if the authentication\r\n\t\t\tmethod is other than EAP (802.1x).')
ahClientRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxDataFrames.setDescription('The number of data frames received from client\r\n\t\t\tto AP')
ahClientRxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxDataOctets.setStatus('current')
if mibBuilder.loadTexts: ahClientRxDataOctets.setDescription('The number of data octets received from client\r\n\t\t\tto AP')
ahClientRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxMgtFrames.setDescription('The number of mgt frames received from client\r\n\t\t\tto AP')
ahClientRxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxUnicastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxUnicastFrames.setDescription('The number of unitcast frames received from client\r\n\t\t\tto AP')
ahClientRxMulticastFrames = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxMulticastFrames.setDescription('The number of multicast frames received\r\n\t\t\tfrom client to AP.')
ahClientRxBroadcastFrames = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxBroadcastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxBroadcastFrames.setDescription('The number of broadcast frames received\r\n\t\t\tfrom client to AP.')
ahClientRxMICFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMICFailures.setStatus('current')
if mibBuilder.loadTexts: ahClientRxMICFailures.setDescription('The number of frames dropped due to Message\r\n\t\t\tIntegrity Check failure from client to AP.')
ahClientTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxDataFrames.setDescription('The number of transmitted data frames\r\n\t\t\tfrom .')
ahClientTxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxMgtFrames.setDescription('The number of transmitted management frames\r\n\t\t\tfrom .')
ahClientTxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxDataOctets.setStatus('current')
if mibBuilder.loadTexts: ahClientTxDataOctets.setDescription('The number of transmitted data in octets\r\n\t\t\tfrom .')
ahClientTxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxUnicastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxUnicastFrames.setDescription('The number of unitcast frames transmitted from client\r\n\t\t\tto AP')
ahClientTxMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxMulticastFrames.setDescription('The number of multicast frames transmitted from client\r\n\t\t\tto AP')
ahClientTxBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBroadcastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxBroadcastFrames.setDescription('The number of broadcast frames transmitted from client\r\n\t\t\tto AP')
ahClientLastRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLastRxRate.setStatus('current')
if mibBuilder.loadTexts: ahClientLastRxRate.setDescription('The rate (KBPS) of last received frame from client.')
ahClientTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBeDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxBeDataFrames.setDescription('The number of transmitted best effort priority data frames\r\n\t\t\tfrom AP to client.')
ahClientTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBgDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxBgDataFrames.setDescription('The number of transmitted back ground priority data frames\r\n\t\t\tfrom AP to client.')
ahClientTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxViDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxViDataFrames.setDescription('The number of transmitted video priority data frames\r\n\t\t\tfrom AP to client.')
ahClientTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxVoDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxVoDataFrames.setDescription('The number of transmitted voice priority data frames\r\n\t\t\tfrom AP to client.')
ahClientTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahClientTxAirtime.setDescription('The accumulative transmit time in microseconds ()\r\n\t\t\tfrom AP to client.')
ahClientRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahClientRxAirtime.setDescription('The accumulative receive time in microseconds (us)\r\n\t\t\tfrom client to AP.')
ahClientAssociationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientAssociationTime.setStatus('current')
if mibBuilder.loadTexts: ahClientAssociationTime.setDescription('The association time(s) of client connect to AP.')
ahClientBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 37), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientBSSID.setStatus('current')
if mibBuilder.loadTexts: ahClientBSSID.setDescription('It is the basic service set identifier of the client.')
ahRadioStatsTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3), )
if mibBuilder.loadTexts: ahRadioStatsTable.setStatus('current')
if mibBuilder.loadTexts: ahRadioStatsTable.setDescription('Table of radio interface statistics.')
ahRadioStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahRadioStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ahRadioStatsEntry.setDescription('Individual entry of client table')
ahRadioTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxDataFrames.setDescription('The number of transmit data frames for the given\r\n\t\t\tinterface.')
ahRadioTxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxUnicastDataFrames.setDescription('The number of transmitted unicast frames   \r\n\t\t\t for the given interface.')
ahRadioTxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxMulticastDataFrames.setDescription('The number of transmitted multicast frames   \r\n\t\t\t for the given interface.')
ahRadioTxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBroadcastDataFrames.setDescription('The number of transmitted broadcast frames   \r\n\t\t\t for the given interface.')
ahRadioTxNonBeaconMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxNonBeaconMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxNonBeaconMgtFrames.setDescription('The number of transmit management frames\r\n\t\t\tother than beacon for the given interface.')
ahRadioTxBeaconFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBeaconFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBeaconFrames.setDescription('The number of transmit beacon frames for the given \r\n\t\t\tinterface.')
ahRadioTxTotalRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalRetries.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxTotalRetries.setDescription('The total number of transmit retries for the given \r\n\t\t\tinterface.')
ahRadioTxTotalFramesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalFramesDropped.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxTotalFramesDropped.setDescription('The number of transmit frames dropped\r\n\t\t\tfor the given interface.')
ahRadioTxTotalFrameErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalFrameErrors.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxTotalFrameErrors.setDescription('The total number of transmit frames in error\r\n\t\t\t for the given interface.')
ahRadioTxFEForExcessiveHWRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxFEForExcessiveHWRetries.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxFEForExcessiveHWRetries.setDescription('The number of transmit frames in error due to \r\n\t\t\texcessive hardware retries for the given interface.')
ahRadioRxTotalDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxTotalDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxTotalDataFrames.setDescription('The total number of received data frames \r\n\t\t\tfor the given interface.')
ahRadioRxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxUnicastDataFrames.setDescription('The number of received unicast frames   \r\n\t\t\t for the given interface.')
ahRadioRxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxMulticastDataFrames.setDescription('The number of received multicast frames   \r\n\t\t\t for the given interface.')
ahRadioRxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxBroadcastDataFrames.setDescription('The number of received broadcast frames   \r\n\t\t\t for the given interface.')
ahRadioRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxMgtFrames.setDescription('The number of received management frames \r\n\t\t\tfor the given interface.')
ahRadioRxTotalFrameDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxTotalFrameDropped.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxTotalFrameDropped.setDescription('The total number of dropped received frames   \r\n\t\t\tfor the given interface.')
ahRadioTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBeDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBeDataFrames.setDescription('The number of transmitted best effort priority data frames\r\n\t\t\tfrom the radio.')
ahRadioTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBgDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBgDataFrames.setDescription('The number of transmitted back ground priority data frames\r\n\t\t\tfrom the radio.')
ahRadioTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxViDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxViDataFrames.setDescription('The number of transmitted video priority data frames\r\n\t\t\tfrom the radio.')
ahRadioTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxVoDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxVoDataFrames.setDescription('The number of transmitted voice priority data frames\r\n\t\t\tfrom the radio.')
ahRadioTXRTSFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTXRTSFailures.setStatus('current')
if mibBuilder.loadTexts: ahRadioTXRTSFailures.setDescription('The number of transmitted RTS failures\r\n\t\t\tfrom the Radio.')
ahRadioTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxAirtime.setDescription('The accumulative transmit time in microseconds (us)\r\n\t\t\tfrom the given Radio.')
ahRadioRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxAirtime.setDescription('The accumulative receive time in microseconds (us)\r\n\t\t\tto the given radio.')
ahVIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4), )
if mibBuilder.loadTexts: ahVIfStatsTable.setStatus('current')
if mibBuilder.loadTexts: ahVIfStatsTable.setDescription('Table of virtual interface (vif) statistics.')
ahVIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahVIfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ahVIfStatsEntry.setDescription('Individual entry of VIf statistics')
ahVIfRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxDataFrames.setDescription('The number of received data frames for the given\r\n\t\t\tvirtual interface.')
ahVIfRxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxUnicastDataFrames.setDescription('The number of received unicast data frames   \r\n\t\t\t for the given virtual interface.')
ahVIfRxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxMulticastDataFrames.setDescription('The number of received multicast data frames   \r\n\t\t\t for the given virtual interface.')
ahVIfRxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxBroadcastDataFrames.setDescription('The number of received broadcast data frames   \r\n\t\t\t for the given virtual interface.')
ahVIfRxErrorFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxErrorFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxErrorFrames.setDescription('The number of received error frames for the given\r\n\t\t\tvirtual interface.')
ahVIfRxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxDroppedFrames.setDescription('The number of received dropped frames for the given\r\n\t\t\tvirtual interface.')
ahVIfTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxDataFrames.setDescription('The number of trasmitted data frames \r\n\t\t\tfor the given virtual interface.')
ahVIfTxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxUnicastDataFrames.setDescription('The number of transmitted unicast data frames   \r\n\t\t\t for the given virtual interface.')
ahVIfTxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxMulticastDataFrames.setDescription('The number of transmitted multicast data frames   \r\n\t\t\t for the given virtual interface.')
ahVIfTxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxBroadcastDataFrames.setDescription('The number of transmitted broadcast data frames   \r\n\t\t\t for the given virtual interface.')
ahVIfTxErrorFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxErrorFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxErrorFrames.setDescription('The number of trasmitted frames encontered error \r\n\t\t\tfor the given virtual interface.')
ahVIfTxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxDroppedFrames.setDescription('The number of trasmitted frames dropped due to error  \r\n\t\t\tcondition for the given virtual interface.')
ahVIfTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBeDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxBeDataFrames.setDescription('The number of transmitted best effort priority data frames\r\n\t\t\tfrom the virtual interface.')
ahVIfTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBgDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxBgDataFrames.setDescription('The number of transmitted back ground priority data frames\r\n\t\t\tfrom the virtual interface.')
ahVIfTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxViDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxViDataFrames.setDescription('The number of transmitted video priority data frames\r\n\t\t\tfrom the virtual interface.')
ahVIfTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxVoDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxVoDataFrames.setDescription('The number of transmitted voice priority data frames\r\n\t\t\tfrom the virtual interface.')
ahVifTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVifTxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahVifTxAirtime.setDescription('The accumulative transmit time in microseconds (us)\r\n\t\t\tfrom the given SSID.')
ahVifRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVifRxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahVifRxAirtime.setDescription('The accumulative receive time in microseconds (us)\r\n\t\t\tto the given SSID.')
ahRadioAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5), )
if mibBuilder.loadTexts: ahRadioAttributeTable.setStatus('current')
if mibBuilder.loadTexts: ahRadioAttributeTable.setDescription('Table of radio interface statistics.')
ahRadioAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahRadioAttributeEntry.setStatus('current')
if mibBuilder.loadTexts: ahRadioAttributeEntry.setDescription('Individual entry for each Radio')
ahRadioChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioChannel.setStatus('current')
if mibBuilder.loadTexts: ahRadioChannel.setDescription('The channel number currently in use for this radio.')
ahRadioTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxPower.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxPower.setDescription('The transmit power currently for the radio in dbm. The range \r\n\t\t\t\tis 0 to 20 dBm')
ahRadioNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioNoiseFloor.setStatus('current')
if mibBuilder.loadTexts: ahRadioNoiseFloor.setDescription('The noise floor for the radio dbm. The range is 0 to 256 dBm.\r\n\t\t\t\tThe value of this variable is the actual value plus 256 dBm.')
mibBuilder.exportSymbols("AH-INTERFACE-MIB", ahRadioTxVoDataFrames=ahRadioTxVoDataFrames, ahRadioNoiseFloor=ahRadioNoiseFloor, ahClientRxMICFailures=ahClientRxMICFailures, ahClientRxUnicastFrames=ahClientRxUnicastFrames, ahVifRxAirtime=ahVifRxAirtime, ahClientAuthMethod=ahClientAuthMethod, ahRadioRxMgtFrames=ahRadioRxMgtFrames, PYSNMP_MODULE_ID=ahInterface, ahIfConfMode=ahIfConfMode, ahRadioRxMulticastDataFrames=ahRadioRxMulticastDataFrames, ahIfMode=ahIfMode, ahIfName=ahIfName, ahRadioChannel=ahRadioChannel, ahClientBSSID=ahClientBSSID, ahClientMac=ahClientMac, ahClientTxDataFrames=ahClientTxDataFrames, ahVIfTxErrorFrames=ahVIfTxErrorFrames, ahRadioTxUnicastDataFrames=ahRadioTxUnicastDataFrames, ahClientCWPUsed=ahClientCWPUsed, ahVIfTxVoDataFrames=ahVIfTxVoDataFrames, ahRadioRxUnicastDataFrames=ahRadioRxUnicastDataFrames, ahSSIDName=ahSSIDName, ahRadioRxTotalDataFrames=ahRadioRxTotalDataFrames, ahClientTxDataOctets=ahClientTxDataOctets, ahRadioStatsTable=ahRadioStatsTable, ahXIfEntry=ahXIfEntry, ahClientRxDataFrames=ahClientRxDataFrames, ahClientChannel=ahClientChannel, ahVIfTxDataFrames=ahVIfTxDataFrames, ahRadioAttributeEntry=ahRadioAttributeEntry, ahRadioTxTotalRetries=ahRadioTxTotalRetries, AhEncrytionMethod=AhEncrytionMethod, ahRadioTxMulticastDataFrames=ahRadioTxMulticastDataFrames, ahRadioTxDataFrames=ahRadioTxDataFrames, ahVIfTxBgDataFrames=ahVIfTxBgDataFrames, ahAssociationEntry=ahAssociationEntry, ahClientUserProfId=ahClientUserProfId, ahClientLastTxRate=ahClientLastTxRate, ahVIfRxMulticastDataFrames=ahVIfRxMulticastDataFrames, ahXIfTable=ahXIfTable, ahRadioTxTotalFrameErrors=ahRadioTxTotalFrameErrors, ahClientVLAN=ahClientVLAN, ahRadioRxAirtime=ahRadioRxAirtime, ahClientRxMulticastFrames=ahClientRxMulticastFrames, ahClientTxBgDataFrames=ahClientTxBgDataFrames, ahClientHostname=ahClientHostname, ahVIfTxUnicastDataFrames=ahVIfTxUnicastDataFrames, ahClientUsername=ahClientUsername, ahIfType=ahIfType, ahClientRxMgtFrames=ahClientRxMgtFrames, ahClientIP=ahClientIP, ahRadioTxNonBeaconMgtFrames=ahRadioTxNonBeaconMgtFrames, ahRadioRxBroadcastDataFrames=ahRadioRxBroadcastDataFrames, ahInterface=ahInterface, ahVIfTxBroadcastDataFrames=ahVIfTxBroadcastDataFrames, ahVIfRxDataFrames=ahVIfRxDataFrames, ahClientLinkUptime=ahClientLinkUptime, ahClientTxViDataFrames=ahClientTxViDataFrames, ahVIfStatsEntry=ahVIfStatsEntry, ahRadioTxBeDataFrames=ahRadioTxBeDataFrames, ahClientTxBeDataFrames=ahClientTxBeDataFrames, ahClientTxVoDataFrames=ahClientTxVoDataFrames, ahRadioTxPower=ahRadioTxPower, ahVIfRxDroppedFrames=ahVIfRxDroppedFrames, ahRadioAttributeTable=ahRadioAttributeTable, ahRadioTxViDataFrames=ahRadioTxViDataFrames, ahIfPromiscuous=ahIfPromiscuous, ahRadioStatsEntry=ahRadioStatsEntry, ahVIfRxUnicastDataFrames=ahVIfRxUnicastDataFrames, ahVIfRxBroadcastDataFrames=ahVIfRxBroadcastDataFrames, ahClientLastRxRate=ahClientLastRxRate, ahClientRxAirtime=ahClientRxAirtime, ahVIfTxDroppedFrames=ahVIfTxDroppedFrames, ahAssociationTable=ahAssociationTable, ahRadioTxAirtime=ahRadioTxAirtime, ahClientTxAirtime=ahClientTxAirtime, ahVIfRxErrorFrames=ahVIfRxErrorFrames, ahClientAssociationTime=ahClientAssociationTime, ahRadioTxFEForExcessiveHWRetries=ahRadioTxFEForExcessiveHWRetries, ahVIfTxMulticastDataFrames=ahVIfTxMulticastDataFrames, ahClientTxMulticastFrames=ahClientTxMulticastFrames, ahClientTxBroadcastFrames=ahClientTxBroadcastFrames, ahClientRxDataOctets=ahClientRxDataOctets, ahRadioTxTotalFramesDropped=ahRadioTxTotalFramesDropped, ahClientRSSI=ahClientRSSI, ahClientTxUnicastFrames=ahClientTxUnicastFrames, ahRadioRxTotalFrameDropped=ahRadioRxTotalFrameDropped, ahVIfStatsTable=ahVIfStatsTable, ahClientEncryptionMethod=ahClientEncryptionMethod, ahVIfTxViDataFrames=ahVIfTxViDataFrames, AhAuthenticationMethod=AhAuthenticationMethod, ahClientSSID=ahClientSSID, ahRadioTxBgDataFrames=ahRadioTxBgDataFrames, ahClientMACProtocol=ahClientMACProtocol, ahVifTxAirtime=ahVifTxAirtime, ahRadioTXRTSFailures=ahRadioTXRTSFailures, ahRadioTxBroadcastDataFrames=ahRadioTxBroadcastDataFrames, ahClientRxBroadcastFrames=ahClientRxBroadcastFrames, ahRadioTxBeaconFrames=ahRadioTxBeaconFrames, ahVIfTxBeDataFrames=ahVIfTxBeDataFrames, ahClientTxMgtFrames=ahClientTxMgtFrames)
