#
# PySNMP MIB module IANA-PWE3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-PWE3-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 12:07:58 2022
# On host fv-az619-657 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, mib_2, Unsigned32, IpAddress, Counter32, ObjectIdentity, Counter64, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "mib-2", "Unsigned32", "IpAddress", "Counter32", "ObjectIdentity", "Counter64", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaPwe3MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 174))
ianaPwe3MIB.setRevisions(('2009-06-11 00:00',))
if mibBuilder.loadTexts: ianaPwe3MIB.setLastUpdated('200906110000Z')
if mibBuilder.loadTexts: ianaPwe3MIB.setOrganization('IANA')
class IANAPwTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 32767))
    namedValues = NamedValues(("other", 0), ("frameRelayDlciMartiniMode", 1), ("atmAal5SduVcc", 2), ("atmTransparent", 3), ("ethernetTagged", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cem", 8), ("atmCellNto1Vcc", 9), ("atmCellNto1Vpc", 10), ("ipLayer2Transport", 11), ("atmCell1to1Vcc", 12), ("atmCell1to1Vpc", 13), ("atmAal5PduVcc", 14), ("frameRelayPortMode", 15), ("cep", 16), ("e1Satop", 17), ("t1Satop", 18), ("e3Satop", 19), ("t3Satop", 20), ("basicCesPsn", 21), ("basicTdmIp", 22), ("tdmCasCesPsn", 23), ("tdmCasTdmIp", 24), ("frDlci", 25), ("wildcard", 32767))

class IANAPwPsnTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mpls", 1), ("l2tp", 2), ("udpOverIp", 3), ("mplsOverIp", 4), ("mplsOverGre", 5), ("other", 6))

class IANAPwCapabilities(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwStatusIndication", 0), ("pwVCCV", 1))

mibBuilder.exportSymbols("IANA-PWE3-MIB", ianaPwe3MIB=ianaPwe3MIB, IANAPwTypeTC=IANAPwTypeTC, IANAPwPsnTypeTC=IANAPwPsnTypeTC, PYSNMP_MODULE_ID=ianaPwe3MIB, IANAPwCapabilities=IANAPwCapabilities)
