#
# PySNMP MIB module ASCOM-IPDECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ascom/ASCOM-IPDECT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:30 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Integer32, IpAddress, iso, Bits, MibIdentifier, ObjectIdentity, NotificationType, Unsigned32, Counter64, enterprises, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Integer32", "IpAddress", "iso", "Bits", "MibIdentifier", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter64", "enterprises", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ascomIpdectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1))
ascomIpdectMIB.setRevisions(('1917-06-27 00:00', '1917-02-15 00:00', '1914-01-17 00:00', '1913-10-07 00:00', '1913-10-04 00:00', '1913-05-14 00:00', '1913-05-07 00:00', '1913-04-22 00:00', '1912-09-11 00:00', '1912-08-31 00:00', '1910-11-23 00:00', '1910-06-17 00:00', '1908-09-25 00:00', '1907-12-01 00:00', '1907-12-01 00:00',))
if mibBuilder.loadTexts: ascomIpdectMIB.setLastUpdated('1310070000Z')
if mibBuilder.loadTexts: ascomIpdectMIB.setOrganization('Ascom Sweden AB')
ascom = MibIdentifier((1, 3, 6, 1, 4, 1, 27614))
ascomTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 27614, 0))
ascomMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 27614, 1))
ascomIpdect = MibIdentifier((1, 3, 6, 1, 4, 1, 27614, 1, 1))
ipDectAttr = MibIdentifier((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1))
ipDectFaults = MibIdentifier((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2))
ipDectFaultLogEntries = MibScalar((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultLogEntries.setStatus('current')
ipDectAlarmLogEntries = MibScalar((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmLogEntries.setStatus('current')
ipDectLastErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectLastErrorCode.setStatus('current')
ipDectFaultLogTable = MibTable((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: ipDectFaultLogTable.setStatus('current')
ipDectFaultLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "ASCOM-IPDECT-MIB", "ipDectFaultIndex"))
if mibBuilder.loadTexts: ipDectFaultLogEntry.setStatus('current')
ipDectFaultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultIndex.setStatus('current')
ipDectFaultDate = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultDate.setStatus('current')
ipDectFaultTime = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultTime.setStatus('current')
ipDectFaultActivity = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("alarm", 0), ("alarmCleared", 1), ("alarmTimeout", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultActivity.setStatus('current')
ipDectFaultCode = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(65537, 65538, 65539, 196609, 196865, 197121, 197122, 197123, 197124, 197125, 197126, 197127, 197128, 197136, 197377, 197378, 197379, 197380, 197633, 327681, 327682, 327683, 327684, 327685, 327686, 327688, 327689, 393217, 393218, 393219, 393220, 393221, 393222, 458753, 458755, 458756, 458757, 458758, 458759, 458763, 524289, 524290, 720897, 786698, 786954, 786708, 786964, 786709, 786965, 786710, 786966, 786718, 786974, 786728, 786984, 786729, 786985, 786730, 786986, 786731, 786987, 786732, 786988, 786733, 786989, 786734, 786990, 786735, 786991, 786736, 786992, 786737, 786993, 786738, 786994, 786739, 786995, 786748, 787004, 786758, 787014, 786759, 787015, 786768, 787024, 786778, 787034, 786788, 787044, 787459, 787462, 787463, 790528, 790529, 917505, 917506, 917507, 917508, 917509, 917510, 917512, 917513, 917514, 983041, 983042, 983044, 983048, 983056, 1048577, 1048578, 1048580, 1048584, 1114112, 1114113, 1114114, 1114137, 1114138, 1114139, 1114177, 1114182, 1114183, 1114185, 1114192, 1114193, 1114195, 1114202, 1114203, 1114204, 1114205, 1114206, 1114207, 1179649, 1310721, 1310821, 1310822, 1310823, 1376257, 1638401, 1638402, 1703937, 1704192, 2097152, 2162689, 2162690, 2162691, 2162692, 2162693, 2162694))).clone(namedValues=NamedValues(("gwInterfaceDown", 65537), ("gwRegDown", 65538), ("gwProtocolError", 65539), ("usersTheLdapReplicatorIsNotConnected", 196609), ("radioCpuResourcesAreNotAvailable", 196865), ("masterStandbyActive", 197121), ("masterUserRegDown", 197122), ("masterEmergencyRegDown", 197123), ("masterRadioRegDown", 197124), ("masterPrimaryOrRedundantTrunkIsDown", 197125), ("masterActive", 197126), ("masterInactive", 197127), ("masterLimitStaticRadiosReached", 197128), ("masterAbnormalCallRelease", 197136), ("mobmInboundMobmRegDown", 197377), ("mobmOutboundMobmRegDown", 197378), ("mobmMasterRegDown", 197379), ("mobmStandbyActive", 197380), ("cmInboundMobmRegDown", 197633), ("rtpNoMediaDataReceived", 327681), ("rtpExcessiveLossOfData", 327682), ("rtpWrongPayloadTypeReceived", 327683), ("rtpStunFailure", 327684), ("rtpSrtpAuthFailure", 327685), ("rtpSrtcpAuthFailure", 327686), ("rtpIceFailure", 327688), ("rtpSrtpAuthFailure", 327689), ("h323UnexpectedMessageReceived", 393217), ("h323StatusEnquiry", 393218), ("h323SignalingTCPFailed", 393219), ("h323SignalingTimeout", 393220), ("h323SrtpKeyMismatch", 393221), ("h323MediaIncompatible", 393222), ("sipNatDiscoverFailure", 458753), ("sipOverloadDetected", 458755), ("sipCoderSelectionFailure", 458756), ("sipMediaConfigFailure", 458757), ("sipDnsFailed", 458758), ("sipIntMediaNegotiationFailed", 458759), ("sipDnsFailed", 458763), ("webmInvalidUrl", 524289), ("webmCoderMissingInUrl", 524290), ("cmdRestart", 720897), ("tlsUnexpectedMessage", 786698), ("tlsUnexpectedMessage", 786954), ("tlsBadMac", 786708), ("tlsBadMac", 786964), ("tlsDecryptionFailed", 786709), ("tlsDecryptionFailed", 786965), ("tlsRecordOverflow", 786710), ("tlsRecordOverflow", 786966), ("tlsDecompressionFailure", 786718), ("tlsDecompressionFailure", 786974), ("tlsHandshakeFailure", 786728), ("tlsHandshakeFailure", 786984), ("tlsNoCertificate", 786729), ("tlsNoCertificate", 786985), ("tlsBadCertificate", 786730), ("tlsBadCertificate", 786986), ("tlsUnsupportedCertificate", 786731), ("tlsUnsupportedCertificate", 786987), ("tlsRevocedCertificate", 786732), ("tlsRevocedCertificate", 786988), ("tlsExpiredCertificate", 786733), ("tlsExpiredCertificate", 786989), ("tlsUnknownCertificate", 786734), ("tlsUnknownCertificate", 786990), ("tlsIllegalParameter", 786735), ("tlsIllegalParameter", 786991), ("tlsUnknownCA", 786736), ("tlsUnknownCA", 786992), ("tlsAccessDenied", 786737), ("tlsAccessDenied", 786993), ("tlsDecodeError", 786738), ("tlsDecodeError", 786994), ("tlsDecryptionError", 786739), ("tlsDecryptionError", 786995), ("tlsExportRestriction", 786748), ("tlsExportRestriction", 787004), ("tlsProtocolVersion", 786758), ("tlsProtocolVersion", 787014), ("tlsInsufficientSecurity", 786759), ("tlsInsufficientSecurity", 787015), ("tlsInternalError", 786768), ("tlsInternalError", 787024), ("tlsUserCancelled", 786778), ("tlsUserCancelled", 787034), ("tlsNoRenegotiation", 786788), ("tlsNoRenegotiation", 787044), ("kerberosServiceNotFound", 787459), ("kerberosServerUnreachable", 787462), ("kerberosCrossRealmFailure", 787463), ("x509SystemTimeNotSet", 790528), ("x509CertificateNearExpiration", 790529), ("rfpDisconnected", 917505), ("rfpMalfunctioning", 917506), ("rfpDisabled", 917507), ("rfpSwDlFailed", 917508), ("rfpUnsynchronized", 917509), ("rfpAlienSyncLost", 917510), ("rfpDetectedSysidCollision", 917512), ("rfpSyncMasterFailedToResynchronizeToReference", 917513), ("rfpRestarted", 917514), ("envHighTemperature", 983041), ("envHighPowerConsumption", 983042), ("envSupplyVoltageLow", 983044), ("envSupplyVoltageHigh", 983048), ("envFanFailure", 983056), ("syncRingBroken", 1048577), ("syncRefSignalLost", 1048578), ("syncLost", 1048580), ("syncUnsynchronizedToReference", 1048584), ("ipInterfaceDown", 1114112), ("ipInterfaceNotConfigured", 1114113), ("ipDhcpServerNotResponding", 1114114), ("ipInvalidUdpRtpPortRange", 1114137), ("ipInvalidUdpNatPortRange", 1114138), ("ipInvalidNatPortRange", 1114139), ("ipArpPoisoningDetected", 1114177), ("ipOutOfTcpNatPorts", 1114182), ("ipOutOfTcpPorts", 1114183), ("ipTcpBindError", 1114185), ("ipOutOfUdpRtpPorts", 1114192), ("ipOutOfUdpPorts", 1114193), ("ipUdpBindError", 1114195), ("ipNoRouteToDestination", 1114202), ("ipNoRouteToDestinationIfDown", 1114203), ("ipNoRouteToDestinationIfUnknown", 1114204), ("ipNoRouteToDestinationIfNotConfigured", 1114205), ("ipNoRouteToDestinationNoGateway", 1114206), ("ipNoRouteToDestinationLoop", 1114207), ("boxMemoryLow", 1179649), ("rfpBusyForSpeech", 1310721), ("dectDefEncKeyTimeout", 1310821), ("dectCipherTimeout", 1310822), ("dectMasterConnectionTimeout", 1310823), ("sysBusyForSpeech", 1376257), ("provisioningDataCommunicationsError", 1638401), ("provisioningDataCommunicationsPutError", 1638402), ("uniteCommunicationFailure", 1703937), ("cuniteCommunicationFailure", 1704192), ("icpConnectionDown", 2097152), ("updateScriptGetFailed", 2162689), ("bootGetFailed", 2162690), ("firmwareGetFailed", 2162691), ("configGetFailed", 2162692), ("bmcGetFailed", 2162693), ("configPutFailed", 2162694)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultCode.setStatus('current')
ipDectFaultSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 99))).clone(namedValues=NamedValues(("indeterminate", 0), ("major", 1), ("critical", 2), ("none", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultSeverity.setStatus('current')
ipDectFaultSource = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultSource.setStatus('current')
ipDectFaultIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultIp.setStatus('current')
ipDectFaultDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectFaultDescription.setStatus('current')
ipDectActiveAlarmsTable = MibTable((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2), )
if mibBuilder.loadTexts: ipDectActiveAlarmsTable.setStatus('current')
ipDectActiveAlarmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1), ).setIndexNames((0, "ASCOM-IPDECT-MIB", "ipDectActiveAlarmsIndex"))
if mibBuilder.loadTexts: ipDectActiveAlarmsEntry.setStatus('current')
ipDectActiveAlarmsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectActiveAlarmsIndex.setStatus('current')
ipDectAlarmDate = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmDate.setStatus('current')
ipDectAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmTime.setStatus('current')
ipDectAlarmCode = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(65537, 65538, 65539, 196609, 196865, 197121, 197122, 197123, 197124, 197125, 197126, 197127, 197128, 197136, 197377, 197378, 197379, 197380, 197633, 327681, 327682, 327683, 327684, 327685, 327686, 327688, 327689, 393217, 393218, 393219, 393220, 393221, 393222, 458753, 458755, 458756, 458757, 458758, 458759, 458763, 524289, 524290, 720897, 786698, 786954, 786708, 786964, 786709, 786965, 786710, 786966, 786718, 786974, 786728, 786984, 786729, 786985, 786730, 786986, 786731, 786987, 786732, 786988, 786733, 786989, 786734, 786990, 786735, 786991, 786736, 786992, 786737, 786993, 786738, 786994, 786739, 786995, 786748, 787004, 786758, 787014, 786759, 787015, 786768, 787024, 786778, 787034, 786788, 787044, 787459, 787462, 787463, 790528, 790529, 917505, 917506, 917507, 917508, 917509, 917510, 917512, 917513, 917514, 983041, 983042, 983044, 983048, 983056, 1048577, 1048578, 1048580, 1048584, 1114112, 1114113, 1114114, 1114137, 1114138, 1114139, 1114177, 1114182, 1114183, 1114185, 1114192, 1114193, 1114195, 1114202, 1114203, 1114204, 1114205, 1114206, 1114207, 1179649, 1310721, 1310821, 1310822, 1310823, 1376257, 1638401, 1638402, 1703937, 1704192, 2097152, 2162689, 2162690, 2162691, 2162692, 2162693, 2162694))).clone(namedValues=NamedValues(("gwInterfaceDown", 65537), ("gwRegDown", 65538), ("gwProtocolError", 65539), ("usersTheLdapReplicatorIsNotConnected", 196609), ("radioCpuResourcesAreNotAvailable", 196865), ("masterStandbyActive", 197121), ("masterUserRegDown", 197122), ("masterEmergencyRegDown", 197123), ("masterRadioRegDown", 197124), ("masterPrimaryOrRedundantTrunkIsDown", 197125), ("masterActive", 197126), ("masterInactive", 197127), ("masterLimitStaticRadiosReached", 197128), ("masterAbnormalCallRelease", 197136), ("mobmInboundMobmRegDown", 197377), ("mobmOutboundMobmRegDown", 197378), ("mobmMasterRegDown", 197379), ("mobmStandbyActive", 197380), ("cmInboundMobmRegDown", 197633), ("rtpNoMediaDataReceived", 327681), ("rtpExcessiveLossOfData", 327682), ("rtpWrongPayloadTypeReceived", 327683), ("rtpStunFailure", 327684), ("rtpSrtpAuthFailure", 327685), ("rtpSrtcpAuthFailure", 327686), ("rtpIceFailure", 327688), ("rtpSrtpAuthFailure", 327689), ("h323UnexpectedMessageReceived", 393217), ("h323StatusEnquiry", 393218), ("h323SignalingTCPFailed", 393219), ("h323SignalingTimeout", 393220), ("h323SrtpKeyMismatch", 393221), ("h323MediaIncompatible", 393222), ("sipNatDiscoverFailure", 458753), ("sipOverloadDetected", 458755), ("sipCoderSelectionFailure", 458756), ("sipMediaConfigFailure", 458757), ("sipDnsFailed", 458758), ("sipIntMediaNegotiationFailed", 458759), ("sipDnsFailed", 458763), ("webmInvalidUrl", 524289), ("webmCoderMissingInUrl", 524290), ("cmdRestart", 720897), ("tlsUnexpectedMessage", 786698), ("tlsUnexpectedMessage", 786954), ("tlsBadMac", 786708), ("tlsBadMac", 786964), ("tlsDecryptionFailed", 786709), ("tlsDecryptionFailed", 786965), ("tlsRecordOverflow", 786710), ("tlsRecordOverflow", 786966), ("tlsDecompressionFailure", 786718), ("tlsDecompressionFailure", 786974), ("tlsHandshakeFailure", 786728), ("tlsHandshakeFailure", 786984), ("tlsNoCertificate", 786729), ("tlsNoCertificate", 786985), ("tlsBadCertificate", 786730), ("tlsBadCertificate", 786986), ("tlsUnsupportedCertificate", 786731), ("tlsUnsupportedCertificate", 786987), ("tlsRevocedCertificate", 786732), ("tlsRevocedCertificate", 786988), ("tlsExpiredCertificate", 786733), ("tlsExpiredCertificate", 786989), ("tlsUnknownCertificate", 786734), ("tlsUnknownCertificate", 786990), ("tlsIllegalParameter", 786735), ("tlsIllegalParameter", 786991), ("tlsUnknownCA", 786736), ("tlsUnknownCA", 786992), ("tlsAccessDenied", 786737), ("tlsAccessDenied", 786993), ("tlsDecodeError", 786738), ("tlsDecodeError", 786994), ("tlsDecryptionError", 786739), ("tlsDecryptionError", 786995), ("tlsExportRestriction", 786748), ("tlsExportRestriction", 787004), ("tlsProtocolVersion", 786758), ("tlsProtocolVersion", 787014), ("tlsInsufficientSecurity", 786759), ("tlsInsufficientSecurity", 787015), ("tlsInternalError", 786768), ("tlsInternalError", 787024), ("tlsUserCancelled", 786778), ("tlsUserCancelled", 787034), ("tlsNoRenegotiation", 786788), ("tlsNoRenegotiation", 787044), ("kerberosServiceNotFound", 787459), ("kerberosServerUnreachable", 787462), ("kerberosCrossRealmFailure", 787463), ("x509SystemTimeNotSet", 790528), ("x509CertificateNearExpiration", 790529), ("rfpDisconnected", 917505), ("rfpMalfunctioning", 917506), ("rfpDisabled", 917507), ("rfpSwDlFailed", 917508), ("rfpUnsynchronized", 917509), ("rfpAlienSyncLost", 917510), ("rfpDetectedSysidCollision", 917512), ("rfpSyncMasterFailedToResynchronizeToReference", 917513), ("rfpRestarted", 917514), ("envHighTemperature", 983041), ("envHighPowerConsumption", 983042), ("envSupplyVoltageLow", 983044), ("envSupplyVoltageHigh", 983048), ("envFanFailure", 983056), ("syncRingBroken", 1048577), ("syncRefSignalLost", 1048578), ("syncLost", 1048580), ("syncUnsynchronizedToReference", 1048584), ("ipInterfaceDown", 1114112), ("ipInterfaceNotConfigured", 1114113), ("ipDhcpServerNotResponding", 1114114), ("ipInvalidUdpRtpPortRange", 1114137), ("ipInvalidUdpNatPortRange", 1114138), ("ipInvalidNatPortRange", 1114139), ("ipArpPoisoningDetected", 1114177), ("ipOutOfTcpNatPorts", 1114182), ("ipOutOfTcpPorts", 1114183), ("ipTcpBindError", 1114185), ("ipOutOfUdpRtpPorts", 1114192), ("ipOutOfUdpPorts", 1114193), ("ipUdpBindError", 1114195), ("ipNoRouteToDestination", 1114202), ("ipNoRouteToDestinationIfDown", 1114203), ("ipNoRouteToDestinationIfUnknown", 1114204), ("ipNoRouteToDestinationIfNotConfigured", 1114205), ("ipNoRouteToDestinationNoGateway", 1114206), ("ipNoRouteToDestinationLoop", 1114207), ("boxMemoryLow", 1179649), ("rfpBusyForSpeech", 1310721), ("dectDefEncKeyTimeout", 1310821), ("dectCipherTimeout", 1310822), ("dectMasterConnectionTimeout", 1310823), ("sysBusyForSpeech", 1376257), ("provisioningDataCommunicationsError", 1638401), ("provisioningDataCommunicationsPutError", 1638402), ("uniteCommunicationFailure", 1703937), ("cuniteCommunicationFailure", 1704192), ("icpConnectionDown", 2097152), ("updateScriptGetFailed", 2162689), ("bootGetFailed", 2162690), ("firmwareGetFailed", 2162691), ("configGetFailed", 2162692), ("bmcGetFailed", 2162693), ("configPutFailed", 2162694)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmCode.setStatus('current')
ipDectAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("indeterminate", 0), ("major", 1), ("critical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmSeverity.setStatus('current')
ipDectAlarmSource = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmSource.setStatus('current')
ipDectAlarmIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmIp.setStatus('current')
ipDectAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDectAlarmDescription.setStatus('current')
ascomColdStart = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 0))
if mibBuilder.loadTexts: ascomColdStart.setStatus('current')
ascomWarmStart = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 1))
if mibBuilder.loadTexts: ascomWarmStart.setStatus('current')
ascomLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ascomLinkDown.setStatus('current')
ascomLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ascomLinkUp.setStatus('current')
ascomAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 4))
if mibBuilder.loadTexts: ascomAuthenticationFailure.setStatus('current')
ipDectSetCriticalAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 11)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectSetCriticalAlarmTrap.setStatus('current')
ipDectSetMajorAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 12)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectSetMajorAlarmTrap.setStatus('current')
ipDectSetMinorAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 13)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectSetMinorAlarmTrap.setStatus('current')
ipDectSetIndeterminateAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 14)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectSetIndeterminateAlarmTrap.setStatus('current')
ipDectClearAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 15)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectClearAlarmTrap.setStatus('current')
ipDectCriticalFaultTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 16)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectCriticalFaultTrap.setStatus('current')
ipDectMajorFaultTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 17)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectMajorFaultTrap.setStatus('current')
ipDectMinorFaultTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 18)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectMinorFaultTrap.setStatus('current')
ipDectIndeterminateFaultTrap = NotificationType((1, 3, 6, 1, 4, 1, 27614, 0, 19)).setObjects(("ASCOM-IPDECT-MIB", "ipDectLastErrorCode"))
if mibBuilder.loadTexts: ipDectIndeterminateFaultTrap.setStatus('current')
mibBuilder.exportSymbols("ASCOM-IPDECT-MIB", ipDectFaultSource=ipDectFaultSource, PYSNMP_MODULE_ID=ascomIpdectMIB, ascomWarmStart=ascomWarmStart, ipDectActiveAlarmsTable=ipDectActiveAlarmsTable, ipDectFaultIp=ipDectFaultIp, ipDectActiveAlarmsEntry=ipDectActiveAlarmsEntry, ipDectFaultSeverity=ipDectFaultSeverity, ipDectClearAlarmTrap=ipDectClearAlarmTrap, ipDectAlarmDescription=ipDectAlarmDescription, ipDectAlarmSource=ipDectAlarmSource, ipDectMinorFaultTrap=ipDectMinorFaultTrap, ipDectFaults=ipDectFaults, ipDectFaultLogTable=ipDectFaultLogTable, ipDectSetIndeterminateAlarmTrap=ipDectSetIndeterminateAlarmTrap, ascomMibs=ascomMibs, ipDectAlarmCode=ipDectAlarmCode, ascomLinkUp=ascomLinkUp, ipDectFaultActivity=ipDectFaultActivity, ipDectAlarmSeverity=ipDectAlarmSeverity, ipDectFaultDescription=ipDectFaultDescription, ipDectAlarmIp=ipDectAlarmIp, ascomTraps=ascomTraps, ipDectFaultIndex=ipDectFaultIndex, ascomAuthenticationFailure=ascomAuthenticationFailure, ascomIpdectMIB=ascomIpdectMIB, ipDectAlarmTime=ipDectAlarmTime, ipDectLastErrorCode=ipDectLastErrorCode, ipDectSetMajorAlarmTrap=ipDectSetMajorAlarmTrap, ipDectFaultTime=ipDectFaultTime, ipDectMajorFaultTrap=ipDectMajorFaultTrap, ascom=ascom, ipDectCriticalFaultTrap=ipDectCriticalFaultTrap, ipDectAttr=ipDectAttr, ipDectAlarmDate=ipDectAlarmDate, ipDectActiveAlarmsIndex=ipDectActiveAlarmsIndex, ascomIpdect=ascomIpdect, ipDectFaultLogEntries=ipDectFaultLogEntries, ascomLinkDown=ascomLinkDown, ipDectFaultLogEntry=ipDectFaultLogEntry, ascomColdStart=ascomColdStart, ipDectSetMinorAlarmTrap=ipDectSetMinorAlarmTrap, ipDectAlarmLogEntries=ipDectAlarmLogEntries, ipDectIndeterminateFaultTrap=ipDectIndeterminateFaultTrap, ipDectFaultDate=ipDectFaultDate, ipDectFaultCode=ipDectFaultCode, ipDectSetCriticalAlarmTrap=ipDectSetCriticalAlarmTrap)
