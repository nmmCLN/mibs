#
# PySNMP MIB module ARISTA-BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-BGP4V2-TC-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 15:46:55 2022
# On host fv-az267-189 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
aristaExperiment, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaExperiment")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ModuleIdentity, Counter64, TimeTicks, Counter32, Integer32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ModuleIdentity", "Counter64", "TimeTicks", "Counter32", "Integer32", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaBgp4V2TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 4, 2))
aristaBgp4V2TC.setRevisions(('2014-08-15 00:00', '2012-10-19 00:00', '2011-01-17 00:00',))
if mibBuilder.loadTexts: aristaBgp4V2TC.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaBgp4V2TC.setOrganization('Arista Networks, Inc.')
class AristaBgp4V2IdentifierTC(TextualConvention, OctetString):
    reference = 'RFC 4273, Section 4.2'
    status = 'current'
    displayHint = '1d.'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class AristaBgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class AristaBgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3. The value of this object should be restricted to be between the values of 0 and 255.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("mpls", 4))

mibBuilder.exportSymbols("ARISTA-BGP4V2-TC-MIB", AristaBgp4V2SubsequentAddressFamilyIdentifierTC=AristaBgp4V2SubsequentAddressFamilyIdentifierTC, AristaBgp4V2IdentifierTC=AristaBgp4V2IdentifierTC, aristaBgp4V2TC=aristaBgp4V2TC, PYSNMP_MODULE_ID=aristaBgp4V2TC, AristaBgp4V2AddressFamilyIdentifierTC=AristaBgp4V2AddressFamilyIdentifierTC)
