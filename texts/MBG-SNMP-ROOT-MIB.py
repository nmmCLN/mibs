#
# PySNMP MIB module MBG-SNMP-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 10:12:12 2022
# On host fv-az377-643 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, MibIdentifier, enterprises, Bits, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, IpAddress, TimeTicks, ModuleIdentity, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibIdentifier", "enterprises", "Bits", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "ModuleIdentity", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mbgSnmpRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597))
mbgSnmpRoot.setRevisions(('2012-01-25 07:45', '2011-10-14 06:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mbgSnmpRoot.setRevisionsDescriptions((' Rev 1.01  25 January 2012 7:45 UTC Philipp Rahns\n          Changed MIB module name', ' Rev 1.00  14 October 2011 6:30 UTC Philipp Rahns\n          Initial revision',))
if mibBuilder.loadTexts: mbgSnmpRoot.setLastUpdated('201201250745Z')
if mibBuilder.loadTexts: mbgSnmpRoot.setOrganization('Meinberg Radio Clocks GmbH & Co. KG')
if mibBuilder.loadTexts: mbgSnmpRoot.setContactInfo('postal:   Meinberg Funkuhren\n                    Lange Wand 9\n                    31812 Bad Pyrmont\n                    Germany\n\n          email:    info@meinberg.de\n            web:    http://www.meinberg.de\n            tel:    +49 (0) 52 81 / 93 09 - 0\n            fax:    +49 (0) 52 81 / 93 09 - 30')
if mibBuilder.loadTexts: mbgSnmpRoot.setDescription(' Meinberg SNMP Management Information Root Base ')
class MeinbergSwitch(TextualConvention, Integer32):
    description = 'indicating whether something is actived or not => like a switch'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

mibBuilder.exportSymbols("MBG-SNMP-ROOT-MIB", mbgSnmpRoot=mbgSnmpRoot, PYSNMP_MODULE_ID=mbgSnmpRoot, MeinbergSwitch=MeinbergSwitch)
