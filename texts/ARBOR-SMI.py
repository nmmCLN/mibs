#
# PySNMP MIB module ARBOR-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-SMI
# Produced by pysmi-1.1.8 at Thu Sep 15 09:59:40 2022
# On host fv-az377-643 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32, enterprises, ObjectIdentity, ModuleIdentity, iso, Integer32, IpAddress, Counter64, NotificationType, MibIdentifier, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32", "enterprises", "ObjectIdentity", "ModuleIdentity", "iso", "Integer32", "IpAddress", "Counter64", "NotificationType", "MibIdentifier", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ARBOR-SMI", arbornetworksProducts=arbornetworksProducts, arbornetworks=arbornetworks, PYSNMP_MODULE_ID=arbornetworks, arborExperimental=arborExperimental)
