#
# PySNMP MIB module SIAE-EQUIPTYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIPTYPE-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 13:29:02 2023
# On host fv-az203-74 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, IpAddress, Integer32, Gauge32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, ModuleIdentity, NotificationType, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "IpAddress", "Integer32", "Gauge32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "ModuleIdentity", "NotificationType", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
equipTypeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 501))
equipTypeMib.setRevisions(('2015-04-23 00:00', '2014-10-29 00:00', '2014-06-23 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: equipTypeMib.setLastUpdated('201504230000Z')
if mibBuilder.loadTexts: equipTypeMib.setOrganization('SIAE MICROELETTRONICA spa')
equipTypeList = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5))
equipTypeUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 1))
if mibBuilder.loadTexts: equipTypeUnknown.setStatus('current')
equipTypeALFO80HD = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 74))
if mibBuilder.loadTexts: equipTypeALFO80HD.setStatus('current')
equipTypeALFO80HDsm = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 75))
if mibBuilder.loadTexts: equipTypeALFO80HDsm.setStatus('current')
equipTypeAGS20 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 76))
if mibBuilder.loadTexts: equipTypeAGS20.setStatus('current')
equipTypeALFOplus2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 77))
if mibBuilder.loadTexts: equipTypeALFOplus2.setStatus('current')
equipTypeEasyCellGateway = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 78))
if mibBuilder.loadTexts: equipTypeEasyCellGateway.setStatus('current')
mibBuilder.exportSymbols("SIAE-EQUIPTYPE-MIB", PYSNMP_MODULE_ID=equipTypeMib, equipTypeALFO80HDsm=equipTypeALFO80HDsm, equipTypeUnknown=equipTypeUnknown, equipTypeEasyCellGateway=equipTypeEasyCellGateway, equipTypeList=equipTypeList, equipTypeALFOplus2=equipTypeALFOplus2, equipTypeAGS20=equipTypeAGS20, equipTypeALFO80HD=equipTypeALFO80HD, equipTypeMib=equipTypeMib)
