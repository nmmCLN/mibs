#
# PySNMP MIB module CTFPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTFPS-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:41 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ctFPS, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFPS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Counter64, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, TimeTicks, MibIdentifier, Gauge32, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "TimeTicks", "MibIdentifier", "Gauge32", "Bits", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fpsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1))
fpsSystemSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsSystemSlotNum.setStatus('mandatory')
fpsSystemMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bridge", 1), ("switch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsSystemMode.setStatus('mandatory')
fpsMaxPktRam = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsMaxPktRam.setStatus('mandatory')
fpsFreePktRam = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsFreePktRam.setStatus('mandatory')
fpsOperTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsOperTime.setStatus('mandatory')
fpsInPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsInPkts.setStatus('mandatory')
fpsOutPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsOutPkts.setStatus('mandatory')
fpsInOctets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsInOctets.setStatus('mandatory')
fpsOutOctets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsOutOctets.setStatus('mandatory')
fpsPort = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2))
fpsActivePorts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsActivePorts.setStatus('mandatory')
fpsMaxPortNum = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsMaxPortNum.setStatus('mandatory')
fpsPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3), )
if mibBuilder.loadTexts: fpsPortTable.setStatus('mandatory')
fpsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1), ).setIndexNames((0, "CTFPS-MIB", "fpsPortNum"))
if mibBuilder.loadTexts: fpsPortEntry.setStatus('mandatory')
fpsPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortNum.setStatus('mandatory')
fpsPortIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortIfNum.setStatus('mandatory')
fpsPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ether", 1), ("tokenRing", 2), ("inb", 3), ("fddi", 4), ("host", 5), ("atm", 6), ("wan", 7), ("other", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortType.setStatus('mandatory')
fpsPortClusterNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortClusterNum.setStatus('mandatory')
fpsPortTotalAvailQueDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortTotalAvailQueDepth.setStatus('mandatory')
fpsPortMaxQueDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortMaxQueDepth.setStatus('mandatory')
fpsPortCurrentQueDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortCurrentQueDepth.setStatus('mandatory')
fpsPortBandwidthRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortBandwidthRequested.setStatus('mandatory')
fpsPortBandwidthAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortBandwidthAllocated.setStatus('mandatory')
fpsPortXmitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortXmitStatus.setStatus('mandatory')
fpsPortFwdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortFwdStatus.setStatus('mandatory')
fpsPortLearningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortLearningStatus.setStatus('mandatory')
fpsPortUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortUnknownStatus.setStatus('mandatory')
fpsPortBroadcastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortBroadcastStatus.setStatus('mandatory')
fpsPortViolationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortViolationStatus.setStatus('mandatory')
fpsPortCopyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortCopyStatus.setStatus('mandatory')
fpsPortStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortStatsStatus.setStatus('mandatory')
fpsPortSpecialPortsSMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortSpecialPortsSMT.setStatus('mandatory')
fpsPortSpecialPortsHost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortSpecialPortsHost.setStatus('mandatory')
fpsPortSpecialPortsError = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortSpecialPortsError.setStatus('mandatory')
fpsCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3))
fpsActiveClusters = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsActiveClusters.setStatus('mandatory')
fpsClusterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2), )
if mibBuilder.loadTexts: fpsClusterTable.setStatus('mandatory')
fpsClusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1), ).setIndexNames((0, "CTFPS-MIB", "fpsClusterNumber"))
if mibBuilder.loadTexts: fpsClusterEntry.setStatus('mandatory')
fpsClusterNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsClusterNumber.setStatus('mandatory')
fpsClusterType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("ethernet", 1), ("token-ring", 2), ("inb", 3), ("fnb", 4), ("host", 5), ("atm", 6), ("wan", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsClusterType.setStatus('mandatory')
fpsClusterRoundRobin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpsClusterRoundRobin.setStatus('mandatory')
fpsPortsPerCluster = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpsPortsPerCluster.setStatus('mandatory')
fpsDMAF = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 4))
dmafBandWidth3SecUtil = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmafBandWidth3SecUtil.setStatus('mandatory')
fpsBAF = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5))
bafEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bafEntryCount.setStatus('mandatory')
bafMaxEntry = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bafMaxEntry.setStatus('mandatory')
baf3SecUtil = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baf3SecUtil.setStatus('mandatory')
mibBuilder.exportSymbols("CTFPS-MIB", fpsActiveClusters=fpsActiveClusters, fpsInOctets=fpsInOctets, fpsPortIfNum=fpsPortIfNum, fpsPortBroadcastStatus=fpsPortBroadcastStatus, fpsClusterType=fpsClusterType, fpsPortUnknownStatus=fpsPortUnknownStatus, fpsPortsPerCluster=fpsPortsPerCluster, fpsClusterRoundRobin=fpsClusterRoundRobin, fpsPortBandwidthRequested=fpsPortBandwidthRequested, fpsPortSpecialPortsError=fpsPortSpecialPortsError, fpsDMAF=fpsDMAF, fpsOutPkts=fpsOutPkts, fpsPortViolationStatus=fpsPortViolationStatus, fpsBAF=fpsBAF, fpsSystemSlotNum=fpsSystemSlotNum, fpsSystemMode=fpsSystemMode, fpsOperTime=fpsOperTime, fpsCluster=fpsCluster, fpsPortSpecialPortsSMT=fpsPortSpecialPortsSMT, dmafBandWidth3SecUtil=dmafBandWidth3SecUtil, fpsPortMaxQueDepth=fpsPortMaxQueDepth, baf3SecUtil=baf3SecUtil, fpsMaxPktRam=fpsMaxPktRam, fpsPortType=fpsPortType, fpsPortClusterNum=fpsPortClusterNum, fpsClusterTable=fpsClusterTable, fpsPortNum=fpsPortNum, fpsPortLearningStatus=fpsPortLearningStatus, fpsOutOctets=fpsOutOctets, fpsPortXmitStatus=fpsPortXmitStatus, fpsPortSpecialPortsHost=fpsPortSpecialPortsHost, fpsActivePorts=fpsActivePorts, bafEntryCount=bafEntryCount, fpsClusterEntry=fpsClusterEntry, fpsPortBandwidthAllocated=fpsPortBandwidthAllocated, fpsPort=fpsPort, fpsInPkts=fpsInPkts, fpsSystem=fpsSystem, fpsMaxPortNum=fpsMaxPortNum, fpsPortStatsStatus=fpsPortStatsStatus, fpsPortEntry=fpsPortEntry, fpsClusterNumber=fpsClusterNumber, bafMaxEntry=bafMaxEntry, fpsPortCopyStatus=fpsPortCopyStatus, fpsPortTotalAvailQueDepth=fpsPortTotalAvailQueDepth, fpsPortCurrentQueDepth=fpsPortCurrentQueDepth, fpsFreePktRam=fpsFreePktRam, fpsPortFwdStatus=fpsPortFwdStatus, fpsPortTable=fpsPortTable)
