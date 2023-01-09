#
# PySNMP MIB module AT-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LOG-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:48 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Integer32, Unsigned32, Counter64, Counter32, Bits, IpAddress, TimeTicks, Gauge32, MibIdentifier, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Integer32", "Unsigned32", "Counter64", "Counter32", "Bits", "IpAddress", "TimeTicks", "Gauge32", "MibIdentifier", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
log = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601))
log.setRevisions(('2016-06-23 00:00', '2012-06-08 00:00', '2012-06-07 00:00', '2011-05-30 00:00', '2011-04-18 00:00', '2010-09-07 00:00', '2010-06-14 05:11', '2008-10-08 00:00',))
if mibBuilder.loadTexts: log.setLastUpdated('201606230000Z')
if mibBuilder.loadTexts: log.setOrganization('Allied Telesis Labs New Zealand')
logNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 0))
logProcessKilledNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 0, 1)).setObjects(("AT-LOG-MIB", "logProcessKilled"))
if mibBuilder.loadTexts: logProcessKilledNotify.setStatus('current')
logTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1), )
if mibBuilder.loadTexts: logTable.setStatus('current')
logEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1), ).setIndexNames((0, "AT-LOG-MIB", "logIndex"))
if mibBuilder.loadTexts: logEntry.setStatus('current')
logIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: logIndex.setStatus('current')
logDate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logDate.setStatus('current')
logTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logTime.setStatus('current')
logFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logFacility.setStatus('current')
logSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSeverity.setStatus('current')
logProgram = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logProgram.setStatus('current')
logMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMessage.setStatus('current')
logOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2))
logSource = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bufferedLog", 1), ("permanentLog", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logSource.setStatus('current')
logAll = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logAll.setStatus('current')
clearLog = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearLog.setStatus('current')
logProcessKilled = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logProcessKilled.setStatus('current')
mibBuilder.exportSymbols("AT-LOG-MIB", logProcessKilled=logProcessKilled, clearLog=clearLog, logIndex=logIndex, logSource=logSource, logProgram=logProgram, logSeverity=logSeverity, logTime=logTime, log=log, logOptions=logOptions, logProcessKilledNotify=logProcessKilledNotify, logEntry=logEntry, logNotifications=logNotifications, logTable=logTable, logAll=logAll, logDate=logDate, logFacility=logFacility, PYSNMP_MODULE_ID=log, logMessage=logMessage)
