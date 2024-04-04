#
# PySNMP MIB module AT-EPSRv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-EPSRv2-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:34 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, ObjectIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Integer32, Unsigned32, IpAddress, NotificationType, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Integer32", "Unsigned32", "IpAddress", "NotificationType", "Counter32", "Counter64")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
atEpsrv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536))
atEpsrv2.setRevisions(('2011-07-07 00:00', '2010-09-07 00:00', '2010-06-14 04:55', '2010-05-24 01:19', '2010-01-15 00:39', '2008-12-23 01:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atEpsrv2.setRevisionsDescriptions(('Added 5 new objects for superloop prevention (EPSR-SLP)', 'Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'OID of atEpsrv2Events reverted to 1 but deprecated. Added atEpsrv2Notifications', 'Changed the OID value of atEpsrv2Events from 1 to 0 to meet RFC 3584 3.1', 'Initial Revision',))
if mibBuilder.loadTexts: atEpsrv2.setLastUpdated('201107070000Z')
if mibBuilder.loadTexts: atEpsrv2.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: atEpsrv2.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atEpsrv2.setDescription('Convert epsrv2Variables into a table entry, so variable of multiple\n                EPSRv2 domains can be obtained.')
class AtEpsrv2NodeState(TextualConvention, Integer32):
    description = 'Defines the node states that can be passed around\n                in EPSRv2 Node Traps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 0), ("complete", 1), ("failed", 2), ("linksUp", 3), ("linksDown", 4), ("preForward", 5), ("unknown", 6))

class AtEpsrv2InterfaceState(TextualConvention, Integer32):
    description = 'Defines the interface states that can be passed around\n                in EPSRv2 Node Traps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("down", 2), ("blocked", 3), ("forward", 4))

atEpsrv2Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 0))
atEpsrv2Notify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 0, 1)).setObjects(("AT-EPSRv2-MIB", "atEpsrv2NodeType"), ("AT-EPSRv2-MIB", "atEpsrv2DomainName"), ("AT-EPSRv2-MIB", "atEpsrv2DomainID"), ("AT-EPSRv2-MIB", "atEpsrv2FromState"), ("AT-EPSRv2-MIB", "atEpsrv2CurrentState"), ("AT-EPSRv2-MIB", "atEpsrv2ControlVlanId"), ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfIndex"), ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfState"), ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfIndex"), ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfState"), ("AT-EPSRv2-MIB", "atEpsrv2DomainPriority"), ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfIsOnCommonSeg"), ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfIsOnCommonSeg"), ("AT-EPSRv2-MIB", "atEpsrv2HasControlOfPrimaryIf"), ("AT-EPSRv2-MIB", "atEpsrv2HasControlOfSecondaryIf"))
if mibBuilder.loadTexts: atEpsrv2Notify.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2Notify.setDescription('EPSRv2 Master/Transit node state transition notification.')
atEpsrv2Events = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 1))
atEpsrv2NodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 1, 1)).setObjects(("AT-EPSRv2-MIB", "atEpsrv2NodeType"), ("AT-EPSRv2-MIB", "atEpsrv2DomainName"), ("AT-EPSRv2-MIB", "atEpsrv2DomainID"), ("AT-EPSRv2-MIB", "atEpsrv2FromState"), ("AT-EPSRv2-MIB", "atEpsrv2CurrentState"), ("AT-EPSRv2-MIB", "atEpsrv2ControlVlanId"), ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfIndex"), ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfState"), ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfIndex"), ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfState"))
if mibBuilder.loadTexts: atEpsrv2NodeTrap.setStatus('deprecated')
if mibBuilder.loadTexts: atEpsrv2NodeTrap.setDescription('EPSRv2 Master/Transit node state transition trap.')
atEpsrv2VariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2), )
if mibBuilder.loadTexts: atEpsrv2VariablesTable.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2VariablesTable.setDescription('This table contains rows of epsrv2VariablesEntry.')
atEpsrv2VariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1), ).setIndexNames((0, "AT-EPSRv2-MIB", "atEpsrv2DomainID"))
if mibBuilder.loadTexts: atEpsrv2VariablesEntry.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2VariablesEntry.setDescription('An entry in the ATL enterprise epsrv2VariablesTable.')
atEpsrv2NodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("masterNode", 1), ("transitNode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2NodeType.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2NodeType.setDescription('This is the type of the EPSRv2 node (master/transit).')
atEpsrv2DomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 2), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2DomainName.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2DomainName.setDescription('Assigned name of the EPSRv2 domain.')
atEpsrv2DomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2DomainID.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2DomainID.setDescription('Assigned ID of the EPSRv2 domain.')
atEpsrv2FromState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 4), AtEpsrv2NodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2FromState.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2FromState.setDescription('Defined state that an EPSR domain is transitioning from.')
atEpsrv2CurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 5), AtEpsrv2NodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2CurrentState.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2CurrentState.setDescription('Defined the current state of an EPSRv2 domain.')
atEpsrv2ControlVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2ControlVlanId.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2ControlVlanId.setDescription('VLAN identifier for the control VLAN.')
atEpsrv2PrimaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 7), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2PrimaryIfIndex.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2PrimaryIfIndex.setDescription('IfIndex of the primary interface.')
atEpsrv2PrimaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 8), AtEpsrv2InterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2PrimaryIfState.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2PrimaryIfState.setDescription('Defined current state of the primary interface.')
atEpsrv2SecondaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2SecondaryIfIndex.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2SecondaryIfIndex.setDescription('IfIndex of the secondary interface.')
atEpsrv2SecondaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 10), AtEpsrv2InterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2SecondaryIfState.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2SecondaryIfState.setDescription('Defined current state of the secondary interface.')
atEpsrv2DomainPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2DomainPriority.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2DomainPriority.setDescription('The priority of the EPSRv2 domain. This value is used for\n                 superloop prevention.')
atEpsrv2PrimaryIfIsOnCommonSeg = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2PrimaryIfIsOnCommonSeg.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2PrimaryIfIsOnCommonSeg.setDescription('Returns 1 (true) if the primary interface is on a common\n                 segment i.e. the port is shared with other instances that have\n                 the port in the same set of data VLANs, else it returns\n                 2 (false).')
atEpsrv2SecondaryIfIsOnCommonSeg = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2SecondaryIfIsOnCommonSeg.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2SecondaryIfIsOnCommonSeg.setDescription('Returns 1 (true) if the secondary interface is on a common\n                 segment i.e. the port is shared with other instances that have\n                 the port in the same set of data VLANs, else it returns\n                 2 (false).')
atEpsrv2HasControlOfPrimaryIf = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2HasControlOfPrimaryIf.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2HasControlOfPrimaryIf.setDescription('Returns 2 (false) if the EPSR instance does not have physical\n                 control of its primary interface because it is on a common\n                 segment and is not the highest priority instance, else it\n                 returns 1 (true).')
atEpsrv2HasControlOfSecondaryIf = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2HasControlOfSecondaryIf.setStatus('current')
if mibBuilder.loadTexts: atEpsrv2HasControlOfSecondaryIf.setDescription('Returns 2 (false) if the EPSR instance does not have physical\n                 control of its secondary interface because it is on a common\n                 segment and is not the highest priority instance, else it\n                 returns 1 (true).')
mibBuilder.exportSymbols("AT-EPSRv2-MIB", atEpsrv2Notifications=atEpsrv2Notifications, atEpsrv2SecondaryIfState=atEpsrv2SecondaryIfState, atEpsrv2VariablesTable=atEpsrv2VariablesTable, atEpsrv2PrimaryIfIndex=atEpsrv2PrimaryIfIndex, atEpsrv2PrimaryIfState=atEpsrv2PrimaryIfState, atEpsrv2=atEpsrv2, atEpsrv2SecondaryIfIsOnCommonSeg=atEpsrv2SecondaryIfIsOnCommonSeg, atEpsrv2Notify=atEpsrv2Notify, AtEpsrv2NodeState=AtEpsrv2NodeState, atEpsrv2DomainName=atEpsrv2DomainName, atEpsrv2HasControlOfPrimaryIf=atEpsrv2HasControlOfPrimaryIf, PYSNMP_MODULE_ID=atEpsrv2, atEpsrv2CurrentState=atEpsrv2CurrentState, atEpsrv2SecondaryIfIndex=atEpsrv2SecondaryIfIndex, atEpsrv2VariablesEntry=atEpsrv2VariablesEntry, atEpsrv2HasControlOfSecondaryIf=atEpsrv2HasControlOfSecondaryIf, atEpsrv2FromState=atEpsrv2FromState, atEpsrv2NodeType=atEpsrv2NodeType, atEpsrv2ControlVlanId=atEpsrv2ControlVlanId, atEpsrv2DomainPriority=atEpsrv2DomainPriority, AtEpsrv2InterfaceState=AtEpsrv2InterfaceState, atEpsrv2NodeTrap=atEpsrv2NodeTrap, atEpsrv2PrimaryIfIsOnCommonSeg=atEpsrv2PrimaryIfIsOnCommonSeg, atEpsrv2DomainID=atEpsrv2DomainID, atEpsrv2Events=atEpsrv2Events)
