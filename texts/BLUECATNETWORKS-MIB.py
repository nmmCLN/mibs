#
# PySNMP MIB module BLUECATNETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BLUECATNETWORKS-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:23:59 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, enterprises, ModuleIdentity, Counter32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, TimeTicks, iso, ObjectIdentity, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "enterprises", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "TimeTicks", "iso", "ObjectIdentity", "IpAddress", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecatnetworksId = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 1))
bluecatnetworksId.setRevisions(('2010-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecatnetworksId.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bluecatnetworksId.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bluecatnetworksId.setOrganization('BlueCat Networks Inc.')
if mibBuilder.loadTexts: bluecatnetworksId.setContactInfo('BlueCat Networks Inc.\n\t\t \n\t\t Tel: +1 866 491 2228 (toll free)\n\t\t      +1 416 646 8400 (international) \n\t\t Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bluecatnetworksId.setDescription('New oid assignments for Cisco REPEATER MIB and others.')
bluecatnetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 13315))
appliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100))
mibBuilder.exportSymbols("BLUECATNETWORKS-MIB", bluecatnetworks=bluecatnetworks, appliances=appliances, PYSNMP_MODULE_ID=bluecatnetworksId, bluecatnetworksId=bluecatnetworksId)
