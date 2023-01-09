#
# PySNMP MIB module ACD-REGULATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-REGULATOR-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:20 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Counter64, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Bits, Integer32, ObjectIdentity, Counter32, TimeTicks, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Bits", "Integer32", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "iso")
TextualConvention, TruthValue, RowStatus, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString", "DateAndTime")
acdRegulator = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 6))
acdRegulator.setRevisions(('2011-10-10 01:00', '2010-11-10 01:00', '2008-05-01 01:00', '2008-02-06 01:00', '2007-03-28 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acdRegulator.setRevisionsDescriptions(('Add acdRegulatorTableLastChangeTid.', 'Add compliance section.', 'Add RowStatus in acdRegulatorTable table.', 'Add support for history table.', 'Initial version of MIB module ACD-REGULATOR-MIB.',))
if mibBuilder.loadTexts: acdRegulator.setLastUpdated('201110100100Z')
if mibBuilder.loadTexts: acdRegulator.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: acdRegulator.setContactInfo('Accedian Technical Assistance Center\n             Accedian Networks, Inc.\n             4878 Levy, suite 202\n             Saint-Laurent, Quebec Canada H4R 2P1\n             E-mail: support@accedian.com')
if mibBuilder.loadTexts: acdRegulator.setDescription('The Regulators database for this Accedian Networks device.')
acdRegulatorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 4))
acdRegulatorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 5))
acdRegulatorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6))
acdRegulatorTableTid = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1))
acdRegulatorTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1), )
if mibBuilder.loadTexts: acdRegulatorTable.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorTable.setDescription('Table of all Regulators')
acdRegulatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1), ).setIndexNames((0, "ACD-REGULATOR-MIB", "acdRegulatorID"))
if mibBuilder.loadTexts: acdRegulatorEntry.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorEntry.setDescription('A Regulator is a two rates three colors engine to regulate a\n             given traffic.')
acdRegulatorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorID.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorID.setDescription('Unique value for each regulator entry. Its value ranges from 1 to\n        MAXINT (4 bytes). ')
acdRegulatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorName.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorName.setDescription('This is a string to identify the regulator.')
acdRegulatorCir = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 3), Unsigned32().clone(20000)).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorCir.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorCir.setDescription('The committed information rate.')
acdRegulatorCbs = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 4), Unsigned32().clone(8)).setUnits('Kbytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorCbs.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorCbs.setDescription('The committed burst size.')
acdRegulatorEir = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 5), Unsigned32().clone(1000)).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorEir.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorEir.setDescription('The excess information rate.')
acdRegulatorEbs = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 6), Unsigned32().clone(8)).setUnits('Kbytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorEbs.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorEbs.setDescription('The excess burst size.')
acdRegulatorIsBlind = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorIsBlind.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorIsBlind.setDescription('Enable or disable the pre-marking color processing.')
acdRegulatorIsCouple = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorIsCouple.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorIsCouple.setDescription('Enable or disable the coupling flag in this regulator.')
acdRegulatorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdRegulatorRowStatus.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorRowStatus.setDescription('All columns must have a valid value before a row can be activated. To\n        create a new regulator you shall provide the a unique name for\n        an empty row with the RowStatus set to Create and Go. To delete the\n        row you need to set the RowStatus to destroy.')
acdRegulatorStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2), )
if mibBuilder.loadTexts: acdRegulatorStatsTable.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsTable.setDescription('Table of all counters associated with each regulator.')
acdRegulatorStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1), ).setIndexNames((0, "ACD-REGULATOR-MIB", "acdRegulatorStatsID"))
if mibBuilder.loadTexts: acdRegulatorStatsEntry.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsEntry.setDescription('An Entry consists of statitics related to a regulator entry.')
acdRegulatorStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorStatsID.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsID.setDescription('Unique value for each regulator entry. Its value ranges from 1 to\n        MAXINT (4 bytes).')
acdRegulatorStatsAcceptOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 2), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOctets.setDescription('The total number of octets received by this regulator. This is a\n         32 bits counter. Combined with acdRegulatorStatsAcceptOverflowOctets,\n         it provides the equivalent of the 64 bits counter\n         acdRegulatorStatsAcceptHCOctets.')
acdRegulatorStatsAcceptOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 3), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOverflowOctets.setDescription('The number of times the associated acdRegulatorStatsAcceptOctets\n         counter has overflowed. This is a 32 bits counter. Combined with \n         acdRegulatorStatsAcceptOctets, it provides the equivalent of the\n         64 bits counter acdRegulatorStatsAccpetHCOctets.')
acdRegulatorStatsAcceptHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 4), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptHCOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsAcceptHCOctets.setDescription('The total number of octets received by this regulator.')
acdRegulatorStatsAcceptPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 5), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsAcceptPkts.setDescription('The total number of packets received by this regulator. This is a\n         32 bits counter. Combined with acdRegulatorStatsAcceptOverflowPkts,\n         it provides the equivalent of the 64 bits counter\n         acdRegulatorStatsAcceptHCPkts.')
acdRegulatorStatsAcceptOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 6), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOverflowPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsAcceptOverflowPkts.setDescription('The number of times the associated acdRegulatorStatsAcceptPkts\n         counter has overflowed. This is a 32 bits counter. Combined with \n         acdRegulatorStatsAcceptPkts, it provides the equivalent of the\n         64 bits counter acdRegulatorStatsAcceptHCPkts.')
acdRegulatorStatsAcceptHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 7), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptHCPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsAcceptHCPkts.setDescription('The total number of packets received by this regulator.')
acdRegulatorStatsAcceptRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 8), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsAcceptRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsAcceptRate.setDescription('The accept rate.')
acdRegulatorStatsDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 9), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsDropOctets.setDescription('The total number of octets received by this regulator. This is a\n         32 bits counter. Combined with acdRegulatorStatsDropOverflowOctets,\n         it provides the equivalent of the 64 bits counter\n         acdRegulatorStatsDropHCOctets.')
acdRegulatorStatsDropOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 10), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsDropOverflowOctets.setDescription('The number of times the associated acdRegulatorStatsDropOctets\n         counter has overflowed. This is a 32 bits counter. Combined with \n         acdRegulatorStatsDropOctets, it provides the equivalent of the\n         64 bits counter acdRegulatorStatsDropHCOctets.')
acdRegulatorStatsDropHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 11), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropHCOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsDropHCOctets.setDescription('The total number of octets received by this regulator.')
acdRegulatorStatsDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 12), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsDropPkts.setDescription('The total number of packets received by this regulator. This is a\n         32 bits counter. Combined with acdRegulatorStatsDropOverflowPkts,\n         it provides the equivalent of the 64 bits counter\n         acdRegulatorStatsDropHCPkts.')
acdRegulatorStatsDropOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 13), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropOverflowPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsDropOverflowPkts.setDescription('The number of times the associated acdRegulatorStatsDropPkts\n         counter has overflowed. This is a 32 bits counter. Combined with \n         acdRegulatorStatsDropPkts, it provides the equivalent of the\n         64 bits counter acdRegulatorStatsDropHCPkts.')
acdRegulatorStatsDropHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 14), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropHCPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsDropHCPkts.setDescription('The total number of packets received by this regulator.')
acdRegulatorStatsDropRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 15), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorStatsDropRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsDropRate.setDescription('The drop rate.')
acdRegulatorHistStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3), )
if mibBuilder.loadTexts: acdRegulatorHistStatsTable.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsTable.setDescription('Table of all counters associated with each regulator.')
acdRegulatorHistStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1), ).setIndexNames((0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsID"), (0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsSampleIndex"))
if mibBuilder.loadTexts: acdRegulatorHistStatsEntry.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsEntry.setDescription('An Entry consists of statitics related to a regulator entry.')
acdRegulatorHistStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorHistStatsID.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsID.setDescription('Unique value for each regulator entry. Its value ranges from 1 to\n        MAXINT (4 bytes).')
acdRegulatorHistStatsSampleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: acdRegulatorHistStatsSampleIndex.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsSampleIndex.setDescription('An index that uniquely identifies the particular sample this entry\n         represents among all samples associated with the same regulator\n         instance. This index starts at 1 and increases by one as each new\n         sample.')
acdRegulatorHistStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsStatus.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsStatus.setDescription('The status of this acdRegulatorHistStats entry.')
acdRegulatorHistStatsDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDuration.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDuration.setDescription('The interval in seconds over which the data is sampled for this entry.')
acdRegulatorHistStatsIntervalEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsIntervalEnd.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsIntervalEnd.setDescription('This is the time of the end of this entry.')
acdRegulatorHistStatsAcceptOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 6), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOctets.setDescription('The total number of octets received by this regulator during this\n         sampling interval. This is a 32 bits counter. Combined with\n         acdRegulatorHistStatsAcceptOverflowOctets, it provides the equivalent\n         of the 64 bits counter acdRegulatorHistStatsAcceptHCOctets.')
acdRegulatorHistStatsAcceptOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 7), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOverflowOctets.setDescription('The number of times the associated acdRegulatorHistStatsAcceptOctets\n         counter has overflowed during this sampling interval. This is a\n         32 bits counter. Combined with acdRegulatorHistStatsAcceptOctets,\n         it provides the equivalent of the 64 bits counter\n         acdRegulatorHistStatsAcceptHCOctets.')
acdRegulatorHistStatsAcceptHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 8), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptHCOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptHCOctets.setDescription('The total number of octets received by this regulator during this\n         sampling interval.')
acdRegulatorHistStatsAcceptPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 9), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptPkts.setDescription('The total number of packets received by this regulator during this\n         sampling interval. This is a 32 bits counter. Combined with\n         acdRegulatorHistStatsAcceptOverflowPkts, it provides the equivalent\n         of the 64 bits counter acdRegulatorHistStatsAcceptHCPkts.')
acdRegulatorHistStatsAcceptOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 10), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOverflowPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptOverflowPkts.setDescription('The number of times the associated acdRegulatorHistStatsAcceptPkts\n         counter has overflowed during this sampling interval. This is a\n         32 bits counter. Combined with acdRegulatorHistStatsAcceptPkts, it\n         provides the equivalent of the 64 bits counter\n         acdRegulatorHistStatsAcceptHCPkts.')
acdRegulatorHistStatsAcceptHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 11), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptHCPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptHCPkts.setDescription('The total number of packets received by this regulator during this\n         sampling interval.')
acdRegulatorHistStatsAcceptAvgRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 12), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptAvgRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptAvgRate.setDescription('The average accept rate during this sampling interval.')
acdRegulatorHistStatsAcceptMinRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 13), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptMinRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptMinRate.setDescription('The minimum accept rate during this sampling interval.')
acdRegulatorHistStatsAcceptMaxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 14), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptMaxRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsAcceptMaxRate.setDescription('The maximum accept rate during this sampling interval.')
acdRegulatorHistStatsDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 15), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOctets.setDescription('The total number of octets received by this regulator during this\n         sampling interval. This is a 32 bits counter. Combined the overflow,\n         counter it provides the equivalent of the 64 bits counter\n         acdRegulatorHistStatsDropHCOctets.')
acdRegulatorHistStatsDropOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 16), Counter32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOverflowOctets.setDescription('The number of times the associated acdRegulatorHistStatsDropOctets\n         counter has overflowed during this sampling interval. This is a\n         32 bits counter. Combined with acdRegulatorHistStatsDropOctets, it\n         provides the equivalent of the 64 bits counter\n         acdRegulatorHistStatsDropHCOctets.')
acdRegulatorHistStatsDropHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 17), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropHCOctets.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropHCOctets.setDescription('The total number of octets received by this regulator during this\n         sampling interval.')
acdRegulatorHistStatsDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 18), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropPkts.setDescription('The total number of packets received by this regulator during this\n         sampling interval. This is a 32 bits counter. Combined with\n         acdRegulatorHistStatsDropOverflowPkts, it provides the equivalent of\n         the 64 bits counter acdRegulatorHistStatsDropHCPkts.')
acdRegulatorHistStatsDropOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 19), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOverflowPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropOverflowPkts.setDescription('The number of times the associated acdRegulatorHistStatsDropPkts\n         counter has overflowed during this sampling interval. This is a\n         32 bits counter. Combined with acdRegulatorHistStatsDropPkts, it\n         provides the equivalent of the 64 bits counter\n         acdRegulatorHistStatsDropHCPkts.')
acdRegulatorHistStatsDropHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 20), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropHCPkts.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropHCPkts.setDescription('The total number of packets received by this regulator during this\n         sampling interval.')
acdRegulatorHistStatsDropAvgRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 21), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropAvgRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropAvgRate.setDescription('The average drop rate during this sampling interval.')
acdRegulatorHistStatsDropMinRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 22), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropMinRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropMinRate.setDescription('The minimum drop rate during this sampling interval.')
acdRegulatorHistStatsDropMaxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 23), Gauge32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorHistStatsDropMaxRate.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsDropMaxRate.setDescription('The maximum drop rate during this sampling interval.')
acdRegulatorTableLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdRegulatorTableLastChangeTid.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorTableLastChangeTid.setDescription('This is the transaction ID of the last change of the acdRegulatorTable\n        table.  If this value is different since the last read this is indicate \n        a table change.')
acdRegulatorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1))
acdRegulatorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2))
acdRegulatorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 1)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorName"), ("ACD-REGULATOR-MIB", "acdRegulatorCir"), ("ACD-REGULATOR-MIB", "acdRegulatorCbs"), ("ACD-REGULATOR-MIB", "acdRegulatorEir"), ("ACD-REGULATOR-MIB", "acdRegulatorEbs"), ("ACD-REGULATOR-MIB", "acdRegulatorIsBlind"), ("ACD-REGULATOR-MIB", "acdRegulatorIsCouple"), ("ACD-REGULATOR-MIB", "acdRegulatorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorGroup = acdRegulatorGroup.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorGroup.setDescription('Objects for the Regulator configurtion Group.')
acdRegulatorStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 2)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptRate"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorStatsGroup = acdRegulatorStatsGroup.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorStatsGroup.setDescription('Objects for the Regulator statistics Group.')
acdRegulatorHistStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 3)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorHistStatsStatus"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDuration"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsIntervalEnd"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptAvgRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMinRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMaxRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCOctets"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCPkts"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropAvgRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMinRate"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMaxRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorHistStatsGroup = acdRegulatorHistStatsGroup.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorHistStatsGroup.setDescription('Objects for the Regulator history statistics Group.')
acdRegulatorTidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 4)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorTableLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdRegulatorTidGroup = acdRegulatorTidGroup.setStatus('current')
if mibBuilder.loadTexts: acdRegulatorTidGroup.setDescription('List of scalars to monitior changes in tables.')
acdPaaCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1, 1)).setObjects(("ACD-REGULATOR-MIB", "acdRegulatorGroup"), ("ACD-REGULATOR-MIB", "acdRegulatorStatsGroup"), ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGroup"), ("ACD-REGULATOR-MIB", "acdRegulatorTidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdPaaCompliance = acdPaaCompliance.setStatus('current')
if mibBuilder.loadTexts: acdPaaCompliance.setDescription('The compliance statement for support of the ACD-REGULATOR-MIB module.')
mibBuilder.exportSymbols("ACD-REGULATOR-MIB", acdRegulatorRowStatus=acdRegulatorRowStatus, acdRegulatorStatsAcceptPkts=acdRegulatorStatsAcceptPkts, acdRegulatorHistStatsDropPkts=acdRegulatorHistStatsDropPkts, acdRegulatorTableTid=acdRegulatorTableTid, acdRegulatorHistStatsAcceptHCOctets=acdRegulatorHistStatsAcceptHCOctets, acdRegulatorHistStatsAcceptMinRate=acdRegulatorHistStatsAcceptMinRate, acdRegulatorStatsDropOverflowOctets=acdRegulatorStatsDropOverflowOctets, acdRegulatorHistStatsDropAvgRate=acdRegulatorHistStatsDropAvgRate, acdRegulatorStatsTable=acdRegulatorStatsTable, acdRegulatorCompliances=acdRegulatorCompliances, acdRegulatorIsCouple=acdRegulatorIsCouple, acdRegulatorName=acdRegulatorName, acdRegulatorHistStatsDropMaxRate=acdRegulatorHistStatsDropMaxRate, acdRegulatorTable=acdRegulatorTable, acdRegulatorCbs=acdRegulatorCbs, acdRegulatorStatsAcceptHCPkts=acdRegulatorStatsAcceptHCPkts, acdRegulatorEir=acdRegulatorEir, acdRegulatorTidGroup=acdRegulatorTidGroup, acdRegulatorHistStatsDropOctets=acdRegulatorHistStatsDropOctets, acdRegulatorEntry=acdRegulatorEntry, acdRegulatorHistStatsID=acdRegulatorHistStatsID, acdRegulatorHistStatsDropHCOctets=acdRegulatorHistStatsDropHCOctets, acdRegulatorTableLastChangeTid=acdRegulatorTableLastChangeTid, acdRegulatorHistStatsAcceptMaxRate=acdRegulatorHistStatsAcceptMaxRate, acdRegulatorMIBObjects=acdRegulatorMIBObjects, acdRegulatorStatsAcceptOctets=acdRegulatorStatsAcceptOctets, acdRegulatorGroup=acdRegulatorGroup, acdRegulatorStatsAcceptOverflowOctets=acdRegulatorStatsAcceptOverflowOctets, acdRegulator=acdRegulator, acdRegulatorGroups=acdRegulatorGroups, acdRegulatorHistStatsAcceptOctets=acdRegulatorHistStatsAcceptOctets, acdRegulatorStatsDropHCPkts=acdRegulatorStatsDropHCPkts, acdRegulatorHistStatsAcceptAvgRate=acdRegulatorHistStatsAcceptAvgRate, acdRegulatorHistStatsDropMinRate=acdRegulatorHistStatsDropMinRate, acdRegulatorHistStatsIntervalEnd=acdRegulatorHistStatsIntervalEnd, acdRegulatorStatsAcceptHCOctets=acdRegulatorStatsAcceptHCOctets, acdRegulatorHistStatsDuration=acdRegulatorHistStatsDuration, acdPaaCompliance=acdPaaCompliance, acdRegulatorHistStatsAcceptHCPkts=acdRegulatorHistStatsAcceptHCPkts, acdRegulatorStatsDropOctets=acdRegulatorStatsDropOctets, acdRegulatorStatsDropOverflowPkts=acdRegulatorStatsDropOverflowPkts, acdRegulatorHistStatsAcceptPkts=acdRegulatorHistStatsAcceptPkts, acdRegulatorHistStatsDropOverflowPkts=acdRegulatorHistStatsDropOverflowPkts, acdRegulatorHistStatsDropHCPkts=acdRegulatorHistStatsDropHCPkts, acdRegulatorHistStatsEntry=acdRegulatorHistStatsEntry, acdRegulatorStatsGroup=acdRegulatorStatsGroup, acdRegulatorEbs=acdRegulatorEbs, acdRegulatorHistStatsDropOverflowOctets=acdRegulatorHistStatsDropOverflowOctets, acdRegulatorNotifications=acdRegulatorNotifications, PYSNMP_MODULE_ID=acdRegulator, acdRegulatorHistStatsStatus=acdRegulatorHistStatsStatus, acdRegulatorHistStatsTable=acdRegulatorHistStatsTable, acdRegulatorStatsAcceptRate=acdRegulatorStatsAcceptRate, acdRegulatorIsBlind=acdRegulatorIsBlind, acdRegulatorStatsDropRate=acdRegulatorStatsDropRate, acdRegulatorHistStatsAcceptOverflowPkts=acdRegulatorHistStatsAcceptOverflowPkts, acdRegulatorStatsDropPkts=acdRegulatorStatsDropPkts, acdRegulatorConformance=acdRegulatorConformance, acdRegulatorStatsID=acdRegulatorStatsID, acdRegulatorCir=acdRegulatorCir, acdRegulatorHistStatsSampleIndex=acdRegulatorHistStatsSampleIndex, acdRegulatorStatsAcceptOverflowPkts=acdRegulatorStatsAcceptOverflowPkts, acdRegulatorStatsDropHCOctets=acdRegulatorStatsDropHCOctets, acdRegulatorHistStatsAcceptOverflowOctets=acdRegulatorHistStatsAcceptOverflowOctets, acdRegulatorHistStatsGroup=acdRegulatorHistStatsGroup, acdRegulatorStatsEntry=acdRegulatorStatsEntry, acdRegulatorID=acdRegulatorID)
