#
# PySNMP MIB module F5-BIGIP-WAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-BIGIP-WAM-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:17 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
bigipCompliances, bigipTrafficMgmt, bigipGroups, LongDisplayString = mibBuilder.importSymbols("F5-BIGIP-COMMON-MIB", "bigipCompliances", "bigipTrafficMgmt", "bigipGroups", "LongDisplayString")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Bits, Opaque, NotificationType, Counter64, MibIdentifier, ObjectIdentity, enterprises, Integer32, Counter32, TimeTicks, iso, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Bits", "Opaque", "NotificationType", "Counter64", "MibIdentifier", "ObjectIdentity", "enterprises", "Integer32", "Counter32", "TimeTicks", "iso", "Unsigned32", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
bigipWAM = ModuleIdentity((1, 3, 6, 1, 4, 1, 3375, 2, 7))
if mibBuilder.loadTexts: bigipWAM.setLastUpdated('202004092224Z')
if mibBuilder.loadTexts: bigipWAM.setOrganization('F5 Networks, Inc.')
if mibBuilder.loadTexts: bigipWAM.setContactInfo('postal: F5 Networks, Inc. \n\t \t  801 Fifth Avenue\n                  Seattle, WA 98104\n          phone:  (206) 272-6500\n          email:  support@f5.com')
if mibBuilder.loadTexts: bigipWAM.setDescription('Top-level infrastructure of the F5 enterprise MIB tree.')
wamAppStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1))
wamAppStatResetStats = MibScalar((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wamAppStatResetStats.setStatus('current')
if mibBuilder.loadTexts: wamAppStatResetStats.setDescription('The action to reset resettable statistics data in wamAppStat.\n\t\t Setting this value to 1 will reset statistics data.\n\t\t Note, some statistics data may not be reset including data that are incremental counters.')
wamAppStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatNumber.setStatus('current')
if mibBuilder.loadTexts: wamAppStatNumber.setDescription('The number of wamAppStat entries in the table.')
wamAppStatTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3), )
if mibBuilder.loadTexts: wamAppStatTable.setStatus('current')
if mibBuilder.loadTexts: wamAppStatTable.setDescription('A table containing per application statistics for the web accelerator module')
wamAppStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1), ).setIndexNames((0, "F5-BIGIP-WAM-MIB", "wamAppStatName"))
if mibBuilder.loadTexts: wamAppStatEntry.setStatus('current')
if mibBuilder.loadTexts: wamAppStatEntry.setDescription('Columns in the wamAppStat Table')
wamAppStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 1), LongDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatName.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatName.setDescription('The name of the web accelerator application.')
wamAppStatVsName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 2), LongDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatVsName.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatVsName.setDescription('The name of the virtual server.')
wamAppStatRqstTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatRqstTotal.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatRqstTotal.setDescription('The total number of requests made to this web accelerator\n\t     application.')
wamAppStatProxied = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied.setDescription('The total number of requests proxied by this web accelerator\n\t     application.')
wamAppStatProxiedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedBytes.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedBytes.setDescription('The total number of requests proxied by this web accelerator\n\t     application measured in bytes.')
wamAppStatProxied1500 = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied1500.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied1500.setDescription('The total number of requests between 0 and 1500 bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxied10k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied10k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied10k.setDescription('The total number of requests between 1500 and 10K bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxied50k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied50k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied50k.setDescription('The total number of requests between 10K and 50K bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxied100k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied100k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied100k.setDescription('The total number of requests between 50K and 100K bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxied500k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied500k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied500k.setDescription('The total number of requests between 100K and 500K bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxied1m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied1m.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied1m.setDescription('The total number of requests between 500k and 1M bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxied5m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied5m.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxied5m.setDescription('The total number of requests between 1M and 5M bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxiedLarge = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedLarge.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedLarge.setDescription('The total number of requests larger than 5M bytes proxied\n\t     by this web accelerator application.')
wamAppStatProxiedNew = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedNew.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedNew.setDescription('The total number of new requests proxied by this\n\t     web accelerator application.')
wamAppStatProxiedExpired = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedExpired.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedExpired.setDescription('The total number of expired requests proxied by this\n\t     web accelerator application.')
wamAppStatProxiedPerPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerPolicy.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedPerPolicy.setDescription('The total number of requests proxied per policy by this\n\t     web accelerator application.')
wamAppStatProxiedPerIrule = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerIrule.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedPerIrule.setDescription('The total number of requests proxied per iRule by this\n\t     web accelerator application.')
wamAppStatProxiedPerInvalidation = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerInvalidation.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedPerInvalidation.setDescription('The total number of requests proxied by invalidation rules by this\n\t     web accelerator application.')
wamAppStatProxiedPerClientRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerClientRequest.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedPerClientRequest.setDescription('The total number of requests proxied by client request headers by this\n\t    web accelerator application.')
wamAppStatProxiedBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedBypass.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatProxiedBypass.setDescription('The total number of proxy requests bypassed by this\n\t     web accelerator application.')
wamAppStatFromCache = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache.setDescription('The total number of requests served from cache by this\n\t     web accelerator application.')
wamAppStatFromCacheBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCacheBytes.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCacheBytes.setDescription('The total number of request bytes served from cache by this\n\t     web accelerator application.')
wamAppStatFromCache1500 = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache1500.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache1500.setDescription('The total number of requests between 0 and 1500 bytes served\n\t     from cache by this web accelerator application.')
wamAppStatFromCache10k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache10k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache10k.setDescription('The total number of requests between 1500 and 10K bytes served\n\t     from cache by this web accelerator application.')
wamAppStatFromCache50k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache50k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache50k.setDescription('The total number of requests between 10K and 50K bytes served\n\t     from cache by this web accelerator application.')
wamAppStatFromCache100k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache100k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache100k.setDescription('The total number of requests between 50K and 100K bytes served\n\t     from cache by this web accelerator application.')
wamAppStatFromCache500k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache500k.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache500k.setDescription('The total number of requests between 100K and 500K bytes served\n\t     from cache by this web accelerator application.')
wamAppStatFromCache1m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache1m.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache1m.setDescription('The total number of requests between 500k and 1M bytes served\n\t     from cache by this web accelerator application.')
wamAppStatFromCache5m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache5m.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCache5m.setDescription('The total number of requests between 1M and 5M bytes served\n\t     from cache by this web accelerator application.')
wamAppStatFromCacheLarge = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCacheLarge.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatFromCacheLarge.setDescription('The total number of requests larger than 5M bytes served\n\t     from cache by this web accelerator application.')
wamAppStatOws2xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws2xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatOws2xx.setDescription('The number of origin web server responses in the range of\n\t     200 to 206 (successful responses).')
wamAppStatOws3xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws3xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatOws3xx.setDescription('The number of origin web server responses in the range of\n\t     300 to 307 (redirection responses).')
wamAppStatOws4xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws4xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatOws4xx.setDescription('The number of origin web server responses in the range of\n\t     400 to 417 (client errors).')
wamAppStatOws5xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws5xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatOws5xx.setDescription('The number of origin web server responses in the range of\n\t    500 to 505 (server errors).')
wamAppStatOwsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOwsDropped.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatOwsDropped.setDescription('The number of requests dropped by origin web server.')
wamAppStatOwsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOwsRejected.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatOwsRejected.setDescription('The number of requests rejected by origin web server.')
wamAppStatWam2xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam2xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatWam2xx.setDescription('The number of responses in the range of 200 to 206 \n\t     (successful responses) served by this web accelerator application.')
wamAppStatWam3xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam3xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatWam3xx.setDescription('The number of responses in the range of 300 to 307\n\t     (redirection responses) served by this web accelerator application.')
wamAppStatWam4xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam4xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatWam4xx.setDescription('The number of responses in the range of 400 to 417\n\t     (client errors) served by this web accelerator application.')
wamAppStatWam5xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam5xx.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatWam5xx.setDescription('The number of responses in the range of 500 to 505\n\t     (server errors) served by this web accelerator application.')
wamAppStatWam503 = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam503.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatWam503.setDescription('The number of 503 response served by this web accelerator application.')
wamAppStatWamDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWamDropped.setStatus('obsolete')
if mibBuilder.loadTexts: wamAppStatWamDropped.setDescription('The number of requests dropped by this web accelerator application.')
bigipWAMCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3375, 2, 5, 1, 7)).setObjects(("F5-BIGIP-WAM-MIB", "bigipWAMGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bigipWAMCompliance = bigipWAMCompliance.setStatus('current')
if mibBuilder.loadTexts: bigipWAMCompliance.setDescription('This specifies the objects that are required to claim \n                 compliance to F5 Traffic Management System.')
bigipWAMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 7))
wamAppStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 7, 1)).setObjects(("F5-BIGIP-WAM-MIB", "wamAppStatResetStats"), ("F5-BIGIP-WAM-MIB", "wamAppStatNumber"), ("F5-BIGIP-WAM-MIB", "wamAppStatName"), ("F5-BIGIP-WAM-MIB", "wamAppStatVsName"), ("F5-BIGIP-WAM-MIB", "wamAppStatRqstTotal"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedBytes"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied1500"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied10k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied50k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied100k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied500k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied1m"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied5m"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedLarge"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedNew"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedExpired"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerPolicy"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerIrule"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerInvalidation"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerClientRequest"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedBypass"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCacheBytes"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache1500"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache10k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache50k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache100k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache500k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache1m"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache5m"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCacheLarge"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws2xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws3xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws4xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws5xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOwsDropped"), ("F5-BIGIP-WAM-MIB", "wamAppStatOwsRejected"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam2xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam3xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam4xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam5xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam503"), ("F5-BIGIP-WAM-MIB", "wamAppStatWamDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wamAppStatGroup = wamAppStatGroup.setStatus('current')
if mibBuilder.loadTexts: wamAppStatGroup.setDescription('A collection of objects of wamAppStat MIB.')
mibBuilder.exportSymbols("F5-BIGIP-WAM-MIB", wamAppStatFromCache50k=wamAppStatFromCache50k, wamAppStatWam4xx=wamAppStatWam4xx, wamAppStatOws5xx=wamAppStatOws5xx, wamAppStatProxiedPerClientRequest=wamAppStatProxiedPerClientRequest, wamAppStatProxied10k=wamAppStatProxied10k, wamAppStatProxied50k=wamAppStatProxied50k, wamAppStatWamDropped=wamAppStatWamDropped, wamAppStatProxiedLarge=wamAppStatProxiedLarge, wamAppStatFromCache=wamAppStatFromCache, wamAppStatOws3xx=wamAppStatOws3xx, wamAppStatProxied=wamAppStatProxied, wamAppStatProxiedPerInvalidation=wamAppStatProxiedPerInvalidation, wamAppStat=wamAppStat, wamAppStatWam5xx=wamAppStatWam5xx, bigipWAMCompliance=bigipWAMCompliance, wamAppStatProxiedPerPolicy=wamAppStatProxiedPerPolicy, wamAppStatWam3xx=wamAppStatWam3xx, wamAppStatProxied500k=wamAppStatProxied500k, bigipWAM=bigipWAM, wamAppStatName=wamAppStatName, wamAppStatVsName=wamAppStatVsName, wamAppStatNumber=wamAppStatNumber, wamAppStatProxied100k=wamAppStatProxied100k, wamAppStatProxied1m=wamAppStatProxied1m, wamAppStatFromCache1m=wamAppStatFromCache1m, wamAppStatProxiedPerIrule=wamAppStatProxiedPerIrule, wamAppStatWam2xx=wamAppStatWam2xx, wamAppStatWam503=wamAppStatWam503, wamAppStatTable=wamAppStatTable, wamAppStatProxiedExpired=wamAppStatProxiedExpired, wamAppStatFromCache100k=wamAppStatFromCache100k, wamAppStatGroup=wamAppStatGroup, wamAppStatFromCache1500=wamAppStatFromCache1500, wamAppStatProxied5m=wamAppStatProxied5m, wamAppStatProxiedNew=wamAppStatProxiedNew, bigipWAMGroups=bigipWAMGroups, wamAppStatResetStats=wamAppStatResetStats, wamAppStatFromCache500k=wamAppStatFromCache500k, PYSNMP_MODULE_ID=bigipWAM, wamAppStatEntry=wamAppStatEntry, wamAppStatOwsRejected=wamAppStatOwsRejected, wamAppStatProxied1500=wamAppStatProxied1500, wamAppStatFromCacheLarge=wamAppStatFromCacheLarge, wamAppStatProxiedBytes=wamAppStatProxiedBytes, wamAppStatFromCacheBytes=wamAppStatFromCacheBytes, wamAppStatFromCache5m=wamAppStatFromCache5m, wamAppStatProxiedBypass=wamAppStatProxiedBypass, wamAppStatOwsDropped=wamAppStatOwsDropped, wamAppStatOws4xx=wamAppStatOws4xx, wamAppStatOws2xx=wamAppStatOws2xx, wamAppStatFromCache10k=wamAppStatFromCache10k, wamAppStatRqstTotal=wamAppStatRqstTotal)
