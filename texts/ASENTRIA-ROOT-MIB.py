#
# PySNMP MIB module ASENTRIA-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/asentria/ASENTRIA-ROOT-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:21:12 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, NotificationType, TimeTicks, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, enterprises, Counter32, Counter64, iso, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "NotificationType", "TimeTicks", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "enterprises", "Counter32", "Counter64", "iso", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
asentria = ModuleIdentity((1, 3, 6, 1, 4, 1, 3052))
asentria.setRevisions(('2010-03-09 00:00', '2007-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: asentria.setRevisionsDescriptions(('Updated CONTACT-INFO comment.', 'Asentria root MIB module',))
if mibBuilder.loadTexts: asentria.setLastUpdated('201003090000Z')
if mibBuilder.loadTexts: asentria.setOrganization('Asentria Corporation')
if mibBuilder.loadTexts: asentria.setContactInfo('Phone:  206-344-8800\n      Fax:    206-344-2116\n      Email:  support@asentria.com')
if mibBuilder.loadTexts: asentria.setDescription('Asentria root MIB module')
mibBuilder.exportSymbols("ASENTRIA-ROOT-MIB", asentria=asentria, PYSNMP_MODULE_ID=asentria)
