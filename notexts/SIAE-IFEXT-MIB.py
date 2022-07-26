#
# PySNMP MIB module SIAE-IFEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-IFEXT-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:34:11 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, iso, Counter64, NotificationType, TimeTicks, Unsigned32, Gauge32, Bits, IpAddress, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "iso", "Counter64", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ifext = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 73))
ifext.setRevisions(('2016-04-18 00:00', '2015-07-21 00:00', '2014-12-02 00:00', '2014-09-26 00:00', '2014-06-05 00:00', '2014-02-21 00:00', '2013-10-28 00:00',))
if mibBuilder.loadTexts: ifext.setLastUpdated('201604180000Z')
if mibBuilder.loadTexts: ifext.setOrganization('SIAE MICROELETTRONICA spa')
ifextMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextMibVersion.setStatus('current')
ifextTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2), )
if mibBuilder.loadTexts: ifextTable.setStatus('current')
ifextTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1), ).setIndexNames((0, "SIAE-IFEXT-MIB", "ifextIfIndex"))
if mibBuilder.loadTexts: ifextTableEntry.setStatus('current')
ifextIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ifextIfIndex.setStatus('current')
ifextLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextLabel.setStatus('current')
ifextAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("loopback", 4))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextAdminStatus.setStatus('current')
ifextPortUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unused", 0), ("lan", 1), ("radio", 2), ("mgmt", 3), ("stack", 4), ("aux", 5), ("pwe3", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextPortUsage.setStatus('current')
ifextMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("copper", 1), ("fiber", 2), ("combo", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextMediumType.setStatus('current')
ifextMediumSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("copper", 1), ("fiber", 2))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextMediumSelection.setStatus('current')
ifextAlarmReportEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifextAlarmReportEnable.setStatus('current')
ifextSfpId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextSfpId.setStatus('current')
ifextCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 9), Bits().clone(namedValues=NamedValues(("ifextCapabilityLoop", 0), ("ifextCapability2g5Bps", 1), ("ifextCapabilityMabSensor", 2), ("ifextCapabilityEncrypt", 3), ("ifextCapability10gBps", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextCapabilities.setStatus('current')
ifextLosAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextLosAlarm.setStatus('current')
ifextRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifextRowStatus.setStatus('current')
ifextMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3), )
if mibBuilder.loadTexts: ifextMaintTable.setStatus('current')
ifextMaintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3, 1), ).setIndexNames((0, "SIAE-IFEXT-MIB", "ifextIfIndex"))
if mibBuilder.loadTexts: ifextMaintTableEntry.setStatus('current')
ifextLineLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextLineLoop.setStatus('current')
ifextLosAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifextLosAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-IFEXT-MIB", ifextLosAlarmSeverityCode=ifextLosAlarmSeverityCode, ifextLosAlarm=ifextLosAlarm, ifextPortUsage=ifextPortUsage, ifextAdminStatus=ifextAdminStatus, ifextMediumType=ifextMediumType, ifextTable=ifextTable, ifextIfIndex=ifextIfIndex, ifextMibVersion=ifextMibVersion, ifextAlarmReportEnable=ifextAlarmReportEnable, ifextSfpId=ifextSfpId, ifextMaintTable=ifextMaintTable, ifextRowStatus=ifextRowStatus, ifext=ifext, ifextMaintTableEntry=ifextMaintTableEntry, PYSNMP_MODULE_ID=ifext, ifextLabel=ifextLabel, ifextLineLoop=ifextLineLoop, ifextCapabilities=ifextCapabilities, ifextMediumSelection=ifextMediumSelection, ifextTableEntry=ifextTableEntry)
