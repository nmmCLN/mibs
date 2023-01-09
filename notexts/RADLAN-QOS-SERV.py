#
# PySNMP MIB module RADLAN-QOS-SERV (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-QOS-SERV
# Produced by pysmi-1.1.8 at Mon Jan  9 10:36:30 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
RowStatus, TruthValue = mibBuilder.importSymbols("RADLAN-SNMPv2", "RowStatus", "TruthValue")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibIdentifier, Counter32, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "ModuleIdentity")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
rlQosServ = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 99))
rlQosServ.setRevisions(('2003-10-28 00:24',))
if mibBuilder.loadTexts: rlQosServ.setLastUpdated('200308280024Z')
if mibBuilder.loadTexts: rlQosServ.setOrganization('Radlan Computer Communication Ltd.')
class RlQosServServiceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("suspended", 2))

class RlQosServNamedTableId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fcl", 1), ("fce", 2), ("profile", 3))

rlQosServTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 1), )
if mibBuilder.loadTexts: rlQosServTemplateTable.setStatus('current')
rlQosServTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 1, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServTemplateIndex"))
if mibBuilder.loadTexts: rlQosServTemplateEntry.setStatus('current')
rlQosServTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rlQosServTemplateIndex.setStatus('current')
rlQosServTemplateDestMac = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateDestMac.setStatus('current')
rlQosServTemplateDestMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateDestMacMask.setStatus('current')
rlQosServTemplateSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateSrcMac.setStatus('current')
rlQosServTemplateSrcMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateSrcMacMask.setStatus('current')
rlQosServTemplateVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateVlan.setStatus('current')
rlQosServTemplateDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateDestIp.setStatus('current')
rlQosServTemplateDestIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 8), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateDestIpMask.setStatus('current')
rlQosServTemplateSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateSrcIp.setStatus('current')
rlQosServTemplateSrcIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 10), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateSrcIpMask.setStatus('current')
rlQosServTemplateIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateIpProtocol.setStatus('current')
rlQosServTemplateSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateSrcPort.setStatus('current')
rlQosServTemplateDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateDestPort.setStatus('current')
rlQosServTemplateTos = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateTos.setStatus('current')
rlQosServTemplateVpt = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateVpt.setStatus('current')
rlQosServTemplateEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateEtherType.setStatus('current')
rlQosServTemplateTcpFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateTcpFlags.setStatus('current')
rlQosServTemplateIcmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateIcmpType.setStatus('current')
rlQosServTemplateIcmpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 19), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateIcmpCode.setStatus('current')
rlQosServTemplateIgmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 20), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServTemplateIgmpType.setStatus('current')
rlQosServFclTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 2), )
if mibBuilder.loadTexts: rlQosServFclTable.setStatus('current')
rlQosServFclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 2, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServFclIndex"), (0, "RADLAN-QOS-SERV", "rlQosServFclFcePriority"))
if mibBuilder.loadTexts: rlQosServFclEntry.setStatus('current')
rlQosServFclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlQosServFclIndex.setStatus('current')
rlQosServFclFcePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: rlQosServFclFcePriority.setStatus('current')
rlQosServFclFceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFclFceIndex.setStatus('current')
rlQosServFclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFclStatus.setStatus('current')
rlQosServFceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 3), )
if mibBuilder.loadTexts: rlQosServFceTable.setStatus('current')
rlQosServFceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 3, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServFceIndex"))
if mibBuilder.loadTexts: rlQosServFceEntry.setStatus('current')
rlQosServFceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rlQosServFceIndex.setStatus('current')
rlQosServFceErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noError", 1), ("noTemplate", 2))).clone('noError')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServFceErrorCode.setStatus('current')
rlQosServFceSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 3), Bits().clone(namedValues=NamedValues(("macDestAddr", 0), ("macSrcAddr", 1), ("vlan", 2), ("ipDestAddr", 3), ("ipSrcAddr", 4), ("ipProtocol", 5), ("destPort", 6), ("srcPort", 7), ("dscp", 8), ("ipPrecedence", 9), ("vpt", 10), ("etherType", 11), ("tcpFlags", 12), ("icmpType", 13), ("icmpCode", 14), ("igmpType", 15)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceSelection.setStatus('current')
rlQosServFceDestMac = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceDestMac.setStatus('current')
rlQosServFceDestMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceDestMacMask.setStatus('current')
rlQosServFceSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 6), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceSrcMac.setStatus('current')
rlQosServFceSrcMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceSrcMacMask.setStatus('current')
rlQosServFceVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceVlan.setStatus('current')
rlQosServFceVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceVlanMask.setStatus('current')
rlQosServFceDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 10), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceDestIp.setStatus('current')
rlQosServFceDestIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 11), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceDestIpMask.setStatus('current')
rlQosServFceSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 12), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceSrcIp.setStatus('current')
rlQosServFceSrcIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 13), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceSrcIpMask.setStatus('current')
rlQosServFceIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceIpProtocol.setStatus('current')
rlQosServFceDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceDestPort.setStatus('current')
rlQosServFceDestPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceDestPortMask.setStatus('current')
rlQosServFceSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceSrcPort.setStatus('current')
rlQosServFceSrcPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceSrcPortMask.setStatus('current')
rlQosServFceDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceDscp.setStatus('current')
rlQosServFceIpPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceIpPrecedence.setStatus('current')
rlQosServFceVpt = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceVpt.setStatus('current')
rlQosServFceVptMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 22), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceVptMask.setStatus('current')
rlQosServFceEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1501, 65536)).clone(1501)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceEtherType.setStatus('current')
rlQosServFceTcpFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceTcpFlags.setStatus('current')
rlQosServFceTcpFlagsMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceTcpFlagsMask.setStatus('current')
rlQosServFceIcmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceIcmpType.setStatus('current')
rlQosServFceIcmpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceIcmpCode.setStatus('current')
rlQosServFceIgmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceIgmpType.setStatus('current')
rlQosServFceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 29), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServFceStatus.setStatus('current')
rlQosServProfileTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 4), )
if mibBuilder.loadTexts: rlQosServProfileTable.setStatus('current')
rlQosServProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 4, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServProfileIndex"))
if mibBuilder.loadTexts: rlQosServProfileEntry.setStatus('current')
rlQosServProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: rlQosServProfileIndex.setStatus('current')
rlQosServProfileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("regular", 1), ("aggregate", 2))).clone('regular')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServProfileType.setStatus('current')
rlQosServProfileServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("bestEffort", 1), ("minDelay", 2), ("committedDelay", 3), ("minMaxBandwidth", 4), ("committedBoundBandwidth", 5), ("rateLimit", 6), ("trustCos", 7), ("trustDscp", 8), ("trust", 9), ("drop", 10), ("dropAndDisablePort", 11))).clone('bestEffort')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServProfileServiceType.setStatus('current')
rlQosServProfileIngressBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000)).clone(3000)).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServProfileIngressBurstSize.setStatus('current')
rlQosServProfileMaxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServProfileMaxBandwidth.setStatus('current')
rlQosServProfileMinBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServProfileMinBandwidth.setStatus('current')
rlQosServProfileMaxDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 7), Unsigned32()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServProfileMaxDelay.setStatus('current')
rlQosServProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServProfileStatus.setStatus('current')
rlQosServServiceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 5), )
if mibBuilder.loadTexts: rlQosServServiceTable.setStatus('current')
rlQosServServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 5, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServServiceIndex"))
if mibBuilder.loadTexts: rlQosServServiceEntry.setStatus('current')
rlQosServServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: rlQosServServiceIndex.setStatus('current')
rlQosServServicePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServServicePriority.setStatus('current')
rlQosServServiceProfilePointer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServServiceProfilePointer.setStatus('current')
rlQosServServiceFclPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServServiceFclPointer.setStatus('current')
rlQosServServiceInIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 5), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServServiceInIfList.setStatus('current')
rlQosServServiceOutIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 6), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServServiceOutIfList.setStatus('current')
rlQosServServiceScaledOutIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 7), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServServiceScaledOutIfList.setStatus('current')
rlQosServServiceProfileParamOper = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServServiceProfileParamOper.setStatus('current')
rlQosServServiceStatusOper = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 9), RlQosServServiceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServServiceStatusOper.setStatus('current')
rlQosServServiceStatusAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 10), RlQosServServiceStatus().clone('suspended')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServServiceStatusAdmin.setStatus('current')
rlQosServServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServServiceStatus.setStatus('current')
rlQosServServicePriorityTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 6), )
if mibBuilder.loadTexts: rlQosServServicePriorityTable.setStatus('current')
rlQosServServicePriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 6, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServServicePriorityIndex"))
if mibBuilder.loadTexts: rlQosServServicePriorityEntry.setStatus('current')
rlQosServServicePriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: rlQosServServicePriorityIndex.setStatus('current')
rlQosServServicePriorityPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServServicePriorityPointer.setStatus('current')
rlQosServServiceDefaultMappingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 7), )
if mibBuilder.loadTexts: rlQosServServiceDefaultMappingTable.setStatus('current')
rlQosServServiceDefaultMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 7, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServServiceDefaultMappingType"))
if mibBuilder.loadTexts: rlQosServServiceDefaultMappingEntry.setStatus('current')
rlQosServServiceDefaultMappingType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("bestEffort", 1), ("minDelay", 2), ("committedDelay", 3), ("minMaxBandwidth", 4), ("committedBoundBandwidth", 5), ("rateLimit", 6), ("trustDscp", 7))))
if mibBuilder.loadTexts: rlQosServServiceDefaultMappingType.setStatus('current')
rlQosServServiceDefaultMappingDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServServiceDefaultMappingDscp.setStatus('current')
rlQosServServiceDefaultMappingVpt = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServServiceDefaultMappingVpt.setStatus('current')
rlQosServScalingErrorTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 8), )
if mibBuilder.loadTexts: rlQosServScalingErrorTable.setStatus('current')
rlQosServScalingErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 8, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServScalingErrorIfIndex"))
if mibBuilder.loadTexts: rlQosServScalingErrorEntry.setStatus('current')
rlQosServScalingErrorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlQosServScalingErrorIfIndex.setStatus('current')
rlQosServScalingErrorReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("changeSpeed-10000to1000", 1), ("changeSpeed-10000to100", 2), ("changeSpeed-10000to10", 3), ("changeSpeed-1000to100", 4), ("changeSpeed-1000to10", 5), ("changeSpeed-100to10", 6), ("changeSpeed-10to100", 7), ("changeSpeed-10to1000", 8), ("changeSpeed-10to10000", 9), ("changeSpeed-100to1000", 10), ("changeSpeed-100to10000", 11), ("changeSpeed-1000to10000", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServScalingErrorReason.setStatus('current')
rlQosServFreeSequentialTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 9), )
if mibBuilder.loadTexts: rlQosServFreeSequentialTable.setStatus('current')
rlQosServFreeSequentialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 9, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServFreeSequentialId"))
if mibBuilder.loadTexts: rlQosServFreeSequentialEntry.setStatus('current')
rlQosServFreeSequentialId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("fcl", 1), ("fce", 2), ("profile", 3), ("service", 4), ("priorityService", 5))))
if mibBuilder.loadTexts: rlQosServFreeSequentialId.setStatus('current')
rlQosServFreeSequentialValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServFreeSequentialValue.setStatus('current')
rlQosServNameToIndexTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 10), )
if mibBuilder.loadTexts: rlQosServNameToIndexTable.setStatus('current')
rlQosServNameToIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 10, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServNameToIndexTableId"), (0, "RADLAN-QOS-SERV", "rlQosServNameToIndexName"))
if mibBuilder.loadTexts: rlQosServNameToIndexEntry.setStatus('current')
rlQosServNameToIndexTableId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 1), RlQosServNamedTableId())
if mibBuilder.loadTexts: rlQosServNameToIndexTableId.setStatus('current')
rlQosServNameToIndexName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlQosServNameToIndexName.setStatus('current')
rlQosServNameToIndexValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServNameToIndexValue.setStatus('current')
rlQosServNameToIndexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlQosServNameToIndexStatus.setStatus('current')
rlQosServIndexToNameTable = MibTable((1, 3, 6, 1, 4, 1, 89, 99, 11), )
if mibBuilder.loadTexts: rlQosServIndexToNameTable.setStatus('current')
rlQosServIndexToNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 99, 11, 1), ).setIndexNames((0, "RADLAN-QOS-SERV", "rlQosServIndexToNameTableId"), (0, "RADLAN-QOS-SERV", "rlQosServIndexToNameIndex"))
if mibBuilder.loadTexts: rlQosServIndexToNameEntry.setStatus('current')
rlQosServIndexToNameTableId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 11, 1, 1), RlQosServNamedTableId())
if mibBuilder.loadTexts: rlQosServIndexToNameTableId.setStatus('current')
rlQosServIndexToNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 11, 1, 2), Integer32())
if mibBuilder.loadTexts: rlQosServIndexToNameIndex.setStatus('current')
rlQosServIndexToNameValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 99, 11, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServIndexToNameValue.setStatus('current')
rlQosServMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 99, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlQosServMibVersion.setStatus('current')
rlQosServMibAction = MibScalar((1, 3, 6, 1, 4, 1, 89, 99, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("importPolicy", 2), ("noImportPolicy", 3), ("flatServicePriorities", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlQosServMibAction.setStatus('current')
mibBuilder.exportSymbols("RADLAN-QOS-SERV", rlQosServFreeSequentialTable=rlQosServFreeSequentialTable, rlQosServFceErrorCode=rlQosServFceErrorCode, rlQosServNameToIndexTableId=rlQosServNameToIndexTableId, rlQosServScalingErrorTable=rlQosServScalingErrorTable, rlQosServProfileMaxDelay=rlQosServProfileMaxDelay, rlQosServTemplateVlan=rlQosServTemplateVlan, rlQosServTemplateDestMac=rlQosServTemplateDestMac, rlQosServServiceStatusAdmin=rlQosServServiceStatusAdmin, rlQosServServiceDefaultMappingVpt=rlQosServServiceDefaultMappingVpt, rlQosServFreeSequentialId=rlQosServFreeSequentialId, rlQosServNameToIndexStatus=rlQosServNameToIndexStatus, rlQosServFclStatus=rlQosServFclStatus, rlQosServFceSrcMac=rlQosServFceSrcMac, rlQosServFceDestPortMask=rlQosServFceDestPortMask, rlQosServFceSrcPortMask=rlQosServFceSrcPortMask, rlQosServServiceScaledOutIfList=rlQosServServiceScaledOutIfList, rlQosServFceIpPrecedence=rlQosServFceIpPrecedence, rlQosServIndexToNameIndex=rlQosServIndexToNameIndex, rlQosServTemplateSrcMacMask=rlQosServTemplateSrcMacMask, rlQosServFclFceIndex=rlQosServFclFceIndex, rlQosServIndexToNameTable=rlQosServIndexToNameTable, rlQosServFceVlanMask=rlQosServFceVlanMask, rlQosServFceIndex=rlQosServFceIndex, rlQosServFceDestIpMask=rlQosServFceDestIpMask, rlQosServFceIcmpCode=rlQosServFceIcmpCode, rlQosServFceEtherType=rlQosServFceEtherType, rlQosServFceVlan=rlQosServFceVlan, rlQosServNameToIndexTable=rlQosServNameToIndexTable, rlQosServMibAction=rlQosServMibAction, rlQosServTemplateDestMacMask=rlQosServTemplateDestMacMask, rlQosServServiceProfilePointer=rlQosServServiceProfilePointer, rlQosServFceIpProtocol=rlQosServFceIpProtocol, rlQosServTemplateIndex=rlQosServTemplateIndex, rlQosServProfileIndex=rlQosServProfileIndex, rlQosServFceTcpFlags=rlQosServFceTcpFlags, rlQosServFceSrcIp=rlQosServFceSrcIp, rlQosServTemplateTcpFlags=rlQosServTemplateTcpFlags, rlQosServFceSrcMacMask=rlQosServFceSrcMacMask, rlQosServServiceStatusOper=rlQosServServiceStatusOper, rlQosServFceSelection=rlQosServFceSelection, rlQosServFceStatus=rlQosServFceStatus, rlQosServFceSrcPort=rlQosServFceSrcPort, rlQosServServicePriorityTable=rlQosServServicePriorityTable, rlQosServTemplateIpProtocol=rlQosServTemplateIpProtocol, rlQosServFceTcpFlagsMask=rlQosServFceTcpFlagsMask, rlQosServTemplateTable=rlQosServTemplateTable, rlQosServProfileEntry=rlQosServProfileEntry, rlQosServFceDscp=rlQosServFceDscp, rlQosServProfileServiceType=rlQosServProfileServiceType, rlQosServFclFcePriority=rlQosServFclFcePriority, rlQosServServiceInIfList=rlQosServServiceInIfList, RlQosServServiceStatus=RlQosServServiceStatus, rlQosServFceVptMask=rlQosServFceVptMask, rlQosServFceEntry=rlQosServFceEntry, rlQosServFreeSequentialEntry=rlQosServFreeSequentialEntry, rlQosServProfileType=rlQosServProfileType, rlQosServServicePriorityPointer=rlQosServServicePriorityPointer, rlQosServTemplateVpt=rlQosServTemplateVpt, rlQosServServiceTable=rlQosServServiceTable, rlQosServTemplateDestIpMask=rlQosServTemplateDestIpMask, rlQosServIndexToNameEntry=rlQosServIndexToNameEntry, rlQosServServicePriorityEntry=rlQosServServicePriorityEntry, PYSNMP_MODULE_ID=rlQosServ, rlQosServFceDestMacMask=rlQosServFceDestMacMask, rlQosServNameToIndexValue=rlQosServNameToIndexValue, rlQosServFceDestMac=rlQosServFceDestMac, rlQosServProfileIngressBurstSize=rlQosServProfileIngressBurstSize, rlQosServFceDestPort=rlQosServFceDestPort, rlQosServTemplateSrcIp=rlQosServTemplateSrcIp, rlQosServFceIgmpType=rlQosServFceIgmpType, rlQosServIndexToNameTableId=rlQosServIndexToNameTableId, rlQosServIndexToNameValue=rlQosServIndexToNameValue, rlQosServProfileTable=rlQosServProfileTable, rlQosServTemplateDestPort=rlQosServTemplateDestPort, rlQosServFreeSequentialValue=rlQosServFreeSequentialValue, rlQosServServiceDefaultMappingType=rlQosServServiceDefaultMappingType, rlQosServServiceFclPointer=rlQosServServiceFclPointer, rlQosServTemplateSrcMac=rlQosServTemplateSrcMac, rlQosServServiceDefaultMappingTable=rlQosServServiceDefaultMappingTable, rlQosServTemplateSrcIpMask=rlQosServTemplateSrcIpMask, rlQosServFclIndex=rlQosServFclIndex, rlQosServTemplateDestIp=rlQosServTemplateDestIp, rlQosServFceTable=rlQosServFceTable, rlQosServFclEntry=rlQosServFclEntry, rlQosServServicePriority=rlQosServServicePriority, rlQosServMibVersion=rlQosServMibVersion, rlQosServServiceDefaultMappingDscp=rlQosServServiceDefaultMappingDscp, rlQosServNameToIndexName=rlQosServNameToIndexName, rlQosServTemplateSrcPort=rlQosServTemplateSrcPort, rlQosServServiceEntry=rlQosServServiceEntry, rlQosServFceDestIp=rlQosServFceDestIp, rlQosServServiceOutIfList=rlQosServServiceOutIfList, rlQosServScalingErrorIfIndex=rlQosServScalingErrorIfIndex, rlQosServServiceProfileParamOper=rlQosServServiceProfileParamOper, rlQosServProfileMaxBandwidth=rlQosServProfileMaxBandwidth, rlQosServFceSrcIpMask=rlQosServFceSrcIpMask, rlQosServNameToIndexEntry=rlQosServNameToIndexEntry, rlQosServProfileMinBandwidth=rlQosServProfileMinBandwidth, rlQosServTemplateTos=rlQosServTemplateTos, RlQosServNamedTableId=RlQosServNamedTableId, rlQosServTemplateIcmpType=rlQosServTemplateIcmpType, rlQosServTemplateEntry=rlQosServTemplateEntry, rlQosServProfileStatus=rlQosServProfileStatus, rlQosServServicePriorityIndex=rlQosServServicePriorityIndex, rlQosServFceVpt=rlQosServFceVpt, rlQosServTemplateIgmpType=rlQosServTemplateIgmpType, rlQosServ=rlQosServ, rlQosServTemplateIcmpCode=rlQosServTemplateIcmpCode, rlQosServServiceDefaultMappingEntry=rlQosServServiceDefaultMappingEntry, rlQosServScalingErrorEntry=rlQosServScalingErrorEntry, rlQosServFceIcmpType=rlQosServFceIcmpType, rlQosServServiceIndex=rlQosServServiceIndex, rlQosServFclTable=rlQosServFclTable, rlQosServScalingErrorReason=rlQosServScalingErrorReason, rlQosServTemplateEtherType=rlQosServTemplateEtherType, rlQosServServiceStatus=rlQosServServiceStatus)
