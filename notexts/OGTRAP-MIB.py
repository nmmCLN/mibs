#
# PySNMP MIB module OGTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OGTRAP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:17 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, IpAddress, NotificationType, Counter32, Integer32, ModuleIdentity, iso, NotificationType, Unsigned32, Bits, Counter64, MibIdentifier, TimeTicks, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "Counter32", "Integer32", "ModuleIdentity", "iso", "NotificationType", "Unsigned32", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("OGTRAP-MIB", ogConnectMibObjects=ogConnectMibObjects, ogdataEventBytes=ogdataEventBytes, ogconnEventUsername=ogconnEventUsername, ogsgnlEventOccurred=ogsgnlEventOccurred, ogpatnEventOccurred=ogpatnEventOccurred, ogfovrEventTable=ogfovrEventTable, ogfovrEventSecondary=ogfovrEventSecondary, ogdataEvent=ogdataEvent, ognupsEventType=ognupsEventType, ogdataEventOccurred=ogdataEventOccurred, ogSensorMib=ogSensorMib, oghostEventTable=oghostEventTable, ogsgnlEventType=ogsgnlEventType, ogsensStatusOccurred=ogsensStatusOccurred, ogconnEventPortLabel=ogconnEventPortLabel, ogLegacyMgmt=ogLegacyMgmt, ogNetUpsMibObjects=ogNetUpsMibObjects, ogfovrEventPrimary=ogfovrEventPrimary, ogsensStatus=ogsensStatus, opengear=opengear, ogpatnEventTable=ogpatnEventTable, oghostEventOccurred=oghostEventOccurred, ogfovrEventEntry=ogfovrEventEntry, ogpatnEventEntry=ogpatnEventEntry, ogconnEventTable=ogconnEventTable, ogDataMib=ogDataMib, ogsgnlEvent=ogsgnlEvent, ogdataEventDevice=ogdataEventDevice, oghostEventUsername=oghostEventUsername, ogSensorMibObjects=ogSensorMibObjects, ognupsEvent=ognupsEvent, ogconnEventPortNumber=ogconnEventPortNumber, ogdataEventTable=ogdataEventTable, ogsgnlEventTable=ogsgnlEventTable, oghostEventPort=oghostEventPort, ogFailoverMib=ogFailoverMib, ogdataEventEntry=ogdataEventEntry, ogPatternMib=ogPatternMib, ogconnEventOccurred=ogconnEventOccurred, ogsgnlEventEntry=ogsgnlEventEntry, ogpatnEventDescription=ogpatnEventDescription, ogSignalMibObjects=ogSignalMibObjects, ogsgnlEventPortLabel=ogsgnlEventPortLabel, ogdataEventSeconds=ogdataEventSeconds, ogHostMib=ogHostMib, ogsensStatusValue=ogsensStatusValue, oghostEventAddress=oghostEventAddress, ogsensStatusTable=ogsensStatusTable, ogsgnlEventState=ogsgnlEventState, ogConnectMib=ogConnectMib, ogFailoverMibObjects=ogFailoverMibObjects, ogdataEventState=ogdataEventState, ognupsEventOccurred=ognupsEventOccurred, ogsensStatusName=ogsensStatusName, ogpatnEventText=ogpatnEventText, ogpatnEventPortLabel=ogpatnEventPortLabel, ogconnEventEntry=ogconnEventEntry, ogDataMibObjects=ogDataMibObjects, ogfovrEvent=ogfovrEvent, ogpatnEventPortNumber=ogpatnEventPortNumber, ognupsEventEntry=ognupsEventEntry, ogsgnlEventPortNumber=ogsgnlEventPortNumber, ognupsEventName=ognupsEventName, ogconnEvent=ogconnEvent, ogNetUpsMib=ogNetUpsMib, ogsensStatusDevType=ogsensStatusDevType, oghostEventProtocol=oghostEventProtocol, oghostEventEntry=oghostEventEntry, oghostEventType=oghostEventType, ogPatternMibObjects=ogPatternMibObjects, oghostEvent=oghostEvent, ogpatnEvent=ogpatnEvent, ogHostMibObjects=ogHostMibObjects, ognupsEventTable=ognupsEventTable, ogsensStatusEntry=ogsensStatusEntry, oghostEventDescription=oghostEventDescription, ogconnEventType=ogconnEventType, ogSignalMib=ogSignalMib, ogsensStatusType=ogsensStatusType, ogfovrEventOccurred=ogfovrEventOccurred)
