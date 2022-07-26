#
# PySNMP MIB module ALCATEL-NMC-PROXY-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/ALCATEL-NMC-PROXY-AGENT-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:55 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
openViewSeverity, = mibBuilder.importSymbols("HPOV-NNM-MIB", "openViewSeverity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Gauge32, Counter32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ModuleIdentity, NotificationType, IpAddress, Integer32, NotificationType, iso, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "Counter32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ModuleIdentity", "NotificationType", "IpAddress", "Integer32", "NotificationType", "iso", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatel = MibIdentifier((1, 3, 6, 1, 4, 1, 637))
abs = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64))
nmc4755 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0))
notification = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10))
nmcProxyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1))
nmcProxyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2))
cmipEventArg = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1))
objectClass = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 1))
objectInstance = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2))
topClass = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topClass.setStatus('mandatory')
baseClass = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseClass.setStatus('mandatory')
containmentTree = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1))
a4400 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89))
shelf = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29))
board = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29, 23))
actOrSuEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29, 23, 175))
terminal = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29, 23, 175, 82))
logicalLinks = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 101))
dect = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 201))
rdnDepth = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnDepth.setStatus('mandatory')
rdnValues = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3))
rdn1 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1))
classId1 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId1.setStatus('mandatory')
rdnValue1 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue1.setStatus('mandatory')
rdn2 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2))
classId2 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId2.setStatus('mandatory')
rdnValue2 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue2.setStatus('mandatory')
rdn3 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3))
classId3 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId3.setStatus('mandatory')
rdnValue3 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue3.setStatus('mandatory')
rdn4 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4))
classId4 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId4.setStatus('mandatory')
rdnValue4 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue4.setStatus('mandatory')
rdn5 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5))
classId5 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId5.setStatus('mandatory')
rdnValue5 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue5.setStatus('mandatory')
eventTime = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTime.setStatus('mandatory')
eventType = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 10, 11))).clone(namedValues=NamedValues(("communicationAlarm", 2), ("environmentalAlarm", 3), ("equipmentAlarm", 4), ("processingErrorAlarm", 10), ("qualityOfServiceAlarm", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('mandatory')
severity = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("indeterminate", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("clear", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: severity.setStatus('mandatory')
probableCause = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57))).clone(namedValues=NamedValues(("Unknown", 0), ("AdapterError", 1), ("ApplicationSubsystemFailure", 2), ("BandWidthReduced", 3), ("CallEstablishmentError", 4), ("CommunicationsProtocolError", 5), ("CommunicationsSubsystemFailure", 6), ("ConfigurationOrCustomizationError", 7), ("Congestion", 8), ("CorruptData", 9), ("CpuCyclesLimitExceeded", 10), ("DataSetOrModemError", 11), ("DegradedSignal", 12), ("DteDceInterfaceError", 13), ("EnclosureDoorOpen", 14), ("EquipmentMalFunction", 15), ("ExcessiveVibration", 16), ("FileError", 17), ("FireDetected", 18), ("FloodDetected", 19), ("FramingError", 20), ("HeatingVentilationCoolingSystemProblem", 21), ("HumidityUnacceptable", 22), ("InputOutputDeviceError", 23), ("InputDeviceError", 24), ("LANError", 25), ("LeakDetected", 26), ("LocalNodeTransmissionError", 27), ("LossOfFrame", 28), ("LossOfSignal", 29), ("MaterialSupplyExhausted", 30), ("MultiplexerProblem", 31), ("OutOfMemory", 32), ("OutputDeviceError", 33), ("PerformanceDegraded", 34), ("PowerProblem", 35), ("PressureUnacceptable", 36), ("ProcessorProblem", 37), ("PumpFailure", 38), ("QueueSizeExceeded", 39), ("ReceiveFailure", 40), ("ReceiverFailure", 41), ("RemoteNodeTransmissionFailure", 42), ("ResourceAtOrNearingCapacity", 43), ("ResponseTimeExcessive", 44), ("RetransmissionRateExcessive", 45), ("SoftwareError", 46), ("SoftwareProgramAbnormallyTerminated", 47), ("SoftwareProgramError", 48), ("StorageCapacityProblem", 49), ("TemperatureUnacceptable", 50), ("ThresholdCrossed", 51), ("TimingProblem", 52), ("ToxicLeakDetected", 53), ("TransmitFailure", 54), ("TransmitterFailure", 55), ("UnderlyingResourceUnavailable", 56), ("VersionMismatch", 57)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probableCause.setStatus('mandatory')
voiceIds = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4))
objectNumber = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: objectNumber.setStatus('optional')
parentNumber = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: parentNumber.setStatus('optional')
packedForm = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packedForm.setStatus('mandatory')
notificationId = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationId.setStatus('mandatory')
addText = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: addText.setStatus('optional')
packedCmipTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,1)).setObjects(("HPOV-NNM-MIB", "openViewSeverity"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "packedForm"))
startOfResyncTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,2))
cmipTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,3)).setObjects(("ALCATEL-NMC-PROXY-AGENT-MIB", "topClass"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "baseClass"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnDepth"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId2"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue2"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId3"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue3"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId4"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue4"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId5"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue5"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "eventTime"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "eventType"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "severity"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "probableCause"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "notificationId"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "addText"))
startProxyTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,4))
stopProxyTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,5))
eventLostTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,6))
topClassStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,7)).setObjects(("ALCATEL-NMC-PROXY-AGENT-MIB", "classId1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "severity"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "objectNumber"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "parentNumber"))
mibBuilder.exportSymbols("ALCATEL-NMC-PROXY-AGENT-MIB", objectNumber=objectNumber, cmipTrap=cmipTrap, dect=dect, board=board, rdnDepth=rdnDepth, terminal=terminal, cmipEventArg=cmipEventArg, rdnValues=rdnValues, objectInstance=objectInstance, rdnValue1=rdnValue1, objectClass=objectClass, rdnValue2=rdnValue2, logicalLinks=logicalLinks, packedForm=packedForm, eventLostTrap=eventLostTrap, nmcProxyTraps=nmcProxyTraps, rdn2=rdn2, rdnValue3=rdnValue3, classId2=classId2, classId5=classId5, voiceIds=voiceIds, addText=addText, notification=notification, rdnValue5=rdnValue5, baseClass=baseClass, shelf=shelf, rdn1=rdn1, rdn5=rdn5, notificationId=notificationId, startProxyTrap=startProxyTrap, abs=abs, a4400=a4400, classId1=classId1, alcatel=alcatel, rdn3=rdn3, classId3=classId3, packedCmipTrap=packedCmipTrap, containmentTree=containmentTree, topClass=topClass, eventType=eventType, parentNumber=parentNumber, eventTime=eventTime, rdn4=rdn4, nmc4755=nmc4755, nmcProxyAgent=nmcProxyAgent, classId4=classId4, topClassStateTrap=topClassStateTrap, probableCause=probableCause, startOfResyncTrap=startOfResyncTrap, severity=severity, actOrSuEvents=actOrSuEvents, rdnValue4=rdnValue4, stopProxyTrap=stopProxyTrap)
