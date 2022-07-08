#
# PySNMP MIB module DOCS-SUBMGT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/DOCS-SUBMGT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:07 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
docsIfCmtsCmStatusIndex, docsIfCmtsCmStatusEntry = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusIndex", "docsIfCmtsCmStatusEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Integer32, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Gauge32, IpAddress, Counter32, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Integer32", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Gauge32", "IpAddress", "Counter32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Unsigned32")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
docsSubMgt = ModuleIdentity((1, 3, 6, 1, 3, 83, 4))
if mibBuilder.loadTexts: docsSubMgt.setLastUpdated('0007120000Z')
if mibBuilder.loadTexts: docsSubMgt.setOrganization('IETF IPCDN Working Group')
if mibBuilder.loadTexts: docsSubMgt.setContactInfo('        Wilson Sawyer\n                Postal: Arris Interactive\n                        6 Riverside Drive\n                        Andover, MA 01810\n                        U.S.A.\n                Phone:  +1 978 946 4711\n                E-mail: wsawyer@ieee.org')
if mibBuilder.loadTexts: docsSubMgt.setDescription('This is the CMTS centric subscriber management MIB for\n           DOCSIS compliant CMTS.  This will be rooted in experimental\n           space with a future transition to be incorporated into the\n           cable device MIB.')
docsSubMgtObjects = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 1))
class IpV4orV6Addr(TextualConvention, OctetString):
    description = 'An IP V4 or V6 address expressed as an octet string.  The\n       zero length string is equal to both 0.0.0.0 and the IPv6 :0\n       address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
docsSubMgtCpeControlTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 1), )
if mibBuilder.loadTexts: docsSubMgtCpeControlTable.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeControlTable.setDescription('This table extends the docsIfCmtsCmStatusTable and adds 4\n\n\n       objects which reflect the state of subscriber management on a\n       particular CM.')
docsSubMgtCpeControlEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 1, 1), )
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlEntry"))
docsSubMgtCpeControlEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsSubMgtCpeControlEntry.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeControlEntry.setDescription('A row in the docsSubMgtCpeControlTable.  All the values\n       are either set from the system default, or are set from objects\n       included in the DOCSIS registration request sent upstream to\n       the CMTS from the CM.')
docsSubMgtCpeControlMaxCpeIp = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlMaxCpeIp.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeControlMaxCpeIp.setDescription('The number of simultaneous IP addresses permitted behind\n       the CM. If this is set to zero, all CPE traffic from the CM is\n       dropped.  If the provisioning object corresponding to\n       docsSubMgtCpeIpTable includes more CPE IP address entries for\n       this modem than the value of this object, then this object is\n       set to the count of the number of rows in docsSubMgtCpeIpTable\n       that have the same docsIfCmtsCmStatusIndex value. (E.g. if the\n       CM has 5 IP addresses specified for it, this value is 5). This\n       limit applies to learned and docsis-provisioned entries, but\n       does not limit entries added through some administrative\n       process at the CMTS. If not set through DOCSIS provisioning,\n       this object defaults to docsSubMgtCpeMaxIpDefault. Note that\n       this object is only meaningful if docsSubMgtCpeControlActive\n       is true.')
docsSubMgtCpeControlActive = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlActive.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeControlActive.setDescription('If this is set to true, CMTS based CPE control is active and\n       all the actions required by the various filter tables and\n\n\n       controls apply at the CMTS.  If this is set to false, no\n       subscriber management filtering is done at the CMTS (but other\n       filters may apply). If not set through DOCSIS provisioning,\n       this object defaults to docsSubMgtCpeActiveDefault.')
docsSubMgtCpeControlLearnable = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlLearnable.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeControlLearnable.setDescription('If this is set to true, the CMTS may learn up to\n       docsSubMgtMaxCpeIp addresses (less any DOCSIS-provisioned\n       entries) related to this CM.  Those IP addresses are added (by\n       internal process) to the docsSubMgtCpeIpTable. The nature of the\n       learning mechanism is not specified here. If not set through\n       DOCSIS provisioning, this object defaults to\n       docsSubMgtCpeLearnableDefault. Note that this object is only\n       meaningful if docsSubMgtCpeControlActive is true.')
docsSubMgtCpeControlReset = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlReset.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeControlReset.setDescription("This object always returns false on read.  If this object is\n       set to true, the rows with  'learned' addresses in\n       docsSubMgtCpeIpTable for this CM are deleted from that table.")
docsSubMgtCpeMaxIpDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeMaxIpDefault.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeMaxIpDefault.setDescription('The default value for docsSubMgtCpeControlMaxCpeIp if not\n       signaled in the DOCSIS Registration request. Upon initial CMTS\n       initialization, this defaults to 16.')
docsSubMgtCpeActiveDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeActiveDefault.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeActiveDefault.setDescription('The default value for docsSubMgtCpeControlActive if not\n       signaled in the DOCSIS Registration request. Upon initial CMTS\n       initialization, this defaults to false.')
docsSubMgtCpeLearnableDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeLearnableDefault.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeLearnableDefault.setDescription('The default value for docsSubMgtCpeControlLearnable if not\n       signaled in the DOCSIS Registration request. Upon initial CMTS\n       initialization, this defaults to true.')
docsSubMgtCpeIpTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 5), )
if mibBuilder.loadTexts: docsSubMgtCpeIpTable.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeIpTable.setDescription('A table of CPE IP addresses known on a per CM basis.')
docsSubMgtCpeIpEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 5, 1), ).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"), (0, "DOCS-SUBMGT-MIB", "docsSubMgtCpeIpIndex"))
if mibBuilder.loadTexts: docsSubMgtCpeIpEntry.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeIpEntry.setDescription("An entry in the docsSubMgtCpeIpTable.  The first index is\n       the specific modem we're referring to, the second index is the\n       specific CPE IP entry.")
docsSubMgtCpeIpIndex = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: docsSubMgtCpeIpIndex.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeIpIndex.setDescription('The index of this CPE IP address relative to the indexed CM.\n       An entry is created either through the included CPE IP addresses\n       in the provisioning object, or via learning.  If a CMTS receives\n       an IP packet from a CM that contains a source IP address which\n       does not match one of the docsSubMgtCpeIpAddr entries for this\n       CM, one of two things occurs.  If the number of entries is less\n       than docsSubMgtCpeControlMaxCpeIp, the source address is added to\n       the table and the packet is forwarded.  If the number of entries\n       equals the docsSubMgtCpeControlMaxCpeIp, AND\n       docsSubMgtCpeControlActive is true, then the packet is dropped.\n       Otherwise the packet is forwarded. ')
docsSubMgtCpeIpAddr = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 2), IpV4orV6Addr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeIpAddr.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeIpAddr.setDescription('The IP address either set from provisioning or learned via\n       wiretapping. See docsSubMgtCpeIpIndex for the mechanism.')
docsSubMgtCpeIpLearned = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeIpLearned.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCpeIpLearned.setDescription('If true, this entry was learned from IP packets sent\n       upstream rather than from the provisioning objects.')
docsSubMgtPktFilterTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 6), )
if mibBuilder.loadTexts: docsSubMgtPktFilterTable.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterTable.setDescription('A table of filter or classifier criteria. Classifiers are\n       assigned by group to the individual CMs.  That assignment is made\n       via the configuration objects sent upstream from the CM to the\n       CMTS during registration.')
docsSubMgtPktFilterEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 6, 1), ).setIndexNames((0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterGroup"), (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterIndex"))
if mibBuilder.loadTexts: docsSubMgtPktFilterEntry.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterEntry.setDescription('An entry in the docsSubMgtPktFilterTable.')
docsSubMgtPktFilterGroup = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: docsSubMgtPktFilterGroup.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterGroup.setDescription('Identifies an ordered group of filters. Each modem may be\n       associated with a filter group for its upstream traffic\n       (docsSubMgtCmFilterUpstream) and a filter group for its\n       downstream traffic (docsSubMgtCmFilterDownstream). Typically,\n       many modems will use the same filter group.')
docsSubMgtPktFilterIndex = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: docsSubMgtPktFilterIndex.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterIndex.setDescription('An index which describes the ordering of a set of filter\n       specifications within the group.  Filters are applied in index\n       order.')
docsSubMgtPktFilterSrcAddr = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 3), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterSrcAddr.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterSrcAddr.setDescription("The source IP address to match in the packet to be\n       classified.  By default, this is the all-zero's IP v4 and v6\n       address. A packet matches the SrcAddr filter if the following is\n       true:\n            AND (FilterSrcAddr, FilterSrcMask) ==\n            AND (Packet SrcAddr, FilterSrcMask).\n       The mask value is applied to both the match value in this table\n       and to the packet IP address.")
docsSubMgtPktFilterSrcMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 4), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterSrcMask.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterSrcMask.setDescription("A bit mask that is to be applied to the source address\n       prior to matching. This, taken with the SrcAddr specifies a\n       matching criteria.  By default, the pair specifies a filter\n       which matches all source addresses. This mask is not\n       necessarily the same as a subnet mask, but for IPv4 addresses\n       the 1's bits must be leftmost and contiguous. IPv6 masks have\n       no such restriction.")
docsSubMgtPktFilterDstAddr = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 5), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterDstAddr.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterDstAddr.setDescription("The destination IP address to match in the packet to be\n       classified.  By default, this is the all-zero's IP v4 and v6\n       address. A packet matches the DstAddr filter if the following is\n       true:\n            AND (FilterDstAddr, FilterDstMask) ==\n            AND (Packet DstAddr, FilterDstMask).\n       The mask value is applied to both the match value in this table\n       and to the packet IP address.")
docsSubMgtPktFilterDstMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 6), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterDstMask.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterDstMask.setDescription("A bit mask that is to be applied to the destination\n       address prior to matching. This, taken with the DstAddr\n       specifies a matching criteria.  By default, the pair specifies\n       a filter which matches all destination addresses. This mask is\n       not necessarily the same as a subnet mask, but for IPv4\n       addresses the 1's bits must be leftmost and contiguous. IPv6\n       masks have no such restriction.")
docsSubMgtPktFilterUlp = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterUlp.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterUlp.setDescription('Upper level protocol to match.  If this value is 256,\n       matches ALL ULP values.  Otherwise, this matches the specific\n       protocol value.  Note that if the packet ULP is either 6 (tcp) or\n       17 (udp), then docsSubMgtPktTcpUdpFilterTable must also be\n       consulted (if its entry exists) to see if this entry matches.\n\n\n       Obviously, if this value is neither tcp, udp nor 256, then that\n       table need not be matched against.')
docsSubMgtPktFilterTosValue = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="0")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterTosValue.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterTosValue.setDescription('The TOS value to match in the IP packet.')
docsSubMgtPktFilterTosMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="0")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterTosMask.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterTosMask.setDescription('The mask to apply against the TOS value to be matched in the\n       IP packet.  The default for both these objects taken together\n       matches all TOS values. A packet matches this filter if the\n       following is true:\n           AND (FilterTosValue, FilterTosMask) ==\n           AND (Packet TOS Value, FilterTosMask).')
docsSubMgtPktFilterAction = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accept", 1), ("drop", 2))).clone('accept')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterAction.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterAction.setDescription('The action to take upon this filter matching.  Accept means\n       to accept the packet for further processing.  Drop means to drop\n       the packet.')
docsSubMgtPktFilterMatches = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtPktFilterMatches.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterMatches.setDescription('This object counts the number of times this specific rule\n       has been matched.  This is incremented any time this rule is\n       encountered and all components match. It is only incremented for\n       the first (lowest-indexed) filter matching a packet.')
docsSubMgtPktFilterStatus = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterStatus.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtPktFilterStatus.setDescription('Standard rowStatus object for creating this row.  Any object\n       in this row which is writable may be changed at any time while\n       the row is active.')
docsSubMgtTcpUdpFilterTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 7), )
if mibBuilder.loadTexts: docsSubMgtTcpUdpFilterTable.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtTcpUdpFilterTable.setDescription("This is an adjunct to docsSubMgtPktFilterTable. It provides\n            optional filtering based on elements in TCP or UDP headers.\n            This table is separate from docsSubMgtPktFilterTable only\n            because it is expected to be used more rarely. This table\n            is not consulted unless the upper-layer protocol is TCP,\n            UDP, or 'any'.")
docsSubMgtTcpUdpFilterEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 7, 1), ).setIndexNames((0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterGroup"), (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterIndex"))
if mibBuilder.loadTexts: docsSubMgtTcpUdpFilterEntry.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtTcpUdpFilterEntry.setDescription('Defines filtering criteria for TCP and UDP headers.')
docsSubMgtTcpUdpSrcPort = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536)).clone(65536)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpUdpSrcPort.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtTcpUdpSrcPort.setDescription('The source port to match.  65536 matches any value in the\n       TCP or UDP source port field.')
docsSubMgtTcpUdpDstPort = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536)).clone(65536)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpUdpDstPort.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtTcpUdpDstPort.setDescription('The destination port to match.  65536 matches any value in\n       the TCP or UDP destination port field.')
docsSubMgtTcpFlagValues = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 3), Bits().clone(namedValues=NamedValues(("urgent", 0), ("ack", 1), ("push", 2), ("reset", 3), ("syn", 4), ("fin", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpFlagValues.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtTcpFlagValues.setDescription('The value of the flags of interest.  The value of this\n       object MUST always be a subset (proper or otherwise) of\n       docsSubMgtTcpFlagMask.  An attempt to violate this constraint\n       returns an inconsistentValue error for an SNMPv2 or v3 agent\n       and a badValue error for an SNMPv1 agent.')
docsSubMgtTcpFlagMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 4), Bits().clone(namedValues=NamedValues(("urgent", 0), ("ack", 1), ("push", 2), ("reset", 3), ("syn", 4), ("fin", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpFlagMask.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtTcpFlagMask.setDescription('This bit set indicates the flags of interest in the TCP\n       header for the packet to be matched.  For example to match all\n       packets where the urgent bit is set, but that are not either syn\n       or fin, the value of docsSubMgtTcpFlagValues would be { urgent },\n       and the value of this object would be { urgent, syn, fin }')
docsSubMgtTcpUdpStatus = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpUdpStatus.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtTcpUdpStatus.setDescription('Standard row object for this table.  Any object in the\n       conceptual row may be modified regardless of whether this row is\n       active or not.')
docsSubMgtCmFilterTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 8), )
if mibBuilder.loadTexts: docsSubMgtCmFilterTable.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCmFilterTable.setDescription('Binds filter groups to modems. This table identifies for\n       each modem the upstream and downstream filter groups that apply\n       to packets for that modem. Zero is used as a distinguished value\n       to mean no filter group.')
docsSubMgtCmFilterEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 8, 1), )
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterEntry"))
docsSubMgtCmFilterEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsSubMgtCmFilterEntry.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCmFilterEntry.setDescription('Binds a filter group to each direction of traffic for a\n       modem.')
docsSubMgtSubFilterDownstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterDownstream.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtSubFilterDownstream.setDescription('The filter group applied to traffic destined for subscribers\n       attached to the referenced CM.  This is set upon row creation to\n       either the default (docsSubMgtSubFilterDownDefault), or to the\n       value in the provisioning object sent upstream from the CM to the\n       CMTS during registration. The value of this object is a pointer\n       into the docsSubMgtPktFilterTable and refers to all filter rows\n       with matching docsSubMgtPktFilterGroup indices. If there are no\n\n\n       matching filter rows in that table, or if this object is set to\n       zero, no filtering is applied to traffic destined to hosts\n       attached to this CM.')
docsSubMgtSubFilterUpstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterUpstream.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtSubFilterUpstream.setDescription('The filter group applied to traffic originating from\n       subscribers attached to the referenced CM.  This is set upon row\n       creation to either the default (docsSubMgtSubFilterUpDefault), or\n       to the value in the provisioning object sent upstream from the CM\n       to the CMTS. The value of this object is a pointer into the\n       docsSubMgtPktFilterTable and refers to all filter rows with\n       matching docsSubMgtPktFilterGroup indices. If there are no\n       matching filter rows in that table, or if this object is set to\n       zero, no filtering is applied to traffic originating from\n       hosts attached to this CM.')
docsSubMgtCmFilterDownstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterDownstream.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCmFilterDownstream.setDescription('The filter group applied to traffic destined for the\n       referenced CM itself.  This is set upon row creation to either\n       the default (docsSubMgtCmFilterDownDefault), or to the value in\n       the provisioning object sent upstream from the CM to the CMTS\n       during registration. The value of this object is a pointer into\n       the docsSubMgtPktFilterTable and refers to all filter rows with\n       matching docsSubMgtPktFilterGroup indices. If there are no\n       matching filter rows in that table, or if this object is set to\n       zero, no filtering is applied to traffic destined to this CM.')
docsSubMgtCmFilterUpstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterUpstream.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCmFilterUpstream.setDescription('The filter group applied to traffic originating from the\n       referenced CM itself.  This is set upon row creation to either\n       the default (docsSubMgtCmFilterUpDefault), or to the value in\n       the provisioning object sent upstream from the CM to the CMTS.\n       The value of this object is a pointer into the\n       docsSubMgtPktFilterTable and refers to all filter rows with\n       matching docsSubMgtPktFilterGroup indices. If there are no\n       matching filter rows in that table, or if this object is set\n       to zero, no filtering is applied to traffic originating from\n\n\n       this CM.')
docsSubMgtSubFilterDownDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterDownDefault.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtSubFilterDownDefault.setDescription('Upon a row creation in docsSubMgtCmFilterTable,\n       docsSubMgtSubFilterDownstream is set to this value if no\n       provisioning object is present to override it.  This object is\n       persistent across CMTS reboots.  Upon initial CMTS\n       initialization, this defaults to 0.')
docsSubMgtSubFilterUpDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterUpDefault.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtSubFilterUpDefault.setDescription('Upon a row creation in docsSubMgtCmFilterTable,\n       docsSubMgtSubFilterUpstream is set to this value if no\n       provisioning object is present to override it.  This object is\n       persistent across CMTS reboots.  Upon initial CMTS\n       initialization, this defaults to 0.')
docsSubMgtCmFilterDownDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterDownDefault.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCmFilterDownDefault.setDescription('Upon a row creation in docsSubMgtCmFilterTable,\n       docsSubMgtCmFilterDownstream is set to this value if no\n       provisioning object is present to override it.  This object is\n       persistent across CMTS reboots.  Upon initial CMTS\n       initialization, this defaults to 0.')
docsSubMgtCmFilterUpDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterUpDefault.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtCmFilterUpDefault.setDescription('Upon a row creation in docsSubMgtCmFilterTable,\n       docsSubMgtCmFilterUpstream is set to this value if no\n       provisioning object is present to override it.  This object is\n       persistent across CMTS reboots.  Upon initial CMTS\n       initialization, this defaults to 0.')
docsSubMgtNotification = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 2))
docsSubMgtConformance = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 3))
docsSubMgtCompliances = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 3, 1))
docsSubMgtGroups = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 3, 2))
docsSubMgtBasicCompliance = ModuleCompliance((1, 3, 6, 1, 3, 83, 4, 3, 1, 1)).setObjects(("DOCS-SUBMGT-MIB", "docsSubMgtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSubMgtBasicCompliance = docsSubMgtBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtBasicCompliance.setDescription('The compliance statement for CMTS devices that implement\n       CMTS centric subscriber management.')
docsSubMgtGroup = ObjectGroup((1, 3, 6, 1, 3, 83, 4, 3, 2, 1)).setObjects(("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlMaxCpeIp"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlActive"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlLearnable"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlReset"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeMaxIpDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeActiveDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeLearnableDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeIpAddr"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeIpLearned"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterSrcAddr"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterSrcMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterDstAddr"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterDstMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterUlp"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterTosValue"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterTosMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterAction"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterMatches"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterStatus"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpSrcPort"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpDstPort"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpFlagValues"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpFlagMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpStatus"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterDownstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterUpstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterDownstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterUpstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterDownDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterUpDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterDownDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterUpDefault"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSubMgtGroup = docsSubMgtGroup.setStatus('current')
if mibBuilder.loadTexts: docsSubMgtGroup.setDescription('The objects use to managed host-based cable modems\n                   via a set of CMTS enforced controls.')
mibBuilder.exportSymbols("DOCS-SUBMGT-MIB", IpV4orV6Addr=IpV4orV6Addr, docsSubMgtTcpUdpDstPort=docsSubMgtTcpUdpDstPort, docsSubMgtTcpUdpFilterTable=docsSubMgtTcpUdpFilterTable, docsSubMgtPktFilterTosMask=docsSubMgtPktFilterTosMask, PYSNMP_MODULE_ID=docsSubMgt, docsSubMgtCompliances=docsSubMgtCompliances, docsSubMgtObjects=docsSubMgtObjects, docsSubMgtCpeControlEntry=docsSubMgtCpeControlEntry, docsSubMgtPktFilterTable=docsSubMgtPktFilterTable, docsSubMgtPktFilterTosValue=docsSubMgtPktFilterTosValue, docsSubMgtPktFilterMatches=docsSubMgtPktFilterMatches, docsSubMgtTcpFlagMask=docsSubMgtTcpFlagMask, docsSubMgtCmFilterUpstream=docsSubMgtCmFilterUpstream, docsSubMgtTcpUdpSrcPort=docsSubMgtTcpUdpSrcPort, docsSubMgtCpeIpTable=docsSubMgtCpeIpTable, docsSubMgtCmFilterDownDefault=docsSubMgtCmFilterDownDefault, docsSubMgtCpeActiveDefault=docsSubMgtCpeActiveDefault, docsSubMgtCmFilterUpDefault=docsSubMgtCmFilterUpDefault, docsSubMgtPktFilterUlp=docsSubMgtPktFilterUlp, docsSubMgtCpeControlLearnable=docsSubMgtCpeControlLearnable, docsSubMgtCpeControlMaxCpeIp=docsSubMgtCpeControlMaxCpeIp, docsSubMgtTcpUdpFilterEntry=docsSubMgtTcpUdpFilterEntry, docsSubMgtCmFilterEntry=docsSubMgtCmFilterEntry, docsSubMgtSubFilterUpDefault=docsSubMgtSubFilterUpDefault, docsSubMgtCpeMaxIpDefault=docsSubMgtCpeMaxIpDefault, docsSubMgtCmFilterDownstream=docsSubMgtCmFilterDownstream, docsSubMgtCpeIpLearned=docsSubMgtCpeIpLearned, docsSubMgtPktFilterSrcAddr=docsSubMgtPktFilterSrcAddr, docsSubMgtNotification=docsSubMgtNotification, docsSubMgtPktFilterDstAddr=docsSubMgtPktFilterDstAddr, docsSubMgtGroups=docsSubMgtGroups, docsSubMgtCpeIpAddr=docsSubMgtCpeIpAddr, docsSubMgtPktFilterEntry=docsSubMgtPktFilterEntry, docsSubMgtCpeIpEntry=docsSubMgtCpeIpEntry, docsSubMgtPktFilterStatus=docsSubMgtPktFilterStatus, docsSubMgtCpeControlTable=docsSubMgtCpeControlTable, docsSubMgtCpeControlReset=docsSubMgtCpeControlReset, docsSubMgtTcpFlagValues=docsSubMgtTcpFlagValues, docsSubMgtCmFilterTable=docsSubMgtCmFilterTable, docsSubMgtSubFilterDownDefault=docsSubMgtSubFilterDownDefault, docsSubMgtBasicCompliance=docsSubMgtBasicCompliance, docsSubMgtPktFilterIndex=docsSubMgtPktFilterIndex, docsSubMgtSubFilterUpstream=docsSubMgtSubFilterUpstream, docsSubMgtPktFilterGroup=docsSubMgtPktFilterGroup, docsSubMgt=docsSubMgt, docsSubMgtCpeControlActive=docsSubMgtCpeControlActive, docsSubMgtSubFilterDownstream=docsSubMgtSubFilterDownstream, docsSubMgtCpeIpIndex=docsSubMgtCpeIpIndex, docsSubMgtPktFilterDstMask=docsSubMgtPktFilterDstMask, docsSubMgtGroup=docsSubMgtGroup, docsSubMgtPktFilterSrcMask=docsSubMgtPktFilterSrcMask, docsSubMgtTcpUdpStatus=docsSubMgtTcpUdpStatus, docsSubMgtPktFilterAction=docsSubMgtPktFilterAction, docsSubMgtConformance=docsSubMgtConformance, docsSubMgtCpeLearnableDefault=docsSubMgtCpeLearnableDefault)
