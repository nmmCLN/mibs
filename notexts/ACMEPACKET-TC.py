#
# PySNMP MIB module ACMEPACKET-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-TC
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacket, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacket")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, NotificationType, MibIdentifier, iso, Unsigned32, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "iso", "Unsigned32", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
apTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 0))
apTextualConventions.setRevisions(('2012-02-06 23:05', '2012-05-05 23:05', '2014-06-26 00:00',))
if mibBuilder.loadTexts: apTextualConventions.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apTextualConventions.setOrganization('Oracle Communications')
class ApHardwareModuleFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 17, 18, 19, 24, 25, 26, 240, 241, 242))
    namedValues = NamedValues(("unknown", 0), ("spu", 17), ("npu", 18), ("tcu", 19), ("niuCopper", 24), ("niuFiber", 25), ("miu", 26), ("fanTray", 240), ("powerSupply", 241), ("niu10g", 242))

class ApRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 0), ("initial", 1), ("active", 2), ("standby", 3), ("outOfService", 4), ("unassigned", 5), ("activePending", 6), ("standbyPending", 7), ("outOfServicePending", 8), ("recovery", 9))

class ApPhyPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unknown", 0), ("sfp", 1))

class ApPresence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("inserted", 1), ("removed", 2))

class ApTransportType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tcp", 1), ("sctp", 2))

class ApServerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inservice", 0), ("lowerpriority", 1), ("oosunreachable", 2))

class ApDiamResultCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1001, 2001, 2002, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 4001, 4002, 4003, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017))
    namedValues = NamedValues(("diameterMultiRoundAuth", 1001), ("diameterSuccess", 2001), ("diameterLimitedSuccess", 2002), ("diameterCommandUnsupported", 3001), ("diameterUnableToDeliver", 3002), ("diameterRealmNotServed", 3003), ("diameterTooBusy", 3004), ("diameterLoopDetected", 3005), ("diameterRedirectIndicatoion", 3006), ("diameterApplicationUnsupported", 3007), ("diameterInvalidHdrBits", 3008), ("diameterInvalidAvpBits", 3009), ("diameterUnknownPeer", 3010), ("diameterAuthenticationRejected", 4001), ("diameterOutOfSpace", 4002), ("electionLost", 4003), ("diameterAvpUnsupported", 5001), ("diameterUnknownSessionId", 5002), ("diameterAuthoriszationRejected", 5003), ("diameterInvalidAvpValue", 5004), ("diameterMissingAvp", 5005), ("diameterResourcesExceeded", 5006), ("diameterContradictingAvps", 5007), ("diameterAvpNotAllowed", 5008), ("diameterAvpTooManyTimes", 5009), ("diameterNoCommonApplication", 5010), ("diameterUnsupportedVersion", 5011), ("diameterUnableToComply", 5012), ("diameterInvalidBitInHeader", 5013), ("diameterInvalidAvpLength", 5014), ("diameterInvalidMessageLength", 5015), ("diameterInvalidAvpBitCombo", 5016), ("diameterNoCommonSecurity", 5017))

class ApPercentage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class ApSipMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("invite", 2), ("ack", 3), ("bye", 4), ("register", 5), ("cancel", 6), ("prack", 7), ("options", 8), ("info", 9), ("subscribe", 10), ("notify", 11), ("refer", 12), ("update", 13), ("message", 14), ("publish", 15))

class ApThreadOverloaded(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notApplicable", 1), ("true", 2), ("false", 3))

class ApCommMonitorState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("outofservice", 0), ("connecting", 1), ("connected", 2), ("inservice", 3))

class ApAclType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("untrusted", 0), ("trusted", 1))

mibBuilder.exportSymbols("ACMEPACKET-TC", ApAclType=ApAclType, ApCommMonitorState=ApCommMonitorState, ApPresence=ApPresence, apTextualConventions=apTextualConventions, ApHardwareModuleFamily=ApHardwareModuleFamily, ApPhyPortType=ApPhyPortType, ApTransportType=ApTransportType, PYSNMP_MODULE_ID=apTextualConventions, ApPercentage=ApPercentage, ApRedundancyState=ApRedundancyState, ApSipMethod=ApSipMethod, ApServerStatus=ApServerStatus, ApDiamResultCode=ApDiamResultCode, ApThreadOverloaded=ApThreadOverloaded)
