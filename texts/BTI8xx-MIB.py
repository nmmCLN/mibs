#
# PySNMP MIB module BTI8xx-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:33:44 2022
# On host fv-az299-344 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, Counter32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, enterprises, Counter64, Bits, TimeTicks, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Counter32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso", "enterprises", "Counter64", "Bits", "TimeTicks", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bti8xx = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7))
bti8xx.setRevisions(('2013-12-26 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bti8xx.setRevisionsDescriptions(('Initial version of MIB.',))
if mibBuilder.loadTexts: bti8xx.setLastUpdated('201312261200Z')
if mibBuilder.loadTexts: bti8xx.setOrganization('Actus Networks Inc.')
if mibBuilder.loadTexts: bti8xx.setContactInfo('Technical Support\n\t\t ')
if mibBuilder.loadTexts: bti8xx.setDescription('This is a top-level MIB for BTI800 whose purpose is to lay out\n                  the top-level objects in the OID hierarchy from which\n                  BTI MIB OIDs descend.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 30005))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1))
mibBuilder.exportSymbols("BTI8xx-MIB", btiProducts=btiProducts, btiSystems=btiSystems, bti8xx=bti8xx, PYSNMP_MODULE_ID=bti8xx)
