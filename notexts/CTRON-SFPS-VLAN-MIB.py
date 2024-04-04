#
# PySNMP MIB module CTRON-SFPS-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:39 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
vlanAPI, vlanCountAPI, vlanName, vlanPort, vlanTestAPI, vlanAMRSubnets, vlanSystem, vlanAMRStats, vlanAMRRules = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "vlanAPI", "vlanCountAPI", "vlanName", "vlanPort", "vlanTestAPI", "vlanAMRSubnets", "vlanSystem", "vlanAMRStats", "vlanAMRRules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Counter32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Counter32", "iso", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class VlanSwitchInstance(Integer32):
    pass

class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class HexInteger(Integer32):
    pass

class SfpsSwitchPort(Integer32):
    pass

sfpsVAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("other", 1), ("add-vlan", 2), ("delete-vlan", 3), ("enable-vlan", 4), ("disable-vlan", 5), ("map-port", 6), ("unmap-port", 7), ("enable-port", 8), ("disable-port", 9), ("map-user", 10), ("unmap-user", 11), ("tap-vlan", 12), ("untap-vlan", 13), ("auto-register", 14), ("auto-unregister", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIVerb.setStatus('mandatory')
sfpsVAPIInPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 2), SfpsSwitchPort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIInPort.setStatus('mandatory')
sfpsVAPIVlanName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIVlanName.setStatus('mandatory')
sfpsVAPIOutPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 4), SfpsSwitchPort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIOutPort.setStatus('mandatory')
sfpsVAPIUserMAC = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 5), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUserMAC.setStatus('mandatory')
sfpsVAPIUserAliasTag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("aoMacDx", 1), ("aoIpxSap", 2), ("aoIpxRIP", 3), ("aoInetYP", 4), ("aoInetUDP", 5), ("aoIpxIpx", 6), ("aoInetIP", 7), ("aoInetRPC", 8), ("aoInetRIP", 9), ("aoMacDXMcast", 10), ("aoAtDDP", 11), ("aoEmpty", 12), ("aoVlan", 13), ("aoHostName", 14), ("aoNetBiosName", 15), ("aoInetIPMask", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUserAliasTag.setStatus('mandatory')
sfpsVAPIUserAlias = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUserAlias.setStatus('mandatory')
sfpsVAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAdminStatus.setStatus('mandatory')
sfpsVAPIAutoRegisterRule = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("ether-type", 2), ("ip-subnet", 3), ("netBIOS", 4), ("ipx-Server", 5), ("appleTalk", 6), ("decNET", 7), ("vines", 8), ("bpdu", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAutoRegisterRule.setStatus('mandatory')
sfpsVAPIAutoRegMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAutoRegMask.setStatus('mandatory')
sfpsVAPIAutoRegValue = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAutoRegValue.setStatus('mandatory')
sfpsVAPIUnicastPolicy = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("open", 2), ("secure", 3))).clone('open')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUnicastPolicy.setStatus('mandatory')
sfpsVAPIPortPolicy = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("normal", 2), ("locked", 3))).clone('locked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIPortPolicy.setStatus('mandatory')
sfpsVAPIFloodPolicy = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("flooding-on", 2), ("flooding-off", 3))).clone('flooding-on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIFloodPolicy.setStatus('mandatory')
sfpsVAPIRouterPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("router-port", 2), ("no-router", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIRouterPort.setStatus('mandatory')
sfpsVAPIVlanId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIVlanId.setStatus('mandatory')
sfpsVAPINvramId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPINvramId.setStatus('mandatory')
sfpsVAPIRelayAgent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIRelayAgent.setStatus('mandatory')
sfpsVAPILayer3Learning = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("learning-enabled", 2), ("learning-disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPILayer3Learning.setStatus('mandatory')
vlanNameTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1), )
if mibBuilder.loadTexts: vlanNameTable.setStatus('mandatory')
vlanNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanNameNHash"), (0, "CTRON-SFPS-VLAN-MIB", "vlanNameIndex"))
if mibBuilder.loadTexts: vlanNameEntry.setStatus('mandatory')
vlanNameNHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameNHash.setStatus('mandatory')
vlanNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameIndex.setStatus('mandatory')
vlanNameVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameVlanName.setStatus('mandatory')
vlanNameAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameAdminStatus.setStatus('mandatory')
vlanNameOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("shutdown-pending", 4), ("startup-pending", 5), ("invalid-config", 6), ("testing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameOperStatus.setStatus('mandatory')
vlanNameUniPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("open", 2), ("secure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameUniPolicy.setStatus('mandatory')
vlanNameFloodPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 2))).clone(namedValues=NamedValues(("other", 1), ("flood-on", 3), ("flood-off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameFloodPolicy.setStatus('mandatory')
vlanNameStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameStatusTime.setStatus('mandatory')
vlanNameNumUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameNumUsers.setStatus('mandatory')
vlanNameEnabledPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameEnabledPorts.setStatus('mandatory')
vlanNameMappedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameMappedPorts.setStatus('mandatory')
vlanNameVlanRule = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameVlanRule.setStatus('mandatory')
vlanNameFloodPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameFloodPorts.setStatus('mandatory')
vlanNameVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameVlanId.setStatus('mandatory')
vlanNameRelayAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameRelayAgent.setStatus('mandatory')
vlanSystemTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1), )
if mibBuilder.loadTexts: vlanSystemTable.setStatus('mandatory')
vlanSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanSystemSwitchInstance"))
if mibBuilder.loadTexts: vlanSystemEntry.setStatus('mandatory')
vlanSystemSwitchInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 1), VlanSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemSwitchInstance.setStatus('mandatory')
vlanSystemAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemAdminStatus.setStatus('mandatory')
vlanSystemAdminReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemAdminReset.setStatus('mandatory')
vlanSystemOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pending-disable", 4), ("pending-enable", 5), ("invalid-config", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemOperStatus.setStatus('mandatory')
vlanSystemOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemOperTime.setStatus('mandatory')
vlanSystemLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemLastChange.setStatus('mandatory')
vlanSystemVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemVersion.setStatus('mandatory')
vlanSystemMibRev = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemMibRev.setStatus('mandatory')
vlanSystemAgentIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemAgentIP.setStatus('mandatory')
vlanSystemDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemDomainName.setStatus('mandatory')
vlanSystemPollCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemPollCount.setStatus('mandatory')
vlanSystemFirstPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemFirstPollTime.setStatus('mandatory')
vlanSystemLastPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemLastPollTime.setStatus('mandatory')
vlanSystemPriorPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemPriorPollTime.setStatus('mandatory')
vlanSystemDeltaPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemDeltaPollTime.setStatus('mandatory')
vlanTestAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("other", 1), ("add-vlan", 2), ("delete-vlan", 3), ("enable-vlan", 4), ("disable-vlan", 5), ("open-vlan", 6), ("secure-vlan", 7), ("enable-vlan-port", 8), ("disable-vlan-port", 9), ("map-vlan-port", 10), ("unmap-vlan-port", 11), ("tap-vlan-port", 12), ("untap-vlan-port", 13), ("get-vlan-info", 14), ("get-port-info", 15), ("fill-table", 16), ("empty-table", 17)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIVerb.setStatus('mandatory')
vlanTestAPIVlanName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIVlanName.setStatus('mandatory')
vlanTestAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIPort.setStatus('mandatory')
vlanTestAPIVlanId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIVlanId.setStatus('mandatory')
vlanTestAPIOutputTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4), )
if mibBuilder.loadTexts: vlanTestAPIOutputTable.setStatus('mandatory')
vlanTestAPIOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanTestAPIOutputIndex"))
if mibBuilder.loadTexts: vlanTestAPIOutputEntry.setStatus('mandatory')
vlanTestAPIOutputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputIndex.setStatus('mandatory')
vlanTestAPIOutputVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputVlanName.setStatus('mandatory')
vlanTestAPIOutputUserCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputUserCnt.setStatus('mandatory')
vlanTestAPIOutputStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputStatus.setStatus('mandatory')
vlanTestAPIOutputPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("normal", 2), ("secure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputPolicy.setStatus('mandatory')
vlanTestAPIOutputPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputPort.setStatus('mandatory')
vlanTestAPIOutputMap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("unmapped", 2), ("mapped", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputMap.setStatus('mandatory')
vlanTestAPIOutputAble = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputAble.setStatus('mandatory')
vlanTestAPIOutputTap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("untapped", 2), ("tapped", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputTap.setStatus('mandatory')
vlanTestAPIOutputVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputVlanId.setStatus('mandatory')
vlanCountAPITotal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanCountAPITotal.setStatus('mandatory')
vlanCountAPIAdmin = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanCountAPIAdmin.setStatus('mandatory')
vlanCountAPIAutoreg = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanCountAPIAutoreg.setStatus('mandatory')
vlanAMRRulesTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1), )
if mibBuilder.loadTexts: vlanAMRRulesTable.setStatus('mandatory')
vlanAMRRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanAMRRulesRule"))
if mibBuilder.loadTexts: vlanAMRRulesEntry.setStatus('mandatory')
vlanAMRRulesRule = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("etherType", 2), ("ipSubNet", 3), ("netBIOS", 4), ("ipxServer", 5), ("appleTalk", 6), ("decNET", 7), ("vines", 8), ("bpdu", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRRulesRule.setStatus('mandatory')
vlanAMRRulesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRRulesStatus.setStatus('mandatory')
vlanAMRStatsNumRulesEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRStatsNumRulesEnabled.setStatus('mandatory')
vlanAMRStatsSingleMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 8, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRStatsSingleMask.setStatus('mandatory')
vlanAMRSubnetsPrefix = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 7, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRSubnetsPrefix.setStatus('mandatory')
vlanAMRSubnetsMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 7, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRSubnetsMask.setStatus('mandatory')
vlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1), )
if mibBuilder.loadTexts: vlanPortTable.setStatus('mandatory')
vlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanPortPortNum"))
if mibBuilder.loadTexts: vlanPortEntry.setStatus('mandatory')
vlanPortPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortPortNum.setStatus('mandatory')
vlanPortPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortPortStatus.setStatus('mandatory')
vlanPortPortPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("normal", 2), ("locked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortPortPolicy.setStatus('mandatory')
vlanPortVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortVlanName.setStatus('mandatory')
vlanPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortAdminStatus.setStatus('mandatory')
vlanPortUniPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("open", 2), ("secure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortUniPolicy.setStatus('mandatory')
vlanPortFloodPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("floodOn", 2), ("floodOff", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortFloodPolicy.setStatus('mandatory')
vlanPortRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("routerPort", 2), ("noRouter", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortRouterPort.setStatus('mandatory')
vlanPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortVlanId.setStatus('mandatory')
vlanPortRelayAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortRelayAgent.setStatus('mandatory')
vlanPortLayer3Learning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortLayer3Learning.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-VLAN-MIB", vlanSystemLastPollTime=vlanSystemLastPollTime, sfpsVAPIVlanId=sfpsVAPIVlanId, vlanNameAdminStatus=vlanNameAdminStatus, sfpsVAPILayer3Learning=sfpsVAPILayer3Learning, vlanNameVlanId=vlanNameVlanId, vlanPortPortNum=vlanPortPortNum, vlanNameVlanRule=vlanNameVlanRule, vlanSystemTable=vlanSystemTable, vlanTestAPIOutputTable=vlanTestAPIOutputTable, vlanPortVlanName=vlanPortVlanName, vlanSystemSwitchInstance=vlanSystemSwitchInstance, sfpsVAPIOutPort=sfpsVAPIOutPort, vlanTestAPIOutputUserCnt=vlanTestAPIOutputUserCnt, sfpsVAPIRelayAgent=sfpsVAPIRelayAgent, vlanSystemPriorPollTime=vlanSystemPriorPollTime, sfpsVAPIAdminStatus=sfpsVAPIAdminStatus, vlanAMRRulesTable=vlanAMRRulesTable, vlanNameRelayAgent=vlanNameRelayAgent, vlanNameOperStatus=vlanNameOperStatus, vlanNameTable=vlanNameTable, SfpsSwitchPort=SfpsSwitchPort, vlanTestAPIOutputAble=vlanTestAPIOutputAble, vlanAMRRulesRule=vlanAMRRulesRule, vlanNameNHash=vlanNameNHash, sfpsVAPIInPort=sfpsVAPIInPort, sfpsVAPIRouterPort=sfpsVAPIRouterPort, sfpsVAPIVerb=sfpsVAPIVerb, vlanPortUniPolicy=vlanPortUniPolicy, sfpsVAPIUnicastPolicy=sfpsVAPIUnicastPolicy, vlanSystemDomainName=vlanSystemDomainName, sfpsVAPINvramId=sfpsVAPINvramId, vlanNameFloodPolicy=vlanNameFloodPolicy, vlanAMRSubnetsMask=vlanAMRSubnetsMask, vlanPortVlanId=vlanPortVlanId, vlanTestAPIVlanId=vlanTestAPIVlanId, vlanAMRStatsNumRulesEnabled=vlanAMRStatsNumRulesEnabled, vlanTestAPIVlanName=vlanTestAPIVlanName, vlanSystemFirstPollTime=vlanSystemFirstPollTime, vlanPortRelayAgent=vlanPortRelayAgent, SfpsAddress=SfpsAddress, vlanCountAPIAdmin=vlanCountAPIAdmin, vlanPortRouterPort=vlanPortRouterPort, vlanNameIndex=vlanNameIndex, vlanTestAPIOutputStatus=vlanTestAPIOutputStatus, vlanTestAPIOutputMap=vlanTestAPIOutputMap, vlanSystemAgentIP=vlanSystemAgentIP, vlanTestAPIOutputEntry=vlanTestAPIOutputEntry, vlanTestAPIPort=vlanTestAPIPort, vlanPortPortStatus=vlanPortPortStatus, vlanPortFloodPolicy=vlanPortFloodPolicy, sfpsVAPIUserMAC=sfpsVAPIUserMAC, vlanNameEnabledPorts=vlanNameEnabledPorts, vlanNameUniPolicy=vlanNameUniPolicy, vlanSystemOperStatus=vlanSystemOperStatus, sfpsVAPIAutoRegMask=sfpsVAPIAutoRegMask, vlanPortAdminStatus=vlanPortAdminStatus, vlanCountAPIAutoreg=vlanCountAPIAutoreg, vlanNameVlanName=vlanNameVlanName, sfpsVAPIUserAlias=sfpsVAPIUserAlias, vlanPortEntry=vlanPortEntry, vlanAMRSubnetsPrefix=vlanAMRSubnetsPrefix, vlanTestAPIOutputPolicy=vlanTestAPIOutputPolicy, vlanSystemAdminStatus=vlanSystemAdminStatus, vlanPortTable=vlanPortTable, vlanSystemPollCount=vlanSystemPollCount, VlanSwitchInstance=VlanSwitchInstance, HexInteger=HexInteger, vlanNameNumUsers=vlanNameNumUsers, vlanCountAPITotal=vlanCountAPITotal, vlanAMRStatsSingleMask=vlanAMRStatsSingleMask, vlanNameStatusTime=vlanNameStatusTime, vlanNameMappedPorts=vlanNameMappedPorts, vlanTestAPIVerb=vlanTestAPIVerb, vlanSystemDeltaPollTime=vlanSystemDeltaPollTime, vlanTestAPIOutputVlanName=vlanTestAPIOutputVlanName, vlanAMRRulesStatus=vlanAMRRulesStatus, vlanNameFloodPorts=vlanNameFloodPorts, vlanSystemAdminReset=vlanSystemAdminReset, vlanTestAPIOutputPort=vlanTestAPIOutputPort, sfpsVAPIAutoRegisterRule=sfpsVAPIAutoRegisterRule, vlanSystemOperTime=vlanSystemOperTime, vlanSystemMibRev=vlanSystemMibRev, sfpsVAPIUserAliasTag=sfpsVAPIUserAliasTag, vlanSystemVersion=vlanSystemVersion, sfpsVAPIAutoRegValue=sfpsVAPIAutoRegValue, vlanTestAPIOutputIndex=vlanTestAPIOutputIndex, vlanSystemEntry=vlanSystemEntry, sfpsVAPIVlanName=sfpsVAPIVlanName, vlanTestAPIOutputVlanId=vlanTestAPIOutputVlanId, vlanPortLayer3Learning=vlanPortLayer3Learning, vlanTestAPIOutputTap=vlanTestAPIOutputTap, vlanSystemLastChange=vlanSystemLastChange, vlanPortPortPolicy=vlanPortPortPolicy, sfpsVAPIPortPolicy=sfpsVAPIPortPolicy, vlanAMRRulesEntry=vlanAMRRulesEntry, vlanNameEntry=vlanNameEntry, sfpsVAPIFloodPolicy=sfpsVAPIFloodPolicy)
