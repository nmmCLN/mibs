#
# PySNMP MIB module SL-FT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-FT-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:53 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ifIndex, ifAlias = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifAlias")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ModuleIdentity, Counter32, ObjectIdentity, Bits, NotificationType, Unsigned32, IpAddress, TimeTicks, Counter64, MibIdentifier, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "NotificationType", "Unsigned32", "IpAddress", "TimeTicks", "Counter64", "MibIdentifier", "iso", "Integer32")
TruthValue, TextualConvention, RowPointer, DisplayString, RowStatus, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowPointer", "DisplayString", "RowStatus", "TimeStamp")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

slFt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30))
if mibBuilder.loadTexts: slFt.setLastUpdated('200007240000Z')
if mibBuilder.loadTexts: slFt.setOrganization('PacketLight Networks Ltd.')
slFtGen = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1))
slFtSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1))
slFtAgnt = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2))
slFtFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12))
class SftpUserLogin(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class SftpUserPassword(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

slFtFileServerIP = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileServerIP.setStatus('current')
slFtFileName = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileName.setStatus('current')
slFtFileTransCmd = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 255))).clone(namedValues=NamedValues(("swDwnLoad", 1), ("configDwnLoad", 2), ("configUpLoad", 3), ("coProcDwnLoad", 4), ("stateUpLoad", 5), ("dwnLoadUserFile", 6), ("upLoadUserFile", 7), ("swDwnLoadAndReset", 8), ("swUpLoad", 9), ("swDwnLoad2BkupStorage", 10), ("bootDwnLoad", 11), ("bootUpLoad", 12), ("swUpLoadFromBkupStorage", 13), ("licenseDwnLoad", 14), ("configDwnLoadToDefaultFile", 15), ("noOp", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransCmd.setStatus('current')
slFtTftpRetryTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtTftpRetryTimeOut.setStatus('current')
slFtTftpTotalTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtTftpTotalTimeOut.setStatus('current')
slFtTftpStatus = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noOp", 2), ("connecting", 3), ("transferringData", 4), ("endedTimeOut", 5), ("endedOk", 6), ("error", 7))).clone('noOp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtTftpStatus.setStatus('current')
slFtTftpError = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2).clone(hexValue="0000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: slFtTftpError.setStatus('current')
slFtFileTransferToSubSystems = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransferToSubSystems.setStatus('current')
slFtFileNameWithinProduct = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileNameWithinProduct.setStatus('current')
slFtFileTransferServerPort = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 14), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransferServerPort.setStatus('current')
slFtFileTransferProtocol = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tftp", 1), ("sftp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransferProtocol.setStatus('current')
slFtSftpUserLogin = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 16), SftpUserLogin()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtSftpUserLogin.setStatus('current')
slFtSftpPasswordLogin = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 17), SftpUserPassword()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtSftpPasswordLogin.setStatus('current')
slFtSystemReset = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("off", 2), ("on", 3), ("resetConfig", 4), ("resetMapping", 5), ("resetStandby", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtSystemReset.setStatus('current')
slFtAgnSwVersionSwapCmd = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("off", 2), ("mainAndBackup", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtAgnSwVersionSwapCmd.setStatus('current')
slFtSystemsEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1, 0))
if mibBuilder.loadTexts: slFtSystemsEvents.setStatus('current')
slFtTftpStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1, 0, 1)).setObjects(("SL-FT-MIB", "slFtTftpStatus"))
if mibBuilder.loadTexts: slFtTftpStatusChangeTrap.setStatus('current')
mibBuilder.exportSymbols("SL-FT-MIB", slFtSystems=slFtSystems, SftpUserLogin=SftpUserLogin, slFtTftpTotalTimeOut=slFtTftpTotalTimeOut, slFtFileName=slFtFileName, slFtFileTransfer=slFtFileTransfer, slFtFileTransCmd=slFtFileTransCmd, slFtTftpStatus=slFtTftpStatus, MacAddress=MacAddress, PYSNMP_MODULE_ID=slFt, slFtFileTransferToSubSystems=slFtFileTransferToSubSystems, slFtGen=slFtGen, slFtFileServerIP=slFtFileServerIP, slFtSystemReset=slFtSystemReset, slFtTftpError=slFtTftpError, slFtAgnt=slFtAgnt, slFtSystemsEvents=slFtSystemsEvents, slFtTftpStatusChangeTrap=slFtTftpStatusChangeTrap, slFt=slFt, slFtAgnSwVersionSwapCmd=slFtAgnSwVersionSwapCmd, slFtFileNameWithinProduct=slFtFileNameWithinProduct, slFtFileTransferServerPort=slFtFileTransferServerPort, SftpUserPassword=SftpUserPassword, slFtSftpUserLogin=slFtSftpUserLogin, slFtSftpPasswordLogin=slFtSftpPasswordLogin, slFtFileTransferProtocol=slFtFileTransferProtocol, slFtTftpRetryTimeOut=slFtTftpRetryTimeOut)
