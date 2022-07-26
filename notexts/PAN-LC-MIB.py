#
# PySNMP MIB module PAN-LC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-LC-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:42 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
panModules, panProductsMibs = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules", "panProductsMibs")
panM_100, = mibBuilder.importSymbols("PAN-PRODUCTS-MIB", "panM-100")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, TimeTicks, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Bits, ModuleIdentity, Counter32, Gauge32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "TimeTicks", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Bits", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("PAN-LC-MIB", panLcLogDurationTraffic=panLcLogDurationTraffic, panLcLogDurationAppstat=panLcLogDurationAppstat, panLcLogDuration=panLcLogDuration, PYSNMP_MODULE_ID=panLogCollectorMibsModule, panLcIsRedundancyMember=panLcIsRedundancyMember, panLcLogDurationThsum=panLcLogDurationThsum, panLcLogDurationSystem=panLcLogDurationSystem, panLcLogRate=panLcLogRate, panLcDiskUsageLd1=panLcDiskUsageLd1, panLcLogDurationConfig=panLcLogDurationConfig, panLcLogDurationHipmatch=panLcLogDurationHipmatch, panLcLogDurationUserid=panLcLogDurationUserid, panLcLogDurationThreat=panLcLogDurationThreat, panLcLogDurationAlarm=panLcLogDurationAlarm, panLcStat=panLcStat, panLcDiskUsageLd2=panLcDiskUsageLd2, panLcDiskUsageLd3=panLcDiskUsageLd3, panLcDiskUsageLd4=panLcDiskUsageLd4, panLcLogDurationEvent=panLcLogDurationEvent, panLcDiskUsage=panLcDiskUsage, panLcLogDurationTrsum=panLcLogDurationTrsum, panLogCollectorMibsModule=panLogCollectorMibsModule)
