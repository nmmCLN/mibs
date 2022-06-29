#
# PySNMP MIB module CM-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-COMMON-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:50 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Gauge32, Counter32, IpAddress, iso, ModuleIdentity, ObjectIdentity, Unsigned32, MibIdentifier, Bits, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Gauge32", "Counter32", "IpAddress", "iso", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Bits", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1))
cmCommonMIB.setRevisions(('2021-01-27 00:00',))
if mibBuilder.loadTexts: cmCommonMIB.setLastUpdated('202101270000Z')
if mibBuilder.loadTexts: cmCommonMIB.setOrganization('ADVA Optical Networking SE')
subproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1))
f3Capabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2))
nemihubshelf = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 1))
ge101 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 2))
ge206 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 3))
ge201 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 4))
ge201se = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 5))
ge206f = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 6))
cmagg = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 7))
ge112 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 8))
ge114 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 9))
ge206v = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 10))
xg210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 11))
t1804 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 12))
t3204 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 13))
gesyncprobe = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 14))
ge114H = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 15))
ge114PH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 16))
ge114S = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 17))
ge114SH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 18))
sh1pcs = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 19))
ge112Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 20))
ge112ProM = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 21))
ge114Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 22))
ge114ProC = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 23))
ge114ProSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 24))
ge114ProCSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 25))
ge114ProHE = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 26))
xg210c = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 27))
ge112ProH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 28))
ge114G = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 29))
ge114ProVMH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 30))
ge114ProVMCH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 31))
ge114ProVMCSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 32))
ge112ProVM = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 33))
ge101Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 34))
go102ProS = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 35))
go102ProSP = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 36))
cx101Pro30A = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 37))
cx102Pro30A = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 38))
xg116Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 39))
xg120Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 40))
xg116ProH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 41))
ge102ProH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 42))
ge102ProEFMH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 43))
go102ProSM = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 44))
xg118ProSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 45))
xg118ProacSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 46))
ge114ProVMSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 47))
ge104 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 48))
xg120ProSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 49))
class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eth-access", 1), ("eth-network", 2))

class TrafficDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("a2n", 1), ("n2a", 2), ("ingress", 3), ("egress", 4), ("n2n", 5))

class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class VlanPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class VlanTagType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("inner-vlantag", 1), ("outer-vlantag", 2), ("n2a-priorityMapping", 3), ("mplsLabel", 4), ("vcLabel", 5), ("encapOuterVlanTag", 6))

class AdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("in-service", 1), ("management", 2), ("maintenance", 3), ("disabled", 4), ("unassigned", 5), ("monitored", 6))

class OperationalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("outage", 2))

class SecondaryState(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("not-applicable", 0), ("active", 1), ("automaticinservice", 2), ("facilityfailure", 3), ("fault", 4), ("loopback", 5), ("maintenance", 6), ("mismatchedeqpt", 7), ("standbyhot", 8), ("supportingentityoutage", 9), ("unassigned", 10), ("unequipped", 11), ("disabled", 12), ("forcedoffline", 13), ("initializing", 14), ("prtcl", 15), ("blckd", 16), ("mon-tx", 17), ("mir-rx", 18), ("cema", 19), ("lkdo", 20), ("nomber", 21))

class EthernetPortSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("speed-unknown", 0), ("speed-10MB-full", 1), ("speed-10MB-half", 2), ("speed-100MB-full", 3), ("speed-100MB-half", 4), ("speed-1000MB-full", 5), ("speed-1000MB-half", 6), ("speed-auto", 7), ("speed-auto-10MB-full", 8), ("speed-auto-10MB-half", 9), ("speed-auto-100MB-full", 10), ("speed-auto-100MB-half", 11), ("speed-auto-1000MB-full", 12), ("speed-auto-1000MB-half", 13), ("speed-negotiating", 14), ("speed-auto-1000MB-full-master", 15), ("speed-auto-1000MB-full-slave", 16), ("speed-none", 17), ("speed-auto-1000MB-full-master-preferred", 18), ("speed-auto-1000MB-full-slave-preferred", 19), ("speed-10G-full", 20), ("speed-auto-detect", 21))

class EthernetMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("not-applicable", 0), ("copper", 1), ("fiber", 2), ("coppersfp", 3), ("auto", 4), ("none", 5), ("xdsl", 6), ("vmServerBackplane", 7))

class PerfCounter64(TextualConvention, Counter64):
    status = 'current'

class PerfCounter32(TextualConvention, Counter32):
    status = 'current'

class IpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class IpPriorityMapMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("not-applicable", 0), ("none", 1), ("priomap-tos", 2), ("priomap-dscp", 3))

class PriorityMapMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("priomap-none", 1), ("priomap-tos", 2), ("priomap-dscp", 3), ("priomap-8021p", 4), ("priomap-8021p-inner", 5), ("priomap-exp", 6), ("priomap-exp-inner", 7))

class SfpConnectorValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("not-applicable", 0), ("unknown", 1), ("sc", 2), ("fcs1cu", 3), ("fcs2cu", 4), ("bnc-tnc", 5), ("fccoaxhdr", 6), ("fjack", 7), ("lc", 8), ("mt-rj", 9), ("mu", 10), ("sg", 11), ("optpigtail", 12), ("hssdc", 13), ("cupigtail", 14), ("vendorspecific", 15), ("rj45", 16))

class SfpIdentifierValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("notApplicable", 0), ("unknown", 1), ("gbic", 2), ("modsol", 3), ("sfp", 4), ("xbi300pin", 5), ("xenpak", 6), ("xfp", 7), ("xff", 8), ("xfpE", 9), ("xpak", 10), ("x2", 11), ("vendorSpecific", 12))

class RestartType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("not-applicable", 0), ("warm-start", 1), ("cold-start", 2), ("boot-maintenance", 3), ("boot-normal", 4), ("boot-pxe", 5))

class SfpMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("not-applicable", 0), ("singlemode", 1), ("multimode", 2), ("multimode62-5", 3), ("copper", 4))

class ScheduleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("periodic", 1), ("one-shot", 2))

class SchedActivityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("initial", 1), ("active", 2), ("suspended", 3), ("completed", 4))

class SchedActivityAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("suspend", 1), ("resume", 2))

class MepDestinationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("mepid", 1), ("macaddress", 2))

class ClassOfServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("cos-not-applicable", 0), ("cos-zero", 1), ("cos-one", 2), ("cos-two", 3), ("cos-three", 4), ("cos-four", 5), ("cos-five", 6), ("cos-six", 7), ("cos-seven", 8))

class SignalDirectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

class AfpTagControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ctag", 1), ("stag", 2), ("both", 3))

class CmP2PFlowType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("eline", 1))

class CmTrafficACLPriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("acl-tos", 1), ("acl-dscp", 2))

class CmTrafficAclFilterActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("permit", 1), ("deny", 2))

class CmTrafficAclFilterType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ipv4", 2), ("ipv6", 3))

class CmTrafficAclProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("tcp", 1), ("udp", 2))

class VlanEthertype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cvlan", 1), ("svlan", 2))

class CmPmBinAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("not-applicable", 0), ("clear", 1))

class CmPmIntervalType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("interval-15min", 1), ("interval-1day", 2), ("rollover", 3), ("interval-5min", 4))

class TDMFrequencySourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("loopTiming", 1), ("systemTiming", 2), ("lineTiming", 3))

class F3DisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2047a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2047)

class Decimal32(TextualConvention, Unsigned32):
    status = 'current'

class UserInterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cli", 1), ("gui", 2), ("netconf", 3), ("snmp", 4))

class FlowSecState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("secureNormal", 1), ("secureBlocked", 2), ("unsecureNormal", 3), ("unsecureBlocked", 4))

class UsbOperationalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cellular-modem", 1), ("srv-access", 2), ("nte-access", 3))

mibBuilder.exportSymbols("CM-COMMON-MIB", IpPriorityMapMode=IpPriorityMapMode, ge114ProCSH=ge114ProCSH, ge206f=ge206f, xg118ProacSH=xg118ProacSH, ge114=ge114, MepDestinationType=MepDestinationType, F3DisplayString=F3DisplayString, sh1pcs=sh1pcs, ge112ProVM=ge112ProVM, CmTrafficAclProtocolType=CmTrafficAclProtocolType, OperationalState=OperationalState, ge114ProVMH=ge114ProVMH, ge114ProVMCH=ge114ProVMCH, EthernetPortSpeed=EthernetPortSpeed, xg120ProSH=xg120ProSH, SchedActivityAction=SchedActivityAction, TDMFrequencySourceType=TDMFrequencySourceType, ge112=ge112, PriorityMapMode=PriorityMapMode, SignalDirectionType=SignalDirectionType, ge114PH=ge114PH, ge201se=ge201se, go102ProS=go102ProS, SfpMediaType=SfpMediaType, PerfCounter32=PerfCounter32, xg120Pro=xg120Pro, ScheduleType=ScheduleType, xg210c=xg210c, ge112Pro=ge112Pro, go102ProSM=go102ProSM, UsbOperationalMode=UsbOperationalMode, ge114H=ge114H, subproducts=subproducts, CmPmIntervalType=CmPmIntervalType, ge201=ge201, CmTrafficACLPriorityType=CmTrafficACLPriorityType, ge101Pro=ge101Pro, IpVersion=IpVersion, CmPmBinAction=CmPmBinAction, cmCommonMIB=cmCommonMIB, AfpTagControl=AfpTagControl, Decimal32=Decimal32, xg118ProSH=xg118ProSH, ge206=ge206, CmTrafficAclFilterType=CmTrafficAclFilterType, ClassOfServiceType=ClassOfServiceType, cmagg=cmagg, FlowSecState=FlowSecState, PortType=PortType, VlanPriority=VlanPriority, go102ProSP=go102ProSP, SecondaryState=SecondaryState, ge114G=ge114G, ge114ProHE=ge114ProHE, cx101Pro30A=cx101Pro30A, ge114ProVMSH=ge114ProVMSH, ge114ProC=ge114ProC, f3Capabilities=f3Capabilities, CmP2PFlowType=CmP2PFlowType, nemihubshelf=nemihubshelf, SfpIdentifierValue=SfpIdentifierValue, EthernetMediaType=EthernetMediaType, VlanId=VlanId, ge104=ge104, ge114SH=ge114SH, ge102ProEFMH=ge102ProEFMH, VlanEthertype=VlanEthertype, t1804=t1804, RestartType=RestartType, xg210=xg210, t3204=t3204, SchedActivityStatus=SchedActivityStatus, CmTrafficAclFilterActionType=CmTrafficAclFilterActionType, PYSNMP_MODULE_ID=cmCommonMIB, ge114S=ge114S, ge114Pro=ge114Pro, ge102ProH=ge102ProH, xg116ProH=xg116ProH, ge101=ge101, PerfCounter64=PerfCounter64, ge112ProM=ge112ProM, ge114ProSH=ge114ProSH, VlanTagType=VlanTagType, TrafficDirection=TrafficDirection, ge206v=ge206v, cx102Pro30A=cx102Pro30A, ge112ProH=ge112ProH, xg116Pro=xg116Pro, UserInterfaceType=UserInterfaceType, ge114ProVMCSH=ge114ProVMCSH, SfpConnectorValue=SfpConnectorValue, AdminState=AdminState, gesyncprobe=gesyncprobe)
