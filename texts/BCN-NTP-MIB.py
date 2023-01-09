#
# PySNMP MIB module BCN-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-NTP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:47 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Bits, Counter32, ObjectIdentity, Counter64, NotificationType, TimeTicks, ModuleIdentity, Integer32, IpAddress, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Bits", "Counter32", "ObjectIdentity", "Counter64", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "IpAddress", "Gauge32", "Unsigned32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
bcnNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 1))
bcnNtpMIB.setRevisions(('2010-12-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnNtpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnNtpMIB.setLastUpdated('201012150000Z')
if mibBuilder.loadTexts: bcnNtpMIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnNtpMIB.setContactInfo('BlueCat Networks. Customer Care.\n\n        North America\n        Call: +1.866.491.2228\n        Europe\n        Call: +44.8081.011.306\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnNtpMIB.setDescription('This module provides status as well as statistical information\n        about the NTP service.\n\n\t\tMost of the OIDs defined on this MIB are based on the work done by\n        A.S. Sethi and Dave Mills in the University of Delaware and published\n        as:\n\t\tManagement of the Network Time Protocol (NTP) with SNMP\n        Technical Report No. 98-09\n        Other references used in the creation of this MIB are RFC-1305 and\n        RFC-5905')
bcnNtp = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4))
bcnNtpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2))
bcnNtpNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3))
bcnNtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4))
class NTPTimeStamp(TextualConvention, OctetString):
    reference = "D.L. Mills, University of Delaware,\n\t\t'Network Time Protocol(Version 3)',\n        RFC-1305, March 1992, Section 3.1"
    description = 'NTP timestamps are represented as a 64-bit\n        unsigned fixed-point number, in seconds relative to\n        00:00 on 1 January 1900.  The integer part is in the\n        first 32 bits and the fraction part is in the last\n        32 bits.'
    status = 'current'
    displayHint = '4x.4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(TextualConvention, Integer32):
    reference = "D.L. Mills, University of Delaware,\n\t\t'Network Time Protocol(Version 3)',\n        RFC-1305, March 1992, Section 3.2.1"
    description = 'This is a two-bit code warning of an impending leap second to be\n         inserted in the NTP timescale. The bits are set before 23:59 on\n         the day of insertion and reset after 00:00 on the following day.\n         This causes the number of seconds (rollover interval) in the day\n         of insertion to be increased or decreased by one. In the case of \n         primary servers the bits are set by operator intervention, while\n         in the case of secondary servers the bits are set by the protocol.\n         The two bits, bit 0 and bit 1, respectively, are coded as follows:\n            00, no warning\n            01, last minute has 61 seconds\n            10, last minute has 59 seconds\n            11, alarm condition (clock not synchronized)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPRefId(TextualConvention, OctetString):
    reference = "D.L. Mills, University of Delaware,\n\t\t'Network Time Protocol(Version 3)',\n         RFC-5905, June 2010, Section 7.3"
    description = '32-bit code identifying the particular server or reference clock.\n        The interpretation depends on the value in the stratum field. For\n        packet stratum 0 (unspecified or invalid), this is a four-character\n        ASCII string. For stratum 1 (reference clock), this is a four-octet,\n        left-justified, zero-padded ASCII string assigned to the reference\n        clock.\n        Above stratum 1 (secondary servers and clients): this is the\n        reference identifier of the server and can be used to detect timing\n        loops. If using the IPv4 address family, the identifier is the four-\n        octet IPv4 address. If using the IPv6 address family, it is the first\n        four octets of the MD5 hash of the IPv6 address.'
    status = 'current'
    displayHint = '4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

bcnNtpServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 1))
if mibBuilder.loadTexts: bcnNtpServiceStatus.setStatus('current')
if mibBuilder.loadTexts: bcnNtpServiceStatus.setDescription('General state of the NTP Service.')
bcnNtpSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSerOperState.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSerOperState.setDescription('Operational state of the Service. The possible states are:\n        running(1)    The service is running normally.\n        notRunning(2) The service is stopped either intentionally (i.e.:\n                      the service is not supposed to run on this node) or\n                      unintentionally (a problem has occurred).\n        starting(3)   The service is in the process of starting, either\n                      for the first time of after an event occurred.\n        stopping(4)   The service is in the process of stopping. Stopping\n                      a service might be necessary after a configuration\n                      change.\n        fault(5)      An error has been detected and the state is undefined.\n        ')
bcnNtpSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2))
if mibBuilder.loadTexts: bcnNtpSystem.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSystem.setDescription('General NTP system information.')
bcnNtpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 1), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysLeap.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysLeap.setDescription('Two-bit code warning of an impending leap\n         second to be inserted in the NTP timescale.')
bcnNtpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysStratum.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysStratum.setDescription('Indicating the stratum of the local clock.\n         0, unspecified\n         1, primary reference (e.g., calibrated atomic clock, radio clock)\n         2-255, secondary reference (via NTP)')
bcnNtpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysPrecision.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysPrecision.setDescription('Signed integer indicating the precision of the various clocks,\n        in seconds to the nearest power\n        of two.')
bcnNtpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRootDelay.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysRootDelay.setDescription('The total roundtrip delay to the primary reference source at the\n        root of the synchronization subnet, in seconds.\n        This is an ASCII string representing a floating point number.')
bcnNtpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRootDispersion.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysRootDispersion.setDescription('The maximum error relative to the primary reference source at the\n        root of the synchronization subnet, in seconds. Only positive values\n        greater than zero are possible.\n        This is an ASCII string representing a floating point number.')
bcnNtpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRefId.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysRefId.setDescription('The particular reference clock.')
bcnNtpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRefTime.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysRefTime.setDescription('The local time when the local clock was last updated. If the\n        local clock has never been synchronized, the value is zero.')
bcnNtpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysPoll.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysPoll.setDescription('The minimum interval between transmitted\n        messages, in seconds as a power of two. For instance,\n        a value of six indicates a minimum interval of 64 seconds.')
bcnNtpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysPeer.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysPeer.setDescription('The current synchronization source. This is the association ID\n        of the system peer. The special value NULL indicates there is no\n        currently valid synchronization source.')
bcnNtpSysFreq = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysFreq.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysFreq.setDescription('The clock frequency offset (PPM)\n        This is an ASCII string representing a floating point number.')
bcnNtpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 11), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysClock.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysClock.setDescription('The current local time. Local time is derived from the hardware\n        clock of the particular machine and increments at intervals\n        depending on the design used.')
bcnNtpSysSystem = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysSystem.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysSystem.setDescription('The type of the local Operating System')
bcnNtpSysProcessor = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysProcessor.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysProcessor.setDescription('The type of the local Processor')
bcnNtpSysJitter = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysJitter.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSysJitter.setDescription("Indicates how much the individual pulses vary from second to \n        second (as measured by the operating system's clock).\n        This is an ASCII string representing a floating point number.")
bcnNtpPeers = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3))
if mibBuilder.loadTexts: bcnNtpPeers.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeers.setDescription('NTP peers information.')
bcnNtpPeersVarTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1), )
if mibBuilder.loadTexts: bcnNtpPeersVarTable.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersVarTable.setDescription('A table listing the peers known to the server as well as summary\n        information of their state.')
bcnNtpPeersVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1), ).setIndexNames((0, "BCN-NTP-MIB", "bcnNtpPeersAssocId"))
if mibBuilder.loadTexts: bcnNtpPeersVarEntry.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersVarEntry.setDescription('A logical row in the bcnNtpPeersVarTable.')
bcnNtpPeersAssocId = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnNtpPeersAssocId.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersAssocId.setDescription('Association ID of the peer.')
bcnNtpPeersConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersConfigured.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersConfigured.setDescription('This is a bit indicating that the association\n         was created from configuration information and should not\n         be demobilized if the peer becomes unreachable.')
bcnNtpPeersPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerAddressType.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersPeerAddressType.setDescription('The Internet address type of the peer.')
bcnNtpPeersPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerAddress.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersPeerAddress.setDescription('The Internet address of the peer.')
bcnNtpPeersPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 5), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerPort.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersPeerPort.setDescription('16-bit port number of the peer.')
bcnNtpPeersHostAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostAddressType.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersHostAddressType.setDescription('The Internet address type of the host.')
bcnNtpPeersHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostAddress.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersHostAddress.setDescription('The Internet address of the host.')
bcnNtpPeersHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 8), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostPort.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersHostPort.setDescription('16-bit port number of the host.')
bcnNtpPeersLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 9), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersLeap.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersLeap.setDescription('Two-bit code warning of an impending leap\n         second to be inserted in the NTP timescale.')
bcnNtpPeersMode = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersMode.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersMode.setDescription('The association mode,with values coded as\n         follows:\n         0, unspecified\n         1, symmetric active\n         2, symmetric passive\n         3, client\n         4, server\n         5, broadcast\n         6, reserved for NTP control messages\n         7, reserved for private use')
bcnNtpPeersStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersStratum.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersStratum.setDescription('Indicates the stratum of the peer clock.\n         0, unspecified\n         1, primary reference (e.g., calibrated atomic clock, radio clock)\n         2-255, secondary reference (via NTP)')
bcnNtpPeersPeerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerPoll.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersPeerPoll.setDescription('Poll interval of the peer')
bcnNtpPeersHostPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostPoll.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersHostPoll.setDescription('Poll interval of the host')
bcnNtpPeersPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPrecision.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersPrecision.setDescription('The same as the systemPrecision except this is for the peer.')
bcnNtpPeersRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRootDelay.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersRootDelay.setDescription('The same as the systemRootDealy except this is for the peer.')
bcnNtpPeersRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRootDispersion.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersRootDispersion.setDescription('The same as the systemDispersion except this is for the peer.')
bcnNtpPeersRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 17), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRefId.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersRefId.setDescription('The same as the systemRefid except this is for the peer.')
bcnNtpPeersRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 18), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRefTime.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersRefTime.setDescription('The same as the systemRefTime except this is for the peer.')
bcnNtpPeersOrgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 19), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersOrgTime.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersOrgTime.setDescription('The local time at the peer when its latest\n         NTP message was sent. If the peer becomes unreachable the\n         value is set to zero.')
bcnNtpPeersReceiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 20), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersReceiveTime.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersReceiveTime.setDescription('The local time when the latest NTP message\n         from the peer arrived. If the peer becomes unreachable the\n         value is set to zero.')
bcnNtpPeersTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 21), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersTransmitTime.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersTransmitTime.setDescription('The local time at which the NTP message departed the sender.')
bcnNtpPeersReach = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersReach.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersReach.setDescription('A shift register of NTP.WINDOW bits used to determine\n        the reachability status of the peer, with bits entering\n        from the least significant (rightmost) end. A peer is\n        considered reachable if at least one bit in this register is\n        set to one.')
bcnNtpPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersOffset.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersOffset.setDescription('Filter offset.\n        This is an ASCII string representing a floating point number.')
bcnNtpPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersDelay.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersDelay.setDescription('Filter delay.\n        This is an ASCII string representing a floating point number.')
bcnNtpPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersDispersion.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersDispersion.setDescription('Filter dispersion.\n        This is an ASCII string representing a floating point number.')
bcnNtpPeersJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersJitter.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersJitter.setDescription("bcnNtpPeersJitter indicates how much the individual pulses vary\n        from second to second (as measured by the operating system's clock).\n        This is an ASCII string representing a floating point number.")
bcnNtpNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 0))
bcnNtpNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1))
bcnNtpAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnNtpAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: bcnNtpAlarmSeverity.setDescription('Severity classification for the alarm.')
bcnNtpAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnNtpAlarmInfo.setStatus('current')
if mibBuilder.loadTexts: bcnNtpAlarmInfo.setDescription('Descriptive information about the alarm event.')
bcnNtpAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 0, 1)).setObjects(("BCN-NTP-MIB", "bcnNtpSerOperState"), ("BCN-NTP-MIB", "bcnNtpAlarmSeverity"), ("BCN-NTP-MIB", "bcnNtpAlarmInfo"))
if mibBuilder.loadTexts: bcnNtpAlarmNotif.setStatus('current')
if mibBuilder.loadTexts: bcnNtpAlarmNotif.setDescription('A bcnNtpAlarmNotif signifies that the NTP service has transitioned\n        state or a particular event has been detected on the service.')
bcnNtpServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 1))
bcnNtpServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2))
bcnNtpServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 1)).setObjects(("BCN-NTP-MIB", "bcnNtpSerOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpServiceStatusGroup = bcnNtpServiceStatusGroup.setStatus('current')
if mibBuilder.loadTexts: bcnNtpServiceStatusGroup.setDescription('Status conformance.')
bcnNtpSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 2)).setObjects(("BCN-NTP-MIB", "bcnNtpSysLeap"), ("BCN-NTP-MIB", "bcnNtpSysStratum"), ("BCN-NTP-MIB", "bcnNtpSysPrecision"), ("BCN-NTP-MIB", "bcnNtpSysRootDelay"), ("BCN-NTP-MIB", "bcnNtpSysRootDispersion"), ("BCN-NTP-MIB", "bcnNtpSysRefId"), ("BCN-NTP-MIB", "bcnNtpSysRefTime"), ("BCN-NTP-MIB", "bcnNtpSysPoll"), ("BCN-NTP-MIB", "bcnNtpSysPeer"), ("BCN-NTP-MIB", "bcnNtpSysFreq"), ("BCN-NTP-MIB", "bcnNtpSysClock"), ("BCN-NTP-MIB", "bcnNtpSysSystem"), ("BCN-NTP-MIB", "bcnNtpSysProcessor"), ("BCN-NTP-MIB", "bcnNtpSysJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpSystemGroup = bcnNtpSystemGroup.setStatus('current')
if mibBuilder.loadTexts: bcnNtpSystemGroup.setDescription('System variables conformance.')
bcnNtpPeersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 3)).setObjects(("BCN-NTP-MIB", "bcnNtpPeersConfigured"), ("BCN-NTP-MIB", "bcnNtpPeersPeerAddressType"), ("BCN-NTP-MIB", "bcnNtpPeersPeerAddress"), ("BCN-NTP-MIB", "bcnNtpPeersPeerPort"), ("BCN-NTP-MIB", "bcnNtpPeersHostAddressType"), ("BCN-NTP-MIB", "bcnNtpPeersHostAddress"), ("BCN-NTP-MIB", "bcnNtpPeersHostPort"), ("BCN-NTP-MIB", "bcnNtpPeersLeap"), ("BCN-NTP-MIB", "bcnNtpPeersMode"), ("BCN-NTP-MIB", "bcnNtpPeersStratum"), ("BCN-NTP-MIB", "bcnNtpPeersPeerPoll"), ("BCN-NTP-MIB", "bcnNtpPeersHostPoll"), ("BCN-NTP-MIB", "bcnNtpPeersPrecision"), ("BCN-NTP-MIB", "bcnNtpPeersRootDelay"), ("BCN-NTP-MIB", "bcnNtpPeersRootDispersion"), ("BCN-NTP-MIB", "bcnNtpPeersRefId"), ("BCN-NTP-MIB", "bcnNtpPeersRefTime"), ("BCN-NTP-MIB", "bcnNtpPeersOrgTime"), ("BCN-NTP-MIB", "bcnNtpPeersReceiveTime"), ("BCN-NTP-MIB", "bcnNtpPeersTransmitTime"), ("BCN-NTP-MIB", "bcnNtpPeersReach"), ("BCN-NTP-MIB", "bcnNtpPeersOffset"), ("BCN-NTP-MIB", "bcnNtpPeersDelay"), ("BCN-NTP-MIB", "bcnNtpPeersDispersion"), ("BCN-NTP-MIB", "bcnNtpPeersJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpPeersGroup = bcnNtpPeersGroup.setStatus('current')
if mibBuilder.loadTexts: bcnNtpPeersGroup.setDescription('Peer variables conformance.')
bcnNtpNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 4)).setObjects(("BCN-NTP-MIB", "bcnNtpAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpNotificationEventGroup = bcnNtpNotificationEventGroup.setStatus('current')
if mibBuilder.loadTexts: bcnNtpNotificationEventGroup.setDescription('Server statistics conformance.')
bcnNtpNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 5)).setObjects(("BCN-NTP-MIB", "bcnNtpAlarmSeverity"), ("BCN-NTP-MIB", "bcnNtpAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpNotificationDataGroup = bcnNtpNotificationDataGroup.setStatus('current')
if mibBuilder.loadTexts: bcnNtpNotificationDataGroup.setDescription('Server statistics conformance.')
bcnNtpStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 1, 1)).setObjects(("BCN-NTP-MIB", "bcnNtpServiceStatusGroup"), ("BCN-NTP-MIB", "bcnNtpSystemGroup"), ("BCN-NTP-MIB", "bcnNtpPeersGroup"), ("BCN-NTP-MIB", "bcnNtpNotificationEventGroup"), ("BCN-NTP-MIB", "bcnNtpNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpStatusCompliance = bcnNtpStatusCompliance.setStatus('current')
if mibBuilder.loadTexts: bcnNtpStatusCompliance.setDescription('Basic conformance')
mibBuilder.exportSymbols("BCN-NTP-MIB", bcnNtpPeersPeerAddress=bcnNtpPeersPeerAddress, bcnNtpSysRootDispersion=bcnNtpSysRootDispersion, bcnNtpSystem=bcnNtpSystem, bcnNtpPeersPeerPort=bcnNtpPeersPeerPort, bcnNtpPeersRefTime=bcnNtpPeersRefTime, bcnNtpPeersHostPort=bcnNtpPeersHostPort, bcnNtpServiceCompliances=bcnNtpServiceCompliances, bcnNtpSysProcessor=bcnNtpSysProcessor, bcnNtpSysLeap=bcnNtpSysLeap, bcnNtpPeersOrgTime=bcnNtpPeersOrgTime, bcnNtpPeersOffset=bcnNtpPeersOffset, bcnNtpServiceStatusGroup=bcnNtpServiceStatusGroup, NTPRefId=NTPRefId, bcnNtpPeersPeerPoll=bcnNtpPeersPeerPoll, NTPTimeStamp=NTPTimeStamp, bcnNtpPeersConfigured=bcnNtpPeersConfigured, bcnNtpPeersLeap=bcnNtpPeersLeap, bcnNtpPeersRootDelay=bcnNtpPeersRootDelay, bcnNtpNotificationEvents=bcnNtpNotificationEvents, bcnNtpSysClock=bcnNtpSysClock, bcnNtpPeersHostAddressType=bcnNtpPeersHostAddressType, bcnNtpAlarmInfo=bcnNtpAlarmInfo, bcnNtpSysPoll=bcnNtpSysPoll, bcnNtpPeersStratum=bcnNtpPeersStratum, bcnNtpPeersPrecision=bcnNtpPeersPrecision, bcnNtp=bcnNtp, bcnNtpPeersAssocId=bcnNtpPeersAssocId, bcnNtpPeersVarTable=bcnNtpPeersVarTable, bcnNtpMIB=bcnNtpMIB, bcnNtpPeers=bcnNtpPeers, bcnNtpPeersReceiveTime=bcnNtpPeersReceiveTime, NTPLeapIndicator=NTPLeapIndicator, PYSNMP_MODULE_ID=bcnNtpMIB, bcnNtpNotificationData=bcnNtpNotificationData, bcnNtpSysRefTime=bcnNtpSysRefTime, bcnNtpPeersHostAddress=bcnNtpPeersHostAddress, bcnNtpSysPrecision=bcnNtpSysPrecision, bcnNtpNotification=bcnNtpNotification, bcnNtpAlarmSeverity=bcnNtpAlarmSeverity, bcnNtpPeersRootDispersion=bcnNtpPeersRootDispersion, bcnNtpServiceStatus=bcnNtpServiceStatus, bcnNtpPeersDispersion=bcnNtpPeersDispersion, bcnNtpPeersMode=bcnNtpPeersMode, bcnNtpPeersHostPoll=bcnNtpPeersHostPoll, bcnNtpNotificationEventGroup=bcnNtpNotificationEventGroup, bcnNtpStatusCompliance=bcnNtpStatusCompliance, bcnNtpSysFreq=bcnNtpSysFreq, bcnNtpPeersDelay=bcnNtpPeersDelay, bcnNtpSysJitter=bcnNtpSysJitter, bcnNtpPeersVarEntry=bcnNtpPeersVarEntry, bcnNtpSystemGroup=bcnNtpSystemGroup, bcnNtpPeersGroup=bcnNtpPeersGroup, bcnNtpPeersPeerAddressType=bcnNtpPeersPeerAddressType, bcnNtpServiceGroups=bcnNtpServiceGroups, bcnNtpSysRootDelay=bcnNtpSysRootDelay, bcnNtpPeersReach=bcnNtpPeersReach, bcnNtpSerOperState=bcnNtpSerOperState, bcnNtpPeersRefId=bcnNtpPeersRefId, bcnNtpNotificationDataGroup=bcnNtpNotificationDataGroup, bcnNtpConformance=bcnNtpConformance, bcnNtpPeersJitter=bcnNtpPeersJitter, bcnNtpSysRefId=bcnNtpSysRefId, bcnNtpObjects=bcnNtpObjects, bcnNtpSysPeer=bcnNtpSysPeer, bcnNtpAlarmNotif=bcnNtpAlarmNotif, bcnNtpSysStratum=bcnNtpSysStratum, bcnNtpPeersTransmitTime=bcnNtpPeersTransmitTime, bcnNtpSysSystem=bcnNtpSysSystem)
