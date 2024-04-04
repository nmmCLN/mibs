#
# PySNMP MIB module CAMBIUM-PTP250-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cambium/CAMBIUM-PTP250-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:32 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, iso, Integer32, Counter64, Gauge32, enterprises, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "iso", "Integer32", "Counter64", "Gauge32", "enterprises", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cambium = ModuleIdentity((1, 3, 6, 1, 4, 1, 17713))
cambium.setRevisions(('2012-12-07 09:35', '2011-10-18 10:47',))
if mibBuilder.loadTexts: cambium.setLastUpdated('201212070935Z')
if mibBuilder.loadTexts: cambium.setOrganization('Cambium Networks')
ptp = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 1))
ptmp = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 2))
ptp250 = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250))
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 1))
ethernet = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 2))
licence = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 3))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 4))
phyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 5))
alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 6))
smtp = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 7))
snmpControl = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 8))
ntp = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 9))
versions = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 10))
pubStats = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 11))
ptpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 98))
ptpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 99))
ptpTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 250, 99, 0))
ptpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 17713, 250, 97)).setObjects(("CAMBIUM-PTP250-MIB", "configurationGroup"), ("CAMBIUM-PTP250-MIB", "ethernetGroup"), ("CAMBIUM-PTP250-MIB", "licenceGroup"), ("CAMBIUM-PTP250-MIB", "managementGroup"), ("CAMBIUM-PTP250-MIB", "phyStatusGroup"), ("CAMBIUM-PTP250-MIB", "alarmsGroup"), ("CAMBIUM-PTP250-MIB", "smtpGroup"), ("CAMBIUM-PTP250-MIB", "snmpControlGroup"), ("CAMBIUM-PTP250-MIB", "ntpGroup"), ("CAMBIUM-PTP250-MIB", "versionsGroup"), ("CAMBIUM-PTP250-MIB", "pubStatsGroup"), ("CAMBIUM-PTP250-MIB", "notificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpCompliance = ptpCompliance.setStatus('current')
configurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 5)).setObjects(("CAMBIUM-PTP250-MIB", "iPAddress"), ("CAMBIUM-PTP250-MIB", "subnetMask"), ("CAMBIUM-PTP250-MIB", "gatewayIPAddress"), ("CAMBIUM-PTP250-MIB", "masterSlaveMode"), ("CAMBIUM-PTP250-MIB", "maximumTransmitPower"), ("CAMBIUM-PTP250-MIB", "antennaGain"), ("CAMBIUM-PTP250-MIB", "cableLoss"), ("CAMBIUM-PTP250-MIB", "channelBandwidth"), ("CAMBIUM-PTP250-MIB", "remoteIPAddress"), ("CAMBIUM-PTP250-MIB", "remoteMACAddress"), ("CAMBIUM-PTP250-MIB", "linkName"), ("CAMBIUM-PTP250-MIB", "siteName"), ("CAMBIUM-PTP250-MIB", "band"), ("CAMBIUM-PTP250-MIB", "configuredModulationMode"), ("CAMBIUM-PTP250-MIB", "configuredRange"), ("CAMBIUM-PTP250-MIB", "channelSelection"), ("CAMBIUM-PTP250-MIB", "vlanTagging"), ("CAMBIUM-PTP250-MIB", "vlanId"), ("CAMBIUM-PTP250-MIB", "vlanPriority"), ("CAMBIUM-PTP250-MIB", "fixedModMode"), ("CAMBIUM-PTP250-MIB", "dualPayload"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configurationGroup = configurationGroup.setStatus('current')
ethernetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 6)).setObjects(("CAMBIUM-PTP250-MIB", "dataPortAutoNegotiation"), ("CAMBIUM-PTP250-MIB", "dataPortAutoNegAdvertisement"), ("CAMBIUM-PTP250-MIB", "dataPortStatus"), ("CAMBIUM-PTP250-MIB", "dataPortSpeedAndDuplex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ethernetGroup = ethernetGroup.setStatus('current')
licenceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 8)).setObjects(("CAMBIUM-PTP250-MIB", "regionCode"), ("CAMBIUM-PTP250-MIB", "productVariant"), ("CAMBIUM-PTP250-MIB", "productName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    licenceGroup = licenceGroup.setStatus('current')
managementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 9)).setObjects(("CAMBIUM-PTP250-MIB", "installArmState"), ("CAMBIUM-PTP250-MIB", "tFTPServerIPAddress"), ("CAMBIUM-PTP250-MIB", "tFTPServerPortNumber"), ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeFileName"), ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeStatus"), ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeStatusText"), ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeStatusAdditionalText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    managementGroup = managementGroup.setStatus('current')
phyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 12)).setObjects(("CAMBIUM-PTP250-MIB", "receivePower"), ("CAMBIUM-PTP250-MIB", "vectorError"), ("CAMBIUM-PTP250-MIB", "transmitPower"), ("CAMBIUM-PTP250-MIB", "linkLoss"), ("CAMBIUM-PTP250-MIB", "currentChannel"), ("CAMBIUM-PTP250-MIB", "extendedChannel"), ("CAMBIUM-PTP250-MIB", "receiveModulationMode"), ("CAMBIUM-PTP250-MIB", "transmitModulationMode"), ("CAMBIUM-PTP250-MIB", "currentFreqMHz"), ("CAMBIUM-PTP250-MIB", "extendedFreqMHz"), ("CAMBIUM-PTP250-MIB", "signalStrengthRatio"), ("CAMBIUM-PTP250-MIB", "searchState"), ("CAMBIUM-PTP250-MIB", "noiseFloor"), ("CAMBIUM-PTP250-MIB", "radarDetectChannel"), ("CAMBIUM-PTP250-MIB", "measuredRange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    phyStatusGroup = phyStatusGroup.setStatus('current')
alarmsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 13)).setObjects(("CAMBIUM-PTP250-MIB", "noWirelessChannelAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmsGroup = alarmsGroup.setStatus('current')
smtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 15)).setObjects(("CAMBIUM-PTP250-MIB", "sMTPServerIPAddress"), ("CAMBIUM-PTP250-MIB", "sMTPServerPortNumber"), ("CAMBIUM-PTP250-MIB", "sMTPSourceEmailAddress"), ("CAMBIUM-PTP250-MIB", "sMTPDestinationEmailAddress"), ("CAMBIUM-PTP250-MIB", "sMTPEnabledMessages"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smtpGroup = smtpGroup.setStatus('current')
snmpControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 16)).setObjects(("CAMBIUM-PTP250-MIB", "sNMPCommunityTableNumber"), ("CAMBIUM-PTP250-MIB", "sNMPTrapTableNumber"), ("CAMBIUM-PTP250-MIB", "sNMPEnabledTraps"), ("CAMBIUM-PTP250-MIB", "sNMPTrapIPAddress"), ("CAMBIUM-PTP250-MIB", "sNMPTrapPortNumber"), ("CAMBIUM-PTP250-MIB", "sNMPCommunityString"), ("CAMBIUM-PTP250-MIB", "sNMPCommunityAccess"), ("CAMBIUM-PTP250-MIB", "sNMPCommunityOid"), ("CAMBIUM-PTP250-MIB", "sNMPTrapCommunity"), ("CAMBIUM-PTP250-MIB", "sNMPTrapVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpControlGroup = snmpControlGroup.setStatus('current')
ntpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 17)).setObjects(("CAMBIUM-PTP250-MIB", "nTPState"), ("CAMBIUM-PTP250-MIB", "nTPPollInterval"), ("CAMBIUM-PTP250-MIB", "nTPSync"), ("CAMBIUM-PTP250-MIB", "nTPLastSync"), ("CAMBIUM-PTP250-MIB", "systemClock"), ("CAMBIUM-PTP250-MIB", "timeZone"), ("CAMBIUM-PTP250-MIB", "nTPServerIp"), ("CAMBIUM-PTP250-MIB", "nTPServerPortNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpGroup = ntpGroup.setStatus('current')
versionsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 19)).setObjects(("CAMBIUM-PTP250-MIB", "softwareVersion"), ("CAMBIUM-PTP250-MIB", "hardwareVersion"), ("CAMBIUM-PTP250-MIB", "bootVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    versionsGroup = versionsGroup.setStatus('current')
pubStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 20)).setObjects(("CAMBIUM-PTP250-MIB", "receiveDataRate"), ("CAMBIUM-PTP250-MIB", "transmitDataRate"), ("CAMBIUM-PTP250-MIB", "aggregateDataRate"), ("CAMBIUM-PTP250-MIB", "wirelessLinkStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pubStatsGroup = pubStatsGroup.setStatus('current')
notificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 17713, 250, 98, 99)).setObjects(("CAMBIUM-PTP250-MIB", "dataPortStatusTrap"), ("CAMBIUM-PTP250-MIB", "installArmStateTrap"), ("CAMBIUM-PTP250-MIB", "noWirelessChannelAvailableTrap"), ("CAMBIUM-PTP250-MIB", "linkStatusTrap"), ("CAMBIUM-PTP250-MIB", "radarDetectTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationsGroup = notificationsGroup.setStatus('current')
sNMPCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 250, 8, 2), )
if mibBuilder.loadTexts: sNMPCommunityTable.setStatus('current')
sNMPCommunityTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1), ).setIndexNames((0, "CAMBIUM-PTP250-MIB", "sNMPCommunityTableIndex"))
if mibBuilder.loadTexts: sNMPCommunityTableEntry.setStatus('current')
sNMPTrapTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 250, 8, 4), )
if mibBuilder.loadTexts: sNMPTrapTable.setStatus('current')
sNMPTrapTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1), ).setIndexNames((0, "CAMBIUM-PTP250-MIB", "sNMPTrapTableIndex"))
if mibBuilder.loadTexts: sNMPTrapTableEntry.setStatus('current')
iPAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iPAddress.setStatus('current')
subnetMask = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subnetMask.setStatus('current')
gatewayIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gatewayIPAddress.setStatus('current')
remoteMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteMACAddress.setStatus('current')
masterSlaveMode = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("slave", 0), ("master", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: masterSlaveMode.setStatus('current')
maximumTransmitPower = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-15, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumTransmitPower.setStatus('current')
antennaGain = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 610))).setMaxAccess("readonly")
if mibBuilder.loadTexts: antennaGain.setStatus('current')
cableLoss = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cableLoss.setStatus('current')
channelBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("bw20MHz", 0), ("bw40MHz", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelBandwidth.setStatus('current')
remoteIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteIPAddress.setStatus('current')
linkName = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkName.setStatus('current')
siteName = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: siteName.setStatus('current')
configuredModulationMode = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("modBpskHalf", 0), ("modQpskHalf", 1), ("modQpskThreeQuarters", 2), ("mod16QamHalf", 3), ("mod16QamThreeQuarters", 4), ("mod64QamTwoThirds", 5), ("mod64QamThreeQuarters", 6), ("mod64QamFiveSixths", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configuredModulationMode.setStatus('current')
band = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unset", 0), ("freq5400MHz", 1), ("freq5800MHz", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: band.setStatus('current')
configuredRange = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configuredRange.setStatus('current')
channelSelection = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 16), Bits().clone(namedValues=NamedValues(("channum100", 0), ("channum104", 1), ("channum108", 2), ("channum112", 3), ("channum116", 4), ("channum120", 5), ("channum124", 6), ("channum128", 7), ("channum132", 8), ("channum136", 9), ("channum140", 10), ("channum149", 11), ("channum153", 12), ("channum157", 13), ("channum161", 14), ("channum165", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelSelection.setStatus('current')
vlanTagging = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTagging.setStatus('current')
vlanId = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanId.setStatus('current')
vlanPriority = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPriority.setStatus('current')
fixedModMode = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fixedModMode.setStatus('current')
dualPayload = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dualPayload.setStatus('current')
dataPortAutoNegotiation = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataPortAutoNegotiation.setStatus('current')
dataPortAutoNegAdvertisement = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 2, 2), Bits().clone(namedValues=NamedValues(("negInvalid", 0), ("neg10MbpsHalfDuplex", 1), ("neg10MbpsFullDuplex", 2), ("neg100MbpsHalfDuplex", 3), ("neg100MbpsFullDuplex", 4), ("neg1000MbpsFullDuplex", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataPortAutoNegAdvertisement.setStatus('current')
dataPortStatus = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataPortStatus.setStatus('current')
dataPortSpeedAndDuplex = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("speed1000MbpsFullDuplex", 0), ("speed100MbpsFullDuplex", 1), ("speed100MbpsHalfDuplex", 2), ("speed10MbpsFullDuplex", 3), ("speed10MbpsHalfDuplex", 4), ("speedUnknown6", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataPortSpeedAndDuplex.setStatus('current')
regionCode = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: regionCode.setStatus('current')
productVariant = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("ptpXX400Full", 0), ("ptpXX400Deprecated1", 1), ("ptpXX400Deprecated2", 2), ("ptpXX400Lite", 3), ("spare1", 4), ("ptpXX300", 5), ("spare2", 6), ("spare3", 7), ("ptpXX500FullDeprecated", 8), ("ptpXX500LiteDeprecated", 9), ("ptpXX500", 10), ("ptpXX600Lite", 11), ("ptpXX600Full", 12), ("spare5", 13), ("spare6", 14), ("ptp800", 15), ("ptp250", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productVariant.setStatus('current')
productName = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
installArmState = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disarmed", 0), ("armed", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: installArmState.setStatus('current')
tFTPServerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 4, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tFTPServerIPAddress.setStatus('current')
tFTPServerPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tFTPServerPortNumber.setStatus('current')
tFTPSoftwareUpgradeFileName = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 4, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tFTPSoftwareUpgradeFileName.setStatus('current')
tFTPSoftwareUpgradeStatus = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 0), ("uploadinprogress", 1), ("uploadsuccessfulprogrammingFLASH", 2), ("upgradesuccessfulreboottorunthenewsoftwareimage", 3), ("upgradefailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tFTPSoftwareUpgradeStatus.setStatus('current')
tFTPSoftwareUpgradeStatusText = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 4, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tFTPSoftwareUpgradeStatusText.setStatus('current')
tFTPSoftwareUpgradeStatusAdditionalText = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 4, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tFTPSoftwareUpgradeStatusAdditionalText.setStatus('current')
receivePower = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receivePower.setStatus('current')
vectorError = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vectorError.setStatus('current')
transmitPower = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transmitPower.setStatus('current')
linkLoss = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-500, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkLoss.setStatus('current')
currentChannel = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentChannel.setStatus('current')
extendedChannel = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extendedChannel.setStatus('current')
receiveModulationMode = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("acquisition", 0), ("modBpskHalfSingle", 1), ("modQpskHalfSingle", 2), ("modQpskThreeQuartersSingle", 3), ("mod16QamHalfSingle", 4), ("mod16QamThreeQuartersSingle", 5), ("mod64QamTwoThirdsSingle", 6), ("mod64QamThreeQuartersSingle", 7), ("mod64QamFiveSixthsSingle", 8), ("modBpskHalfDual", 9), ("modQpskHalfDual", 10), ("modQpskThreeQuartersDual", 11), ("mod16QamHalfDual", 12), ("mod16QamThreeQuartersDual", 13), ("mod64QamTwoThirdsDual", 14), ("mod64QamThreeQuartersDual", 15), ("mod64QamFiveSixthsDual", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: receiveModulationMode.setStatus('current')
transmitModulationMode = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("acquisition", 0), ("modBpskHalfSingle", 1), ("modQpskHalfSingle", 2), ("modQpskThreeQuartersSingle", 3), ("mod16QamHalfSingle", 4), ("mod16QamThreeQuartersSingle", 5), ("mod64QamTwoThirdsSingle", 6), ("mod64QamThreeQuartersSingle", 7), ("mod64QamFiveSixthsSingle", 8), ("modBpskHalfDual", 9), ("modQpskHalfDual", 10), ("modQpskThreeQuartersDual", 11), ("mod16QamHalfDual", 12), ("mod16QamThreeQuartersDual", 13), ("mod64QamTwoThirdsDual", 14), ("mod64QamThreeQuartersDual", 15), ("mod64QamFiveSixthsDual", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transmitModulationMode.setStatus('current')
currentFreqMHz = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentFreqMHz.setStatus('current')
extendedFreqMHz = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extendedFreqMHz.setStatus('current')
signalStrengthRatio = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signalStrengthRatio.setStatus('current')
searchState = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("up", 0), ("registering", 1), ("acquiring", 2), ("searching", 3), ("radarCAC", 4), ("initialising", 5), ("noChannels", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: searchState.setStatus('current')
noiseFloor = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiseFloor.setStatus('current')
radarDetectChannel = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: radarDetectChannel.setStatus('current')
measuredRange = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 5, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: measuredRange.setStatus('current')
noWirelessChannelAvailable = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("noWirelessChannelAvailable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noWirelessChannelAvailable.setStatus('current')
sMTPServerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 7, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sMTPServerIPAddress.setStatus('current')
sMTPServerPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sMTPServerPortNumber.setStatus('current')
sMTPSourceEmailAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 7, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sMTPSourceEmailAddress.setStatus('current')
sMTPDestinationEmailAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sMTPDestinationEmailAddress.setStatus('current')
sMTPEnabledMessages = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 7, 5), Bits().clone(namedValues=NamedValues(("dataPortUpDown", 0), ("wirelessLinkUpDown", 1), ("coldStart", 2), ("radarDetect", 3), ("installArmState", 4), ("noChannelAvailable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sMTPEnabledMessages.setStatus('current')
sNMPCommunityTableNumber = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPCommunityTableNumber.setStatus('current')
sNMPTrapTableNumber = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPTrapTableNumber.setStatus('current')
sNMPEnabledTraps = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 8, 6), Bits().clone(namedValues=NamedValues(("dataPortUpDown", 0), ("wirelessLinkUpDown", 1), ("coldStart", 2), ("radarDetect", 3), ("installArmState", 4), ("noChannelAvailable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPEnabledTraps.setStatus('current')
sNMPCommunityTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: sNMPCommunityTableIndex.setStatus('current')
sNMPCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPCommunityString.setStatus('current')
sNMPCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("readOnly", 0), ("readWrite", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPCommunityAccess.setStatus('current')
sNMPCommunityOid = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPCommunityOid.setStatus('current')
sNMPTrapTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: sNMPTrapTableIndex.setStatus('current')
sNMPTrapIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPTrapIPAddress.setStatus('current')
sNMPTrapPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPTrapPortNumber.setStatus('current')
sNMPTrapCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPTrapCommunity.setStatus('current')
sNMPTrapVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("v1", 0), ("v2c", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNMPTrapVersion.setStatus('current')
nTPState = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nTPState.setStatus('current')
nTPPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 43200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nTPPollInterval.setStatus('current')
nTPSync = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noSync", 0), ("inSync", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nTPSync.setStatus('current')
nTPLastSync = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nTPLastSync.setStatus('current')
systemClock = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemClock.setStatus('current')
timeZone = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50))).clone(namedValues=NamedValues(("gmtMinus1200", 0), ("gmtMinus1130", 1), ("gmtMinus1100", 2), ("gmtMinus1030", 3), ("gmtMinus1000", 4), ("gmtMinus0930", 5), ("gmtMinus0900", 6), ("gmtMinus0830", 7), ("gmtMinus0800", 8), ("gmtMinus0730", 9), ("gmtMinus0700", 10), ("gmtMinus0630", 11), ("gmtMinus0600", 12), ("gmtMinus0530", 13), ("gmtMinus0500", 14), ("gmtMinus0430", 15), ("gmtMinus0400", 16), ("gmtMinus0330", 17), ("gmtMinus0300", 18), ("gmtMinus0230", 19), ("gmtMinus0200", 20), ("gmtMinus0130", 21), ("gmtMinus0100", 22), ("gmtMinus0030", 23), ("gmtZero", 24), ("gmtPlus0030", 25), ("gmtPlus0100", 26), ("gmtPlus0130", 27), ("gmtPlus0200", 28), ("gmtPlus0230", 29), ("gmtPlus0300", 30), ("gmtPlus0330", 31), ("gmtPlus0400", 32), ("gmtPlus0430", 33), ("gmtPlus0500", 34), ("gmtPlus0530", 35), ("gmtPlus0600", 36), ("gmtPlus0630", 37), ("gmtPlus0700", 38), ("gmtPlus0730", 39), ("gmtPlus0800", 40), ("gmtPlus0830", 41), ("gmtPlus0900", 42), ("gmtPlus0930", 43), ("gmtPlus1000", 44), ("gmtPlus1030", 45), ("gmtPlus1100", 46), ("gmtPlus1130", 47), ("gmtPlus1200", 48), ("gmtPlus1230", 49), ("gmtPlus1300", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeZone.setStatus('current')
nTPServerIp = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nTPServerIp.setStatus('current')
nTPServerPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 9, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nTPServerPortNumber.setStatus('current')
softwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareVersion.setStatus('current')
hardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 10, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareVersion.setStatus('current')
bootVersion = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 10, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootVersion.setStatus('current')
receiveDataRate = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receiveDataRate.setStatus('current')
transmitDataRate = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 11, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transmitDataRate.setStatus('current')
aggregateDataRate = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 11, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggregateDataRate.setStatus('current')
wirelessLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 17713, 250, 11, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessLinkStatus.setStatus('current')
dataPortStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 1)).setObjects(("CAMBIUM-PTP250-MIB", "dataPortStatus"))
if mibBuilder.loadTexts: dataPortStatusTrap.setStatus('current')
installArmStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 2)).setObjects(("CAMBIUM-PTP250-MIB", "installArmState"))
if mibBuilder.loadTexts: installArmStateTrap.setStatus('current')
noWirelessChannelAvailableTrap = NotificationType((1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 3)).setObjects(("CAMBIUM-PTP250-MIB", "noWirelessChannelAvailable"))
if mibBuilder.loadTexts: noWirelessChannelAvailableTrap.setStatus('current')
linkStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 4)).setObjects(("CAMBIUM-PTP250-MIB", "wirelessLinkStatus"))
if mibBuilder.loadTexts: linkStatusTrap.setStatus('current')
radarDetectTrap = NotificationType((1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 5)).setObjects(("CAMBIUM-PTP250-MIB", "radarDetectChannel"))
if mibBuilder.loadTexts: radarDetectTrap.setStatus('current')
mibBuilder.exportSymbols("CAMBIUM-PTP250-MIB", tFTPSoftwareUpgradeStatusText=tFTPSoftwareUpgradeStatusText, aggregateDataRate=aggregateDataRate, dataPortAutoNegotiation=dataPortAutoNegotiation, ntpGroup=ntpGroup, transmitModulationMode=transmitModulationMode, hardwareVersion=hardwareVersion, ptpCompliance=ptpCompliance, ptpGroups=ptpGroups, sMTPServerIPAddress=sMTPServerIPAddress, tFTPServerPortNumber=tFTPServerPortNumber, wirelessLinkStatus=wirelessLinkStatus, pubStatsGroup=pubStatsGroup, smtpGroup=smtpGroup, sNMPCommunityOid=sNMPCommunityOid, sMTPEnabledMessages=sMTPEnabledMessages, nTPLastSync=nTPLastSync, linkStatusTrap=linkStatusTrap, cableLoss=cableLoss, receiveDataRate=receiveDataRate, maximumTransmitPower=maximumTransmitPower, extendedFreqMHz=extendedFreqMHz, installArmState=installArmState, receivePower=receivePower, tFTPSoftwareUpgradeStatus=tFTPSoftwareUpgradeStatus, ptp250=ptp250, sNMPTrapVersion=sNMPTrapVersion, productVariant=productVariant, sNMPEnabledTraps=sNMPEnabledTraps, vectorError=vectorError, licence=licence, remoteIPAddress=remoteIPAddress, nTPState=nTPState, noWirelessChannelAvailableTrap=noWirelessChannelAvailableTrap, band=band, dataPortSpeedAndDuplex=dataPortSpeedAndDuplex, siteName=siteName, cambium=cambium, tFTPServerIPAddress=tFTPServerIPAddress, receiveModulationMode=receiveModulationMode, licenceGroup=licenceGroup, ptp=ptp, alarmsGroup=alarmsGroup, configuration=configuration, linkLoss=linkLoss, sNMPTrapCommunity=sNMPTrapCommunity, PYSNMP_MODULE_ID=cambium, ptpTrapPrefix=ptpTrapPrefix, sNMPCommunityTable=sNMPCommunityTable, dataPortStatus=dataPortStatus, installArmStateTrap=installArmStateTrap, configuredRange=configuredRange, sMTPDestinationEmailAddress=sMTPDestinationEmailAddress, currentChannel=currentChannel, nTPServerPortNumber=nTPServerPortNumber, sNMPTrapTableNumber=sNMPTrapTableNumber, sMTPSourceEmailAddress=sMTPSourceEmailAddress, phyStatus=phyStatus, sNMPCommunityAccess=sNMPCommunityAccess, vlanId=vlanId, ethernet=ethernet, dataPortStatusTrap=dataPortStatusTrap, productName=productName, tFTPSoftwareUpgradeFileName=tFTPSoftwareUpgradeFileName, versionsGroup=versionsGroup, channelBandwidth=channelBandwidth, fixedModMode=fixedModMode, ptpTraps=ptpTraps, noiseFloor=noiseFloor, timeZone=timeZone, antennaGain=antennaGain, configurationGroup=configurationGroup, sMTPServerPortNumber=sMTPServerPortNumber, masterSlaveMode=masterSlaveMode, measuredRange=measuredRange, snmpControlGroup=snmpControlGroup, currentFreqMHz=currentFreqMHz, ntp=ntp, alarms=alarms, pubStats=pubStats, sNMPTrapIPAddress=sNMPTrapIPAddress, vlanPriority=vlanPriority, searchState=searchState, nTPSync=nTPSync, nTPServerIp=nTPServerIp, softwareVersion=softwareVersion, dataPortAutoNegAdvertisement=dataPortAutoNegAdvertisement, gatewayIPAddress=gatewayIPAddress, radarDetectTrap=radarDetectTrap, extendedChannel=extendedChannel, sNMPTrapPortNumber=sNMPTrapPortNumber, sNMPCommunityTableNumber=sNMPCommunityTableNumber, subnetMask=subnetMask, bootVersion=bootVersion, phyStatusGroup=phyStatusGroup, sNMPTrapTableEntry=sNMPTrapTableEntry, channelSelection=channelSelection, transmitPower=transmitPower, sNMPTrapTable=sNMPTrapTable, noWirelessChannelAvailable=noWirelessChannelAvailable, vlanTagging=vlanTagging, ethernetGroup=ethernetGroup, linkName=linkName, versions=versions, notificationsGroup=notificationsGroup, configuredModulationMode=configuredModulationMode, smtp=smtp, transmitDataRate=transmitDataRate, sNMPCommunityString=sNMPCommunityString, management=management, snmpControl=snmpControl, managementGroup=managementGroup, regionCode=regionCode, iPAddress=iPAddress, tFTPSoftwareUpgradeStatusAdditionalText=tFTPSoftwareUpgradeStatusAdditionalText, sNMPTrapTableIndex=sNMPTrapTableIndex, radarDetectChannel=radarDetectChannel, dualPayload=dualPayload, sNMPCommunityTableEntry=sNMPCommunityTableEntry, remoteMACAddress=remoteMACAddress, systemClock=systemClock, nTPPollInterval=nTPPollInterval, ptmp=ptmp, sNMPCommunityTableIndex=sNMPCommunityTableIndex, signalStrengthRatio=signalStrengthRatio)
