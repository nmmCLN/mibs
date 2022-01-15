#
# PySNMP MIB module CTRON-CDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-CDP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:13 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctCDP, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctCDP")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, ObjectIdentity, Unsigned32, Counter64, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter64", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "iso", "Bits")
TimeStamp, TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString", "MacAddress")
ctronCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3))
if mibBuilder.loadTexts: ctronCdpMIB.setLastUpdated('199908280000Z')
if mibBuilder.loadTexts: ctronCdpMIB.setOrganization('Cabletron Systems, Inc.')
class CTCDPCapability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("igmp", 1), ("rip", 2), ("bgp", 3), ("ospf", 4), ("dvmrp", 5), ("ieee8021q", 6), ("gvrp", 7), ("gmrp", 8), ("igmpSnoop", 9), ("dhcpServer", 10), ("dnsServer", 11), ("activeDirectory", 12))

ctCDPNeighbor = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1))
ctCDPStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2))
ctCDPStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4))
ctCDPNeighborLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborLastChange.setStatus('current')
ctCDPNeighborLastDelete = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborLastDelete.setStatus('current')
ctCDPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3), )
if mibBuilder.loadTexts: ctCDPNeighborTable.setStatus('current')
ctCDPNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1), ).setIndexNames((0, "CTRON-CDP-MIB", "ctCDPNeighborTimeMark"), (0, "IF-MIB", "ifIndex"), (0, "CTRON-CDP-MIB", "ctCDPNeighborMAC"))
if mibBuilder.loadTexts: ctCDPNeighborEntry.setStatus('current')
ctCDPNeighborTimeMark = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 1), TimeFilter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborTimeMark.setStatus('current')
ctCDPNeighborMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborMAC.setStatus('current')
ctCDPNeighborIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborIP.setStatus('current')
ctCDPNeighborPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborPort.setStatus('current')
ctCDPNeighborType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("secureFastSwitch", 1), ("dot1qSwitch", 2), ("router", 3), ("dot1dBridge", 4), ("vlanManager", 5), ("dnsServer", 6), ("dhcpServer", 7), ("dnsDhcpServer", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborType.setStatus('current')
ctCDPNeighborChassisMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborChassisMAC.setStatus('current')
ctCDPNeighborChassisIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborChassisIP.setStatus('current')
ctCDPNeighborDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborDescription.setStatus('current')
ctCDPNeighborPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborPortName.setStatus('current')
ctCDPNeighborCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 10), CTCDPCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPNeighborCapability.setStatus('current')
ctCDPGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("autoEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPGlobalStatus.setStatus('current')
ctCDPAuthenticationCode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPAuthenticationCode.setStatus('current')
ctCDPPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3), )
if mibBuilder.loadTexts: ctCDPPortTable.setStatus('current')
ctCDPPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1), ).setIndexNames((0, "CTRON-CDP-MIB", "ctCDPPort"))
if mibBuilder.loadTexts: ctCDPPortTableEntry.setStatus('current')
ctCDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPPort.setStatus('current')
ctCDPPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("autoEnable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPPortStatus.setStatus('current')
ctCDPTransmitFrequency = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 900))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPTransmitFrequency.setStatus('current')
ctCDPHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCDPHoldTime.setStatus('current')
ctCDPVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPVersion.setStatus('current')
ctCDPInPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPInPackets.setStatus('current')
ctCDPOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPOutPackets.setStatus('current')
ctCDPInvalidVersionPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPInvalidVersionPackets.setStatus('current')
ctCDPParseErrorPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPParseErrorPackets.setStatus('current')
ctCDPTransmitErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPTransmitErrors.setStatus('current')
ctCDPMemoryErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctCDPMemoryErrors.setStatus('current')
ctCDPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11))
ctCDPCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 1))
ctCDPGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 2))
ctCDPComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 1, 1)).setObjects(("CTRON-CDP-MIB", "ctCdpGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctCDPComplianceV10 = ctCDPComplianceV10.setStatus('current')
ctCdpGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 2, 1)).setObjects(("CTRON-CDP-MIB", "ctCDPNeighborLastChange"), ("CTRON-CDP-MIB", "ctCDPNeighborLastDelete"), ("CTRON-CDP-MIB", "ctCDPNeighborTimeMark"), ("CTRON-CDP-MIB", "ctCDPNeighborMAC"), ("CTRON-CDP-MIB", "ctCDPNeighborIP"), ("CTRON-CDP-MIB", "ctCDPNeighborPort"), ("CTRON-CDP-MIB", "ctCDPNeighborType"), ("CTRON-CDP-MIB", "ctCDPNeighborChassisMAC"), ("CTRON-CDP-MIB", "ctCDPNeighborChassisIP"), ("CTRON-CDP-MIB", "ctCDPGlobalStatus"), ("CTRON-CDP-MIB", "ctCDPAuthenticationCode"), ("CTRON-CDP-MIB", "ctCDPPort"), ("CTRON-CDP-MIB", "ctCDPPortStatus"), ("CTRON-CDP-MIB", "ctCDPNeighborDescription"), ("CTRON-CDP-MIB", "ctCDPNeighborPortName"), ("CTRON-CDP-MIB", "ctCDPNeighborCapability"), ("CTRON-CDP-MIB", "ctCDPTransmitFrequency"), ("CTRON-CDP-MIB", "ctCDPHoldTime"), ("CTRON-CDP-MIB", "ctCDPVersion"), ("CTRON-CDP-MIB", "ctCDPInPackets"), ("CTRON-CDP-MIB", "ctCDPOutPackets"), ("CTRON-CDP-MIB", "ctCDPInvalidVersionPackets"), ("CTRON-CDP-MIB", "ctCDPParseErrorPackets"), ("CTRON-CDP-MIB", "ctCDPTransmitErrors"), ("CTRON-CDP-MIB", "ctCDPMemoryErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctCdpGroupV10 = ctCdpGroupV10.setStatus('current')
mibBuilder.exportSymbols("CTRON-CDP-MIB", ctCDPNeighborType=ctCDPNeighborType, ctCDPGlobalStatus=ctCDPGlobalStatus, ctCDPParseErrorPackets=ctCDPParseErrorPackets, CTCDPCapability=CTCDPCapability, ctCDPPortTableEntry=ctCDPPortTableEntry, ctCDPHoldTime=ctCDPHoldTime, ctCDPNeighborChassisIP=ctCDPNeighborChassisIP, ctCDPTransmitFrequency=ctCDPTransmitFrequency, PYSNMP_MODULE_ID=ctronCdpMIB, ctCDPNeighborChassisMAC=ctCDPNeighborChassisMAC, ctCdpGroupV10=ctCdpGroupV10, ctCDPCompliances=ctCDPCompliances, ctCDPNeighborMAC=ctCDPNeighborMAC, ctCDPTransmitErrors=ctCDPTransmitErrors, ctCDPInvalidVersionPackets=ctCDPInvalidVersionPackets, ctronCdpMIB=ctronCdpMIB, ctCDPStats=ctCDPStats, ctCDPNeighborEntry=ctCDPNeighborEntry, ctCDPStatus=ctCDPStatus, ctCDPNeighbor=ctCDPNeighbor, ctCDPInPackets=ctCDPInPackets, ctCDPAuthenticationCode=ctCDPAuthenticationCode, ctCDPNeighborIP=ctCDPNeighborIP, ctCDPNeighborPortName=ctCDPNeighborPortName, ctCDPNeighborDescription=ctCDPNeighborDescription, ctCDPConformance=ctCDPConformance, ctCDPPort=ctCDPPort, ctCDPNeighborLastDelete=ctCDPNeighborLastDelete, ctCDPOutPackets=ctCDPOutPackets, ctCDPMemoryErrors=ctCDPMemoryErrors, ctCDPComplianceV10=ctCDPComplianceV10, ctCDPNeighborTable=ctCDPNeighborTable, ctCDPGroups=ctCDPGroups, ctCDPNeighborTimeMark=ctCDPNeighborTimeMark, ctCDPNeighborCapability=ctCDPNeighborCapability, ctCDPPortTable=ctCDPPortTable, ctCDPPortStatus=ctCDPPortStatus, ctCDPVersion=ctCDPVersion, ctCDPNeighborPort=ctCDPNeighborPort, ctCDPNeighborLastChange=ctCDPNeighborLastChange)
