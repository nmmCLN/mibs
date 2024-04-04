#
# PySNMP MIB module COLUBRIS-VIRTUAL-AP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-VIRTUAL-AP-MIB.my
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:56 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSecurity, ColubrisUsersAuthenticationMode, ColubrisProfileIndexOrZero, ColubrisSSID, ColubrisPriorityQueue = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSecurity", "ColubrisUsersAuthenticationMode", "ColubrisProfileIndexOrZero", "ColubrisSSID", "ColubrisPriorityQueue")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, MibIdentifier, ModuleIdentity, IpAddress, Counter32, Counter64, Gauge32, NotificationType, Integer32, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "Gauge32", "NotificationType", "Integer32", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
colubrisVirtualApMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 11))
if mibBuilder.loadTexts: colubrisVirtualApMIB.setLastUpdated('200607250000Z')
if mibBuilder.loadTexts: colubrisVirtualApMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisVirtualApMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisVirtualApMIB.setDescription('Colubris Networks Virtual Access Point MIB.')
colubrisVirtualApMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1))
coVirtualApConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1))
coVirtualAccessPointConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1), )
if mibBuilder.loadTexts: coVirtualAccessPointConfigTable.setStatus('current')
if mibBuilder.loadTexts: coVirtualAccessPointConfigTable.setDescription('VSC  configuration attributes. In tabular form to\n                 allow for multiple instances.')
coVirtualAccessPointConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApWlanProfileIndex"))
if mibBuilder.loadTexts: coVirtualAccessPointConfigEntry.setStatus('current')
if mibBuilder.loadTexts: coVirtualAccessPointConfigEntry.setDescription('An entry in the coVirtualAccessPointConfigTable.\n                 ifIndex - Each 802.11 interface is represented by an ifEntry.\n                           Interface tables in this MIB module are indexed by\n                           ifIndex.\n                 coVirtualWlanProfileIndex - Uniquely access a profile for this\n                                             particular 802.11 interface.')
coVirtualApWlanProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coVirtualApWlanProfileIndex.setStatus('current')
if mibBuilder.loadTexts: coVirtualApWlanProfileIndex.setDescription('Specifies the index of the VSC profile.')
coVirtualApSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 2), ColubrisSSID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApSSID.setStatus('current')
if mibBuilder.loadTexts: coVirtualApSSID.setDescription('Service Set ID assigned to the VSC. This value must be \n                 unique per radio interface.')
coVirtualApBroadcastSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApBroadcastSSID.setStatus('current')
if mibBuilder.loadTexts: coVirtualApBroadcastSSID.setDescription("Specifies if the SSID is included in beacon frames.\n                 On Intersil hardware, only the first profile is\n                 manageable. Reading this attribute shall always return\n                 'false' for the other profiles. Writing into this attribute\n                 for the other profiles will return an error.")
coVirtualApMaximumNumberOfUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApMaximumNumberOfUsers.setStatus('current')
if mibBuilder.loadTexts: coVirtualApMaximumNumberOfUsers.setDescription('Specifies the maximum number of concurrent users that this\n                 profile can accept.')
coVirtualApDefaultVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApDefaultVLAN.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultVLAN.setDescription('Specifies the default VLAN to use for this profile\n                 when no radius authentication has taken place.\n                 The value 0 is used when no VLAN has been assigned to this \n                 profile. Writing to this object is only available on\n                 satellite devices.')
coVirtualApSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 6), ColubrisSecurity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApSecurity.setStatus('current')
if mibBuilder.loadTexts: coVirtualApSecurity.setDescription('Identifies all supported authentication/encryption algorithms.')
coVirtualApAuthenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 7), ColubrisUsersAuthenticationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApAuthenMode.setStatus('current')
if mibBuilder.loadTexts: coVirtualApAuthenMode.setDescription('Specifies if user authentication is performed locally or via\n                 an AAA server.')
coVirtualApAuthenProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 8), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApAuthenProfileIndex.setStatus('current')
if mibBuilder.loadTexts: coVirtualApAuthenProfileIndex.setDescription("Specifies the AAA server profile to use for user authentication. \n                 This parameter only applies when the coVirtualApSecurity\n                 is set to 'wpa' or 'ieee802dot1x' or 'ieee802dot1xWithWep' and\n                 the coVirtualApAuthenMode set to 'profile' or\n                 'localAndProfile'. When set to Zero, no AAA server profile \n                 is selected or on a public satellite device it could represent\n                 a pre-configured AAA profile.")
coVirtualApUserAccountingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApUserAccountingEnabled.setStatus('current')
if mibBuilder.loadTexts: coVirtualApUserAccountingEnabled.setDescription('Indicates if accounting information is generated by the\n                 device and sent to the AAA server for users connecting to\n                 this profile. Accounting information will be generated only \n                 if a valid AAA server profile is configured for the\n                 coVirtualApAccountingProfileIndex attribute.')
coVirtualApUserAccountingProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 10), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApUserAccountingProfileIndex.setStatus('current')
if mibBuilder.loadTexts: coVirtualApUserAccountingProfileIndex.setDescription('Identifies the AAA server profile to be used for accounting\n                 information. The special value Zero indicates that no accounting\n                 profile is selected.')
coVirtualApDefaultUserRateLimitationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserRateLimitationEnabled.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserRateLimitationEnabled.setDescription('Indicates if the default user rate limitation is enabled.')
coVirtualApDefaultUserMaxTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxTransmitRate.setDescription('Identifies the default user maximum transmit rate.')
coVirtualApDefaultUserMaxReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxReceiveRate.setDescription('Identifies the default user maximum receive rate.')
coVirtualApDefaultUserBandwidthLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 14), ColubrisPriorityQueue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserBandwidthLevel.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserBandwidthLevel.setDescription('Identifies the default user bandwidth level.')
coVirtualApOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApOperState.setStatus('current')
if mibBuilder.loadTexts: coVirtualApOperState.setDescription('Activate/Deactivate the Virtual Service Community in\n                 the radio.')
colubrisVirtualApMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2))
colubrisVirtualApMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 1))
colubrisVirtualApMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 2))
colubrisVirtualApMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 1, 1)).setObjects(("COLUBRIS-VIRTUAL-AP-MIB", "colubrisVirtualApMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVirtualApMIBCompliance = colubrisVirtualApMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisVirtualApMIBCompliance.setDescription('The compliance statement for the Virtual Access Point MIB.')
colubrisVirtualApMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 2, 1)).setObjects(("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApSSID"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApBroadcastSSID"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApMaximumNumberOfUsers"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultVLAN"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApSecurity"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApAuthenMode"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApAuthenProfileIndex"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApUserAccountingEnabled"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApUserAccountingProfileIndex"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserRateLimitationEnabled"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserMaxTransmitRate"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserMaxReceiveRate"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserBandwidthLevel"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVirtualApMIBGroup = colubrisVirtualApMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisVirtualApMIBGroup.setDescription('A collection of objects for use with Virtual Access Points.')
mibBuilder.exportSymbols("COLUBRIS-VIRTUAL-AP-MIB", coVirtualApAuthenMode=coVirtualApAuthenMode, coVirtualApBroadcastSSID=coVirtualApBroadcastSSID, colubrisVirtualApMIBCompliances=colubrisVirtualApMIBCompliances, colubrisVirtualApMIBObjects=colubrisVirtualApMIBObjects, coVirtualApSSID=coVirtualApSSID, coVirtualApAuthenProfileIndex=coVirtualApAuthenProfileIndex, coVirtualApDefaultUserMaxTransmitRate=coVirtualApDefaultUserMaxTransmitRate, coVirtualAccessPointConfigEntry=coVirtualAccessPointConfigEntry, colubrisVirtualApMIBCompliance=colubrisVirtualApMIBCompliance, coVirtualApConfig=coVirtualApConfig, coVirtualApDefaultUserRateLimitationEnabled=coVirtualApDefaultUserRateLimitationEnabled, coVirtualApDefaultUserBandwidthLevel=coVirtualApDefaultUserBandwidthLevel, coVirtualApWlanProfileIndex=coVirtualApWlanProfileIndex, coVirtualApUserAccountingEnabled=coVirtualApUserAccountingEnabled, coVirtualApMaximumNumberOfUsers=coVirtualApMaximumNumberOfUsers, PYSNMP_MODULE_ID=colubrisVirtualApMIB, colubrisVirtualApMIBGroup=colubrisVirtualApMIBGroup, coVirtualApUserAccountingProfileIndex=coVirtualApUserAccountingProfileIndex, colubrisVirtualApMIBConformance=colubrisVirtualApMIBConformance, coVirtualApSecurity=coVirtualApSecurity, coVirtualApDefaultVLAN=coVirtualApDefaultVLAN, colubrisVirtualApMIBGroups=colubrisVirtualApMIBGroups, coVirtualApDefaultUserMaxReceiveRate=coVirtualApDefaultUserMaxReceiveRate, coVirtualApOperState=coVirtualApOperState, coVirtualAccessPointConfigTable=coVirtualAccessPointConfigTable, colubrisVirtualApMIB=colubrisVirtualApMIB)
