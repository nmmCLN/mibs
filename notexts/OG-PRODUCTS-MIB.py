#
# PySNMP MIB module OG-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:13:31 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ogProducts, ogModules = mibBuilder.importSymbols("OG-SMI-MIB", "ogProducts", "ogModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Counter64, NotificationType, iso, ObjectIdentity, ModuleIdentity, Bits, TimeTicks, Unsigned32, IpAddress, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Counter64", "NotificationType", "iso", "ObjectIdentity", "ModuleIdentity", "Bits", "TimeTicks", "Unsigned32", "IpAddress", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogProductsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 11, 2))
ogProductsMib.setRevisions(('2018-06-15 00:00', '2016-06-27 00:00', '2016-02-10 00:00', '2015-06-02 00:00', '2013-08-11 00:00', '2011-08-15 01:23', '2010-04-15 11:27',))
if mibBuilder.loadTexts: ogProductsMib.setLastUpdated('201806150000Z')
if mibBuilder.loadTexts: ogProductsMib.setOrganization('Opengear Inc.')
ogCM4001 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 1))
ogCM4002 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 2))
ogCM4008 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 3))
ogCM41xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 10))
ogCM71xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 11))
ogCM7196 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 12))
ogSD4001 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 20))
ogSD4002 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 21))
ogSD4008 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 22))
ogSD4001DW = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 23))
ogSD4002DX = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 24))
ogCD = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 30))
ogCMx86 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 31))
ogCMS61xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 40))
ogLighthouse = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 41))
ogLighthouse5 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 42))
ogIM4004 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 50))
ogIM42xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 60))
ogIM72xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 61))
ogKCS61xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 70))
ogACM500x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 80))
ogACM550x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 81))
ogACM700x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 90))
ogACM70045 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 91))
mibBuilder.exportSymbols("OG-PRODUCTS-MIB", ogCM4002=ogCM4002, ogACM70045=ogACM70045, ogSD4001=ogSD4001, ogIM42xx=ogIM42xx, ogCM71xx=ogCM71xx, ogSD4002=ogSD4002, ogCM4008=ogCM4008, ogIM4004=ogIM4004, ogLighthouse=ogLighthouse, ogCD=ogCD, ogLighthouse5=ogLighthouse5, ogACM700x=ogACM700x, ogIM72xx=ogIM72xx, ogCM41xx=ogCM41xx, PYSNMP_MODULE_ID=ogProductsMib, ogCMS61xx=ogCMS61xx, ogACM500x=ogACM500x, ogKCS61xx=ogKCS61xx, ogCMx86=ogCMx86, ogSD4008=ogSD4008, ogACM550x=ogACM550x, ogSD4001DW=ogSD4001DW, ogSD4002DX=ogSD4002DX, ogCM7196=ogCM7196, ogCM4001=ogCM4001, ogProductsMib=ogProductsMib)
