#
# PySNMP MIB module DRAFT-MSDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/MSDP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:43 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, experimental, NotificationType, ObjectIdentity, Unsigned32, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, IpAddress, Counter32, ModuleIdentity, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "experimental", "NotificationType", "ObjectIdentity", "Unsigned32", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "IpAddress", "Counter32", "ModuleIdentity", "Counter64", "Gauge32")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
msdpMIB = ModuleIdentity((1, 3, 6, 1, 3, 92))
if mibBuilder.loadTexts: msdpMIB.setLastUpdated('9912160000Z')
if mibBuilder.loadTexts: msdpMIB.setOrganization('IETF MSDP Working Group')
if mibBuilder.loadTexts: msdpMIB.setContactInfo(' Bill Fenner\n              75 Willow Road\n              Menlo Park, CA  94025\n              Phone: +1 650 867 6073\n              E-mail: fenner@research.att.com\n\n              Dave Thaler\n              One Microsoft Way\n              Redmond, WA  98052\n              Phone: +1 425 703 8835\n              Email: dthaler@microsoft.com')
if mibBuilder.loadTexts: msdpMIB.setDescription('An experimental MIB module for MSDP Management.')
msdpMIBobjects = MibIdentifier((1, 3, 6, 1, 3, 92, 1))
msdp = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1))
msdpEnabled = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msdpEnabled.setStatus('current')
if mibBuilder.loadTexts: msdpEnabled.setDescription('The state of MSDP on this MSDP speaker - globally\n            enabled or disabled.')
msdpCacheLifetime = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 2), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msdpCacheLifetime.setStatus('current')
if mibBuilder.loadTexts: msdpCacheLifetime.setDescription('The lifetime given to SA cache entries when created\n            or refreshed.  A value of 0 means no SA caching is\n            done by this MSDP speaker.')
msdpNumSACacheEntries = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpNumSACacheEntries.setStatus('current')
if mibBuilder.loadTexts: msdpNumSACacheEntries.setDescription('The total number of entries in the SA Cache table.')
msdpSAHoldDownPeriod = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(90)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSAHoldDownPeriod.setStatus('current')
if mibBuilder.loadTexts: msdpSAHoldDownPeriod.setDescription('The number of seconds in the MSDP SA Hold-down\n            period')
msdpRequestsTable = MibTable((1, 3, 6, 1, 3, 92, 1, 1, 4), )
if mibBuilder.loadTexts: msdpRequestsTable.setStatus('current')
if mibBuilder.loadTexts: msdpRequestsTable.setDescription('The (conceptual) table listing group ranges and MSDP\n            peers used when deciding where to send an SA Request\n            message when required.  If SA Caching is enabled, this\n            table may be empty.')
msdpRequestsEntry = MibTableRow((1, 3, 6, 1, 3, 92, 1, 1, 4, 1), ).setIndexNames((0, "DRAFT-MSDP-MIB", "msdpRequestsGroupAddress"), (0, "DRAFT-MSDP-MIB", "msdpRequestsGroupMask"))
if mibBuilder.loadTexts: msdpRequestsEntry.setStatus('current')
if mibBuilder.loadTexts: msdpRequestsEntry.setDescription('An entry (conceptual row) representing a group range\n            used when deciding where to send an SA Request\n            message.')
msdpRequestsGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: msdpRequestsGroupAddress.setStatus('current')
if mibBuilder.loadTexts: msdpRequestsGroupAddress.setDescription('The group address that, when combined with the mask\n            in this entry, represents the group range for which\n            this peer will service MSDP SA Requests.')
msdpRequestsGroupMask = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: msdpRequestsGroupMask.setStatus('current')
if mibBuilder.loadTexts: msdpRequestsGroupMask.setDescription('The mask that, when combined with the group address\n            in this entry, represents the group range for which\n            this peer will service MSDP SA Requests.')
msdpRequestsPeer = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpRequestsPeer.setStatus('current')
if mibBuilder.loadTexts: msdpRequestsPeer.setDescription("The peer to which MSDP SA Requests for groups\n            matching this entry's group range will be sent.  Must\n            match the INDEX of a row in the msdpPeerTable.")
msdpRequestsStatus = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpRequestsStatus.setStatus('current')
if mibBuilder.loadTexts: msdpRequestsStatus.setDescription('The status of this row, by which new rows may be\n            added to the table.')
msdpPeerTable = MibTable((1, 3, 6, 1, 3, 92, 1, 1, 5), )
if mibBuilder.loadTexts: msdpPeerTable.setStatus('current')
if mibBuilder.loadTexts: msdpPeerTable.setDescription("The (conceptual) table listing the MSDP speaker's\n            peers.")
msdpPeerEntry = MibTableRow((1, 3, 6, 1, 3, 92, 1, 1, 5, 1), ).setIndexNames((0, "DRAFT-MSDP-MIB", "msdpPeerRemoteAddress"))
if mibBuilder.loadTexts: msdpPeerEntry.setStatus('current')
if mibBuilder.loadTexts: msdpPeerEntry.setDescription('An entry (conceptual row) representing an MSDP peer.')
msdpPeerRemoteAddress = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: msdpPeerRemoteAddress.setStatus('current')
if mibBuilder.loadTexts: msdpPeerRemoteAddress.setDescription('The address of the remote MSDP peer.')
msdpPeerState = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inactive", 1), ("listen", 2), ("connecting", 3), ("established", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerState.setStatus('current')
if mibBuilder.loadTexts: msdpPeerState.setDescription('The state of the MSDP TCP connection with this peer.')
msdpPeerRPFFailures = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerRPFFailures.setStatus('current')
if mibBuilder.loadTexts: msdpPeerRPFFailures.setDescription('The number of RPF failures on SA messages received\n            from this peer.')
msdpPeerInSAs = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInSAs.setStatus('current')
if mibBuilder.loadTexts: msdpPeerInSAs.setDescription('The number of MSDP SA messages received on this\n            connection.  This object should be initialized to zero\n            when the connection is established.')
msdpPeerOutSAs = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutSAs.setStatus('current')
if mibBuilder.loadTexts: msdpPeerOutSAs.setDescription('The number of MSDP SA messages transmitted on this\n            connection.  This object should be initialized to zero\n            when the connection is established.')
msdpPeerInSARequests = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInSARequests.setStatus('current')
if mibBuilder.loadTexts: msdpPeerInSARequests.setDescription('The number of MSDP SA-Request messages received on\n            this connection.  This object should be initialized to\n            zero when the connection is established.')
msdpPeerOutSARequests = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutSARequests.setStatus('current')
if mibBuilder.loadTexts: msdpPeerOutSARequests.setDescription('The number of MSDP SA-Request messages transmitted on\n            this connection.  This object should be initialized to\n            zero when the connection is established.')
msdpPeerInSAResponses = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInSAResponses.setStatus('current')
if mibBuilder.loadTexts: msdpPeerInSAResponses.setDescription('The number of MSDP SA-Response messages received on\n            this connection.  This object should be initialized to\n            zero when the connection is established.')
msdpPeerOutSAResponses = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutSAResponses.setStatus('current')
if mibBuilder.loadTexts: msdpPeerOutSAResponses.setDescription('The number of MSDP SA Response messages transmitted\n            on this TCP connection.  This object should be\n            initialized to zero when the connection is\n            established.')
msdpPeerInControlMessages = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInControlMessages.setStatus('current')
if mibBuilder.loadTexts: msdpPeerInControlMessages.setDescription('The total number of MSDP messages received on this\n            TCP connection.  This object should be initialized to\n            zero when the connection is established.')
msdpPeerOutControlMessages = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutControlMessages.setStatus('current')
if mibBuilder.loadTexts: msdpPeerOutControlMessages.setDescription('The total number of MSDP messages transmitted on this\n            TCP connection.  This object should be initialized to\n            zero when the connection is established.')
msdpPeerInDataPackets = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInDataPackets.setStatus('current')
if mibBuilder.loadTexts: msdpPeerInDataPackets.setDescription('The total number of encapsulated data packets\n            received from this peer.  This object should be\n            initialized to zero when the connection is\n            established.')
msdpPeerOutDataPackets = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutDataPackets.setStatus('current')
if mibBuilder.loadTexts: msdpPeerOutDataPackets.setDescription('The total number of encapsulated data packets sent to\n            this peer.  This object should be initialized to zero\n            when the connection is established.')
msdpPeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerFsmEstablishedTransitions.setStatus('current')
if mibBuilder.loadTexts: msdpPeerFsmEstablishedTransitions.setDescription('The total number of times the MSDP FSM transitioned\n            into the established state.')
msdpPeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 16), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerFsmEstablishedTime.setStatus('current')
if mibBuilder.loadTexts: msdpPeerFsmEstablishedTime.setDescription('This timer indicates how long (in seconds) this peer\n            has been in the Established state or how long since\n            this peer was last in the Established state.  It is\n            set to zero when a new peer is configured or the MSDP\n            speaker is booted.')
msdpPeerInMessageElapsedTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 17), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInMessageElapsedTime.setStatus('current')
if mibBuilder.loadTexts: msdpPeerInMessageElapsedTime.setDescription('Elapsed time in seconds since the last MSDP message\n            was received from the peer.  Each time\n            msdpPeerInControlMessages is incremented, the value of\n            this object is set to zero (0).')
msdpPeerLocalAddress = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerLocalAddress.setStatus('current')
if mibBuilder.loadTexts: msdpPeerLocalAddress.setDescription("The local IP address of this entry's MSDP\n            connection.")
msdpPeerSAAdvPeriod = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerSAAdvPeriod.setStatus('current')
if mibBuilder.loadTexts: msdpPeerSAAdvPeriod.setDescription('Time interval in seconds for the\n            MinSAAdvertisementInterval MSDP timer.')
msdpPeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(120)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerConnectRetryInterval.setStatus('current')
if mibBuilder.loadTexts: msdpPeerConnectRetryInterval.setDescription('Time interval in seconds for the ConnectRetry timer.')
msdpPeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), )).clone(90)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerHoldTimeConfigured.setStatus('current')
if mibBuilder.loadTexts: msdpPeerHoldTimeConfigured.setDescription('Time interval in seconds for the Hold Timer\n            configured for this MSDP speaker with this peer.')
msdpPeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), )).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerKeepAliveConfigured.setStatus('current')
if mibBuilder.loadTexts: msdpPeerKeepAliveConfigured.setDescription('Time interval in seconds for the KeepAlive timer\n            configured for this MSDP speaker with this peer.  A\n            reasonable maximum value for this timer would be\n            configured to be one third of that of\n            msdpPeerHoldTimeConfigured.  If the value of this\n            object is zero (0), no periodic KEEPALIVE messages are\n            sent to the peer after the MSDP connection has been\n            established.')
msdpPeerDataTtl = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerDataTtl.setStatus('current')
if mibBuilder.loadTexts: msdpPeerDataTtl.setDescription('The minimum TTL a packet is required to have before\n            it may be forwarded using SA encapsulation to this\n            peer.')
msdpPeerProcessRequestsFrom = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 24), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerProcessRequestsFrom.setStatus('current')
if mibBuilder.loadTexts: msdpPeerProcessRequestsFrom.setDescription('This object indicates whether or not to process MSDP\n            SA Request messages from this peer.  If True(1), MSDP\n            SA Request messages from this peer are processed and\n            replied to (if appropriate) with SA Response messages.\n            If False(2), MSDP SA Request messages from this peer\n            are silently ignored.  It defaults to False when\n            msdpCacheLifetime is 0 and True when msdpCacheLifetime\n            is non-0.')
msdpPeerStatus = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerStatus.setStatus('current')
if mibBuilder.loadTexts: msdpPeerStatus.setDescription("The RowStatus object by which peers can be added and\n            deleted.  A transition to 'active' will cause the MSDP\n            Start Event to be generated.  A transition out of the\n            'active' state will cause the MSDP Stop Event to be\n            generated.  Care should be used in providing write\n            access to this object without adequate\n            authentication.")
msdpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerRemotePort.setStatus('current')
if mibBuilder.loadTexts: msdpPeerRemotePort.setDescription('The remote port for the TCP connection between the\n            MSDP peers.')
msdpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerLocalPort.setStatus('current')
if mibBuilder.loadTexts: msdpPeerLocalPort.setDescription('The local port for the TCP connection between the\n            MSDP peers.')
msdpPeerEncapsulationState = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("default", 1), ("received", 2), ("advertising", 3), ("sent", 4), ("agreed", 5), ("failed", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerEncapsulationState.setStatus('current')
if mibBuilder.loadTexts: msdpPeerEncapsulationState.setDescription('The status of the encapsulation negotiation state\n            machine.')
msdpPeerEncapsulationType = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tcp", 1), ("udp", 2), ("gre", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerEncapsulationType.setStatus('current')
if mibBuilder.loadTexts: msdpPeerEncapsulationType.setDescription('The encapsulation in use when encapsulating data in\n            SA messages to this peer.')
msdpPeerConnectionAttempts = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerConnectionAttempts.setStatus('current')
if mibBuilder.loadTexts: msdpPeerConnectionAttempts.setDescription('The number of times the state machine has\n            transitioned from inactive to connecting.')
msdpPeerInNotifications = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInNotifications.setStatus('current')
if mibBuilder.loadTexts: msdpPeerInNotifications.setDescription('The number of MSDP Notification messages received on\n            this connection.  This object should be initialized to\n            zero when the connection is established.')
msdpPeerOutNotifications = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutNotifications.setStatus('current')
if mibBuilder.loadTexts: msdpPeerOutNotifications.setDescription('The number of MSDP Notification messages transmitted\n            on this connection.  This object should be initialized\n            to zero when the connection is established.')
msdpPeerLastError = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 33), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2).clone(hexValue="0000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerLastError.setStatus('current')
if mibBuilder.loadTexts: msdpPeerLastError.setDescription('The last error code and subcode seen by this peer on\n            this connection.  If no error has occurred, this field\n            is zero.  Otherwise, the first byte of this two byte\n            OCTET STRING contains the error code, and the second\n            byte contains the subcode.')
msdpSACacheTable = MibTable((1, 3, 6, 1, 3, 92, 1, 1, 6), )
if mibBuilder.loadTexts: msdpSACacheTable.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheTable.setDescription("The (conceptual) table listing the MSDP SA\n            advertisements currently in the MSDP speaker's cache.")
msdpSACacheEntry = MibTableRow((1, 3, 6, 1, 3, 92, 1, 1, 6, 1), ).setIndexNames((0, "DRAFT-MSDP-MIB", "msdpSACacheGroupAddr"), (0, "DRAFT-MSDP-MIB", "msdpSACacheSourceAddr"), (0, "DRAFT-MSDP-MIB", "msdpSACacheOriginRP"))
if mibBuilder.loadTexts: msdpSACacheEntry.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheEntry.setDescription('An entry (conceptual row) representing an MSDP SA\n            advert.')
msdpSACacheGroupAddr = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: msdpSACacheGroupAddr.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheGroupAddr.setDescription('The group address of the SA Cache entry.')
msdpSACacheSourceAddr = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: msdpSACacheSourceAddr.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheSourceAddr.setDescription('The source address of the SA Cache entry.')
msdpSACacheOriginRP = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: msdpSACacheOriginRP.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheOriginRP.setDescription('The address of the RP which originated the last SA\n            message accepted for this entry.')
msdpSACachePeerLearnedFrom = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACachePeerLearnedFrom.setStatus('current')
if mibBuilder.loadTexts: msdpSACachePeerLearnedFrom.setDescription('The peer from which this SA Cache entry was last\n            accepted.  This address must correspond to the\n            msdpPeerRemoteAddress value for a row in the MSDP Peer\n            Table.')
msdpSACacheRPFPeer = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheRPFPeer.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheRPFPeer.setDescription('The peer from which an SA message corresponding to\n            this cache entry would be accepted (i.e. the RPF peer\n            for msdpSACacheOriginRP).  This may be different than\n            msdpSACachePeerLearnedFrom if this entry was created\n            by an MSDP SA-Response.  This address must correspond\n            to the msdpPeerRemoteAddress value for a row in the\n            MSDP Peer Table.')
msdpSACacheInSAs = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheInSAs.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheInSAs.setDescription('The number of MSDP SA messages received relevant to\n            this cache entry.  This object must be initialized to\n            zero when creating a cache entry.')
msdpSACacheInDataPackets = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheInDataPackets.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheInDataPackets.setDescription('The number of MSDP encapsulated data packets received\n            relevant to this cache entry.  This object must be\n            initialized to zero when creating a cache entry.')
msdpSACacheUpTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheUpTime.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheUpTime.setDescription('The time since this entry was placed in the SA\n            cache.')
msdpSACacheExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheExpiryTime.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheExpiryTime.setDescription('The time remaining before this entry will expire from\n            the SA cache.')
msdpSACacheStatus = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msdpSACacheStatus.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheStatus.setDescription("The status of this row in the table.  The only\n            allowable actions are to retreive the status, which\n            will be `active', or to set the status to `destroy' in\n            order to remove this entry from the cache.")
msdpTraps = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 7))
msdpEstablished = NotificationType((1, 3, 6, 1, 3, 92, 1, 1, 7, 1)).setObjects(("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTransitions"))
if mibBuilder.loadTexts: msdpEstablished.setStatus('current')
if mibBuilder.loadTexts: msdpEstablished.setDescription('The MSDP Established event is generated when the MSDP\n            FSM enters the ESTABLISHED state.')
msdpBackwardTransition = NotificationType((1, 3, 6, 1, 3, 92, 1, 1, 7, 2)).setObjects(("DRAFT-MSDP-MIB", "msdpPeerState"))
if mibBuilder.loadTexts: msdpBackwardTransition.setStatus('current')
if mibBuilder.loadTexts: msdpBackwardTransition.setDescription('The MSDPBackwardTransition Event is generated when\n            the MSDP FSM moves from a higher numbered state to a\n            lower numbered state.')
msdpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 8))
msdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 8, 1))
msdpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 8, 2))
msdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 92, 1, 1, 8, 1, 1)).setObjects(("DRAFT-MSDP-MIB", "msdpMIBGlobalsGroup"), ("DRAFT-MSDP-MIB", "msdpSACacheGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    msdpMIBCompliance = msdpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: msdpMIBCompliance.setDescription('The compliance statement for entities which implement\n            the MSDP MIB.')
msdpMIBGlobalsGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 1)).setObjects(("DRAFT-MSDP-MIB", "msdpEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    msdpMIBGlobalsGroup = msdpMIBGlobalsGroup.setStatus('current')
if mibBuilder.loadTexts: msdpMIBGlobalsGroup.setDescription('A collection of objects providing information on\n            global MSDP state.')
msdpMIBPeerGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 2)).setObjects(("DRAFT-MSDP-MIB", "msdpPeerRPFFailures"), ("DRAFT-MSDP-MIB", "msdpPeerState"), ("DRAFT-MSDP-MIB", "msdpPeerInSAs"), ("DRAFT-MSDP-MIB", "msdpPeerOutSAs"), ("DRAFT-MSDP-MIB", "msdpPeerInSARequests"), ("DRAFT-MSDP-MIB", "msdpPeerOutSARequests"), ("DRAFT-MSDP-MIB", "msdpPeerInSAResponses"), ("DRAFT-MSDP-MIB", "msdpPeerOutSAResponses"), ("DRAFT-MSDP-MIB", "msdpPeerInNotifications"), ("DRAFT-MSDP-MIB", "msdpPeerOutNotifications"), ("DRAFT-MSDP-MIB", "msdpPeerInControlMessages"), ("DRAFT-MSDP-MIB", "msdpPeerOutControlMessages"), ("DRAFT-MSDP-MIB", "msdpPeerInDataPackets"), ("DRAFT-MSDP-MIB", "msdpPeerOutDataPackets"), ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTransitions"), ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTime"), ("DRAFT-MSDP-MIB", "msdpPeerLocalAddress"), ("DRAFT-MSDP-MIB", "msdpPeerRemotePort"), ("DRAFT-MSDP-MIB", "msdpPeerLocalPort"), ("DRAFT-MSDP-MIB", "msdpPeerSAAdvPeriod"), ("DRAFT-MSDP-MIB", "msdpPeerConnectRetryInterval"), ("DRAFT-MSDP-MIB", "msdpPeerHoldTimeConfigured"), ("DRAFT-MSDP-MIB", "msdpPeerKeepAliveConfigured"), ("DRAFT-MSDP-MIB", "msdpPeerInMessageElapsedTime"), ("DRAFT-MSDP-MIB", "msdpPeerDataTtl"), ("DRAFT-MSDP-MIB", "msdpPeerProcessRequestsFrom"), ("DRAFT-MSDP-MIB", "msdpPeerEncapsulationState"), ("DRAFT-MSDP-MIB", "msdpPeerEncapsulationType"), ("DRAFT-MSDP-MIB", "msdpPeerConnectionAttempts"), ("DRAFT-MSDP-MIB", "msdpPeerLastError"), ("DRAFT-MSDP-MIB", "msdpPeerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    msdpMIBPeerGroup = msdpMIBPeerGroup.setStatus('current')
if mibBuilder.loadTexts: msdpMIBPeerGroup.setDescription('A collection of objects for managing MSDP peers.')
msdpSACacheGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 3)).setObjects(("DRAFT-MSDP-MIB", "msdpCacheLifetime"), ("DRAFT-MSDP-MIB", "msdpNumSACacheEntries"), ("DRAFT-MSDP-MIB", "msdpSAHoldDownPeriod"), ("DRAFT-MSDP-MIB", "msdpSACachePeerLearnedFrom"), ("DRAFT-MSDP-MIB", "msdpSACacheRPFPeer"), ("DRAFT-MSDP-MIB", "msdpSACacheInSAs"), ("DRAFT-MSDP-MIB", "msdpSACacheInDataPackets"), ("DRAFT-MSDP-MIB", "msdpSACacheUpTime"), ("DRAFT-MSDP-MIB", "msdpSACacheExpiryTime"), ("DRAFT-MSDP-MIB", "msdpSACacheStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    msdpSACacheGroup = msdpSACacheGroup.setStatus('current')
if mibBuilder.loadTexts: msdpSACacheGroup.setDescription('A collection of objects for managing MSDP SA cache\n            entries.')
mibBuilder.exportSymbols("DRAFT-MSDP-MIB", msdpSACacheRPFPeer=msdpSACacheRPFPeer, msdpPeerInControlMessages=msdpPeerInControlMessages, msdpPeerInSAResponses=msdpPeerInSAResponses, msdpPeerTable=msdpPeerTable, msdpMIBPeerGroup=msdpMIBPeerGroup, msdpPeerRemotePort=msdpPeerRemotePort, msdp=msdp, msdpPeerEncapsulationState=msdpPeerEncapsulationState, msdpMIBConformance=msdpMIBConformance, msdpSACacheSourceAddr=msdpSACacheSourceAddr, msdpSACacheOriginRP=msdpSACacheOriginRP, msdpTraps=msdpTraps, msdpPeerInSARequests=msdpPeerInSARequests, msdpPeerLocalPort=msdpPeerLocalPort, msdpBackwardTransition=msdpBackwardTransition, msdpRequestsGroupMask=msdpRequestsGroupMask, msdpSACacheUpTime=msdpSACacheUpTime, msdpSACacheExpiryTime=msdpSACacheExpiryTime, msdpSACacheStatus=msdpSACacheStatus, msdpEnabled=msdpEnabled, msdpPeerInDataPackets=msdpPeerInDataPackets, msdpPeerStatus=msdpPeerStatus, msdpSACacheInDataPackets=msdpSACacheInDataPackets, msdpPeerConnectionAttempts=msdpPeerConnectionAttempts, msdpSACacheGroupAddr=msdpSACacheGroupAddr, msdpPeerInNotifications=msdpPeerInNotifications, msdpSACacheTable=msdpSACacheTable, msdpMIBobjects=msdpMIBobjects, msdpPeerKeepAliveConfigured=msdpPeerKeepAliveConfigured, msdpRequestsTable=msdpRequestsTable, msdpPeerRPFFailures=msdpPeerRPFFailures, msdpPeerRemoteAddress=msdpPeerRemoteAddress, msdpPeerOutSAResponses=msdpPeerOutSAResponses, msdpNumSACacheEntries=msdpNumSACacheEntries, msdpMIBGroups=msdpMIBGroups, msdpPeerState=msdpPeerState, msdpPeerProcessRequestsFrom=msdpPeerProcessRequestsFrom, msdpMIBCompliances=msdpMIBCompliances, msdpSACacheGroup=msdpSACacheGroup, msdpRequestsPeer=msdpRequestsPeer, msdpPeerOutSAs=msdpPeerOutSAs, msdpPeerFsmEstablishedTransitions=msdpPeerFsmEstablishedTransitions, msdpPeerDataTtl=msdpPeerDataTtl, msdpSACachePeerLearnedFrom=msdpSACachePeerLearnedFrom, msdpPeerEntry=msdpPeerEntry, msdpEstablished=msdpEstablished, msdpRequestsEntry=msdpRequestsEntry, msdpPeerLastError=msdpPeerLastError, msdpRequestsStatus=msdpRequestsStatus, msdpPeerOutControlMessages=msdpPeerOutControlMessages, PYSNMP_MODULE_ID=msdpMIB, msdpPeerOutSARequests=msdpPeerOutSARequests, msdpPeerOutDataPackets=msdpPeerOutDataPackets, msdpPeerLocalAddress=msdpPeerLocalAddress, msdpPeerHoldTimeConfigured=msdpPeerHoldTimeConfigured, msdpSACacheInSAs=msdpSACacheInSAs, msdpSACacheEntry=msdpSACacheEntry, msdpPeerConnectRetryInterval=msdpPeerConnectRetryInterval, msdpPeerEncapsulationType=msdpPeerEncapsulationType, msdpPeerInSAs=msdpPeerInSAs, msdpRequestsGroupAddress=msdpRequestsGroupAddress, msdpMIBGlobalsGroup=msdpMIBGlobalsGroup, msdpPeerOutNotifications=msdpPeerOutNotifications, msdpMIB=msdpMIB, msdpMIBCompliance=msdpMIBCompliance, msdpPeerFsmEstablishedTime=msdpPeerFsmEstablishedTime, msdpPeerInMessageElapsedTime=msdpPeerInMessageElapsedTime, msdpCacheLifetime=msdpCacheLifetime, msdpPeerSAAdvPeriod=msdpPeerSAAdvPeriod, msdpSAHoldDownPeriod=msdpSAHoldDownPeriod)
