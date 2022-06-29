#
# PySNMP MIB module F3-AMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-AMP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:49 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
VlanId, = mibBuilder.importSymbols("CM-COMMON-MIB", "VlanId")
IpManagementTunnelType, IpSourceAddrType, IpManagementTunnelEncapsulationType = mibBuilder.importSymbols("CM-IP-MIB", "IpManagementTunnelType", "IpSourceAddrType", "IpManagementTunnelEncapsulationType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Gauge32, Counter32, IpAddress, iso, ModuleIdentity, ObjectIdentity, Unsigned32, MibIdentifier, Bits, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Gauge32", "Counter32", "IpAddress", "iso", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Bits", "TimeTicks", "Integer32")
TruthValue, RowStatus, StorageType, TextualConvention, VariablePointer, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "StorageType", "TextualConvention", "VariablePointer", "DisplayString", "DateAndTime")
f3AMPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24))
f3AMPMIB.setRevisions(('2012-09-30 00:00',))
if mibBuilder.loadTexts: f3AMPMIB.setLastUpdated('201209310000Z')
if mibBuilder.loadTexts: f3AMPMIB.setOrganization('ADVA Optical Networking')
class AMPRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("client", 1), ("server", 2))

class AMPStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notAvailable", 1), ("disabled", 2), ("associatingActive", 3), ("associatingPassive", 4), ("associated", 5), ("noPeer", 6))

class AMPConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("provision", 2), ("noPeer", 3), ("request", 4), ("configSuccess", 5), ("configFail", 6), ("timeout", 7))

class AMPProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("efmOam", 1))

class AMPConfigAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noAction", 1), ("clearStats", 2))

f3AmpConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1))
f3AmpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2))
f3AmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3))
f3AmpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1), )
if mibBuilder.loadTexts: f3AmpConfigTable.setStatus('current')
f3AmpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1), ).setIndexNames((0, "F3-AMP-MIB", "f3AmpConfigIndex"))
if mibBuilder.loadTexts: f3AmpConfigEntry.setStatus('current')
f3AmpConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: f3AmpConfigIndex.setStatus('current')
f3AmpConfigRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 2), AMPRole()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRole.setStatus('current')
f3AmpConfigProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 3), AMPProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigProtocol.setStatus('current')
f3AmpConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigEnabled.setStatus('current')
f3AmpConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 5), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigPort.setStatus('current')
f3AmpConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 6), AMPStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigStatus.setStatus('current')
f3AmpConfigRemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysName.setStatus('current')
f3AmpConfigRemSysIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysIpAddr.setStatus('current')
f3AmpConfigRemSysIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysIpMask.setStatus('current')
f3AmpConfigRemSysDefGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysDefGateway.setStatus('current')
f3AmpConfigRemSysSNMPV1IfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigRemSysSNMPV1IfName.setStatus('current')
f3AmpConfigRemSysSrcIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 12), IpSourceAddrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigRemSysSrcIpAddrType.setStatus('current')
f3AmpConfigRemSysSrcIpAddrIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigRemSysSrcIpAddrIfName.setStatus('current')
f3AmpConfigRemTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIndex.setStatus('current')
f3AmpConfigRemTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 15), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelName.setStatus('current')
f3AmpConfigRemTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 16), IpManagementTunnelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelType.setStatus('current')
f3AmpConfigRemTunnelIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 17), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIpAddr.setStatus('current')
f3AmpConfigRemTunnelIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIpMask.setStatus('current')
f3AmpConfigRemTunnelVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 19), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelVlanId.setStatus('current')
f3AmpConfigRemTunnelSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 20), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelSVlanId.setStatus('current')
f3AmpConfigRemTunnelSVlanIdEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 21), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelSVlanIdEnabled.setStatus('current')
f3AmpConfigRemTunnelRip2PktsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 22), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelRip2PktsEnabled.setStatus('current')
f3AmpConfigRemTunnelCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelCOS.setStatus('current')
f3AmpConfigRemTunnelCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 24), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelCIR.setStatus('current')
f3AmpConfigRemTunnelEIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 25), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelEIR.setStatus('current')
f3AmpConfigRemTunnelBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 26), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelBufferSize.setStatus('current')
f3AmpConfigRemTunnelEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 27), IpManagementTunnelEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelEncapType.setStatus('current')
f3AmpConfigRemTunnelMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 28), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelMtu.setStatus('current')
f3AmpConfigAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 29), AMPConfigAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigAction.setStatus('current')
f3AmpConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 30), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigStorageType.setStatus('current')
f3AmpConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 31), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRowStatus.setStatus('current')
f3AmpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1), )
if mibBuilder.loadTexts: f3AmpStatsTable.setStatus('current')
f3AmpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1), ).setIndexNames((0, "F3-AMP-MIB", "f3AmpConfigIndex"))
if mibBuilder.loadTexts: f3AmpStatsEntry.setStatus('current')
f3AmpStatsProvDataTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvDataTx.setStatus('current')
f3AmpStatsProvDataRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvDataRx.setStatus('current')
f3AmpStatsProvRequestTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvRequestTx.setStatus('current')
f3AmpStatsProvRequestRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvRequestRx.setStatus('current')
f3AmpStatsConfigSuccessTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigSuccessTx.setStatus('current')
f3AmpStatsConfigSuccessRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigSuccessRx.setStatus('current')
f3AmpStatsConfigFailTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigFailTx.setStatus('current')
f3AmpStatsConfigFailRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigFailRx.setStatus('current')
f3AmpStatsSpuriousMessageRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsSpuriousMessageRx.setStatus('current')
f3AmpStatsTimeoutRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsTimeoutRx.setStatus('current')
f3AmpStatsLastRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 11), AMPConfigStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsLastRxStatus.setStatus('current')
f3AmpStatsRxTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsRxTimeStamp.setStatus('current')
f3AmpStatsLastTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 13), AMPConfigStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsLastTxStatus.setStatus('current')
f3AmpStatsTxTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 14), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsTxTimeStamp.setStatus('current')
f3AmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 1))
f3AmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2))
f3AmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 1, 1)).setObjects(("F3-AMP-MIB", "f3AmpConfigGroup"), ("F3-AMP-MIB", "f3AmpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AmpCompliance = f3AmpCompliance.setStatus('current')
f3AmpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2, 1)).setObjects(("F3-AMP-MIB", "f3AmpConfigRole"), ("F3-AMP-MIB", "f3AmpConfigProtocol"), ("F3-AMP-MIB", "f3AmpConfigEnabled"), ("F3-AMP-MIB", "f3AmpConfigPort"), ("F3-AMP-MIB", "f3AmpConfigStatus"), ("F3-AMP-MIB", "f3AmpConfigRemSysName"), ("F3-AMP-MIB", "f3AmpConfigRemSysIpAddr"), ("F3-AMP-MIB", "f3AmpConfigRemSysIpMask"), ("F3-AMP-MIB", "f3AmpConfigRemSysDefGateway"), ("F3-AMP-MIB", "f3AmpConfigRemSysSNMPV1IfName"), ("F3-AMP-MIB", "f3AmpConfigRemSysSrcIpAddrType"), ("F3-AMP-MIB", "f3AmpConfigRemSysSrcIpAddrIfName"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelIndex"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelName"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelType"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelIpAddr"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelIpMask"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelVlanId"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelSVlanId"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelSVlanIdEnabled"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelRip2PktsEnabled"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelCOS"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelCIR"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelEIR"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelBufferSize"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelEncapType"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelMtu"), ("F3-AMP-MIB", "f3AmpConfigAction"), ("F3-AMP-MIB", "f3AmpConfigStorageType"), ("F3-AMP-MIB", "f3AmpConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AmpConfigGroup = f3AmpConfigGroup.setStatus('current')
f3AmpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2, 2)).setObjects(("F3-AMP-MIB", "f3AmpStatsProvDataTx"), ("F3-AMP-MIB", "f3AmpStatsProvDataRx"), ("F3-AMP-MIB", "f3AmpStatsProvRequestTx"), ("F3-AMP-MIB", "f3AmpStatsProvRequestRx"), ("F3-AMP-MIB", "f3AmpStatsConfigSuccessTx"), ("F3-AMP-MIB", "f3AmpStatsConfigSuccessRx"), ("F3-AMP-MIB", "f3AmpStatsConfigFailTx"), ("F3-AMP-MIB", "f3AmpStatsConfigFailRx"), ("F3-AMP-MIB", "f3AmpStatsSpuriousMessageRx"), ("F3-AMP-MIB", "f3AmpStatsTimeoutRx"), ("F3-AMP-MIB", "f3AmpStatsLastRxStatus"), ("F3-AMP-MIB", "f3AmpStatsRxTimeStamp"), ("F3-AMP-MIB", "f3AmpStatsLastTxStatus"), ("F3-AMP-MIB", "f3AmpStatsTxTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AmpStatsGroup = f3AmpStatsGroup.setStatus('current')
mibBuilder.exportSymbols("F3-AMP-MIB", f3AmpStatsLastTxStatus=f3AmpStatsLastTxStatus, f3AmpConfigRemTunnelIndex=f3AmpConfigRemTunnelIndex, AMPProtocol=AMPProtocol, f3AmpConfigRemTunnelType=f3AmpConfigRemTunnelType, f3AmpConfigRemTunnelCOS=f3AmpConfigRemTunnelCOS, f3AmpStatsProvDataRx=f3AmpStatsProvDataRx, f3AMPMIB=f3AMPMIB, f3AmpStatsSpuriousMessageRx=f3AmpStatsSpuriousMessageRx, AMPRole=AMPRole, f3AmpConfigRemTunnelVlanId=f3AmpConfigRemTunnelVlanId, f3AmpCompliance=f3AmpCompliance, f3AmpGroups=f3AmpGroups, f3AmpConfigRemTunnelSVlanIdEnabled=f3AmpConfigRemTunnelSVlanIdEnabled, AMPStatus=AMPStatus, f3AmpStatsConfigSuccessRx=f3AmpStatsConfigSuccessRx, f3AmpCompliances=f3AmpCompliances, f3AmpStatsGroup=f3AmpStatsGroup, f3AmpStatsObjects=f3AmpStatsObjects, f3AmpConfigRemTunnelMtu=f3AmpConfigRemTunnelMtu, f3AmpConfigRemTunnelIpMask=f3AmpConfigRemTunnelIpMask, f3AmpConfigProtocol=f3AmpConfigProtocol, f3AmpStatsLastRxStatus=f3AmpStatsLastRxStatus, AMPConfigAction=AMPConfigAction, f3AmpStatsRxTimeStamp=f3AmpStatsRxTimeStamp, f3AmpStatsConfigFailTx=f3AmpStatsConfigFailTx, f3AmpConfigRemTunnelName=f3AmpConfigRemTunnelName, f3AmpConfigRemTunnelEIR=f3AmpConfigRemTunnelEIR, f3AmpStatsProvRequestRx=f3AmpStatsProvRequestRx, f3AmpConfigStatus=f3AmpConfigStatus, f3AmpStatsProvDataTx=f3AmpStatsProvDataTx, f3AmpConfigRemSysSNMPV1IfName=f3AmpConfigRemSysSNMPV1IfName, AMPConfigStatus=AMPConfigStatus, f3AmpConfigEnabled=f3AmpConfigEnabled, f3AmpConfigTable=f3AmpConfigTable, f3AmpConfigRemTunnelSVlanId=f3AmpConfigRemTunnelSVlanId, f3AmpConfigRemTunnelIpAddr=f3AmpConfigRemTunnelIpAddr, f3AmpConfigAction=f3AmpConfigAction, f3AmpConfigRemTunnelEncapType=f3AmpConfigRemTunnelEncapType, f3AmpConfigGroup=f3AmpConfigGroup, f3AmpStatsConfigFailRx=f3AmpStatsConfigFailRx, f3AmpConformance=f3AmpConformance, f3AmpConfigIndex=f3AmpConfigIndex, f3AmpConfigRemSysIpMask=f3AmpConfigRemSysIpMask, f3AmpConfigRemSysSrcIpAddrType=f3AmpConfigRemSysSrcIpAddrType, f3AmpConfigRemTunnelBufferSize=f3AmpConfigRemTunnelBufferSize, f3AmpConfigRemSysIpAddr=f3AmpConfigRemSysIpAddr, f3AmpConfigRemSysDefGateway=f3AmpConfigRemSysDefGateway, f3AmpStatsProvRequestTx=f3AmpStatsProvRequestTx, f3AmpConfigStorageType=f3AmpConfigStorageType, f3AmpConfigEntry=f3AmpConfigEntry, f3AmpConfigRemTunnelRip2PktsEnabled=f3AmpConfigRemTunnelRip2PktsEnabled, f3AmpConfigPort=f3AmpConfigPort, f3AmpConfigRemTunnelCIR=f3AmpConfigRemTunnelCIR, f3AmpStatsEntry=f3AmpStatsEntry, f3AmpConfigObjects=f3AmpConfigObjects, f3AmpConfigRowStatus=f3AmpConfigRowStatus, f3AmpStatsConfigSuccessTx=f3AmpStatsConfigSuccessTx, f3AmpStatsTxTimeStamp=f3AmpStatsTxTimeStamp, f3AmpConfigRemSysSrcIpAddrIfName=f3AmpConfigRemSysSrcIpAddrIfName, f3AmpStatsTimeoutRx=f3AmpStatsTimeoutRx, f3AmpConfigRole=f3AmpConfigRole, PYSNMP_MODULE_ID=f3AMPMIB, f3AmpStatsTable=f3AmpStatsTable, f3AmpConfigRemSysName=f3AmpConfigRemSysName)
