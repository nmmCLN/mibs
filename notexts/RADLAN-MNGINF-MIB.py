#
# PySNMP MIB module RADLAN-MNGINF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-MNGINF-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:36:30 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibIdentifier, Counter32, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "ModuleIdentity")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlMngInf = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 89))
rlMngInf.setRevisions(('2003-09-21 00:00',))
if mibBuilder.loadTexts: rlMngInf.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlMngInf.setOrganization('Radlan Computer Communications Ltd.')
class RlMngInfServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("dontCare", 0), ("telnet", 1), ("snmp", 2), ("http", 3), ("https", 4), ("ssh", 5))

class RlMngInfActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("permit", 0), ("deny", 1))

rlMngInfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfMibVersion.setStatus('current')
rlMngInfEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfEnable.setStatus('current')
rlMngInfActiveListName = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfActiveListName.setStatus('current')
rlMngInfListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 89, 4), )
if mibBuilder.loadTexts: rlMngInfListTable.setStatus('current')
rlMngInfListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 89, 4, 1), ).setIndexNames((0, "RADLAN-MNGINF-MIB", "rlMngInfListName"), (0, "RADLAN-MNGINF-MIB", "rlMngInfListPriority"))
if mibBuilder.loadTexts: rlMngInfListEntry.setStatus('current')
rlMngInfListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListName.setStatus('current')
rlMngInfListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListPriority.setStatus('current')
rlMngInfListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIfIndex.setStatus('current')
rlMngInfListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIpAddr.setStatus('current')
rlMngInfListIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIpNetMask.setStatus('current')
rlMngInfListService = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 6), RlMngInfServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListService.setStatus('current')
rlMngInfListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 7), RlMngInfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListAction.setStatus('current')
rlMngInfListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListRowStatus.setStatus('current')
rlMngInfAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfAuditingEnable.setStatus('current')
mibBuilder.exportSymbols("RADLAN-MNGINF-MIB", rlMngInfListRowStatus=rlMngInfListRowStatus, rlMngInfListIpNetMask=rlMngInfListIpNetMask, rlMngInfListEntry=rlMngInfListEntry, rlMngInfListService=rlMngInfListService, rlMngInf=rlMngInf, rlMngInfListPriority=rlMngInfListPriority, rlMngInfListIfIndex=rlMngInfListIfIndex, rlMngInfListIpAddr=rlMngInfListIpAddr, rlMngInfAuditingEnable=rlMngInfAuditingEnable, rlMngInfMibVersion=rlMngInfMibVersion, rlMngInfListAction=rlMngInfListAction, RlMngInfServiceType=RlMngInfServiceType, rlMngInfEnable=rlMngInfEnable, rlMngInfListTable=rlMngInfListTable, PYSNMP_MODULE_ID=rlMngInf, rlMngInfActiveListName=rlMngInfActiveListName, rlMngInfListName=rlMngInfListName, RlMngInfActionType=RlMngInfActionType)
