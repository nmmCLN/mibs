#
# PySNMP MIB module RAPID-IPSEC-ENDPOINT-PAIR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-IPSEC-ENDPOINT-PAIR-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:01 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, MibIdentifier, TimeTicks, Counter32, IpAddress, Integer32, enterprises, Bits, ModuleIdentity, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibIdentifier", "TimeTicks", "Counter32", "IpAddress", "Integer32", "enterprises", "Bits", "ModuleIdentity", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsIpsecEndpointPairModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 5))
rsIpsecEndpointPairModule.setRevisions(('2000-03-21 12:00', '2002-11-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsIpsecEndpointPairModule.setRevisionsDescriptions(('Initial revision.', 'Changed CONTACT-INFO.',))
if mibBuilder.loadTexts: rsIpsecEndpointPairModule.setLastUpdated('9909081200Z')
if mibBuilder.loadTexts: rsIpsecEndpointPairModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsIpsecEndpointPairModule.setContactInfo('   Ella Yu\n                      WatchGuard Technologies, Inc.\n                      1841 Zanker Road\n                      San Jose, CA 95112\n                      USA\n\n                      408-519-4888\n                      ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsIpsecEndpointPairModule.setDescription("The MIB module describes generic Ipsec Endpoint Pair information\n            of RapidStream system.  Mainly, the information \n            obtained from this MIB is used to constructed topological\n            view of IPSec security gateways that are connected by\n            IPSec tunnels. \n               \n            An IPSec Endpoint Pair is a pair of security gateways that\n            are connected with 0 or more IPSec SA's in tunnel mode.  \n            It contains information of aggregated information \n            of tunnel mode SA's between two security gateways.\n\n            An IPSec Endpoint Pair is identified by a pair of IP addresses.\n            Therefore, if an IPSec security gateway X has 2 external\n            IP addresses while IPsec secruity gateway Y has 3 external\n            IP addresses, there are potentially 6 IPsec Endpoint Pairs\n            between X and Y.")
rsIpsecEndpointPairMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1))
if mibBuilder.loadTexts: rsIpsecEndpointPairMIB.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairMIB.setDescription('This is the base object identifier for all IPSec tunnel\n             branches.')
rsIpsecEndpointPair = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1))
if mibBuilder.loadTexts: rsIpsecEndpointPair.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPair.setDescription('This is the base object identifier for all IPSec\n            tunnel information.')
rsIpsecEndpointPairStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2))
if mibBuilder.loadTexts: rsIpsecEndpointPairStatistics.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairStatistics.setDescription('This is the base object identifier for all objects which\n            are global counters for IPSec tunnels.')
rsIpsecEndpointPairNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairNum.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairNum.setDescription('The total number of entries in the rsIpsecEndpointPairTable. ')
rsIpsecEndpointPairTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2), )
if mibBuilder.loadTexts: rsIpsecEndpointPairTable.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTable.setDescription('This is the connection table describing all current\n            IPSec tunnels exist on this entity.')
rsIpsecEndpointPairEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1), ).setIndexNames((0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairIndex"))
if mibBuilder.loadTexts: rsIpsecEndpointPairEntry.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairEntry.setDescription('An entry (conceptual row) containing the information on a\n            IPSec tunnel between two IPSec security gateways.')
rsIpsecEndpointPairIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairIndex.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairIndex.setDescription('The running index of this IPSec endpoint pair.')
rsIpsecEndpointPairLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairLocalAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairLocalAddr.setDescription('The local IP address of the current IPSec ednpoint pair.')
rsIpsecEndpointPairPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerAddr.setDescription('The remote IP address of the current IPSec endpoint pair.')
rsIpsecEndpointPairInSAs = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairInSAs.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairInSAs.setDescription("The number of inbound IPSEC SA's within this\n             IPSec endpoint pair.")
rsIpsecEndpointPairOutSAs = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOutSAs.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairOutSAs.setDescription("The number of outbound IPSEC SA's within this\n             IPSec endpoint pair.")
rsIpsecEndpointPairInAccKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 6), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairInAccKbytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairInAccKbytes.setDescription('Total inbound traffic in Kbytes since the establish of\n             this connection.')
rsIpsecEndpointPairOutAccKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 7), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOutAccKbytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairOutAccKbytes.setDescription('Total outound traffic in Kbytes since the establish of\n            this connection.')
rsIpsecEndpointPairInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairInPackets.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairInPackets.setDescription('Total number of inbound packets since the establish of\n            this connection.')
rsIpsecEndpointPairOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOutPackets.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairOutPackets.setDescription('Total number of outound packets since the establish of\n            this connection.')
rsIpsecEndpointPairDecryptErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairDecryptErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairDecryptErrors.setDescription('Total number of packets discarded due to decryption\n            error since the establish of this connection.')
rsIpsecEndpointPairAuthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairAuthErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairAuthErrors.setDescription('Total number of packets discarded due to authentication\n            error since the establish of this connection.')
rsIpsecEndpointPairReplayErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairReplayErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairReplayErrors.setDescription('Total number of packets discarded due to replay\n            error since the establish of this connection.')
rsIpsecEndpointPairPolicyErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPolicyErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPolicyErrors.setDescription('Total number of packets discarded due to policy\n            error since the establish of this connection.')
rsIpsecEndpointPairPadErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPadErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPadErrors.setDescription('Total number of packets discarded due to pad value\n            error since the establish of this connection.')
rsIpsecEndpointPairOtherReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOtherReceiveErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairOtherReceiveErrors.setDescription('The number of packets discarded  due to errors\n            other than decryption, authentication or replay errors. This\n            may include packets dropped due to a lack of receive\n            buffers, and may include packets dropped due to congestion\n            at the decryption element.')
rsIpsecEndpointPairSendErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairSendErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairSendErrors.setDescription('The number of packets discarded due to any error.\n            This may include errors due to a lack of transmit buffers.')
rsIpsecEndpointPairTotalInSAs = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInSAs.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInSAs.setDescription("The total number of active inbound SA's in the entity.")
rsIpsecEndpointPairTotalOutSAs = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutSAs.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutSAs.setDescription("The total number of active outbound SA's in the entity.")
rsIpsecEndpointPairTotalInAccKbytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 3), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInAccKbytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInAccKbytes.setDescription('The total inbound IPsec traffic of this entity.')
rsIpsecEndpointPairTotalOutAccKbytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutAccKbytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutAccKbytes.setDescription('The total outbound IPsec traffic of this entity.')
rsIpsecEndpointPairTotalInPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 5), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInPackets.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInPackets.setDescription('The total inbound IPsec packets of this entity.')
rsIpsecEndpointPairTotalOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutPackets.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutPackets.setDescription('The total outbound IPsec packets of this entity.')
rsIpsecEndpointPairTotalDecryptErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalDecryptErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalDecryptErrors.setDescription('Total number of packets on this entity discarded due to encryption\n           error.')
rsIpsecEndpointPairTotalAuthErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalAuthErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalAuthErrors.setDescription('Total number of packets on this entity discarded \n           due to authentication errors.')
rsIpsecEndpointPairTotalReplayErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalReplayErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalReplayErrors.setDescription('Total number of packets discarded due to replay\n           errors on this entity.')
rsIpsecEndpointPairTotalPolicyErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalPolicyErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalPolicyErrors.setDescription('Total number of packets discarded due to policy\n           errors on this entity.')
rsIpsecEndpointPairTotalPadErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalPadErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalPadErrors.setDescription('Total number of packets on this entity  discarded due to pad value\n           error.')
rsIpsecEndpointPairTotalOtherReceiveErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOtherReceiveErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOtherReceiveErrors.setDescription('The total number of packets on this entity discarded  due to errors\n            other than decryption, authentication or replay errors. This\n            may include packets dropped due to a lack of receive\n            buffers, and may include packets dropped due to congestion\n            at the decryption element.')
rsIpsecEndpointPairTotalSendErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalSendErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalSendErrors.setDescription('The total number of packets discarded due to any error on\n            this entity.')
rsIpsecEndpointPairPeerIPToTunnel = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3))
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnel.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnel.setDescription('This is the base object identifier for all tunnels\n             information of the policies.')
rsIpsecEndpointPairPeerIPToTunnelNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelNum.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelNum.setDescription('The total number of tunnels in the peeriptotunnel table. ')
rsIpsecEndpointPairPeerIPToTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2), )
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelTable.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelTable.setDescription('The peeriptotunnel table in the endpointpair mib.')
rsIpsecEndpointPairPeerIPToTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1), ).setIndexNames((0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairPeerIPToTunnelPeerIP"), (0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairPeerIPToTunnelTunnelID"))
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelEntry.setDescription('An entry (conceptual row) containing the peer ip and tunnel\n            information.')
rsIpsecEndpointPairPeerIPToTunnelPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelPeerIP.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelPeerIP.setDescription('The peer ip of the peeriptotunnel table.')
rsIpsecEndpointPairPeerIPToTunnelTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelTunnelID.setStatus('current')
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelTunnelID.setDescription('The tunnel id of the peeriptotunnel table.')
mibBuilder.exportSymbols("RAPID-IPSEC-ENDPOINT-PAIR-MIB", rsIpsecEndpointPairPeerIPToTunnelTable=rsIpsecEndpointPairPeerIPToTunnelTable, rsIpsecEndpointPairTotalOutSAs=rsIpsecEndpointPairTotalOutSAs, rsIpsecEndpointPairTotalReplayErrors=rsIpsecEndpointPairTotalReplayErrors, rsIpsecEndpointPairAuthErrors=rsIpsecEndpointPairAuthErrors, rsIpsecEndpointPairModule=rsIpsecEndpointPairModule, rsIpsecEndpointPairInAccKbytes=rsIpsecEndpointPairInAccKbytes, rsIpsecEndpointPairPolicyErrors=rsIpsecEndpointPairPolicyErrors, rsIpsecEndpointPairTotalOutAccKbytes=rsIpsecEndpointPairTotalOutAccKbytes, rsIpsecEndpointPairEntry=rsIpsecEndpointPairEntry, rsIpsecEndpointPairTotalInSAs=rsIpsecEndpointPairTotalInSAs, rsIpsecEndpointPairTotalOtherReceiveErrors=rsIpsecEndpointPairTotalOtherReceiveErrors, rsIpsecEndpointPairMIB=rsIpsecEndpointPairMIB, rsIpsecEndpointPairTotalDecryptErrors=rsIpsecEndpointPairTotalDecryptErrors, rsIpsecEndpointPairTotalPadErrors=rsIpsecEndpointPairTotalPadErrors, PYSNMP_MODULE_ID=rsIpsecEndpointPairModule, rsIpsecEndpointPair=rsIpsecEndpointPair, rsIpsecEndpointPairReplayErrors=rsIpsecEndpointPairReplayErrors, rsIpsecEndpointPairTotalOutPackets=rsIpsecEndpointPairTotalOutPackets, rsIpsecEndpointPairPeerIPToTunnelPeerIP=rsIpsecEndpointPairPeerIPToTunnelPeerIP, rsIpsecEndpointPairOutAccKbytes=rsIpsecEndpointPairOutAccKbytes, rsIpsecEndpointPairTotalInAccKbytes=rsIpsecEndpointPairTotalInAccKbytes, rsIpsecEndpointPairTotalSendErrors=rsIpsecEndpointPairTotalSendErrors, rsIpsecEndpointPairIndex=rsIpsecEndpointPairIndex, rsIpsecEndpointPairPeerIPToTunnelTunnelID=rsIpsecEndpointPairPeerIPToTunnelTunnelID, rsIpsecEndpointPairLocalAddr=rsIpsecEndpointPairLocalAddr, rsIpsecEndpointPairDecryptErrors=rsIpsecEndpointPairDecryptErrors, rsIpsecEndpointPairNum=rsIpsecEndpointPairNum, rsIpsecEndpointPairPeerIPToTunnelNum=rsIpsecEndpointPairPeerIPToTunnelNum, rsIpsecEndpointPairSendErrors=rsIpsecEndpointPairSendErrors, rsIpsecEndpointPairInSAs=rsIpsecEndpointPairInSAs, rsIpsecEndpointPairOtherReceiveErrors=rsIpsecEndpointPairOtherReceiveErrors, rsIpsecEndpointPairOutSAs=rsIpsecEndpointPairOutSAs, rsIpsecEndpointPairStatistics=rsIpsecEndpointPairStatistics, rsIpsecEndpointPairTotalInPackets=rsIpsecEndpointPairTotalInPackets, rsIpsecEndpointPairTotalAuthErrors=rsIpsecEndpointPairTotalAuthErrors, rsIpsecEndpointPairPadErrors=rsIpsecEndpointPairPadErrors, rsIpsecEndpointPairTotalPolicyErrors=rsIpsecEndpointPairTotalPolicyErrors, rsIpsecEndpointPairPeerAddr=rsIpsecEndpointPairPeerAddr, rsIpsecEndpointPairPeerIPToTunnel=rsIpsecEndpointPairPeerIPToTunnel, rsIpsecEndpointPairInPackets=rsIpsecEndpointPairInPackets, rsIpsecEndpointPairOutPackets=rsIpsecEndpointPairOutPackets, rsIpsecEndpointPairPeerIPToTunnelEntry=rsIpsecEndpointPairPeerIPToTunnelEntry, rsIpsecEndpointPairTable=rsIpsecEndpointPairTable)
