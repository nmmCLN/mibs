#
# PySNMP MIB module COLUBRIS-CDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-CDP-MIB.my
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:54 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ObjectIdentity, Counter32, Bits, ModuleIdentity, Integer32, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ObjectIdentity", "Counter32", "Bits", "ModuleIdentity", "Integer32", "NotificationType", "iso", "Gauge32")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
colubrisCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 9))
if mibBuilder.loadTexts: colubrisCdpMIB.setLastUpdated('200402200000Z')
if mibBuilder.loadTexts: colubrisCdpMIB.setOrganization('Colubris Networks, Inc.')
colubrisCdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1))
coCdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1))
coCdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2))
coCdpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1), )
if mibBuilder.loadTexts: coCdpCacheTable.setStatus('current')
coCdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-CDP-MIB", "coCdpCacheDeviceIndex"))
if mibBuilder.loadTexts: coCdpCacheEntry.setStatus('current')
coCdpCacheDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coCdpCacheDeviceIndex.setStatus('current')
coCdpCacheLocalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheLocalInterface.setStatus('current')
coCdpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheAddress.setStatus('current')
coCdpCacheDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheDeviceId.setStatus('current')
coCdpCacheTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheTimeToLive.setStatus('current')
coCdpCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheCapabilities.setStatus('current')
coCdpCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheVersion.setStatus('current')
coCdpCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCachePlatform.setStatus('current')
coCdpCachePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCachePortId.setStatus('current')
coCdpGlobalMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdpGlobalMessageInterval.setStatus('current')
coCdpGlobalHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdpGlobalHoldTime.setStatus('current')
colubrisCdpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2))
colubrisCdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 1))
colubrisCdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 2))
colubrisCdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 1, 1)).setObjects(("COLUBRIS-CDP-MIB", "colubrisCdpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisCdpMIBCompliance = colubrisCdpMIBCompliance.setStatus('current')
colubrisCdpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 2, 1)).setObjects(("COLUBRIS-CDP-MIB", "coCdpCacheLocalInterface"), ("COLUBRIS-CDP-MIB", "coCdpCacheAddress"), ("COLUBRIS-CDP-MIB", "coCdpCacheDeviceId"), ("COLUBRIS-CDP-MIB", "coCdpCacheTimeToLive"), ("COLUBRIS-CDP-MIB", "coCdpCacheCapabilities"), ("COLUBRIS-CDP-MIB", "coCdpCacheVersion"), ("COLUBRIS-CDP-MIB", "coCdpCachePlatform"), ("COLUBRIS-CDP-MIB", "coCdpCachePortId"), ("COLUBRIS-CDP-MIB", "coCdpGlobalMessageInterval"), ("COLUBRIS-CDP-MIB", "coCdpGlobalHoldTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisCdpMIBGroup = colubrisCdpMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-CDP-MIB", colubrisCdpMIBGroup=colubrisCdpMIBGroup, colubrisCdpMIBObjects=colubrisCdpMIBObjects, coCdpCache=coCdpCache, coCdpCacheAddress=coCdpCacheAddress, coCdpGlobalMessageInterval=coCdpGlobalMessageInterval, colubrisCdpMIBConformance=colubrisCdpMIBConformance, colubrisCdpMIBCompliance=colubrisCdpMIBCompliance, coCdpCacheTimeToLive=coCdpCacheTimeToLive, coCdpCacheEntry=coCdpCacheEntry, coCdpGlobal=coCdpGlobal, coCdpCachePortId=coCdpCachePortId, coCdpCachePlatform=coCdpCachePlatform, coCdpCacheDeviceIndex=coCdpCacheDeviceIndex, coCdpCacheTable=coCdpCacheTable, coCdpCacheDeviceId=coCdpCacheDeviceId, colubrisCdpMIBGroups=colubrisCdpMIBGroups, coCdpCacheCapabilities=coCdpCacheCapabilities, coCdpGlobalHoldTime=coCdpGlobalHoldTime, colubrisCdpMIBCompliances=colubrisCdpMIBCompliances, colubrisCdpMIB=colubrisCdpMIB, PYSNMP_MODULE_ID=colubrisCdpMIB, coCdpCacheVersion=coCdpCacheVersion, coCdpCacheLocalInterface=coCdpCacheLocalInterface)
