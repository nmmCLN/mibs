#
# PySNMP MIB module IPMROUTE-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IPMROUTE-STD-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:31:06 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
IANAipRouteProtocol, IANAipMRouteProtocol = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol", "IANAipMRouteProtocol")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
mib_2, TimeTicks, Integer32, Bits, ObjectIdentity, Counter64, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "TimeTicks", "Integer32", "Bits", "ObjectIdentity", "Counter64", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32", "ModuleIdentity", "iso")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
ipMRouteStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 83))
ipMRouteStdMIB.setRevisions(('2000-09-22 00:00',))
if mibBuilder.loadTexts: ipMRouteStdMIB.setLastUpdated('200009220000Z')
if mibBuilder.loadTexts: ipMRouteStdMIB.setOrganization('IETF IDMR Working Group')
class LanguageTag(TextualConvention, OctetString):
    status = 'current'
    displayHint = '100a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 100)

ipMRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 1))
ipMRoute = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 1, 1))
ipMRouteEnable = MibScalar((1, 3, 6, 1, 2, 1, 83, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMRouteEnable.setStatus('current')
ipMRouteEntryCount = MibScalar((1, 3, 6, 1, 2, 1, 83, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteEntryCount.setStatus('current')
ipMRouteTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 2), )
if mibBuilder.loadTexts: ipMRouteTable.setStatus('current')
ipMRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"))
if mibBuilder.loadTexts: ipMRouteEntry.setStatus('current')
ipMRouteGroup = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRouteGroup.setStatus('current')
ipMRouteSource = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteSource.setStatus('current')
ipMRouteSourceMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRouteSourceMask.setStatus('current')
ipMRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteUpstreamNeighbor.setStatus('current')
ipMRouteInIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInIfIndex.setStatus('current')
ipMRouteUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteUpTime.setStatus('current')
ipMRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteExpiryTime.setStatus('current')
ipMRoutePkts = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoutePkts.setStatus('current')
ipMRouteDifferentInIfPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteDifferentInIfPackets.setStatus('current')
ipMRouteOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteOctets.setStatus('current')
ipMRouteProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 11), IANAipMRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteProtocol.setStatus('current')
ipMRouteRtProto = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 12), IANAipRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtProto.setStatus('current')
ipMRouteRtAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtAddress.setStatus('current')
ipMRouteRtMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtMask.setStatus('current')
ipMRouteRtType = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unicast", 1), ("multicast", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtType.setStatus('current')
ipMRouteHCOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteHCOctets.setStatus('current')
ipMRouteNextHopTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 3), )
if mibBuilder.loadTexts: ipMRouteNextHopTable.setStatus('current')
ipMRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"))
if mibBuilder.loadTexts: ipMRouteNextHopEntry.setStatus('current')
ipMRouteNextHopGroup = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopGroup.setStatus('current')
ipMRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopSource.setStatus('current')
ipMRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopSourceMask.setStatus('current')
ipMRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: ipMRouteNextHopIfIndex.setStatus('current')
ipMRouteNextHopAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 5), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopAddress.setStatus('current')
ipMRouteNextHopState = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pruned", 1), ("forwarding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopState.setStatus('current')
ipMRouteNextHopUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopUpTime.setStatus('current')
ipMRouteNextHopExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopExpiryTime.setStatus('current')
ipMRouteNextHopClosestMemberHops = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopClosestMemberHops.setStatus('current')
ipMRouteNextHopProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 10), IANAipMRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopProtocol.setStatus('current')
ipMRouteNextHopPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopPkts.setStatus('current')
ipMRouteInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 4), )
if mibBuilder.loadTexts: ipMRouteInterfaceTable.setStatus('current')
ipMRouteInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteInterfaceIfIndex"))
if mibBuilder.loadTexts: ipMRouteInterfaceEntry.setStatus('current')
ipMRouteInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipMRouteInterfaceIfIndex.setStatus('current')
ipMRouteInterfaceTtl = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMRouteInterfaceTtl.setStatus('current')
ipMRouteInterfaceProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 3), IANAipMRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceProtocol.setStatus('current')
ipMRouteInterfaceRateLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMRouteInterfaceRateLimit.setStatus('current')
ipMRouteInterfaceInMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceInMcastOctets.setStatus('current')
ipMRouteInterfaceOutMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceOutMcastOctets.setStatus('current')
ipMRouteInterfaceHCInMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceHCInMcastOctets.setStatus('current')
ipMRouteInterfaceHCOutMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceHCOutMcastOctets.setStatus('current')
ipMRouteBoundaryTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 5), )
if mibBuilder.loadTexts: ipMRouteBoundaryTable.setStatus('current')
ipMRouteBoundaryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryIfIndex"), (0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryAddress"), (0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryAddressMask"))
if mibBuilder.loadTexts: ipMRouteBoundaryEntry.setStatus('current')
ipMRouteBoundaryIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipMRouteBoundaryIfIndex.setStatus('current')
ipMRouteBoundaryAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteBoundaryAddress.setStatus('current')
ipMRouteBoundaryAddressMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRouteBoundaryAddressMask.setStatus('current')
ipMRouteBoundaryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteBoundaryStatus.setStatus('current')
ipMRouteScopeNameTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 6), )
if mibBuilder.loadTexts: ipMRouteScopeNameTable.setStatus('current')
ipMRouteScopeNameEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteScopeNameAddress"), (0, "IPMROUTE-STD-MIB", "ipMRouteScopeNameAddressMask"), (1, "IPMROUTE-STD-MIB", "ipMRouteScopeNameLanguage"))
if mibBuilder.loadTexts: ipMRouteScopeNameEntry.setStatus('current')
ipMRouteScopeNameAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRouteScopeNameAddress.setStatus('current')
ipMRouteScopeNameAddressMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteScopeNameAddressMask.setStatus('current')
ipMRouteScopeNameLanguage = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 3), LanguageTag())
if mibBuilder.loadTexts: ipMRouteScopeNameLanguage.setStatus('current')
ipMRouteScopeNameString = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteScopeNameString.setStatus('current')
ipMRouteScopeNameDefault = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteScopeNameDefault.setStatus('current')
ipMRouteScopeNameStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteScopeNameStatus.setStatus('current')
ipMRouteMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 2))
ipMRouteMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 2, 1))
ipMRouteMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 2, 2))
ipMRouteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 83, 2, 1, 1)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteMIBBasicGroup"), ("IPMROUTE-STD-MIB", "ipMRouteMIBRouteGroup"), ("IPMROUTE-STD-MIB", "ipMRouteMIBBoundaryGroup"), ("IPMROUTE-STD-MIB", "ipMRouteMIBHCInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBCompliance = ipMRouteMIBCompliance.setStatus('current')
ipMRouteMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 1)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteEnable"), ("IPMROUTE-STD-MIB", "ipMRouteEntryCount"), ("IPMROUTE-STD-MIB", "ipMRouteUpstreamNeighbor"), ("IPMROUTE-STD-MIB", "ipMRouteInIfIndex"), ("IPMROUTE-STD-MIB", "ipMRouteUpTime"), ("IPMROUTE-STD-MIB", "ipMRouteExpiryTime"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopState"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopUpTime"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopExpiryTime"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopProtocol"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopPkts"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceTtl"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceProtocol"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceRateLimit"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceInMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceOutMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBBasicGroup = ipMRouteMIBBasicGroup.setStatus('current')
ipMRouteMIBHopCountGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 2)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteNextHopClosestMemberHops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBHopCountGroup = ipMRouteMIBHopCountGroup.setStatus('current')
ipMRouteMIBBoundaryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 3)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteBoundaryStatus"), ("IPMROUTE-STD-MIB", "ipMRouteScopeNameString"), ("IPMROUTE-STD-MIB", "ipMRouteScopeNameDefault"), ("IPMROUTE-STD-MIB", "ipMRouteScopeNameStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBBoundaryGroup = ipMRouteMIBBoundaryGroup.setStatus('current')
ipMRouteMIBPktsOutGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 4)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteNextHopPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBPktsOutGroup = ipMRouteMIBPktsOutGroup.setStatus('current')
ipMRouteMIBHCInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 5)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteInterfaceHCInMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceHCOutMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBHCInterfaceGroup = ipMRouteMIBHCInterfaceGroup.setStatus('current')
ipMRouteMIBRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 6)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteRtProto"), ("IPMROUTE-STD-MIB", "ipMRouteRtAddress"), ("IPMROUTE-STD-MIB", "ipMRouteRtMask"), ("IPMROUTE-STD-MIB", "ipMRouteRtType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBRouteGroup = ipMRouteMIBRouteGroup.setStatus('current')
ipMRouteMIBPktsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 7)).setObjects(("IPMROUTE-STD-MIB", "ipMRoutePkts"), ("IPMROUTE-STD-MIB", "ipMRouteDifferentInIfPackets"), ("IPMROUTE-STD-MIB", "ipMRouteOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBPktsGroup = ipMRouteMIBPktsGroup.setStatus('current')
mibBuilder.exportSymbols("IPMROUTE-STD-MIB", ipMRouteNextHopState=ipMRouteNextHopState, ipMRouteBoundaryAddressMask=ipMRouteBoundaryAddressMask, ipMRouteBoundaryEntry=ipMRouteBoundaryEntry, ipMRouteInterfaceTtl=ipMRouteInterfaceTtl, ipMRouteBoundaryTable=ipMRouteBoundaryTable, ipMRouteOctets=ipMRouteOctets, ipMRouteNextHopSource=ipMRouteNextHopSource, ipMRouteMIBConformance=ipMRouteMIBConformance, ipMRouteScopeNameStatus=ipMRouteScopeNameStatus, ipMRouteEntry=ipMRouteEntry, ipMRouteScopeNameAddress=ipMRouteScopeNameAddress, ipMRouteScopeNameAddressMask=ipMRouteScopeNameAddressMask, ipMRouteRtProto=ipMRouteRtProto, ipMRouteInterfaceHCOutMcastOctets=ipMRouteInterfaceHCOutMcastOctets, ipMRouteScopeNameString=ipMRouteScopeNameString, ipMRouteMIBBoundaryGroup=ipMRouteMIBBoundaryGroup, ipMRouteMIBHCInterfaceGroup=ipMRouteMIBHCInterfaceGroup, ipMRouteGroup=ipMRouteGroup, ipMRouteNextHopSourceMask=ipMRouteNextHopSourceMask, ipMRouteNextHopTable=ipMRouteNextHopTable, ipMRouteUpTime=ipMRouteUpTime, LanguageTag=LanguageTag, ipMRouteBoundaryIfIndex=ipMRouteBoundaryIfIndex, ipMRouteMIBCompliances=ipMRouteMIBCompliances, ipMRouteNextHopClosestMemberHops=ipMRouteNextHopClosestMemberHops, ipMRouteBoundaryStatus=ipMRouteBoundaryStatus, PYSNMP_MODULE_ID=ipMRouteStdMIB, ipMRouteSourceMask=ipMRouteSourceMask, ipMRouteMIBGroups=ipMRouteMIBGroups, ipMRouteMIBBasicGroup=ipMRouteMIBBasicGroup, ipMRoutePkts=ipMRoutePkts, ipMRouteMIBHopCountGroup=ipMRouteMIBHopCountGroup, ipMRouteNextHopIfIndex=ipMRouteNextHopIfIndex, ipMRouteTable=ipMRouteTable, ipMRouteHCOctets=ipMRouteHCOctets, ipMRouteScopeNameTable=ipMRouteScopeNameTable, ipMRouteInterfaceInMcastOctets=ipMRouteInterfaceInMcastOctets, ipMRouteScopeNameLanguage=ipMRouteScopeNameLanguage, ipMRouteInterfaceProtocol=ipMRouteInterfaceProtocol, ipMRouteEnable=ipMRouteEnable, ipMRouteRtAddress=ipMRouteRtAddress, ipMRouteNextHopAddress=ipMRouteNextHopAddress, ipMRouteMIBObjects=ipMRouteMIBObjects, ipMRouteMIBRouteGroup=ipMRouteMIBRouteGroup, ipMRouteRtMask=ipMRouteRtMask, ipMRouteScopeNameEntry=ipMRouteScopeNameEntry, ipMRouteEntryCount=ipMRouteEntryCount, ipMRouteInterfaceEntry=ipMRouteInterfaceEntry, ipMRouteInIfIndex=ipMRouteInIfIndex, ipMRouteNextHopExpiryTime=ipMRouteNextHopExpiryTime, ipMRouteInterfaceRateLimit=ipMRouteInterfaceRateLimit, ipMRouteMIBPktsOutGroup=ipMRouteMIBPktsOutGroup, ipMRouteExpiryTime=ipMRouteExpiryTime, ipMRouteNextHopGroup=ipMRouteNextHopGroup, ipMRouteBoundaryAddress=ipMRouteBoundaryAddress, ipMRouteSource=ipMRouteSource, ipMRouteUpstreamNeighbor=ipMRouteUpstreamNeighbor, ipMRouteDifferentInIfPackets=ipMRouteDifferentInIfPackets, ipMRouteProtocol=ipMRouteProtocol, ipMRouteStdMIB=ipMRouteStdMIB, ipMRoute=ipMRoute, ipMRouteNextHopUpTime=ipMRouteNextHopUpTime, ipMRouteScopeNameDefault=ipMRouteScopeNameDefault, ipMRouteNextHopProtocol=ipMRouteNextHopProtocol, ipMRouteNextHopPkts=ipMRouteNextHopPkts, ipMRouteInterfaceIfIndex=ipMRouteInterfaceIfIndex, ipMRouteMIBCompliance=ipMRouteMIBCompliance, ipMRouteInterfaceHCInMcastOctets=ipMRouteInterfaceHCInMcastOctets, ipMRouteMIBPktsGroup=ipMRouteMIBPktsGroup, ipMRouteInterfaceOutMcastOctets=ipMRouteInterfaceOutMcastOctets, ipMRouteRtType=ipMRouteRtType, ipMRouteNextHopEntry=ipMRouteNextHopEntry, ipMRouteInterfaceTable=ipMRouteInterfaceTable)
