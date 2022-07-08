#
# PySNMP MIB module COLUBRIS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-PRODUCTS-MIB.my
# Produced by pysmi-1.1.8 at Fri Jul  8 09:20:26 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
colubrisProducts, colubrisModules = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisProducts", "colubrisModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Integer32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, iso, Counter32, MibIdentifier, Counter64, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "iso", "Counter32", "MibIdentifier", "Counter64", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 4, 2))
if mibBuilder.loadTexts: colubrisProductsMIB.setLastUpdated('200709060000Z')
if mibBuilder.loadTexts: colubrisProductsMIB.setOrganization('Colubris Networks, Inc.')
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
mibBuilder.exportSymbols("COLUBRIS-PRODUCTS-MIB", colubrisCN1000LIGHT=colubrisCN1000LIGHT, colubrisCN1054=colubrisCN1054, colubrisCN100HEREUARE=colubrisCN100HEREUARE, colubrisCN1000HEREUARE=colubrisCN1000HEREUARE, colubrisProductsMIB=colubrisProductsMIB, colubrisCN1050=colubrisCN1050, colubrisCN330=colubrisCN330, colubrisCN1200=colubrisCN1200, colubrisCN1550=colubrisCN1550, colubrisMSC5200=colubrisMSC5200, colubrisCN200=colubrisCN200, colubrisCN320=colubrisCN320, colubrisCN3200=colubrisCN3200, colubrisWCB200=colubrisWCB200, colubrisCN3100=colubrisCN3100, colubrisMAP630=colubrisMAP630, colubrisMSM410=colubrisMSM410, colubris1500=colubris1500, colubrisCN100TRAVELNET=colubrisCN100TRAVELNET, colubrisCN1500=colubrisCN1500, colubrisMAP625=colubrisMAP625, PYSNMP_MODULE_ID=colubrisProductsMIB, colubris1300=colubris1300, colubrisCN300=colubrisCN300, colubrisCN3500=colubrisCN3500, colubrisMSC5100=colubrisMSC5100, colubrisCN1000=colubrisCN1000, colubrisCN3300=colubrisCN3300, colubrisCN1150=colubrisCN1150, colubrisCN1250=colubrisCN1250, colubrisCN1220=colubrisCN1220, colubrisCN320SE=colubrisCN320SE, colubrisCN3000=colubrisCN3000, colubrisMSC5500=colubrisMSC5500, colubrisCN310=colubrisCN310, colubrisMAP330SENSOR=colubrisMAP330SENSOR)
