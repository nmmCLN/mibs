#
# PySNMP MIB module SIAE-CLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-CLOG-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:16 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
alarmTrap, = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap")
equipIpSnmpAgentAddress, = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
accessControlLoginIpAddress, = mibBuilder.importSymbols("SIAE-USER-MIB", "accessControlLoginIpAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, TimeTicks, Unsigned32, Counter32, ModuleIdentity, Counter64, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Unsigned32", "Counter32", "ModuleIdentity", "Counter64", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
commandLog = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 40))
commandLog.setRevisions(('2015-03-23 00:00', '2014-06-23 00:00', '2014-02-03 00:00', '2013-12-18 00:00',))
if mibBuilder.loadTexts: commandLog.setLastUpdated('201503230000Z')
if mibBuilder.loadTexts: commandLog.setOrganization('SIAE MICROELETTRONICA spa')
commandLogMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogMibVersion.setStatus('current')
commandLogActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notActive", 0), ("delete", 1), ("read", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogActionRequest.setStatus('current')
commandLogFtpFile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogFtpFile.setStatus('current')
commandLogMgmtInterfaceFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 4), Bits().clone(namedValues=NamedValues(("cli", 0), ("web", 1), ("snmp", 2), ("remoteCli", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogMgmtInterfaceFilter.setStatus('current')
commandLogStartTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogStartTimeFilter.setStatus('current')
commandLogEndTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogEndTimeFilter.setStatus('current')
commandLogUserNameFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogUserNameFilter.setStatus('current')
commandLogSourceAddressFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogSourceAddressFilter.setStatus('current')
commandLogFtpStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("transferring", 1), ("completed", 2), ("interrupted", 3), ("empty", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogFtpStatus.setStatus('current')
commandLogFtpStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandLogFtpStatusTrapNotification.setStatus('current')
commandLogLastCommandTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogLastCommandTime.setStatus('current')
commandLogLastCommandUser = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 40, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandLogLastCommandUser.setStatus('current')
commandLogFtpStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 4001)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-CLOG-MIB", "commandLogFtpStatus"), ("SIAE-USER-MIB", "accessControlLoginIpAddress"))
if mibBuilder.loadTexts: commandLogFtpStatusTrap.setStatus('current')
mibBuilder.exportSymbols("SIAE-CLOG-MIB", commandLogActionRequest=commandLogActionRequest, commandLogMgmtInterfaceFilter=commandLogMgmtInterfaceFilter, commandLogFtpStatus=commandLogFtpStatus, commandLog=commandLog, commandLogFtpFile=commandLogFtpFile, commandLogUserNameFilter=commandLogUserNameFilter, commandLogFtpStatusTrapNotification=commandLogFtpStatusTrapNotification, commandLogLastCommandUser=commandLogLastCommandUser, PYSNMP_MODULE_ID=commandLog, commandLogFtpStatusTrap=commandLogFtpStatusTrap, commandLogSourceAddressFilter=commandLogSourceAddressFilter, commandLogLastCommandTime=commandLogLastCommandTime, commandLogStartTimeFilter=commandLogStartTimeFilter, commandLogMibVersion=commandLogMibVersion, commandLogEndTimeFilter=commandLogEndTimeFilter)
