#
# PySNMP MIB module SL-SNTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-SNTP-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:38 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, TimeTicks, IpAddress, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "TimeTicks", "IpAddress", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter32")
RowStatus, TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
slSntp = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21))
if mibBuilder.loadTexts: slSntp.setLastUpdated('200007240000Z')
if mibBuilder.loadTexts: slSntp.setOrganization('PacketLight Networks Ltd.')
slSntpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1))
slSntpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2))
slSntpConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("unicast", 2), ("broadcast", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigMode.setStatus('current')
slSntpConfigPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigPollInterval.setStatus('current')
slSntpConfigRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 3), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigRetryCount.setStatus('current')
slSntpConfigTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigTimeZone.setStatus('current')
slSntpConfigDayLightSaving = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigDayLightSaving.setStatus('current')
slSntpConfigFractTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigFractTimeZone.setStatus('current')
slSntpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10), )
if mibBuilder.loadTexts: slSntpConfigTable.setStatus('current')
slSntpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1), ).setIndexNames((0, "SL-SNTP-MIB", "slSntpConfigAddress"))
if mibBuilder.loadTexts: slSntpConfigEntry.setStatus('current')
slSntpConfigAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigAddress.setStatus('current')
slSntpConfigVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigVersion.setStatus('current')
slSntpConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigPriority.setStatus('current')
slSntpConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSntpConfigRowStatus.setStatus('current')
slSntpConfigMaxVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7200000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigMaxVariance.setStatus('current')
slSntpConfigVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSntpConfigVariance.setStatus('current')
slSntpConfigVarianceDetectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSntpConfigVarianceDetectEnable.setStatus('current')
slSntpConfigServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("disconnected", 1), ("connected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSntpConfigServerStatus.setStatus('current')
slSntpPeerFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2, 1)).setObjects(("SL-SNTP-MIB", "slSntpConfigAddress"))
if mibBuilder.loadTexts: slSntpPeerFailureTrap.setStatus('current')
slSntpConfigVarianceTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2, 2)).setObjects(("SL-SNTP-MIB", "slSntpConfigAddress"), ("SL-SNTP-MIB", "slSntpConfigMaxVariance"), ("SL-SNTP-MIB", "slSntpConfigVariance"))
if mibBuilder.loadTexts: slSntpConfigVarianceTrap.setStatus('current')
mibBuilder.exportSymbols("SL-SNTP-MIB", PYSNMP_MODULE_ID=slSntp, slSntpConfigPollInterval=slSntpConfigPollInterval, slSntpConfigServerStatus=slSntpConfigServerStatus, slSntpConfigRetryCount=slSntpConfigRetryCount, slSntpConfigVersion=slSntpConfigVersion, slSntpConfigDayLightSaving=slSntpConfigDayLightSaving, slSntpConfigEntry=slSntpConfigEntry, slSntpConfigVariance=slSntpConfigVariance, slSntp=slSntp, slSntpConfigFractTimeZone=slSntpConfigFractTimeZone, slSntpConfigTimeZone=slSntpConfigTimeZone, slSntpConfigVarianceTrap=slSntpConfigVarianceTrap, slSntpConfigPriority=slSntpConfigPriority, slSntpConfigTable=slSntpConfigTable, slSntpPeerFailureTrap=slSntpPeerFailureTrap, slSntpTraps=slSntpTraps, slSntpConfigVarianceDetectEnable=slSntpConfigVarianceDetectEnable, slSntpConfigMode=slSntpConfigMode, slSntpConfigRowStatus=slSntpConfigRowStatus, slSntpConfigAddress=slSntpConfigAddress, slSntpConfig=slSntpConfig, slSntpConfigMaxVariance=slSntpConfigMaxVariance)
