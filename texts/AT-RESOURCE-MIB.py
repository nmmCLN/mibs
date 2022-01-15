#
# PySNMP MIB module AT-RESOURCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-RESOURCE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:26 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Counter32, ModuleIdentity, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Counter32", "ModuleIdentity", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
resource = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21))
resource.setRevisions(('2014-05-26 00:00', '2014-04-30 00:00', '2014-04-16 00:00', '2012-09-21 00:00', '2012-05-22 03:00', '2010-06-15 00:15', '2009-10-22 23:00', '2008-10-20 10:00', '1920-08-09 04:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: resource.setRevisionsDescriptions(('Updated decriptions for hostInfoTable and hostInfoEntry', 'Updated decriptions to refer to chassisMappingTable', 'Added more descriptions to rscStkId for VCStack Plus and increase\n                 the range to 1-24.', 'Added chassis switch (e.g. SBx8100) descriptions to stack-related MIB objects', 'rscStkId range now 1..12 (from 1..8).', 'MIB revision history dates in descriptions updated.', 'In standalone mode the AT-RESOURCE-MIB was indexed by the\n                default stack member ID of 1.  This has been updated to index\n                by the stack member ID of the device.', 'Add objects for displaying host information. ', 'Initial version.',))
if mibBuilder.loadTexts: resource.setLastUpdated('201405260000Z')
if mibBuilder.loadTexts: resource.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: resource.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: resource.setDescription('The AT-RESOURCE-MIB contains objects for displaying system\n                hardware resource information.')
rscBoardTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1), )
if mibBuilder.loadTexts: rscBoardTable.setStatus('current')
if mibBuilder.loadTexts: rscBoardTable.setDescription('A table of information about boards installed in a device.')
rscBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1), ).setIndexNames((0, "AT-RESOURCE-MIB", "rscStkId"), (0, "AT-RESOURCE-MIB", "rscResourceId"))
if mibBuilder.loadTexts: rscBoardEntry.setStatus('current')
if mibBuilder.loadTexts: rscBoardEntry.setDescription('A conceptual row of entries of rscBoardTable.')
rscStkId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)))
if mibBuilder.loadTexts: rscStkId.setStatus('current')
if mibBuilder.loadTexts: rscStkId.setDescription('The ID of the stack member. It is a number assigned to\n                a stackable unit by the operating system when it is stacked.\n                An initial value of 1 is given to a stand alone unit. For a\n                chassis switch, it corresponds to the card ID. For VCStack Plus,\n                1-12 refers to the cards on VCS stack member 1 and 13-24 refers\n                to the cards on VCS stack member 2.\n                Refer to chassisMappingTable for more details.')
rscResourceId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)))
if mibBuilder.loadTexts: rscResourceId.setStatus('current')
if mibBuilder.loadTexts: rscResourceId.setDescription('The resource ID number of the board. It is a number assigned to\n                a hardware resource when the operating system detects\n                its existence.')
rscBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardType.setStatus('current')
if mibBuilder.loadTexts: rscBoardType.setDescription("This object indicates the type of the board. Its value can be\n                'Base', 'Expansion', 'Fan module' or 'PSU', etc.")
rscBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardName.setStatus('current')
if mibBuilder.loadTexts: rscBoardName.setDescription("This object represents the name of the board. Its value can be\n                'SwitchBlade x908', 'XEM-12S' or 'AT-PWR05-AC', etc.")
rscBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardID.setStatus('current')
if mibBuilder.loadTexts: rscBoardID.setDescription('This object represents the ID number of the board. Its value is an\n                Allied Telesis assigned number, such as 274 for the XEM-12S, or 255\n                for the AT-9924Ts. ')
rscBoardBay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscBoardBay.setStatus('current')
if mibBuilder.loadTexts: rscBoardBay.setDescription("This object indicates the board installation location. Its\n                value can be 'Bay1', 'Bay2' or 'PSU1', etc. For a base board,\n                it has a value of a single character space. ")
rscBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardRevision.setStatus('current')
if mibBuilder.loadTexts: rscBoardRevision.setDescription('This object represents the revision number of the board.')
rscBoardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardSerialNumber.setStatus('current')
if mibBuilder.loadTexts: rscBoardSerialNumber.setDescription('This object represents the serial number of the board.')
hostInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2), )
if mibBuilder.loadTexts: hostInfoTable.setStatus('current')
if mibBuilder.loadTexts: hostInfoTable.setDescription('A list of host entries.')
hostInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1), ).setIndexNames((0, "AT-RESOURCE-MIB", "rscStkId"))
if mibBuilder.loadTexts: hostInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hostInfoEntry.setDescription('A set of parameters that describe a single host.')
hostInfoDRAM = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoDRAM.setStatus('current')
if mibBuilder.loadTexts: hostInfoDRAM.setDescription('This object indicates the host DRAM information.')
hostInfoFlash = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoFlash.setStatus('current')
if mibBuilder.loadTexts: hostInfoFlash.setDescription('This object indicates the host Flash information.')
hostInfoUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoUptime.setStatus('current')
if mibBuilder.loadTexts: hostInfoUptime.setDescription('This object represents the host up time.')
hostInfoBootloaderVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoBootloaderVersion.setStatus('current')
if mibBuilder.loadTexts: hostInfoBootloaderVersion.setDescription('This object represents the host boot loader version.')
mibBuilder.exportSymbols("AT-RESOURCE-MIB", hostInfoEntry=hostInfoEntry, rscBoardEntry=rscBoardEntry, PYSNMP_MODULE_ID=resource, hostInfoTable=hostInfoTable, rscBoardName=rscBoardName, hostInfoUptime=hostInfoUptime, rscBoardRevision=rscBoardRevision, resource=resource, rscResourceId=rscResourceId, hostInfoBootloaderVersion=hostInfoBootloaderVersion, hostInfoFlash=hostInfoFlash, rscBoardID=rscBoardID, rscBoardType=rscBoardType, hostInfoDRAM=hostInfoDRAM, rscStkId=rscStkId, rscBoardBay=rscBoardBay, rscBoardSerialNumber=rscBoardSerialNumber, rscBoardTable=rscBoardTable)
