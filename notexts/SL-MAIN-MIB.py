#
# PySNMP MIB module SL-MAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-MAIN-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:39 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, MibIdentifier, Gauge32, Unsigned32, Counter32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Opaque, Integer32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "MibIdentifier", "Gauge32", "Unsigned32", "Counter32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Opaque", "Integer32", "iso", "Counter64")
TimeStamp, TruthValue, RowStatus, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "RowStatus", "DateAndTime", "TextualConvention", "DisplayString")
slMain = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3))
if mibBuilder.loadTexts: slMain.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slMain.setOrganization('PacketLight Networks Ltd.')
slmSys = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1))
slmAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2))
slmAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 3))
slmLogin = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 4))
slmTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5))
slmLogFile = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 8))
slmConfigFile = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 9))
slmChPass = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 12))
slmLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 17))
class UserLogin(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class UserPassword(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class UserCommunity(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class SoftwareRevision(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class AdminAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("read", 1), ("readwrite", 2), ("provisioning", 3), ("admin", 4), ("trap", 5))

slmSysGatewayAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysGatewayAddr.setStatus('current')
slmSysSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysSubnetMask.setStatus('current')
slmSysIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysIpAddr.setStatus('current')
slmSysAlmAct = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysAlmAct.setStatus('current')
slmSysAlmDeact = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysAlmDeact.setStatus('current')
slmSysAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("warmBoot", 3), ("coldBoot", 4), ("factoryBoot", 5), ("testing", 6), ("hotBoot", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysAdminStatus.setStatus('current')
slmSysOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysOperStatus.setStatus('current')
slmBoxSize = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmBoxSize.setStatus('current')
slmSysCalendarTime = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 9), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysCalendarTime.setStatus('current')
slmSysPmStartOfDay = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysPmStartOfDay.setStatus('current')
slmSysActiveSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("swRevA", 1), ("swRevB", 2), ("swRevFtpStart", 3), ("swRevFtpEnd", 4), ("swRevAHot", 5), ("swRevBHot", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysActiveSwVersion.setStatus('current')
slmSwRevTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12), )
if mibBuilder.loadTexts: slmSwRevTable.setStatus('current')
slmConfigSysUptime = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmConfigSysUptime.setStatus('current')
slmConfigSysSignalType = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmConfigSysSignalType.setStatus('current')
slmRebootDelay = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmRebootDelay.setStatus('current')
slmVcatDelay = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmVcatDelay.setStatus('current')
slmTid = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmTid.setStatus('current')
slmPsuNumber = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmPsuNumber.setStatus('current')
slmOemType = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmOemType.setStatus('current')
slmSysName = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysName.setStatus('current')
slmSysLocation = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysLocation.setStatus('current')
slmSysResetPm = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysResetPm.setStatus('current')
slmSysUplinkRate = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up100", 1), ("up1000", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysUplinkRate.setStatus('current')
slmSysChassisId = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysChassisId.setStatus('current')
slmSysNetworkPrefix = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 26), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysNetworkPrefix.setStatus('current')
slmSysLanIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 27), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysLanIpAddr.setStatus('current')
slmSysLanSubnetAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 28), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysLanSubnetAddr.setStatus('current')
slmPmAvailable = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 29), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmPmAvailable.setStatus('current')
slmPortsNumber = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmPortsNumber.setStatus('current')
slmEdfaNumber = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmEdfaNumber.setStatus('current')
slmMuxNumber = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmMuxNumber.setStatus('current')
slmOpticalSwitchExist = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 33), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmOpticalSwitchExist.setStatus('current')
slmReadCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 34), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmReadCommunity.setStatus('current')
slmWriteCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 35), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmWriteCommunity.setStatus('current')
slmSysEffectiveSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 36), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysEffectiveSubnetMask.setStatus('current')
slmSysEffectiveIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 37), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysEffectiveIpAddr.setStatus('current')
slmSysLanEffectiveIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 38), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysLanEffectiveIpAddr.setStatus('current')
slmSysLanEffectiveSubnetAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 39), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysLanEffectiveSubnetAddr.setStatus('current')
slmSysGatewayEffectiveIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 40), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysGatewayEffectiveIpAddr.setStatus('current')
slmSysMode = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 41), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysMode.setStatus('current')
slmSysTrapFormat = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fullIfIndex", 1), ("portIfIndex", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysTrapFormat.setStatus('current')
slmSysTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysTemperature.setStatus('current')
slmNetworkMode = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("switching", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmNetworkMode.setStatus('current')
slm40GConf = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 100))).clone(namedValues=NamedValues(("g40", 0), ("g41", 1), ("g42", 2), ("g43", 3), ("g100", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slm40GConf.setStatus('current')
slmRstpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 46), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmRstpEnabled.setStatus('current')
slmTopologyEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 47), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmTopologyEnabled.setStatus('current')
slmAdminCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 48), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmAdminCommunity.setStatus('current')
slmTrapCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 49), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmTrapCommunity.setStatus('current')
slmSysSnmpVersion = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4))).clone(namedValues=NamedValues(("v3Only", 3), ("v1v2v3", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmSysSnmpVersion.setStatus('current')
slmSysEncryptionCapability = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSysEncryptionCapability.setStatus('current')
slmSwRevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmSwRevDirectory"))
if mibBuilder.loadTexts: slmSwRevEntry.setStatus('current')
slmSwRevDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("swRevDirA", 1), ("swRevDirB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSwRevDirectory.setStatus('current')
slmSwRevStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2), ("copyingToStandby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSwRevStatus.setStatus('current')
slmSwRevName = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 3), SoftwareRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSwRevName.setStatus('current')
slmSwRevDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmSwRevDate.setStatus('current')
slmAdminTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1), )
if mibBuilder.loadTexts: slmAdminTable.setStatus('current')
slmAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmAdminLogin"))
if mibBuilder.loadTexts: slmAdminEntry.setStatus('current')
slmAdminLogin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 3), UserLogin()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmAdminLogin.setStatus('current')
slmAdminPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 4), UserPassword()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmAdminPassword.setStatus('current')
slmAdminRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmAdminRowStatus.setStatus('current')
slmAdminAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 6), AdminAccess()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmAdminAccess.setStatus('current')
slmSnmpv3Auth = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noaccess", 1), ("noauth", 2), ("md5", 3), ("sha", 4), ("sha224", 5), ("sha256", 6), ("sha384", 7), ("sha512", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSnmpv3Auth.setStatus('current')
slmSnmpv3Priv = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noaccess", 1), ("nopriv", 2), ("des", 3), ("aes", 4), ("des3", 5), ("aes192", 6), ("aes256", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSnmpv3Priv.setStatus('current')
slmSnmpv3Password = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 9), UserPassword()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSnmpv3Password.setStatus('current')
slmAuthTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1), )
if mibBuilder.loadTexts: slmAuthTable.setStatus('current')
slmAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmAuthLogin"), (0, "SL-MAIN-MIB", "slmAuthPassword"))
if mibBuilder.loadTexts: slmAuthEntry.setStatus('current')
slmAuthLogin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1, 1), UserLogin())
if mibBuilder.loadTexts: slmAuthLogin.setStatus('current')
slmAuthPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1, 2), UserPassword())
if mibBuilder.loadTexts: slmAuthPassword.setStatus('current')
slmAuthCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1, 3), UserCommunity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmAuthCommunity.setStatus('current')
slmChPassTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1), )
if mibBuilder.loadTexts: slmChPassTable.setStatus('current')
slmChPassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmChPassLogin"), (0, "SL-MAIN-MIB", "slmChPassOldPass"))
if mibBuilder.loadTexts: slmChPassEntry.setStatus('current')
slmChPassLogin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1, 1), UserLogin())
if mibBuilder.loadTexts: slmChPassLogin.setStatus('current')
slmChPassOldPass = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1, 2), UserPassword())
if mibBuilder.loadTexts: slmChPassOldPass.setStatus('current')
slmChPassNewPass = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1, 3), UserPassword()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slmChPassNewPass.setStatus('current')
slmTrapDestTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1), )
if mibBuilder.loadTexts: slmTrapDestTable.setStatus('current')
slmTrapDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmTrapDestAddress"))
if mibBuilder.loadTexts: slmTrapDestEntry.setStatus('current')
slmTrapDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapDestAddress.setStatus('current')
slmTrapDestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapDestRowStatus.setStatus('current')
slmTrapDestCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 3), UserCommunity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapDestCommunity.setStatus('current')
slmTrapDestProtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("snmpVer1", 1), ("snmpVer2", 2), ("snmpVer3", 3))).clone('snmpVer2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapDestProtVersion.setStatus('current')
slmTrapUserLogin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 5), UserLogin()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapUserLogin.setStatus('current')
slmTrapUserAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 6), AdminAccess()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapUserAccess.setStatus('current')
slmTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapEnable.setStatus('current')
slmTrapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapPort.setStatus('current')
slmTrapDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmTrapDestIpAddress.setStatus('current')
slmTrapLogTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2), )
if mibBuilder.loadTexts: slmTrapLogTable.setStatus('current')
slmTrapLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmTrapLogId"))
if mibBuilder.loadTexts: slmTrapLogEntry.setStatus('current')
slmTrapLogId = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogId.setStatus('current')
slmTrapLogName = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogName.setStatus('current')
slmTrapLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogTimeStamp.setStatus('current')
slmTrapLogParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogParam1.setStatus('current')
slmTrapLogParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogParam2.setStatus('current')
slmTrapLogParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogParam3.setStatus('current')
slmTrapLogParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogParam4.setStatus('current')
slmTrapLogParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogParam5.setStatus('current')
slmTrapLogParam6 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmTrapLogParam6.setStatus('current')
slmTrapSoftwareStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 4)).setObjects(("SL-MAIN-MIB", "slmSwRevDirectory"), ("SL-MAIN-MIB", "slmSwRevStatus"))
if mibBuilder.loadTexts: slmTrapSoftwareStatusChange.setStatus('current')
slmTrapSysNameChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 5)).setObjects(("SL-MAIN-MIB", "slmSysName"))
if mibBuilder.loadTexts: slmTrapSysNameChange.setStatus('current')
slmTrapSysLocationChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 6)).setObjects(("SL-MAIN-MIB", "slmSysLocation"))
if mibBuilder.loadTexts: slmTrapSysLocationChange.setStatus('current')
slmSyslogDestTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7), )
if mibBuilder.loadTexts: slmSyslogDestTable.setStatus('current')
slmSyslogDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmSyslogDestAddress"))
if mibBuilder.loadTexts: slmSyslogDestEntry.setStatus('current')
slmSyslogDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSyslogDestAddress.setStatus('current')
slmSyslogDestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSyslogDestRowStatus.setStatus('current')
slmSyslogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("traps", 1), ("log", 2), ("debug", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSyslogLevel.setStatus('current')
slmSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSyslogPort.setStatus('current')
slmSyslogDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slmSyslogDestIpAddress.setStatus('current')
slmLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1), )
if mibBuilder.loadTexts: slmLicenseTable.setStatus('current')
slmLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1), ).setIndexNames((0, "SL-MAIN-MIB", "slmLicenseIndex"))
if mibBuilder.loadTexts: slmLicenseEntry.setStatus('current')
slmLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmLicenseIndex.setStatus('current')
slmLicenseExpiration = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmLicenseExpiration.setStatus('current')
slmLicenseId = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slmLicenseId.setStatus('current')
mibBuilder.exportSymbols("SL-MAIN-MIB", slmSysPmStartOfDay=slmSysPmStartOfDay, slmSwRevEntry=slmSwRevEntry, slmRebootDelay=slmRebootDelay, slmLogin=slmLogin, slmSnmpv3Auth=slmSnmpv3Auth, slmTid=slmTid, slmSysCalendarTime=slmSysCalendarTime, slmLicenseIndex=slmLicenseIndex, slmOemType=slmOemType, slmRstpEnabled=slmRstpEnabled, slmTrapSoftwareStatusChange=slmTrapSoftwareStatusChange, slmSysSnmpVersion=slmSysSnmpVersion, slmTrapUserLogin=slmTrapUserLogin, slmSysEffectiveIpAddr=slmSysEffectiveIpAddr, slmPsuNumber=slmPsuNumber, slmSysActiveSwVersion=slmSysActiveSwVersion, slmLicenseId=slmLicenseId, slmTrapPort=slmTrapPort, SoftwareRevision=SoftwareRevision, slmSysLanSubnetAddr=slmSysLanSubnetAddr, slmSwRevTable=slmSwRevTable, slmTrapEnable=slmTrapEnable, slmEdfaNumber=slmEdfaNumber, slmTrapLogEntry=slmTrapLogEntry, slmSyslogPort=slmSyslogPort, slmTrapLogParam2=slmTrapLogParam2, slmAdminPassword=slmAdminPassword, UserLogin=UserLogin, slmAdminTable=slmAdminTable, slmSysUplinkRate=slmSysUplinkRate, slmSnmpv3Priv=slmSnmpv3Priv, slmSysAdminStatus=slmSysAdminStatus, slmChPassNewPass=slmChPassNewPass, slmMuxNumber=slmMuxNumber, slmTrapDestAddress=slmTrapDestAddress, slmSwRevName=slmSwRevName, slmAuthEntry=slmAuthEntry, slmAuthLogin=slmAuthLogin, slmTrapDestRowStatus=slmTrapDestRowStatus, slmAdminRowStatus=slmAdminRowStatus, slm40GConf=slm40GConf, UserCommunity=UserCommunity, slmLicenseExpiration=slmLicenseExpiration, slmPortsNumber=slmPortsNumber, UserPassword=UserPassword, slmSysChassisId=slmSysChassisId, slmSyslogDestTable=slmSyslogDestTable, slmAdmin=slmAdmin, slMain=slMain, slmSyslogDestAddress=slmSyslogDestAddress, slmSysLocation=slmSysLocation, slmChPassLogin=slmChPassLogin, slmLicenseTable=slmLicenseTable, slmBoxSize=slmBoxSize, slmTrapCommunity=slmTrapCommunity, slmTrapDestCommunity=slmTrapDestCommunity, slmPmAvailable=slmPmAvailable, slmSysLanIpAddr=slmSysLanIpAddr, slmChPass=slmChPass, slmTrapUserAccess=slmTrapUserAccess, slmSwRevDirectory=slmSwRevDirectory, slmTrapDestIpAddress=slmTrapDestIpAddress, slmAdminEntry=slmAdminEntry, slmVcatDelay=slmVcatDelay, slmSyslogDestRowStatus=slmSyslogDestRowStatus, AdminAccess=AdminAccess, slmSysLanEffectiveIpAddr=slmSysLanEffectiveIpAddr, slmLicense=slmLicense, slmTrapSysNameChange=slmTrapSysNameChange, slmAuth=slmAuth, slmSysNetworkPrefix=slmSysNetworkPrefix, slmWriteCommunity=slmWriteCommunity, slmSysTemperature=slmSysTemperature, slmChPassOldPass=slmChPassOldPass, slmSysAlmAct=slmSysAlmAct, slmSysEncryptionCapability=slmSysEncryptionCapability, slmSysSubnetMask=slmSysSubnetMask, slmSyslogDestIpAddress=slmSyslogDestIpAddress, slmSnmpv3Password=slmSnmpv3Password, slmReadCommunity=slmReadCommunity, slmSysEffectiveSubnetMask=slmSysEffectiveSubnetMask, slmTrapLogId=slmTrapLogId, slmSysGatewayEffectiveIpAddr=slmSysGatewayEffectiveIpAddr, slmSysResetPm=slmSysResetPm, slmAuthPassword=slmAuthPassword, slmTrapLogTimeStamp=slmTrapLogTimeStamp, PYSNMP_MODULE_ID=slMain, slmLicenseEntry=slmLicenseEntry, slmTrap=slmTrap, slmLogFile=slmLogFile, slmAdminAccess=slmAdminAccess, slmTrapDestProtVersion=slmTrapDestProtVersion, slmOpticalSwitchExist=slmOpticalSwitchExist, slmTrapSysLocationChange=slmTrapSysLocationChange, slmSys=slmSys, slmConfigFile=slmConfigFile, slmChPassEntry=slmChPassEntry, slmSysIpAddr=slmSysIpAddr, slmTrapLogTable=slmTrapLogTable, slmSyslogLevel=slmSyslogLevel, slmSwRevDate=slmSwRevDate, slmConfigSysSignalType=slmConfigSysSignalType, slmAdminLogin=slmAdminLogin, slmTrapLogParam1=slmTrapLogParam1, slmConfigSysUptime=slmConfigSysUptime, slmChPassTable=slmChPassTable, slmSyslogDestEntry=slmSyslogDestEntry, slmSysGatewayAddr=slmSysGatewayAddr, slmNetworkMode=slmNetworkMode, slmTrapLogParam3=slmTrapLogParam3, slmSwRevStatus=slmSwRevStatus, slmSysName=slmSysName, slmSysMode=slmSysMode, slmTrapLogName=slmTrapLogName, slmTrapDestEntry=slmTrapDestEntry, slmSysTrapFormat=slmSysTrapFormat, slmAuthTable=slmAuthTable, slmSysAlmDeact=slmSysAlmDeact, slmTrapLogParam5=slmTrapLogParam5, slmTopologyEnabled=slmTopologyEnabled, slmTrapLogParam4=slmTrapLogParam4, slmSysLanEffectiveSubnetAddr=slmSysLanEffectiveSubnetAddr, slmSysOperStatus=slmSysOperStatus, slmTrapDestTable=slmTrapDestTable, slmAdminCommunity=slmAdminCommunity, slmAuthCommunity=slmAuthCommunity, slmTrapLogParam6=slmTrapLogParam6)
