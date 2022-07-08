#
# PySNMP MIB module OGTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OGTRAP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:38 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, TimeTicks, ModuleIdentity, Counter64, MibIdentifier, Counter32, ObjectIdentity, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, IpAddress, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "TimeTicks", "ModuleIdentity", "Counter64", "MibIdentifier", "Counter32", "ObjectIdentity", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "IpAddress", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
opengear = MibIdentifier((1, 3, 6, 1, 4, 1, 25049))
ogLegacyMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2))
ogConnectMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 10))
ogSignalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11))
ogPatternMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12))
ogSensorMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13))
ogHostMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14))
ogFailoverMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15))
ogNetUpsMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16))
ogDataMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17))
ogConnectMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10))
ogconnEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1))
ogconnEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1))
ogconnEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1))
ogconnEventUsername = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventUsername.setStatus('mandatory')
ogconnEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventType.setStatus('mandatory')
ogconnEventPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortNumber.setStatus('mandatory')
ogconnEventPortLabel = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortLabel.setStatus('mandatory')
ogconnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1001)).setObjects(("OGTRAP-MIB", "ogconnEventUsername"), ("OGTRAP-MIB", "ogconnEventType"), ("OGTRAP-MIB", "ogconnEventPortNumber"), ("OGTRAP-MIB", "ogconnEventPortLabel"))
ogSignalMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10))
ogsgnlEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1))
ogsgnlEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1))
ogsgnlEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1))
ogsgnlEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventType.setStatus('mandatory')
ogsgnlEventState = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventState.setStatus('mandatory')
ogsgnlEventPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventPortNumber.setStatus('mandatory')
ogsgnlEventPortLabel = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventPortLabel.setStatus('mandatory')
ogsgnlEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1002)).setObjects(("OGTRAP-MIB", "ogsgnlEventType"), ("OGTRAP-MIB", "ogsgnlEventState"), ("OGTRAP-MIB", "ogsgnlEventPortNumber"), ("OGTRAP-MIB", "ogsgnlEventPortLabel"))
ogPatternMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10))
ogpatnEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1))
ogpatnEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1))
ogpatnEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1))
ogpatnEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventDescription.setStatus('mandatory')
ogpatnEventText = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventText.setStatus('mandatory')
ogpatnEventPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortNumber.setStatus('mandatory')
ogpatnEventPortLabel = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortLabel.setStatus('mandatory')
ogpatnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1003)).setObjects(("OGTRAP-MIB", "ogpatnEventDescription"), ("OGTRAP-MIB", "ogpatnEventText"), ("OGTRAP-MIB", "ogpatnEventPortNumber"), ("OGTRAP-MIB", "ogpatnEventPortLabel"))
ogSensorMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10))
ogsensStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1))
ogsensStatusTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1))
ogsensStatusEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1))
ogsensStatusName = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusName.setStatus('mandatory')
ogsensStatusDevType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusDevType.setStatus('mandatory')
ogsensStatusType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusType.setStatus('mandatory')
ogsensStatusValue = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusValue.setStatus('mandatory')
ogsensStatusOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1004)).setObjects(("OGTRAP-MIB", "ogsensStatusName"), ("OGTRAP-MIB", "ogsensStatusDevType"), ("OGTRAP-MIB", "ogsensStatusType"), ("OGTRAP-MIB", "ogsensStatusValue"))
ogHostMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10))
oghostEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1))
oghostEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1))
oghostEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1))
oghostEventUsername = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventUsername.setStatus('mandatory')
oghostEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventType.setStatus('mandatory')
oghostEventAddress = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventAddress.setStatus('mandatory')
oghostEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventDescription.setStatus('mandatory')
oghostEventProtocol = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventProtocol.setStatus('mandatory')
oghostEventPort = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventPort.setStatus('mandatory')
oghostEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2001)).setObjects(("OGTRAP-MIB", "oghostEventUsername"), ("OGTRAP-MIB", "oghostEventType"), ("OGTRAP-MIB", "oghostEventAddress"), ("OGTRAP-MIB", "oghostEventDescription"), ("OGTRAP-MIB", "oghostEventProtocol"), ("OGTRAP-MIB", "oghostEventPort"))
ogFailoverMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10))
ogfovrEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1))
ogfovrEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1))
ogfovrEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1))
ogfovrEventPrimary = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventPrimary.setStatus('mandatory')
ogfovrEventSecondary = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventSecondary.setStatus('mandatory')
ogfovrEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2002)).setObjects(("OGTRAP-MIB", "ogfovrEventPrimary"), ("OGTRAP-MIB", "ogfovrEventSecondary"))
ogNetUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10))
ognupsEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1))
ognupsEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1))
ognupsEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1))
ognupsEventName = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventName.setStatus('mandatory')
ognupsEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventType.setStatus('mandatory')
ognupsEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2003)).setObjects(("OGTRAP-MIB", "ognupsEventName"), ("OGTRAP-MIB", "ognupsEventType"))
ogDataMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10))
ogdataEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1))
ogdataEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1))
ogdataEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1))
ogdataEventBytes = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventBytes.setStatus('mandatory')
ogdataEventSeconds = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventSeconds.setStatus('mandatory')
ogdataEventDevice = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventDevice.setStatus('mandatory')
ogdataEventState = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventState.setStatus('mandatory')
ogdataEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2004)).setObjects(("OGTRAP-MIB", "ogdataEventBytes"), ("OGTRAP-MIB", "ogdataEventSeconds"), ("OGTRAP-MIB", "ogdataEventDevice"), ("OGTRAP-MIB", "ogdataEventState"))
mibBuilder.exportSymbols("OGTRAP-MIB", ogSignalMibObjects=ogSignalMibObjects, ogpatnEventTable=ogpatnEventTable, ogdataEventTable=ogdataEventTable, ogdataEventOccurred=ogdataEventOccurred, ognupsEventEntry=ognupsEventEntry, ogsensStatusType=ogsensStatusType, oghostEventAddress=oghostEventAddress, ogDataMib=ogDataMib, ogsensStatusName=ogsensStatusName, oghostEvent=oghostEvent, ogconnEventTable=ogconnEventTable, ogNetUpsMibObjects=ogNetUpsMibObjects, ogSensorMib=ogSensorMib, ogfovrEvent=ogfovrEvent, oghostEventProtocol=oghostEventProtocol, ogpatnEventText=ogpatnEventText, ogsensStatusOccurred=ogsensStatusOccurred, ogconnEventUsername=ogconnEventUsername, oghostEventTable=oghostEventTable, ogfovrEventTable=ogfovrEventTable, ogfovrEventEntry=ogfovrEventEntry, ogfovrEventPrimary=ogfovrEventPrimary, oghostEventUsername=oghostEventUsername, ogPatternMibObjects=ogPatternMibObjects, ogsensStatusValue=ogsensStatusValue, ogSensorMibObjects=ogSensorMibObjects, ognupsEvent=ognupsEvent, ogdataEventState=ogdataEventState, ogconnEventPortLabel=ogconnEventPortLabel, ognupsEventName=ognupsEventName, ogFailoverMibObjects=ogFailoverMibObjects, ogdataEvent=ogdataEvent, ogpatnEvent=ogpatnEvent, oghostEventPort=oghostEventPort, ogsgnlEvent=ogsgnlEvent, ogsensStatus=ogsensStatus, ogpatnEventPortNumber=ogpatnEventPortNumber, ogconnEventOccurred=ogconnEventOccurred, ogsgnlEventEntry=ogsgnlEventEntry, ogsgnlEventPortNumber=ogsgnlEventPortNumber, ogNetUpsMib=ogNetUpsMib, ogPatternMib=ogPatternMib, ogdataEventSeconds=ogdataEventSeconds, ogsgnlEventPortLabel=ogsgnlEventPortLabel, ogConnectMib=ogConnectMib, ogpatnEventOccurred=ogpatnEventOccurred, oghostEventOccurred=oghostEventOccurred, ogSignalMib=ogSignalMib, ogconnEvent=ogconnEvent, ogsensStatusDevType=ogsensStatusDevType, ogdataEventDevice=ogdataEventDevice, ogconnEventType=ogconnEventType, ogsensStatusTable=ogsensStatusTable, ognupsEventType=ognupsEventType, ognupsEventTable=ognupsEventTable, ogpatnEventDescription=ogpatnEventDescription, ogsgnlEventType=ogsgnlEventType, ogsensStatusEntry=ogsensStatusEntry, ogsgnlEventTable=ogsgnlEventTable, ogConnectMibObjects=ogConnectMibObjects, ogdataEventEntry=ogdataEventEntry, ogconnEventEntry=ogconnEventEntry, ogfovrEventSecondary=ogfovrEventSecondary, ogLegacyMgmt=ogLegacyMgmt, ogpatnEventPortLabel=ogpatnEventPortLabel, ogFailoverMib=ogFailoverMib, ogsgnlEventOccurred=ogsgnlEventOccurred, ogHostMib=ogHostMib, oghostEventType=oghostEventType, oghostEventDescription=oghostEventDescription, ogDataMibObjects=ogDataMibObjects, ogsgnlEventState=ogsgnlEventState, oghostEventEntry=oghostEventEntry, ogfovrEventOccurred=ogfovrEventOccurred, ogHostMibObjects=ogHostMibObjects, ogpatnEventEntry=ogpatnEventEntry, ogconnEventPortNumber=ogconnEventPortNumber, ognupsEventOccurred=ognupsEventOccurred, opengear=opengear, ogdataEventBytes=ogdataEventBytes)
