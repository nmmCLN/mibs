#
# PySNMP MIB module DNS-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DNS-SERVER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, ObjectIdentity, Integer32, Counter32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ObjectIdentity", "Integer32", "Counter32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
dns = ObjectIdentity((1, 3, 6, 1, 2, 1, 32))
if mibBuilder.loadTexts: dns.setStatus('current')
dnsServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 32, 1))
if mibBuilder.loadTexts: dnsServMIB.setLastUpdated('9401282251Z')
if mibBuilder.loadTexts: dnsServMIB.setOrganization('IETF DNS Working Group')
dnsServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1))
dnsServConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 1))
dnsServCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 2))
dnsServOptCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 3))
dnsServZone = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 4))
class DnsName(TextualConvention, OctetString):
    reference = 'RFC-1034 section 3.1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class DnsNameAsIndex(DnsName):
    reference = 'RFC-1034 section 3.1, RFC-1448 section 4.1.'
    status = 'current'

class DnsClass(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.4.'
    status = 'current'
    displayHint = '2d'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsType(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.2.'
    status = 'current'
    displayHint = '2d'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsQClass(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.5.'
    status = 'current'
    displayHint = '2d'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsQType(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.3.'
    status = 'current'
    displayHint = '2d'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsTime(TextualConvention, Gauge32):
    reference = 'RFC-1035.'
    status = 'current'
    displayHint = '4d'

class DnsOpCode(TextualConvention, Integer32):
    reference = 'RFC-1035 section 4.1.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class DnsRespCode(TextualConvention, Integer32):
    reference = 'RFC-1035 section 4.1.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

dnsServConfigImplementIdent = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServConfigImplementIdent.setStatus('current')
dnsServConfigRecurs = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("available", 1), ("restricted", 2), ("unavailable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServConfigRecurs.setStatus('current')
dnsServConfigUpTime = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 3), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServConfigUpTime.setStatus('current')
dnsServConfigResetTime = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 4), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServConfigResetTime.setStatus('current')
dnsServConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServConfigReset.setStatus('current')
dnsServCounterAuthAns = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterAuthAns.setStatus('current')
dnsServCounterAuthNoNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterAuthNoNames.setStatus('current')
dnsServCounterAuthNoDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterAuthNoDataResps.setStatus('current')
dnsServCounterNonAuthDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterNonAuthDatas.setStatus('current')
dnsServCounterNonAuthNoDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterNonAuthNoDatas.setStatus('current')
dnsServCounterReferrals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterReferrals.setStatus('current')
dnsServCounterErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterErrors.setStatus('current')
dnsServCounterRelNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterRelNames.setStatus('current')
dnsServCounterReqRefusals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterReqRefusals.setStatus('current')
dnsServCounterReqUnparses = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterReqUnparses.setStatus('current')
dnsServCounterOtherErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterOtherErrors.setStatus('current')
dnsServCounterTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13), )
if mibBuilder.loadTexts: dnsServCounterTable.setStatus('current')
dnsServCounterEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1), ).setIndexNames((0, "DNS-SERVER-MIB", "dnsServCounterOpCode"), (0, "DNS-SERVER-MIB", "dnsServCounterQClass"), (0, "DNS-SERVER-MIB", "dnsServCounterQType"), (0, "DNS-SERVER-MIB", "dnsServCounterTransport"))
if mibBuilder.loadTexts: dnsServCounterEntry.setStatus('current')
dnsServCounterOpCode = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 1), DnsOpCode())
if mibBuilder.loadTexts: dnsServCounterOpCode.setStatus('current')
dnsServCounterQClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 2), DnsClass())
if mibBuilder.loadTexts: dnsServCounterQClass.setStatus('current')
dnsServCounterQType = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 3), DnsType())
if mibBuilder.loadTexts: dnsServCounterQType.setStatus('current')
dnsServCounterTransport = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("udp", 1), ("tcp", 2), ("other", 3))))
if mibBuilder.loadTexts: dnsServCounterTransport.setStatus('current')
dnsServCounterRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterRequests.setStatus('current')
dnsServCounterResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterResponses.setStatus('current')
dnsServOptCounterSelfAuthAns = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthAns.setStatus('current')
dnsServOptCounterSelfAuthNoNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthNoNames.setStatus('current')
dnsServOptCounterSelfAuthNoDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthNoDataResps.setStatus('current')
dnsServOptCounterSelfNonAuthDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfNonAuthDatas.setStatus('current')
dnsServOptCounterSelfNonAuthNoDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfNonAuthNoDatas.setStatus('current')
dnsServOptCounterSelfReferrals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfReferrals.setStatus('current')
dnsServOptCounterSelfErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfErrors.setStatus('current')
dnsServOptCounterSelfRelNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfRelNames.setStatus('current')
dnsServOptCounterSelfReqRefusals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfReqRefusals.setStatus('current')
dnsServOptCounterSelfReqUnparses = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfReqUnparses.setStatus('current')
dnsServOptCounterSelfOtherErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfOtherErrors.setStatus('current')
dnsServOptCounterFriendsAuthAns = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthAns.setStatus('current')
dnsServOptCounterFriendsAuthNoNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthNoNames.setStatus('current')
dnsServOptCounterFriendsAuthNoDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthNoDataResps.setStatus('current')
dnsServOptCounterFriendsNonAuthDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsNonAuthDatas.setStatus('current')
dnsServOptCounterFriendsNonAuthNoDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsNonAuthNoDatas.setStatus('current')
dnsServOptCounterFriendsReferrals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsReferrals.setStatus('current')
dnsServOptCounterFriendsErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsErrors.setStatus('current')
dnsServOptCounterFriendsRelNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsRelNames.setStatus('current')
dnsServOptCounterFriendsReqRefusals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsReqRefusals.setStatus('current')
dnsServOptCounterFriendsReqUnparses = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsReqUnparses.setStatus('current')
dnsServOptCounterFriendsOtherErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsOtherErrors.setStatus('current')
dnsServZoneTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1), )
if mibBuilder.loadTexts: dnsServZoneTable.setStatus('current')
dnsServZoneEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1), ).setIndexNames((0, "DNS-SERVER-MIB", "dnsServZoneName"), (0, "DNS-SERVER-MIB", "dnsServZoneClass"))
if mibBuilder.loadTexts: dnsServZoneEntry.setStatus('current')
dnsServZoneName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 1), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsServZoneName.setStatus('current')
dnsServZoneClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 2), DnsClass())
if mibBuilder.loadTexts: dnsServZoneClass.setStatus('current')
dnsServZoneLastReloadSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 3), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastReloadSuccess.setStatus('current')
dnsServZoneLastReloadAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 4), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastReloadAttempt.setStatus('current')
dnsServZoneLastSourceAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastSourceAttempt.setStatus('current')
dnsServZoneStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsServZoneStatus.setStatus('current')
dnsServZoneSerial = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneSerial.setStatus('current')
dnsServZoneCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneCurrent.setStatus('current')
dnsServZoneLastSourceSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastSourceSuccess.setStatus('current')
dnsServZoneSrcTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2), )
if mibBuilder.loadTexts: dnsServZoneSrcTable.setStatus('current')
dnsServZoneSrcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1), ).setIndexNames((0, "DNS-SERVER-MIB", "dnsServZoneSrcName"), (0, "DNS-SERVER-MIB", "dnsServZoneSrcClass"), (0, "DNS-SERVER-MIB", "dnsServZoneSrcAddr"))
if mibBuilder.loadTexts: dnsServZoneSrcEntry.setStatus('current')
dnsServZoneSrcName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 1), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsServZoneSrcName.setStatus('current')
dnsServZoneSrcClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 2), DnsClass())
if mibBuilder.loadTexts: dnsServZoneSrcClass.setStatus('current')
dnsServZoneSrcAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: dnsServZoneSrcAddr.setStatus('current')
dnsServZoneSrcStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsServZoneSrcStatus.setStatus('current')
dnsServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 2))
dnsServConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 1)).setObjects(("DNS-SERVER-MIB", "dnsServConfigImplementIdent"), ("DNS-SERVER-MIB", "dnsServConfigRecurs"), ("DNS-SERVER-MIB", "dnsServConfigUpTime"), ("DNS-SERVER-MIB", "dnsServConfigResetTime"), ("DNS-SERVER-MIB", "dnsServConfigReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServConfigGroup = dnsServConfigGroup.setStatus('current')
dnsServCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 2)).setObjects(("DNS-SERVER-MIB", "dnsServCounterAuthAns"), ("DNS-SERVER-MIB", "dnsServCounterAuthNoNames"), ("DNS-SERVER-MIB", "dnsServCounterAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServCounterNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServCounterNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServCounterReferrals"), ("DNS-SERVER-MIB", "dnsServCounterErrors"), ("DNS-SERVER-MIB", "dnsServCounterRelNames"), ("DNS-SERVER-MIB", "dnsServCounterReqRefusals"), ("DNS-SERVER-MIB", "dnsServCounterReqUnparses"), ("DNS-SERVER-MIB", "dnsServCounterOtherErrors"), ("DNS-SERVER-MIB", "dnsServCounterOpCode"), ("DNS-SERVER-MIB", "dnsServCounterQClass"), ("DNS-SERVER-MIB", "dnsServCounterQType"), ("DNS-SERVER-MIB", "dnsServCounterTransport"), ("DNS-SERVER-MIB", "dnsServCounterRequests"), ("DNS-SERVER-MIB", "dnsServCounterResponses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServCounterGroup = dnsServCounterGroup.setStatus('current')
dnsServOptCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 3)).setObjects(("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthAns"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoNames"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReferrals"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfRelNames"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReqRefusals"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReqUnparses"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfOtherErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthAns"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoNames"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReferrals"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsRelNames"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqRefusals"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqUnparses"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsOtherErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServOptCounterGroup = dnsServOptCounterGroup.setStatus('current')
dnsServZoneGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 4)).setObjects(("DNS-SERVER-MIB", "dnsServZoneName"), ("DNS-SERVER-MIB", "dnsServZoneClass"), ("DNS-SERVER-MIB", "dnsServZoneLastReloadSuccess"), ("DNS-SERVER-MIB", "dnsServZoneLastReloadAttempt"), ("DNS-SERVER-MIB", "dnsServZoneLastSourceAttempt"), ("DNS-SERVER-MIB", "dnsServZoneLastSourceSuccess"), ("DNS-SERVER-MIB", "dnsServZoneStatus"), ("DNS-SERVER-MIB", "dnsServZoneSerial"), ("DNS-SERVER-MIB", "dnsServZoneCurrent"), ("DNS-SERVER-MIB", "dnsServZoneSrcName"), ("DNS-SERVER-MIB", "dnsServZoneSrcClass"), ("DNS-SERVER-MIB", "dnsServZoneSrcAddr"), ("DNS-SERVER-MIB", "dnsServZoneSrcStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServZoneGroup = dnsServZoneGroup.setStatus('current')
dnsServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 3))
dnsServMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 32, 1, 3, 1)).setObjects(("DNS-SERVER-MIB", "dnsServConfigGroup"), ("DNS-SERVER-MIB", "dnsServCounterGroup"), ("DNS-SERVER-MIB", "dnsServOptCounterGroup"), ("DNS-SERVER-MIB", "dnsServZoneGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServMIBCompliance = dnsServMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("DNS-SERVER-MIB", dnsServConfigRecurs=dnsServConfigRecurs, dnsServCounterTable=dnsServCounterTable, dnsServConfigGroup=dnsServConfigGroup, dnsServZoneTable=dnsServZoneTable, dnsServZoneStatus=dnsServZoneStatus, dnsServOptCounterSelfRelNames=dnsServOptCounterSelfRelNames, dnsServConfigResetTime=dnsServConfigResetTime, PYSNMP_MODULE_ID=dnsServMIB, dnsServCounterRequests=dnsServCounterRequests, dnsServOptCounterFriendsAuthNoNames=dnsServOptCounterFriendsAuthNoNames, dnsServCounterErrors=dnsServCounterErrors, dnsServOptCounterFriendsNonAuthDatas=dnsServOptCounterFriendsNonAuthDatas, dnsServZoneGroup=dnsServZoneGroup, dnsServOptCounterSelfNonAuthNoDatas=dnsServOptCounterSelfNonAuthNoDatas, dnsServOptCounterSelfErrors=dnsServOptCounterSelfErrors, dnsServCounterReferrals=dnsServCounterReferrals, dnsServCounterRelNames=dnsServCounterRelNames, dnsServOptCounterSelfReferrals=dnsServOptCounterSelfReferrals, dnsServZoneCurrent=dnsServZoneCurrent, dnsServMIBObjects=dnsServMIBObjects, dnsServZoneSrcEntry=dnsServZoneSrcEntry, dnsServZoneClass=dnsServZoneClass, dnsServCounterAuthNoDataResps=dnsServCounterAuthNoDataResps, dnsServOptCounterSelfAuthAns=dnsServOptCounterSelfAuthAns, dnsServCounterReqRefusals=dnsServCounterReqRefusals, dnsServZoneLastSourceSuccess=dnsServZoneLastSourceSuccess, dnsServCounterNonAuthNoDatas=dnsServCounterNonAuthNoDatas, dnsServConfigReset=dnsServConfigReset, dnsServZoneSrcAddr=dnsServZoneSrcAddr, dnsServOptCounterFriendsReqUnparses=dnsServOptCounterFriendsReqUnparses, dnsServZoneSerial=dnsServZoneSerial, dnsServConfigImplementIdent=dnsServConfigImplementIdent, dnsServZoneEntry=dnsServZoneEntry, dnsServOptCounterFriendsRelNames=dnsServOptCounterFriendsRelNames, dnsServConfigUpTime=dnsServConfigUpTime, dnsServOptCounterSelfReqRefusals=dnsServOptCounterSelfReqRefusals, dnsServZoneSrcStatus=dnsServZoneSrcStatus, dnsServOptCounterFriendsOtherErrors=dnsServOptCounterFriendsOtherErrors, DnsTime=DnsTime, dnsServCounterOpCode=dnsServCounterOpCode, dnsServCounterOtherErrors=dnsServCounterOtherErrors, DnsNameAsIndex=DnsNameAsIndex, dnsServMIB=dnsServMIB, dnsServCounterQType=dnsServCounterQType, dnsServOptCounterFriendsAuthNoDataResps=dnsServOptCounterFriendsAuthNoDataResps, dnsServMIBCompliance=dnsServMIBCompliance, dnsServOptCounterSelfNonAuthDatas=dnsServOptCounterSelfNonAuthDatas, dnsServOptCounterFriendsErrors=dnsServOptCounterFriendsErrors, dnsServZoneSrcClass=dnsServZoneSrcClass, dnsServOptCounterFriendsNonAuthNoDatas=dnsServOptCounterFriendsNonAuthNoDatas, dnsServCounterResponses=dnsServCounterResponses, DnsName=DnsName, dnsServOptCounterSelfAuthNoDataResps=dnsServOptCounterSelfAuthNoDataResps, dns=dns, dnsServZoneLastSourceAttempt=dnsServZoneLastSourceAttempt, dnsServOptCounterGroup=dnsServOptCounterGroup, dnsServZoneSrcTable=dnsServZoneSrcTable, DnsOpCode=DnsOpCode, dnsServMIBCompliances=dnsServMIBCompliances, DnsRespCode=DnsRespCode, DnsQType=DnsQType, dnsServMIBGroups=dnsServMIBGroups, dnsServCounterAuthAns=dnsServCounterAuthAns, dnsServConfig=dnsServConfig, dnsServCounterQClass=dnsServCounterQClass, dnsServCounterGroup=dnsServCounterGroup, dnsServOptCounterSelfOtherErrors=dnsServOptCounterSelfOtherErrors, dnsServZoneLastReloadAttempt=dnsServZoneLastReloadAttempt, dnsServCounter=dnsServCounter, dnsServOptCounterFriendsReferrals=dnsServOptCounterFriendsReferrals, dnsServOptCounterSelfAuthNoNames=dnsServOptCounterSelfAuthNoNames, dnsServOptCounter=dnsServOptCounter, dnsServOptCounterFriendsReqRefusals=dnsServOptCounterFriendsReqRefusals, dnsServCounterNonAuthDatas=dnsServCounterNonAuthDatas, dnsServCounterAuthNoNames=dnsServCounterAuthNoNames, DnsQClass=DnsQClass, dnsServCounterReqUnparses=dnsServCounterReqUnparses, dnsServOptCounterFriendsAuthAns=dnsServOptCounterFriendsAuthAns, dnsServZoneLastReloadSuccess=dnsServZoneLastReloadSuccess, DnsType=DnsType, DnsClass=DnsClass, dnsServOptCounterSelfReqUnparses=dnsServOptCounterSelfReqUnparses, dnsServZoneSrcName=dnsServZoneSrcName, dnsServZoneName=dnsServZoneName, dnsServZone=dnsServZone, dnsServCounterEntry=dnsServCounterEntry, dnsServCounterTransport=dnsServCounterTransport)
