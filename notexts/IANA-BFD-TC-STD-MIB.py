#
# PySNMP MIB module IANA-BFD-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-BFD-TC-STD-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:23 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, MibIdentifier, Integer32, Gauge32, Counter64, TimeTicks, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "MibIdentifier", "Integer32", "Gauge32", "Counter64", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaBfdTCStdMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 224))
ianaBfdTCStdMib.setRevisions(('2014-08-12 00:00',))
if mibBuilder.loadTexts: ianaBfdTCStdMib.setLastUpdated('201408120000Z')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setOrganization('IANA')
class IANAbfdDiagTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Allan, D., Swallow, G., and Drake, J., Proactive Connectivity Verification, Continuity Check, and Remote Defect Indication for the MPLS Transport Profile, RFC 6428, November 2011.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8), ("misConnectivityDefect", 9))

class IANAbfdSessTypeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for Multihop Paths, RFC 5883, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("singleHop", 1), ("multiHopTotallyArbitraryPaths", 2), ("multiHopOutOfBandSignaling", 3), ("multiHopUnidirectionalLinks", 4))

class IANAbfdSessOperModeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4))

class IANAbfdSessStateTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ("failing", 5))

class IANAbfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAuthentication", -1), ("reserved", 0), ("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5))

class IANAbfdSessAuthenticationKeyTC(TextualConvention, OctetString):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 252)

mibBuilder.exportSymbols("IANA-BFD-TC-STD-MIB", IANAbfdSessOperModeTC=IANAbfdSessOperModeTC, ianaBfdTCStdMib=ianaBfdTCStdMib, PYSNMP_MODULE_ID=ianaBfdTCStdMib, IANAbfdSessTypeTC=IANAbfdSessTypeTC, IANAbfdSessStateTC=IANAbfdSessStateTC, IANAbfdSessAuthenticationKeyTC=IANAbfdSessAuthenticationKeyTC, IANAbfdSessAuthenticationTypeTC=IANAbfdSessAuthenticationTypeTC, IANAbfdDiagTC=IANAbfdDiagTC)
