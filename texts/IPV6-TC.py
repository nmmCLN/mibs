#
# PySNMP MIB module IPV6-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IPV6-TC
# Produced by pysmi-1.1.12 at Thu Apr  4 09:20:33 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, Counter32, Integer32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Bits, IpAddress, NotificationType, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Counter32", "Integer32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Bits", "IpAddress", "NotificationType", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses.\n                This is a binary string of 16 octets in network\n                byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class Ipv6AddressPrefix(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 address\n               prefixes. This is a binary string of up to 16\n               octets in network byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 address\n               interface identifiers. This is a binary string\n                of up to 8 octets in network byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class Ipv6IfIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero for each\n               internetwork-layer interface in the managed\n               system. It is recommended that values are assigned\n               contiguously starting from 1. The value for each\n               internetwork-layer interface must remain constant\n               at least from one re-initialization of the entity's\n               network management system to the next\n               re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the\n                 Ipv6IfIndex convention.  The latter defines\n                 a greater than zero value used to identify an IPv6\n                 interface in the managed system.  This extension\n                 permits the additional value of zero.  The value\n                 zero is object-specific and must therefore be\n                 defined as part of the description of any object\n                 which uses this syntax.  Examples of the usage of\n                 zero might include situations where interface was\n                 unknown, or when none or all interfaces need to be\n                 referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("IPV6-TC", Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero, Ipv6Address=Ipv6Address, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier, Ipv6IfIndex=Ipv6IfIndex)
