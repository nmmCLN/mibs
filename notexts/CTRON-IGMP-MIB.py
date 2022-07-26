#
# PySNMP MIB module CTRON-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-IGMP-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:41 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ctIGMPBranch, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctIGMPBranch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanId, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ObjectIdentity, Counter64, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, TimeTicks, Gauge32, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Bits", "ModuleIdentity", "iso")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
ctIGMP = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1))
ctIGMP.setRevisions(('2005-05-09 20:30', '2005-03-15 20:38', '2003-12-10 14:56',))
if mibBuilder.loadTexts: ctIGMP.setLastUpdated('200505092030Z')
if mibBuilder.loadTexts: ctIGMP.setOrganization('Enterasys Networks, Inc')
class IgmpPortModeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("reporter", 1), ("source", 2))

class IgmpProtocolClassTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("multicastData", 1), ("routingProtocol", 2), ("ignore", 3))

class IgmpProtocolIdTc(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("hopopt", 0), ("icmp", 1), ("igmp", 2), ("ggp", 3), ("ip", 4), ("st", 5), ("tcp", 6), ("cbt", 7), ("egp", 8), ("igp", 9), ("bbnRccMon", 10), ("nvpII", 11), ("pup", 12), ("argus", 13), ("emcon", 14), ("xnet", 15), ("chaos", 16), ("udp", 17), ("mux", 18), ("dcnMeas", 19), ("hmp", 20), ("prm", 21), ("xnsIdp", 22), ("trunk1", 23), ("trunk2", 24), ("leaf1", 25), ("leaf2", 26), ("rdp", 27), ("irtp", 28), ("isoTp4", 29), ("netblt", 30), ("mfeNsp", 31), ("meritInp", 32), ("sep", 33), ("x3pc", 34), ("idpr", 35), ("xtp", 36), ("ddp", 37), ("idprCmtp", 38), ("tpPlusPlus", 39), ("il", 40), ("ipv6", 41), ("sdrp", 42), ("ipv6Route", 43), ("ipv6Frag", 44), ("idrp", 45), ("rsvp", 46), ("gre", 47), ("mhrp", 48), ("bna", 49), ("esp", 50), ("ah", 51), ("inlsp", 52), ("swipe", 53), ("narp", 54), ("mobile", 55), ("tlsp", 56), ("skip", 57), ("ipv6Icmp", 58), ("ipv6NoNxt", 59), ("ipv6Opts", 60), ("ipProt61", 61), ("cftp", 62), ("ipProt63", 63), ("satExpak", 64), ("kryptolan", 65), ("rvd", 66), ("ippc", 67), ("ipProt64", 68), ("satMon", 69), ("visa", 70), ("ipcv", 71), ("cpnx", 72), ("cphb", 73), ("wsn", 74), ("pvp", 75), ("brSatMon", 76), ("sunNd", 77), ("wbMon", 78), ("wbExpak", 79), ("isoIp", 80), ("vmtp", 81), ("secureVmtp", 82), ("vines", 83), ("ttp", 84), ("nsfnetIgp", 85), ("dgp", 86), ("tcf", 87), ("eigrp", 88), ("ospfIgp", 89), ("spriteRpc", 90), ("larp", 91), ("mtp", 92), ("ax25", 93), ("ipip", 94), ("micp", 95), ("sccSp", 96), ("etherIp", 97), ("encap", 98), ("ipProt99", 99), ("gmtp", 100), ("ifmp", 101), ("pnni", 102), ("pim", 103), ("aris", 104), ("scps", 105), ("qnx", 106), ("an", 107), ("ipComp", 108), ("snp", 109), ("compaqPeer", 110), ("ipxInIp", 111), ("vrrp", 112), ("pgm", 113), ("ipProt114", 114), ("l2tp", 115), ("ddx", 116), ("iatp", 117), ("stp", 118), ("srp", 119), ("uti", 120), ("smp", 121), ("sm", 122), ("ptp", 123), ("isisIpv4", 124), ("fire", 125), ("crtp", 126), ("crudp", 127), ("sscopmce", 128), ("iplt", 129), ("sps", 130), ("pipe", 131), ("sctp", 132), ("fc", 133), ("rsvpE2eIgn", 134), ("mobHeader", 135), ("udpLite", 136), ("mpls", 137), ("ipProto138", 138), ("ipProto139", 139), ("ipProto140", 140), ("ipProto141", 141), ("ipProto142", 142), ("ipProto143", 143), ("ipProto144", 144), ("ipProto145", 145), ("ipProto146", 146), ("ipProto147", 147), ("ipProto148", 148), ("ipProto149", 149), ("ipProto150", 150), ("ipProto151", 151), ("ipProto152", 152), ("ipProto153", 153), ("ipProto154", 154), ("ipProto155", 155), ("ipProto156", 156), ("ipProto157", 157), ("ipProto158", 158), ("ipProto159", 159), ("ipProto160", 160), ("ipProto161", 161), ("ipProto162", 162), ("ipProto163", 163), ("ipProto164", 164), ("ipProto165", 165), ("ipProto166", 166), ("ipProto167", 167), ("ipProto168", 168), ("ipProto169", 169), ("ipProto170", 170), ("ipProto171", 171), ("ipProto172", 172), ("ipProto173", 173), ("ipProto174", 174), ("ipProto175", 175), ("ipProto176", 176), ("ipProto177", 177), ("ipProto178", 178), ("ipProto179", 179), ("ipProto180", 180), ("ipProto181", 181), ("ipProto182", 182), ("ipProto183", 183), ("ipProto184", 184), ("ipProto185", 185), ("ipProto186", 186), ("ipProto187", 187), ("ipProto188", 188), ("ipProto189", 189), ("ipProto190", 190), ("ipProto191", 191), ("ipProto192", 192), ("ipProto193", 193), ("ipProto194", 194), ("ipProto195", 195), ("ipProto196", 196), ("ipProto197", 197), ("ipProto198", 198), ("ipProto199", 199), ("ipProto200", 200), ("ipProto201", 201), ("ipProto202", 202), ("ipProto203", 203), ("ipProto204", 204), ("ipProto205", 205), ("ipProto206", 206), ("ipProto207", 207), ("ipProto208", 208), ("ipProto209", 209), ("ipProto210", 210), ("ipProto211", 211), ("ipProto212", 212), ("ipProto213", 213), ("ipProto214", 214), ("ipProto215", 215), ("ipProto216", 216), ("ipProto217", 217), ("ipProto218", 218), ("ipProto219", 219), ("ipProto220", 220), ("ipProto221", 221), ("ipProto222", 222), ("ipProto223", 223), ("ipProto224", 224), ("ipProto225", 225), ("ipProto226", 226), ("ipProto227", 227), ("ipProto228", 228), ("ipProto229", 229), ("ipProto230", 230), ("ipProto231", 231), ("ipProto232", 232), ("ipProto233", 233), ("ipProto234", 234), ("ipProto235", 235), ("ipProto236", 236), ("ipProto237", 237), ("ipProto238", 238), ("ipProto239", 239), ("ipProto240", 240), ("ipProto241", 241), ("ipProto242", 242), ("ipProto243", 243), ("ipProto244", 244), ("ipProto245", 245), ("ipProto246", 246), ("ipProto247", 247), ("ipProto248", 248), ("ipProto249", 249), ("ipProto250", 250), ("ipProto251", 251), ("ipProto252", 252), ("ipProto253", 253), ("ipProto254", 254)) + NamedValues(("ipProto255", 255))

ctIGMPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1))
ctIGMPNewDefaultState = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIGMPNewDefaultState.setStatus('current')
ctIGMPMibRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPMibRev.setStatus('current')
ctIGMPMibRevString = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPMibRevString.setStatus('current')
ctIGMPConfigGroupTblFullAction = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routers", 1), ("flood", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIGMPConfigGroupTblFullAction.setStatus('current')
ctIGMPVlanTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2), )
if mibBuilder.loadTexts: ctIGMPVlanTable.setStatus('current')
ctIGMPVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPVlanId"))
if mibBuilder.loadTexts: ctIGMPVlanEntry.setStatus('current')
ctIGMPVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: ctIGMPVlanId.setStatus('current')
ctIGMPVlanQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 2), Integer32().clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPVlanQueryInterval.setStatus('current')
ctIGMPVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPVlanStatus.setStatus('current')
ctIGMPVlanVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2))).clone('version2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPVlanVersion.setStatus('current')
ctIGMPVlanQuerier = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPVlanQuerier.setStatus('current')
ctIGMPVlanQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPVlanQueryMaxResponseTime.setStatus('current')
ctIGMPVlanRobustness = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 7), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPVlanRobustness.setStatus('current')
ctIGMPVlanLastMembQueryIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 8), Integer32().clone(10)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPVlanLastMembQueryIntvl.setStatus('current')
ctIGMPVlanQuerierUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 9), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPVlanQuerierUpTime.setStatus('current')
ctIGMPVlanQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 10), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPVlanQuerierExpiryTime.setStatus('current')
ctIGMPVlanQuerierIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPVlanQuerierIP.setStatus('current')
ctIGMPCacheTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3), )
if mibBuilder.loadTexts: ctIGMPCacheTable.setStatus('current')
ctIGMPCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPCacheAddress"), (0, "CTRON-IGMP-MIB", "ctIGMPCacheVlanId"), (0, "CTRON-IGMP-MIB", "ctIGMPCacheIfIndex"))
if mibBuilder.loadTexts: ctIGMPCacheEntry.setStatus('current')
ctIGMPCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: ctIGMPCacheAddress.setStatus('current')
ctIGMPCacheVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 2), VlanId())
if mibBuilder.loadTexts: ctIGMPCacheVlanId.setStatus('current')
ctIGMPCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: ctIGMPCacheIfIndex.setStatus('current')
ctIGMPCacheLastReporter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPCacheLastReporter.setStatus('current')
ctIGMPCacheUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPCacheUpTime.setStatus('current')
ctIGMPCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPCacheExpiryTime.setStatus('current')
ctIGMPCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 7), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPCacheVersion1HostTimer.setStatus('current')
ctIGMPPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4), )
if mibBuilder.loadTexts: ctIGMPPolicyTable.setStatus('deprecated')
ctIGMPPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPPolicyAddress"), (0, "CTRON-IGMP-MIB", "ctIGMPPolicyVlanId"), (0, "CTRON-IGMP-MIB", "ctIGMPPolicyIfIndex"))
if mibBuilder.loadTexts: ctIGMPPolicyEntry.setStatus('deprecated')
ctIGMPPolicyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: ctIGMPPolicyAddress.setStatus('deprecated')
ctIGMPPolicyVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: ctIGMPPolicyVlanId.setStatus('deprecated')
ctIGMPPolicyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: ctIGMPPolicyIfIndex.setStatus('deprecated')
ctIGMPPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPPolicyStatus.setStatus('deprecated')
ctIGMPPolicyInclusion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2))).clone('exclude')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPPolicyInclusion.setStatus('deprecated')
ctIGMPStaticTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5), )
if mibBuilder.loadTexts: ctIGMPStaticTable.setStatus('deprecated')
ctIGMPStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupAddress"), (0, "CTRON-IGMP-MIB", "ctIGMPStaticVlanId"))
if mibBuilder.loadTexts: ctIGMPStaticEntry.setStatus('deprecated')
ctIGMPStaticGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: ctIGMPStaticGroupAddress.setStatus('deprecated')
ctIGMPStaticVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: ctIGMPStaticVlanId.setStatus('deprecated')
ctIGMPStaticOutPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIGMPStaticOutPortList.setStatus('deprecated')
ctIGMPStaticRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPStaticRowStatus.setStatus('deprecated')
ctIGMPStaticGroupTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6), )
if mibBuilder.loadTexts: ctIGMPStaticGroupTable.setStatus('current')
ctIGMPStaticGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupIPAddress"), (0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupVlanId"), (0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupSourceIPAddress"))
if mibBuilder.loadTexts: ctIGMPStaticGroupEntry.setStatus('current')
ctIGMPStaticGroupIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: ctIGMPStaticGroupIPAddress.setStatus('current')
ctIGMPStaticGroupVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 2), VlanId())
if mibBuilder.loadTexts: ctIGMPStaticGroupVlanId.setStatus('current')
ctIGMPStaticGroupSourceIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: ctIGMPStaticGroupSourceIPAddress.setStatus('current')
ctIGMPStaticGroupIncludeList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIGMPStaticGroupIncludeList.setStatus('current')
ctIGMPStaticGroupExcludeList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIGMPStaticGroupExcludeList.setStatus('current')
ctIGMPStaticGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctIGMPStaticGroupRowStatus.setStatus('current')
ctIGMPExtCacheTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7), )
if mibBuilder.loadTexts: ctIGMPExtCacheTable.setStatus('current')
ctIGMPExtCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPExtCacheAddress"), (0, "CTRON-IGMP-MIB", "ctIGMPExtCacheVlanId"), (0, "CTRON-IGMP-MIB", "ctIGMPExtCacheSourceIPAddress"))
if mibBuilder.loadTexts: ctIGMPExtCacheEntry.setStatus('current')
ctIGMPExtCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 1), IpAddress())
if mibBuilder.loadTexts: ctIGMPExtCacheAddress.setStatus('current')
ctIGMPExtCacheVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 2), VlanId())
if mibBuilder.loadTexts: ctIGMPExtCacheVlanId.setStatus('current')
ctIGMPExtCacheSourceIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 3), IpAddress())
if mibBuilder.loadTexts: ctIGMPExtCacheSourceIPAddress.setStatus('current')
ctIGMPExtCacheLastReporter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPExtCacheLastReporter.setStatus('current')
ctIGMPExtCacheUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPExtCacheUpTime.setStatus('current')
ctIGMPExtCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPExtCacheExpiryTime.setStatus('current')
ctIGMPExtCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 7), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPExtCacheVersion1HostTimer.setStatus('current')
ctIGMPExtCacheOutPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 8), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPExtCacheOutPortList.setStatus('current')
ctIGMPExtCacheSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPExtCacheSrcPort.setStatus('current')
ctIGMPDiscoveredRouterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8), )
if mibBuilder.loadTexts: ctIGMPDiscoveredRouterTable.setStatus('current')
ctIGMPDiscoveredRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPDiscoveredRouterVlanId"))
if mibBuilder.loadTexts: ctIGMPDiscoveredRouterEntry.setStatus('current')
ctIGMPDiscoveredRouterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 2), VlanId())
if mibBuilder.loadTexts: ctIGMPDiscoveredRouterVlanId.setStatus('current')
ctIGMPDiscoveredRouterPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPDiscoveredRouterPortList.setStatus('current')
ctIGMPDiscoveredRouterEgressPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPDiscoveredRouterEgressPortList.setStatus('current')
ctIGMPDiscoveredRouterStaticPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIGMPDiscoveredRouterStaticPortList.setStatus('current')
ctIGMPPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9), )
if mibBuilder.loadTexts: ctIGMPPortTable.setStatus('current')
ctIGMPPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPPortMode"), (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "CTRON-IGMP-MIB", "ctIGMPPortTableGroupAddress"), (0, "CTRON-IGMP-MIB", "ctIGMPPortTableVlanId"), (0, "CTRON-IGMP-MIB", "ctIGMPPortTableSourceIPAddress"))
if mibBuilder.loadTexts: ctIGMPPortTableEntry.setStatus('current')
ctIGMPPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 1), IgmpPortModeTc())
if mibBuilder.loadTexts: ctIGMPPortMode.setStatus('current')
ctIGMPPortTableGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 2), IpAddress())
if mibBuilder.loadTexts: ctIGMPPortTableGroupAddress.setStatus('current')
ctIGMPPortTableVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 3), VlanId())
if mibBuilder.loadTexts: ctIGMPPortTableVlanId.setStatus('current')
ctIGMPPortTableSourceIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 4), IpAddress())
if mibBuilder.loadTexts: ctIGMPPortTableSourceIPAddress.setStatus('current')
ctIGMPPortTableExpireTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 5), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPPortTableExpireTime.setStatus('current')
ctIGMPStatsCntrs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10))
ctIGMPStatsCntrsGroupFull = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsGroupFull.setStatus('current')
ctIGMPStatsCntrsNumV1QueriesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumV1QueriesSent.setStatus('current')
ctIGMPStatsCntrsNumV2QueriesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumV2QueriesSent.setStatus('current')
ctIGMPStatsCntrsNumV3QueriesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumV3QueriesSent.setStatus('current')
ctIGMPStatsCntrsNumGSQueriesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumGSQueriesSent.setStatus('current')
ctIGMPStatsCntrsNumQueriesRcvd = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumQueriesRcvd.setStatus('current')
ctIGMPStatsCntrsNumV1ReportsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumV1ReportsRcvd.setStatus('current')
ctIGMPStatsCntrsNumV2ReportsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumV2ReportsRcvd.setStatus('current')
ctIGMPStatsCntrsNumV3ReportsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumV3ReportsReceived.setStatus('current')
ctIGMPStatsCntrsNumLeavesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumLeavesReceived.setStatus('current')
ctIGMPStatsCntrsNumDroppedFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIGMPStatsCntrsNumDroppedFrames.setStatus('current')
ctIGMPProtocolClassificationTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11), )
if mibBuilder.loadTexts: ctIGMPProtocolClassificationTable.setStatus('current')
ctIGMPProtocolClassificationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11, 1), ).setIndexNames((0, "CTRON-IGMP-MIB", "ctIGMPProtocolClassification"))
if mibBuilder.loadTexts: ctIGMPProtocolClassificationEntry.setStatus('current')
ctIGMPProtocolClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11, 1, 1), IgmpProtocolClassTc())
if mibBuilder.loadTexts: ctIGMPProtocolClassification.setStatus('current')
ctIGMPProtocolIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11, 1, 2), IgmpProtocolIdTc()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIGMPProtocolIdentifier.setStatus('current')
mibBuilder.exportSymbols("CTRON-IGMP-MIB", ctIGMPExtCacheVersion1HostTimer=ctIGMPExtCacheVersion1HostTimer, ctIGMPPortTableVlanId=ctIGMPPortTableVlanId, ctIGMPPortMode=ctIGMPPortMode, ctIGMPPolicyVlanId=ctIGMPPolicyVlanId, ctIGMPStatsCntrsNumQueriesRcvd=ctIGMPStatsCntrsNumQueriesRcvd, ctIGMP=ctIGMP, ctIGMPStaticVlanId=ctIGMPStaticVlanId, ctIGMPVlanLastMembQueryIntvl=ctIGMPVlanLastMembQueryIntvl, ctIGMPStaticGroupAddress=ctIGMPStaticGroupAddress, ctIGMPNewDefaultState=ctIGMPNewDefaultState, ctIGMPExtCacheVlanId=ctIGMPExtCacheVlanId, ctIGMPPortTableSourceIPAddress=ctIGMPPortTableSourceIPAddress, ctIGMPExtCacheTable=ctIGMPExtCacheTable, ctIGMPExtCacheUpTime=ctIGMPExtCacheUpTime, ctIGMPPortTableEntry=ctIGMPPortTableEntry, ctIGMPVlanStatus=ctIGMPVlanStatus, ctIGMPExtCacheSourceIPAddress=ctIGMPExtCacheSourceIPAddress, ctIGMPExtCacheOutPortList=ctIGMPExtCacheOutPortList, ctIGMPStatsCntrsNumV1ReportsRcvd=ctIGMPStatsCntrsNumV1ReportsRcvd, ctIGMPCacheVlanId=ctIGMPCacheVlanId, ctIGMPStaticRowStatus=ctIGMPStaticRowStatus, ctIGMPCacheIfIndex=ctIGMPCacheIfIndex, ctIGMPVlanId=ctIGMPVlanId, ctIGMPCacheTable=ctIGMPCacheTable, ctIGMPStaticOutPortList=ctIGMPStaticOutPortList, ctIGMPVlanQuerierExpiryTime=ctIGMPVlanQuerierExpiryTime, ctIGMPVlanVersion=ctIGMPVlanVersion, ctIGMPStaticGroupIncludeList=ctIGMPStaticGroupIncludeList, ctIGMPStatsCntrsNumDroppedFrames=ctIGMPStatsCntrsNumDroppedFrames, ctIGMPStatsCntrsNumV3QueriesSent=ctIGMPStatsCntrsNumV3QueriesSent, ctIGMPProtocolClassificationTable=ctIGMPProtocolClassificationTable, ctIGMPProtocolClassificationEntry=ctIGMPProtocolClassificationEntry, ctIGMPStaticGroupVlanId=ctIGMPStaticGroupVlanId, ctIGMPStatsCntrsNumV3ReportsReceived=ctIGMPStatsCntrsNumV3ReportsReceived, ctIGMPProtocolClassification=ctIGMPProtocolClassification, ctIGMPCacheAddress=ctIGMPCacheAddress, ctIGMPDiscoveredRouterVlanId=ctIGMPDiscoveredRouterVlanId, ctIGMPStaticGroupTable=ctIGMPStaticGroupTable, ctIGMPConfig=ctIGMPConfig, ctIGMPVlanQueryInterval=ctIGMPVlanQueryInterval, ctIGMPExtCacheAddress=ctIGMPExtCacheAddress, ctIGMPCacheUpTime=ctIGMPCacheUpTime, ctIGMPExtCacheSrcPort=ctIGMPExtCacheSrcPort, ctIGMPStatsCntrsNumGSQueriesSent=ctIGMPStatsCntrsNumGSQueriesSent, PYSNMP_MODULE_ID=ctIGMP, ctIGMPVlanEntry=ctIGMPVlanEntry, ctIGMPPolicyIfIndex=ctIGMPPolicyIfIndex, ctIGMPStatsCntrs=ctIGMPStatsCntrs, ctIGMPCacheExpiryTime=ctIGMPCacheExpiryTime, ctIGMPDiscoveredRouterTable=ctIGMPDiscoveredRouterTable, IgmpPortModeTc=IgmpPortModeTc, ctIGMPVlanQuerierIP=ctIGMPVlanQuerierIP, ctIGMPVlanRobustness=ctIGMPVlanRobustness, ctIGMPDiscoveredRouterStaticPortList=ctIGMPDiscoveredRouterStaticPortList, ctIGMPPortTableGroupAddress=ctIGMPPortTableGroupAddress, ctIGMPStaticGroupEntry=ctIGMPStaticGroupEntry, ctIGMPStatsCntrsNumV2QueriesSent=ctIGMPStatsCntrsNumV2QueriesSent, ctIGMPExtCacheEntry=ctIGMPExtCacheEntry, ctIGMPStaticGroupExcludeList=ctIGMPStaticGroupExcludeList, ctIGMPPolicyTable=ctIGMPPolicyTable, ctIGMPStaticEntry=ctIGMPStaticEntry, ctIGMPDiscoveredRouterEntry=ctIGMPDiscoveredRouterEntry, IgmpProtocolClassTc=IgmpProtocolClassTc, ctIGMPVlanQueryMaxResponseTime=ctIGMPVlanQueryMaxResponseTime, ctIGMPVlanQuerierUpTime=ctIGMPVlanQuerierUpTime, ctIGMPPolicyInclusion=ctIGMPPolicyInclusion, ctIGMPDiscoveredRouterPortList=ctIGMPDiscoveredRouterPortList, ctIGMPStatsCntrsNumV2ReportsRcvd=ctIGMPStatsCntrsNumV2ReportsRcvd, ctIGMPCacheLastReporter=ctIGMPCacheLastReporter, ctIGMPMibRevString=ctIGMPMibRevString, ctIGMPConfigGroupTblFullAction=ctIGMPConfigGroupTblFullAction, ctIGMPStatsCntrsGroupFull=ctIGMPStatsCntrsGroupFull, ctIGMPVlanTable=ctIGMPVlanTable, ctIGMPStaticGroupRowStatus=ctIGMPStaticGroupRowStatus, ctIGMPPolicyEntry=ctIGMPPolicyEntry, ctIGMPStatsCntrsNumLeavesReceived=ctIGMPStatsCntrsNumLeavesReceived, ctIGMPExtCacheExpiryTime=ctIGMPExtCacheExpiryTime, ctIGMPExtCacheLastReporter=ctIGMPExtCacheLastReporter, ctIGMPCacheVersion1HostTimer=ctIGMPCacheVersion1HostTimer, ctIGMPPortTable=ctIGMPPortTable, ctIGMPPolicyAddress=ctIGMPPolicyAddress, ctIGMPVlanQuerier=ctIGMPVlanQuerier, ctIGMPMibRev=ctIGMPMibRev, ctIGMPPortTableExpireTime=ctIGMPPortTableExpireTime, ctIGMPStatsCntrsNumV1QueriesSent=ctIGMPStatsCntrsNumV1QueriesSent, IgmpProtocolIdTc=IgmpProtocolIdTc, ctIGMPPolicyStatus=ctIGMPPolicyStatus, ctIGMPCacheEntry=ctIGMPCacheEntry, ctIGMPStaticGroupIPAddress=ctIGMPStaticGroupIPAddress, ctIGMPStaticTable=ctIGMPStaticTable, ctIGMPStaticGroupSourceIPAddress=ctIGMPStaticGroupSourceIPAddress, ctIGMPDiscoveredRouterEgressPortList=ctIGMPDiscoveredRouterEgressPortList, ctIGMPProtocolIdentifier=ctIGMPProtocolIdentifier)
