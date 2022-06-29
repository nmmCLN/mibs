#
# PySNMP MIB module OGTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OGTRAP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:13:32 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, iso, Integer32, ModuleIdentity, TimeTicks, Gauge32, NotificationType, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Bits, Unsigned32, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Integer32", "ModuleIdentity", "TimeTicks", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32", "enterprises", "NotificationType")
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
if mibBuilder.loadTexts: ogconnEventUsername.setDescription('The user pertaining to the connection event')
ogconnEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventType.setStatus('mandatory')
if mibBuilder.loadTexts: ogconnEventType.setDescription('The type of connection event')
ogconnEventPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ogconnEventPortNumber.setDescription('Serial port number on which this connection applies')
ogconnEventPortLabel = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortLabel.setStatus('mandatory')
if mibBuilder.loadTexts: ogconnEventPortLabel.setDescription('The label for the serial port where the connection\n\t\t\toccurred.')
ogconnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1001)).setObjects(("OGTRAP-MIB", "ogconnEventUsername"), ("OGTRAP-MIB", "ogconnEventType"), ("OGTRAP-MIB", "ogconnEventPortNumber"), ("OGTRAP-MIB", "ogconnEventPortLabel"))
if mibBuilder.loadTexts: ogconnEventOccurred.setDescription('The alert sent when a user connection event occurs.')
ogSignalMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10))
ogsgnlEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1))
ogsgnlEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1))
ogsgnlEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1))
ogsgnlEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventType.setStatus('mandatory')
if mibBuilder.loadTexts: ogsgnlEventType.setDescription('The particular signal which changed')
ogsgnlEventState = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventState.setStatus('mandatory')
if mibBuilder.loadTexts: ogsgnlEventState.setDescription('The current signal state')
ogsgnlEventPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ogsgnlEventPortNumber.setDescription('Serial port number on which this signal applies')
ogsgnlEventPortLabel = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventPortLabel.setStatus('mandatory')
if mibBuilder.loadTexts: ogsgnlEventPortLabel.setDescription('The label for the serial port where the signal applies.')
ogsgnlEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1002)).setObjects(("OGTRAP-MIB", "ogsgnlEventType"), ("OGTRAP-MIB", "ogsgnlEventState"), ("OGTRAP-MIB", "ogsgnlEventPortNumber"), ("OGTRAP-MIB", "ogsgnlEventPortLabel"))
if mibBuilder.loadTexts: ogsgnlEventOccurred.setDescription('The alert sent when a signal change occurs')
ogPatternMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10))
ogpatnEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1))
ogpatnEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1))
ogpatnEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1))
ogpatnEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventDescription.setStatus('mandatory')
if mibBuilder.loadTexts: ogpatnEventDescription.setDescription('A description of the matches purpose')
ogpatnEventText = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventText.setStatus('mandatory')
if mibBuilder.loadTexts: ogpatnEventText.setDescription('The full text which matched the pattern')
ogpatnEventPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ogpatnEventPortNumber.setDescription('Serial port number on which the pattern matched')
ogpatnEventPortLabel = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortLabel.setStatus('mandatory')
if mibBuilder.loadTexts: ogpatnEventPortLabel.setDescription('The label for the serial port where pattern match\n\t\t\toccurred')
ogpatnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1003)).setObjects(("OGTRAP-MIB", "ogpatnEventDescription"), ("OGTRAP-MIB", "ogpatnEventText"), ("OGTRAP-MIB", "ogpatnEventPortNumber"), ("OGTRAP-MIB", "ogpatnEventPortLabel"))
if mibBuilder.loadTexts: ogpatnEventOccurred.setDescription('The alert sent when a pre-defined pattern was\n\t\t\tmatched text in a consoles serial character stream')
ogSensorMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10))
ogsensStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1))
ogsensStatusTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1))
ogsensStatusEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1))
ogsensStatusName = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusName.setStatus('mandatory')
if mibBuilder.loadTexts: ogsensStatusName.setDescription('The name of the device pertaining to the status event')
ogsensStatusDevType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusDevType.setStatus('mandatory')
if mibBuilder.loadTexts: ogsensStatusDevType.setDescription('The type of device pertaining to the status event')
ogsensStatusType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusType.setStatus('mandatory')
if mibBuilder.loadTexts: ogsensStatusType.setDescription('The type of sensor pertaining to the status event')
ogsensStatusValue = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusValue.setStatus('mandatory')
if mibBuilder.loadTexts: ogsensStatusValue.setDescription('The value of the sensor pertaining to the status event')
ogsensStatusOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1004)).setObjects(("OGTRAP-MIB", "ogsensStatusName"), ("OGTRAP-MIB", "ogsensStatusDevType"), ("OGTRAP-MIB", "ogsensStatusType"), ("OGTRAP-MIB", "ogsensStatusValue"))
if mibBuilder.loadTexts: ogsensStatusOccurred.setDescription('The trap sent when a sensor event occurs')
ogHostMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10))
oghostEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1))
oghostEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1))
oghostEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1))
oghostEventUsername = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventUsername.setStatus('mandatory')
if mibBuilder.loadTexts: oghostEventUsername.setDescription('The user pertaining to the connection event')
oghostEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventType.setStatus('mandatory')
if mibBuilder.loadTexts: oghostEventType.setDescription('The type of connection event')
oghostEventAddress = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventAddress.setStatus('mandatory')
if mibBuilder.loadTexts: oghostEventAddress.setDescription('The address of the host to which this connection applies.')
oghostEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventDescription.setStatus('mandatory')
if mibBuilder.loadTexts: oghostEventDescription.setDescription('The description of the host to which this connection applies.')
oghostEventProtocol = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: oghostEventProtocol.setDescription('The internet protocl to which this connection applies.')
oghostEventPort = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventPort.setStatus('mandatory')
if mibBuilder.loadTexts: oghostEventPort.setDescription('The applicable port number of the host.')
oghostEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2001)).setObjects(("OGTRAP-MIB", "oghostEventUsername"), ("OGTRAP-MIB", "oghostEventType"), ("OGTRAP-MIB", "oghostEventAddress"), ("OGTRAP-MIB", "oghostEventDescription"), ("OGTRAP-MIB", "oghostEventProtocol"), ("OGTRAP-MIB", "oghostEventPort"))
if mibBuilder.loadTexts: oghostEventOccurred.setDescription('The alert sent when a user connection event occurs')
ogFailoverMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10))
ogfovrEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1))
ogfovrEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1))
ogfovrEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1))
ogfovrEventPrimary = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventPrimary.setStatus('mandatory')
if mibBuilder.loadTexts: ogfovrEventPrimary.setDescription('The name of the network interface which failed')
ogfovrEventSecondary = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventSecondary.setStatus('mandatory')
if mibBuilder.loadTexts: ogfovrEventSecondary.setDescription('The name of the network interface which was connected\n\t\t\tinstead')
ogfovrEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2002)).setObjects(("OGTRAP-MIB", "ogfovrEventPrimary"), ("OGTRAP-MIB", "ogfovrEventSecondary"))
if mibBuilder.loadTexts: ogfovrEventOccurred.setDescription('The alert sent when a network failover event occurs')
ogNetUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10))
ognupsEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1))
ognupsEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1))
ognupsEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1))
ognupsEventName = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventName.setStatus('mandatory')
if mibBuilder.loadTexts: ognupsEventName.setDescription('The name of the UPS pertaining to the status event')
ognupsEventType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventType.setStatus('mandatory')
if mibBuilder.loadTexts: ognupsEventType.setDescription('The type of status event')
ognupsEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2003)).setObjects(("OGTRAP-MIB", "ognupsEventName"), ("OGTRAP-MIB", "ognupsEventType"))
if mibBuilder.loadTexts: ognupsEventOccurred.setDescription('The alert sent when a UPS status event occurs')
ogDataMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10))
ogdataEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1))
ogdataEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1))
ogdataEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1))
ogdataEventBytes = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ogdataEventBytes.setDescription('The amount of bytes which triggers this usage alert')
ogdataEventSeconds = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventSeconds.setStatus('mandatory')
if mibBuilder.loadTexts: ogdataEventSeconds.setDescription('The time in seconds over which bytes are measured')
ogdataEventDevice = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventDevice.setStatus('mandatory')
if mibBuilder.loadTexts: ogdataEventDevice.setDescription('The ID for the interface thos pertains to')
ogdataEventState = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventState.setStatus('mandatory')
if mibBuilder.loadTexts: ogdataEventState.setDescription('Whether data usage alert is on (1) or off (0)')
ogdataEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2004)).setObjects(("OGTRAP-MIB", "ogdataEventBytes"), ("OGTRAP-MIB", "ogdataEventSeconds"), ("OGTRAP-MIB", "ogdataEventDevice"), ("OGTRAP-MIB", "ogdataEventState"))
if mibBuilder.loadTexts: ogdataEventOccurred.setDescription('The trap sent when a data usage alert occurs')
mibBuilder.exportSymbols("OGTRAP-MIB", ogLegacyMgmt=ogLegacyMgmt, ognupsEventOccurred=ognupsEventOccurred, ogsgnlEventType=ogsgnlEventType, ogsensStatusOccurred=ogsensStatusOccurred, ogdataEventEntry=ogdataEventEntry, ogsgnlEventState=ogsgnlEventState, oghostEventDescription=oghostEventDescription, ogFailoverMib=ogFailoverMib, ogconnEventPortLabel=ogconnEventPortLabel, ogpatnEventText=ogpatnEventText, oghostEventOccurred=oghostEventOccurred, ogsensStatusEntry=ogsensStatusEntry, ogsgnlEvent=ogsgnlEvent, ogdataEventTable=ogdataEventTable, ogSignalMib=ogSignalMib, oghostEvent=oghostEvent, ogSignalMibObjects=ogSignalMibObjects, ogdataEventBytes=ogdataEventBytes, oghostEventEntry=oghostEventEntry, ogconnEventUsername=ogconnEventUsername, oghostEventProtocol=oghostEventProtocol, ogconnEventPortNumber=ogconnEventPortNumber, ogfovrEventOccurred=ogfovrEventOccurred, ogdataEventSeconds=ogdataEventSeconds, ogdataEventDevice=ogdataEventDevice, ogfovrEventTable=ogfovrEventTable, ogpatnEventDescription=ogpatnEventDescription, ogPatternMib=ogPatternMib, ogfovrEventSecondary=ogfovrEventSecondary, ogsensStatus=ogsensStatus, ogconnEventTable=ogconnEventTable, ogfovrEvent=ogfovrEvent, ogsensStatusType=ogsensStatusType, ogpatnEventPortLabel=ogpatnEventPortLabel, ognupsEventType=ognupsEventType, ogconnEventEntry=ogconnEventEntry, ogsensStatusTable=ogsensStatusTable, ogpatnEventPortNumber=ogpatnEventPortNumber, ogSensorMib=ogSensorMib, ogSensorMibObjects=ogSensorMibObjects, opengear=opengear, ogDataMib=ogDataMib, ogpatnEventEntry=ogpatnEventEntry, oghostEventUsername=oghostEventUsername, ogsensStatusDevType=ogsensStatusDevType, oghostEventAddress=oghostEventAddress, oghostEventPort=oghostEventPort, ogpatnEvent=ogpatnEvent, ogconnEventOccurred=ogconnEventOccurred, ogNetUpsMibObjects=ogNetUpsMibObjects, ogPatternMibObjects=ogPatternMibObjects, ogsgnlEventPortLabel=ogsgnlEventPortLabel, ogdataEventState=ogdataEventState, ogConnectMibObjects=ogConnectMibObjects, ogsgnlEventTable=ogsgnlEventTable, ogConnectMib=ogConnectMib, ogsgnlEventPortNumber=ogsgnlEventPortNumber, ogFailoverMibObjects=ogFailoverMibObjects, ogconnEvent=ogconnEvent, ogfovrEventPrimary=ogfovrEventPrimary, ogdataEvent=ogdataEvent, ogpatnEventTable=ogpatnEventTable, ognupsEvent=ognupsEvent, ognupsEventTable=ognupsEventTable, ogsgnlEventEntry=ogsgnlEventEntry, ogsgnlEventOccurred=ogsgnlEventOccurred, ogDataMibObjects=ogDataMibObjects, ogconnEventType=ogconnEventType, ogpatnEventOccurred=ogpatnEventOccurred, ogsensStatusName=ogsensStatusName, ogdataEventOccurred=ogdataEventOccurred, ognupsEventName=ognupsEventName, oghostEventTable=oghostEventTable, ogfovrEventEntry=ogfovrEventEntry, ogsensStatusValue=ogsensStatusValue, ogHostMibObjects=ogHostMibObjects, ogHostMib=ogHostMib, ogNetUpsMib=ogNetUpsMib, ognupsEventEntry=ognupsEventEntry, oghostEventType=oghostEventType)
