#
# PySNMP MIB module IANA-ADDRESS-FAMILY-NUMBERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-ADDRESS-FAMILY-NUMBERS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:13:46 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, IpAddress, NotificationType, Counter64, Bits, ModuleIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, mib_2, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "Counter64", "Bits", "ModuleIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "mib-2", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72))
ianaAddressFamilyNumbers.setRevisions(('2014-09-02 00:00', '2013-09-25 00:00', '2013-07-16 00:00', '2013-06-26 00:00', '2013-06-18 00:00', '2002-03-14 00:00', '2000-09-08 00:00', '2000-03-01 00:00', '2000-02-04 00:00', '1999-08-26 00:00',))
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setLastUpdated('201409020000Z')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setOrganization('IANA')
class AddressFamilyNumbers(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 65535))
    namedValues = NamedValues(("other", 0), ("ipV4", 1), ("ipV6", 2), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("e163", 7), ("e164", 8), ("f69", 9), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("afi", 25), ("mplsTpSectionEndpointIdentifier", 26), ("mplsTpLspEndpointIdentifier", 27), ("mplsTpPseudowireEndpointIdentifier", 28), ("eigrpCommonServiceFamily", 16384), ("eigrpIpv4ServiceFamily", 16385), ("eigrpIpv6ServiceFamily", 16386), ("lispCanonicalAddressFormat", 16387), ("bgpLs", 16388), ("fortyeightBitMac", 16389), ("sixtyfourBitMac", 16390), ("oui", 16391), ("mac24", 16392), ("mac40", 16393), ("ipv664", 16394), ("rBridgePortID", 16395), ("trillNickname", 16396), ("reserved", 65535))

mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", ianaAddressFamilyNumbers=ianaAddressFamilyNumbers, PYSNMP_MODULE_ID=ianaAddressFamilyNumbers, AddressFamilyNumbers=AddressFamilyNumbers)
