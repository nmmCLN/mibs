#
# PySNMP MIB module DOCS-SUBMGT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/DOCS-SUBMGT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:26 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
docsIfCmtsCmStatusIndex, docsIfCmtsCmStatusEntry = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusIndex", "docsIfCmtsCmStatusEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Integer32, TimeTicks, NotificationType, Gauge32, Bits, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter64, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "Bits", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "Counter32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
docsSubMgt = ModuleIdentity((1, 3, 6, 1, 3, 83, 4))
if mibBuilder.loadTexts: docsSubMgt.setLastUpdated('0007120000Z')
if mibBuilder.loadTexts: docsSubMgt.setOrganization('IETF IPCDN Working Group')
docsSubMgtObjects = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 1))
class IpV4orV6Addr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
docsSubMgtCpeControlTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 1), )
if mibBuilder.loadTexts: docsSubMgtCpeControlTable.setStatus('current')
docsSubMgtCpeControlEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 1, 1), )
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlEntry"))
docsSubMgtCpeControlEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsSubMgtCpeControlEntry.setStatus('current')
docsSubMgtCpeControlMaxCpeIp = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlMaxCpeIp.setStatus('current')
docsSubMgtCpeControlActive = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlActive.setStatus('current')
docsSubMgtCpeControlLearnable = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlLearnable.setStatus('current')
docsSubMgtCpeControlReset = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlReset.setStatus('current')
docsSubMgtCpeMaxIpDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeMaxIpDefault.setStatus('current')
docsSubMgtCpeActiveDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeActiveDefault.setStatus('current')
docsSubMgtCpeLearnableDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeLearnableDefault.setStatus('current')
docsSubMgtCpeIpTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 5), )
if mibBuilder.loadTexts: docsSubMgtCpeIpTable.setStatus('current')
docsSubMgtCpeIpEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 5, 1), ).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"), (0, "DOCS-SUBMGT-MIB", "docsSubMgtCpeIpIndex"))
if mibBuilder.loadTexts: docsSubMgtCpeIpEntry.setStatus('current')
docsSubMgtCpeIpIndex = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: docsSubMgtCpeIpIndex.setStatus('current')
docsSubMgtCpeIpAddr = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 2), IpV4orV6Addr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeIpAddr.setStatus('current')
docsSubMgtCpeIpLearned = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeIpLearned.setStatus('current')
docsSubMgtPktFilterTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 6), )
if mibBuilder.loadTexts: docsSubMgtPktFilterTable.setStatus('current')
docsSubMgtPktFilterEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 6, 1), ).setIndexNames((0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterGroup"), (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterIndex"))
if mibBuilder.loadTexts: docsSubMgtPktFilterEntry.setStatus('current')
docsSubMgtPktFilterGroup = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: docsSubMgtPktFilterGroup.setStatus('current')
docsSubMgtPktFilterIndex = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: docsSubMgtPktFilterIndex.setStatus('current')
docsSubMgtPktFilterSrcAddr = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 3), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterSrcAddr.setStatus('current')
docsSubMgtPktFilterSrcMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 4), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterSrcMask.setStatus('current')
docsSubMgtPktFilterDstAddr = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 5), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterDstAddr.setStatus('current')
docsSubMgtPktFilterDstMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 6), IpV4orV6Addr().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterDstMask.setStatus('current')
docsSubMgtPktFilterUlp = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterUlp.setStatus('current')
docsSubMgtPktFilterTosValue = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="0")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterTosValue.setStatus('current')
docsSubMgtPktFilterTosMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="0")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterTosMask.setStatus('current')
docsSubMgtPktFilterAction = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accept", 1), ("drop", 2))).clone('accept')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterAction.setStatus('current')
docsSubMgtPktFilterMatches = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtPktFilterMatches.setStatus('current')
docsSubMgtPktFilterStatus = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtPktFilterStatus.setStatus('current')
docsSubMgtTcpUdpFilterTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 7), )
if mibBuilder.loadTexts: docsSubMgtTcpUdpFilterTable.setStatus('current')
docsSubMgtTcpUdpFilterEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 7, 1), ).setIndexNames((0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterGroup"), (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterIndex"))
if mibBuilder.loadTexts: docsSubMgtTcpUdpFilterEntry.setStatus('current')
docsSubMgtTcpUdpSrcPort = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536)).clone(65536)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpUdpSrcPort.setStatus('current')
docsSubMgtTcpUdpDstPort = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536)).clone(65536)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpUdpDstPort.setStatus('current')
docsSubMgtTcpFlagValues = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 3), Bits().clone(namedValues=NamedValues(("urgent", 0), ("ack", 1), ("push", 2), ("reset", 3), ("syn", 4), ("fin", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpFlagValues.setStatus('current')
docsSubMgtTcpFlagMask = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 4), Bits().clone(namedValues=NamedValues(("urgent", 0), ("ack", 1), ("push", 2), ("reset", 3), ("syn", 4), ("fin", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpFlagMask.setStatus('current')
docsSubMgtTcpUdpStatus = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubMgtTcpUdpStatus.setStatus('current')
docsSubMgtCmFilterTable = MibTable((1, 3, 6, 1, 3, 83, 4, 1, 8), )
if mibBuilder.loadTexts: docsSubMgtCmFilterTable.setStatus('current')
docsSubMgtCmFilterEntry = MibTableRow((1, 3, 6, 1, 3, 83, 4, 1, 8, 1), )
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterEntry"))
docsSubMgtCmFilterEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsSubMgtCmFilterEntry.setStatus('current')
docsSubMgtSubFilterDownstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterDownstream.setStatus('current')
docsSubMgtSubFilterUpstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterUpstream.setStatus('current')
docsSubMgtCmFilterDownstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterDownstream.setStatus('current')
docsSubMgtCmFilterUpstream = MibTableColumn((1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterUpstream.setStatus('current')
docsSubMgtSubFilterDownDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterDownDefault.setStatus('current')
docsSubMgtSubFilterUpDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtSubFilterUpDefault.setStatus('current')
docsSubMgtCmFilterDownDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterDownDefault.setStatus('current')
docsSubMgtCmFilterUpDefault = MibScalar((1, 3, 6, 1, 3, 83, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterUpDefault.setStatus('current')
docsSubMgtNotification = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 2))
docsSubMgtConformance = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 3))
docsSubMgtCompliances = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 3, 1))
docsSubMgtGroups = MibIdentifier((1, 3, 6, 1, 3, 83, 4, 3, 2))
docsSubMgtBasicCompliance = ModuleCompliance((1, 3, 6, 1, 3, 83, 4, 3, 1, 1)).setObjects(("DOCS-SUBMGT-MIB", "docsSubMgtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSubMgtBasicCompliance = docsSubMgtBasicCompliance.setStatus('current')
docsSubMgtGroup = ObjectGroup((1, 3, 6, 1, 3, 83, 4, 3, 2, 1)).setObjects(("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlMaxCpeIp"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlActive"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlLearnable"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlReset"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeMaxIpDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeActiveDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeLearnableDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeIpAddr"), ("DOCS-SUBMGT-MIB", "docsSubMgtCpeIpLearned"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterSrcAddr"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterSrcMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterDstAddr"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterDstMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterUlp"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterTosValue"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterTosMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterAction"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterMatches"), ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterStatus"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpSrcPort"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpDstPort"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpFlagValues"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpFlagMask"), ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpStatus"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterDownstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterUpstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterDownstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterUpstream"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterDownDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterUpDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterDownDefault"), ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterUpDefault"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSubMgtGroup = docsSubMgtGroup.setStatus('current')
mibBuilder.exportSymbols("DOCS-SUBMGT-MIB", docsSubMgtPktFilterIndex=docsSubMgtPktFilterIndex, docsSubMgtSubFilterDownstream=docsSubMgtSubFilterDownstream, docsSubMgt=docsSubMgt, docsSubMgtPktFilterUlp=docsSubMgtPktFilterUlp, docsSubMgtCmFilterUpstream=docsSubMgtCmFilterUpstream, docsSubMgtCpeMaxIpDefault=docsSubMgtCpeMaxIpDefault, docsSubMgtCmFilterEntry=docsSubMgtCmFilterEntry, docsSubMgtPktFilterDstAddr=docsSubMgtPktFilterDstAddr, docsSubMgtCpeControlReset=docsSubMgtCpeControlReset, IpV4orV6Addr=IpV4orV6Addr, docsSubMgtCmFilterDownstream=docsSubMgtCmFilterDownstream, docsSubMgtGroup=docsSubMgtGroup, docsSubMgtCpeIpTable=docsSubMgtCpeIpTable, docsSubMgtCpeControlActive=docsSubMgtCpeControlActive, docsSubMgtPktFilterEntry=docsSubMgtPktFilterEntry, docsSubMgtTcpUdpDstPort=docsSubMgtTcpUdpDstPort, PYSNMP_MODULE_ID=docsSubMgt, docsSubMgtTcpFlagMask=docsSubMgtTcpFlagMask, docsSubMgtConformance=docsSubMgtConformance, docsSubMgtCmFilterUpDefault=docsSubMgtCmFilterUpDefault, docsSubMgtCompliances=docsSubMgtCompliances, docsSubMgtCpeActiveDefault=docsSubMgtCpeActiveDefault, docsSubMgtCpeIpAddr=docsSubMgtCpeIpAddr, docsSubMgtCpeControlLearnable=docsSubMgtCpeControlLearnable, docsSubMgtPktFilterSrcAddr=docsSubMgtPktFilterSrcAddr, docsSubMgtCpeIpEntry=docsSubMgtCpeIpEntry, docsSubMgtPktFilterTosMask=docsSubMgtPktFilterTosMask, docsSubMgtNotification=docsSubMgtNotification, docsSubMgtCpeLearnableDefault=docsSubMgtCpeLearnableDefault, docsSubMgtCpeIpIndex=docsSubMgtCpeIpIndex, docsSubMgtCpeIpLearned=docsSubMgtCpeIpLearned, docsSubMgtPktFilterDstMask=docsSubMgtPktFilterDstMask, docsSubMgtTcpUdpFilterTable=docsSubMgtTcpUdpFilterTable, docsSubMgtCpeControlEntry=docsSubMgtCpeControlEntry, docsSubMgtSubFilterUpDefault=docsSubMgtSubFilterUpDefault, docsSubMgtPktFilterAction=docsSubMgtPktFilterAction, docsSubMgtPktFilterGroup=docsSubMgtPktFilterGroup, docsSubMgtBasicCompliance=docsSubMgtBasicCompliance, docsSubMgtTcpUdpStatus=docsSubMgtTcpUdpStatus, docsSubMgtPktFilterSrcMask=docsSubMgtPktFilterSrcMask, docsSubMgtCpeControlTable=docsSubMgtCpeControlTable, docsSubMgtPktFilterTosValue=docsSubMgtPktFilterTosValue, docsSubMgtTcpUdpSrcPort=docsSubMgtTcpUdpSrcPort, docsSubMgtObjects=docsSubMgtObjects, docsSubMgtPktFilterMatches=docsSubMgtPktFilterMatches, docsSubMgtTcpFlagValues=docsSubMgtTcpFlagValues, docsSubMgtCpeControlMaxCpeIp=docsSubMgtCpeControlMaxCpeIp, docsSubMgtPktFilterTable=docsSubMgtPktFilterTable, docsSubMgtTcpUdpFilterEntry=docsSubMgtTcpUdpFilterEntry, docsSubMgtCmFilterTable=docsSubMgtCmFilterTable, docsSubMgtGroups=docsSubMgtGroups, docsSubMgtSubFilterUpstream=docsSubMgtSubFilterUpstream, docsSubMgtSubFilterDownDefault=docsSubMgtSubFilterDownDefault, docsSubMgtPktFilterStatus=docsSubMgtPktFilterStatus, docsSubMgtCmFilterDownDefault=docsSubMgtCmFilterDownDefault)
