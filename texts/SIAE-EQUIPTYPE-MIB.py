#
# PySNMP MIB module SIAE-EQUIPTYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIPTYPE-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:18 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, Bits, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Gauge32, Counter32, iso, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Bits", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Gauge32", "Counter32", "iso", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
equipTypeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 501))
equipTypeMib.setRevisions(('2015-04-23 00:00', '2014-10-29 00:00', '2014-06-23 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: equipTypeMib.setRevisionsDescriptions(('Added equipTypeEasyCellGateway (78).\n            ', 'Added equipTypeALFOplus2 (77).\n            ', 'Fixed IMPORTS clause.\n            ', 'Initial version\n            ',))
if mibBuilder.loadTexts: equipTypeMib.setLastUpdated('201504230000Z')
if mibBuilder.loadTexts: equipTypeMib.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: equipTypeMib.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: equipTypeMib.setDescription("Types of SIAE's equipment.\n            ")
equipTypeList = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5))
equipTypeUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 1))
if mibBuilder.loadTexts: equipTypeUnknown.setStatus('current')
if mibBuilder.loadTexts: equipTypeUnknown.setDescription('Unrecognized equip type')
if mibBuilder.loadTexts: equipTypeUnknown.setReference('None')
equipTypeALFO80HD = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 74))
if mibBuilder.loadTexts: equipTypeALFO80HD.setStatus('current')
if mibBuilder.loadTexts: equipTypeALFO80HD.setDescription('ALFO 80GHz HD')
if mibBuilder.loadTexts: equipTypeALFO80HD.setReference('None')
equipTypeALFO80HDsm = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 75))
if mibBuilder.loadTexts: equipTypeALFO80HDsm.setStatus('current')
if mibBuilder.loadTexts: equipTypeALFO80HDsm.setDescription('ALFO 80GHz HD Split Mount')
if mibBuilder.loadTexts: equipTypeALFO80HDsm.setReference('None')
equipTypeAGS20 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 76))
if mibBuilder.loadTexts: equipTypeAGS20.setStatus('current')
if mibBuilder.loadTexts: equipTypeAGS20.setDescription('AGS20')
if mibBuilder.loadTexts: equipTypeAGS20.setReference('None')
equipTypeALFOplus2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 77))
if mibBuilder.loadTexts: equipTypeALFOplus2.setStatus('current')
if mibBuilder.loadTexts: equipTypeALFOplus2.setDescription('AGS20')
if mibBuilder.loadTexts: equipTypeALFOplus2.setReference('None')
equipTypeEasyCellGateway = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 78))
if mibBuilder.loadTexts: equipTypeEasyCellGateway.setStatus('current')
if mibBuilder.loadTexts: equipTypeEasyCellGateway.setDescription('EasyCellGateway')
if mibBuilder.loadTexts: equipTypeEasyCellGateway.setReference('None')
mibBuilder.exportSymbols("SIAE-EQUIPTYPE-MIB", PYSNMP_MODULE_ID=equipTypeMib, equipTypeMib=equipTypeMib, equipTypeAGS20=equipTypeAGS20, equipTypeUnknown=equipTypeUnknown, equipTypeALFO80HDsm=equipTypeALFO80HDsm, equipTypeEasyCellGateway=equipTypeEasyCellGateway, equipTypeALFO80HD=equipTypeALFO80HD, equipTypeALFOplus2=equipTypeALFOplus2, equipTypeList=equipTypeList)
