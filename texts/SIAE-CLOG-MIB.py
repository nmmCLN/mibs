#
# PySNMP MIB module SIAE-CLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-CLOG-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:39 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
alarmTrap, = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap")
equipIpSnmpAgentAddress, = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
accessControlLoginIpAddress, = mibBuilder.importSymbols("SIAE-USER-MIB", "accessControlLoginIpAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, TimeTicks, iso, Counter64, Integer32, ObjectIdentity, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "TimeTicks", "iso", "Counter64", "Integer32", "ObjectIdentity", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
commandLog = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 40))
commandLog.setRevisions(('2015-03-23 00:00', '2014-06-23 00:00', '2014-02-03 00:00', '2013-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: commandLog.setRevisionsDescriptions(('Removed alarmTrapNumber from commandLogFtpStatusTrap and IMPORTS.\n            ', 'Fixed IMPORTS of accessControlLoginIpAddress\n            ', 'Improved description of commandLogMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: commandLog.setLastUpdated('201503230000Z')
if mibBuilder.loadTexts: commandLog.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: commandLog.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: help@siaemic.com\n            ')
if mibBuilder.loadTexts: commandLog.setDescription('Recorder of the commands entered from SNMP/CLI/WEB\n            ')
commandLogMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogMibVersion.setStatus('current')
if mibBuilder.loadTexts: commandLogMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
commandLogActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notActive", 0), ("delete", 1), ("read", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogActionRequest.setStatus('current')
if mibBuilder.loadTexts: commandLogActionRequest.setDescription('This leaf is used to delete record or to read it by FTP.')
commandLogFtpFile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogFtpFile.setStatus('current')
if mibBuilder.loadTexts: commandLogFtpFile.setDescription('This leaf is reserved to file path where to transfer data.')
commandLogMgmtInterfaceFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 4), Bits().clone(namedValues=NamedValues(("cli", 0), ("web", 1), ("snmp", 2), ("remoteCli", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogMgmtInterfaceFilter.setStatus('current')
if mibBuilder.loadTexts: commandLogMgmtInterfaceFilter.setDescription('Select which items are to be read or deleted \n             according to interface used to enter the registered command.\n             Bits set to 1 select the relative interface, bits set to 0\n             filter the relative interface')
commandLogStartTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogStartTimeFilter.setStatus('current')
if mibBuilder.loadTexts: commandLogStartTimeFilter.setDescription('The events with EventTime greater than this object are\n             read/delete from the log.\n             Null value means no filter.')
commandLogEndTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogEndTimeFilter.setStatus('current')
if mibBuilder.loadTexts: commandLogEndTimeFilter.setDescription('The events with EventTime less than this object are read/delete\n             from the log.\n             Null value means no filter.')
commandLogUserNameFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogUserNameFilter.setStatus('current')
if mibBuilder.loadTexts: commandLogUserNameFilter.setDescription('Name of the user that sent the request for the filter to manage\n             commands in the record. ** value means no filter.')
commandLogSourceAddressFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogSourceAddressFilter.setStatus('current')
if mibBuilder.loadTexts: commandLogSourceAddressFilter.setDescription('IP address of source machine of filter to manage\n             commands in the record. 0 value means no filter.')
commandLogFtpStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("transferring", 1), ("completed", 2), ("interrupted", 3), ("empty", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogFtpStatus.setStatus('current')
if mibBuilder.loadTexts: commandLogFtpStatus.setDescription('This leaf is used for the status of transfer.')
commandLogFtpStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogFtpStatusTrapNotification.setStatus('current')
if mibBuilder.loadTexts: commandLogFtpStatusTrapNotification.setDescription('Enables/disables the trap generation on FTP tranfer operation.')
commandLogLastCommandTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogLastCommandTime.setStatus('current')
if mibBuilder.loadTexts: commandLogLastCommandTime.setDescription('Describes the time, in seconds since 01/01/1970, of the last\n             SNMP command. The commands saves must be from a LOM. Some type\n             of commands, as login action or timestamp set, are skipped.')
commandLogLastCommandUser = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogLastCommandUser.setStatus('current')
if mibBuilder.loadTexts: commandLogLastCommandUser.setDescription('Describes the user that have made of the last SNMP command.\n             The commands saves must be from a LOM. Some type\n             of commands, as login action or timestamp set, are skipped.')
commandLogFtpStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 4001)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-CLOG-MIB", "commandLogFtpStatus"), ("SIAE-USER-MIB", "accessControlLoginIpAddress"))
if mibBuilder.loadTexts: commandLogFtpStatusTrap.setStatus('current')
if mibBuilder.loadTexts: commandLogFtpStatusTrap.setDescription('This event is generated when the status of FTP transfer is changed.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) commandLogFtpStatus\n                3) accessControlLoginIpAddress')
mibBuilder.exportSymbols("SIAE-CLOG-MIB", commandLogStartTimeFilter=commandLogStartTimeFilter, commandLogFtpStatusTrapNotification=commandLogFtpStatusTrapNotification, commandLogMibVersion=commandLogMibVersion, commandLog=commandLog, commandLogMgmtInterfaceFilter=commandLogMgmtInterfaceFilter, commandLogFtpFile=commandLogFtpFile, commandLogEndTimeFilter=commandLogEndTimeFilter, commandLogSourceAddressFilter=commandLogSourceAddressFilter, commandLogFtpStatus=commandLogFtpStatus, commandLogLastCommandTime=commandLogLastCommandTime, PYSNMP_MODULE_ID=commandLog, commandLogActionRequest=commandLogActionRequest, commandLogFtpStatusTrap=commandLogFtpStatusTrap, commandLogLastCommandUser=commandLogLastCommandUser, commandLogUserNameFilter=commandLogUserNameFilter)
