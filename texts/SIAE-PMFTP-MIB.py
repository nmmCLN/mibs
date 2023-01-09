#
# PySNMP MIB module SIAE-PMFTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-PMFTP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:29 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
alarmTrap, = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap")
equipIpSnmpAgentAddress, = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
accessControlLoginIpAddress, = mibBuilder.importSymbols("SIAE-USER-MIB", "accessControlLoginIpAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, NotificationType, iso, Counter32, Unsigned32, Integer32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "iso", "Counter32", "Unsigned32", "Integer32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pmFTP = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 31))
pmFTP.setRevisions(('2015-03-23 00:00', '2014-09-29 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pmFTP.setRevisionsDescriptions(('Removed alarmTrapNumber from pmFTPStatusTrap and IMPORTS.\n            ', 'MIB 01.00.01\n             - Added enumerator readInterval(7) to pmFTPActionRequest\n             - Added pmFTPBeginInterval and pmFTPEndInterval\n             - changed SYNTAX of pmFTPTpRmonOwner from INTEGER to OwnerString.\n            ', 'Improved description of pmFTPMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: pmFTP.setLastUpdated('201503230000Z')
if mibBuilder.loadTexts: pmFTP.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: pmFTP.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: help@siaemic.com\n            ')
if mibBuilder.loadTexts: pmFTP.setDescription('Transfer of data gathered by Performance Monitoring and RMON \n             to managers through the FTP protocol.\n             ')
pmFTPMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmFTPMibVersion.setStatus('current')
if mibBuilder.loadTexts: pmFTPMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
pmFTPfileName = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPfileName.setStatus('current')
if mibBuilder.loadTexts: pmFTPfileName.setDescription('Path and file name used when the PM data file is transferred\n             using Ftp (action = read).\n             The Agent software concatenates the following fields to the display\n             string set in this object:\n              1) groupName: it identifies the name of the P.M. mib group\n              2) tpClassName: it identifies the termination point\n              3) index: only for RMON data\n              4) date: YYMMDD\n             As example: when the string set is equal to /pub/pm/G828/alcplus\n             The name of the file transfered to the defined directory is:\n             alcplus_pmRxPwr_Radio1_081015.csv.')
pmFTPTpClass = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPTpClass.setStatus('current')
if mibBuilder.loadTexts: pmFTPTpClass.setDescription('Object identifier of the first leaf of the record selected \n             to transfer. To read all rows of a table, this object should be\n             set with the object identifier of the table entry.\n             The SET of the value {0 0} is accepted and means that no record\n             is selected.\n            ')
pmFTPTpRmonOwner = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 4), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPTpRmonOwner.setStatus('current')
if mibBuilder.loadTexts: pmFTPTpRmonOwner.setDescription('For PM is meaningless.\n             For RMON it corresponds to historyControlOwner of\n             historyControlTable and it cannot be null.\n             If pmFTPTpClass is set in order to read all rows of RMON history,\n             this object is used to select rows belonging to selected owner.\n            ')
pmFTPActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3, 5, 6, 7))).clone(namedValues=NamedValues(("none", 0), ("dayBeforeRead", 1), ("currentDayRead", 3), ("readAll", 5), ("readAbort", 6), ("readInterval", 7))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPActionRequest.setStatus('current')
if mibBuilder.loadTexts: pmFTPActionRequest.setDescription('Action requested to the equipment:\n              - none          : no action required;\n              - dayBeforeRead : for the selected PM or RMON group according to\n                                the selected TpClass a file with record of \n                                previous day is sent to the manager;\n              - currentDayRead: for the selected PM or RMON group according to\n                                the selected TpClass a file with records of\n                                the current day is sent to the manager;\n              - readAll       : for the selected PM or RMON group a file with\n                                records of current and previous day are\n                                sent to the manager;\n              - readAbort     : the action in progress will be interrupted.\n              - readInterval  : for the selected PM or RMON group according\n                                to the selected TpClass a file with records in\n                                the selected interval (see pmFTPBeginInterval\n                                and pmFTPEndInterval) is sent to the manager\n             The value of this object is self cleared (reset to the value none)\n             after its use.\n             The source IP address of the SNMP packet setting this object\n             is used as target Ip address, it identifies the server where the \n             files are transferred.')
pmFTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("transferring", 1), ("completed", 2), ("interrupted", 3), ("empty", 4), ("deleting", 5))).clone('completed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmFTPStatus.setStatus('current')
if mibBuilder.loadTexts: pmFTPStatus.setDescription('Status of pm Ftp transfer/delete operation.')
pmFTPStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPStatusTrapNotification.setStatus('current')
if mibBuilder.loadTexts: pmFTPStatusTrapNotification.setDescription('Enable/disable the trap generation on FTP tranfer operation.')
pmFTPCompressedFile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPCompressedFile.setStatus('current')
if mibBuilder.loadTexts: pmFTPCompressedFile.setDescription('Enable/disable the compression (zip) of the transferred files.\n             For RMON only.')
pmFTPBeginInterval = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPBeginInterval.setStatus('current')
if mibBuilder.loadTexts: pmFTPBeginInterval.setDescription('Defines the begin of the selected interval for the action \n             readInterval(7) (see pmFTPActionRequest). It is the number of\n             seconds since midnight of January 1, 1970.')
pmFTPEndInterval = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 31, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmFTPEndInterval.setStatus('current')
if mibBuilder.loadTexts: pmFTPEndInterval.setDescription('Defines the begin of the selected interval for the action \n             readInterval(7) (see pmFTPActionRequest). It is the number of\n             seconds since midnight of January 1, 1970. The value of this object\n             can not be less than pmFTPBeginInterval.')
pmFTPStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3101)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-PMFTP-MIB", "pmFTPStatus"), ("SIAE-USER-MIB", "accessControlLoginIpAddress"))
if mibBuilder.loadTexts: pmFTPStatusTrap.setStatus('current')
if mibBuilder.loadTexts: pmFTPStatusTrap.setDescription('This event is generated by NE when the status of FTP transfer is changed.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) pmFTPStatus\n                3) accessControlLoginIpAddress')
mibBuilder.exportSymbols("SIAE-PMFTP-MIB", pmFTPStatus=pmFTPStatus, pmFTP=pmFTP, pmFTPTpClass=pmFTPTpClass, pmFTPMibVersion=pmFTPMibVersion, pmFTPActionRequest=pmFTPActionRequest, pmFTPStatusTrapNotification=pmFTPStatusTrapNotification, pmFTPCompressedFile=pmFTPCompressedFile, pmFTPBeginInterval=pmFTPBeginInterval, pmFTPEndInterval=pmFTPEndInterval, PYSNMP_MODULE_ID=pmFTP, pmFTPStatusTrap=pmFTPStatusTrap, pmFTPfileName=pmFTPfileName, pmFTPTpRmonOwner=pmFTPTpRmonOwner)
