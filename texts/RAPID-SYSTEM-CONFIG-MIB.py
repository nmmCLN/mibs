#
# PySNMP MIB module RAPID-SYSTEM-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:13 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, enterprises, iso, TimeTicks, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, NotificationType, Bits, Counter64, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "iso", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "NotificationType", "Bits", "Counter64", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsSystemConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 2))
rsSystemConfigMIB.setRevisions(('1999-06-26 12:00', '2002-11-01 12:00', '2004-06-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsSystemConfigMIB.setRevisionsDescriptions(('Initial revision.', 'Changed CONTACT-INFO.', 'Removed old MIB objects.',))
if mibBuilder.loadTexts: rsSystemConfigMIB.setLastUpdated('9906261200Z')
if mibBuilder.loadTexts: rsSystemConfigMIB.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsSystemConfigMIB.setContactInfo('   Ella Yu\n                     WatchGuard Technologies, Inc.\n                     1841 Zanker Road\n                     San Jose, CA 95112\n                     USA\n\n                     408-519-4888\n                     ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsSystemConfigMIB.setDescription('The MIB module to describe WatchGuard Firebox system\n             configuration.')
rsSysTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 3))
if mibBuilder.loadTexts: rsSysTraps.setStatus('current')
if mibBuilder.loadTexts: rsSysTraps.setDescription('This is the base object for system wide traps \n             in this entity.')
rsSysTrapObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 4))
if mibBuilder.loadTexts: rsSysTrapObjects.setStatus('current')
if mibBuilder.loadTexts: rsSysTrapObjects.setDescription('This is the base object for objects which are used\n             as part of traps.')
rsSysTrapControl = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 5))
if mibBuilder.loadTexts: rsSysTrapControl.setStatus('current')
if mibBuilder.loadTexts: rsSysTrapControl.setDescription('This is the base object identifier for all objects\n             which are trap control for the entity.')
rsAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmId.setStatus('current')
if mibBuilder.loadTexts: rsAlarmId.setDescription('The id of the alarm that generates a trap.')
rsAlarmLabel = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmLabel.setStatus('current')
if mibBuilder.loadTexts: rsAlarmLabel.setDescription('The name of the alarm that generates a trap.')
rsAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmTime.setStatus('current')
if mibBuilder.loadTexts: rsAlarmTime.setDescription('The date and time of the alarm that generates a trap.')
rsAlarmLevel = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 3, 2, 1))).clone(namedValues=NamedValues(("normal", 4), ("warning", 3), ("error", 2), ("critical", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmLevel.setStatus('current')
if mibBuilder.loadTexts: rsAlarmLevel.setDescription('The level of an alarm generated.')
rsAlarmHostname = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmHostname.setStatus('current')
if mibBuilder.loadTexts: rsAlarmHostname.setDescription('The host name of the system where alarm occurred')
rsAlarmMsg = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmMsg.setStatus('current')
if mibBuilder.loadTexts: rsAlarmMsg.setDescription('The message describing the nature of this alarm.')
rsAlarmTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmTrapEnable.setStatus('current')
if mibBuilder.loadTexts: rsAlarmTrapEnable.setDescription('Indicates whether rsAlarmTrap trap should be generated.')
rsSysTrapsPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0))
if mibBuilder.loadTexts: rsSysTrapsPrefix.setStatus('current')
if mibBuilder.loadTexts: rsSysTrapsPrefix.setDescription('')
rsAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 1)).setObjects(("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmId"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLabel"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmTime"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLevel"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmHostname"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmMsg"))
if mibBuilder.loadTexts: rsAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: rsAlarmTrap.setDescription('An alarm was raised by Monitoring Agent of this\n             RapidStream entity.')
rsSnmpStart = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 2))
if mibBuilder.loadTexts: rsSnmpStart.setStatus('current')
if mibBuilder.loadTexts: rsSnmpStart.setDescription('This trap is sent when the snmp starts.')
rsSnmpShutdown = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 3))
if mibBuilder.loadTexts: rsSnmpShutdown.setStatus('current')
if mibBuilder.loadTexts: rsSnmpShutdown.setDescription('This trap is sent when the snmp terminates.')
mibBuilder.exportSymbols("RAPID-SYSTEM-CONFIG-MIB", rsAlarmTime=rsAlarmTime, rsSysTrapControl=rsSysTrapControl, rsAlarmLevel=rsAlarmLevel, rsAlarmHostname=rsAlarmHostname, rsSnmpStart=rsSnmpStart, rsAlarmTrap=rsAlarmTrap, PYSNMP_MODULE_ID=rsSystemConfigMIB, rsSysTrapObjects=rsSysTrapObjects, rsAlarmId=rsAlarmId, rsSysTrapsPrefix=rsSysTrapsPrefix, rsAlarmTrapEnable=rsAlarmTrapEnable, rsSnmpShutdown=rsSnmpShutdown, rsAlarmMsg=rsAlarmMsg, rsSystemConfigMIB=rsSystemConfigMIB, rsSysTraps=rsSysTraps, rsAlarmLabel=rsAlarmLabel)
