#
# PySNMP MIB module RADLAN-rlLcli-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-rlLcli-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:14:41 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, Gauge32, NotificationType, TimeTicks, ModuleIdentity, IpAddress, ObjectIdentity, Unsigned32, Counter32, Counter64, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "NotificationType", "TimeTicks", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Unsigned32", "Counter32", "Counter64", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
rlLCli = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 74))
rlLCli.setRevisions(('2005-04-11 00:00', '2005-03-28 00:00', '2004-03-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlLCli.setRevisionsDescriptions(("Changed lower range of rlLCliTimeout, rlLCliSshTimeout, rlLCliTelnetTimeout to 0\n                  to support 0 as 'no timeout' ", '1) Added Module-identity range.\n                  2) Changed description of rlLCliMibVersion\n                  3) Added ranges to rlLCliTimeout, rlLCliSshTimeout, rlLCliTelnetTimeout ', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: rlLCli.setLastUpdated('200503280000Z')
if mibBuilder.loadTexts: rlLCli.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlLCli.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlLCli.setDescription('The private MIB module definition for Radlan CLI MIB.')
rlLCliMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLCliMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlLCliMibVersion.setDescription("MIB's version, the current version is 3.")
rlLCliTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTimeout.setStatus('current')
if mibBuilder.loadTexts: rlLCliTimeout.setDescription('LCLI Timeout indicates the interval in seconds, that\n        the system waits until user input is detected.')
rlLCliHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliHistoryEnable.setStatus('current')
if mibBuilder.loadTexts: rlLCliHistoryEnable.setDescription('Indicates if command history function is supported.')
rlLCliHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliHistorySize.setStatus('current')
if mibBuilder.loadTexts: rlLCliHistorySize.setDescription('Indicates number of commands that the system will record\n        in its history buffer.')
rlLcliCommandLevelTable = MibTable((1, 3, 6, 1, 4, 1, 89, 74, 5), )
if mibBuilder.loadTexts: rlLcliCommandLevelTable.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelTable.setDescription('This Table maps a CLI command to its level. ')
rlLcliCommandLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 74, 5, 1), ).setIndexNames((0, "RADLAN-rlLcli-MIB", "rlLcliCommandLevelCommandName"), (0, "RADLAN-rlLcli-MIB", "rlLcliCommandLevelContextName"))
if mibBuilder.loadTexts: rlLcliCommandLevelEntry.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelEntry.setDescription('The row definition for this table.')
rlLcliCommandLevelCommandName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelCommandName.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelCommandName.setDescription(' The CLI command name ')
rlLcliCommandLevelContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelContextName.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelContextName.setDescription(' The CLI context ID which the command name is associated with ')
rlLcliCommandLevelInsertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelInsertTime.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelInsertTime.setDescription('The time elapsed until this entry was created.')
rlLcliCommandLevelCommandLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelCommandLevel.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelCommandLevel.setDescription(' The level which is associated with the command name ')
rlLcliCommandLevelActionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("set", 1), ("reset", 2), ("setAll", 3), ("resetAll", 4))).clone('set')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelActionMode.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelActionMode.setDescription(' The level action which is associated with the command name ')
rlLcliCommandLevelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelStatus.setStatus('current')
if mibBuilder.loadTexts: rlLcliCommandLevelStatus.setDescription(' The status of the commandLevel table entry. ')
rlLCliSshTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshTimeout.setStatus('current')
if mibBuilder.loadTexts: rlLCliSshTimeout.setDescription('LCLI Timeout indicates the interval in seconds, that\n        the system waits until user input is detected on SSH LCLI.')
rlLCliTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetTimeout.setStatus('current')
if mibBuilder.loadTexts: rlLCliTelnetTimeout.setDescription('LCLI Timeout indicates the interval in seconds, that\n        the system waits until user input is detected on telnet LCLI.')
rlLCliTelnetHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetHistoryEnable.setStatus('current')
if mibBuilder.loadTexts: rlLCliTelnetHistoryEnable.setDescription('Indicates if command history function is supported for Telnet.')
rlLCliTelnetHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetHistorySize.setStatus('current')
if mibBuilder.loadTexts: rlLCliTelnetHistorySize.setDescription('Indicates number of commands that the system will record\n         in its history buffer for Telnet.')
rlLCliSshHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 10), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshHistoryEnable.setStatus('current')
if mibBuilder.loadTexts: rlLCliSshHistoryEnable.setDescription('Indicates if command history function is supported for Ssh.')
rlLCliSshHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshHistorySize.setStatus('current')
if mibBuilder.loadTexts: rlLCliSshHistorySize.setDescription('Indicates number of commands that the system will record\n         in its history buffer for Ssh.')
mibBuilder.exportSymbols("RADLAN-rlLcli-MIB", rlLcliCommandLevelActionMode=rlLcliCommandLevelActionMode, rlLCliTelnetHistoryEnable=rlLCliTelnetHistoryEnable, rlLCliHistorySize=rlLCliHistorySize, rlLcliCommandLevelInsertTime=rlLcliCommandLevelInsertTime, rlLCliSshHistorySize=rlLCliSshHistorySize, rlLCliHistoryEnable=rlLCliHistoryEnable, rlLCliMibVersion=rlLCliMibVersion, rlLcliCommandLevelContextName=rlLcliCommandLevelContextName, rlLCliTelnetTimeout=rlLCliTelnetTimeout, rlLCliTimeout=rlLCliTimeout, rlLcliCommandLevelEntry=rlLcliCommandLevelEntry, rlLCliTelnetHistorySize=rlLCliTelnetHistorySize, rlLcliCommandLevelTable=rlLcliCommandLevelTable, rlLCliSshHistoryEnable=rlLCliSshHistoryEnable, rlLcliCommandLevelCommandName=rlLcliCommandLevelCommandName, rlLCliSshTimeout=rlLCliSshTimeout, rlLcliCommandLevelStatus=rlLcliCommandLevelStatus, rlLCli=rlLCli, rlLcliCommandLevelCommandLevel=rlLcliCommandLevelCommandLevel, PYSNMP_MODULE_ID=rlLCli)
