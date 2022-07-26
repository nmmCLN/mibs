#
# PySNMP MIB module MDS-IF-NX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-NX-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:28:32 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Unsigned32, MibIdentifier, Counter64, Bits, Gauge32, ModuleIdentity, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64", "Bits", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "NotificationType", "Integer32")
MacAddress, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TruthValue", "DisplayString")
mdsIfNxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3))
mdsIfNxMIB.setRevisions(('2018-05-16 00:00', '2016-09-21 00:00', '2015-08-21 00:00', '2015-06-12 00:00', '2015-03-27 00:00', '2014-10-20 00:00', '2014-05-13 00:00',))
if mibBuilder.loadTexts: mdsIfNxMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfNxMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mIfNxMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1))
mIfNxConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 1))
mIfNxStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2))
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LinkStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("initializing", 0), ("scanning", 1), ("negotiating", 2), ("authenticating", 3), ("associated", 4), ("disassociated", 5))

class InitStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("off", 0), ("initializing", 1), ("discovering", 2), ("reprogramming", 3), ("configuring", 4), ("complete", 5), ("error", 6))

class DeviceModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("remote", 0), ("accessPoint", 1), ("storeAndForward", 2), ("test", 3))

class ModemType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 10))
    namedValues = NamedValues(("e125kbps", 0), ("e250kbps", 1), ("e500kbps", 2), ("e1000kbps", 3), ("e1000Wkbps", 4), ("e1250kbps", 5), ("auto", 10))

class AlarmFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("notCalibrated", 23), ("vswrFault", 16), ("temperature", 0))

class FirmwareRevision(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'

class InetIpAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
mIfNxStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1), )
if mibBuilder.loadTexts: mIfNxStatusTable.setStatus('current')
mIfNxStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfNxStatusEntry.setStatus('current')
mIfNxLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 1), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLinkStatus.setStatus('current')
mIfNxInitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 2), InitStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxInitStatus.setStatus('current')
mIfNxCurrentModem = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 3), ModemType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxCurrentModem.setStatus('current')
mIfNxAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 4), AlarmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxAlarms.setStatus('current')
mIfNxSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxSerialNumber.setStatus('current')
mIfNxFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 6), FirmwareRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxFirmwareRevision.setStatus('current')
mIfNxHardwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 7), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxHardwareId.setStatus('current')
mIfNxHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 8), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxHardwareRevision.setStatus('current')
mIfNxTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxTemperature.setStatus('current')
mIfNxApInfoApAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoApAddress.setStatus('current')
mIfNxApInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 11), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoIpAddress.setStatus('current')
mIfNxApInfoConnectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoConnectedTime.setStatus('current')
mIfNxApInfoAvgRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoAvgRssi.setStatus('current')
mIfNxApInfoAvgLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoAvgLqi.setStatus('current')
mIfNxMacStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxSuccess.setStatus('current')
mIfNxMacStatsTxFail = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxFail.setStatus('current')
mIfNxMacStatsTxQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxQueueFull.setStatus('current')
mIfNxMacStatsTxNoSync = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxNoSync.setStatus('current')
mIfNxMacStatsTxNoAssoc = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxNoAssoc.setStatus('current')
mIfNxMacStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxError.setStatus('current')
mIfNxMacStatsTxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxRetry.setStatus('current')
mIfNxMacStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsRxSuccess.setStatus('current')
mIfNxMacStatsSyncCheckError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsSyncCheckError.setStatus('current')
mIfNxMacStatsSyncChange = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsSyncChange.setStatus('current')
mIfNxCurrentDeviceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 25), DeviceModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxCurrentDeviceMode.setStatus('current')
mIfNxLastRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLastRssi.setStatus('current')
mIfNxLastLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLastLqi.setStatus('current')
mIfNxLastChan = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLastChan.setStatus('current')
mIfNxActiveNic = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 29), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxActiveNic.setStatus('current')
mIfNxStatusConnRemTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2), )
if mibBuilder.loadTexts: mIfNxStatusConnRemTable.setStatus('current')
mIfNxStatusConnRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-NX-MIB", "mIfNxStatusConnRemAddress"))
if mibBuilder.loadTexts: mIfNxStatusConnRemEntry.setStatus('current')
mIfNxStatusConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAddress.setStatus('current')
mIfNxStatusConnRemIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemIpAddress.setStatus('current')
mIfNxStatusConnRemTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemTimeToLive.setStatus('current')
mIfNxStatusConnRemLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 4), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemLinkStatus.setStatus('current')
mIfNxStatusConnRemNicId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 5), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemNicId.setStatus('current')
mIfNxStatusConnRemAvgRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgRssi.setStatus('current')
mIfNxStatusConnRemAvgLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgLqi.setStatus('current')
mIfNxStatusConnRemStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxPackets.setStatus('current')
mIfNxStatusConnRemStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxBytes.setStatus('current')
mIfNxStatusConnRemStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxPackets.setStatus('current')
mIfNxStatusConnRemStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxBytes.setStatus('current')
mIfNxStatusConnRemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxError.setStatus('current')
mIfNxStatusConnRemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxError.setStatus('current')
mIfNxStatusConnRemStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxDrop.setStatus('current')
mIfNxStatusConnRemStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxDrop.setStatus('current')
mIfNxStatusConnRemAvgSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgSnr.setStatus('current')
mIfNxStatusConnRemStatsGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 17), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsGateway.setStatus('current')
mIfNxStatusConnRemStatsAllIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsAllIp.setStatus('current')
mIfNxStatusConnRemStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsName.setStatus('current')
mIfNxStatusConnRemStatsAlarmed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsAlarmed.setStatus('current')
mIfNxStatusConnRemStatsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsVersion.setStatus('current')
mIfNxStatusConnRemStatsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTemp.setStatus('current')
mIfNxStatusConnRemStatsDwnRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnRssi.setStatus('current')
mIfNxStatusConnRemStatsDwnLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnLqi.setStatus('current')
mIfNxStatusConnRemStatsDwnSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnSnr.setStatus('current')
mIfNxStatusEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3), )
if mibBuilder.loadTexts: mIfNxStatusEndpointTable.setStatus('current')
mIfNxStatusEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-NX-MIB", "mIfNxStatusEndpointAddress"))
if mibBuilder.loadTexts: mIfNxStatusEndpointEntry.setStatus('current')
mIfNxStatusEndpointAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointAddress.setStatus('current')
mIfNxStatusEndpointIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointIpAddress.setStatus('current')
mIfNxStatusEndpointTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointTimeToLive.setStatus('current')
mIfNxStatusEndpointRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointRemAddress.setStatus('current')
mIfNxStatusEndpointStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxPackets.setStatus('current')
mIfNxStatusEndpointStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxBytes.setStatus('current')
mIfNxStatusEndpointStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxPackets.setStatus('current')
mIfNxStatusEndpointStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxBytes.setStatus('current')
mIfNxStatusEndpointStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxError.setStatus('current')
mIfNxStatusEndpointStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxError.setStatus('current')
mIfNxStatusEndpointStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxDrop.setStatus('current')
mIfNxStatusEndpointStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxDrop.setStatus('current')
mIfNxStatusActChanTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4), )
if mibBuilder.loadTexts: mIfNxStatusActChanTable.setStatus('current')
mIfNxStatusActChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-NX-MIB", "mIfNxStatusActChanChannel"))
if mibBuilder.loadTexts: mIfNxStatusActChanEntry.setStatus('current')
mIfNxStatusActChanChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 1), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanChannel.setStatus('current')
mIfNxStatusActChanFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanFrequency.setStatus('current')
mIfNxStatusActChanAvgRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanAvgRssi.setStatus('current')
mIfNxStatusActChanAvgLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanAvgLqi.setStatus('current')
mdsIfNxMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3))
mdsIfNxMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 1))
mdsIfNxMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2))
mIfNxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 1, 1)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusGroup"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemGroup"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointGroup"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxCompliance = mIfNxCompliance.setStatus('current')
mIfNxStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 1)).setObjects(("MDS-IF-NX-MIB", "mIfNxLinkStatus"), ("MDS-IF-NX-MIB", "mIfNxInitStatus"), ("MDS-IF-NX-MIB", "mIfNxCurrentModem"), ("MDS-IF-NX-MIB", "mIfNxAlarms"), ("MDS-IF-NX-MIB", "mIfNxSerialNumber"), ("MDS-IF-NX-MIB", "mIfNxFirmwareRevision"), ("MDS-IF-NX-MIB", "mIfNxHardwareId"), ("MDS-IF-NX-MIB", "mIfNxHardwareRevision"), ("MDS-IF-NX-MIB", "mIfNxTemperature"), ("MDS-IF-NX-MIB", "mIfNxApInfoApAddress"), ("MDS-IF-NX-MIB", "mIfNxApInfoIpAddress"), ("MDS-IF-NX-MIB", "mIfNxApInfoConnectedTime"), ("MDS-IF-NX-MIB", "mIfNxApInfoAvgRssi"), ("MDS-IF-NX-MIB", "mIfNxApInfoAvgLqi"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxSuccess"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxFail"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxQueueFull"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxNoSync"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxNoAssoc"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxError"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxRetry"), ("MDS-IF-NX-MIB", "mIfNxMacStatsRxSuccess"), ("MDS-IF-NX-MIB", "mIfNxMacStatsSyncCheckError"), ("MDS-IF-NX-MIB", "mIfNxMacStatsSyncChange"), ("MDS-IF-NX-MIB", "mIfNxCurrentDeviceMode"), ("MDS-IF-NX-MIB", "mIfNxLastRssi"), ("MDS-IF-NX-MIB", "mIfNxLastLqi"), ("MDS-IF-NX-MIB", "mIfNxLastChan"), ("MDS-IF-NX-MIB", "mIfNxActiveNic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusGroup = mIfNxStatusGroup.setStatus('current')
mIfNxStatusConnRemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 2)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusConnRemAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemIpAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemTimeToLive"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemLinkStatus"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemNicId"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgRssi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgLqi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxError"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxError"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxDrop"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxDrop"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgSnr"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsGateway"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsAllIp"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsName"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsAlarmed"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsVersion"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTemp"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnRssi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnLqi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnSnr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusConnRemGroup = mIfNxStatusConnRemGroup.setStatus('current')
mIfNxStatusEndpointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 3)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusEndpointAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointIpAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointTimeToLive"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointRemAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxError"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxError"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxDrop"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusEndpointGroup = mIfNxStatusEndpointGroup.setStatus('current')
mIfNxStatusActChanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 4)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusActChanChannel"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanFrequency"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanAvgRssi"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanAvgLqi"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusActChanGroup = mIfNxStatusActChanGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-IF-NX-MIB", mIfNxStatusActChanTable=mIfNxStatusActChanTable, mIfNxCurrentModem=mIfNxCurrentModem, FirmwareRevision=FirmwareRevision, mIfNxStatusActChanEntry=mIfNxStatusActChanEntry, mIfNxStatusConnRemStatsDwnRssi=mIfNxStatusConnRemStatsDwnRssi, mIfNxStatusConnRemStatsRxDrop=mIfNxStatusConnRemStatsRxDrop, mIfNxStatusEndpointStatsRxPackets=mIfNxStatusEndpointStatsRxPackets, mIfNxStatusConnRemStatsGateway=mIfNxStatusConnRemStatsGateway, mIfNxStatusActChanChannel=mIfNxStatusActChanChannel, mIfNxFirmwareRevision=mIfNxFirmwareRevision, mIfNxStatusEndpointTimeToLive=mIfNxStatusEndpointTimeToLive, mIfNxStatusEndpointRemAddress=mIfNxStatusEndpointRemAddress, mdsIfNxMIB=mdsIfNxMIB, mIfNxApInfoIpAddress=mIfNxApInfoIpAddress, mIfNxStatusActChanAvgLqi=mIfNxStatusActChanAvgLqi, mIfNxLastRssi=mIfNxLastRssi, mIfNxStatusEndpointStatsRxBytes=mIfNxStatusEndpointStatsRxBytes, mIfNxStatusConnRemStatsTxBytes=mIfNxStatusConnRemStatsTxBytes, mIfNxLinkStatus=mIfNxLinkStatus, mIfNxMacStatsSyncCheckError=mIfNxMacStatsSyncCheckError, mIfNxStatusConnRemStatsRxError=mIfNxStatusConnRemStatsRxError, mIfNxCurrentDeviceMode=mIfNxCurrentDeviceMode, mIfNxStatusConnRemStatsVersion=mIfNxStatusConnRemStatsVersion, mIfNxStatusConnRemStatsRxPackets=mIfNxStatusConnRemStatsRxPackets, AlarmFlags=AlarmFlags, mIfNxApInfoAvgLqi=mIfNxApInfoAvgLqi, mIfNxStatus=mIfNxStatus, mIfNxStatusConnRemAvgLqi=mIfNxStatusConnRemAvgLqi, mdsIfNxMIBConformance=mdsIfNxMIBConformance, UnsignedShort=UnsignedShort, mIfNxStatusConnRemStatsTxDrop=mIfNxStatusConnRemStatsTxDrop, mIfNxStatusConnRemIpAddress=mIfNxStatusConnRemIpAddress, ModemType=ModemType, DeviceModeType=DeviceModeType, mIfNxCompliance=mIfNxCompliance, mIfNxMacStatsTxFail=mIfNxMacStatsTxFail, mIfNxMacStatsTxError=mIfNxMacStatsTxError, mIfNxStatusEndpointStatsTxBytes=mIfNxStatusEndpointStatsTxBytes, mIfNxMacStatsTxQueueFull=mIfNxMacStatsTxQueueFull, mIfNxStatusEndpointTable=mIfNxStatusEndpointTable, mIfNxStatusGroup=mIfNxStatusGroup, LinkStatus=LinkStatus, PYSNMP_MODULE_ID=mdsIfNxMIB, mIfNxMacStatsTxSuccess=mIfNxMacStatsTxSuccess, mIfNxStatusEndpointStatsTxDrop=mIfNxStatusEndpointStatsTxDrop, mIfNxLastLqi=mIfNxLastLqi, mIfNxStatusEntry=mIfNxStatusEntry, mIfNxStatusConnRemTimeToLive=mIfNxStatusConnRemTimeToLive, mIfNxApInfoApAddress=mIfNxApInfoApAddress, mIfNxMacStatsTxRetry=mIfNxMacStatsTxRetry, mIfNxStatusEndpointGroup=mIfNxStatusEndpointGroup, mIfNxStatusEndpointStatsTxError=mIfNxStatusEndpointStatsTxError, mIfNxMIBObjects=mIfNxMIBObjects, mIfNxStatusEndpointStatsRxDrop=mIfNxStatusEndpointStatsRxDrop, mIfNxStatusConnRemTable=mIfNxStatusConnRemTable, mIfNxStatusEndpointIpAddress=mIfNxStatusEndpointIpAddress, mIfNxStatusActChanFrequency=mIfNxStatusActChanFrequency, mIfNxHardwareId=mIfNxHardwareId, mIfNxStatusConnRemAvgSnr=mIfNxStatusConnRemAvgSnr, mIfNxStatusConnRemAddress=mIfNxStatusConnRemAddress, mIfNxStatusConnRemStatsAllIp=mIfNxStatusConnRemStatsAllIp, InetIpAddress=InetIpAddress, mIfNxMacStatsTxNoSync=mIfNxMacStatsTxNoSync, mIfNxMacStatsRxSuccess=mIfNxMacStatsRxSuccess, mIfNxStatusConnRemStatsTemp=mIfNxStatusConnRemStatsTemp, mIfNxStatusActChanAvgRssi=mIfNxStatusActChanAvgRssi, mIfNxStatusEndpointEntry=mIfNxStatusEndpointEntry, mIfNxStatusConnRemNicId=mIfNxStatusConnRemNicId, mIfNxStatusConnRemEntry=mIfNxStatusConnRemEntry, mIfNxStatusConnRemStatsDwnLqi=mIfNxStatusConnRemStatsDwnLqi, mIfNxActiveNic=mIfNxActiveNic, mIfNxStatusEndpointStatsRxError=mIfNxStatusEndpointStatsRxError, mIfNxSerialNumber=mIfNxSerialNumber, mdsIfNxMIBGroups=mdsIfNxMIBGroups, mIfNxStatusConnRemAvgRssi=mIfNxStatusConnRemAvgRssi, mIfNxApInfoAvgRssi=mIfNxApInfoAvgRssi, mIfNxHardwareRevision=mIfNxHardwareRevision, UnsignedByte=UnsignedByte, mIfNxStatusConnRemStatsRxBytes=mIfNxStatusConnRemStatsRxBytes, mIfNxApInfoConnectedTime=mIfNxApInfoConnectedTime, mIfNxAlarms=mIfNxAlarms, mIfNxLastChan=mIfNxLastChan, mIfNxMacStatsTxNoAssoc=mIfNxMacStatsTxNoAssoc, mIfNxStatusConnRemStatsDwnSnr=mIfNxStatusConnRemStatsDwnSnr, mdsIfNxMIBCompliances=mdsIfNxMIBCompliances, mIfNxStatusConnRemStatsTxError=mIfNxStatusConnRemStatsTxError, mIfNxStatusConnRemStatsTxPackets=mIfNxStatusConnRemStatsTxPackets, InitStatus=InitStatus, mIfNxStatusConnRemStatsAlarmed=mIfNxStatusConnRemStatsAlarmed, mIfNxStatusConnRemStatsName=mIfNxStatusConnRemStatsName, mIfNxMacStatsSyncChange=mIfNxMacStatsSyncChange, mIfNxStatusEndpointAddress=mIfNxStatusEndpointAddress, mIfNxStatusConnRemGroup=mIfNxStatusConnRemGroup, mIfNxStatusActChanGroup=mIfNxStatusActChanGroup, mIfNxStatusConnRemLinkStatus=mIfNxStatusConnRemLinkStatus, mIfNxInitStatus=mIfNxInitStatus, mIfNxStatusEndpointStatsTxPackets=mIfNxStatusEndpointStatsTxPackets, mIfNxStatusTable=mIfNxStatusTable, mIfNxConfig=mIfNxConfig, mIfNxTemperature=mIfNxTemperature)
