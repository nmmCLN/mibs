#
# PySNMP MIB module IPV6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IPV6-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:13:03 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
Ipv6AddressPrefix, Ipv6IfIndexOrZero, Ipv6IfIndex, Ipv6Address, Ipv6AddressIfIdentifier = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix", "Ipv6IfIndexOrZero", "Ipv6IfIndex", "Ipv6Address", "Ipv6AddressIfIdentifier")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, NotificationType, Gauge32, TimeTicks, Counter64, Integer32, Bits, Counter32, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, IpAddress, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Gauge32", "TimeTicks", "Counter64", "Integer32", "Bits", "Counter32", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "IpAddress", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString, TimeStamp, TruthValue, PhysAddress, RowPointer, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "TruthValue", "PhysAddress", "RowPointer", "VariablePointer")
ipv6MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 55))
if mibBuilder.loadTexts: ipv6MIB.setLastUpdated('9802052155Z')
if mibBuilder.loadTexts: ipv6MIB.setOrganization('IETF IPv6 Working Group')
ipv6MIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 1))
ipv6Forwarding = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6Forwarding.setStatus('current')
ipv6DefaultHopLimit = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6DefaultHopLimit.setStatus('current')
ipv6Interfaces = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6Interfaces.setStatus('current')
ipv6IfTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfTableLastChange.setStatus('current')
ipv6IfTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 5), )
if mibBuilder.loadTexts: ipv6IfTable.setStatus('current')
ipv6IfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 5, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"))
if mibBuilder.loadTexts: ipv6IfEntry.setStatus('current')
ipv6IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 1), Ipv6IfIndex())
if mibBuilder.loadTexts: ipv6IfIndex.setStatus('current')
ipv6IfDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfDescr.setStatus('current')
ipv6IfLowerLayer = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfLowerLayer.setStatus('current')
ipv6IfEffectiveMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 4), Unsigned32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfEffectiveMtu.setStatus('current')
ipv6IfReasmMaxSize = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfReasmMaxSize.setStatus('current')
ipv6IfIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 6), Ipv6AddressIfIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfIdentifier.setStatus('current')
ipv6IfIdentifierLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setUnits('bits').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfIdentifierLength.setStatus('current')
ipv6IfPhysicalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 8), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfPhysicalAddress.setStatus('current')
ipv6IfAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfAdminStatus.setStatus('current')
ipv6IfOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("noIfIdentifier", 3), ("unknown", 4), ("notPresent", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfOperStatus.setStatus('current')
ipv6IfLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfLastChange.setStatus('current')
ipv6IfStatsTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 6), )
if mibBuilder.loadTexts: ipv6IfStatsTable.setStatus('current')
ipv6IfStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 6, 1), )
ipv6IfEntry.registerAugmentions(("IPV6-MIB", "ipv6IfStatsEntry"))
ipv6IfStatsEntry.setIndexNames(*ipv6IfEntry.getIndexNames())
if mibBuilder.loadTexts: ipv6IfStatsEntry.setStatus('current')
ipv6IfStatsInReceives = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInReceives.setStatus('current')
ipv6IfStatsInHdrErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInHdrErrors.setStatus('current')
ipv6IfStatsInTooBigErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInTooBigErrors.setStatus('current')
ipv6IfStatsInNoRoutes = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInNoRoutes.setStatus('current')
ipv6IfStatsInAddrErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInAddrErrors.setStatus('current')
ipv6IfStatsInUnknownProtos = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInUnknownProtos.setStatus('current')
ipv6IfStatsInTruncatedPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInTruncatedPkts.setStatus('current')
ipv6IfStatsInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInDiscards.setStatus('current')
ipv6IfStatsInDelivers = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInDelivers.setStatus('current')
ipv6IfStatsOutForwDatagrams = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutForwDatagrams.setStatus('current')
ipv6IfStatsOutRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutRequests.setStatus('current')
ipv6IfStatsOutDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutDiscards.setStatus('current')
ipv6IfStatsOutFragOKs = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutFragOKs.setStatus('current')
ipv6IfStatsOutFragFails = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutFragFails.setStatus('current')
ipv6IfStatsOutFragCreates = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutFragCreates.setStatus('current')
ipv6IfStatsReasmReqds = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsReasmReqds.setStatus('current')
ipv6IfStatsReasmOKs = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsReasmOKs.setStatus('current')
ipv6IfStatsReasmFails = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsReasmFails.setStatus('current')
ipv6IfStatsInMcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInMcastPkts.setStatus('current')
ipv6IfStatsOutMcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutMcastPkts.setStatus('current')
ipv6AddrPrefixTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 7), )
if mibBuilder.loadTexts: ipv6AddrPrefixTable.setStatus('current')
ipv6AddrPrefixEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 7, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"), (0, "IPV6-MIB", "ipv6AddrPrefix"), (0, "IPV6-MIB", "ipv6AddrPrefixLength"))
if mibBuilder.loadTexts: ipv6AddrPrefixEntry.setStatus('current')
ipv6AddrPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: ipv6AddrPrefix.setStatus('current')
ipv6AddrPrefixLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setUnits('bits')
if mibBuilder.loadTexts: ipv6AddrPrefixLength.setStatus('current')
ipv6AddrPrefixOnLinkFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixOnLinkFlag.setStatus('current')
ipv6AddrPrefixAutonomousFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixAutonomousFlag.setStatus('current')
ipv6AddrPrefixAdvPreferredLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixAdvPreferredLifetime.setStatus('current')
ipv6AddrPrefixAdvValidLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixAdvValidLifetime.setStatus('current')
ipv6AddrTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 8), )
if mibBuilder.loadTexts: ipv6AddrTable.setStatus('current')
ipv6AddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 8, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"), (0, "IPV6-MIB", "ipv6AddrAddress"))
if mibBuilder.loadTexts: ipv6AddrEntry.setStatus('current')
ipv6AddrAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6AddrAddress.setStatus('current')
ipv6AddrPfxLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setUnits('bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPfxLength.setStatus('current')
ipv6AddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stateless", 1), ("stateful", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrType.setStatus('current')
ipv6AddrAnycastFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrAnycastFlag.setStatus('current')
ipv6AddrStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("preferred", 1), ("deprecated", 2), ("invalid", 3), ("inaccessible", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrStatus.setStatus('current')
ipv6RouteNumber = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteNumber.setStatus('current')
ipv6DiscardedRoutes = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6DiscardedRoutes.setStatus('current')
ipv6RouteTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 11), )
if mibBuilder.loadTexts: ipv6RouteTable.setStatus('current')
ipv6RouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 11, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6RouteDest"), (0, "IPV6-MIB", "ipv6RoutePfxLength"), (0, "IPV6-MIB", "ipv6RouteIndex"))
if mibBuilder.loadTexts: ipv6RouteEntry.setStatus('current')
ipv6RouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6RouteDest.setStatus('current')
ipv6RoutePfxLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setUnits('bits')
if mibBuilder.loadTexts: ipv6RoutePfxLength.setStatus('current')
ipv6RouteIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 3), Unsigned32())
if mibBuilder.loadTexts: ipv6RouteIndex.setStatus('current')
ipv6RouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 4), Ipv6IfIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteIfIndex.setStatus('current')
ipv6RouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 5), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteNextHop.setStatus('current')
ipv6RouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("discard", 2), ("local", 3), ("remote", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteType.setStatus('current')
ipv6RouteProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("ndisc", 4), ("rip", 5), ("ospf", 6), ("bgp", 7), ("idrp", 8), ("igrp", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteProtocol.setStatus('current')
ipv6RoutePolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RoutePolicy.setStatus('current')
ipv6RouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteAge.setStatus('current')
ipv6RouteNextHopRDI = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteNextHopRDI.setStatus('current')
ipv6RouteMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteMetric.setStatus('current')
ipv6RouteWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteWeight.setStatus('current')
ipv6RouteInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 13), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteInfo.setStatus('current')
ipv6RouteValid = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 14), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6RouteValid.setStatus('current')
ipv6NetToMediaTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 12), )
if mibBuilder.loadTexts: ipv6NetToMediaTable.setStatus('current')
ipv6NetToMediaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 12, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"), (0, "IPV6-MIB", "ipv6NetToMediaNetAddress"))
if mibBuilder.loadTexts: ipv6NetToMediaEntry.setStatus('current')
ipv6NetToMediaNetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6NetToMediaNetAddress.setStatus('current')
ipv6NetToMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6NetToMediaPhysAddress.setStatus('current')
ipv6NetToMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("dynamic", 2), ("static", 3), ("local", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6NetToMediaType.setStatus('current')
ipv6IfNetToMediaState = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("reachable", 1), ("stale", 2), ("delay", 3), ("probe", 4), ("invalid", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfNetToMediaState.setStatus('current')
ipv6IfNetToMediaLastUpdated = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfNetToMediaLastUpdated.setStatus('current')
ipv6NetToMediaValid = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6NetToMediaValid.setStatus('current')
ipv6Notifications = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 2))
ipv6NotificationPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 2, 0))
ipv6IfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 55, 2, 0, 1)).setObjects(("IPV6-MIB", "ipv6IfDescr"), ("IPV6-MIB", "ipv6IfOperStatus"))
if mibBuilder.loadTexts: ipv6IfStateChange.setStatus('current')
ipv6Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 3))
ipv6Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 3, 1))
ipv6Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 3, 2))
ipv6Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 55, 3, 1, 1)).setObjects(("IPV6-MIB", "ipv6GeneralGroup"), ("IPV6-MIB", "ipv6NotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6Compliance = ipv6Compliance.setStatus('current')
ipv6GeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 55, 3, 2, 1)).setObjects(("IPV6-MIB", "ipv6Forwarding"), ("IPV6-MIB", "ipv6DefaultHopLimit"), ("IPV6-MIB", "ipv6Interfaces"), ("IPV6-MIB", "ipv6IfTableLastChange"), ("IPV6-MIB", "ipv6IfDescr"), ("IPV6-MIB", "ipv6IfLowerLayer"), ("IPV6-MIB", "ipv6IfEffectiveMtu"), ("IPV6-MIB", "ipv6IfReasmMaxSize"), ("IPV6-MIB", "ipv6IfIdentifier"), ("IPV6-MIB", "ipv6IfIdentifierLength"), ("IPV6-MIB", "ipv6IfPhysicalAddress"), ("IPV6-MIB", "ipv6IfAdminStatus"), ("IPV6-MIB", "ipv6IfOperStatus"), ("IPV6-MIB", "ipv6IfLastChange"), ("IPV6-MIB", "ipv6IfStatsInReceives"), ("IPV6-MIB", "ipv6IfStatsInHdrErrors"), ("IPV6-MIB", "ipv6IfStatsInTooBigErrors"), ("IPV6-MIB", "ipv6IfStatsInNoRoutes"), ("IPV6-MIB", "ipv6IfStatsInAddrErrors"), ("IPV6-MIB", "ipv6IfStatsInUnknownProtos"), ("IPV6-MIB", "ipv6IfStatsInTruncatedPkts"), ("IPV6-MIB", "ipv6IfStatsInDiscards"), ("IPV6-MIB", "ipv6IfStatsInDelivers"), ("IPV6-MIB", "ipv6IfStatsOutForwDatagrams"), ("IPV6-MIB", "ipv6IfStatsOutRequests"), ("IPV6-MIB", "ipv6IfStatsOutDiscards"), ("IPV6-MIB", "ipv6IfStatsOutFragOKs"), ("IPV6-MIB", "ipv6IfStatsOutFragFails"), ("IPV6-MIB", "ipv6IfStatsOutFragCreates"), ("IPV6-MIB", "ipv6IfStatsReasmReqds"), ("IPV6-MIB", "ipv6IfStatsReasmOKs"), ("IPV6-MIB", "ipv6IfStatsReasmFails"), ("IPV6-MIB", "ipv6IfStatsInMcastPkts"), ("IPV6-MIB", "ipv6IfStatsOutMcastPkts"), ("IPV6-MIB", "ipv6AddrPrefixOnLinkFlag"), ("IPV6-MIB", "ipv6AddrPrefixAutonomousFlag"), ("IPV6-MIB", "ipv6AddrPrefixAdvPreferredLifetime"), ("IPV6-MIB", "ipv6AddrPrefixAdvValidLifetime"), ("IPV6-MIB", "ipv6AddrPfxLength"), ("IPV6-MIB", "ipv6AddrType"), ("IPV6-MIB", "ipv6AddrAnycastFlag"), ("IPV6-MIB", "ipv6AddrStatus"), ("IPV6-MIB", "ipv6RouteNumber"), ("IPV6-MIB", "ipv6DiscardedRoutes"), ("IPV6-MIB", "ipv6RouteIfIndex"), ("IPV6-MIB", "ipv6RouteNextHop"), ("IPV6-MIB", "ipv6RouteType"), ("IPV6-MIB", "ipv6RouteProtocol"), ("IPV6-MIB", "ipv6RoutePolicy"), ("IPV6-MIB", "ipv6RouteAge"), ("IPV6-MIB", "ipv6RouteNextHopRDI"), ("IPV6-MIB", "ipv6RouteMetric"), ("IPV6-MIB", "ipv6RouteWeight"), ("IPV6-MIB", "ipv6RouteInfo"), ("IPV6-MIB", "ipv6RouteValid"), ("IPV6-MIB", "ipv6NetToMediaPhysAddress"), ("IPV6-MIB", "ipv6NetToMediaType"), ("IPV6-MIB", "ipv6IfNetToMediaState"), ("IPV6-MIB", "ipv6IfNetToMediaLastUpdated"), ("IPV6-MIB", "ipv6NetToMediaValid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6GeneralGroup = ipv6GeneralGroup.setStatus('current')
ipv6NotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 55, 3, 2, 2)).setObjects(("IPV6-MIB", "ipv6IfStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6NotificationGroup = ipv6NotificationGroup.setStatus('current')
mibBuilder.exportSymbols("IPV6-MIB", ipv6RouteNextHop=ipv6RouteNextHop, ipv6RouteProtocol=ipv6RouteProtocol, ipv6IfStatsTable=ipv6IfStatsTable, ipv6IfLowerLayer=ipv6IfLowerLayer, ipv6IfStatsOutMcastPkts=ipv6IfStatsOutMcastPkts, ipv6IfEntry=ipv6IfEntry, ipv6AddrAddress=ipv6AddrAddress, ipv6IfStatsReasmOKs=ipv6IfStatsReasmOKs, ipv6RoutePfxLength=ipv6RoutePfxLength, ipv6AddrAnycastFlag=ipv6AddrAnycastFlag, ipv6RouteWeight=ipv6RouteWeight, ipv6RouteNextHopRDI=ipv6RouteNextHopRDI, ipv6IfAdminStatus=ipv6IfAdminStatus, ipv6DiscardedRoutes=ipv6DiscardedRoutes, ipv6NetToMediaValid=ipv6NetToMediaValid, ipv6AddrPrefix=ipv6AddrPrefix, ipv6IfEffectiveMtu=ipv6IfEffectiveMtu, ipv6RouteMetric=ipv6RouteMetric, ipv6MIB=ipv6MIB, ipv6IfStatsOutRequests=ipv6IfStatsOutRequests, ipv6NetToMediaEntry=ipv6NetToMediaEntry, ipv6NetToMediaNetAddress=ipv6NetToMediaNetAddress, ipv6Interfaces=ipv6Interfaces, ipv6AddrPrefixLength=ipv6AddrPrefixLength, ipv6AddrPrefixAutonomousFlag=ipv6AddrPrefixAutonomousFlag, ipv6IfStatsInDelivers=ipv6IfStatsInDelivers, ipv6AddrTable=ipv6AddrTable, ipv6Forwarding=ipv6Forwarding, ipv6AddrPfxLength=ipv6AddrPfxLength, ipv6NetToMediaType=ipv6NetToMediaType, ipv6RoutePolicy=ipv6RoutePolicy, ipv6MIBObjects=ipv6MIBObjects, ipv6IfStatsInMcastPkts=ipv6IfStatsInMcastPkts, ipv6RouteTable=ipv6RouteTable, ipv6IfNetToMediaState=ipv6IfNetToMediaState, ipv6AddrPrefixTable=ipv6AddrPrefixTable, ipv6RouteEntry=ipv6RouteEntry, ipv6RouteType=ipv6RouteType, ipv6IfStatsInUnknownProtos=ipv6IfStatsInUnknownProtos, ipv6IfNetToMediaLastUpdated=ipv6IfNetToMediaLastUpdated, ipv6RouteAge=ipv6RouteAge, ipv6AddrPrefixAdvPreferredLifetime=ipv6AddrPrefixAdvPreferredLifetime, ipv6IfStatsReasmReqds=ipv6IfStatsReasmReqds, ipv6IfLastChange=ipv6IfLastChange, ipv6IfTable=ipv6IfTable, ipv6Compliance=ipv6Compliance, ipv6DefaultHopLimit=ipv6DefaultHopLimit, ipv6Conformance=ipv6Conformance, PYSNMP_MODULE_ID=ipv6MIB, ipv6IfStatsInAddrErrors=ipv6IfStatsInAddrErrors, ipv6AddrPrefixEntry=ipv6AddrPrefixEntry, ipv6NotificationPrefix=ipv6NotificationPrefix, ipv6IfStatsOutFragCreates=ipv6IfStatsOutFragCreates, ipv6Groups=ipv6Groups, ipv6IfStatsInReceives=ipv6IfStatsInReceives, ipv6IfDescr=ipv6IfDescr, ipv6IfStatsInDiscards=ipv6IfStatsInDiscards, ipv6IfStatsOutForwDatagrams=ipv6IfStatsOutForwDatagrams, ipv6RouteIfIndex=ipv6RouteIfIndex, ipv6Compliances=ipv6Compliances, ipv6IfStatsInTruncatedPkts=ipv6IfStatsInTruncatedPkts, ipv6RouteInfo=ipv6RouteInfo, ipv6IfStatsReasmFails=ipv6IfStatsReasmFails, ipv6IfStatsInHdrErrors=ipv6IfStatsInHdrErrors, ipv6IfIdentifierLength=ipv6IfIdentifierLength, ipv6IfStateChange=ipv6IfStateChange, ipv6AddrPrefixOnLinkFlag=ipv6AddrPrefixOnLinkFlag, ipv6IfIdentifier=ipv6IfIdentifier, ipv6IfPhysicalAddress=ipv6IfPhysicalAddress, ipv6GeneralGroup=ipv6GeneralGroup, ipv6RouteDest=ipv6RouteDest, ipv6AddrPrefixAdvValidLifetime=ipv6AddrPrefixAdvValidLifetime, ipv6RouteIndex=ipv6RouteIndex, ipv6IfReasmMaxSize=ipv6IfReasmMaxSize, ipv6IfStatsInNoRoutes=ipv6IfStatsInNoRoutes, ipv6NetToMediaPhysAddress=ipv6NetToMediaPhysAddress, ipv6IfStatsInTooBigErrors=ipv6IfStatsInTooBigErrors, ipv6IfStatsOutDiscards=ipv6IfStatsOutDiscards, ipv6IfOperStatus=ipv6IfOperStatus, ipv6IfTableLastChange=ipv6IfTableLastChange, ipv6AddrEntry=ipv6AddrEntry, ipv6RouteValid=ipv6RouteValid, ipv6NetToMediaTable=ipv6NetToMediaTable, ipv6Notifications=ipv6Notifications, ipv6IfStatsEntry=ipv6IfStatsEntry, ipv6NotificationGroup=ipv6NotificationGroup, ipv6IfStatsOutFragOKs=ipv6IfStatsOutFragOKs, ipv6AddrType=ipv6AddrType, ipv6RouteNumber=ipv6RouteNumber, ipv6IfStatsOutFragFails=ipv6IfStatsOutFragFails, ipv6IfIndex=ipv6IfIndex, ipv6AddrStatus=ipv6AddrStatus)
