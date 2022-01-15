#
# PySNMP MIB module IANA-ITU-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANA-ITU-ALARM-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, iso, Integer32, mib_2, Bits, Counter32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "Integer32", "mib-2", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaItuAlarmNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 119))
ianaItuAlarmNumbers.setRevisions(('2014-05-22 00:00', '2004-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaItuAlarmNumbers.setRevisionsDescriptions(('Updated contact info.', 'Initial version, published as RFC 3877.',))
if mibBuilder.loadTexts: ianaItuAlarmNumbers.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianaItuAlarmNumbers.setOrganization('IANA')
if mibBuilder.loadTexts: ianaItuAlarmNumbers.setContactInfo('Postal:    Internet Assigned Numbers Authority\n                        Internet Corporation for Assigned Names\n                        and Numbers\n                        12025 Waterfront Drive, Suite 300\n                        Los Angeles, CA 90094-2536\n                        USA\n\n            Tel:    +1  310-301-5800\n            E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianaItuAlarmNumbers.setDescription('The MIB module defines the ITU Alarm\n            textual convention for objects expected to require\n            regular extension.\n\n            Copyright (C) The Internet Society (2004).  The\n            initial version of this MIB module was published\n            in RFC 3877. For full legal notices see the RFC\n            itself. Supplementary information may be available on:\n                 http://www.ietf.org/copyrights/ianamib.html')
class IANAItuProbableCause(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information\n               Model', 1995\n            ITU Recommendation X.733, 'Information Technology - Open\n               Systems Interconnection - System Management: Alarm\n               Reporting Function', 1992\n            ITU Recommendation X.736, 'Information Technology - Open\n               Systems Interconnection - System Management: Security\n               Alarm Reporting Function', 1992"
    description = 'ITU-T probable cause values. Duplicate values defined in\n            X.733 are appended with X733 to ensure syntactic uniqueness.\n            Probable cause value 0 is reserved for special purposes.\n\n            The Internet Assigned Number Authority (IANA) is responsible\n            for the assignment of the enumerations in this TC.\n            IANAItuProbableCause value of 0 is reserved for special\n            purposes and MUST NOT be assigned.\n\n            Values of IANAItuProbableCause in the range 1 to 1023 are\n            reserved for causes that correspond to ITU-T probable cause.\n\n            All other requests for new causes will be handled on a\n            first-come, first served basis and will be assigned\n            enumeration values starting with 1025.\n\n            Request should  come in the form of well-formed\n            SMI [RFC2578] for enumeration names that are unique and\n            sufficiently descriptive.\n\n            While some effort will be taken to ensure that new probable\n            causes do not conceptually duplicate existing probable\n            causes it is acknowledged that the existence of conceptual\n            duplicates in the starting probable cause list is an known\n            industry reality.\n\n            To aid IANA in the administration of probable cause names\n            and values, the OPS Area Director will appoint one or more\n            experts to help review requests.\n\n            See http://www.iana.org'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 201, 202, 203, 204, 205, 206, 207, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 1024))
    namedValues = NamedValues(("aIS", 1), ("callSetUpFailure", 2), ("degradedSignal", 3), ("farEndReceiverFailure", 4), ("framingError", 5), ("lossOfFrame", 6), ("lossOfPointer", 7), ("lossOfSignal", 8), ("payloadTypeMismatch", 9), ("transmissionError", 10), ("remoteAlarmInterface", 11), ("excessiveBER", 12), ("pathTraceMismatch", 13), ("unavailable", 14), ("signalLabelMismatch", 15), ("lossOfMultiFrame", 16), ("receiveFailure", 17), ("transmitFailure", 18), ("modulationFailure", 19), ("demodulationFailure", 20), ("broadcastChannelFailure", 21), ("connectionEstablishmentError", 22), ("invalidMessageReceived", 23), ("localNodeTransmissionError", 24), ("remoteNodeTransmissionError", 25), ("routingFailure", 26), ("backplaneFailure", 51), ("dataSetProblem", 52), ("equipmentIdentifierDuplication", 53), ("externalIFDeviceProblem", 54), ("lineCardProblem", 55), ("multiplexerProblem", 56), ("nEIdentifierDuplication", 57), ("powerProblem", 58), ("processorProblem", 59), ("protectionPathFailure", 60), ("receiverFailure", 61), ("replaceableUnitMissing", 62), ("replaceableUnitTypeMismatch", 63), ("synchronizationSourceMismatch", 64), ("terminalProblem", 65), ("timingProblem", 66), ("transmitterFailure", 67), ("trunkCardProblem", 68), ("replaceableUnitProblem", 69), ("realTimeClockFailure", 70), ("antennaFailure", 71), ("batteryChargingFailure", 72), ("diskFailure", 73), ("frequencyHoppingFailure", 74), ("iODeviceError", 75), ("lossOfSynchronisation", 76), ("lossOfRedundancy", 77), ("powerSupplyFailure", 78), ("signalQualityEvaluationFailure", 79), ("tranceiverFailure", 80), ("protectionMechanismFailure", 81), ("protectingResourceFailure", 82), ("airCompressorFailure", 101), ("airConditioningFailure", 102), ("airDryerFailure", 103), ("batteryDischarging", 104), ("batteryFailure", 105), ("commercialPowerFailure", 106), ("coolingFanFailure", 107), ("engineFailure", 108), ("fireDetectorFailure", 109), ("fuseFailure", 110), ("generatorFailure", 111), ("lowBatteryThreshold", 112), ("pumpFailure", 113), ("rectifierFailure", 114), ("rectifierHighVoltage", 115), ("rectifierLowFVoltage", 116), ("ventilationsSystemFailure", 117), ("enclosureDoorOpen", 118), ("explosiveGas", 119), ("fire", 120), ("flood", 121), ("highHumidity", 122), ("highTemperature", 123), ("highWind", 124), ("iceBuildUp", 125), ("intrusionDetection", 126), ("lowFuel", 127), ("lowHumidity", 128), ("lowCablePressure", 129), ("lowTemperatue", 130), ("lowWater", 131), ("smoke", 132), ("toxicGas", 133), ("coolingSystemFailure", 134), ("externalEquipmentFailure", 135), ("externalPointFailure", 136), ("storageCapacityProblem", 151), ("memoryMismatch", 152), ("corruptData", 153), ("outOfCPUCycles", 154), ("sfwrEnvironmentProblem", 155), ("sfwrDownloadFailure", 156), ("lossOfRealTimel", 157), ("applicationSubsystemFailure", 158), ("configurationOrCustomisationError", 159), ("databaseInconsistency", 160), ("fileError", 161), ("outOfMemory", 162), ("softwareError", 163), ("timeoutExpired", 164), ("underlayingResourceUnavailable", 165), ("versionMismatch", 166), ("bandwidthReduced", 201), ("congestion", 202), ("excessiveErrorRate", 203), ("excessiveResponseTime", 204), ("excessiveRetransmissionRate", 205), ("reducedLoggingCapability", 206), ("systemResourcesOverload", 207), ("adapterError", 500), ("applicationSubsystemFailture", 501), ("bandwidthReducedX733", 502), ("callEstablishmentError", 503), ("communicationsProtocolError", 504), ("communicationsSubsystemFailure", 505), ("configurationOrCustomizationError", 506), ("congestionX733", 507), ("coruptData", 508), ("cpuCyclesLimitExceeded", 509), ("dataSetOrModemError", 510), ("degradedSignalX733", 511), ("dteDceInterfaceError", 512), ("enclosureDoorOpenX733", 513), ("equipmentMalfunction", 514), ("excessiveVibration", 515), ("fileErrorX733", 516), ("fireDetected", 517), ("framingErrorX733", 518), ("heatingVentCoolingSystemProblem", 519), ("humidityUnacceptable", 520), ("inputOutputDeviceError", 521), ("inputDeviceError", 522), ("lanError", 523), ("leakDetected", 524), ("localNodeTransmissionErrorX733", 525), ("lossOfFrameX733", 526), ("lossOfSignalX733", 527), ("materialSupplyExhausted", 528), ("multiplexerProblemX733", 529), ("outOfMemoryX733", 530), ("ouputDeviceError", 531), ("performanceDegraded", 532), ("powerProblems", 533), ("pressureUnacceptable", 534), ("processorProblems", 535), ("pumpFailureX733", 536), ("queueSizeExceeded", 537), ("receiveFailureX733", 538), ("receiverFailureX733", 539), ("remoteNodeTransmissionErrorX733", 540), ("resourceAtOrNearingCapacity", 541), ("responseTimeExecessive", 542), ("retransmissionRateExcessive", 543), ("softwareErrorX733", 544), ("softwareProgramAbnormallyTerminated", 545), ("softwareProgramError", 546), ("storageCapacityProblemX733", 547), ("temperatureUnacceptable", 548), ("thresholdCrossed", 549), ("timingProblemX733", 550), ("toxicLeakDetected", 551), ("transmitFailureX733", 552), ("transmiterFailure", 553), ("underlyingResourceUnavailable", 554), ("versionMismatchX733", 555), ("authenticationFailure", 600), ("breachOfConfidentiality", 601), ("cableTamper", 602), ("delayedInformation", 603), ("denialOfService", 604), ("duplicateInformation", 605), ("informationMissing", 606), ("informationModificationDetected", 607), ("informationOutOfSequence", 608), ("keyExpired", 609), ("nonRepudiationFailure", 610), ("outOfHoursActivity", 611), ("outOfService", 612), ("proceduralError", 613), ("unauthorizedAccessAttempt", 614), ("unexpectedInformation", 615), ("other", 1024))

class IANAItuEventType(TextualConvention, Integer32):
    reference = "ITU Recommendation X.736, 'Information Technology - Open\n               Systems Interconnection - System Management: Security\n               Alarm Reporting Function', 1992"
    description = 'The ITU event Type values.\n\n               The Internet Assigned Number Authority (IANA) is\n               responsible for the assignment of the enumerations\n               in this TC.\n\n               Request should  come in the form of well-formed\n               SMI [RFC2578] for enumeration names that are unique\n               and sufficiently descriptive.\n\n               See http://www.iana.org '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("communicationsAlarm", 2), ("qualityOfServiceAlarm", 3), ("processingErrorAlarm", 4), ("equipmentAlarm", 5), ("environmentalAlarm", 6), ("integrityViolation", 7), ("operationalViolation", 8), ("physicalViolation", 9), ("securityServiceOrMechanismViolation", 10), ("timeDomainViolation", 11))

mibBuilder.exportSymbols("IANA-ITU-ALARM-TC-MIB", IANAItuEventType=IANAItuEventType, ianaItuAlarmNumbers=ianaItuAlarmNumbers, PYSNMP_MODULE_ID=ianaItuAlarmNumbers, IANAItuProbableCause=IANAItuProbableCause)
