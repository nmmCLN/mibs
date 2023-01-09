#
# PySNMP MIB module APNNCItuX733Alarm-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APNNCItuX733Alarm-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, NotificationType, enterprises, Unsigned32, iso, Counter32, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "enterprises", "Unsigned32", "iso", "Counter32", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
apNNCItuX733AlarmModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6))
apNNCItuX733AlarmModule.setRevisions(('2013-07-20 00:00', '2014-06-26 00:00', '2018-03-28 00:00',))
if mibBuilder.loadTexts: apNNCItuX733AlarmModule.setLastUpdated('201803070000Z')
if mibBuilder.loadTexts: apNNCItuX733AlarmModule.setOrganization('ORACLE, Inc')
acmepacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9148))
acmepacketMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3))
apEMSModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8))
apNNCItuX733AlarmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 1))
apNNCItuX733NotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2))
apNNCItuX733NotificationId = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733NotificationId.setStatus('current')
apNNCItuX733ManagedObjectClass = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733ManagedObjectClass.setStatus('current')
apNNCItuX733ManagedObjectInstance = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733ManagedObjectInstance.setStatus('current')
apNNCItuX733PerceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733PerceivedSeverity.setStatus('current')
apNNCItuX733EventTime = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733EventTime.setStatus('current')
apNNCItuX733EventType = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("other", 1), ("communicationsAlarm", 2), ("qualityOfServiceAlarm", 3), ("processingErrorAlarm", 4), ("equipmentAlarm", 5), ("environmentalAlarm", 6), ("integrityViolation", 7), ("operationalViolation", 8), ("physicalViolation", 9), ("securityServiceOrMechanismViolation", 10), ("timeDomainViolation", 11)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733EventType.setStatus('current')
apNNCItuX733ProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75))).clone(namedValues=NamedValues(("other", 1), ("adapterError", 2), ("applicationSubsystemFailure", 3), ("bandwidthReduced", 4), ("callEstablishmentError", 5), ("communicationsProtocolError", 6), ("communicationsSubsystemFailure", 7), ("configurationOrCustomizationError", 8), ("congestion", 9), ("corruptData", 10), ("cpuCyclesLimitExceeded", 11), ("dataSetOrModemError", 12), ("degradedSignal", 13), ("dteDceInterfaceError", 14), ("enclosureDoorOpen", 15), ("equipmentMalfunction", 16), ("excessiveVibration", 17), ("fileError", 18), ("fireDetected", 19), ("floodDetected", 20), ("framingError", 21), ("heatingVentCoolingSystemProblem", 22), ("humidityUnacceptable", 23), ("inputOutputDeviceError", 24), ("inputDeviceError", 25), ("lanError", 26), ("leakDetected", 27), ("localNodeTransmissionError", 28), ("lossOfFrame", 29), ("lossOfSignal", 30), ("materialSupplyExhausted", 31), ("multiplexerProblem", 32), ("outOfMemory", 33), ("ouputDeviceError", 34), ("performanceDegraded", 35), ("powerProblem", 36), ("pressureUnacceptable", 37), ("processorProblem", 38), ("pumpFailure", 39), ("queueSizeExceeded", 40), ("receiveFailure", 41), ("receiverFailure", 42), ("remoteNodeTransmissionError", 43), ("resourceAtOrNearingCapacity", 44), ("responseTimeExecessive", 45), ("retransmissionRateExcessive", 46), ("softwareError", 47), ("softwareProgramAbnormallyTerminated", 48), ("softwareProgramError", 49), ("storageCapacityProblem", 50), ("temperatureUnacceptable", 51), ("thresholdCrossed", 52), ("timingProblem", 53), ("toxicLeakDetected", 54), ("transmitFailure", 55), ("transmitterFailure", 56), ("underlyingResourceUnavailable", 57), ("versionMismatch", 58), ("authenticationFailure", 59), ("breachOfConfidentiality", 60), ("cableTamper", 61), ("delayedInformation", 62), ("denialOfService", 63), ("duplicateInformation", 64), ("informationMissing", 65), ("informationModificationDetected", 66), ("informationOutOfSequence", 67), ("intrusionDetection", 68), ("keyExpired", 69), ("nonRepudiationFailure", 70), ("outOfHoursActivity", 71), ("outOfService", 72), ("proceduralError", 73), ("unauthorizedAccessAttempt", 74), ("unexpectedInformation", 75)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733ProbableCause.setStatus('current')
apNNCItuX733AdditionalText = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2048))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733AdditionalText.setStatus('current')
apNNCItuX733ThresholdInformation = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733ThresholdInformation.setStatus('current')
apNNCItuX733SpecificProblem = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733SpecificProblem.setStatus('current')
apNNCItuX733CorrelationNotificationIds = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 11), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733CorrelationNotificationIds.setStatus('current')
apNNCItuX733AdditionalInformation = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 12), ).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733AdditionalInformation.setStatus('current')
apNNCItuX733AdditionalInformationSeq = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 12, 1), ).setIndexNames((0, "APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalInformationIdentifier"))
if mibBuilder.loadTexts: apNNCItuX733AdditionalInformationSeq.setStatus('current')
apNNCItuX733AdditionalInformationIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("keyValue", 1), ("text", 2))).clone('keyValue')).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733AdditionalInformationIdentifier.setStatus('current')
apNNCItuX733AdditionalInformationIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 12, 1, 2), TruthValue().clone('false')).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733AdditionalInformationIndicator.setStatus('current')
apNNCItuX733AdditionalInformationInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 12, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2048))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733AdditionalInformationInformation.setStatus('current')
apNNCItuX733ProposedRepairAction = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 13), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apNNCItuX733ProposedRepairAction.setStatus('current')
apNNCItuX733Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 3))
apNNCItuX733NotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 3, 0))
apNNCItuX733Notification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 3, 0, 1)).setObjects(("APNNCItuX733Alarm-MIB", "apNNCItuX733NotificationId"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectClass"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectInstance"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733PerceivedSeverity"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventTime"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventType"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProbableCause"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalText"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ThresholdInformation"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733SpecificProblem"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733CorrelationNotificationIds"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalInformation"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProposedRepairAction"))
if mibBuilder.loadTexts: apNNCItuX733Notification.setStatus('current')
apNNCItuX733ModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4))
apNNCItuX733Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 1))
apNNCItuX733NotificationsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 2))
apNNCItuX733NotificationObjectsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 3))
apNNCItuX733NotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 2, 1)).setObjects(("APNNCItuX733Alarm-MIB", "apNNCItuX733Notification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCItuX733NotificationsGroup = apNNCItuX733NotificationsGroup.setStatus('current')
apNNCItuX733NotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 3, 1)).setObjects(("APNNCItuX733Alarm-MIB", "apNNCItuX733NotificationId"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectClass"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectInstance"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733PerceivedSeverity"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventTime"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventType"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProbableCause"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalText"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ThresholdInformation"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733SpecificProblem"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733CorrelationNotificationIds"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalInformationIdentifier"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalInformationIndicator"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalInformationInformation"), ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProposedRepairAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNNCItuX733NotificationObjectsGroup = apNNCItuX733NotificationObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("APNNCItuX733Alarm-MIB", apNNCItuX733SpecificProblem=apNNCItuX733SpecificProblem, apNNCItuX733NotificationsPrefix=apNNCItuX733NotificationsPrefix, apNNCItuX733Notifications=apNNCItuX733Notifications, apNNCItuX733EventType=apNNCItuX733EventType, apNNCItuX733AdditionalInformationSeq=apNNCItuX733AdditionalInformationSeq, apEMSModule=apEMSModule, apNNCItuX733ProposedRepairAction=apNNCItuX733ProposedRepairAction, apNNCItuX733ThresholdInformation=apNNCItuX733ThresholdInformation, apNNCItuX733ModuleConformance=apNNCItuX733ModuleConformance, apNNCItuX733NotificationsGroups=apNNCItuX733NotificationsGroups, apNNCItuX733EventTime=apNNCItuX733EventTime, apNNCItuX733NotificationObjects=apNNCItuX733NotificationObjects, apNNCItuX733NotificationId=apNNCItuX733NotificationId, acmepacket=acmepacket, acmepacketMgmt=acmepacketMgmt, apNNCItuX733ManagedObjectClass=apNNCItuX733ManagedObjectClass, PYSNMP_MODULE_ID=apNNCItuX733AlarmModule, apNNCItuX733PerceivedSeverity=apNNCItuX733PerceivedSeverity, apNNCItuX733AdditionalInformationIdentifier=apNNCItuX733AdditionalInformationIdentifier, apNNCItuX733AdditionalText=apNNCItuX733AdditionalText, apNNCItuX733ProbableCause=apNNCItuX733ProbableCause, apNNCItuX733CorrelationNotificationIds=apNNCItuX733CorrelationNotificationIds, apNNCItuX733Notification=apNNCItuX733Notification, apNNCItuX733AdditionalInformationIndicator=apNNCItuX733AdditionalInformationIndicator, apNNCItuX733Groups=apNNCItuX733Groups, apNNCItuX733AdditionalInformationInformation=apNNCItuX733AdditionalInformationInformation, apNNCItuX733ManagedObjectInstance=apNNCItuX733ManagedObjectInstance, apNNCItuX733AlarmModule=apNNCItuX733AlarmModule, apNNCItuX733NotificationObjectsGroup=apNNCItuX733NotificationObjectsGroup, apNNCItuX733NotificationsGroup=apNNCItuX733NotificationsGroup, apNNCItuX733NotificationObjectsGroups=apNNCItuX733NotificationObjectsGroups, apNNCItuX733AdditionalInformation=apNNCItuX733AdditionalInformation, apNNCItuX733AlarmMIBObjects=apNNCItuX733AlarmMIBObjects)
