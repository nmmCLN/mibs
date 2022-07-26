#
# PySNMP MIB module DNS-RESOLVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DNS-RESOLVER-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:33:27 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
DnsType, DnsTime, DnsQType, DnsNameAsIndex, DnsOpCode, dns, DnsName, DnsQClass, DnsClass, DnsRespCode = mibBuilder.importSymbols("DNS-SERVER-MIB", "DnsType", "DnsTime", "DnsQType", "DnsNameAsIndex", "DnsOpCode", "dns", "DnsName", "DnsQClass", "DnsClass", "DnsRespCode")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Integer32, Bits, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Gauge32, IpAddress, TimeTicks, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Bits", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Gauge32", "IpAddress", "TimeTicks", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
dnsResMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 32, 2))
if mibBuilder.loadTexts: dnsResMIB.setLastUpdated('9401282250Z')
if mibBuilder.loadTexts: dnsResMIB.setOrganization('IETF DNS Working Group')
dnsResMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 1))
dnsResConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 1, 1))
dnsResCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 1, 2))
dnsResLameDelegation = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 1, 3))
dnsResCache = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 1, 4))
dnsResNCache = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 1, 5))
dnsResOptCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 1, 6))
dnsResConfigImplementIdent = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResConfigImplementIdent.setStatus('current')
dnsResConfigService = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("recursiveOnly", 1), ("iterativeOnly", 2), ("recursiveAndIterative", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResConfigService.setStatus('current')
dnsResConfigMaxCnames = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResConfigMaxCnames.setStatus('current')
dnsResConfigSbeltTable = MibTable((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4), )
if mibBuilder.loadTexts: dnsResConfigSbeltTable.setStatus('current')
dnsResConfigSbeltEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1), ).setIndexNames((0, "DNS-RESOLVER-MIB", "dnsResConfigSbeltAddr"), (0, "DNS-RESOLVER-MIB", "dnsResConfigSbeltSubTree"), (0, "DNS-RESOLVER-MIB", "dnsResConfigSbeltClass"))
if mibBuilder.loadTexts: dnsResConfigSbeltEntry.setStatus('current')
dnsResConfigSbeltAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: dnsResConfigSbeltAddr.setStatus('current')
dnsResConfigSbeltName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 2), DnsName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsResConfigSbeltName.setStatus('current')
dnsResConfigSbeltRecursion = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("iterative", 1), ("recursive", 2), ("recursiveAndIterative", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsResConfigSbeltRecursion.setStatus('current')
dnsResConfigSbeltPref = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsResConfigSbeltPref.setStatus('current')
dnsResConfigSbeltSubTree = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 5), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsResConfigSbeltSubTree.setStatus('current')
dnsResConfigSbeltClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 6), DnsClass())
if mibBuilder.loadTexts: dnsResConfigSbeltClass.setStatus('current')
dnsResConfigSbeltStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsResConfigSbeltStatus.setStatus('current')
dnsResConfigUpTime = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 5), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResConfigUpTime.setStatus('current')
dnsResConfigResetTime = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 6), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResConfigResetTime.setStatus('current')
dnsResConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResConfigReset.setStatus('current')
dnsResCounterByOpcodeTable = MibTable((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3), )
if mibBuilder.loadTexts: dnsResCounterByOpcodeTable.setStatus('current')
dnsResCounterByOpcodeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1), ).setIndexNames((0, "DNS-RESOLVER-MIB", "dnsResCounterByOpcodeCode"))
if mibBuilder.loadTexts: dnsResCounterByOpcodeEntry.setStatus('current')
dnsResCounterByOpcodeCode = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1, 1), DnsOpCode())
if mibBuilder.loadTexts: dnsResCounterByOpcodeCode.setStatus('current')
dnsResCounterByOpcodeQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterByOpcodeQueries.setStatus('current')
dnsResCounterByOpcodeResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterByOpcodeResponses.setStatus('current')
dnsResCounterByRcodeTable = MibTable((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4), )
if mibBuilder.loadTexts: dnsResCounterByRcodeTable.setStatus('current')
dnsResCounterByRcodeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4, 1), ).setIndexNames((0, "DNS-RESOLVER-MIB", "dnsResCounterByRcodeCode"))
if mibBuilder.loadTexts: dnsResCounterByRcodeEntry.setStatus('current')
dnsResCounterByRcodeCode = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4, 1, 1), DnsRespCode())
if mibBuilder.loadTexts: dnsResCounterByRcodeCode.setStatus('current')
dnsResCounterByRcodeResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterByRcodeResponses.setStatus('current')
dnsResCounterNonAuthDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterNonAuthDataResps.setStatus('current')
dnsResCounterNonAuthNoDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterNonAuthNoDataResps.setStatus('current')
dnsResCounterMartians = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterMartians.setStatus('current')
dnsResCounterRecdResponses = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterRecdResponses.setStatus('current')
dnsResCounterUnparseResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterUnparseResps.setStatus('current')
dnsResCounterFallbacks = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCounterFallbacks.setStatus('current')
dnsResLameDelegationOverflows = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResLameDelegationOverflows.setStatus('current')
dnsResLameDelegationTable = MibTable((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2), )
if mibBuilder.loadTexts: dnsResLameDelegationTable.setStatus('current')
dnsResLameDelegationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1), ).setIndexNames((0, "DNS-RESOLVER-MIB", "dnsResLameDelegationSource"), (0, "DNS-RESOLVER-MIB", "dnsResLameDelegationName"), (0, "DNS-RESOLVER-MIB", "dnsResLameDelegationClass"))
if mibBuilder.loadTexts: dnsResLameDelegationEntry.setStatus('current')
dnsResLameDelegationSource = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: dnsResLameDelegationSource.setStatus('current')
dnsResLameDelegationName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 2), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsResLameDelegationName.setStatus('current')
dnsResLameDelegationClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 3), DnsClass())
if mibBuilder.loadTexts: dnsResLameDelegationClass.setStatus('current')
dnsResLameDelegationCounts = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResLameDelegationCounts.setStatus('current')
dnsResLameDelegationStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResLameDelegationStatus.setStatus('current')
dnsResCacheStatus = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("clear", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResCacheStatus.setStatus('current')
dnsResCacheMaxTTL = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 2), DnsTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResCacheMaxTTL.setStatus('current')
dnsResCacheGoodCaches = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCacheGoodCaches.setStatus('current')
dnsResCacheBadCaches = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCacheBadCaches.setStatus('current')
dnsResCacheRRTable = MibTable((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5), )
if mibBuilder.loadTexts: dnsResCacheRRTable.setStatus('current')
dnsResCacheRREntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1), ).setIndexNames((0, "DNS-RESOLVER-MIB", "dnsResCacheRRName"), (0, "DNS-RESOLVER-MIB", "dnsResCacheRRClass"), (0, "DNS-RESOLVER-MIB", "dnsResCacheRRType"), (0, "DNS-RESOLVER-MIB", "dnsResCacheRRIndex"))
if mibBuilder.loadTexts: dnsResCacheRREntry.setStatus('current')
dnsResCacheRRName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 1), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsResCacheRRName.setStatus('current')
dnsResCacheRRClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 2), DnsClass())
if mibBuilder.loadTexts: dnsResCacheRRClass.setStatus('current')
dnsResCacheRRType = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 3), DnsType())
if mibBuilder.loadTexts: dnsResCacheRRType.setStatus('current')
dnsResCacheRRTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 4), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCacheRRTTL.setStatus('current')
dnsResCacheRRElapsedTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 5), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCacheRRElapsedTTL.setStatus('current')
dnsResCacheRRSource = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCacheRRSource.setStatus('current')
dnsResCacheRRData = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCacheRRData.setStatus('current')
dnsResCacheRRStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResCacheRRStatus.setStatus('current')
dnsResCacheRRIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 9), Integer32())
if mibBuilder.loadTexts: dnsResCacheRRIndex.setStatus('current')
dnsResCacheRRPrettyName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 10), DnsName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResCacheRRPrettyName.setStatus('current')
dnsResNCacheStatus = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("clear", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResNCacheStatus.setStatus('current')
dnsResNCacheMaxTTL = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 2), DnsTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResNCacheMaxTTL.setStatus('current')
dnsResNCacheGoodNCaches = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheGoodNCaches.setStatus('current')
dnsResNCacheBadNCaches = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheBadNCaches.setStatus('current')
dnsResNCacheErrTable = MibTable((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5), )
if mibBuilder.loadTexts: dnsResNCacheErrTable.setStatus('current')
dnsResNCacheErrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1), ).setIndexNames((0, "DNS-RESOLVER-MIB", "dnsResNCacheErrQName"), (0, "DNS-RESOLVER-MIB", "dnsResNCacheErrQClass"), (0, "DNS-RESOLVER-MIB", "dnsResNCacheErrQType"), (0, "DNS-RESOLVER-MIB", "dnsResNCacheErrIndex"))
if mibBuilder.loadTexts: dnsResNCacheErrEntry.setStatus('current')
dnsResNCacheErrQName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 1), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsResNCacheErrQName.setStatus('current')
dnsResNCacheErrQClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 2), DnsQClass())
if mibBuilder.loadTexts: dnsResNCacheErrQClass.setStatus('current')
dnsResNCacheErrQType = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 3), DnsQType())
if mibBuilder.loadTexts: dnsResNCacheErrQType.setStatus('current')
dnsResNCacheErrTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 4), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheErrTTL.setStatus('current')
dnsResNCacheErrElapsedTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 5), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheErrElapsedTTL.setStatus('current')
dnsResNCacheErrSource = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheErrSource.setStatus('current')
dnsResNCacheErrCode = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonexistantName", 1), ("noData", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheErrCode.setStatus('current')
dnsResNCacheErrStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResNCacheErrStatus.setStatus('current')
dnsResNCacheErrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheErrIndex.setStatus('current')
dnsResNCacheErrPrettyName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 10), DnsName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResNCacheErrPrettyName.setStatus('current')
dnsResOptCounterReferals = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResOptCounterReferals.setStatus('current')
dnsResOptCounterRetrans = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResOptCounterRetrans.setStatus('current')
dnsResOptCounterNoResponses = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResOptCounterNoResponses.setStatus('current')
dnsResOptCounterRootRetrans = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResOptCounterRootRetrans.setStatus('current')
dnsResOptCounterInternals = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResOptCounterInternals.setStatus('current')
dnsResOptCounterInternalTimeOuts = MibScalar((1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsResOptCounterInternalTimeOuts.setStatus('current')
dnsResMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 2))
dnsResConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 2, 2, 1)).setObjects(("DNS-RESOLVER-MIB", "dnsResConfigImplementIdent"), ("DNS-RESOLVER-MIB", "dnsResConfigService"), ("DNS-RESOLVER-MIB", "dnsResConfigMaxCnames"), ("DNS-RESOLVER-MIB", "dnsResConfigSbeltAddr"), ("DNS-RESOLVER-MIB", "dnsResConfigSbeltName"), ("DNS-RESOLVER-MIB", "dnsResConfigSbeltRecursion"), ("DNS-RESOLVER-MIB", "dnsResConfigSbeltPref"), ("DNS-RESOLVER-MIB", "dnsResConfigSbeltSubTree"), ("DNS-RESOLVER-MIB", "dnsResConfigSbeltClass"), ("DNS-RESOLVER-MIB", "dnsResConfigSbeltStatus"), ("DNS-RESOLVER-MIB", "dnsResConfigUpTime"), ("DNS-RESOLVER-MIB", "dnsResConfigResetTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsResConfigGroup = dnsResConfigGroup.setStatus('current')
dnsResCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 2, 2, 2)).setObjects(("DNS-RESOLVER-MIB", "dnsResCounterByOpcodeCode"), ("DNS-RESOLVER-MIB", "dnsResCounterByOpcodeQueries"), ("DNS-RESOLVER-MIB", "dnsResCounterByOpcodeResponses"), ("DNS-RESOLVER-MIB", "dnsResCounterByRcodeCode"), ("DNS-RESOLVER-MIB", "dnsResCounterByRcodeResponses"), ("DNS-RESOLVER-MIB", "dnsResCounterNonAuthDataResps"), ("DNS-RESOLVER-MIB", "dnsResCounterNonAuthNoDataResps"), ("DNS-RESOLVER-MIB", "dnsResCounterMartians"), ("DNS-RESOLVER-MIB", "dnsResCounterRecdResponses"), ("DNS-RESOLVER-MIB", "dnsResCounterUnparseResps"), ("DNS-RESOLVER-MIB", "dnsResCounterFallbacks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsResCounterGroup = dnsResCounterGroup.setStatus('current')
dnsResLameDelegationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 2, 2, 3)).setObjects(("DNS-RESOLVER-MIB", "dnsResLameDelegationOverflows"), ("DNS-RESOLVER-MIB", "dnsResLameDelegationSource"), ("DNS-RESOLVER-MIB", "dnsResLameDelegationName"), ("DNS-RESOLVER-MIB", "dnsResLameDelegationClass"), ("DNS-RESOLVER-MIB", "dnsResLameDelegationCounts"), ("DNS-RESOLVER-MIB", "dnsResLameDelegationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsResLameDelegationGroup = dnsResLameDelegationGroup.setStatus('current')
dnsResCacheGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 2, 2, 4)).setObjects(("DNS-RESOLVER-MIB", "dnsResCacheStatus"), ("DNS-RESOLVER-MIB", "dnsResCacheMaxTTL"), ("DNS-RESOLVER-MIB", "dnsResCacheGoodCaches"), ("DNS-RESOLVER-MIB", "dnsResCacheBadCaches"), ("DNS-RESOLVER-MIB", "dnsResCacheRRName"), ("DNS-RESOLVER-MIB", "dnsResCacheRRClass"), ("DNS-RESOLVER-MIB", "dnsResCacheRRType"), ("DNS-RESOLVER-MIB", "dnsResCacheRRTTL"), ("DNS-RESOLVER-MIB", "dnsResCacheRRElapsedTTL"), ("DNS-RESOLVER-MIB", "dnsResCacheRRSource"), ("DNS-RESOLVER-MIB", "dnsResCacheRRData"), ("DNS-RESOLVER-MIB", "dnsResCacheRRStatus"), ("DNS-RESOLVER-MIB", "dnsResCacheRRIndex"), ("DNS-RESOLVER-MIB", "dnsResCacheRRPrettyName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsResCacheGroup = dnsResCacheGroup.setStatus('current')
dnsResNCacheGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 2, 2, 5)).setObjects(("DNS-RESOLVER-MIB", "dnsResNCacheStatus"), ("DNS-RESOLVER-MIB", "dnsResNCacheMaxTTL"), ("DNS-RESOLVER-MIB", "dnsResNCacheGoodNCaches"), ("DNS-RESOLVER-MIB", "dnsResNCacheBadNCaches"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrQName"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrQClass"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrQType"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrTTL"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrElapsedTTL"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrSource"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrCode"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrStatus"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrIndex"), ("DNS-RESOLVER-MIB", "dnsResNCacheErrPrettyName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsResNCacheGroup = dnsResNCacheGroup.setStatus('current')
dnsResOptCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 2, 2, 6)).setObjects(("DNS-RESOLVER-MIB", "dnsResOptCounterReferals"), ("DNS-RESOLVER-MIB", "dnsResOptCounterRetrans"), ("DNS-RESOLVER-MIB", "dnsResOptCounterNoResponses"), ("DNS-RESOLVER-MIB", "dnsResOptCounterRootRetrans"), ("DNS-RESOLVER-MIB", "dnsResOptCounterInternals"), ("DNS-RESOLVER-MIB", "dnsResOptCounterInternalTimeOuts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsResOptCounterGroup = dnsResOptCounterGroup.setStatus('current')
dnsResMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 2, 3))
dnsResMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 32, 2, 3, 1)).setObjects(("DNS-RESOLVER-MIB", "dnsResConfigGroup"), ("DNS-RESOLVER-MIB", "dnsResCounterGroup"), ("DNS-RESOLVER-MIB", "dnsResCacheGroup"), ("DNS-RESOLVER-MIB", "dnsResNCacheGroup"), ("DNS-RESOLVER-MIB", "dnsResLameDelegationGroup"), ("DNS-RESOLVER-MIB", "dnsResOptCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsResMIBCompliance = dnsResMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("DNS-RESOLVER-MIB", dnsResConfigSbeltAddr=dnsResConfigSbeltAddr, dnsResCounterByRcodeCode=dnsResCounterByRcodeCode, PYSNMP_MODULE_ID=dnsResMIB, dnsResCounterUnparseResps=dnsResCounterUnparseResps, dnsResNCacheErrEntry=dnsResNCacheErrEntry, dnsResLameDelegationGroup=dnsResLameDelegationGroup, dnsResOptCounter=dnsResOptCounter, dnsResMIB=dnsResMIB, dnsResCounterByOpcodeTable=dnsResCounterByOpcodeTable, dnsResLameDelegationCounts=dnsResLameDelegationCounts, dnsResConfigSbeltStatus=dnsResConfigSbeltStatus, dnsResConfigMaxCnames=dnsResConfigMaxCnames, dnsResCacheRRType=dnsResCacheRRType, dnsResNCacheErrCode=dnsResNCacheErrCode, dnsResLameDelegationSource=dnsResLameDelegationSource, dnsResCacheGoodCaches=dnsResCacheGoodCaches, dnsResConfigSbeltPref=dnsResConfigSbeltPref, dnsResCache=dnsResCache, dnsResNCacheErrQClass=dnsResNCacheErrQClass, dnsResCounterNonAuthDataResps=dnsResCounterNonAuthDataResps, dnsResOptCounterNoResponses=dnsResOptCounterNoResponses, dnsResConfigSbeltEntry=dnsResConfigSbeltEntry, dnsResMIBGroups=dnsResMIBGroups, dnsResCacheRRElapsedTTL=dnsResCacheRRElapsedTTL, dnsResNCacheErrSource=dnsResNCacheErrSource, dnsResCacheRRIndex=dnsResCacheRRIndex, dnsResNCacheStatus=dnsResNCacheStatus, dnsResMIBObjects=dnsResMIBObjects, dnsResCacheRRTTL=dnsResCacheRRTTL, dnsResConfigSbeltTable=dnsResConfigSbeltTable, dnsResOptCounterRetrans=dnsResOptCounterRetrans, dnsResCacheBadCaches=dnsResCacheBadCaches, dnsResLameDelegationEntry=dnsResLameDelegationEntry, dnsResMIBCompliances=dnsResMIBCompliances, dnsResCounterByOpcodeEntry=dnsResCounterByOpcodeEntry, dnsResLameDelegationStatus=dnsResLameDelegationStatus, dnsResOptCounterInternals=dnsResOptCounterInternals, dnsResCacheRRName=dnsResCacheRRName, dnsResLameDelegation=dnsResLameDelegation, dnsResConfigReset=dnsResConfigReset, dnsResLameDelegationClass=dnsResLameDelegationClass, dnsResNCacheGroup=dnsResNCacheGroup, dnsResCacheRRClass=dnsResCacheRRClass, dnsResCounterByRcodeEntry=dnsResCounterByRcodeEntry, dnsResCacheRRSource=dnsResCacheRRSource, dnsResNCacheMaxTTL=dnsResNCacheMaxTTL, dnsResCounterByOpcodeResponses=dnsResCounterByOpcodeResponses, dnsResConfigSbeltSubTree=dnsResConfigSbeltSubTree, dnsResConfig=dnsResConfig, dnsResNCacheBadNCaches=dnsResNCacheBadNCaches, dnsResNCacheErrTable=dnsResNCacheErrTable, dnsResCacheRRTable=dnsResCacheRRTable, dnsResCounter=dnsResCounter, dnsResCacheMaxTTL=dnsResCacheMaxTTL, dnsResCounterGroup=dnsResCounterGroup, dnsResLameDelegationTable=dnsResLameDelegationTable, dnsResNCacheErrIndex=dnsResNCacheErrIndex, dnsResCounterMartians=dnsResCounterMartians, dnsResConfigService=dnsResConfigService, dnsResCacheStatus=dnsResCacheStatus, dnsResConfigImplementIdent=dnsResConfigImplementIdent, dnsResConfigGroup=dnsResConfigGroup, dnsResOptCounterGroup=dnsResOptCounterGroup, dnsResCacheRRPrettyName=dnsResCacheRRPrettyName, dnsResLameDelegationOverflows=dnsResLameDelegationOverflows, dnsResCounterFallbacks=dnsResCounterFallbacks, dnsResNCacheErrElapsedTTL=dnsResNCacheErrElapsedTTL, dnsResNCacheErrStatus=dnsResNCacheErrStatus, dnsResOptCounterReferals=dnsResOptCounterReferals, dnsResConfigResetTime=dnsResConfigResetTime, dnsResConfigSbeltRecursion=dnsResConfigSbeltRecursion, dnsResCounterNonAuthNoDataResps=dnsResCounterNonAuthNoDataResps, dnsResMIBCompliance=dnsResMIBCompliance, dnsResNCache=dnsResNCache, dnsResCounterByRcodeTable=dnsResCounterByRcodeTable, dnsResConfigUpTime=dnsResConfigUpTime, dnsResConfigSbeltClass=dnsResConfigSbeltClass, dnsResLameDelegationName=dnsResLameDelegationName, dnsResCacheGroup=dnsResCacheGroup, dnsResCacheRREntry=dnsResCacheRREntry, dnsResNCacheGoodNCaches=dnsResNCacheGoodNCaches, dnsResOptCounterInternalTimeOuts=dnsResOptCounterInternalTimeOuts, dnsResNCacheErrPrettyName=dnsResNCacheErrPrettyName, dnsResNCacheErrQType=dnsResNCacheErrQType, dnsResCacheRRData=dnsResCacheRRData, dnsResConfigSbeltName=dnsResConfigSbeltName, dnsResCacheRRStatus=dnsResCacheRRStatus, dnsResCounterByOpcodeQueries=dnsResCounterByOpcodeQueries, dnsResCounterByOpcodeCode=dnsResCounterByOpcodeCode, dnsResCounterByRcodeResponses=dnsResCounterByRcodeResponses, dnsResNCacheErrQName=dnsResNCacheErrQName, dnsResOptCounterRootRetrans=dnsResOptCounterRootRetrans, dnsResNCacheErrTTL=dnsResNCacheErrTTL, dnsResCounterRecdResponses=dnsResCounterRecdResponses)
