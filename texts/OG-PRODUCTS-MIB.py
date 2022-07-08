#
# PySNMP MIB module OG-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:40 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ogModules, ogProducts = mibBuilder.importSymbols("OG-SMI-MIB", "ogModules", "ogProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, TimeTicks, Counter64, iso, Bits, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter64", "iso", "Bits", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("OG-PRODUCTS-MIB", ogCM71xx=ogCM71xx, ogCM4008=ogCM4008, ogSD4001DW=ogSD4001DW, ogCM4001=ogCM4001, ogACM500x=ogACM500x, ogCM4002=ogCM4002, ogACM70045=ogACM70045, ogACM700x=ogACM700x, ogSD4002=ogSD4002, ogCMx86=ogCMx86, ogLighthouse=ogLighthouse, ogCM41xx=ogCM41xx, ogLighthouse5=ogLighthouse5, PYSNMP_MODULE_ID=ogProductsMib, ogSD4001=ogSD4001, ogSD4008=ogSD4008, ogCD=ogCD, ogSD4002DX=ogSD4002DX, ogIM42xx=ogIM42xx, ogKCS61xx=ogKCS61xx, ogIM4004=ogIM4004, ogProductsMib=ogProductsMib, ogIM72xx=ogIM72xx, ogACM550x=ogACM550x, ogCMS61xx=ogCMS61xx, ogCM7196=ogCM7196)
