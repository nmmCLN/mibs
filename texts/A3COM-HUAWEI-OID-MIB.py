#
# PySNMP MIB module A3COM-HUAWEI-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/3com/A3COM-HUAWEI-OID-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:05 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, MibIdentifier, Bits, Unsigned32, ModuleIdentity, TimeTicks, NotificationType, Counter64, IpAddress, enterprises, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "MibIdentifier", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "NotificationType", "Counter64", "IpAddress", "enterprises", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
jv_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45)).setLabel("jv-mib")
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1))
hwLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 1))
hwproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2))
huaweiMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5))
huaweiUtility = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6))
h3c = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10))
hwInternetProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 2))
lanSw = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23))
mlsr = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33))
dlsw = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34))
hwDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7))
hwMpls = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12))
hwpaeExtMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22))
huaweiDatacomm = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25))
hwDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1))
h3cCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2))
h3cEntityVendorTypeOID = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 3))
hwSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6))
h3cSNMPAgCpb = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7))
vrpProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3))
rmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4))
lswCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1))
hwQoS = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32))
h3cFtm = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1))
h3cUIMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2))
h3cEntityExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 6))
h3cIPSecMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7))
h3cAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 8))
h3cVoiceVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9))
h3cL4Redirect = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10))
h3cUser = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 12))
h3cRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13))
h3cPowerEthernetExt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 14))
h3cEntityRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15))
h3cProtocolVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16))
h3cQosProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17))
h3cNat = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 18))
h3cPos = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19))
h3cNS = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 20))
h3cAAL5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21))
h3cSSH = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22))
h3cRSA = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 23))
h3cVrrpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24))
h3cIpa = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25))
h3cPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 26))
h3cVpls = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 27))
h3cE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 28))
h3cT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29))
h3cIKEMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 30))
h3cWebSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 31))
h3cAutoDetect = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 32))
h3cIpBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33))
h3cIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 34))
h3cIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 35))
h3cDhcpSnoop = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 36))
h3cProtocolPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37))
h3cTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 38))
h3cVoice = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39))
h3cIfExt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 40))
h3cCfCard = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41))
h3cEpon = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42))
h3cDldp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 43))
h3cUnicast = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 44))
h3cRrpp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45))
h3cDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46))
h3cIds = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47))
h3cRcr = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48))
h3cAtmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49))
h3cMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 50))
h3cMpm = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51))
h3cOadp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 52))
h3cTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53))
h3cGre = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54))
h3cObjectInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55))
h3cDvpn = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 57))
h3cDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58))
h3cIsis = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 59))
h3cRpr = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60))
h3cSubnetVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61))
h3cDlswExt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62))
h3cSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 63))
h3cFlowTemplate = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64))
h3cQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65))
h3cStormConstrain = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66))
h3cIpAddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67))
h3cMirrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 68))
h3cQINQ = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69))
h3cTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70))
h3cIpv6AddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 71))
h3cBfdMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 72))
h3cRCP = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73))
h3cAcfp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 74))
h3cDot11 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75))
h3cE1T1VI = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76))
h3cwapiMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 77))
h3cL2VpnPwe3 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78))
h3cMplsOam = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 79))
h3cMplsOamPs = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 80))
h3cSiemMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 81))
h3cAFC = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85))
h3cMultCDR = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 86))
h3cMACInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87))
h3cFireWall = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88))
h3cDSP = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 89))
h3cNetMan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90))
h3cStack = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 91))
h3cPosa = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 92))
h3cWebAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93))
h3cLpbkdt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95))
h3cMultiMedia = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 96))
h3cDns = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97))
h3c3GModem = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98))
h3cPortal = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 99))
h3clldp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100))
h3cDHCPServer = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101))
h3cPPPoEServer = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102))
h3cL2Isolate = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103))
h3cSnmpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 104))
h3cVsi = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105))
h3cEvc = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106))
h3cMinm = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107))
h3cBlg = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108))
h3cRS485 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 109))
h3cARPRatelimit = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110))
h3cLI = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111))
h3cDar = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112))
h3cPBR = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113))
h3cAAANasId = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114))
h3cTeTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115))
h3cLB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116))
h3cDldp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117))
h3cWIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 118))
h3cFCoE = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120))
h3cQosCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1))
h3cIfQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1))
h3cCBQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2))
mibBuilder.exportSymbols("A3COM-HUAWEI-OID-MIB", lanSw=lanSw, h3cStormConstrain=h3cStormConstrain, h3cProtocolVlan=h3cProtocolVlan, h3cMACInformation=h3cMACInformation, h3cSubnetVlan=h3cSubnetVlan, h3cARPRatelimit=h3cARPRatelimit, rmonExtend=rmonExtend, hwLocal=hwLocal, h3cPBR=h3cPBR, h3cSnmpExt=h3cSnmpExt, h3cRpr=h3cRpr, h3clldp=h3clldp, h3cEntityExtend=h3cEntityExtend, hwDevice=hwDevice, h3cL2Isolate=h3cL2Isolate, h3cDhcpRelay=h3cDhcpRelay, h3cBlg=h3cBlg, h3cAAANasId=h3cAAANasId, huaweiUtility=huaweiUtility, hwSystem=hwSystem, h3cMultiMedia=h3cMultiMedia, huawei=huawei, h3cNat=h3cNat, hwMpls=hwMpls, h3cVoice=h3cVoice, hwQoS=hwQoS, h3cSyslog=h3cSyslog, h3cAcl=h3cAcl, h3cMpm=h3cMpm, h3cMinm=h3cMinm, h3c=h3c, vrpProtocol=vrpProtocol, h3cEntityVendorTypeOID=h3cEntityVendorTypeOID, h3cVpls=h3cVpls, h3cIPSecMonitor=h3cIPSecMonitor, h3cDldp=h3cDldp, h3cQosCapability=h3cQosCapability, h3cUIMgt=h3cUIMgt, h3cRcr=h3cRcr, h3cIpAddrMIB=h3cIpAddrMIB, huaweiMgmt=huaweiMgmt, h3cMplsOam=h3cMplsOam, h3cWebAuthentication=h3cWebAuthentication, h3cStack=h3cStack, h3cRS485=h3cRS485, h3cE1=h3cE1, lswCommon=lswCommon, h3cTrap=h3cTrap, h3cLpbkdt=h3cLpbkdt, h3cQos2=h3cQos2, h3cDns=h3cDns, h3cLI=h3cLI, h3cDhcpSnoop=h3cDhcpSnoop, h3cCBQos2=h3cCBQos2, h3cEvc=h3cEvc, h3cTransceiver=h3cTransceiver, h3cRCP=h3cRCP, h3cFlowTemplate=h3cFlowTemplate, h3cDomain=h3cDomain, h3cUnicast=h3cUnicast, huaweiDatacomm=huaweiDatacomm, h3cSNMPAgCpb=h3cSNMPAgCpb, h3cProtocolPriority=h3cProtocolPriority, h3cIpBroadcast=h3cIpBroadcast, h3cPowerEthernetExt=h3cPowerEthernetExt, h3cMplsOamPs=h3cMplsOamPs, h3cVoiceVlan=h3cVoiceVlan, h3cFCoE=h3cFCoE, h3cMulticast=h3cMulticast, h3cIPS=h3cIPS, h3cTunnel=h3cTunnel, h3cL4Redirect=h3cL4Redirect, h3cRadius=h3cRadius, h3cIsis=h3cIsis, router=router, hwInternetProtocol=hwInternetProtocol, h3cAcfp=h3cAcfp, h3cPortSecurity=h3cPortSecurity, h3cDar=h3cDar, h3cSSH=h3cSSH, h3cQosProfile=h3cQosProfile, h3cDvpn=h3cDvpn, h3cAFC=h3cAFC, h3cFireWall=h3cFireWall, h3cMultCDR=h3cMultCDR, h3cT1=h3cT1, h3cWIPS=h3cWIPS, h3cDHCPServer=h3cDHCPServer, mlsr=mlsr, h3cVrrpExt=h3cVrrpExt, hwDhcp=hwDhcp, h3cFtm=h3cFtm, h3cEntityRelation=h3cEntityRelation, h3cLB=h3cLB, h3cIds=h3cIds, h3cMirrGroup=h3cMirrGroup, h3cIfExt=h3cIfExt, h3cDSP=h3cDSP, h3cEpon=h3cEpon, h3cIpv6AddrMIB=h3cIpv6AddrMIB, h3cPortal=h3cPortal, h3cE1T1VI=h3cE1T1VI, h3cIpa=h3cIpa, h3cOadp=h3cOadp, h3cDot11=h3cDot11, h3cwapiMIB=h3cwapiMIB, jv_mib=jv_mib, h3cQINQ=h3cQINQ, h3cPPPoEServer=h3cPPPoEServer, h3cPosa=h3cPosa, h3cCommon=h3cCommon, h3c3GModem=h3c3GModem, h3cRSA=h3cRSA, h3cCfCard=h3cCfCard, h3cL2VpnPwe3=h3cL2VpnPwe3, h3cSiemMib=h3cSiemMib, h3cDldp2=h3cDldp2, h3cNS=h3cNS, dlsw=dlsw, h3cTeTunnel=h3cTeTunnel, a3Com=a3Com, h3cObjectInfo=h3cObjectInfo, h3cAAL5=h3cAAL5, h3cIKEMonitor=h3cIKEMonitor, h3cIpx=h3cIpx, hwpaeExtMib=hwpaeExtMib, h3cPos=h3cPos, h3cAutoDetect=h3cAutoDetect, hwproducts=hwproducts, h3cWebSwitch=h3cWebSwitch, h3cIfQos2=h3cIfQos2, h3cBfdMIB=h3cBfdMIB, h3cGre=h3cGre, h3cVsi=h3cVsi, h3cDlswExt=h3cDlswExt, h3cUser=h3cUser, h3cNetMan=h3cNetMan, h3cRrpp=h3cRrpp, h3cAtmDxi=h3cAtmDxi)
