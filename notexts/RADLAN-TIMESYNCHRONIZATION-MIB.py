#
# PySNMP MIB module RADLAN-TIMESYNCHRONIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-TIMESYNCHRONIZATION-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:36:30 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibIdentifier, Counter32, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "ModuleIdentity")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlTimeSynchronization = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 92))
rlTimeSynchronization.setRevisions(('2003-11-23 00:24',))
if mibBuilder.loadTexts: rlTimeSynchronization.setLastUpdated('200408030024Z')
if mibBuilder.loadTexts: rlTimeSynchronization.setOrganization('Radlan Computer Communication Ltd.')
rlTimeSyncMethodMode = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 92, 1))
rlSntpNtpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 92, 2))
rlSntpNtpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 92, 2, 1))
rlSntpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 92, 2, 2))
rlNtpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 92, 2, 3))
class NTPTimeStamp(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.1"
    status = 'current'
    displayHint = '4d.4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPSignedTimeValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d.2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 2.2"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

rlTimeSyncMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTimeSyncMibVersion.setStatus('current')
rndTimeSyncManagedTime = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndTimeSyncManagedTime.setStatus('current')
rndTimeSyncManagedDate = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndTimeSyncManagedDate.setStatus('current')
rndTimeSyncManagedDateTime = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndTimeSyncManagedDateTime.setStatus('current')
rlTimeSyncMethod = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("sntp", 2), ("ntp", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTimeSyncMethod.setStatus('current')
rlTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTimeZone.setStatus('current')
rlTimeZoneCode = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTimeZoneCode.setStatus('current')
rlDaylightSavingTimeMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("recurring", 1), ("date", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDaylightSavingTimeMode.setStatus('current')
rlDaylightSavingTimeStart = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDaylightSavingTimeStart.setStatus('current')
rlDaylightSavingTimeEnd = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDaylightSavingTimeEnd.setStatus('current')
rlDaylightSavingTimeOffset = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 11), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDaylightSavingTimeOffset.setStatus('current')
rlDaylightSavingTimeCode = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDaylightSavingTimeCode.setStatus('current')
rlTZDSTOffset = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTZDSTOffset.setStatus('current')
rlSntpNtpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpMibVersion.setStatus('current')
rlSntpNtpConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("unicast", 2), ("anycast", 3), ("multicast", 4), ("unicastAnycast", 5), ("unicastMulticast", 6), ("anycastMulticast", 7), ("unicastAnycastMulticast", 8))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigMode.setStatus('current')
rlSntpNtpConfigSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 3), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigSysStratum.setStatus('current')
rlSntpNtpConfigPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 4), Integer32().clone(1024)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpNtpConfigPollInterval.setStatus('current')
rlSntpNtpConfigPrimaryPollSrvAddr = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigPrimaryPollSrvAddr.setStatus('current')
rlSntpNtpConfigPrimaryPollSrvMrid = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigPrimaryPollSrvMrid.setStatus('current')
rlSntpNtpConfigPrimaryPollSrvIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigPrimaryPollSrvIfIndex.setStatus('current')
rlSntpNtpConfigPrimaryPollSrvStratum = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 8), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigPrimaryPollSrvStratum.setStatus('current')
rlSntpNtpConfigSyncSrvAddr = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigSyncSrvAddr.setStatus('current')
rlSntpNtpConfigSyncSrvMrid = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigSyncSrvMrid.setStatus('current')
rlSntpNtpConfigSyncSrvIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigSyncSrvIfIndex.setStatus('current')
rlSntpNtpConfigSyncSrvType = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("unicast", 2), ("anycast", 3), ("broadcast", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigSyncSrvType.setStatus('current')
rlSntpNtpConfigSyncSrvStratum = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 13), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigSyncSrvStratum.setStatus('current')
rlSntpNtpConfigRetryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigRetryTimeout.setStatus('current')
rlSntpNtpConfigRetryCnt = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpNtpConfigRetryCnt.setStatus('current')
rlSntpClientMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("active", 2), ("passive", 3))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpClientMode.setStatus('current')
rlSntpUnicastAdminState = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpUnicastAdminState.setStatus('current')
rlSntpBroadcastAdminState = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpBroadcastAdminState.setStatus('current')
rlSntpAnycastAdminState = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAnycastAdminState.setStatus('current')
rlSntpUnicastPollState = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpUnicastPollState.setStatus('current')
rlSntpBroadcastPollState = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpBroadcastPollState.setStatus('current')
rlSntpAnycastPollState = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAnycastPollState.setStatus('current')
rlSntpAuthenticationState = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAuthenticationState.setStatus('current')
rlTimeValidFlag = MibScalar((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTimeValidFlag.setStatus('current')
rlSntpConfigBroadcastTable = MibTable((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10), )
if mibBuilder.loadTexts: rlSntpConfigBroadcastTable.setStatus('current')
rlSntpBroadcastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1), ).setIndexNames((0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpBroadcastIfIndex"))
if mibBuilder.loadTexts: rlSntpBroadcastEntry.setStatus('current')
rlSntpBroadcastIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSntpBroadcastIfIndex.setStatus('current')
rlSntpBroadcastIfAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpBroadcastIfAdminState.setStatus('current')
rlSntpBroadcastMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("receive", 2), ("send", 3), ("receiveSend", 4))).clone('receiveSend')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpBroadcastMode.setStatus('current')
rlSntpBroadcastPolled = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpBroadcastPolled.setStatus('current')
rlSntpBroadcastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpBroadcastAddress.setStatus('current')
rlSntpBroadcastStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 6), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpBroadcastStratum.setStatus('current')
rlSntpBroadcastLastResp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpBroadcastLastResp.setStatus('current')
rlSntpBroadcastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("inProcess", 2), ("up", 3), ("down", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpBroadcastStatus.setStatus('current')
rlSntpBroadcastOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 9), NTPTimeStamp()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpBroadcastOffset.setStatus('current')
rlSntpBroadcastDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 10), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpBroadcastDelay.setStatus('current')
rlSntpBroadcastRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 11), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpBroadcastRowStatus.setStatus('current')
rlSntpConfigAnycastTable = MibTable((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11), )
if mibBuilder.loadTexts: rlSntpConfigAnycastTable.setStatus('current')
rlSntpAnycastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1), ).setIndexNames((0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpAnycastIfIndex"))
if mibBuilder.loadTexts: rlSntpAnycastEntry.setStatus('current')
rlSntpAnycastIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSntpAnycastIfIndex.setStatus('current')
rlSntpAnycastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpAnycastAddress.setStatus('current')
rlSntpAnycastStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 3), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpAnycastStratum.setStatus('current')
rlSntpAnycastLastResp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 4), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpAnycastLastResp.setStatus('current')
rlSntpAnycastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("inProcess", 2), ("up", 3), ("down", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpAnycastStatus.setStatus('current')
rlSntpAnycastOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 6), NTPTimeStamp()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpAnycastOffset.setStatus('current')
rlSntpAnycastDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 7), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpAnycastDelay.setStatus('current')
rlSntpAnycastRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAnycastRowStatus.setStatus('current')
rlSntpConfigServerTable = MibTable((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12), )
if mibBuilder.loadTexts: rlSntpConfigServerTable.setStatus('current')
rlSntpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1), ).setIndexNames((0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpServerAddress"))
if mibBuilder.loadTexts: rlSntpServerEntry.setStatus('current')
rlSntpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 1), IpAddress())
if mibBuilder.loadTexts: rlSntpServerAddress.setStatus('current')
rlSntpServerPolled = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpServerPolled.setStatus('current')
rlSntpServerStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 3), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpServerStratum.setStatus('current')
rlSntpServerLastResp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 4), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpServerLastResp.setStatus('current')
rlSntpServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("inProcess", 2), ("up", 3), ("down", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpServerStatus.setStatus('current')
rlSntpServersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 6), NTPTimeStamp()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpServersOffset.setStatus('current')
rlSntpServersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 7), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSntpServersDelay.setStatus('current')
rlSntpServersKeyIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpServersKeyIdentifier.setStatus('current')
rlSntpServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpServerRowStatus.setStatus('current')
rlSntpConfigAuthenticationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13), )
if mibBuilder.loadTexts: rlSntpConfigAuthenticationTable.setStatus('current')
rlSntpAuthenticationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1), ).setIndexNames((0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpAuthenticationKeyID"))
if mibBuilder.loadTexts: rlSntpAuthenticationEntry.setStatus('current')
rlSntpAuthenticationKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAuthenticationKeyID.setStatus('current')
rlSntpAuthenticationKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAuthenticationKeyValue.setStatus('current')
rlSntpAuthenticationKeyState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAuthenticationKeyState.setStatus('current')
rlSntpAuthenticationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSntpAuthenticationRowStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-TIMESYNCHRONIZATION-MIB", rlSntpNtpConfigPrimaryPollSrvIfIndex=rlSntpNtpConfigPrimaryPollSrvIfIndex, rlSntpClientMode=rlSntpClientMode, rlSntpConfig=rlSntpConfig, rlSntpNtpConfigRetryTimeout=rlSntpNtpConfigRetryTimeout, rlSntpNtpConfigSyncSrvStratum=rlSntpNtpConfigSyncSrvStratum, rlSntpServersOffset=rlSntpServersOffset, rlSntpAnycastIfIndex=rlSntpAnycastIfIndex, rlSntpBroadcastMode=rlSntpBroadcastMode, rlDaylightSavingTimeEnd=rlDaylightSavingTimeEnd, rlTZDSTOffset=rlTZDSTOffset, rlSntpConfigAnycastTable=rlSntpConfigAnycastTable, rlNtpConfig=rlNtpConfig, rlSntpAnycastOffset=rlSntpAnycastOffset, rlSntpAuthenticationRowStatus=rlSntpAuthenticationRowStatus, rlTimeSynchronization=rlTimeSynchronization, rlSntpAnycastAdminState=rlSntpAnycastAdminState, rlSntpServerAddress=rlSntpServerAddress, rlSntpServerStatus=rlSntpServerStatus, rlTimeZoneCode=rlTimeZoneCode, NTPStratum=NTPStratum, rlSntpUnicastAdminState=rlSntpUnicastAdminState, rlSntpConfigBroadcastTable=rlSntpConfigBroadcastTable, rlSntpAuthenticationState=rlSntpAuthenticationState, rlSntpAnycastEntry=rlSntpAnycastEntry, rlSntpAuthenticationKeyValue=rlSntpAuthenticationKeyValue, rlSntpBroadcastOffset=rlSntpBroadcastOffset, rlSntpBroadcastStratum=rlSntpBroadcastStratum, rlSntpServersKeyIdentifier=rlSntpServersKeyIdentifier, rlSntpNtpConfigSyncSrvType=rlSntpNtpConfigSyncSrvType, rlSntpBroadcastAddress=rlSntpBroadcastAddress, rndTimeSyncManagedDate=rndTimeSyncManagedDate, rlSntpBroadcastIfIndex=rlSntpBroadcastIfIndex, rlSntpAuthenticationEntry=rlSntpAuthenticationEntry, rlSntpBroadcastEntry=rlSntpBroadcastEntry, rlDaylightSavingTimeCode=rlDaylightSavingTimeCode, rlSntpBroadcastPolled=rlSntpBroadcastPolled, rlTimeSyncMibVersion=rlTimeSyncMibVersion, rlSntpBroadcastAdminState=rlSntpBroadcastAdminState, rlSntpServersDelay=rlSntpServersDelay, rlSntpServerPolled=rlSntpServerPolled, rndTimeSyncManagedTime=rndTimeSyncManagedTime, rlSntpNtpConfigSyncSrvMrid=rlSntpNtpConfigSyncSrvMrid, rlSntpNtpClient=rlSntpNtpClient, rlTimeSyncMethod=rlTimeSyncMethod, rlSntpAnycastPollState=rlSntpAnycastPollState, rlSntpNtpConfigSysStratum=rlSntpNtpConfigSysStratum, NTPTimeStamp=NTPTimeStamp, rlSntpNtpConfigPrimaryPollSrvStratum=rlSntpNtpConfigPrimaryPollSrvStratum, rlSntpAnycastAddress=rlSntpAnycastAddress, rlSntpBroadcastIfAdminState=rlSntpBroadcastIfAdminState, rlSntpServerLastResp=rlSntpServerLastResp, rlSntpNtpConfigSyncSrvAddr=rlSntpNtpConfigSyncSrvAddr, rlSntpBroadcastDelay=rlSntpBroadcastDelay, rlSntpNtpConfigRetryCnt=rlSntpNtpConfigRetryCnt, rlSntpServerStratum=rlSntpServerStratum, rlSntpServerRowStatus=rlSntpServerRowStatus, rlSntpAnycastRowStatus=rlSntpAnycastRowStatus, rlSntpNtpConfigPollInterval=rlSntpNtpConfigPollInterval, rlSntpConfigAuthenticationTable=rlSntpConfigAuthenticationTable, rlSntpServerEntry=rlSntpServerEntry, rndTimeSyncManagedDateTime=rndTimeSyncManagedDateTime, rlDaylightSavingTimeOffset=rlDaylightSavingTimeOffset, rlSntpNtpConfigPrimaryPollSrvMrid=rlSntpNtpConfigPrimaryPollSrvMrid, rlSntpBroadcastLastResp=rlSntpBroadcastLastResp, rlSntpBroadcastStatus=rlSntpBroadcastStatus, rlSntpNtpConfigSyncSrvIfIndex=rlSntpNtpConfigSyncSrvIfIndex, rlTimeZone=rlTimeZone, rlSntpAnycastStatus=rlSntpAnycastStatus, rlSntpAnycastDelay=rlSntpAnycastDelay, rlSntpBroadcastRowStatus=rlSntpBroadcastRowStatus, rlDaylightSavingTimeStart=rlDaylightSavingTimeStart, rlSntpConfigServerTable=rlSntpConfigServerTable, rlSntpNtpConfig=rlSntpNtpConfig, rlDaylightSavingTimeMode=rlDaylightSavingTimeMode, rlSntpAnycastStratum=rlSntpAnycastStratum, PYSNMP_MODULE_ID=rlTimeSynchronization, rlTimeSyncMethodMode=rlTimeSyncMethodMode, rlSntpAuthenticationKeyID=rlSntpAuthenticationKeyID, rlSntpBroadcastPollState=rlSntpBroadcastPollState, rlSntpAnycastLastResp=rlSntpAnycastLastResp, rlSntpNtpMibVersion=rlSntpNtpMibVersion, rlSntpNtpConfigPrimaryPollSrvAddr=rlSntpNtpConfigPrimaryPollSrvAddr, rlSntpNtpConfigMode=rlSntpNtpConfigMode, rlTimeValidFlag=rlTimeValidFlag, rlSntpUnicastPollState=rlSntpUnicastPollState, rlSntpAuthenticationKeyState=rlSntpAuthenticationKeyState, NTPSignedTimeValue=NTPSignedTimeValue)
