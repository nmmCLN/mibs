#
# PySNMP MIB module CTRON-SFPS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:40 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
sfpsPortAttributeAPI, sfpsPortAttributeTable, sfpsPortStats, sfpsPortConfig = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsPortAttributeAPI", "sfpsPortAttributeTable", "sfpsPortStats", "sfpsPortConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter32", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsSwitchPort(Integer32):
    pass

class HexInteger(Integer32):
    pass

sfpsInPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1), )
if mibBuilder.loadTexts: sfpsInPortConfigTable.setStatus('mandatory')
sfpsInPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsInPortConfigPort"))
if mibBuilder.loadTexts: sfpsInPortConfigEntry.setStatus('mandatory')
sfpsInPortConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigPort.setStatus('mandatory')
sfpsInPortConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("loopback", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigAdminStatus.setStatus('mandatory')
sfpsInPortConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pending-disable", 4), ("pending-enable", 5), ("invalid-config", 6), ("testing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigOperStatus.setStatus('mandatory')
sfpsInPortConfigOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigOperTime.setStatus('mandatory')
sfpsInPortConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("other", 1), ("access-port", 2), ("network-port", 3), ("host-mgmt-port", 4), ("host-ctl-port", 5), ("unknown", 6), ("going-to-access", 7), ("hybrid-port", 8), ("stand-by", 9), ("network-only", 10), ("accessOnly", 11), ("raPrimary", 12), ("uplink", 13), ("fclStandby", 14), ("loopStandby", 15), ("raStandby", 16), ("flood", 17), ("uplinkFlood", 18), ("downlinkFlood", 19), ("unknown-ra-standby", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigType.setStatus('mandatory')
sfpsInPortConfigReservedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigReservedBW.setStatus('mandatory')
sfpsInPortConfigAllocBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigAllocBW.setStatus('mandatory')
sfpsInPortConfigQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigQoS.setStatus('mandatory')
sfpsInPortConfigQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigQSize.setStatus('mandatory')
sfpsInPortConfigQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigQLen.setStatus('mandatory')
sfpsInPortConfigSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigSwitchId.setStatus('mandatory')
sfpsInPortConfigMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("ethernet", 1), ("fddi", 2), ("atm-lec", 3), ("token-ring", 4), ("wan", 5), ("inb", 6), ("hcp", 7), ("hdp", 8), ("atm-svc", 9), ("atm-pvc", 10), ("unknown", 11), ("atm-forum-lec", 12), ("atm-forum-pvc", 13), ("atm-forum-svc", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigMediaType.setStatus('mandatory')
sfpsInPortConfigFrontPanelPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 13), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigFrontPanelPort.setStatus('mandatory')
sfpsInPortConfigLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("linkUp", 2), ("linkDown", 3), ("link-N-A", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigLinkStatus.setStatus('mandatory')
sfpsInPortConfigLinkStateAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigLinkStateAge.setStatus('mandatory')
sfpsInPortConfigRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("router-port", 2), ("no-router", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigRouterPort.setStatus('mandatory')
sfpsInPortConfigSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigSlotNumber.setStatus('mandatory')
sfpsInPortConfigMib2PortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigMib2PortId.setStatus('mandatory')
sfpsInPortConfigTopoAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigTopoAgent.setStatus('mandatory')
sfpsInPortConfigLayer3Learning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigLayer3Learning.setStatus('mandatory')
sfpsOutPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2), )
if mibBuilder.loadTexts: sfpsOutPortConfigTable.setStatus('mandatory')
sfpsOutPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsOutPortConfigPort"))
if mibBuilder.loadTexts: sfpsOutPortConfigEntry.setStatus('mandatory')
sfpsOutPortConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigPort.setStatus('mandatory')
sfpsOutPortConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("loopback", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigAdminStatus.setStatus('mandatory')
sfpsOutPortConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pending-disable", 4), ("pending-enable", 5), ("invalid-config", 6), ("testing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigOperStatus.setStatus('mandatory')
sfpsOutPortConfigOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigOperTime.setStatus('mandatory')
sfpsOutPortConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("other", 1), ("access-port", 2), ("network-port", 3), ("host-mgmt-port", 4), ("host-ctl-port", 5), ("unknown", 6), ("going-to-access", 7), ("hybrid-port", 8), ("stand-by", 9), ("network-only", 10), ("accessOnly", 11), ("raPrimary", 12), ("standbyFCLConflict", 13), ("standbyLoopedPort", 14), ("standbyVersionConflict", 15), ("standbyRANonPrimary", 16), ("flood", 17), ("uplinkFlood", 18), ("downlinkFlood", 19), ("unknown-ra-standby", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigType.setStatus('mandatory')
sfpsOutPortConfigReservedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigReservedBW.setStatus('mandatory')
sfpsOutPortConfigAllocBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigAllocBW.setStatus('mandatory')
sfpsOutPortConfigQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigQoS.setStatus('mandatory')
sfpsOutPortConfigQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigQSize.setStatus('mandatory')
sfpsOutPortConfigQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigQLen.setStatus('mandatory')
sfpsOutPortConfigSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigSwitchId.setStatus('mandatory')
sfpsOutPortConfigMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("ethernet", 1), ("fddi", 2), ("atm-lec", 3), ("token-ring", 4), ("wan", 5), ("inb", 6), ("hcp", 7), ("hdp", 8), ("atm-encap", 9), ("atm-pvc", 10), ("unknown", 11), ("atm-forum-lec", 12), ("atm-forum-pvc", 13), ("atm-forum-svc", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigMediaType.setStatus('mandatory')
sfpsOutPortConfigFrontPanelPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 13), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigFrontPanelPort.setStatus('mandatory')
sfpsOutPortConfigLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("linkUp", 2), ("linkDown", 3), ("linkNA", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigLinkStatus.setStatus('mandatory')
sfpsOutPortConfigLinkStateAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigLinkStateAge.setStatus('mandatory')
sfpsOutPortConfigRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("router-port", 2), ("no-router", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigRouterPort.setStatus('mandatory')
sfpsOutPortConfigSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigSlotNumber.setStatus('mandatory')
sfpsOutPortConfigMib2PortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigMib2PortId.setStatus('mandatory')
sfpsInPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1), )
if mibBuilder.loadTexts: sfpsInPortStatsTable.setStatus('mandatory')
sfpsInPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsInPortStatsPort"))
if mibBuilder.loadTexts: sfpsInPortStatsEntry.setStatus('mandatory')
sfpsInPortStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsPort.setStatus('mandatory')
sfpsInPortStatsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortStatsAdminStatus.setStatus('mandatory')
sfpsInPortStatsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortStatsReset.setStatus('mandatory')
sfpsInPortStatsOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsOperTime.setStatus('mandatory')
sfpsInPortStatsPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsPkts.setStatus('mandatory')
sfpsInPortStatsDiscardPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsDiscardPkts.setStatus('mandatory')
sfpsInPortStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsBytes.setStatus('mandatory')
sfpsInPortStatsDiscardBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsDiscardBytes.setStatus('mandatory')
sfpsInPortStatsQOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsQOverflows.setStatus('mandatory')
sfpsInPortStatsLinkUps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsLinkUps.setStatus('mandatory')
sfpsInPortStatsLinkDowns = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsLinkDowns.setStatus('mandatory')
sfpsOutPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2), )
if mibBuilder.loadTexts: sfpsOutPortStatsTable.setStatus('mandatory')
sfpsOutPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsOutPortStatsPort"))
if mibBuilder.loadTexts: sfpsOutPortStatsEntry.setStatus('mandatory')
sfpsOutPortStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsPort.setStatus('mandatory')
sfpsOutPortStatsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortStatsAdminStatus.setStatus('mandatory')
sfpsOutPortStatsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortStatsReset.setStatus('mandatory')
sfpsOutPortStatsOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsOperTime.setStatus('mandatory')
sfpsOutPortStatsPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsPkts.setStatus('mandatory')
sfpsOutPortStatsDiscardPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsDiscardPkts.setStatus('mandatory')
sfpsOutPortStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsBytes.setStatus('mandatory')
sfpsOutPortStatsDiscardBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsDiscardBytes.setStatus('mandatory')
sfpsOutPortStatsQOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsQOverflows.setStatus('mandatory')
sfpsOutPortStatsLinkUps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsLinkUps.setStatus('mandatory')
sfpsOutPortStatsLinkDowns = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsLinkDowns.setStatus('mandatory')
sfpsPortAttributePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPortAttributePort.setStatus('mandatory')
sfpsPortAttributeAttributes = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 2), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPortAttributeAttributes.setStatus('mandatory')
sfpsPortAttributeLearnSelfArp = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("off", 2), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPortAttributeLearnSelfArp.setStatus('mandatory')
sfpsPortAttributeAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("resetAll", 2), ("resetPort", 3), ("enablePortAttr", 4), ("disablePortAttr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPortAttributeAPIVerb.setStatus('mandatory')
sfpsPortAttributeAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPortAttributeAPIPort.setStatus('mandatory')
sfpsPortAttributeAPIAttribute = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("none", 2), ("learnSelfArp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPortAttributeAPIAttribute.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-PORT-MIB", sfpsInPortConfigRouterPort=sfpsInPortConfigRouterPort, sfpsInPortStatsBytes=sfpsInPortStatsBytes, sfpsOutPortStatsDiscardPkts=sfpsOutPortStatsDiscardPkts, sfpsInPortConfigLayer3Learning=sfpsInPortConfigLayer3Learning, sfpsOutPortStatsDiscardBytes=sfpsOutPortStatsDiscardBytes, sfpsPortAttributePort=sfpsPortAttributePort, sfpsInPortConfigType=sfpsInPortConfigType, sfpsPortAttributeAttributes=sfpsPortAttributeAttributes, HexInteger=HexInteger, sfpsInPortConfigMib2PortId=sfpsInPortConfigMib2PortId, sfpsOutPortConfigReservedBW=sfpsOutPortConfigReservedBW, sfpsOutPortConfigQoS=sfpsOutPortConfigQoS, sfpsPortAttributeAPIVerb=sfpsPortAttributeAPIVerb, sfpsOutPortConfigSlotNumber=sfpsOutPortConfigSlotNumber, sfpsOutPortConfigLinkStateAge=sfpsOutPortConfigLinkStateAge, sfpsOutPortStatsOperTime=sfpsOutPortStatsOperTime, sfpsInPortConfigSwitchId=sfpsInPortConfigSwitchId, sfpsOutPortConfigFrontPanelPort=sfpsOutPortConfigFrontPanelPort, sfpsInPortConfigAllocBW=sfpsInPortConfigAllocBW, sfpsInPortConfigQSize=sfpsInPortConfigQSize, sfpsInPortStatsOperTime=sfpsInPortStatsOperTime, sfpsOutPortStatsLinkDowns=sfpsOutPortStatsLinkDowns, sfpsOutPortStatsPort=sfpsOutPortStatsPort, sfpsInPortConfigFrontPanelPort=sfpsInPortConfigFrontPanelPort, sfpsInPortConfigReservedBW=sfpsInPortConfigReservedBW, sfpsInPortStatsQOverflows=sfpsInPortStatsQOverflows, sfpsOutPortStatsBytes=sfpsOutPortStatsBytes, sfpsInPortStatsLinkDowns=sfpsInPortStatsLinkDowns, sfpsInPortConfigSlotNumber=sfpsInPortConfigSlotNumber, sfpsInPortStatsTable=sfpsInPortStatsTable, sfpsOutPortConfigQSize=sfpsOutPortConfigQSize, sfpsOutPortStatsLinkUps=sfpsOutPortStatsLinkUps, sfpsOutPortStatsQOverflows=sfpsOutPortStatsQOverflows, sfpsOutPortConfigOperStatus=sfpsOutPortConfigOperStatus, sfpsOutPortConfigType=sfpsOutPortConfigType, sfpsOutPortConfigRouterPort=sfpsOutPortConfigRouterPort, sfpsOutPortStatsPkts=sfpsOutPortStatsPkts, sfpsInPortConfigOperTime=sfpsInPortConfigOperTime, sfpsInPortConfigLinkStateAge=sfpsInPortConfigLinkStateAge, sfpsOutPortConfigTable=sfpsOutPortConfigTable, sfpsOutPortConfigEntry=sfpsOutPortConfigEntry, sfpsPortAttributeLearnSelfArp=sfpsPortAttributeLearnSelfArp, sfpsOutPortConfigLinkStatus=sfpsOutPortConfigLinkStatus, sfpsInPortStatsLinkUps=sfpsInPortStatsLinkUps, sfpsOutPortStatsTable=sfpsOutPortStatsTable, sfpsInPortConfigLinkStatus=sfpsInPortConfigLinkStatus, sfpsOutPortConfigSwitchId=sfpsOutPortConfigSwitchId, sfpsPortAttributeAPIPort=sfpsPortAttributeAPIPort, sfpsInPortStatsPort=sfpsInPortStatsPort, sfpsPortAttributeAPIAttribute=sfpsPortAttributeAPIAttribute, sfpsOutPortConfigMediaType=sfpsOutPortConfigMediaType, sfpsOutPortConfigOperTime=sfpsOutPortConfigOperTime, sfpsInPortConfigTopoAgent=sfpsInPortConfigTopoAgent, sfpsOutPortStatsEntry=sfpsOutPortStatsEntry, sfpsOutPortStatsReset=sfpsOutPortStatsReset, sfpsInPortStatsAdminStatus=sfpsInPortStatsAdminStatus, sfpsOutPortConfigMib2PortId=sfpsOutPortConfigMib2PortId, sfpsInPortStatsEntry=sfpsInPortStatsEntry, sfpsInPortConfigQLen=sfpsInPortConfigQLen, sfpsOutPortConfigPort=sfpsOutPortConfigPort, sfpsOutPortStatsAdminStatus=sfpsOutPortStatsAdminStatus, sfpsInPortConfigQoS=sfpsInPortConfigQoS, sfpsOutPortConfigQLen=sfpsOutPortConfigQLen, sfpsInPortConfigTable=sfpsInPortConfigTable, sfpsInPortStatsPkts=sfpsInPortStatsPkts, sfpsInPortStatsReset=sfpsInPortStatsReset, sfpsInPortConfigAdminStatus=sfpsInPortConfigAdminStatus, sfpsInPortConfigOperStatus=sfpsInPortConfigOperStatus, sfpsInPortConfigMediaType=sfpsInPortConfigMediaType, sfpsInPortStatsDiscardPkts=sfpsInPortStatsDiscardPkts, sfpsOutPortConfigAllocBW=sfpsOutPortConfigAllocBW, SfpsSwitchPort=SfpsSwitchPort, sfpsOutPortConfigAdminStatus=sfpsOutPortConfigAdminStatus, sfpsInPortStatsDiscardBytes=sfpsInPortStatsDiscardBytes, sfpsInPortConfigEntry=sfpsInPortConfigEntry, sfpsInPortConfigPort=sfpsInPortConfigPort)
