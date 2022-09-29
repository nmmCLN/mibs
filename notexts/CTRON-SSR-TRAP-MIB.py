#
# PySNMP MIB module CTRON-SSR-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-TRAP-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 08:48:44 2022
# On host fv-az460-75 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
capCPUCurrentUtilization, = mibBuilder.importSymbols("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization")
sysHwModuleSlotNumber, sysHwFan, sysHwPowerSupply, sysHwTemperature = mibBuilder.importSymbols("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber", "sysHwFan", "sysHwPowerSupply", "sysHwTemperature")
polAclName, polAclItem = mibBuilder.importSymbols("CTRON-SSR-POLICY-MIB", "polAclName", "polAclItem")
ssrTraps, ssrMibs = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrTraps", "ssrMibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Bits, iso, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, Counter32, TimeTicks, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Bits", "iso", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter32", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ssrTrapsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300))
ssrTrapsMIB.setRevisions(('2002-07-23 17:20', '2001-02-16 00:00',))
if mibBuilder.loadTexts: ssrTrapsMIB.setLastUpdated('200207231720Z')
if mibBuilder.loadTexts: ssrTrapsMIB.setOrganization('Enterasys Networks, Inc.')
trapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 1))
envTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2))
polTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3))
envPowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyFailed.setStatus('current')
envPowerSupplyRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyRecovered.setStatus('current')
envFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanFailed.setStatus('current')
envFanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanRecovered.setStatus('current')
envTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 5)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempExceeded.setStatus('current')
envTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 6)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempNormal.setStatus('current')
envHotSwapIn = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 7)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapIn.setStatus('current')
envHotSwapOut = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 8)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapOut.setStatus('current')
envBackupControlModuleOnline = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 9)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envBackupControlModuleOnline.setStatus('current')
envBackupControlModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 10)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envBackupControlModuleFailure.setStatus('current')
envLineModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 11)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envLineModuleFailure.setStatus('current')
envCPUThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 12)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"))
if mibBuilder.loadTexts: envCPUThresholdExceeded.setStatus('current')
polNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0))
polAclDenied = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0, 1)).setObjects(("CTRON-SSR-POLICY-MIB", "polAclName"), ("CTRON-SSR-POLICY-MIB", "polAclItem"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: polAclDenied.setStatus('current')
ssrTrapsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2))
ssrTrapsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 1))
ssrTrapsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2))
ssrTrapsComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV10 = ssrTrapsComplianceV10.setStatus('obsolete')
ssrTrapsComplianceV20 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV20"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV20 = ssrTrapsComplianceV20.setStatus('deprecated')
ssrTrapsComplianceV30 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV30"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV30 = ssrTrapsComplianceV30.setStatus('deprecated')
ssrTrapsComplianceV40 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV40"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV40 = ssrTrapsComplianceV40.setStatus('current')
ssrTrapsComplianceV50 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV50"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV50 = ssrTrapsComplianceV50.setStatus('current')
ssrTrapsConfGroupV10 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV10 = ssrTrapsConfGroupV10.setStatus('obsolete')
ssrTrapsConfGroupV20 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV20 = ssrTrapsConfGroupV20.setStatus('deprecated')
ssrTrapsConfGroupV30 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV30 = ssrTrapsConfGroupV30.setStatus('deprecated')
ssrTrapsConfGroupV40 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV40 = ssrTrapsConfGroupV40.setStatus('deprecated')
ssrTrapsConfGroupV50 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"), ("CTRON-SSR-TRAP-MIB", "polAclDenied"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV50 = ssrTrapsConfGroupV50.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-TRAP-MIB", envBackupControlModuleFailure=envBackupControlModuleFailure, envHotSwapOut=envHotSwapOut, ssrTrapsCompliances=ssrTrapsCompliances, envPowerSupplyRecovered=envPowerSupplyRecovered, ssrTrapsComplianceV50=ssrTrapsComplianceV50, PYSNMP_MODULE_ID=ssrTrapsMIB, ssrTrapsConfGroupV30=ssrTrapsConfGroupV30, ssrTrapsConformance=ssrTrapsConformance, ssrTrapsConfGroupV50=ssrTrapsConfGroupV50, ssrTrapsConfGroupV20=ssrTrapsConfGroupV20, envLineModuleFailure=envLineModuleFailure, ssrTrapsComplianceV20=ssrTrapsComplianceV20, envTempNormal=envTempNormal, trapControl=trapControl, envTempExceeded=envTempExceeded, envFanFailed=envFanFailed, polNotifications=polNotifications, ssrTrapsGroups=ssrTrapsGroups, ssrTrapsComplianceV30=ssrTrapsComplianceV30, envBackupControlModuleOnline=envBackupControlModuleOnline, envTrapGroup=envTrapGroup, envCPUThresholdExceeded=envCPUThresholdExceeded, ssrTrapsConfGroupV40=ssrTrapsConfGroupV40, polTrapGroup=polTrapGroup, polAclDenied=polAclDenied, ssrTrapsComplianceV40=ssrTrapsComplianceV40, ssrTrapsConfGroupV10=ssrTrapsConfGroupV10, envPowerSupplyFailed=envPowerSupplyFailed, ssrTrapsMIB=ssrTrapsMIB, envFanRecovered=envFanRecovered, envHotSwapIn=envHotSwapIn, ssrTrapsComplianceV10=ssrTrapsComplianceV10)
