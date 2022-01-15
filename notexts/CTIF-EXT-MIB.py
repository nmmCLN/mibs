#
# PySNMP MIB module CTIF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTIF-EXT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:13 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctronMib2, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronMib2")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
commonDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1))
ctIf = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2))
ctIfPort = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3))
ctIfCp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4))
ctSNMP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5))
ctSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6))
ctVirtual = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7))
ctStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8))
ctFramerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9))
ctIfHC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10))
comDeviceTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 1), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(6, 6), ValueSizeConstraint(8, 8), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceTime.setStatus('mandatory')
comDeviceDate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceDate.setStatus('mandatory')
comDeviceBoardMap = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comDeviceBoardMap.setStatus('mandatory')
ctIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1), )
if mibBuilder.loadTexts: ctIfTable.setStatus('mandatory')
ctIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctIfNumber"))
if mibBuilder.loadTexts: ctIfEntry.setStatus('mandatory')
ctIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfNumber.setStatus('mandatory')
ctIfPortCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortCnt.setStatus('mandatory')
ctIfConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfConnectionType.setStatus('mandatory')
ctIfLAA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfLAA.setStatus('mandatory')
ctIfDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("full", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfDuplex.setStatus('mandatory')
ctIfCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("fullDuplex", 3), ("fastEthernet", 4), ("ethernetBased", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfCapability.setStatus('mandatory')
ctIfRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redundant", 1), ("not-redundant", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfRedundancy.setStatus('mandatory')
ctIfPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1), )
if mibBuilder.loadTexts: ctIfPortTable.setStatus('mandatory')
ctIfPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctIfPortIfNumber"), (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"))
if mibBuilder.loadTexts: ctIfPortEntry.setStatus('mandatory')
ctIfPortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortPortNumber.setStatus('mandatory')
ctIfPortIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortIfNumber.setStatus('mandatory')
ctIfPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortType.setStatus('mandatory')
ctIfPortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notLinked", 1), ("linked", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortLinkStatus.setStatus('mandatory')
ctIfPortTrapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfPortTrapStatus.setStatus('mandatory')
ctCpTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1), )
if mibBuilder.loadTexts: ctCpTable.setStatus('mandatory')
ctCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctComPort"))
if mibBuilder.loadTexts: ctCpEntry.setStatus('mandatory')
ctComPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctComPort.setStatus('mandatory')
ctCpFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("lm", 1), ("ups", 2), ("slip", 3), ("ppp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCpFunction.setStatus('mandatory')
ctIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfNum.setStatus('mandatory')
ctCpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCpAdminStatus.setStatus('mandatory')
enableSNMPv1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableSNMPv1.setStatus('mandatory')
enableSNMPv2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableSNMPv2.setStatus('mandatory')
enableSNMPv1Counter64 = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableSNMPv1Counter64.setStatus('mandatory')
ctSonetTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1), )
if mibBuilder.loadTexts: ctSonetTable.setStatus('deprecated')
ctSonetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctSonetIfIndex"))
if mibBuilder.loadTexts: ctSonetEntry.setStatus('deprecated')
ctSonetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctSonetIfIndex.setStatus('deprecated')
ctSonetMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctSonetMediumType.setStatus('deprecated')
ctVirtualIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1), )
if mibBuilder.loadTexts: ctVirtualIfTable.setStatus('mandatory')
ctVirtualIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctVirtualIfIndex"))
if mibBuilder.loadTexts: ctVirtualIfEntry.setStatus('mandatory')
ctVirtualIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfIndex.setStatus('mandatory')
ctVirtualIfPhysicalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPhysicalInterface.setStatus('mandatory')
ctVirtualIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfType.setStatus('mandatory')
ctVirtualIfNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfNumPorts.setStatus('mandatory')
ctVirtualIfPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2), )
if mibBuilder.loadTexts: ctVirtualIfPortTable.setStatus('mandatory')
ctVirtualIfPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctVirtualIfPortIfIndex"), (0, "CTIF-EXT-MIB", "ctVirtualIfPortNumber"))
if mibBuilder.loadTexts: ctVirtualIfPortEntry.setStatus('mandatory')
ctVirtualIfPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortIfIndex.setStatus('mandatory')
ctVirtualIfPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortNumber.setStatus('mandatory')
ctVirtualIfPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("portVirtualTypeSvc", 1), ("portVirtualTypePvcLlc", 2), ("portVirtualTypePvcVcmux", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortType.setStatus('mandatory')
ctVirtualIfPortVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortVPI.setStatus('mandatory')
ctVirtualIfPortVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortVCI.setStatus('mandatory')
ctStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1), )
if mibBuilder.loadTexts: ctStatsTable.setStatus('mandatory')
ctStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctStatsIfIndex"))
if mibBuilder.loadTexts: ctStatsEntry.setStatus('mandatory')
ctStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctStatsIfIndex.setStatus('mandatory')
ctStatsIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctStatsIfEnable.setStatus('mandatory')
ctIfHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1), )
if mibBuilder.loadTexts: ctIfHCStatsTable.setStatus('mandatory')
ctIfHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctIfHCStatsEntry.setStatus('mandatory')
ctIfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInOctets.setStatus('mandatory')
ctIfInOctetsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInOctetsOverflows.setStatus('mandatory')
ctIfInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInUcastPkts.setStatus('mandatory')
ctIfInUcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInUcastPktsOverflows.setStatus('mandatory')
ctIfInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInMulticastPkts.setStatus('mandatory')
ctIfInMulticastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInMulticastPktsOverflows.setStatus('mandatory')
ctIfInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInBroadcastPkts.setStatus('mandatory')
ctIfInBroadcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInBroadcastPktsOverflows.setStatus('mandatory')
ctIfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutOctets.setStatus('mandatory')
ctIfOutOctetsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutOctetsOverflows.setStatus('mandatory')
ctIfOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutUcastPkts.setStatus('mandatory')
ctIfOutUcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutUcastPktsOverflows.setStatus('mandatory')
ctIfOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutMulticastPkts.setStatus('mandatory')
ctIfOutMulticastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutMulticastPktsOverflows.setStatus('mandatory')
ctIfOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutBroadcastPkts.setStatus('mandatory')
ctIfOutBroadcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutBroadcastPktsOverflows.setStatus('mandatory')
mibBuilder.exportSymbols("CTIF-EXT-MIB", ctIfCapability=ctIfCapability, ctIfRedundancy=ctIfRedundancy, ctVirtualIfPortNumber=ctVirtualIfPortNumber, ctIfLAA=ctIfLAA, ctIfPortType=ctIfPortType, ctVirtualIfPortEntry=ctVirtualIfPortEntry, ctIfInBroadcastPkts=ctIfInBroadcastPkts, ctStats=ctStats, ctIfInMulticastPkts=ctIfInMulticastPkts, ctSonetIfIndex=ctSonetIfIndex, ctIfOutOctets=ctIfOutOctets, ctIfInMulticastPktsOverflows=ctIfInMulticastPktsOverflows, ctSonetMediumType=ctSonetMediumType, ctVirtualIfPortIfIndex=ctVirtualIfPortIfIndex, ctIfPortCnt=ctIfPortCnt, comDeviceDate=comDeviceDate, ctIfHCStatsTable=ctIfHCStatsTable, ctCpAdminStatus=ctCpAdminStatus, ctIfEntry=ctIfEntry, comDeviceBoardMap=comDeviceBoardMap, ctIfHC=ctIfHC, ctIfTable=ctIfTable, ctCpFunction=ctCpFunction, ctComPort=ctComPort, commonDev=commonDev, enableSNMPv1=enableSNMPv1, enableSNMPv1Counter64=enableSNMPv1Counter64, ctIfPortLinkStatus=ctIfPortLinkStatus, ctIfNum=ctIfNum, ctIfOutBroadcastPktsOverflows=ctIfOutBroadcastPktsOverflows, ctSonetEntry=ctSonetEntry, ctVirtualIfPortVPI=ctVirtualIfPortVPI, ctIf=ctIf, ctIfOutMulticastPktsOverflows=ctIfOutMulticastPktsOverflows, ctSNMP=ctSNMP, ctVirtual=ctVirtual, ctStatsTable=ctStatsTable, ctStatsIfEnable=ctStatsIfEnable, ctIfInUcastPkts=ctIfInUcastPkts, ctVirtualIfType=ctVirtualIfType, ctIfOutBroadcastPkts=ctIfOutBroadcastPkts, ctVirtualIfEntry=ctVirtualIfEntry, ctIfInOctetsOverflows=ctIfInOctetsOverflows, ctIfPortIfNumber=ctIfPortIfNumber, ctCpTable=ctCpTable, ctIfInOctets=ctIfInOctets, ctVirtualIfPortType=ctVirtualIfPortType, ctFramerConfig=ctFramerConfig, ctIfOutOctetsOverflows=ctIfOutOctetsOverflows, ctVirtualIfPhysicalInterface=ctVirtualIfPhysicalInterface, ctIfPortTable=ctIfPortTable, ctIfInBroadcastPktsOverflows=ctIfInBroadcastPktsOverflows, ctStatsIfIndex=ctStatsIfIndex, ctVirtualIfIndex=ctVirtualIfIndex, ctIfPort=ctIfPort, ctIfCp=ctIfCp, ctSonetTable=ctSonetTable, ctVirtualIfPortTable=ctVirtualIfPortTable, ctIfNumber=ctIfNumber, ctSonet=ctSonet, ctStatsEntry=ctStatsEntry, ctIfPortTrapStatus=ctIfPortTrapStatus, enableSNMPv2=enableSNMPv2, ctIfOutUcastPktsOverflows=ctIfOutUcastPktsOverflows, ctIfHCStatsEntry=ctIfHCStatsEntry, ctIfOutMulticastPkts=ctIfOutMulticastPkts, comDeviceTime=comDeviceTime, ctIfOutUcastPkts=ctIfOutUcastPkts, ctIfPortEntry=ctIfPortEntry, ctIfPortPortNumber=ctIfPortPortNumber, ctVirtualIfPortVCI=ctVirtualIfPortVCI, ctVirtualIfNumPorts=ctVirtualIfNumPorts, ctVirtualIfTable=ctVirtualIfTable, ctCpEntry=ctCpEntry, ctIfInUcastPktsOverflows=ctIfInUcastPktsOverflows, ctIfConnectionType=ctIfConnectionType, ctIfDuplex=ctIfDuplex)
