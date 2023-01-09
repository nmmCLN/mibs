#
# PySNMP MIB module CTRON-SSR-L2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-L2-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:47 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, TimeTicks, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, iso, Counter64, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "Counter64", "Gauge32", "NotificationType")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
l2MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 500))
l2MIB.setRevisions(('1999-09-22 00:00',))
if mibBuilder.loadTexts: l2MIB.setLastUpdated('9802090000Z')
if mibBuilder.loadTexts: l2MIB.setOrganization('Cabletron Systems, Inc.')
l2Group = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2))
l2LearnedEntryDiscards = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2LearnedEntryDiscards.setStatus('obsolete')
l2LearnedMacEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2LearnedMacEntries.setStatus('obsolete')
l2LearnedFlowEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2LearnedFlowEntries.setStatus('obsolete')
l2ForwardTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4), )
if mibBuilder.loadTexts: l2ForwardTable.setStatus('obsolete')
l2ForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1), ).setIndexNames((0, "CTRON-SSR-L2-MIB", "l2ForwardFilterId"), (0, "CTRON-SSR-L2-MIB", "l2ForwardDstMacAddr"), (0, "CTRON-SSR-L2-MIB", "l2ForwardSrcMacAddr"), (0, "CTRON-SSR-L2-MIB", "l2ForwardVlanId"))
if mibBuilder.loadTexts: l2ForwardEntry.setStatus('obsolete')
l2ForwardFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2ForwardFilterId.setStatus('obsolete')
l2ForwardDstMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2ForwardDstMacAddr.setStatus('obsolete')
l2ForwardSrcMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2ForwardSrcMacAddr.setStatus('obsolete')
l2ForwardVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2ForwardVlanId.setStatus('obsolete')
l2ForwardDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2ForwardDstPort.setStatus('obsolete')
l2ForwardInPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2ForwardInPorts.setStatus('obsolete')
l2PriorityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5), )
if mibBuilder.loadTexts: l2PriorityTable.setStatus('obsolete')
l2PriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1), ).setIndexNames((0, "CTRON-SSR-L2-MIB", "l2PriorityIndex"))
if mibBuilder.loadTexts: l2PriorityEntry.setStatus('obsolete')
l2PriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PriorityIndex.setStatus('obsolete')
l2PriorityDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PriorityDesc.setStatus('obsolete')
l2PriorityDstMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 3), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PriorityDstMacAddr.setStatus('obsolete')
l2PrioritySrcMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 4), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PrioritySrcMacAddr.setStatus('obsolete')
l2PriorityVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PriorityVlanId.setStatus('obsolete')
l2PriorityInPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PriorityInPorts.setStatus('obsolete')
l2Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("low", 1), ("medium", 2), ("high", 3), ("control", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2Priority.setStatus('obsolete')
l2FilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6), )
if mibBuilder.loadTexts: l2FilterTable.setStatus('obsolete')
l2FilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1), ).setIndexNames((0, "CTRON-SSR-L2-MIB", "l2FilterIndex"))
if mibBuilder.loadTexts: l2FilterEntry.setStatus('obsolete')
l2FilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterIndex.setStatus('obsolete')
l2FilterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterDesc.setStatus('obsolete')
l2FilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("staticEntry", 1), ("addressFilter", 2), ("addressLock", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterType.setStatus('obsolete')
l2FilterRestrictions = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("allow", 1), ("disallow", 2), ("force", 3), ("none", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterRestrictions.setStatus('obsolete')
l2FilterSrcMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 5), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterSrcMacAddr.setStatus('obsolete')
l2FilterDstMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 6), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterDstMacAddr.setStatus('obsolete')
l2FilterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterVlanId.setStatus('obsolete')
l2FilterInPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterInPorts.setStatus('obsolete')
l2FilterOutPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2FilterOutPorts.setStatus('obsolete')
l2PortSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7), )
if mibBuilder.loadTexts: l2PortSecurityTable.setStatus('obsolete')
l2PortSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1), ).setIndexNames((0, "CTRON-SSR-L2-MIB", "l2PortSecurityIndex"))
if mibBuilder.loadTexts: l2PortSecurityEntry.setStatus('obsolete')
l2PortSecurityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PortSecurityIndex.setStatus('obsolete')
l2PortSecurityDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PortSecurityDesc.setStatus('obsolete')
l2PortSecurityType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sourceSecure", 1), ("destinationSecure", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PortSecurityType.setStatus('obsolete')
l2PortSecurityVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PortSecurityVlanId.setStatus('obsolete')
l2PortSecurityInPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PortSecurityInPorts.setStatus('obsolete')
l2PortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8), )
if mibBuilder.loadTexts: l2PortTable.setStatus('obsolete')
l2PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1), ).setIndexNames((0, "CTRON-SSR-L2-MIB", "l2Port"))
if mibBuilder.loadTexts: l2PortEntry.setStatus('obsolete')
l2Port = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2Port.setStatus('obsolete')
l2PortAgingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PortAgingStatus.setStatus('obsolete')
l2PortAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2PortAgingTime.setStatus('obsolete')
l2PortDemandAgeHiBound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortDemandAgeHiBound.setStatus('obsolete')
l2PortDemandAgeLowBound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortDemandAgeLowBound.setStatus('obsolete')
l2PortDemandAgeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortDemandAgeCount.setStatus('obsolete')
l2PortLearnedEntryDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortLearnedEntryDiscards.setStatus('obsolete')
l2PortSrcEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortSrcEntries.setStatus('obsolete')
l2PortDstEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortDstEntries.setStatus('obsolete')
l2PortMgmtEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortMgmtEntries.setStatus('obsolete')
l2PortMaxInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortMaxInfo.setStatus('obsolete')
l2PortInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortInFrames.setStatus('obsolete')
l2PortOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortOutFrames.setStatus('obsolete')
l2PortForwardTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9), )
if mibBuilder.loadTexts: l2PortForwardTable.setStatus('obsolete')
l2PortForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1), ).setIndexNames((0, "CTRON-SSR-L2-MIB", "l2PortForwardPort"), (0, "CTRON-SSR-L2-MIB", "l2PortForwardIndex"))
if mibBuilder.loadTexts: l2PortForwardEntry.setStatus('obsolete')
l2PortForwardPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardPort.setStatus('obsolete')
l2PortForwardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardIndex.setStatus('obsolete')
l2PortForwardDstMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardDstMacAddr.setStatus('obsolete')
l2PortForwardSrcMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardSrcMacAddr.setStatus('obsolete')
l2PortForwardVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardVlanId.setStatus('obsolete')
l2PortForwardDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardDstPort.setStatus('obsolete')
l2PortForwardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardStatus.setStatus('obsolete')
l2PortForwardLastDetectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2PortForwardLastDetectedTime.setStatus('obsolete')
l2Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2))
l2Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 1))
l2Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 2))
l2ComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 2, 1, 1)).setObjects(("CTRON-SSR-L2-MIB", "l2ConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2ComplianceV10 = l2ComplianceV10.setStatus('obsolete')
l2ConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 2, 1)).setObjects(("CTRON-SSR-L2-MIB", "l2LearnedEntryDiscards"), ("CTRON-SSR-L2-MIB", "l2LearnedMacEntries"), ("CTRON-SSR-L2-MIB", "l2LearnedFlowEntries"), ("CTRON-SSR-L2-MIB", "l2ForwardFilterId"), ("CTRON-SSR-L2-MIB", "l2ForwardDstMacAddr"), ("CTRON-SSR-L2-MIB", "l2ForwardSrcMacAddr"), ("CTRON-SSR-L2-MIB", "l2ForwardVlanId"), ("CTRON-SSR-L2-MIB", "l2ForwardDstPort"), ("CTRON-SSR-L2-MIB", "l2ForwardInPorts"), ("CTRON-SSR-L2-MIB", "l2PriorityIndex"), ("CTRON-SSR-L2-MIB", "l2PriorityDesc"), ("CTRON-SSR-L2-MIB", "l2PriorityDstMacAddr"), ("CTRON-SSR-L2-MIB", "l2PrioritySrcMacAddr"), ("CTRON-SSR-L2-MIB", "l2PriorityVlanId"), ("CTRON-SSR-L2-MIB", "l2PriorityInPorts"), ("CTRON-SSR-L2-MIB", "l2Priority"), ("CTRON-SSR-L2-MIB", "l2FilterIndex"), ("CTRON-SSR-L2-MIB", "l2FilterDesc"), ("CTRON-SSR-L2-MIB", "l2FilterType"), ("CTRON-SSR-L2-MIB", "l2FilterRestrictions"), ("CTRON-SSR-L2-MIB", "l2FilterSrcMacAddr"), ("CTRON-SSR-L2-MIB", "l2FilterDstMacAddr"), ("CTRON-SSR-L2-MIB", "l2FilterVlanId"), ("CTRON-SSR-L2-MIB", "l2FilterInPorts"), ("CTRON-SSR-L2-MIB", "l2FilterOutPorts"), ("CTRON-SSR-L2-MIB", "l2PortSecurityIndex"), ("CTRON-SSR-L2-MIB", "l2PortSecurityDesc"), ("CTRON-SSR-L2-MIB", "l2PortSecurityType"), ("CTRON-SSR-L2-MIB", "l2PortSecurityVlanId"), ("CTRON-SSR-L2-MIB", "l2PortSecurityInPorts"), ("CTRON-SSR-L2-MIB", "l2Port"), ("CTRON-SSR-L2-MIB", "l2PortAgingStatus"), ("CTRON-SSR-L2-MIB", "l2PortAgingTime"), ("CTRON-SSR-L2-MIB", "l2PortDemandAgeHiBound"), ("CTRON-SSR-L2-MIB", "l2PortDemandAgeLowBound"), ("CTRON-SSR-L2-MIB", "l2PortDemandAgeCount"), ("CTRON-SSR-L2-MIB", "l2PortLearnedEntryDiscards"), ("CTRON-SSR-L2-MIB", "l2PortSrcEntries"), ("CTRON-SSR-L2-MIB", "l2PortDstEntries"), ("CTRON-SSR-L2-MIB", "l2PortMgmtEntries"), ("CTRON-SSR-L2-MIB", "l2PortMaxInfo"), ("CTRON-SSR-L2-MIB", "l2PortInFrames"), ("CTRON-SSR-L2-MIB", "l2PortOutFrames"), ("CTRON-SSR-L2-MIB", "l2PortForwardPort"), ("CTRON-SSR-L2-MIB", "l2PortForwardIndex"), ("CTRON-SSR-L2-MIB", "l2PortForwardDstMacAddr"), ("CTRON-SSR-L2-MIB", "l2PortForwardSrcMacAddr"), ("CTRON-SSR-L2-MIB", "l2PortForwardVlanId"), ("CTRON-SSR-L2-MIB", "l2PortForwardDstPort"), ("CTRON-SSR-L2-MIB", "l2PortForwardStatus"), ("CTRON-SSR-L2-MIB", "l2PortForwardLastDetectedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2ConfGroupV10 = l2ConfGroupV10.setStatus('obsolete')
mibBuilder.exportSymbols("CTRON-SSR-L2-MIB", l2FilterInPorts=l2FilterInPorts, l2PortSecurityVlanId=l2PortSecurityVlanId, l2PortMaxInfo=l2PortMaxInfo, l2PortForwardIndex=l2PortForwardIndex, l2PortSecurityInPorts=l2PortSecurityInPorts, l2FilterSrcMacAddr=l2FilterSrcMacAddr, l2PortSecurityTable=l2PortSecurityTable, l2PortForwardPort=l2PortForwardPort, l2PortInFrames=l2PortInFrames, l2PortDemandAgeHiBound=l2PortDemandAgeHiBound, l2PortForwardEntry=l2PortForwardEntry, l2PortForwardLastDetectedTime=l2PortForwardLastDetectedTime, l2FilterEntry=l2FilterEntry, l2PortSecurityDesc=l2PortSecurityDesc, l2PriorityDesc=l2PriorityDesc, l2PortAgingTime=l2PortAgingTime, l2ForwardInPorts=l2ForwardInPorts, l2Compliances=l2Compliances, l2ConfGroupV10=l2ConfGroupV10, l2ForwardVlanId=l2ForwardVlanId, l2LearnedFlowEntries=l2LearnedFlowEntries, l2PortMgmtEntries=l2PortMgmtEntries, l2PriorityEntry=l2PriorityEntry, l2PortSecurityType=l2PortSecurityType, l2FilterType=l2FilterType, l2PortForwardTable=l2PortForwardTable, l2PortForwardSrcMacAddr=l2PortForwardSrcMacAddr, l2FilterTable=l2FilterTable, l2FilterOutPorts=l2FilterOutPorts, l2Group=l2Group, l2PortSrcEntries=l2PortSrcEntries, l2ForwardFilterId=l2ForwardFilterId, l2PortForwardStatus=l2PortForwardStatus, l2PortDemandAgeCount=l2PortDemandAgeCount, l2PriorityIndex=l2PriorityIndex, l2Groups=l2Groups, PYSNMP_MODULE_ID=l2MIB, l2PriorityInPorts=l2PriorityInPorts, l2LearnedEntryDiscards=l2LearnedEntryDiscards, l2PortDstEntries=l2PortDstEntries, l2PortDemandAgeLowBound=l2PortDemandAgeLowBound, l2PortSecurityIndex=l2PortSecurityIndex, l2FilterDstMacAddr=l2FilterDstMacAddr, l2PortAgingStatus=l2PortAgingStatus, l2PortOutFrames=l2PortOutFrames, l2FilterRestrictions=l2FilterRestrictions, l2FilterVlanId=l2FilterVlanId, l2PortSecurityEntry=l2PortSecurityEntry, l2ForwardDstMacAddr=l2ForwardDstMacAddr, l2PortForwardDstPort=l2PortForwardDstPort, l2PortTable=l2PortTable, l2LearnedMacEntries=l2LearnedMacEntries, l2ForwardSrcMacAddr=l2ForwardSrcMacAddr, l2PortForwardDstMacAddr=l2PortForwardDstMacAddr, l2ComplianceV10=l2ComplianceV10, l2FilterIndex=l2FilterIndex, l2PortLearnedEntryDiscards=l2PortLearnedEntryDiscards, l2PortForwardVlanId=l2PortForwardVlanId, l2Conformance=l2Conformance, l2ForwardDstPort=l2ForwardDstPort, l2ForwardEntry=l2ForwardEntry, l2PortEntry=l2PortEntry, l2PriorityVlanId=l2PriorityVlanId, l2Port=l2Port, l2PriorityDstMacAddr=l2PriorityDstMacAddr, l2MIB=l2MIB, l2ForwardTable=l2ForwardTable, l2Priority=l2Priority, l2PrioritySrcMacAddr=l2PrioritySrcMacAddr, l2PriorityTable=l2PriorityTable, l2FilterDesc=l2FilterDesc)
