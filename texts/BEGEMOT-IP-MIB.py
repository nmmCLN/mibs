#
# PySNMP MIB module BEGEMOT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-IP-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 09:17:58 2022
# On host fv-az343-490 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Unsigned32, Counter64, iso, TimeTicks, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Unsigned32", "Counter64", "iso", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3))
if mibBuilder.loadTexts: begemotIp.setLastUpdated('200602130000Z')
if mibBuilder.loadTexts: begemotIp.setOrganization('German Aerospace Center')
if mibBuilder.loadTexts: begemotIp.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tGerman Aerospace Center\n\t\t\tOberpfaffenhofen\n\t\t\t82234 Wessling\n\t\t\tGermany\n\n\t     Fax:\t+49 8153 28 2843\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotIp.setDescription('The MIB for IP stuff that is not in the official IP MIBs.')
begemotIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
mibBuilder.exportSymbols("BEGEMOT-IP-MIB", begemotIpObjects=begemotIpObjects, PYSNMP_MODULE_ID=begemotIp, begemotIp=begemotIp)
