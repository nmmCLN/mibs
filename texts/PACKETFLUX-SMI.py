#
# PySNMP MIB module PACKETFLUX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-SMI
# Produced by pysmi-1.1.8 at Wed Sep  6 13:36:19 2023
# On host fv-az361-883 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, enterprises, iso, Counter32, TimeTicks, ObjectIdentity, Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "enterprises", "iso", "Counter32", "TimeTicks", "ObjectIdentity", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
packetflux = ModuleIdentity((1, 3, 6, 1, 4, 1, 32050))
packetflux.setRevisions(('2013-06-04 16:31', '2013-06-04 21:58',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: packetflux.setRevisionsDescriptions(('initial version of this module', 'Correct MIB ID',))
if mibBuilder.loadTexts: packetflux.setLastUpdated('201306041631Z')
if mibBuilder.loadTexts: packetflux.setOrganization('PacketFlux Technologies')
if mibBuilder.loadTexts: packetflux.setContactInfo('custsvc@packetflux.com    \n                            http://www.packetflux.com')
if mibBuilder.loadTexts: packetflux.setDescription('SMI MIB for PacketFlux Technologies')
packetfluxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 1))
if mibBuilder.loadTexts: packetfluxProducts.setStatus('current')
if mibBuilder.loadTexts: packetfluxProducts.setDescription('packetfluxProducts is the root OBJECT IDENTIFIER\n                            for products released by packetflux technologies.')
packetfluxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 32050, 2))
if mibBuilder.loadTexts: packetfluxMgmt.setStatus('current')
if mibBuilder.loadTexts: packetfluxMgmt.setDescription('This is the main subtree for all packetflux product\n                            management mibs.')
mibBuilder.exportSymbols("PACKETFLUX-SMI", packetfluxMgmt=packetfluxMgmt, packetflux=packetflux, PYSNMP_MODULE_ID=packetflux, packetfluxProducts=packetfluxProducts)
