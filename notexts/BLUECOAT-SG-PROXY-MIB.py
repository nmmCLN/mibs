#
# PySNMP MIB module BLUECOAT-SG-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-PROXY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:10:14 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, NotificationType, MibIdentifier, iso, ModuleIdentity, Unsigned32, Integer32, ObjectIdentity, Counter32, IpAddress, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "Unsigned32", "Integer32", "ObjectIdentity", "Counter32", "IpAddress", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bluecoatSGProxyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 11))
bluecoatSGProxyMIB.setRevisions(('2011-11-01 03:00', '2007-11-05 03:00', '2007-08-28 03:00',))
if mibBuilder.loadTexts: bluecoatSGProxyMIB.setLastUpdated('201111010300Z')
if mibBuilder.loadTexts: bluecoatSGProxyMIB.setOrganization('Blue Coat Systems, Inc.')
sgProxyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1))
sgProxySystem = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2))
sgProxyHttp = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3))
sgProxyAdmin = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyAdmin.setStatus('current')
sgProxySoftware = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxySoftware.setStatus('current')
sgProxyVersion = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyVersion.setStatus('current')
sgProxySerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxySerialNumber.setStatus('current')
sgProxyCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1))
sgProxyCache = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2))
sgProxyMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3))
sgProxyCpuCoreTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4), )
if mibBuilder.loadTexts: sgProxyCpuCoreTable.setStatus('current')
sgProxyCpuUpTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 1), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuUpTime.setStatus('deprecated')
sgProxyCpuBusyTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 2), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuBusyTime.setStatus('deprecated')
sgProxyCpuIdleTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 3), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuIdleTime.setStatus('deprecated')
sgProxyCpuUpTimeSinceLastAccess = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 4), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuUpTimeSinceLastAccess.setStatus('deprecated')
sgProxyCpuBusyTimeSinceLastAccess = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 5), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuBusyTimeSinceLastAccess.setStatus('deprecated')
sgProxyCpuIdleTimeSinceLastAccess = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 6), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuIdleTimeSinceLastAccess.setStatus('deprecated')
sgProxyCpuBusyPerCent = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 7), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuBusyPerCent.setStatus('deprecated')
sgProxyCpuIdlePerCent = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 8), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuIdlePerCent.setStatus('deprecated')
sgProxyStorage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyStorage.setStatus('current')
sgProxyNumObjects = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyNumObjects.setStatus('current')
sgProxyMemAvailable = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 1), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemAvailable.setStatus('current')
sgProxyMemCacheUsage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 2), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemCacheUsage.setStatus('current')
sgProxyMemSysUsage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 3), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemSysUsage.setStatus('current')
sgProxyMemoryPressure = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 4), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemoryPressure.setStatus('current')
sgProxyCpuCoreTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1), ).setIndexNames((0, "BLUECOAT-SG-PROXY-MIB", "sgProxyCpuCoreIndex"))
if mibBuilder.loadTexts: sgProxyCpuCoreTableEntry.setStatus('current')
sgProxyCpuCoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: sgProxyCpuCoreIndex.setStatus('current')
sgProxyCpuCoreUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 2), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreUpTime.setStatus('current')
sgProxyCpuCoreBusyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 3), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreBusyTime.setStatus('current')
sgProxyCpuCoreIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 4), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreIdleTime.setStatus('current')
sgProxyCpuCoreUpTimeSinceLastAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 5), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreUpTimeSinceLastAccess.setStatus('current')
sgProxyCpuCoreBusyTimeSinceLastAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 6), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreBusyTimeSinceLastAccess.setStatus('current')
sgProxyCpuCoreIdleTimeSinceLastAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 7), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreIdleTimeSinceLastAccess.setStatus('current')
sgProxyCpuCoreBusyPerCent = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 8), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreBusyPerCent.setStatus('current')
sgProxyCpuCoreIdlePerCent = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 9), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreIdlePerCent.setStatus('current')
sgProxyHttpPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1))
sgProxyHttpResponse = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2))
sgProxyHttpMedian = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3))
sgProxyHttpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1))
sgProxyHttpServer = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2))
sgProxyHttpConnections = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3))
sgProxyHttpClientRequests = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientRequests.setStatus('current')
sgProxyHttpClientHits = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientHits.setStatus('current')
sgProxyHttpClientPartialHits = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientPartialHits.setStatus('current')
sgProxyHttpClientMisses = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientMisses.setStatus('current')
sgProxyHttpClientErrors = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientErrors.setStatus('current')
sgProxyHttpClientRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 6), Gauge32()).setUnits('Requests Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientRequestRate.setStatus('current')
sgProxyHttpClientHitRate = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 7), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientHitRate.setStatus('current')
sgProxyHttpClientByteHitRate = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 8), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientByteHitRate.setStatus('current')
sgProxyHttpClientInBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 9), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientInBytes.setStatus('current')
sgProxyHttpClientOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 10), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientOutBytes.setStatus('current')
sgProxyHttpServerRequests = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerRequests.setStatus('current')
sgProxyHttpServerErrors = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerErrors.setStatus('current')
sgProxyHttpServerInBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 3), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerInBytes.setStatus('current')
sgProxyHttpServerOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 4), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerOutBytes.setStatus('current')
sgProxyHttpClientConnections = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientConnections.setStatus('current')
sgProxyHttpClientConnectionsActive = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientConnectionsActive.setStatus('current')
sgProxyHttpClientConnectionsIdle = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientConnectionsIdle.setStatus('current')
sgProxyHttpServerConnections = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerConnections.setStatus('current')
sgProxyHttpServerConnectionsActive = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerConnectionsActive.setStatus('current')
sgProxyHttpServerConnectionsIdle = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerConnectionsIdle.setStatus('current')
sgProxyHttpResponseTime = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1))
sgProxyHttpResponseFirstByte = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2))
sgProxyHttpResponseByteRate = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3))
sgProxyHttpResponseSize = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4))
sgProxyHttpServiceTimeAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 1), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimeAll.setStatus('current')
sgProxyHttpServiceTimeHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 2), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimeHit.setStatus('current')
sgProxyHttpServiceTimePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 3), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimePartialHit.setStatus('current')
sgProxyHttpServiceTimeMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 4), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimeMiss.setStatus('current')
sgProxyHttpTotalFetchTimeAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 5), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeAll.setStatus('current')
sgProxyHttpTotalFetchTimeHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 6), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeHit.setStatus('current')
sgProxyHttpTotalFetchTimePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 7), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimePartialHit.setStatus('current')
sgProxyHttpTotalFetchTimeMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 8), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeMiss.setStatus('current')
sgProxyHttpFirstByteAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 1), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstByteAll.setStatus('current')
sgProxyHttpFirstByteHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 2), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstByteHit.setStatus('current')
sgProxyHttpFirstBytePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 3), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstBytePartialHit.setStatus('current')
sgProxyHttpFirstByteMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 4), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstByteMiss.setStatus('current')
sgProxyHttpByteRateAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 1), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRateAll.setStatus('current')
sgProxyHttpByteRateHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 2), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRateHit.setStatus('current')
sgProxyHttpByteRatePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 3), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRatePartialHit.setStatus('current')
sgProxyHttpByteRateMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 4), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRateMiss.setStatus('current')
sgProxyHttpResponseSizeAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 1), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizeAll.setStatus('current')
sgProxyHttpResponseSizeHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 2), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizeHit.setStatus('current')
sgProxyHttpResponseSizePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 3), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizePartialHit.setStatus('current')
sgProxyHttpResponseSizeMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 4), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizeMiss.setStatus('current')
sgProxyHttpMedianServiceTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1), )
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTable.setStatus('current')
sgProxyHttpMedianServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-PROXY-MIB", "sgProxyHttpMedianServiceTime"))
if mibBuilder.loadTexts: sgProxyHttpMedianServiceEntry.setStatus('current')
sgProxyHttpMedianServiceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5, 60))).clone(namedValues=NamedValues(("one", 1), ("five", 5), ("sixty", 60)))).setUnits('Minutes')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTime.setStatus('current')
sgProxyHttpMedianServiceTimeAll = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 2), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeAll.setStatus('current')
sgProxyHttpMedianServiceTimeHit = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 3), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeHit.setStatus('current')
sgProxyHttpMedianServiceTimePartialHit = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 4), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimePartialHit.setStatus('current')
sgProxyHttpMedianServiceTimeMiss = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 5), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeMiss.setStatus('current')
sgProxyDnsMedianServiceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 6), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyDnsMedianServiceTime.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-PROXY-MIB", sgProxyHttpMedianServiceTimeHit=sgProxyHttpMedianServiceTimeHit, sgProxyHttpClientConnectionsActive=sgProxyHttpClientConnectionsActive, sgProxyNumObjects=sgProxyNumObjects, sgProxyCpuCoreBusyPerCent=sgProxyCpuCoreBusyPerCent, sgProxyHttpResponseTime=sgProxyHttpResponseTime, sgProxyHttpClientInBytes=sgProxyHttpClientInBytes, sgProxyHttpByteRateMiss=sgProxyHttpByteRateMiss, sgProxyCpuCoreIdleTimeSinceLastAccess=sgProxyCpuCoreIdleTimeSinceLastAccess, sgProxyCpuCoreBusyTimeSinceLastAccess=sgProxyCpuCoreBusyTimeSinceLastAccess, sgProxyHttpByteRateHit=sgProxyHttpByteRateHit, sgProxyCpuIdlePerCent=sgProxyCpuIdlePerCent, sgProxyHttpClientMisses=sgProxyHttpClientMisses, sgProxyCpu=sgProxyCpu, sgProxyCpuCoreUpTimeSinceLastAccess=sgProxyCpuCoreUpTimeSinceLastAccess, sgProxyHttpByteRateAll=sgProxyHttpByteRateAll, sgProxyHttpConnections=sgProxyHttpConnections, sgProxyHttpResponse=sgProxyHttpResponse, sgProxyHttpMedianServiceTimePartialHit=sgProxyHttpMedianServiceTimePartialHit, sgProxyHttpClientByteHitRate=sgProxyHttpClientByteHitRate, sgProxyHttpResponseSizePartialHit=sgProxyHttpResponseSizePartialHit, sgProxyHttpServerConnectionsIdle=sgProxyHttpServerConnectionsIdle, sgProxyCpuCoreTable=sgProxyCpuCoreTable, sgProxyHttpFirstByteMiss=sgProxyHttpFirstByteMiss, sgProxyHttpResponseSizeHit=sgProxyHttpResponseSizeHit, sgProxyHttpServerInBytes=sgProxyHttpServerInBytes, sgProxyHttpFirstByteAll=sgProxyHttpFirstByteAll, sgProxyHttpResponseByteRate=sgProxyHttpResponseByteRate, sgProxyHttpServerOutBytes=sgProxyHttpServerOutBytes, sgProxyHttp=sgProxyHttp, sgProxySoftware=sgProxySoftware, sgProxyHttpMedianServiceTimeMiss=sgProxyHttpMedianServiceTimeMiss, sgProxyHttpClientRequestRate=sgProxyHttpClientRequestRate, sgProxyHttpServiceTimeMiss=sgProxyHttpServiceTimeMiss, sgProxyCpuBusyTimeSinceLastAccess=sgProxyCpuBusyTimeSinceLastAccess, sgProxyCpuIdleTime=sgProxyCpuIdleTime, sgProxySystem=sgProxySystem, sgProxyHttpClientHitRate=sgProxyHttpClientHitRate, sgProxyMemCacheUsage=sgProxyMemCacheUsage, sgProxyHttpServiceTimeAll=sgProxyHttpServiceTimeAll, sgProxyCpuBusyTime=sgProxyCpuBusyTime, sgProxyCache=sgProxyCache, sgProxyHttpTotalFetchTimeMiss=sgProxyHttpTotalFetchTimeMiss, sgProxyVersion=sgProxyVersion, sgProxyHttpClient=sgProxyHttpClient, sgProxyHttpServiceTimePartialHit=sgProxyHttpServiceTimePartialHit, sgProxyHttpFirstBytePartialHit=sgProxyHttpFirstBytePartialHit, sgProxyHttpFirstByteHit=sgProxyHttpFirstByteHit, sgProxyHttpResponseSizeMiss=sgProxyHttpResponseSizeMiss, sgProxySerialNumber=sgProxySerialNumber, sgProxyCpuCoreIdlePerCent=sgProxyCpuCoreIdlePerCent, sgProxyCpuCoreIdleTime=sgProxyCpuCoreIdleTime, sgProxyCpuCoreUpTime=sgProxyCpuCoreUpTime, sgProxyHttpTotalFetchTimeHit=sgProxyHttpTotalFetchTimeHit, sgProxyHttpMedianServiceTime=sgProxyHttpMedianServiceTime, sgProxyAdmin=sgProxyAdmin, sgProxyHttpTotalFetchTimeAll=sgProxyHttpTotalFetchTimeAll, sgProxyHttpServer=sgProxyHttpServer, sgProxyHttpResponseSizeAll=sgProxyHttpResponseSizeAll, sgProxyMemory=sgProxyMemory, sgProxyMemSysUsage=sgProxyMemSysUsage, sgProxyHttpClientConnectionsIdle=sgProxyHttpClientConnectionsIdle, sgProxyHttpTotalFetchTimePartialHit=sgProxyHttpTotalFetchTimePartialHit, PYSNMP_MODULE_ID=bluecoatSGProxyMIB, sgProxyHttpPerf=sgProxyHttpPerf, sgProxyCpuUpTimeSinceLastAccess=sgProxyCpuUpTimeSinceLastAccess, sgProxyHttpClientOutBytes=sgProxyHttpClientOutBytes, sgProxyHttpResponseSize=sgProxyHttpResponseSize, sgProxyMemoryPressure=sgProxyMemoryPressure, sgProxyHttpMedian=sgProxyHttpMedian, sgProxyCpuBusyPerCent=sgProxyCpuBusyPerCent, sgProxyHttpClientPartialHits=sgProxyHttpClientPartialHits, sgProxyHttpServerRequests=sgProxyHttpServerRequests, sgProxyHttpServerConnections=sgProxyHttpServerConnections, sgProxyHttpByteRatePartialHit=sgProxyHttpByteRatePartialHit, sgProxyCpuIdleTimeSinceLastAccess=sgProxyCpuIdleTimeSinceLastAccess, sgProxyHttpClientRequests=sgProxyHttpClientRequests, sgProxyHttpResponseFirstByte=sgProxyHttpResponseFirstByte, sgProxyDnsMedianServiceTime=sgProxyDnsMedianServiceTime, sgProxyMemAvailable=sgProxyMemAvailable, sgProxyCpuUpTime=sgProxyCpuUpTime, sgProxyHttpClientErrors=sgProxyHttpClientErrors, sgProxyHttpServerConnectionsActive=sgProxyHttpServerConnectionsActive, sgProxyCpuCoreTableEntry=sgProxyCpuCoreTableEntry, sgProxyHttpClientConnections=sgProxyHttpClientConnections, sgProxyConfig=sgProxyConfig, sgProxyCpuCoreBusyTime=sgProxyCpuCoreBusyTime, sgProxyHttpMedianServiceEntry=sgProxyHttpMedianServiceEntry, sgProxyStorage=sgProxyStorage, sgProxyCpuCoreIndex=sgProxyCpuCoreIndex, sgProxyHttpServiceTimeHit=sgProxyHttpServiceTimeHit, bluecoatSGProxyMIB=bluecoatSGProxyMIB, sgProxyHttpClientHits=sgProxyHttpClientHits, sgProxyHttpServerErrors=sgProxyHttpServerErrors, sgProxyHttpMedianServiceTable=sgProxyHttpMedianServiceTable, sgProxyHttpMedianServiceTimeAll=sgProxyHttpMedianServiceTimeAll)
