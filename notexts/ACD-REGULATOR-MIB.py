#
# PySNMP MIB module ACD-REGULATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-REGULATOR-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:40 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, IpAddress, Gauge32, Bits, Counter32, Integer32, NotificationType, MibIdentifier, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "IpAddress", "Gauge32", "Bits", "Counter32", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "Unsigned32", "iso")
TextualConvention, DateAndTime, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "RowStatus", "TruthValue", "DisplayString")
acdRegulator = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 6))
acdRegulator.setRevisions(('2011-10-10 01:00', '2010-11-10 01:00', '2008-05-01 01:00', '2008-02-06 01:00', '2007-03-28 01:00',))
if mibBuilder.loadTexts: acdRegulator.setLastUpdated('201110100100Z')
if mibBuilder.loadTexts: acdRegulator.setOrganization('Accedian Networks, Inc.')
acdRegulatorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 4))
acdRegulatorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 5))
acdRegulatorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6))
acdRegulatorTableTid = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1))
acdRegulatorTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1), )
if mibBuilder.loadTexts: acdRegulatorTable.setStatus('current')
acdRegulatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1), ).setIndexNames((0, "ACD-REGULATOR-MIB", "acdRegulatorID"))
if mibBuilder.loadTexts: acdRegulatorEntry.setStatus('current')
acdRegulatorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorID.setStatus('current')
acdRegulatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorName.setStatus('current')
acdRegulatorCir = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 3), Unsigned32().clone(20000)).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorCir.setStatus('current')
acdRegulatorCbs = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 4), Unsigned32().clone(8)).setUnits('Kbytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorCbs.setStatus('current')
acdRegulatorEir = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 5), Unsigned32().clone(1000)).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorEir.setStatus('current')
acdRegulatorEbs = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 6), Unsigned32().clone(8)).setUnits('Kbytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorEbs.setStatus('current')
acdRegulatorIsBlind = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorIsBlind.setStatus('current')
acdRegulatorIsCouple = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorIsCouple.setStatus('current')
acdRegulatorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorRowStatus.setStatus('current')
acdRegulatorStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2), )
if mibBuilder.loadTexts: acdRegulatorStatsTable.setStatus('current')
acdRegulatorStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1), ).setIndexNames((0, "ACD-REGULATOR-MIB", "acdRegulatorStatsID"))
if mibBuilder.loadTexts: acdRegulatorStatsEntry.setStatus('current')
acdRegulatorStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorStatsID.setStatus('current')
acdRegulatorStatsAcceptOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 2), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOctets.setStatus('current')
acdRegulatorStatsAcceptOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 3), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOverflowOctets.setStatus('current')
acdRegulatorStatsAcceptHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 4), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptHCOctets.setStatus('current')
acdRegulatorStatsAcceptPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 5), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptPkts.setStatus('current')
acdRegulatorStatsAcceptOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 6), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOverflowPkts.setStatus('current')
acdRegulatorStatsAcceptHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 7), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptHCPkts.setStatus('current')
acdRegulatorStatsAcceptRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 8), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptRate.setStatus('current')
acdRegulatorStatsDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 9), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropOctets.setStatus('current')
acdRegulatorStatsDropOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 10), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropOverflowOctets.setStatus('current')
acdRegulatorStatsDropHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 11), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropHCOctets.setStatus('current')
acdRegulatorStatsDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 12), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropPkts.setStatus('current')
acdRegulatorStatsDropOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 13), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropOverflowPkts.setStatus('current')
acdRegulatorStatsDropHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 14), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropHCPkts.setStatus('current')
acdRegulatorStatsDropRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 15), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropRate.setStatus('current')
acdRegulatorHistStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3), )
if mibBuilder.loadTexts: acdRegulatorHistStatsTable.setStatus('current')
acdRegulatorHistStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1), ).setIndexNames((0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsID"), (0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsSampleIndex"))
if mibBuilder.loadTexts: acdRegulatorHistStatsEntry.setStatus('current')
acdRegulatorHistStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorHistStatsID.setStatus('current')
acdRegulatorHistStatsSampleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorHistStatsSampleIndex.setStatus('current')
acdRegulatorHistStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsStatus.setStatus('current')
acdRegulatorHistStatsDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDuration.setStatus('current')
acdRegulatorHistStatsIntervalEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsIntervalEnd.setStatus('current')
acdRegulatorHistStatsAcceptOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 6), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOctets.setStatus('current')
acdRegulatorHistStatsAcceptOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 7), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOverflowOctets.setStatus('current')
acdRegulatorHistStatsAcceptHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 8), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptHCOctets.setStatus('current')
acdRegulatorHistStatsAcceptPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 9), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptPkts.setStatus('current')
acdRegulatorHistStatsAcceptOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 10), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOverflowPkts.setStatus('current')
acdRegulatorHistStatsAcceptHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 11), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptHCPkts.setStatus('current')
acdRegulatorHistStatsAcceptAvgRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 12), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptAvgRate.setStatus('current')
acdRegulatorHistStatsAcceptMinRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 13), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptMinRate.setStatus('current')
acdRegulatorHistStatsAcceptMaxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 14), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptMaxRate.setStatus('current')
acdRegulatorHistStatsDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 15), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOctets.setStatus('current')
acdRegulatorHistStatsDropOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 16), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOverflowOctets.setStatus('current')
acdRegulatorHistStatsDropHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 17), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropHCOctets.setStatus('current')
acdRegulatorHistStatsDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 18), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropPkts.setStatus('current')
acdRegulatorHistStatsDropOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 19), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOverflowPkts.setStatus('current')
acdRegulatorHistStatsDropHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 20), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropHCPkts.setStatus('current')
acdRegulatorHistStatsDropAvgRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 21), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropAvgRate.setStatus('current')
acdRegulatorHistStatsDropMinRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 22), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropMinRate.setStatus('current')
acdRegulatorHistStatsDropMaxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 23), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropMaxRate.setStatus('current')
acdRegulatorTableLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorTableLastChangeTid.setStatus('current')
acdRegulatorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1))
acdRegulatorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2))
acdRegulatorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 1)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorName"), ("ACD-REGULATOR-MIB", "acdRegulatorCir"), ("ACD-REGULATOR-MIB", "acdRegulatorCbs"), ("ACD-REGULATOR-MIB", "acdRegulatorEir"), ("ACD-REGULATOR-MIB", "acdRegulatorEbs"), ("ACD-REGULATOR-MIB", "acdRegulatorIsBlind"), ("ACD-REGULATOR-MIB", "acdRegulatorIsCouple"), ("ACD-REGULATOR-MIB", "acdRegulatorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorGroup = acdRegulatorGroup.setStatus('current')
acdRegulatorStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 2)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptRate"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorStatsGroup = acdRegulatorStatsGroup.setStatus('current')
acdRegulatorHistStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 3)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorHistStatsStatus"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDuration"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsIntervalEnd"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptAvgRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMinRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMaxRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropAvgRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMinRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMaxRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorHistStatsGroup = acdRegulatorHistStatsGroup.setStatus('current')
acdRegulatorTidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 4)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorTableLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorTidGroup = acdRegulatorTidGroup.setStatus('current')
acdPaaCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1, 1)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorGroup"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsGroup"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGroup"), ("ACD-REGULATOR-MIB", "acdRegulatorTidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdPaaCompliance = acdPaaCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-REGULATOR-MIB", acdRegulatorHistStatsAcceptMaxRate=acdRegulatorHistStatsAcceptMaxRate, acdRegulatorHistStatsAcceptPkts=acdRegulatorHistStatsAcceptPkts, acdRegulatorHistStatsAcceptHCOctets=acdRegulatorHistStatsAcceptHCOctets, acdRegulatorHistStatsEntry=acdRegulatorHistStatsEntry, acdRegulatorHistStatsAcceptAvgRate=acdRegulatorHistStatsAcceptAvgRate, acdRegulatorGroups=acdRegulatorGroups, acdRegulatorEbs=acdRegulatorEbs, acdRegulatorHistStatsDropMaxRate=acdRegulatorHistStatsDropMaxRate, acdRegulatorHistStatsTable=acdRegulatorHistStatsTable, acdRegulatorHistStatsDuration=acdRegulatorHistStatsDuration, acdPaaCompliance=acdPaaCompliance, acdRegulatorStatsDropHCPkts=acdRegulatorStatsDropHCPkts, acdRegulatorHistStatsAcceptOctets=acdRegulatorHistStatsAcceptOctets, acdRegulatorStatsAcceptPkts=acdRegulatorStatsAcceptPkts, PYSNMP_MODULE_ID=acdRegulator, acdRegulatorStatsAcceptOverflowOctets=acdRegulatorStatsAcceptOverflowOctets, acdRegulatorHistStatsDropHCPkts=acdRegulatorHistStatsDropHCPkts, acdRegulatorHistStatsAcceptMinRate=acdRegulatorHistStatsAcceptMinRate, acdRegulatorHistStatsGroup=acdRegulatorHistStatsGroup, acdRegulatorHistStatsDropOverflowOctets=acdRegulatorHistStatsDropOverflowOctets, acdRegulatorID=acdRegulatorID, acdRegulatorStatsID=acdRegulatorStatsID, acdRegulatorTableTid=acdRegulatorTableTid, acdRegulatorStatsAcceptHCPkts=acdRegulatorStatsAcceptHCPkts, acdRegulatorHistStatsSampleIndex=acdRegulatorHistStatsSampleIndex, acdRegulatorHistStatsAcceptHCPkts=acdRegulatorHistStatsAcceptHCPkts, acdRegulatorHistStatsDropAvgRate=acdRegulatorHistStatsDropAvgRate, acdRegulatorStatsDropOverflowPkts=acdRegulatorStatsDropOverflowPkts, acdRegulatorCbs=acdRegulatorCbs, acdRegulatorIsCouple=acdRegulatorIsCouple, acdRegulatorCir=acdRegulatorCir, acdRegulatorStatsAcceptOctets=acdRegulatorStatsAcceptOctets, acdRegulatorStatsTable=acdRegulatorStatsTable, acdRegulatorStatsAcceptHCOctets=acdRegulatorStatsAcceptHCOctets, acdRegulatorHistStatsStatus=acdRegulatorHistStatsStatus, acdRegulatorIsBlind=acdRegulatorIsBlind, acdRegulatorHistStatsIntervalEnd=acdRegulatorHistStatsIntervalEnd, acdRegulatorHistStatsDropHCOctets=acdRegulatorHistStatsDropHCOctets, acdRegulatorHistStatsDropPkts=acdRegulatorHistStatsDropPkts, acdRegulatorCompliances=acdRegulatorCompliances, acdRegulatorEntry=acdRegulatorEntry, acdRegulatorStatsDropRate=acdRegulatorStatsDropRate, acdRegulatorGroup=acdRegulatorGroup, acdRegulatorStatsAcceptOverflowPkts=acdRegulatorStatsAcceptOverflowPkts, acdRegulatorStatsEntry=acdRegulatorStatsEntry, acdRegulator=acdRegulator, acdRegulatorNotifications=acdRegulatorNotifications, acdRegulatorStatsDropHCOctets=acdRegulatorStatsDropHCOctets, acdRegulatorHistStatsDropMinRate=acdRegulatorHistStatsDropMinRate, acdRegulatorStatsDropPkts=acdRegulatorStatsDropPkts, acdRegulatorConformance=acdRegulatorConformance, acdRegulatorHistStatsID=acdRegulatorHistStatsID, acdRegulatorMIBObjects=acdRegulatorMIBObjects, acdRegulatorHistStatsDropOverflowPkts=acdRegulatorHistStatsDropOverflowPkts, acdRegulatorTableLastChangeTid=acdRegulatorTableLastChangeTid, acdRegulatorStatsGroup=acdRegulatorStatsGroup, acdRegulatorTable=acdRegulatorTable, acdRegulatorTidGroup=acdRegulatorTidGroup, acdRegulatorName=acdRegulatorName, acdRegulatorHistStatsAcceptOverflowOctets=acdRegulatorHistStatsAcceptOverflowOctets, acdRegulatorStatsDropOverflowOctets=acdRegulatorStatsDropOverflowOctets, acdRegulatorHistStatsAcceptOverflowPkts=acdRegulatorHistStatsAcceptOverflowPkts, acdRegulatorHistStatsDropOctets=acdRegulatorHistStatsDropOctets, acdRegulatorStatsAcceptRate=acdRegulatorStatsAcceptRate, acdRegulatorStatsDropOctets=acdRegulatorStatsDropOctets, acdRegulatorRowStatus=acdRegulatorRowStatus, acdRegulatorEir=acdRegulatorEir)
