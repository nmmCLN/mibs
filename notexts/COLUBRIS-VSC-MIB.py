#
# PySNMP MIB module COLUBRIS-VSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-VSC-MIB.my
# Produced by pysmi-1.1.8 at Mon Jan  9 10:31:12 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSID, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSID")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Bits, Unsigned32, MibIdentifier, Integer32, iso, Counter64, Counter32, NotificationType, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "iso", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
colubrisVscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 22))
if mibBuilder.loadTexts: colubrisVscMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisVscMIB.setOrganization('Colubris Networks, Inc.')
colubrisVscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1))
coVscConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1))
coVscConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1), )
if mibBuilder.loadTexts: coVscConfigTable.setStatus('current')
coVscConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-VSC-MIB", "coVscCfgIndex"))
if mibBuilder.loadTexts: coVscConfigEntry.setStatus('current')
coVscCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coVscCfgIndex.setStatus('current')
coVscCfgFriendlyVscName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgFriendlyVscName.setStatus('current')
coVscCfgSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 3), ColubrisSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSSID.setStatus('current')
coVscCfgAccessControlled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgAccessControlled.setStatus('current')
coVscCfgSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("ieee802dot1x", 2), ("wpa", 3), ("wpa2", 4), ("wpaAndWpa2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSecurity.setStatus('current')
coVscCfgEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4), ("tkipAndAes", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgEncryption.setStatus('current')
coVscCfg8021xAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("radius", 2), ("psk", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfg8021xAuthentication.setStatus('current')
coVscCfgMACAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgMACAuthentication.setStatus('current')
coVscCfgHTMLAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgHTMLAuthentication.setStatus('current')
colubrisVscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2))
colubrisVscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 1))
colubrisVscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 2))
colubrisVscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 1, 1)).setObjects(("COLUBRIS-VSC-MIB", "colubrisVscMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVscMIBCompliance = colubrisVscMIBCompliance.setStatus('current')
colubrisVscMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 2, 1)).setObjects(("COLUBRIS-VSC-MIB", "coVscCfgFriendlyVscName"), ("COLUBRIS-VSC-MIB", "coVscCfgSSID"), ("COLUBRIS-VSC-MIB", "coVscCfgAccessControlled"), ("COLUBRIS-VSC-MIB", "coVscCfgSecurity"), ("COLUBRIS-VSC-MIB", "coVscCfgEncryption"), ("COLUBRIS-VSC-MIB", "coVscCfg8021xAuthentication"), ("COLUBRIS-VSC-MIB", "coVscCfgMACAuthentication"), ("COLUBRIS-VSC-MIB", "coVscCfgHTMLAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVscMIBGroup = colubrisVscMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-VSC-MIB", coVscCfgHTMLAuthentication=coVscCfgHTMLAuthentication, colubrisVscMIBObjects=colubrisVscMIBObjects, coVscCfgIndex=coVscCfgIndex, coVscCfgSecurity=coVscCfgSecurity, coVscCfgMACAuthentication=coVscCfgMACAuthentication, coVscCfgAccessControlled=coVscCfgAccessControlled, coVscCfgFriendlyVscName=coVscCfgFriendlyVscName, coVscConfigEntry=coVscConfigEntry, coVscCfg8021xAuthentication=coVscCfg8021xAuthentication, colubrisVscMIB=colubrisVscMIB, colubrisVscMIBConformance=colubrisVscMIBConformance, PYSNMP_MODULE_ID=colubrisVscMIB, coVscCfgEncryption=coVscCfgEncryption, colubrisVscMIBGroup=colubrisVscMIBGroup, coVscCfgSSID=coVscCfgSSID, coVscConfigGroup=coVscConfigGroup, coVscConfigTable=coVscConfigTable, colubrisVscMIBGroups=colubrisVscMIBGroups, colubrisVscMIBCompliances=colubrisVscMIBCompliances, colubrisVscMIBCompliance=colubrisVscMIBCompliance)
