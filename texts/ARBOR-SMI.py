#
# PySNMP MIB module ARBOR-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-SMI
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:56 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Unsigned32, IpAddress, MibIdentifier, enterprises, Integer32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, iso, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "enterprises", "Integer32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "iso", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arbornetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 9694))
arbornetworks.setRevisions(('2013-11-14 00:00', '2013-08-19 00:00', '2011-07-20 00:00', '2009-03-30 00:00', '2008-11-13 00:00', '2005-09-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arbornetworks.setRevisionsDescriptions(('Add peakflowMobile product.', 'Updated contact information', 'Added pravail productid.', 'Update contact group name.', 'Update company address. Add arborExperimental.', 'Apply fixes from validation.',))
if mibBuilder.loadTexts: arbornetworks.setLastUpdated('201311140000Z')
if mibBuilder.loadTexts: arbornetworks.setOrganization('Arbor Networks, Inc.')
if mibBuilder.loadTexts: arbornetworks.setContactInfo('\tArbor Networks, Inc.\n\t\t\t\tArbor Technical Assistance Center\n\n\t\t\t\tPostal: 76 Blanchard Road\n\t\t\t\t\tBurlington, MA 01803\n\t\t\t\t\tUSA\n\n\t\t\t\tTel: +1 866 212 7267 (toll free)\n\t\t\t\t     +1 781 362 4300\n\t\t\t\tEmail: support@arbor.net ')
if mibBuilder.loadTexts: arbornetworks.setDescription('The Structure of Management Information for the\n\t\tArbor Networks enterprise.')
arbornetworksProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 1))
if mibBuilder.loadTexts: arbornetworksProducts.setStatus('current')
if mibBuilder.loadTexts: arbornetworksProducts.setDescription('arbornetworksProducts provides a root object identifier\n\t\tfrom which MODULE-IDENTITY values may be assigned.')
arborExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 2))
if mibBuilder.loadTexts: arborExperimental.setStatus('current')
if mibBuilder.loadTexts: arborExperimental.setDescription('arborExperimental provides a root object identifier\n\t\t from which MODULE-IDENTITY for experimental purposes\n\t\t may be assigned.')
mibBuilder.exportSymbols("ARBOR-SMI", arbornetworksProducts=arbornetworksProducts, PYSNMP_MODULE_ID=arbornetworks, arborExperimental=arborExperimental, arbornetworks=arbornetworks)
