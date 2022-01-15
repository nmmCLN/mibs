#
# PySNMP MIB module ICOTERA-I6400-SERIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/icotera/ICOTERA-I6400-SERIES-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:24:53 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, iso, NotificationType, Unsigned32, Counter32, Gauge32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, ObjectIdentity, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "iso", "NotificationType", "Unsigned32", "Counter32", "Gauge32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "ObjectIdentity", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
icotera = ModuleIdentity((1, 3, 6, 1, 4, 1, 29865))
icotera.setRevisions(('2017-03-01 16:46', '2017-02-09 14:27', '2017-01-16 10:32', '2016-08-26 09:24', '2016-08-24 09:04', '2015-04-01 13:57',))
if mibBuilder.loadTexts: icotera.setLastUpdated('201703011646Z')
if mibBuilder.loadTexts: icotera.setOrganization('Icotera A/S')
ictIGW1k = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11))
if mibBuilder.loadTexts: ictIGW1k.setStatus('current')
ictMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 11, 2))
ictServices = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 11, 3))
ictReset = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 11, 5))
ictMcastAnalyzer = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 11, 7))
ictServicesMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1))
if mibBuilder.loadTexts: ictServicesMibs.setStatus('current')
ictCatv = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1))
if mibBuilder.loadTexts: ictCatv.setStatus('current')
catvModuleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleAdminStatus.setStatus('current')
catvModuleFilter = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("pkg1", 1), ("pkg2", 2), ("pkg3", 3), ("pkg4", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleFilter.setStatus('current')
catvModuleRflevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("auto", 0), ("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleRflevel.setStatus('current')
catvModuleLowSignal = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleLowSignal.setStatus('current')
catvModuleSignalDetected = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleSignalDetected.setStatus('current')
catvModulePowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModulePowerLevel.setStatus('current')
ictTransceiver = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3))
if mibBuilder.loadTexts: ictTransceiver.setStatus('current')
transceiverDdmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverDdmTemperature.setStatus('current')
transceiverDdmTxPower = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverDdmTxPower.setStatus('current')
transceiverDdmRxPower = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverDdmRxPower.setStatus('current')
transceiverDdmVoltage = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverDdmVoltage.setStatus('current')
transceiverDdmTxBiasCurrent = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverDdmTxBiasCurrent.setStatus('current')
transceiverTransceiverType = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 0), ("gbic", 1), ("moduleSolderedToMotherboard", 2), ("sfp", 3), ("type300pinXbi", 4), ("xenpak", 5), ("xfp", 6), ("xff", 7), ("xfpE", 8), ("xPak", 9), ("x2", 10), ("dWdmSfp", 11), ("qSfp", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverTransceiverType.setStatus('current')
transceiverLaserWavelength = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverLaserWavelength.setStatus('current')
transceiverConnectorType = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 32, 33, 34))).clone(namedValues=NamedValues(("unknown", 0), ("sc", 1), ("fibreChannelStyle1CopperConnector", 2), ("fibreChannelStyle2CopperConnector", 3), ("bncTnc", 4), ("fibreChannelCoaxialHeaders", 5), ("fiberJack", 6), ("lc", 7), ("mtRj", 8), ("mu", 9), ("sg", 10), ("opticalPigtail", 11), ("mpoParallelOptic", 12), ("hssdcII", 32), ("copperPigtail", 33), ("rj45", 34)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverConnectorType.setStatus('current')
transceiverEthernetCompliance = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverEthernetCompliance.setStatus('current')
transceiverLinkLength = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverLinkLength.setStatus('current')
transceiverDiagCapable = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverDiagCapable.setStatus('current')
ictFacRst = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 5, 1))
if mibBuilder.loadTexts: ictFacRst.setStatus('current')
ictFacRstMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 5, 1, 1))
if mibBuilder.loadTexts: ictFacRstMib.setStatus('current')
performFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("noActionRequested", 0), ("makeFactoryreset", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: performFactoryReset.setStatus('current')
ictMgmtMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1))
if mibBuilder.loadTexts: ictMgmtMib.setStatus('current')
ictFwUpg = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1))
if mibBuilder.loadTexts: ictFwUpg.setStatus('current')
ictCfgUpdate = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2))
if mibBuilder.loadTexts: ictCfgUpdate.setStatus('current')
ictReboot = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 3))
if mibBuilder.loadTexts: ictReboot.setStatus('current')
upgUrl = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upgUrl.setStatus('current')
upgExecute = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notUpgrading", 0), ("startUpgrade", 1), ("validatingUpgrade-CheckErrorCodeIfFailed", 2), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upgExecute.setStatus('current')
upgStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upgStatus.setStatus('current')
cfgTftpPath = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgTftpPath.setStatus('current')
cfgExecute = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("notUpdating", 0), ("startUpdate", 1), ("inProgress", 2), ("someErrorOccured", 3), ("resultOK", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgExecute.setStatus('current')
cfgStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgStatus.setStatus('current')
performCpeReboot = MibScalar((1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("noActionRequested", 0), ("makeReboot", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: performCpeReboot.setStatus('current')
class IctTimeStamp(TextualConvention, Counter32):
    status = 'current'

class IctPortList(TextualConvention, OctetString):
    status = 'current'

class IctJitter(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class IctDelta(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

ictMcastAnalyzerCurrent = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1))
ictMcastAnalyzerHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2))
ictMcastAnalyzerCurrentList = MibTable((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1), )
if mibBuilder.loadTexts: ictMcastAnalyzerCurrentList.setStatus('current')
currentListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1, 1), ).setIndexNames((0, "ICOTERA-I6400-SERIES", "curGroupIndex"))
if mibBuilder.loadTexts: currentListEntry.setStatus('current')
curGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: curGroupIndex.setStatus('current')
curGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curGroupAddr.setStatus('current')
ictMcastAnalyzerCurrentMetrics = MibTable((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2), )
if mibBuilder.loadTexts: ictMcastAnalyzerCurrentMetrics.setStatus('current')
currentMetricsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1), ).setIndexNames((0, "ICOTERA-I6400-SERIES", "curMetrGroupAddr"))
if mibBuilder.loadTexts: currentMetricsEntry.setStatus('current')
curMetrGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrGroupAddr.setStatus('current')
curMetrSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrSourceAddr.setStatus('current')
curMetrDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrDstPort.setStatus('current')
curMetrSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrSrcPort.setStatus('current')
curMetrTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalBytes.setStatus('current')
curMetrTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalPackets.setStatus('current')
curMetrKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrKbps.setStatus('current')
curMetrPps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrPps.setStatus('current')
curMetrAvgKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrAvgKbps.setStatus('current')
curMetrAvgPps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrAvgPps.setStatus('current')
curMetrMaxDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 11), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrMaxDelta.setStatus('current')
curMetrAvgDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 12), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrAvgDelta.setStatus('current')
curMetrTotalMaxDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 13), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalMaxDelta.setStatus('current')
curMetrTotalAvgDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 14), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalAvgDelta.setStatus('current')
curMetrStartTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 15), IctTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrStartTimestamp.setStatus('current')
curMetrStopTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 16), IctTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrStopTimestamp.setStatus('current')
curMetrMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 17), IctPortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrMemberPorts.setStatus('current')
curMetrStreamType = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrStreamType.setStatus('current')
curMetrSkips = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrSkips.setStatus('current')
curMetrDiscontinuities = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrDiscontinuities.setStatus('current')
curMetrLost = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrLost.setStatus('current')
curMetrReordered = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrReordered.setStatus('current')
curMetrTotalSkips = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalSkips.setStatus('current')
curMetrTotalDiscontinuities = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalDiscontinuities.setStatus('current')
curMetrTotalLost = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalLost.setStatus('current')
curMetrTotalReordered = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrTotalReordered.setStatus('current')
curMetrAvgLostPps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 27), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrAvgLostPps.setStatus('current')
curMetrJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 28), IctJitter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curMetrJitter.setStatus('current')
ictMcastAnalyzerHistoryList = MibTable((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1), )
if mibBuilder.loadTexts: ictMcastAnalyzerHistoryList.setStatus('current')
historyListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1, 1), ).setIndexNames((0, "ICOTERA-I6400-SERIES", "histGroupIndex"))
if mibBuilder.loadTexts: historyListEntry.setStatus('current')
histGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histGroupIndex.setStatus('current')
histGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histGroupAddr.setStatus('current')
ictMcastAnalyzerHistoryMetrics = MibTable((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2), )
if mibBuilder.loadTexts: ictMcastAnalyzerHistoryMetrics.setStatus('current')
historyMetricsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1), ).setIndexNames((0, "ICOTERA-I6400-SERIES", "histMetrGroupAddr"))
if mibBuilder.loadTexts: historyMetricsEntry.setStatus('current')
histMetrGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrGroupAddr.setStatus('current')
histMetrSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrSourceAddr.setStatus('current')
histMetrDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrDstPort.setStatus('current')
histMetrSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrSrcPort.setStatus('current')
histMetrTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalBytes.setStatus('current')
histMetrTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalPackets.setStatus('current')
histMetrKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrKbps.setStatus('current')
histMetrPps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrPps.setStatus('current')
histMetrAvgKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrAvgKbps.setStatus('current')
histMetrAvgPps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrAvgPps.setStatus('current')
histMetrMaxDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 11), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrMaxDelta.setStatus('current')
histMetrAvgDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 12), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrAvgDelta.setStatus('current')
histMetrTotalMaxDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 13), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalMaxDelta.setStatus('current')
histMetrTotalAvgDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 14), IctDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalAvgDelta.setStatus('current')
histMetrStartTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 15), IctTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrStartTimestamp.setStatus('current')
histMetrStopTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 16), IctTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrStopTimestamp.setStatus('current')
histMetrMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 17), IctPortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrMemberPorts.setStatus('current')
histMetrStreamType = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrStreamType.setStatus('current')
histMetrSkips = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrSkips.setStatus('current')
histMetrDiscontinuities = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrDiscontinuities.setStatus('current')
histMetrLost = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrLost.setStatus('current')
histMetrReordered = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrReordered.setStatus('current')
histMetrTotalSkips = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalSkips.setStatus('current')
histMetrTotalDiscontinuities = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalDiscontinuities.setStatus('current')
histMetrTotalLost = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalLost.setStatus('current')
histMetrTotalReordered = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrTotalReordered.setStatus('current')
histMetrAvgLostPps = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 27), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrAvgLostPps.setStatus('current')
histMetrJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 28), IctJitter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: histMetrJitter.setStatus('current')
mibBuilder.exportSymbols("ICOTERA-I6400-SERIES", histGroupIndex=histGroupIndex, ictServices=ictServices, curMetrGroupAddr=curMetrGroupAddr, histMetrTotalReordered=histMetrTotalReordered, histMetrDstPort=histMetrDstPort, ictMcastAnalyzerCurrentList=ictMcastAnalyzerCurrentList, histMetrDiscontinuities=histMetrDiscontinuities, ictMcastAnalyzerHistoryMetrics=ictMcastAnalyzerHistoryMetrics, histMetrMemberPorts=histMetrMemberPorts, transceiverConnectorType=transceiverConnectorType, curMetrAvgLostPps=curMetrAvgLostPps, ictFacRst=ictFacRst, cfgTftpPath=cfgTftpPath, ictTransceiver=ictTransceiver, ictFwUpg=ictFwUpg, curMetrAvgPps=curMetrAvgPps, curMetrReordered=curMetrReordered, historyMetricsEntry=historyMetricsEntry, histMetrTotalBytes=histMetrTotalBytes, histMetrAvgLostPps=histMetrAvgLostPps, transceiverDdmTxBiasCurrent=transceiverDdmTxBiasCurrent, histMetrAvgPps=histMetrAvgPps, curMetrTotalLost=curMetrTotalLost, transceiverDdmTemperature=transceiverDdmTemperature, ictIGW1k=ictIGW1k, transceiverEthernetCompliance=transceiverEthernetCompliance, curMetrSourceAddr=curMetrSourceAddr, curMetrStreamType=curMetrStreamType, curMetrLost=curMetrLost, ictMgmtMib=ictMgmtMib, historyListEntry=historyListEntry, histMetrSourceAddr=histMetrSourceAddr, curMetrTotalSkips=curMetrTotalSkips, curMetrPps=curMetrPps, histMetrAvgDelta=histMetrAvgDelta, currentMetricsEntry=currentMetricsEntry, ictMcastAnalyzerHistoryList=ictMcastAnalyzerHistoryList, histMetrPps=histMetrPps, curMetrSkips=curMetrSkips, ictReset=ictReset, catvModuleAdminStatus=catvModuleAdminStatus, icotera=icotera, curMetrMemberPorts=curMetrMemberPorts, curMetrTotalAvgDelta=curMetrTotalAvgDelta, curMetrDiscontinuities=curMetrDiscontinuities, transceiverDdmTxPower=transceiverDdmTxPower, ictMcastAnalyzerHistory=ictMcastAnalyzerHistory, histMetrKbps=histMetrKbps, cfgStatus=cfgStatus, histMetrSkips=histMetrSkips, curMetrStartTimestamp=curMetrStartTimestamp, cfgExecute=cfgExecute, curMetrTotalMaxDelta=curMetrTotalMaxDelta, histMetrAvgKbps=histMetrAvgKbps, catvModuleRflevel=catvModuleRflevel, catvModuleLowSignal=catvModuleLowSignal, catvModulePowerLevel=catvModulePowerLevel, histMetrMaxDelta=histMetrMaxDelta, histMetrStopTimestamp=histMetrStopTimestamp, IctTimeStamp=IctTimeStamp, histMetrLost=histMetrLost, ictReboot=ictReboot, curMetrAvgKbps=curMetrAvgKbps, catvModuleSignalDetected=catvModuleSignalDetected, curMetrTotalBytes=curMetrTotalBytes, IctPortList=IctPortList, histMetrStartTimestamp=histMetrStartTimestamp, histGroupAddr=histGroupAddr, transceiverDiagCapable=transceiverDiagCapable, curMetrAvgDelta=curMetrAvgDelta, curGroupAddr=curGroupAddr, ictServicesMibs=ictServicesMibs, ictMcastAnalyzerCurrentMetrics=ictMcastAnalyzerCurrentMetrics, curMetrJitter=curMetrJitter, curMetrSrcPort=curMetrSrcPort, histMetrTotalPackets=histMetrTotalPackets, histMetrStreamType=histMetrStreamType, IctDelta=IctDelta, curGroupIndex=curGroupIndex, ictMcastAnalyzer=ictMcastAnalyzer, histMetrTotalLost=histMetrTotalLost, transceiverLaserWavelength=transceiverLaserWavelength, PYSNMP_MODULE_ID=icotera, upgUrl=upgUrl, performFactoryReset=performFactoryReset, transceiverDdmRxPower=transceiverDdmRxPower, ictCfgUpdate=ictCfgUpdate, IctJitter=IctJitter, curMetrDstPort=curMetrDstPort, curMetrMaxDelta=curMetrMaxDelta, ictFacRstMib=ictFacRstMib, upgStatus=upgStatus, transceiverTransceiverType=transceiverTransceiverType, transceiverLinkLength=transceiverLinkLength, histMetrReordered=histMetrReordered, catvModuleFilter=catvModuleFilter, currentListEntry=currentListEntry, curMetrTotalDiscontinuities=curMetrTotalDiscontinuities, histMetrSrcPort=histMetrSrcPort, curMetrKbps=curMetrKbps, ictMgmt=ictMgmt, histMetrTotalDiscontinuities=histMetrTotalDiscontinuities, histMetrGroupAddr=histMetrGroupAddr, ictMcastAnalyzerCurrent=ictMcastAnalyzerCurrent, curMetrTotalReordered=curMetrTotalReordered, ictCatv=ictCatv, transceiverDdmVoltage=transceiverDdmVoltage, histMetrTotalAvgDelta=histMetrTotalAvgDelta, upgExecute=upgExecute, performCpeReboot=performCpeReboot, histMetrTotalSkips=histMetrTotalSkips, histMetrJitter=histMetrJitter, curMetrTotalPackets=curMetrTotalPackets, histMetrTotalMaxDelta=histMetrTotalMaxDelta, curMetrStopTimestamp=curMetrStopTimestamp)
