#
# PySNMP MIB module COLUBRIS-VSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-VSC-MIB.my
# Produced by pysmi-1.1.8 at Sat Jan 15 20:23:08 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSID, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSID")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Integer32, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, iso, Gauge32, NotificationType, Unsigned32, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "iso", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "ModuleIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
colubrisVscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 22))
if mibBuilder.loadTexts: colubrisVscMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisVscMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisVscMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisVscMIB.setDescription('Colubris Virtual Service Communities MIB.')
colubrisVscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1))
coVscConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1))
coVscConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1), )
if mibBuilder.loadTexts: coVscConfigTable.setStatus('current')
if mibBuilder.loadTexts: coVscConfigTable.setDescription('Virtual Service Communities configuration attributes.')
coVscConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-VSC-MIB", "coVscCfgIndex"))
if mibBuilder.loadTexts: coVscConfigEntry.setStatus('current')
if mibBuilder.loadTexts: coVscConfigEntry.setDescription('An entry in the coVscConfigTable.\n                 coVscCfgIndex - Uniquely identify a Virtual Service\n                                 Community on the MultiService Access\n                                 Controller.')
coVscCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coVscCfgIndex.setStatus('current')
if mibBuilder.loadTexts: coVscCfgIndex.setDescription('Specifies the index of a Virtual Service Community (VSC)\n                 in the MultiService Controller configuration file.')
coVscCfgFriendlyVscName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgFriendlyVscName.setStatus('current')
if mibBuilder.loadTexts: coVscCfgFriendlyVscName.setDescription('The friendly name associated with the VSC.')
coVscCfgSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 3), ColubrisSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSSID.setStatus('current')
if mibBuilder.loadTexts: coVscCfgSSID.setDescription('Service Set ID assigned to the VSC.')
coVscCfgAccessControlled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgAccessControlled.setStatus('current')
if mibBuilder.loadTexts: coVscCfgAccessControlled.setDescription('Indicates if the VSC is access controlled.')
coVscCfgSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("ieee802dot1x", 2), ("wpa", 3), ("wpa2", 4), ("wpaAndWpa2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSecurity.setStatus('current')
if mibBuilder.loadTexts: coVscCfgSecurity.setDescription('Indicates the type of security used by the VSC.')
coVscCfgEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4), ("tkipAndAes", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgEncryption.setStatus('current')
if mibBuilder.loadTexts: coVscCfgEncryption.setDescription('Indicates the encryption type supported by the VSC.')
coVscCfg8021xAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("radius", 2), ("psk", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfg8021xAuthentication.setStatus('current')
if mibBuilder.loadTexts: coVscCfg8021xAuthentication.setDescription('Indicates the 802.1x authentication type supported by the VSC.')
coVscCfgMACAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgMACAuthentication.setStatus('current')
if mibBuilder.loadTexts: coVscCfgMACAuthentication.setDescription('Indicates if MAC authentication is enabled on the VSC.')
coVscCfgHTMLAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgHTMLAuthentication.setStatus('current')
if mibBuilder.loadTexts: coVscCfgHTMLAuthentication.setDescription('Indicates if HTML authentication is enabled on the\n                 VSC. Always false on a satellite.')
colubrisVscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2))
colubrisVscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 1))
colubrisVscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 2))
colubrisVscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 1, 1)).setObjects(("COLUBRIS-VSC-MIB", "colubrisVscMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVscMIBCompliance = colubrisVscMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisVscMIBCompliance.setDescription('The compliance statement for the Virtual Service\n                 Communities MIB.')
colubrisVscMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 2, 1)).setObjects(("COLUBRIS-VSC-MIB", "coVscCfgFriendlyVscName"), ("COLUBRIS-VSC-MIB", "coVscCfgSSID"), ("COLUBRIS-VSC-MIB", "coVscCfgAccessControlled"), ("COLUBRIS-VSC-MIB", "coVscCfgSecurity"), ("COLUBRIS-VSC-MIB", "coVscCfgEncryption"), ("COLUBRIS-VSC-MIB", "coVscCfg8021xAuthentication"), ("COLUBRIS-VSC-MIB", "coVscCfgMACAuthentication"), ("COLUBRIS-VSC-MIB", "coVscCfgHTMLAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVscMIBGroup = colubrisVscMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisVscMIBGroup.setDescription('A collection of objects for the wireless interface\n                 status.')
mibBuilder.exportSymbols("COLUBRIS-VSC-MIB", colubrisVscMIBGroups=colubrisVscMIBGroups, coVscCfg8021xAuthentication=coVscCfg8021xAuthentication, colubrisVscMIBCompliances=colubrisVscMIBCompliances, coVscCfgAccessControlled=coVscCfgAccessControlled, coVscConfigEntry=coVscConfigEntry, PYSNMP_MODULE_ID=colubrisVscMIB, coVscConfigGroup=coVscConfigGroup, coVscCfgSSID=coVscCfgSSID, coVscCfgMACAuthentication=coVscCfgMACAuthentication, colubrisVscMIBConformance=colubrisVscMIBConformance, coVscConfigTable=coVscConfigTable, colubrisVscMIBCompliance=colubrisVscMIBCompliance, colubrisVscMIBObjects=colubrisVscMIBObjects, coVscCfgIndex=coVscCfgIndex, colubrisVscMIBGroup=colubrisVscMIBGroup, coVscCfgHTMLAuthentication=coVscCfgHTMLAuthentication, coVscCfgSecurity=coVscCfgSecurity, coVscCfgEncryption=coVscCfgEncryption, colubrisVscMIB=colubrisVscMIB, coVscCfgFriendlyVscName=coVscCfgFriendlyVscName)
