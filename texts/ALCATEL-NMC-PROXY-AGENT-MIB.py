#
# PySNMP MIB module ALCATEL-NMC-PROXY-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/ALCATEL-NMC-PROXY-AGENT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:34 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
openViewSeverity, = mibBuilder.importSymbols("HPOV-NNM-MIB", "openViewSeverity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Gauge32, Counter32, Bits, enterprises, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity, NotificationType, NotificationType, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Gauge32", "Counter32", "Bits", "enterprises", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "NotificationType", "NotificationType", "MibIdentifier", "Counter64")
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
if mibBuilder.loadTexts: topClass.setDescription('identifier which allows the identification of the system.\r\r\n\tFor instance an Alcatel 4400')
baseClass = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseClass.setStatus('mandatory')
if mibBuilder.loadTexts: baseClass.setDescription('identifier which allows to identify the impacted object\r\r\n\twithout ambiguity for a given system. For instance\r\r\n\ta board of a 4400')
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
if mibBuilder.loadTexts: rdnDepth.setDescription('value that specifies the depth of the impacted object class\r\r\n\tinside the containment tree')
rdnValues = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3))
rdn1 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1))
classId1 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId1.setStatus('mandatory')
if mibBuilder.loadTexts: classId1.setDescription('object class, level one')
rdnValue1 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue1.setStatus('mandatory')
if mibBuilder.loadTexts: rdnValue1.setDescription('value, level one')
rdn2 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2))
classId2 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId2.setStatus('mandatory')
if mibBuilder.loadTexts: classId2.setDescription('object class, level two')
rdnValue2 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue2.setStatus('mandatory')
if mibBuilder.loadTexts: rdnValue2.setDescription('value, level two')
rdn3 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3))
classId3 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId3.setStatus('mandatory')
if mibBuilder.loadTexts: classId3.setDescription('object class, level three')
rdnValue3 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue3.setStatus('mandatory')
if mibBuilder.loadTexts: rdnValue3.setDescription('value, level three')
rdn4 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4))
classId4 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId4.setStatus('mandatory')
if mibBuilder.loadTexts: classId4.setDescription('object class, level four')
rdnValue4 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue4.setStatus('mandatory')
if mibBuilder.loadTexts: rdnValue4.setDescription('value, level four')
rdn5 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5))
classId5 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: classId5.setStatus('mandatory')
if mibBuilder.loadTexts: classId5.setDescription('object class, level five')
rdnValue5 = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnValue5.setStatus('mandatory')
if mibBuilder.loadTexts: rdnValue5.setDescription('value, level five')
eventTime = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTime.setStatus('mandatory')
if mibBuilder.loadTexts: eventTime.setDescription('date and time of detection of the notification\r\r\n\tby the managed system')
eventType = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 10, 11))).clone(namedValues=NamedValues(("communicationAlarm", 2), ("environmentalAlarm", 3), ("equipmentAlarm", 4), ("processingErrorAlarm", 10), ("qualityOfServiceAlarm", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('mandatory')
if mibBuilder.loadTexts: eventType.setDescription('OSI type of the notification')
severity = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("indeterminate", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("clear", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: severity.setStatus('mandatory')
if mibBuilder.loadTexts: severity.setDescription('OSI severity of the notification')
probableCause = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57))).clone(namedValues=NamedValues(("Unknown", 0), ("AdapterError", 1), ("ApplicationSubsystemFailure", 2), ("BandWidthReduced", 3), ("CallEstablishmentError", 4), ("CommunicationsProtocolError", 5), ("CommunicationsSubsystemFailure", 6), ("ConfigurationOrCustomizationError", 7), ("Congestion", 8), ("CorruptData", 9), ("CpuCyclesLimitExceeded", 10), ("DataSetOrModemError", 11), ("DegradedSignal", 12), ("DteDceInterfaceError", 13), ("EnclosureDoorOpen", 14), ("EquipmentMalFunction", 15), ("ExcessiveVibration", 16), ("FileError", 17), ("FireDetected", 18), ("FloodDetected", 19), ("FramingError", 20), ("HeatingVentilationCoolingSystemProblem", 21), ("HumidityUnacceptable", 22), ("InputOutputDeviceError", 23), ("InputDeviceError", 24), ("LANError", 25), ("LeakDetected", 26), ("LocalNodeTransmissionError", 27), ("LossOfFrame", 28), ("LossOfSignal", 29), ("MaterialSupplyExhausted", 30), ("MultiplexerProblem", 31), ("OutOfMemory", 32), ("OutputDeviceError", 33), ("PerformanceDegraded", 34), ("PowerProblem", 35), ("PressureUnacceptable", 36), ("ProcessorProblem", 37), ("PumpFailure", 38), ("QueueSizeExceeded", 39), ("ReceiveFailure", 40), ("ReceiverFailure", 41), ("RemoteNodeTransmissionFailure", 42), ("ResourceAtOrNearingCapacity", 43), ("ResponseTimeExcessive", 44), ("RetransmissionRateExcessive", 45), ("SoftwareError", 46), ("SoftwareProgramAbnormallyTerminated", 47), ("SoftwareProgramError", 48), ("StorageCapacityProblem", 49), ("TemperatureUnacceptable", 50), ("ThresholdCrossed", 51), ("TimingProblem", 52), ("ToxicLeakDetected", 53), ("TransmitFailure", 54), ("TransmitterFailure", 55), ("UnderlyingResourceUnavailable", 56), ("VersionMismatch", 57)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probableCause.setStatus('mandatory')
if mibBuilder.loadTexts: probableCause.setDescription('probable cause of the notification')
voiceIds = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4))
objectNumber = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: objectNumber.setStatus('optional')
if mibBuilder.loadTexts: objectNumber.setDescription('Object numeric identifier')
parentNumber = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: parentNumber.setStatus('optional')
if mibBuilder.loadTexts: parentNumber.setDescription('Parent object numeric identifier')
packedForm = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packedForm.setStatus('mandatory')
if mibBuilder.loadTexts: packedForm.setDescription('contains the packed form of a part (or all) of the arguments\r\r\n\tof a CMIP notification')
notificationId = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationId.setStatus('mandatory')
if mibBuilder.loadTexts: notificationId.setDescription('number that permits the exact identification of the\r\r\n\talarm that occured')
addText = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: addText.setStatus('optional')
if mibBuilder.loadTexts: addText.setDescription('contains text information')
packedCmipTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,1)).setObjects(("HPOV-NNM-MIB", "openViewSeverity"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "packedForm"))
if mibBuilder.loadTexts: packedCmipTrap.setDescription('packed forwarded trap :\r\r\n\tcontains a part (or all) of the arguments of the CMIP notification\r\r\n\tinside one variable binding.\r\r\n\tThe arguments are selected with the NMC.\r\r\n\tThis form suits well to a simple display of informations.\r\r\n\tHP OpenView Display=> Packed form: $2')
startOfResyncTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,2))
if mibBuilder.loadTexts: startOfResyncTrap.setDescription('start of resynchronization :\r\r\n\tthis trap announces the beginning of the reemission of all\r\r\n\tthe traps corresponding to the active alarms of\r\r\n\tthe managed nodes.\r\r\n\tHP OpenView Display=> Start of resynchronization: $*')
cmipTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,3)).setObjects(("ALCATEL-NMC-PROXY-AGENT-MIB", "topClass"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "baseClass"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnDepth"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId2"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue2"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId3"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue3"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId4"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue4"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId5"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue5"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "eventTime"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "eventType"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "severity"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "probableCause"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "notificationId"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "addText"))
if mibBuilder.loadTexts: cmipTrap.setDescription('developped form trap :\r\r\n\tcontains all arguments of the CMIP notification, each of them\r\r\n\tis placed in one independant variable binding.\r\r\n\tThis form suits well for the processing of informations on\r\r\n\ta supervision station in a view to build an application,\r\r\n\tlike a topology presentation and animation.\r\r\n\tHP OpenView Display=> Top class: $1 | Base Class: $2 | Hierarchy height: $3 | ClassId: $4-$6-$8-$10-$12 Values: $5-$7-$9-$11-$13 | Date: $14 | Event type: $15 | Severity: $16 | Probable cause: $17 | Notification ID: $18 | Add Text: $19')
startProxyTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,4))
if mibBuilder.loadTexts: startProxyTrap.setDescription('proxy started :\r\r\n\tthis trap announces that a proxy has just been started\r\r\n\tHP OpenView Display=> Start of NMC proxy $A')
stopProxyTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,5))
if mibBuilder.loadTexts: stopProxyTrap.setDescription('proxy stopped :\r\r\n\tthis trap announces that a proxy has just been stopped\r\r\n\tHP OpenView Display=> End of proxy: $A')
eventLostTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,6))
if mibBuilder.loadTexts: eventLostTrap.setDescription("event lost :\r\r\n\tthis trap announces that a proxy didn't succeed to send all\r\r\n\tevents and that the operator should perform a resynchronization.\r\r\n\tHP OpenView Display=> Event lost from $A")
topClassStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2) + (0,7)).setObjects(("ALCATEL-NMC-PROXY-AGENT-MIB", "classId1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue1"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "severity"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "objectNumber"), ("ALCATEL-NMC-PROXY-AGENT-MIB", "parentNumber"))
if mibBuilder.loadTexts: topClassStateTrap.setDescription('state trap :\r\r\n\tcontains arguments that describe the current state of a top class\r\r\n\tobject.\r\r\n\tHP OpenView Display=> Voice element $2 of class $1 has state $3')
mibBuilder.exportSymbols("ALCATEL-NMC-PROXY-AGENT-MIB", terminal=terminal, nmc4755=nmc4755, topClass=topClass, alcatel=alcatel, rdnValue3=rdnValue3, classId3=classId3, objectNumber=objectNumber, cmipTrap=cmipTrap, rdnDepth=rdnDepth, containmentTree=containmentTree, topClassStateTrap=topClassStateTrap, rdnValue1=rdnValue1, severity=severity, voiceIds=voiceIds, logicalLinks=logicalLinks, classId5=classId5, classId1=classId1, probableCause=probableCause, addText=addText, baseClass=baseClass, objectInstance=objectInstance, startProxyTrap=startProxyTrap, rdn4=rdn4, rdn1=rdn1, classId2=classId2, notificationId=notificationId, board=board, stopProxyTrap=stopProxyTrap, eventTime=eventTime, rdn5=rdn5, objectClass=objectClass, actOrSuEvents=actOrSuEvents, rdnValue4=rdnValue4, a4400=a4400, abs=abs, notification=notification, rdn3=rdn3, packedCmipTrap=packedCmipTrap, rdnValue5=rdnValue5, eventLostTrap=eventLostTrap, classId4=classId4, parentNumber=parentNumber, packedForm=packedForm, rdnValue2=rdnValue2, rdn2=rdn2, shelf=shelf, rdnValues=rdnValues, nmcProxyAgent=nmcProxyAgent, startOfResyncTrap=startOfResyncTrap, dect=dect, nmcProxyTraps=nmcProxyTraps, cmipEventArg=cmipEventArg, eventType=eventType)
