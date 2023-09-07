#
# PySNMP MIB module IANA-RTPROTO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-RTPROTO-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 11:43:59 2023
# On host fv-az174-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Integer32, MibIdentifier, Bits, ModuleIdentity, Counter64, mib_2, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "MibIdentifier", "Bits", "ModuleIdentity", "Counter64", "mib-2", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaRtProtoMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 84))
ianaRtProtoMIB.setRevisions(('2016-04-25 00:00', '2016-04-06 00:00', '2012-08-30 00:00', '2011-07-22 00:00', '2000-09-26 00:00',))
if mibBuilder.loadTexts: ianaRtProtoMIB.setLastUpdated('201604250000Z')
if mibBuilder.loadTexts: ianaRtProtoMIB.setOrganization('IANA')
class IANAipRouteProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16), ("dvmrp", 17), ("rpl", 18), ("dhcp", 19), ("ttdp", 20))

class IANAipMRouteProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("dvmrp", 4), ("mospf", 5), ("pimSparseDense", 6), ("cbt", 7), ("pimSparseMode", 8), ("pimDenseMode", 9), ("igmpOnly", 10), ("bgmp", 11), ("msdp", 12))

mibBuilder.exportSymbols("IANA-RTPROTO-MIB", PYSNMP_MODULE_ID=ianaRtProtoMIB, IANAipMRouteProtocol=IANAipMRouteProtocol, IANAipRouteProtocol=IANAipRouteProtocol, ianaRtProtoMIB=ianaRtProtoMIB)
