#
# PySNMP MIB module SL-L2TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-L2TOPOLOGY-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:56 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfTotalCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfTotalCount", "PerfIntervalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Bits, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, ObjectIdentity, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "IpAddress", "Integer32")
DisplayString, PhysAddress, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
slL2Topology = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10))
if mibBuilder.loadTexts: slL2Topology.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slL2Topology.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slL2Topology.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slL2Topology.setDescription('This MIB module describes the Layer-2 Topology')
topologyL2Links = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1))
topologyL2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2))
topologyL2LinkTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1), )
if mibBuilder.loadTexts: topologyL2LinkTable.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkTable.setDescription('The Topology L2 Link table.\n\t\tThis table contains the L2 links.')
topologyL2LinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1), ).setIndexNames((0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalIp"), (0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalPort"))
if mibBuilder.loadTexts: topologyL2LinkEntry.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkEntry.setDescription('An entry in the Topology L2 Link table.')
topologyL2LinkLocalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalIp.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalIp.setDescription('The local ip.')
topologyL2LinkLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalPort.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalPort.setDescription('The local node port number.')
topologyL2LinkLocalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalMac.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalMac.setDescription('The local MAC address.')
topologyL2LinkLocalTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalTid.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalTid.setDescription('The local TID.')
topologyL2LinkRemoteIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteIp.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemoteIp.setDescription('The IP of the remote node.')
topologyL2LinkRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemotePort.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemotePort.setDescription('The port number of the remote node.')
topologyL2LinkRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteMac.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemoteMac.setDescription('The remote MAC address.')
topologyL2LinkRemoteTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteTid.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemoteTid.setDescription('The remote TID.')
topologyL2LastChange = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LastChange.setStatus('current')
if mibBuilder.loadTexts: topologyL2LastChange.setDescription("The value of MIB II's sysUpTime object at the\n\t\ttime the TopologyL2LinkTable was last changed.")
topologyL2ChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: topologyL2ChangeTrapEnable.setStatus('current')
if mibBuilder.loadTexts: topologyL2ChangeTrapEnable.setDescription('Indicates whether L2 topology change traps\n\t\tshould be generated.')
topologyL2LinkChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 3))
if mibBuilder.loadTexts: topologyL2LinkChange.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkChange.setDescription('A topologyL2LinkChange trap is sent when the\n\t\tcontent of an instance TopologyL2LinkEntry is changed.')
mibBuilder.exportSymbols("SL-L2TOPOLOGY-MIB", topologyL2LinkRemoteIp=topologyL2LinkRemoteIp, PYSNMP_MODULE_ID=slL2Topology, topologyL2LinkRemotePort=topologyL2LinkRemotePort, topologyL2LinkTable=topologyL2LinkTable, topologyL2Traps=topologyL2Traps, topologyL2LinkEntry=topologyL2LinkEntry, slL2Topology=slL2Topology, topologyL2ChangeTrapEnable=topologyL2ChangeTrapEnable, topologyL2LinkRemoteMac=topologyL2LinkRemoteMac, topologyL2LinkLocalPort=topologyL2LinkLocalPort, topologyL2LinkLocalMac=topologyL2LinkLocalMac, topologyL2LinkLocalTid=topologyL2LinkLocalTid, topologyL2LinkChange=topologyL2LinkChange, topologyL2LinkLocalIp=topologyL2LinkLocalIp, topologyL2LinkRemoteTid=topologyL2LinkRemoteTid, topologyL2Links=topologyL2Links, topologyL2LastChange=topologyL2LastChange)
