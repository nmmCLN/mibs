#
# PySNMP MIB module OG-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:30 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ogProducts, ogModules = mibBuilder.importSymbols("OG-SMI-MIB", "ogProducts", "ogModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Bits, ModuleIdentity, Counter32, iso, Counter64, NotificationType, Unsigned32, ObjectIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Bits", "ModuleIdentity", "Counter32", "iso", "Counter64", "NotificationType", "Unsigned32", "ObjectIdentity", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogProductsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 11, 2))
ogProductsMib.setRevisions(('2018-06-15 00:00', '2016-06-27 00:00', '2016-02-10 00:00', '2015-06-02 00:00', '2013-08-11 00:00', '2011-08-15 01:23', '2010-04-15 11:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogProductsMib.setRevisionsDescriptions(('Add Lighthouse 5 target to the MIB.', 'Add CM7196 target to the MIB.', 'Add CM71xx target to the MIB.', 'Add ACM700x target to the MIB.', 'Renamed from OPENGEAR-PRODUCTS-MIB to OG-PRODUCTS-MIB to\n\t\tfix naming discrepancy.', 'Add ACM550x target to the MIB.', 'Initial version.',))
if mibBuilder.loadTexts: ogProductsMib.setLastUpdated('201806150000Z')
if mibBuilder.loadTexts: ogProductsMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogProductsMib.setContactInfo('Opengear Inc.\n\t\t 630 West 9560 South,\n\t\t Sandy, UT 84070\n\t\t support@opengear.com')
if mibBuilder.loadTexts: ogProductsMib.setDescription('Opengear Product MIB')
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
mibBuilder.exportSymbols("OG-PRODUCTS-MIB", ogCD=ogCD, ogSD4008=ogSD4008, ogIM42xx=ogIM42xx, ogCM4008=ogCM4008, ogACM500x=ogACM500x, ogLighthouse5=ogLighthouse5, PYSNMP_MODULE_ID=ogProductsMib, ogCM4002=ogCM4002, ogIM72xx=ogIM72xx, ogCMS61xx=ogCMS61xx, ogCM7196=ogCM7196, ogCMx86=ogCMx86, ogKCS61xx=ogKCS61xx, ogCM41xx=ogCM41xx, ogCM4001=ogCM4001, ogACM700x=ogACM700x, ogACM550x=ogACM550x, ogSD4001DW=ogSD4001DW, ogSD4002=ogSD4002, ogCM71xx=ogCM71xx, ogLighthouse=ogLighthouse, ogSD4001=ogSD4001, ogACM70045=ogACM70045, ogProductsMib=ogProductsMib, ogIM4004=ogIM4004, ogSD4002DX=ogSD4002DX)
