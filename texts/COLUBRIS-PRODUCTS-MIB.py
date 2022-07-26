#
# PySNMP MIB module COLUBRIS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-PRODUCTS-MIB.my
# Produced by pysmi-1.1.8 at Tue Jul 26 15:28:57 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
colubrisModules, colubrisProducts = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisModules", "colubrisProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, iso, IpAddress, MibIdentifier, Bits, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Integer32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "iso", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Integer32", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 4, 2))
if mibBuilder.loadTexts: colubrisProductsMIB.setLastUpdated('200709060000Z')
if mibBuilder.loadTexts: colubrisProductsMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisProductsMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisProductsMIB.setDescription('Colubris Networks Product Identifiers.')
colubrisCN1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 1))
colubrisCN1000HEREUARE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 2))
colubrisCN1050 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 3))
colubrisCN1054 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 4))
colubrisCN3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 5))
colubrisCN100HEREUARE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 6))
colubrisCN100TRAVELNET = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 7))
colubrisCN300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 8))
colubrisCN1150 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 9))
colubrisCN3100 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 10))
colubrisCN1000LIGHT = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 11))
colubrisCN3500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 12))
colubrisCN310 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 13))
colubrisCN1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 14))
colubrisCN1550 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 15))
colubrisCN3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 16))
colubrisCN1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 17))
colubrisCN1250 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 18))
colubrisCN320SE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 19))
colubrisCN320 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 20))
colubrisCN1220 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 21))
colubrisCN200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 22))
colubrisCN3300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 23))
colubrisCN330 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 24))
colubrisMSC5200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 25))
colubrisWCB200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 26))
colubrisMSC5500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 27))
colubrisMAP625 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 28))
colubrisMAP630 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 29))
colubrisMAP330SENSOR = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 32))
colubris1300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 33))
colubris1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 34))
colubrisMSC5100 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 35))
colubrisMSM410 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 41))
mibBuilder.exportSymbols("COLUBRIS-PRODUCTS-MIB", colubrisCN300=colubrisCN300, colubrisCN1250=colubrisCN1250, colubrisCN3500=colubrisCN3500, colubrisCN1054=colubrisCN1054, colubrisCN1000=colubrisCN1000, colubrisMAP630=colubrisMAP630, colubrisCN1050=colubrisCN1050, colubrisCN1500=colubrisCN1500, PYSNMP_MODULE_ID=colubrisProductsMIB, colubrisMSM410=colubrisMSM410, colubrisCN1000HEREUARE=colubrisCN1000HEREUARE, colubrisCN1000LIGHT=colubrisCN1000LIGHT, colubrisCN3000=colubrisCN3000, colubrisCN1200=colubrisCN1200, colubrisCN320SE=colubrisCN320SE, colubris1300=colubris1300, colubrisProductsMIB=colubrisProductsMIB, colubrisCN100HEREUARE=colubrisCN100HEREUARE, colubrisCN3100=colubrisCN3100, colubrisCN330=colubrisCN330, colubrisMAP625=colubrisMAP625, colubrisMSC5100=colubrisMSC5100, colubris1500=colubris1500, colubrisWCB200=colubrisWCB200, colubrisCN3200=colubrisCN3200, colubrisCN200=colubrisCN200, colubrisCN100TRAVELNET=colubrisCN100TRAVELNET, colubrisCN3300=colubrisCN3300, colubrisCN1550=colubrisCN1550, colubrisMAP330SENSOR=colubrisMAP330SENSOR, colubrisMSC5200=colubrisMSC5200, colubrisMSC5500=colubrisMSC5500, colubrisCN320=colubrisCN320, colubrisCN310=colubrisCN310, colubrisCN1150=colubrisCN1150, colubrisCN1220=colubrisCN1220)
