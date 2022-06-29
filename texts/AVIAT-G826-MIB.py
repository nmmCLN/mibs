#
# PySNMP MIB module AVIAT-G826-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-G826-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:44 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, NotificationType, MibIdentifier, Integer32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter32, Unsigned32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "NotificationType", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter32", "Unsigned32", "Gauge32", "IpAddress")
TruthValue, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DateAndTime", "DisplayString")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatG826Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 14))
aviatG826Module.setRevisions(('2014-01-21 01:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aviatG826Module.setRevisionsDescriptions(('Initial Version.',))
if mibBuilder.loadTexts: aviatG826Module.setLastUpdated('201401210157Z')
if mibBuilder.loadTexts: aviatG826Module.setOrganization('Aviat Networks')
if mibBuilder.loadTexts: aviatG826Module.setContactInfo('Aviat Networks\n                         Customer Service\n\n                         Postal: 5200 Great America Parkway\n                                 Santa Clara\n                                 California 95054\n                                 United States of America\n\n                         Tel: 408 567 7000\n\n                         E-mail: mibsupport@aviatnet.com')
if mibBuilder.loadTexts: aviatG826Module.setDescription('This MIB module supports the ITU standard G.826 Error\n                 Performance Measure.')
class AviatPackedG826Data(TextualConvention, OctetString):
    description = 'This is the G826 data packed into a single object.\n                         Note that these are fixed size fields. The Date and\n                         Time bytes are padded with trailing zeros. Refer to\n                         the individual object definitions in\n                         aviatPerformanceTable for details on the syntax of\n                         each object.\n\n                             Bytes 1-4:     G826 Errored Blocks\n                             Bytes 5-8:     G826 Errored Seconds\n                             Bytes 9-12:    G826 Errored Seconds Ratio\n                             Bytes 13-16:   G826 Severely Errored Seconds\n                             Bytes 17-20:   G826 Severely Errored Seconds Ratio\n                             Bytes 21-24:   G826 Background Block Errors\n                             Bytes 25-28:   G826 Background Block Errors Ratio\n                             Bytes 29-32:   G826 Available Seconds\n                             Bytes 33-36:   G826 Unavailable Seconds\n                             Bytes 37-47:   Date And Time\n                             '
    status = 'current'
    displayHint = '55x'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(47, 47), )
aviatG826Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 14, 1))
aviatG826Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 1))
aviatG826Compliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 2))
aviatG826MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2))
aviatG826ControlTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1), )
if mibBuilder.loadTexts: aviatG826ControlTable.setStatus('current')
if mibBuilder.loadTexts: aviatG826ControlTable.setDescription('A table containing G.826 control objects for entities\n                         within the system.')
aviatG826ControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatG826ControlEntry.setStatus('current')
if mibBuilder.loadTexts: aviatG826ControlEntry.setDescription('A row in the aviatG826ControlTable.')
aviatG826LastQHourChangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826LastQHourChangeIndex.setStatus('current')
if mibBuilder.loadTexts: aviatG826LastQHourChangeIndex.setDescription('This is the index number of the last entry in\n                         aviatG826QHourTable that refers to the given entity.\n                         This index number refers to the aviatG826QHourPeriod\n                         index of the table.')
aviatG826LastDayChangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826LastDayChangeIndex.setStatus('current')
if mibBuilder.loadTexts: aviatG826LastDayChangeIndex.setDescription('This is the index number of the last entry in\n                         aviatG826DayTable that refers to the given entity.\n                         This index number refers to the aviatG826DayPeriod\n                         index of the table.')
aviatG826Reset = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("all", 2), ("realtime", 3), ("quarterhour", 4), ("daily", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatG826Reset.setStatus('current')
if mibBuilder.loadTexts: aviatG826Reset.setDescription('This object resets G826 statistics for an entity.\n                         Setting all(2) will reset realtime, quarter hourly and\n                         daily statistics. Setting realtime(3), quarterhour(4)\n                         or daily(5) will reset only the selected type of\n                         statistics. If quarter hour or daily statistics are\n                         reset, then all saved statistics data of that type\n                         will be deleted. Resetting also resets the current bin\n                         so statistic will begin on next boundary.\n\n                         Reading this object will return none(1).')
aviatG826PerformTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2), )
if mibBuilder.loadTexts: aviatG826PerformTable.setStatus('current')
if mibBuilder.loadTexts: aviatG826PerformTable.setDescription('This is the table containing information about the\n                         radio path G.826 performance of each terminal in the\n                         domain. This performance data is updated every 1\n                         second.')
aviatG826PerformEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatG826PerformEntry.setStatus('current')
if mibBuilder.loadTexts: aviatG826PerformEntry.setDescription('This is an entry in the table containing the receiver\n                         performance data of an entity in the system.')
aviatG826ErroredBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826ErroredBlocks.setStatus('current')
if mibBuilder.loadTexts: aviatG826ErroredBlocks.setDescription('This is the number of G.826 Errored Blocks since the\n                         start of monitoring. This parameter is updated every 1\n                         second.\n\n                         This parameter indicates the number of blocks in which\n                         one or more bits are in error.')
aviatG826ErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826ErroredSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826ErroredSeconds.setDescription('This is the number of G.826 Errored Seconds since the\n                         start of monitoring. This parameter is updated every 1\n                         second.\n\n                         This parameter indicates the number of one second\n                         periods with one or more errored blocks.')
aviatG826ErroredSecondsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826ErroredSecondsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826ErroredSecondsRatio.setDescription('This is the G.826 Errored Seconds Ratio since the\n                         start of monitoring. This parameter is updated every 1\n                         second.\n\n                         The ratio is calculated by dividing the number of\n                         errored seconds by the available time. The ratio is\n                         then multiplied by 1E+7 to preserve 7 decimal places\n                         of the ratio while it is represented as an integer. If\n                         the available time is 0, then this object will also be\n                         0.')
aviatG826SeverelyErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826SeverelyErroredSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826SeverelyErroredSeconds.setDescription('This is the number of G.826 Severely Errored Seconds\n                         since the start of monitoring. This parameter is\n                         updated every 1 second.\n\n                         This parameter indicates the number of one second\n                         periods that contain 30%, or more, errored blocks or\n                         at least one defect.')
aviatG826SeverelyErroredSecsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826SeverelyErroredSecsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826SeverelyErroredSecsRatio.setDescription('This is the G.826 Severely Errored Seconds Ratio since\n                         the start of monitoring. This parameter is updated\n                         every 1 second.\n\n                         The ratio is calculated by dividing the number of\n                         severely errored seconds by the available time. The\n                         ratio is then multiplied by 1E+7 to preserve 7 decimal\n                         places of the ratio while it is represented as an\n                         integer. If the available time is 0, then this object\n                         will also be 0.')
aviatG826BackgroundBlockErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826BackgroundBlockErrors.setStatus('current')
if mibBuilder.loadTexts: aviatG826BackgroundBlockErrors.setDescription('This is the number of G.826 Background Block Errors\n                         since the start of monitoring. This parameter is\n                         updated every 1 second.')
aviatG826BackgroundBlockErrorsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826BackgroundBlockErrorsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826BackgroundBlockErrorsRatio.setDescription('This is the Background Block Errors Ratio since the\n                         start of monitoring. This parameter is updated every 1\n                         second.\n\n                         The ratio is calculated by dividing the number of\n                         Background Block Errors by the total number of blocks\n                         (excluding blocks transmitted during severely errored\n                         seconds). The ratio is then multiplied by 1E+14 to\n                         preserve 14 decimal places of the ratio while it is\n                         represented as an integer. If the total number of\n                         blocks is 0, then this object will also be 0.')
aviatG826AvailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826AvailableSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826AvailableSeconds.setDescription('This is the number of Available Seconds since the\n                         start of monitoring. This parameter is updated every 1\n                         second.\n\n                         This parameter indicates the time in seconds that the\n                         link is available.\n\n                         Note that available time ends at the start of a block\n                         of ten consecutive Severely Errored Seconds and\n                         recommences at the start of a block of ten seconds\n                         each of which is not severely errored.')
aviatG826UnavailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826UnavailableSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826UnavailableSeconds.setDescription('This is the number of Unavailable Seconds since the\n                         start of monitoring. This parameter is updated every 1\n                         second.\n\n                         Note that unavailable time commences at the start of a\n                         block of ten consecutive Severely Errored Seconds and\n                         ends at the start of a block of ten seconds each of\n                         which is not severely errored.')
aviatG826PackedData = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 12), AviatPackedG826Data()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826PackedData.setStatus('current')
if mibBuilder.loadTexts: aviatG826PackedData.setDescription("This is all of the Performance data for this table,\n                         updated every 1 second, packed into a single object.\n\n                         This object is provided to guarantee a 'snapshot'\n                         collection of the performance measures in an entity.\n                         Slowly stepping through the aviatG826PerformTable may\n                         result in changing information being read.")
aviatG826QuarterHourTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3), )
if mibBuilder.loadTexts: aviatG826QuarterHourTable.setStatus('current')
if mibBuilder.loadTexts: aviatG826QuarterHourTable.setDescription('This is the table containing information about the\n                         radio path G.826 performance of each terminal in the\n                         domain. This performance data is recorded for 15\n                         minute periods.')
aviatG826QuarterHourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-G826-MIB", "aviatG826QHourIndex"), (0, "AVIAT-G826-MIB", "aviatG826QHourPeriod"))
if mibBuilder.loadTexts: aviatG826QuarterHourEntry.setStatus('current')
if mibBuilder.loadTexts: aviatG826QuarterHourEntry.setDescription('This is an entry in the table containing the G.826\n                         performance data of a particular entity within the\n                         agent during a 15 minute period. This is required to\n                         maintain a unique index even when the table wraps.')
aviatG826QHourIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 1), Gauge32())
if mibBuilder.loadTexts: aviatG826QHourIndex.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourIndex.setDescription('This is the row number referencing to the quarter\n                         hourly G.826 performance data of a particular entity\n                         in the system.')
aviatG826QHourPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 2), Gauge32())
if mibBuilder.loadTexts: aviatG826QHourPeriod.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourPeriod.setDescription('This is the unique row number for the 15 minute period\n                         during which this block of performance data was\n                         collected.')
aviatG826QHourDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourDateAndTime.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourDateAndTime.setDescription('This is the date and time at the start of the current\n                         15 minute period during which this block of\n                         performance data was collected.')
aviatG826QHourErroredBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourErroredBlocks.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourErroredBlocks.setDescription('This is the number of G.826 Errored Blocks for the\n                         current 15 minute period of monitoring.\n\n                         This parameter indicates the number of blocks in which\n                         one or more bits are in error.')
aviatG826QHourErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourErroredSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourErroredSeconds.setDescription('This is the number of G.826 Errored Seconds for the\n                         current 15 minute period of monitoring.\n\n                         This parameter indicates the number of one second\n                         periods with one or more errored blocks.')
aviatG826QHourErroredSecondsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourErroredSecondsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourErroredSecondsRatio.setDescription('This is the G.826 Errored Seconds Ratio for the\n                         current 15 minute period of monitoring.\n\n                         The ratio is calculated by dividing the number of\n                         errored seconds by the available time. The ratio is\n                         then multiplied by 1E+7 to preserve 7 decimal places\n                         of the ratio while it is represented as an integer. If\n                         the available time is 0, then this object will also be\n                         0.')
aviatG826QHourSeverelyErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourSeverelyErroredSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourSeverelyErroredSeconds.setDescription('This is the number of G.826 Severely Errored Seconds\n                         for the current 15 minute period of monitoring.\n\n                         This parameter indicates the number of one second\n                         periods that contain 30%, or more, errored blocks or\n                         at least one defect.')
aviatG826QHourSeverelyErroredSecsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourSeverelyErroredSecsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourSeverelyErroredSecsRatio.setDescription('This is the G.826 Severely Errored Seconds Ratio for\n                         the current 15 minute period of monitoring.\n\n                         The ratio is calculated by dividing the number of\n                         severely errored seconds by the available time. The\n                         ratio is then multiplied by 1E+7 to preserve 7 decimal\n                         places of the ratio while it represented as an\n                         integer. If the available time is 0, then this object\n                         will also be 0.')
aviatG826QHourBackgroundBlockErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourBackgroundBlockErrors.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourBackgroundBlockErrors.setDescription('This is the number of G.826 Background Block Errors\n                         for the current 15 minute period of monitoring.')
aviatG826QHourBackgroundBlockErrorsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourBackgroundBlockErrorsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourBackgroundBlockErrorsRatio.setDescription('This is the Background Block Errors Ratio for the\n                         current 15 minute period of monitoring.\n\n                         The ratio is calculated by dividing the number of\n                         Background Block Errors by the total number of blocks\n                         (excluding blocks transmitted during severely errored\n                         seconds). The ratio is then multiplied by 1E+7 to\n                         preserve 7 decimal places of the ratio while it is\n                         represented as an integer. If the total number of\n                         blocks is 0, then this object will also be 0.')
aviatG826QHourAvailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourAvailableSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourAvailableSeconds.setDescription('This is the number of Available Seconds for the\n                         current 15 minute period of monitoring.\n\n                         This parameter indicates the time in seconds that the\n                         link is available.\n\n                         Note that available time ends at the start of a block\n                         of ten consecutive Severely Errored Seconds and\n                         recommences at the start of a block of ten seconds\n                         each of which is not severely errored.')
aviatG826QHourUnavailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourUnavailableSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourUnavailableSeconds.setDescription('This is the number of Unavailable Seconds for the\n                         current 15 minute period of monitoring.\n\n                         Note that unavailable time commences at the start of a\n                         block of ten consecutive Severely Errored Seconds and\n                         ends at the start of a block of ten seconds each of\n                         which is not severely errored.')
aviatG826QHourInvalidEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826QHourInvalidEntry.setStatus('current')
if mibBuilder.loadTexts: aviatG826QHourInvalidEntry.setDescription('This indicates the validity of the performance data in\n                         this row of the table. It is set to TRUE when the data\n                         becomes invalid due to the interval not being within\n                         ten seconds of its nominal length otherwise it is set\n                         to FALSE.\n\n                         This could be a result of a time-of-day change.')
aviatG826DayTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4), )
if mibBuilder.loadTexts: aviatG826DayTable.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayTable.setDescription('This is a table containing a collection of information\n                         about the radio path performance of each terminal in\n                         the domain. Performance data in this table is recorded\n                         for 1 day periods.')
aviatG826DayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-G826-MIB", "aviatG826DayIndex"), (0, "AVIAT-G826-MIB", "aviatG826DayPeriod"))
if mibBuilder.loadTexts: aviatG826DayEntry.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayEntry.setDescription('This is an entry in the table containing performance\n                         data of a particular entity within the agent during a\n                         24 hour period.')
aviatG826DayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 1), Gauge32())
if mibBuilder.loadTexts: aviatG826DayIndex.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayIndex.setDescription('This is the row number referencing to the daily G.826\n                         performance data of a particular entity in the system.')
aviatG826DayPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 2), Gauge32())
if mibBuilder.loadTexts: aviatG826DayPeriod.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayPeriod.setDescription('This is the unique row number of the 1 day period\n                         during which this block of performance data was\n                         collected.')
aviatG826DayDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayDateAndTime.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayDateAndTime.setDescription('This is the date and time at the start of the current\n                         day period during which this block of performance data\n                         was collected.')
aviatG826DayErroredBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayErroredBlocks.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayErroredBlocks.setDescription('This is the number of G.826 Errored Blocks for the\n                         current 24 hour period of monitoring.\n\n                         This parameter indicates the number of blocks in which\n                         one or more bits are in error.')
aviatG826DayErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayErroredSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayErroredSeconds.setDescription('This is the number of G.826 Errored Seconds for the\n                         current 24 hour period of monitoring.\n\n                         This parameter indicates the number of one second\n                         periods with one or more errored blocks.')
aviatG826DayErroredSecondsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayErroredSecondsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayErroredSecondsRatio.setDescription('This is the G.826 Errored Seconds Ratio for the\n                         current 24 hour period of monitoring.\n\n                         The ratio is calculated by dividing the number of\n                         errored seconds by the available time. The ratio is\n                         then multiplied by 1E+7 to preserve 7 decimal places\n                         of the ratio while it is represented as an integer. If\n                         the available time is 0, then this object will also be\n                         0.')
aviatG826DaySeverelyErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DaySeverelyErroredSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826DaySeverelyErroredSeconds.setDescription('This is the number of G.826 Severely Errored Seconds\n                         for the current 24 hour period of monitoring.\n\n                         This parameter indicates the number of one second\n                         periods that contain 30%, or more, errored blocks or\n                         at least one defect.')
aviatG826DaySeverelyErroredSecsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DaySeverelyErroredSecsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826DaySeverelyErroredSecsRatio.setDescription('This is the G.826 Severely Errored Seconds Ratio for\n                         the current 24 hour period of monitoring.\n\n                         The ratio is calculated by dividing the number of\n                         severely errored seconds by the available time. The\n                         ratio is then multiplied by 1E+7 to preserve 7 decimal\n                         places of the ratio while it represented as an\n                         integer. If the available time is 0, then this object\n                         will also be 0.')
aviatG826DayBackgroundBlockErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayBackgroundBlockErrors.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayBackgroundBlockErrors.setDescription('This is the number of G.826 Background Block Errors\n                         for the current 24 hour period of monitoring.')
aviatG826DayBackgroundBlockErrorsRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayBackgroundBlockErrorsRatio.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayBackgroundBlockErrorsRatio.setDescription('This is the Background Block Errors Ratio for the\n                         current 24 hour period of monitoring.\n\n                         The ratio is calculated by dividing the number of\n                         Background Block Errors by the total number of blocks\n                         (excluding blocks transmitted during severely errored\n                         seconds). The ratio is then multiplied by 1E+14 to\n                         preserve 14 decimal places of the ratio while it is\n                         represented as an integer. If the total number of\n                         blocks is 0, then this object will also be 0.')
aviatG826DayAvailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayAvailableSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayAvailableSeconds.setDescription('This is the number of Available Seconds for the\n                         current 24 hour period of monitoring.\n\n                         This parameter indicates the time in seconds that the\n                         link is available.\n\n                         Note that available time ends at the start of a block\n                         of ten consecutive Severely Errored Seconds and\n                         recommences at the start of a block of ten seconds\n                         each of which is not severely errored.')
aviatG826DayUnavailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayUnavailableSeconds.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayUnavailableSeconds.setDescription('This is the number of Unavailable Seconds for the\n                         current 24 hour period of monitoring.\n\n                         Note that unavailable time commences at the start of a\n                         block of ten consecutive Severely Errored Seconds and\n                         ends at the start of a block of ten seconds each of\n                         which is not severely errored.')
aviatG826DayInvalidEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatG826DayInvalidEntry.setStatus('current')
if mibBuilder.loadTexts: aviatG826DayInvalidEntry.setDescription('This indicates the validity of the performance data in\n                         this row of the table. It is set to TRUE when the data\n                         becomes invalid due to the interval not being within\n                         ten seconds of its nominal length otherwise it is set\n                         to FALSE.\n\n                         This could be a result of a time-of-day change.')
aviatG826ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 1, 1)).setObjects(("AVIAT-G826-MIB", "aviatG826LastQHourChangeIndex"), ("AVIAT-G826-MIB", "aviatG826LastDayChangeIndex"), ("AVIAT-G826-MIB", "aviatG826Reset"), ("AVIAT-G826-MIB", "aviatG826ErroredBlocks"), ("AVIAT-G826-MIB", "aviatG826ErroredSeconds"), ("AVIAT-G826-MIB", "aviatG826ErroredSecondsRatio"), ("AVIAT-G826-MIB", "aviatG826SeverelyErroredSeconds"), ("AVIAT-G826-MIB", "aviatG826SeverelyErroredSecsRatio"), ("AVIAT-G826-MIB", "aviatG826BackgroundBlockErrors"), ("AVIAT-G826-MIB", "aviatG826BackgroundBlockErrorsRatio"), ("AVIAT-G826-MIB", "aviatG826AvailableSeconds"), ("AVIAT-G826-MIB", "aviatG826UnavailableSeconds"), ("AVIAT-G826-MIB", "aviatG826PackedData"), ("AVIAT-G826-MIB", "aviatG826QHourDateAndTime"), ("AVIAT-G826-MIB", "aviatG826QHourErroredBlocks"), ("AVIAT-G826-MIB", "aviatG826QHourErroredSeconds"), ("AVIAT-G826-MIB", "aviatG826QHourErroredSecondsRatio"), ("AVIAT-G826-MIB", "aviatG826QHourSeverelyErroredSeconds"), ("AVIAT-G826-MIB", "aviatG826QHourSeverelyErroredSecsRatio"), ("AVIAT-G826-MIB", "aviatG826QHourBackgroundBlockErrors"), ("AVIAT-G826-MIB", "aviatG826QHourBackgroundBlockErrorsRatio"), ("AVIAT-G826-MIB", "aviatG826QHourAvailableSeconds"), ("AVIAT-G826-MIB", "aviatG826QHourUnavailableSeconds"), ("AVIAT-G826-MIB", "aviatG826QHourInvalidEntry"), ("AVIAT-G826-MIB", "aviatG826DayDateAndTime"), ("AVIAT-G826-MIB", "aviatG826DayErroredBlocks"), ("AVIAT-G826-MIB", "aviatG826DayErroredSeconds"), ("AVIAT-G826-MIB", "aviatG826DayErroredSecondsRatio"), ("AVIAT-G826-MIB", "aviatG826DaySeverelyErroredSeconds"), ("AVIAT-G826-MIB", "aviatG826DaySeverelyErroredSecsRatio"), ("AVIAT-G826-MIB", "aviatG826DayBackgroundBlockErrors"), ("AVIAT-G826-MIB", "aviatG826DayBackgroundBlockErrorsRatio"), ("AVIAT-G826-MIB", "aviatG826DayAvailableSeconds"), ("AVIAT-G826-MIB", "aviatG826DayUnavailableSeconds"), ("AVIAT-G826-MIB", "aviatG826DayInvalidEntry"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatG826ObjectGroup = aviatG826ObjectGroup.setStatus('current')
if mibBuilder.loadTexts: aviatG826ObjectGroup.setDescription('These are objects in the G826 MIB.')
aviatG826ComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 2, 1)).setObjects(("AVIAT-G826-MIB", "aviatG826ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatG826ComplV1 = aviatG826ComplV1.setStatus('current')
if mibBuilder.loadTexts: aviatG826ComplV1.setDescription('The implementation requirements for this MIB.')
mibBuilder.exportSymbols("AVIAT-G826-MIB", aviatG826DayEntry=aviatG826DayEntry, aviatG826DayIndex=aviatG826DayIndex, aviatG826BackgroundBlockErrors=aviatG826BackgroundBlockErrors, aviatG826QHourSeverelyErroredSecsRatio=aviatG826QHourSeverelyErroredSecsRatio, aviatG826Groups=aviatG826Groups, aviatG826BackgroundBlockErrorsRatio=aviatG826BackgroundBlockErrorsRatio, aviatG826QHourBackgroundBlockErrorsRatio=aviatG826QHourBackgroundBlockErrorsRatio, aviatG826DayErroredSeconds=aviatG826DayErroredSeconds, aviatG826QHourBackgroundBlockErrors=aviatG826QHourBackgroundBlockErrors, aviatG826LastQHourChangeIndex=aviatG826LastQHourChangeIndex, aviatG826UnavailableSeconds=aviatG826UnavailableSeconds, aviatG826QHourPeriod=aviatG826QHourPeriod, aviatG826DayUnavailableSeconds=aviatG826DayUnavailableSeconds, aviatG826ControlEntry=aviatG826ControlEntry, aviatG826QHourIndex=aviatG826QHourIndex, aviatG826ControlTable=aviatG826ControlTable, aviatG826QHourDateAndTime=aviatG826QHourDateAndTime, aviatG826QHourInvalidEntry=aviatG826QHourInvalidEntry, aviatG826DayErroredSecondsRatio=aviatG826DayErroredSecondsRatio, aviatG826ErroredSecondsRatio=aviatG826ErroredSecondsRatio, aviatG826QHourErroredBlocks=aviatG826QHourErroredBlocks, aviatG826Conformance=aviatG826Conformance, aviatG826DayBackgroundBlockErrorsRatio=aviatG826DayBackgroundBlockErrorsRatio, aviatG826DayInvalidEntry=aviatG826DayInvalidEntry, aviatG826PerformEntry=aviatG826PerformEntry, aviatG826QHourAvailableSeconds=aviatG826QHourAvailableSeconds, aviatG826SeverelyErroredSeconds=aviatG826SeverelyErroredSeconds, aviatG826DayPeriod=aviatG826DayPeriod, aviatG826Reset=aviatG826Reset, aviatG826QuarterHourEntry=aviatG826QuarterHourEntry, aviatG826DaySeverelyErroredSeconds=aviatG826DaySeverelyErroredSeconds, aviatG826PackedData=aviatG826PackedData, aviatG826QHourSeverelyErroredSeconds=aviatG826QHourSeverelyErroredSeconds, aviatG826DayTable=aviatG826DayTable, aviatG826QHourUnavailableSeconds=aviatG826QHourUnavailableSeconds, aviatG826AvailableSeconds=aviatG826AvailableSeconds, aviatG826ObjectGroup=aviatG826ObjectGroup, aviatG826DaySeverelyErroredSecsRatio=aviatG826DaySeverelyErroredSecsRatio, aviatG826DayBackgroundBlockErrors=aviatG826DayBackgroundBlockErrors, aviatG826Compliance=aviatG826Compliance, aviatG826DayAvailableSeconds=aviatG826DayAvailableSeconds, aviatG826SeverelyErroredSecsRatio=aviatG826SeverelyErroredSecsRatio, aviatG826MIBObjects=aviatG826MIBObjects, PYSNMP_MODULE_ID=aviatG826Module, aviatG826ErroredSeconds=aviatG826ErroredSeconds, aviatG826QHourErroredSecondsRatio=aviatG826QHourErroredSecondsRatio, aviatG826DayErroredBlocks=aviatG826DayErroredBlocks, aviatG826LastDayChangeIndex=aviatG826LastDayChangeIndex, aviatG826QHourErroredSeconds=aviatG826QHourErroredSeconds, AviatPackedG826Data=AviatPackedG826Data, aviatG826QuarterHourTable=aviatG826QuarterHourTable, aviatG826ComplV1=aviatG826ComplV1, aviatG826DayDateAndTime=aviatG826DayDateAndTime, aviatG826Module=aviatG826Module, aviatG826ErroredBlocks=aviatG826ErroredBlocks, aviatG826PerformTable=aviatG826PerformTable)
