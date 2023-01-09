#
# PySNMP MIB module MIMOSA-NETWORKS-BFIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-NETWORKS-BFIVE-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:14 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mimosaWireless, mimosaConformanceGroup = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosaWireless", "mimosaConformanceGroup")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, ObjectIdentity, IpAddress, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ModuleIdentity, Counter32, Counter64, MibIdentifier, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "IpAddress", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter32", "Counter64", "MibIdentifier", "Integer32", "Gauge32")
TruthValue, MacAddress, DisplayString, TextualConvention, RowStatus, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention", "RowStatus", "PhysAddress")
mimosaB5Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356, 2, 4, 1))
mimosaB5Module.setRevisions(('2017-04-28 00:00',))
if mibBuilder.loadTexts: mimosaB5Module.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: mimosaB5Module.setOrganization('Mimosa Networks www.mimosa.co')
mimosaGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1))
mimosaLocInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2))
mimosaWanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3))
mimosaTdmaInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4))
mimosaMgmtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5))
mimosaRfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6))
mimosaPerfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7))
mimosaServices = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8))
class DecimalOne(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class DecimalTwo(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class DecimalFive(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-5'

mimosaDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaDeviceName.setStatus('current')
mimosaSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSerialNumber.setStatus('current')
mimosaFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaFirmwareVersion.setStatus('current')
mimosaFirmwareBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaFirmwareBuildDate.setStatus('current')
mimosaLastRebootTime = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLastRebootTime.setStatus('current')
mimosaUnlockCode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaUnlockCode.setStatus('current')
mimosaLEDBrightness = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("low", 2), ("medium", 3), ("high", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLEDBrightness.setStatus('current')
mimosaInternalTemp = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 8), DecimalOne()).setUnits('C').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaInternalTemp.setStatus('current')
mimosaRegulatoryDomain = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRegulatoryDomain.setStatus('current')
mimosaLongitude = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 1), DecimalFive()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLongitude.setStatus('current')
mimosaLatitude = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 2), DecimalFive()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLatitude.setStatus('current')
mimosaAltitude = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 3), Integer32()).setUnits('meters').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaAltitude.setStatus('current')
mimosaSatelliteSNR = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 4), DecimalOne()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSatelliteSNR.setStatus('current')
mimosaSatelliteStrength = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("bad", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSatelliteStrength.setStatus('current')
mimosaGPSSatellites = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaGPSSatellites.setStatus('current')
mimosaGlonassSatellites = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaGlonassSatellites.setStatus('current')
mimosaClockAccuracy = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 8), DecimalTwo()).setUnits('PPB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaClockAccuracy.setStatus('current')
mimosaWirelessMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accessPoint", 1), ("station", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWirelessMode.setStatus('current')
mimosaWirelessProtocol = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tdma", 1), ("csma", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWirelessProtocol.setStatus('current')
mimosaTDMAMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("a", 1), ("b", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTDMAMode.setStatus('current')
mimosaTDMAWindow = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 4), Integer32()).setUnits('ms').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTDMAWindow.setStatus('current')
mimosaTrafficSplit = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("symmetric", 1), ("asymmetric", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTrafficSplit.setStatus('current')
mimosaChainTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1), )
if mibBuilder.loadTexts: mimosaChainTable.setStatus('current')
mimosaChainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaChain"))
if mibBuilder.loadTexts: mimosaChainEntry.setStatus('current')
mimosaChain = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mimosaChain.setStatus('current')
mimosaTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 2), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxPower.setStatus('current')
mimosaRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 3), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxPower.setStatus('current')
mimosaRxNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 4), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxNoise.setStatus('current')
mimosaSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 5), DecimalOne()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSNR.setStatus('current')
mimosaCenterFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 6), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaCenterFreq.setStatus('current')
mimosaPolarization = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("horizontal", 1), ("vertical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPolarization.setStatus('current')
mimosaStreamTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2), )
if mibBuilder.loadTexts: mimosaStreamTable.setStatus('current')
mimosaStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaStream"))
if mibBuilder.loadTexts: mimosaStreamEntry.setStatus('current')
mimosaStream = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mimosaStream.setStatus('current')
mimosaTxPhy = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 2), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxPhy.setStatus('current')
mimosaTxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxMCS.setStatus('current')
mimosaTxWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 4), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxWidth.setStatus('current')
mimosaRxPhy = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 5), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxPhy.setStatus('current')
mimosaRxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxMCS.setStatus('current')
mimosaRxWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 7), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxWidth.setStatus('current')
mimosaRxEVM = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 8), DecimalOne()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxEVM.setStatus('current')
mimosaChannelTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3), )
if mibBuilder.loadTexts: mimosaChannelTable.setStatus('current')
mimosaChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaChannel"))
if mibBuilder.loadTexts: mimosaChannelEntry.setStatus('current')
mimosaChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mimosaChannel.setStatus('current')
mimosaChannelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("transmit", 1), ("receive", 2), ("bidirectional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelMode.setStatus('current')
mimosaChannelWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 3), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelWidth.setStatus('current')
mimosaChannelTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 4), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelTxPower.setStatus('current')
mimosaChannelCenterFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 5), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelCenterFreq.setStatus('current')
mimosaAntennaGain = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 4), Integer32()).setUnits('dBi').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaAntennaGain.setStatus('current')
mimosaTotalTxPower = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 5), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTotalTxPower.setStatus('current')
mimosaTotalRxPower = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 6), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTotalRxPower.setStatus('current')
mimosaTargetSignalStrength = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 7), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTargetSignalStrength.setStatus('current')
mimosaWanSsid = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanSsid.setStatus('current')
mimosaWanMac = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanMac.setStatus('current')
mimosaWanStatus = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("disconnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanStatus.setStatus('current')
mimosaWanUpTime = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanUpTime.setStatus('current')
mimosaPhyTxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 1), DecimalTwo()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPhyTxRate.setStatus('current')
mimosaPhyRxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 2), DecimalTwo()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPhyRxRate.setStatus('current')
mimosaPerTxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 3), DecimalTwo()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPerTxRate.setStatus('current')
mimosaPerRxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 4), DecimalTwo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPerRxRate.setStatus('current')
mimosaNetworkMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNetworkMode.setStatus('current')
mimosaRecoverySsid = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRecoverySsid.setStatus('current')
mimosaLocalSsid = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalSsid.setStatus('current')
mimosaLocalChannel = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalChannel.setStatus('current')
mimosaConsoleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 5), Integer32()).setUnits('min').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaConsoleTimeout.setStatus('current')
mimosaMaxClients = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaMaxClients.setStatus('current')
mimosaLocalMac = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalMac.setStatus('current')
mimosaLocalIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalIpAddr.setStatus('current')
mimosaLocalNetMask = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalNetMask.setStatus('current')
mimosaLocalGateway = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalGateway.setStatus('current')
mimosaFlowControl = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaFlowControl.setStatus('current')
mimosaHttpsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaHttpsEnabled.setStatus('current')
mimosaMgmtVlanEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaMgmtVlanEnabled.setStatus('current')
mimosaMgmtCloudEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaMgmtCloudEnabled.setStatus('current')
mimosaRestMgmtEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRestMgmtEnabled.setStatus('current')
mimosaPingWatchdogEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPingWatchdogEnabled.setStatus('current')
mimosaSyslogEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSyslogEnabled.setStatus('current')
mimosaNtpMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("custom", 1), ("standard", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNtpMode.setStatus('current')
mimosaNtpServer = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNtpServer.setStatus('current')
mibBuilder.exportSymbols("MIMOSA-NETWORKS-BFIVE-MIB", mimosaClockAccuracy=mimosaClockAccuracy, mimosaAltitude=mimosaAltitude, mimosaRestMgmtEnabled=mimosaRestMgmtEnabled, mimosaRecoverySsid=mimosaRecoverySsid, mimosaWirelessMode=mimosaWirelessMode, mimosaGeneral=mimosaGeneral, mimosaStream=mimosaStream, mimosaTotalTxPower=mimosaTotalTxPower, mimosaTargetSignalStrength=mimosaTargetSignalStrength, mimosaRfInfo=mimosaRfInfo, mimosaWanUpTime=mimosaWanUpTime, mimosaPerRxRate=mimosaPerRxRate, mimosaHttpsEnabled=mimosaHttpsEnabled, mimosaB5Module=mimosaB5Module, mimosaChannelMode=mimosaChannelMode, mimosaWanStatus=mimosaWanStatus, mimosaConsoleTimeout=mimosaConsoleTimeout, mimosaTxMCS=mimosaTxMCS, mimosaChain=mimosaChain, DecimalOne=DecimalOne, mimosaCenterFreq=mimosaCenterFreq, mimosaLocalChannel=mimosaLocalChannel, mimosaRegulatoryDomain=mimosaRegulatoryDomain, mimosaMgmtCloudEnabled=mimosaMgmtCloudEnabled, mimosaWanInfo=mimosaWanInfo, mimosaRxPhy=mimosaRxPhy, mimosaTxPhy=mimosaTxPhy, mimosaLocalGateway=mimosaLocalGateway, mimosaStreamTable=mimosaStreamTable, mimosaLocalSsid=mimosaLocalSsid, mimosaChannelCenterFreq=mimosaChannelCenterFreq, mimosaTDMAWindow=mimosaTDMAWindow, mimosaChainTable=mimosaChainTable, mimosaLatitude=mimosaLatitude, mimosaLongitude=mimosaLongitude, mimosaSerialNumber=mimosaSerialNumber, mimosaChannel=mimosaChannel, mimosaNtpServer=mimosaNtpServer, mimosaMgmtVlanEnabled=mimosaMgmtVlanEnabled, mimosaRxWidth=mimosaRxWidth, mimosaRxEVM=mimosaRxEVM, mimosaWanSsid=mimosaWanSsid, mimosaServices=mimosaServices, mimosaSatelliteStrength=mimosaSatelliteStrength, mimosaNetworkMode=mimosaNetworkMode, mimosaLocalIpAddr=mimosaLocalIpAddr, mimosaPerTxRate=mimosaPerTxRate, mimosaLEDBrightness=mimosaLEDBrightness, mimosaMgmtInfo=mimosaMgmtInfo, mimosaTxPower=mimosaTxPower, PYSNMP_MODULE_ID=mimosaB5Module, mimosaChannelTable=mimosaChannelTable, mimosaAntennaGain=mimosaAntennaGain, mimosaSyslogEnabled=mimosaSyslogEnabled, mimosaTdmaInfo=mimosaTdmaInfo, mimosaPhyRxRate=mimosaPhyRxRate, mimosaSatelliteSNR=mimosaSatelliteSNR, mimosaRxPower=mimosaRxPower, mimosaLocalMac=mimosaLocalMac, mimosaChannelTxPower=mimosaChannelTxPower, DecimalTwo=DecimalTwo, mimosaFlowControl=mimosaFlowControl, mimosaTotalRxPower=mimosaTotalRxPower, DecimalFive=DecimalFive, mimosaChainEntry=mimosaChainEntry, mimosaChannelWidth=mimosaChannelWidth, mimosaMaxClients=mimosaMaxClients, mimosaNtpMode=mimosaNtpMode, mimosaRxMCS=mimosaRxMCS, mimosaWirelessProtocol=mimosaWirelessProtocol, mimosaPolarization=mimosaPolarization, mimosaFirmwareBuildDate=mimosaFirmwareBuildDate, mimosaLocInfo=mimosaLocInfo, mimosaLocalNetMask=mimosaLocalNetMask, mimosaGlonassSatellites=mimosaGlonassSatellites, mimosaDeviceName=mimosaDeviceName, mimosaStreamEntry=mimosaStreamEntry, mimosaUnlockCode=mimosaUnlockCode, mimosaLastRebootTime=mimosaLastRebootTime, mimosaRxNoise=mimosaRxNoise, mimosaPerfInfo=mimosaPerfInfo, mimosaTDMAMode=mimosaTDMAMode, mimosaFirmwareVersion=mimosaFirmwareVersion, mimosaInternalTemp=mimosaInternalTemp, mimosaSNR=mimosaSNR, mimosaWanMac=mimosaWanMac, mimosaChannelEntry=mimosaChannelEntry, mimosaGPSSatellites=mimosaGPSSatellites, mimosaTxWidth=mimosaTxWidth, mimosaTrafficSplit=mimosaTrafficSplit, mimosaPhyTxRate=mimosaPhyTxRate, mimosaPingWatchdogEnabled=mimosaPingWatchdogEnabled)
