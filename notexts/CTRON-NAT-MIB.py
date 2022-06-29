#
# PySNMP MIB module CTRON-NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-NAT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
nwIpRouter, nwIpMibs, nwIpClientServices, nwIpComponents = mibBuilder.importSymbols("CTRON-IP-ROUTER-MIB", "nwIpRouter", "nwIpMibs", "nwIpClientServices", "nwIpComponents")
nwRtrProtoSuites, = mibBuilder.importSymbols("ROUTER-OIDS", "nwRtrProtoSuites")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctNat = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1))
ctNatConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1))
ctNatServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2))
ctNatConnStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3))
ctNatPublicIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatPublicIfIndex.setStatus('mandatory')
ctNatPublicIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPublicIP.setStatus('mandatory')
ctNatPublicMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPublicMask.setStatus('mandatory')
ctNatMaxConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatMaxConn.setStatus('mandatory')
ctNatTcpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatTcpTimeout.setStatus('mandatory')
ctNatUdpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatUdpTimeout.setStatus('mandatory')
ctNatPktsL2I = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPktsL2I.setStatus('mandatory')
ctNatPktsI2L = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPktsI2L.setStatus('mandatory')
ctNatBytesL2I = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBytesL2I.setStatus('mandatory')
ctNatBytesI2L = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBytesI2L.setStatus('mandatory')
ctNatTcpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTcpConn.setStatus('mandatory')
ctNatUdpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatUdpConn.setStatus('mandatory')
ctNatIcmpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatIcmpConn.setStatus('mandatory')
ctNatRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatRetries.setStatus('mandatory')
ctNatBadSums = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBadSums.setStatus('mandatory')
ctNatTotalPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotalPkts.setStatus('mandatory')
ctNatBadPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBadPkts.setStatus('mandatory')
ctNatResPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatResPkts.setStatus('mandatory')
ctNatTotTcpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotTcpConn.setStatus('mandatory')
ctNatTotUdpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotUdpConn.setStatus('mandatory')
ctNatTotIcmpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotIcmpConn.setStatus('mandatory')
ctNatConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22), )
if mibBuilder.loadTexts: ctNatConfigTable.setStatus('mandatory')
ctNatConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1), ).setIndexNames((0, "CTRON-NAT-MIB", "ctNatConfigId"))
if mibBuilder.loadTexts: ctNatConfigEntry.setStatus('mandatory')
ctNatConfigId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConfigId.setStatus('mandatory')
ctNatAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatAdminStatus.setStatus('mandatory')
ctNatOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("invalid-config", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatOperStatus.setStatus('mandatory')
ctNatLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatLocalIfIndex.setStatus('mandatory')
ctNatLocalIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatLocalIP.setStatus('mandatory')
ctNatLocalMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatLocalMask.setStatus('mandatory')
ctNatTotServerEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotServerEntries.setStatus('mandatory')
ctNatServerListTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2), )
if mibBuilder.loadTexts: ctNatServerListTable.setStatus('mandatory')
ctNatServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1), ).setIndexNames((0, "CTRON-NAT-MIB", "ctNatServerId"))
if mibBuilder.loadTexts: ctNatServerListEntry.setStatus('mandatory')
ctNatServerId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatServerId.setStatus('mandatory')
ctNatProxyServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatProxyServer.setStatus('mandatory')
ctNatTotActiveConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotActiveConn.setStatus('mandatory')
ctNatConnStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2), )
if mibBuilder.loadTexts: ctNatConnStatsTable.setStatus('mandatory')
ctNatConnStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1), ).setIndexNames((0, "CTRON-NAT-MIB", "ctNatConnStatsID"))
if mibBuilder.loadTexts: ctNatConnStatsEntry.setStatus('mandatory')
ctNatConnStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsID.setStatus('mandatory')
ctNatConnStatsForeignIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignIP.setStatus('mandatory')
ctNatConnStatsLocalIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalIP.setStatus('mandatory')
ctNatConnStatsPublicPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsPublicPort.setStatus('mandatory')
ctNatConnStatsLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalPort.setStatus('mandatory')
ctNatConnStatsForeignPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignPort.setStatus('mandatory')
ctNatConnStatsOutgoingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsOutgoingPkts.setStatus('mandatory')
ctNatConnStatsOutgoingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsOutgoingBytes.setStatus('mandatory')
ctNatConnStatsIncomingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsIncomingPkts.setStatus('mandatory')
ctNatConnStatsIncomingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsIncomingBytes.setStatus('mandatory')
ctNatConnStatsTimeSinceUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTimeSinceUse.setStatus('mandatory')
ctNatConnStatsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsProtocol.setStatus('mandatory')
ctNatConnStatsTCPSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTCPSeq.setStatus('mandatory')
ctNatConnStatsTCPAck = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTCPAck.setStatus('mandatory')
ctNatConnStatsTCPState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTCPState.setStatus('mandatory')
ctNatConnStatsLocalRetrys = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalRetrys.setStatus('mandatory')
ctNatConnStatsForeignRetrys = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignRetrys.setStatus('mandatory')
ctNatConnStatsLocalChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalChecksum.setStatus('mandatory')
ctNatConnStatsForeignChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignChecksum.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-NAT-MIB", ctNatTcpTimeout=ctNatTcpTimeout, ctNatBytesI2L=ctNatBytesI2L, ctNatTotServerEntries=ctNatTotServerEntries, ctNatBadSums=ctNatBadSums, ctNatConnStatsIncomingBytes=ctNatConnStatsIncomingBytes, ctNatConnStatsEntry=ctNatConnStatsEntry, ctNatLocalMask=ctNatLocalMask, ctNatBytesL2I=ctNatBytesL2I, ctNatConfigEntry=ctNatConfigEntry, ctNatTcpConn=ctNatTcpConn, ctNatConnStatsTCPSeq=ctNatConnStatsTCPSeq, ctNatConnStatsTCPAck=ctNatConnStatsTCPAck, ctNatConnStatsOutgoingBytes=ctNatConnStatsOutgoingBytes, ctNatUdpConn=ctNatUdpConn, ctNatTotalPkts=ctNatTotalPkts, ctNatConnStatsTCPState=ctNatConnStatsTCPState, ctNatAdminStatus=ctNatAdminStatus, ctNatLocalIfIndex=ctNatLocalIfIndex, ctNatUdpTimeout=ctNatUdpTimeout, ctNat=ctNat, ctNatPublicIP=ctNatPublicIP, ctNatConfigId=ctNatConfigId, ctNatServerListTable=ctNatServerListTable, ctNatConnStatsTimeSinceUse=ctNatConnStatsTimeSinceUse, ctNatServerListEntry=ctNatServerListEntry, ctNatConfigTable=ctNatConfigTable, ctNatTotTcpConn=ctNatTotTcpConn, ctNatConnStatsProtocol=ctNatConnStatsProtocol, ctNatTotIcmpConn=ctNatTotIcmpConn, ctNatRetries=ctNatRetries, ctNatLocalIP=ctNatLocalIP, ctNatConnStatsForeignChecksum=ctNatConnStatsForeignChecksum, ctNatServerGroup=ctNatServerGroup, ctNatServerId=ctNatServerId, ctNatPublicMask=ctNatPublicMask, ctNatConnStatsForeignIP=ctNatConnStatsForeignIP, ctNatConnStatsIncomingPkts=ctNatConnStatsIncomingPkts, ctNatConnStatsLocalRetrys=ctNatConnStatsLocalRetrys, ctNatConnStatsForeignRetrys=ctNatConnStatsForeignRetrys, ctNatResPkts=ctNatResPkts, ctNatConnStatsTable=ctNatConnStatsTable, ctNatConnStatsLocalIP=ctNatConnStatsLocalIP, ctNatOperStatus=ctNatOperStatus, ctNatConnStatsOutgoingPkts=ctNatConnStatsOutgoingPkts, ctNatPktsI2L=ctNatPktsI2L, ctNatIcmpConn=ctNatIcmpConn, ctNatBadPkts=ctNatBadPkts, ctNatConnStatsLocalChecksum=ctNatConnStatsLocalChecksum, ctNatTotActiveConn=ctNatTotActiveConn, ctNatTotUdpConn=ctNatTotUdpConn, ctNatConnStatsID=ctNatConnStatsID, ctNatConnStatsGroup=ctNatConnStatsGroup, ctNatPktsL2I=ctNatPktsL2I, ctNatMaxConn=ctNatMaxConn, ctNatConnStatsForeignPort=ctNatConnStatsForeignPort, ctNatConnStatsLocalPort=ctNatConnStatsLocalPort, ctNatProxyServer=ctNatProxyServer, ctNatConfigGroup=ctNatConfigGroup, ctNatPublicIfIndex=ctNatPublicIfIndex, ctNatConnStatsPublicPort=ctNatConnStatsPublicPort)
