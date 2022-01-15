#
# PySNMP MIB module PAN-LC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-LC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:48 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
panModules, panProductsMibs = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules", "panProductsMibs")
panM_100, = mibBuilder.importSymbols("PAN-PRODUCTS-MIB", "panM-100")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Integer32, Counter64, Gauge32, iso, NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Counter64", "Gauge32", "iso", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
panLogCollectorMibsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 6))
panLogCollectorMibsModule.setRevisions(('2012-01-11 10:13',))
if mibBuilder.loadTexts: panLogCollectorMibsModule.setLastUpdated('201201111013Z')
if mibBuilder.loadTexts: panLogCollectorMibsModule.setOrganization('Palo Alto Networks')
panLcStat = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1))
if mibBuilder.loadTexts: panLcStat.setStatus('current')
panLcLogRate = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogRate.setStatus('current')
panLcLogDuration = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2))
if mibBuilder.loadTexts: panLcLogDuration.setStatus('current')
panLcDiskUsage = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3))
if mibBuilder.loadTexts: panLcDiskUsage.setStatus('current')
panLcDiskUsageLd1 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd1.setStatus('current')
panLcDiskUsageLd2 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd2.setStatus('current')
panLcDiskUsageLd3 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd3.setStatus('current')
panLcDiskUsageLd4 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd4.setStatus('current')
panLcLogDurationTraffic = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationTraffic.setStatus('current')
panLcLogDurationConfig = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationConfig.setStatus('current')
panLcLogDurationSystem = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationSystem.setStatus('current')
panLcLogDurationThreat = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationThreat.setStatus('current')
panLcLogDurationAppstat = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationAppstat.setStatus('current')
panLcLogDurationTrsum = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationTrsum.setStatus('current')
panLcLogDurationThsum = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationThsum.setStatus('current')
panLcLogDurationEvent = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationEvent.setStatus('current')
panLcLogDurationAlarm = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationAlarm.setStatus('current')
panLcLogDurationHipmatch = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationHipmatch.setStatus('current')
panLcLogDurationUserid = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationUserid.setStatus('current')
panLcIsRedundancyMember = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcIsRedundancyMember.setStatus('current')
mibBuilder.exportSymbols("PAN-LC-MIB", panLcLogDurationEvent=panLcLogDurationEvent, panLcLogDurationSystem=panLcLogDurationSystem, panLcDiskUsage=panLcDiskUsage, panLcLogDurationAppstat=panLcLogDurationAppstat, panLcLogDurationTrsum=panLcLogDurationTrsum, panLcLogDurationUserid=panLcLogDurationUserid, panLcIsRedundancyMember=panLcIsRedundancyMember, panLogCollectorMibsModule=panLogCollectorMibsModule, panLcDiskUsageLd1=panLcDiskUsageLd1, panLcLogDurationConfig=panLcLogDurationConfig, panLcLogDurationThreat=panLcLogDurationThreat, panLcLogDurationTraffic=panLcLogDurationTraffic, panLcLogDurationAlarm=panLcLogDurationAlarm, panLcLogDurationHipmatch=panLcLogDurationHipmatch, panLcDiskUsageLd2=panLcDiskUsageLd2, panLcStat=panLcStat, panLcDiskUsageLd3=panLcDiskUsageLd3, panLcLogRate=panLcLogRate, panLcLogDurationThsum=panLcLogDurationThsum, PYSNMP_MODULE_ID=panLogCollectorMibsModule, panLcDiskUsageLd4=panLcDiskUsageLd4, panLcLogDuration=panLcLogDuration)
