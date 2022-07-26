#
# PySNMP MIB module ATKK-WLAN-ACCESS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/ATKK-WLAN-ACCESS-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:23:05 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
wirelesslan, wirelessLanmMIB = mibBuilder.importSymbols("AT-SMI-MIB", "wirelesslan", "wirelessLanmMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, ModuleIdentity, Counter64, MibIdentifier, enterprises, Gauge32, Integer32, iso, IpAddress, Bits, Counter32, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibIdentifier", "enterprises", "Gauge32", "Integer32", "iso", "IpAddress", "Bits", "Counter32", "TimeTicks", "Unsigned32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
atkkWlanAccess = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6))
atkkWlanAccess.setRevisions(('2016-05-25 00:00', '2016-03-23 00:00', '2015-06-17 00:00', '2015-05-11 00:00', '2014-09-30 00:00', '2013-11-22 00:00', '2012-08-13 00:00', '2012-07-09 00:00', '2012-06-06 00:00', '2012-01-11 00:00', '2011-04-08 00:00', '2010-08-20 00:00', '2009-07-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atkkWlanAccess.setRevisionsDescriptions(('1.6.3: - Fixed MIB structure error.', '1.6.2: - Added radar detected channels to DFS radar detection trap.', '1.6.1: - Supported trap for DFS Radar detection.', '1.6.0: - Supported AT-TQ4400e.', '1.5.1: - Changed to import AT-SMI-MIB from ATKK-WLAN-SMI-MIB.', '1.5.0: - Supported AT-TQ3200/AT-TQ3400/AT-TQ4400/AT-TQ4600.\n                - Added 11ac to atkkWiAcClient80211Spec and\n                  atkkWiAcAP80211Spec.', '1.4.0: - Supported AT-TQ3600.', '1.3.2: - Supported atkkWiAcAPDetectConfig2 for TQ2450 wlan1 AP detect \n                  configuration.', '1.3.1: - Expand the range of TrapHostString and CommunityString to 256.', '1.3.0: - Supported AT-TQ2450.\n                - Added 11n to atkkWiAcClient80211Spec and\n                  atkkWiAcClient80211Spec.', '1.2.0: - Supported AT-TQ2403EX.', '1.1.0: - Supported UserID by the Associated-STAs \n                  information, STA Associated/Disassociated trap \n                  and Filtered STA trap.\n                - Added RADIUS Authentication result trap.\n                - Added trap config by the AP information.\n                - Standardized the file head.\n                - Corrected typo.', '1.0.0: Initial release.',))
if mibBuilder.loadTexts: atkkWlanAccess.setLastUpdated('201605250000Z')
if mibBuilder.loadTexts: atkkWlanAccess.setOrganization('Allied Telesis K.K.')
if mibBuilder.loadTexts: atkkWlanAccess.setContactInfo('http://www.allied-telesis.co.jp')
if mibBuilder.loadTexts: atkkWlanAccess.setDescription('Private MIB for the AT-TQ series wireless access point.')
tq2403 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 13))
tq2450 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 19))
tq2403ex = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 20))
tq3600 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 22))
tq3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 24))
tq3400 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 25))
tq4400 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 26))
tq4600 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 27))
tq4400e = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 34))
class SsidString(TextualConvention, OctetString):
    description = 'This type is string for SSID(Service Set ID).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class UserIdString(TextualConvention, OctetString):
    description = 'This type is string for RADIUS UserID.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TrapHostString(TextualConvention, OctetString):
    description = 'This type is string for trap host IP address/hostname.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

class CommunityString(TextualConvention, OctetString):
    description = 'This type is string for trap community.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

class TrapString(TextualConvention, OctetString):
    description = 'This type is string for trap messages.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

class ChannelString(TextualConvention, OctetString):
    description = 'This type is string for channels which detected radar.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

atkkWiAcVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcVersion.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcVersion.setDescription('The version number of this MIB module')
atkkWiAcApInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6))
if mibBuilder.loadTexts: atkkWiAcApInfo.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApInfo.setDescription('AP information')
atkkWiAcApInfoTrapTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1), )
if mibBuilder.loadTexts: atkkWiAcApInfoTrapTable.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApInfoTrapTable.setDescription('Table that contains information about \n               a trap configuration of this AP.')
atkkWiAcApInfoTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcApTrapHost"))
if mibBuilder.loadTexts: atkkWiAcApInfoTrapEntry.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApInfoTrapEntry.setDescription('Information about a trap configuration.')
atkkWiAcApTrapHost = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 1), TrapHostString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapHost.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapHost.setDescription('TrapHost configuration of this AP.')
atkkWiAcApTrapCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 2), CommunityString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapCommunity.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapCommunity.setDescription('TrapCommunity configuration of this AP.')
atkkWiAcApTrapColdStartConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapColdStartConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapColdStartConfig.setDescription('Enable/disable configuration of the ColdStart trap.')
atkkWiAcApTrapLinkConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapLinkConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapLinkConfig.setDescription('Enable/disable configuration of the Link up/down trap.')
atkkWiAcApTrapAuthenticationConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapAuthenticationConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapAuthenticationConfig.setDescription('Enable/disable configuration of the Authentication trap.')
atkkWiAcApTrapAssociationConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapAssociationConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapAssociationConfig.setDescription('Enable/disable configuration of \n                an STA Association/Disassociation trap.')
atkkWiAcApTrapUnknownApConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapUnknownApConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapUnknownApConfig.setDescription('Enable/disable configuration of an Unknown AP detection trap.')
atkkWiAcApTrapFilteredStaConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapFilteredStaConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapFilteredStaConfig.setDescription('Enable/disable configuration of a Filtered STA detection trap.')
atkkWiAcApTrapRadiusAuthSuccessConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapRadiusAuthSuccessConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapRadiusAuthSuccessConfig.setDescription('Enable/disable configuration of the RADIUS Authentication success trap.')
atkkWiAcApTrapRadiusAuthFailConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapRadiusAuthFailConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapRadiusAuthFailConfig.setDescription('Enable/disable configuration of the RADIUS Authentication fail trap.')
atkkWiAcApTrapDfsDetectedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapDfsDetectedConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcApTrapDfsDetectedConfig.setDescription('Enable/disable configuration of the DFS Detected trap.')
atkkWiAcClients = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2))
if mibBuilder.loadTexts: atkkWiAcClients.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClients.setDescription('Connected Stations List.\n         This list consists of entries which describe STAs which are\n         currently connected (associated) to the AP.')
atkkWiAcClientTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1), )
if mibBuilder.loadTexts: atkkWiAcClientTable.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClientTable.setDescription('A table that contains information about STAs\n                 which are currently connected to the AP.')
atkkWiAcClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"))
if mibBuilder.loadTexts: atkkWiAcClientEntry.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClientEntry.setDescription('Information about a STA.')
atkkWiAcClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientAddress.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClientAddress.setDescription('MAC address identifying a peer STA.')
atkkWiAcClientSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 2), SsidString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientSSID.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClientSSID.setDescription('SSID to which the STA is associated.')
atkkWiAcClient80211Spec = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("dot11b", 2), ("dot11g", 3), ("dot11a", 4), ("dot11ng", 5), ("dot11na", 6), ("dot11ac", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClient80211Spec.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClient80211Spec.setDescription('802.11 technology which the STA is using.')
atkkWiAcClientChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientChannel.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClientChannel.setDescription('The radio channel which the STA is using.')
atkkWiAcClientAge = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientAge.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClientAge.setDescription('Time (in seconds) since the STA was associated.')
atkkWiAcClientUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 6), UserIdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientUserID.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcClientUserID.setDescription('UserID of the STA which is associated.')
atkkWiAcAPs = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3))
if mibBuilder.loadTexts: atkkWiAcAPs.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPs.setDescription('Neighboring APs List. \n         This list consists of entries which describe APs which is\n         found by the AP.')
atkkWiAcAPTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1), )
if mibBuilder.loadTexts: atkkWiAcAPTable.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPTable.setDescription('A table that contains information about APs\n         nearby.')
atkkWiAcAPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcAPAddress"))
if mibBuilder.loadTexts: atkkWiAcAPEntry.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPEntry.setDescription('Information about a neighboring AP.')
atkkWiAcAPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPAddress.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPAddress.setDescription('MAC address of the neighbor AP.')
atkkWiAcAPSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 2), SsidString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPSSID.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPSSID.setDescription('SSID of the neighbor AP.')
atkkWiAcAP80211Spec = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("dot11b", 2), ("dot11g", 3), ("dot11a", 4), ("dot11ng", 5), ("dot11na", 6), ("dot11ac", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAP80211Spec.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAP80211Spec.setDescription('802.11 technology which the neighbor AP is using.')
atkkWiAcAPChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPChannel.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPChannel.setDescription('The radio channel which the neighbor AP is using.')
atkkWiAcAPRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPRSSI.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPRSSI.setDescription('RSSI (signal strength) of the neighbor AP.')
atkkWiAcAPRadarDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 6), TrapString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPRadarDetected.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPRadarDetected.setDescription('The message of Radar Detected.')
atkkWiAcAPChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 7), ChannelString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPChannels.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPChannels.setDescription('The channels of Radar Detected.')
atkkWiAcAPDetectConfig = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atkkWiAcAPDetectConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPDetectConfig.setDescription('The enable/disable configuration of the Neighbor AP detection.\n         wlan0/wlan1 for TQ2403/EX\n         wlan0 for TQ2450/TQ3600/TQ3200/TQ3400/TQ4400/TQ4600/TQ4400e')
atkkWiAcAPDetectConfig2 = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atkkWiAcAPDetectConfig2.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAPDetectConfig2.setDescription('The enable/disable configuration of the Neighbor AP detection.\n         wlan1 for TQ2450/TQ3600/TQ3400/TQ4400/TQ4600/TQ4400e')
atkkWiAcMacACL = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4))
if mibBuilder.loadTexts: atkkWiAcMacACL.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcMacACL.setDescription('MAC address filters List.')
atkkWiAcMacACLTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1), )
if mibBuilder.loadTexts: atkkWiAcMacACLTable.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcMacACLTable.setDescription('A table that contains MAC address filters.')
atkkWiAcMacACLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcMacACLAddress"))
if mibBuilder.loadTexts: atkkWiAcMacACLEntry.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcMacACLEntry.setDescription('MAC address filter.')
atkkWiAcMacACLAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcMacACLAddress.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcMacACLAddress.setDescription('MAC address which is filtered.')
atkkWiAcMacACLModeConfig = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("accept", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atkkWiAcMacACLModeConfig.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcMacACLModeConfig.setDescription('The mode configuration of the MAC filtering.')
atkkWiAcNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5))
atkkWiAcNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0))
atkkWiAcAssociated = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 1)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcAssociated.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcAssociated.setDescription('This notification is sent when a STA was connected.')
atkkWiAcDisassociated = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 2)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcDisassociated.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcDisassociated.setDescription('This notification is sent when a STA was disconnected.')
atkkWiAcUnknownAP = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 3)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcAPAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcAP80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPRSSI"))
if mibBuilder.loadTexts: atkkWiAcUnknownAP.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcUnknownAP.setDescription('This notification is sent when an unknown AP was detected.')
atkkWiAcFiltered = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 4)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcFiltered.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcFiltered.setDescription('This notification is sent when an STA was denied by MAC filters.')
atkkWiAcRadiusAuthSucceeded = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 5)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcRadiusAuthSucceeded.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcRadiusAuthSucceeded.setDescription('This notification is sent when RADIUS authentication of \n              an STA succeeded.')
atkkWiAcRadiusAuthFailed = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 6)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcRadiusAuthFailed.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcRadiusAuthFailed.setDescription('This notification is sent when RADIUS authentication of \n              an STA failed.')
atkkWiAcRadarDetected = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 7)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcAPRadarDetected"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPChannels"))
if mibBuilder.loadTexts: atkkWiAcRadarDetected.setStatus('current')
if mibBuilder.loadTexts: atkkWiAcRadarDetected.setDescription('This notification is sent when Radar detected.')
mibBuilder.exportSymbols("ATKK-WLAN-ACCESS", atkkWiAcAPRSSI=atkkWiAcAPRSSI, atkkWiAcAPs=atkkWiAcAPs, atkkWiAcAPDetectConfig2=atkkWiAcAPDetectConfig2, UserIdString=UserIdString, tq3600=tq3600, tq3200=tq3200, atkkWiAcApTrapRadiusAuthSuccessConfig=atkkWiAcApTrapRadiusAuthSuccessConfig, atkkWiAcClients=atkkWiAcClients, atkkWiAcFiltered=atkkWiAcFiltered, atkkWiAcRadiusAuthFailed=atkkWiAcRadiusAuthFailed, atkkWiAcAPChannels=atkkWiAcAPChannels, ChannelString=ChannelString, atkkWiAcApTrapColdStartConfig=atkkWiAcApTrapColdStartConfig, atkkWiAcClientSSID=atkkWiAcClientSSID, atkkWiAcClientAge=atkkWiAcClientAge, atkkWiAcApInfo=atkkWiAcApInfo, atkkWiAcAPDetectConfig=atkkWiAcAPDetectConfig, atkkWiAcMacACLEntry=atkkWiAcMacACLEntry, atkkWiAcDisassociated=atkkWiAcDisassociated, atkkWiAcUnknownAP=atkkWiAcUnknownAP, atkkWiAcClientAddress=atkkWiAcClientAddress, atkkWiAcAPSSID=atkkWiAcAPSSID, atkkWiAcApInfoTrapTable=atkkWiAcApInfoTrapTable, tq4400=tq4400, atkkWiAcApTrapAuthenticationConfig=atkkWiAcApTrapAuthenticationConfig, atkkWiAcApTrapFilteredStaConfig=atkkWiAcApTrapFilteredStaConfig, tq2450=tq2450, atkkWiAcApTrapCommunity=atkkWiAcApTrapCommunity, atkkWiAcClientTable=atkkWiAcClientTable, atkkWiAcApTrapDfsDetectedConfig=atkkWiAcApTrapDfsDetectedConfig, atkkWiAcAPEntry=atkkWiAcAPEntry, atkkWiAcMacACLModeConfig=atkkWiAcMacACLModeConfig, atkkWiAcClient80211Spec=atkkWiAcClient80211Spec, atkkWiAcVersion=atkkWiAcVersion, PYSNMP_MODULE_ID=atkkWlanAccess, tq3400=tq3400, atkkWiAcAssociated=atkkWiAcAssociated, atkkWiAcApTrapAssociationConfig=atkkWiAcApTrapAssociationConfig, atkkWiAcApTrapHost=atkkWiAcApTrapHost, atkkWiAcRadarDetected=atkkWiAcRadarDetected, tq2403=tq2403, atkkWiAcApTrapLinkConfig=atkkWiAcApTrapLinkConfig, atkkWiAcClientChannel=atkkWiAcClientChannel, tq2403ex=tq2403ex, atkkWiAcMacACLTable=atkkWiAcMacACLTable, atkkWlanAccess=atkkWlanAccess, TrapString=TrapString, atkkWiAcAPRadarDetected=atkkWiAcAPRadarDetected, TrapHostString=TrapHostString, atkkWiAcMacACL=atkkWiAcMacACL, CommunityString=CommunityString, atkkWiAcApTrapRadiusAuthFailConfig=atkkWiAcApTrapRadiusAuthFailConfig, atkkWiAcAP80211Spec=atkkWiAcAP80211Spec, atkkWiAcNotification=atkkWiAcNotification, tq4600=tq4600, atkkWiAcAPTable=atkkWiAcAPTable, atkkWiAcClientEntry=atkkWiAcClientEntry, atkkWiAcRadiusAuthSucceeded=atkkWiAcRadiusAuthSucceeded, atkkWiAcApTrapUnknownApConfig=atkkWiAcApTrapUnknownApConfig, atkkWiAcClientUserID=atkkWiAcClientUserID, atkkWiAcAPChannel=atkkWiAcAPChannel, atkkWiAcNotificationObjects=atkkWiAcNotificationObjects, tq4400e=tq4400e, SsidString=SsidString, atkkWiAcApInfoTrapEntry=atkkWiAcApInfoTrapEntry, atkkWiAcMacACLAddress=atkkWiAcMacACLAddress, atkkWiAcAPAddress=atkkWiAcAPAddress)
