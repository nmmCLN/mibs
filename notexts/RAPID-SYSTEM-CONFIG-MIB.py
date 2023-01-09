#
# PySNMP MIB module RAPID-SYSTEM-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:45 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Gauge32, NotificationType, Bits, Counter64, ObjectIdentity, Unsigned32, Integer32, IpAddress, iso, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Gauge32", "NotificationType", "Bits", "Counter64", "ObjectIdentity", "Unsigned32", "Integer32", "IpAddress", "iso", "enterprises", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsSystemConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 2))
rsSystemConfigMIB.setRevisions(('1999-06-26 12:00', '2002-11-01 12:00', '2004-06-01 12:00',))
if mibBuilder.loadTexts: rsSystemConfigMIB.setLastUpdated('9906261200Z')
if mibBuilder.loadTexts: rsSystemConfigMIB.setOrganization('WatchGuard Technologies, Inc.')
rsSysTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 3))
if mibBuilder.loadTexts: rsSysTraps.setStatus('current')
rsSysTrapObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 4))
if mibBuilder.loadTexts: rsSysTrapObjects.setStatus('current')
rsSysTrapControl = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 5))
if mibBuilder.loadTexts: rsSysTrapControl.setStatus('current')
rsAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmId.setStatus('current')
rsAlarmLabel = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmLabel.setStatus('current')
rsAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmTime.setStatus('current')
rsAlarmLevel = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 3, 2, 1))).clone(namedValues=NamedValues(("normal", 4), ("warning", 3), ("error", 2), ("critical", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmLevel.setStatus('current')
rsAlarmHostname = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmHostname.setStatus('current')
rsAlarmMsg = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmMsg.setStatus('current')
rsAlarmTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmTrapEnable.setStatus('current')
rsSysTrapsPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0))
if mibBuilder.loadTexts: rsSysTrapsPrefix.setStatus('current')
rsAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 1)).setObjects(("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmId"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLabel"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmTime"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLevel"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmHostname"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmMsg"))
if mibBuilder.loadTexts: rsAlarmTrap.setStatus('current')
rsSnmpStart = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 2))
if mibBuilder.loadTexts: rsSnmpStart.setStatus('current')
rsSnmpShutdown = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 3))
if mibBuilder.loadTexts: rsSnmpShutdown.setStatus('current')
mibBuilder.exportSymbols("RAPID-SYSTEM-CONFIG-MIB", rsSysTrapControl=rsSysTrapControl, rsSysTraps=rsSysTraps, rsAlarmTime=rsAlarmTime, rsAlarmTrap=rsAlarmTrap, rsSnmpStart=rsSnmpStart, rsAlarmHostname=rsAlarmHostname, PYSNMP_MODULE_ID=rsSystemConfigMIB, rsSystemConfigMIB=rsSystemConfigMIB, rsAlarmId=rsAlarmId, rsAlarmMsg=rsAlarmMsg, rsAlarmTrapEnable=rsAlarmTrapEnable, rsSnmpShutdown=rsSnmpShutdown, rsAlarmLabel=rsAlarmLabel, rsSysTrapsPrefix=rsSysTrapsPrefix, rsAlarmLevel=rsAlarmLevel, rsSysTrapObjects=rsSysTrapObjects)
