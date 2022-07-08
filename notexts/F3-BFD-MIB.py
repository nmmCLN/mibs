#
# PySNMP MIB module F3-BFD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-BFD-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:23 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
bfdSessIndex, bfdSessEntry = mibBuilder.importSymbols("BFD-STD-MIB", "bfdSessIndex", "bfdSessEntry")
AdminState, OperationalState, VlanPriority, SecondaryState, VlanId = mibBuilder.importSymbols("CM-COMMON-MIB", "AdminState", "OperationalState", "VlanPriority", "SecondaryState", "VlanId")
neIndex, = mibBuilder.importSymbols("CM-ENTITY-MIB", "neIndex")
f3L3TrafficIPInterfaceEntry, f3L3TrafficBgpPeerEntry, f3L3TrafficOspfInterfaceEntry, f3VrfEntry = mibBuilder.importSymbols("F3-L3-MIB", "f3L3TrafficIPInterfaceEntry", "f3L3TrafficBgpPeerEntry", "f3L3TrafficOspfInterfaceEntry", "f3VrfEntry")
IANAbfdSessStateTC, = mibBuilder.importSymbols("IANA-BFD-TC-STD-MIB", "IANAbfdSessStateTC")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Integer32, Gauge32, Counter64, TimeTicks, ObjectIdentity, IpAddress, Bits, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Gauge32", "Counter64", "TimeTicks", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32")
TextualConvention, StorageType, DisplayString, RowStatus, TruthValue, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "DisplayString", "RowStatus", "TruthValue", "VariablePointer")
f3BfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38))
f3BfdMIB.setRevisions(('2021-01-28 00:00',))
if mibBuilder.loadTexts: f3BfdMIB.setLastUpdated('202101280000Z')
if mibBuilder.loadTexts: f3BfdMIB.setOrganization('ADVA Optical Networking SE')
f3BfdConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1))
f3BfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2))
class BfdSessPerfAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notApplicable", 0), ("clearCtrlPkts", 1))

bfdSessExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1), )
if mibBuilder.loadTexts: bfdSessExtTable.setStatus('current')
bfdSessExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1), )
bfdSessEntry.registerAugmentions(("F3-BFD-MIB", "bfdSessExtEntry"))
bfdSessExtEntry.setIndexNames(*bfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: bfdSessExtEntry.setStatus('current')
bfdSessExtInnerVlanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtInnerVlanControl.setStatus('current')
bfdSessExtInnerVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtInnerVlanId.setStatus('current')
bfdSessExtInnerVlanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 3), VlanPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtInnerVlanPri.setStatus('current')
bfdSessExtOuterVlanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtOuterVlanControl.setStatus('current')
bfdSessExtOuterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 5), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtOuterVlanId.setStatus('current')
bfdSessExtOuterVlanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 6), VlanPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtOuterVlanPri.setStatus('current')
bfdSessExtIpPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtIpPri.setStatus('current')
bfdSessExtIpGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtIpGateway.setStatus('current')
bfdSessExtAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 9), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtAdminState.setStatus('current')
bfdSessExtOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 10), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessExtOperationalState.setStatus('current')
bfdSessExtSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 11), SecondaryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessExtSecondaryState.setStatus('current')
bfdSessExtNegRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessExtNegRxInterval.setStatus('current')
bfdSessExtAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtAlias.setStatus('current')
bfdSessExtAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 14), BfdSessPerfAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtAction.setStatus('current')
bfdSessExtIpv6Gateway = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 15), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessExtIpv6Gateway.setStatus('current')
f3BfdIpIfMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2), )
if mibBuilder.loadTexts: f3BfdIpIfMemberTable.setStatus('current')
f3BfdIpIfMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1), ).setIndexNames((0, "BFD-STD-MIB", "bfdSessIndex"), (0, "F3-BFD-MIB", "f3BfdIpIfMemberObject"))
if mibBuilder.loadTexts: f3BfdIpIfMemberEntry.setStatus('current')
f3BfdIpIfMemberObject = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1, 1), VariablePointer())
if mibBuilder.loadTexts: f3BfdIpIfMemberObject.setStatus('current')
f3BfdIpIfMemberStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3BfdIpIfMemberStorageType.setStatus('current')
f3BfdIpIfMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3BfdIpIfMemberRowStatus.setStatus('current')
f3L3TrafficIPInterfaceExtBfdTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3), )
if mibBuilder.loadTexts: f3L3TrafficIPInterfaceExtBfdTable.setStatus('current')
f3L3TrafficIPInterfaceExtBfdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3, 1), )
f3L3TrafficIPInterfaceEntry.registerAugmentions(("F3-BFD-MIB", "f3L3TrafficIPInterfaceExtBfdEntry"))
f3L3TrafficIPInterfaceExtBfdEntry.setIndexNames(*f3L3TrafficIPInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: f3L3TrafficIPInterfaceExtBfdEntry.setStatus('current')
f3L3TrafficIPInterfaceExtBfdObject = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3, 1, 1), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3L3TrafficIPInterfaceExtBfdObject.setStatus('current')
f3L3TrafficIPInterfaceExtBfdDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3L3TrafficIPInterfaceExtBfdDesiredMinTxInterval.setStatus('current')
f3L3TrafficIPInterfaceExtBfdReqMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3L3TrafficIPInterfaceExtBfdReqMinRxInterval.setStatus('current')
f3L3TrafficIPInterfaceExtBfdLocalMultiplier = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3L3TrafficIPInterfaceExtBfdLocalMultiplier.setStatus('current')
f3VrfExtBfdConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 4), )
if mibBuilder.loadTexts: f3VrfExtBfdConfigTable.setStatus('current')
f3VrfExtBfdConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 4, 1), )
f3VrfEntry.registerAugmentions(("F3-BFD-MIB", "f3VrfExtBfdConfigEntry"))
f3VrfExtBfdConfigEntry.setIndexNames(*f3VrfEntry.getIndexNames())
if mibBuilder.loadTexts: f3VrfExtBfdConfigEntry.setStatus('current')
f3VrfExtBfdDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3VrfExtBfdDesiredMinTxInterval.setStatus('current')
f3VrfExtBfdReqMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3VrfExtBfdReqMinRxInterval.setStatus('current')
f3VrfExtBfdLocalMultiplier = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3VrfExtBfdLocalMultiplier.setStatus('current')
f3L3TrafficBgpPeerExtBfdConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 5), )
if mibBuilder.loadTexts: f3L3TrafficBgpPeerExtBfdConfigTable.setStatus('current')
f3L3TrafficBgpPeerExtBfdConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 5, 1), )
f3L3TrafficBgpPeerEntry.registerAugmentions(("F3-BFD-MIB", "f3L3TrafficBgpPeerExtBfdConfigEntry"))
f3L3TrafficBgpPeerExtBfdConfigEntry.setIndexNames(*f3L3TrafficBgpPeerEntry.getIndexNames())
if mibBuilder.loadTexts: f3L3TrafficBgpPeerExtBfdConfigEntry.setStatus('current')
f3L3TrafficBgpPeerBfdDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 5, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3L3TrafficBgpPeerBfdDetect.setStatus('current')
f3L3TrafficOspfInterfaceExtBfdConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 6), )
if mibBuilder.loadTexts: f3L3TrafficOspfInterfaceExtBfdConfigTable.setStatus('current')
f3L3TrafficOspfInterfaceExtBfdConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 6, 1), )
f3L3TrafficOspfInterfaceEntry.registerAugmentions(("F3-BFD-MIB", "f3L3TrafficOspfInterfaceExtBfdConfigEntry"))
f3L3TrafficOspfInterfaceExtBfdConfigEntry.setIndexNames(*f3L3TrafficOspfInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: f3L3TrafficOspfInterfaceExtBfdConfigEntry.setStatus('current')
f3L3TrafficOspfInterfaceBfdDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 6, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3L3TrafficOspfInterfaceBfdDetect.setStatus('current')
f3VrfBfdSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 7), )
if mibBuilder.loadTexts: f3VrfBfdSessionTable.setStatus('current')
f3VrfBfdSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 7, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-BFD-MIB", "f3VrfIndex"), (0, "F3-BFD-MIB", "f3VrfBfdSessionIpAddress"), (0, "F3-BFD-MIB", "f3VrfBfdSessionInterface"))
if mibBuilder.loadTexts: f3VrfBfdSessionEntry.setStatus('current')
f3VrfBfdSessionIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 7, 1, 1), DisplayString())
if mibBuilder.loadTexts: f3VrfBfdSessionIpAddress.setStatus('current')
f3VrfBfdSessionInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 7, 1, 2), DisplayString())
if mibBuilder.loadTexts: f3VrfBfdSessionInterface.setStatus('current')
f3VrfBfdSessionNegotiatedTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 7, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3VrfBfdSessionNegotiatedTxInterval.setStatus('current')
f3VrfBfdSessionNegotiatedDetectionTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 7, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3VrfBfdSessionNegotiatedDetectionTimer.setStatus('current')
f3VrfBfdSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 7, 1, 5), IANAbfdSessStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3VrfBfdSessionState.setStatus('current')
f3BfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 1))
f3BfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 2))
f3BfdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 1, 1)).setObjects(("F3-BFD-MIB", "f3BfdConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BfdCompliance = f3BfdCompliance.setStatus('current')
f3BfdConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 2, 1)).setObjects(("F3-BFD-MIB", "bfdSessExtInnerVlanControl"), ("F3-BFD-MIB", "bfdSessExtInnerVlanId"), ("F3-BFD-MIB", "bfdSessExtInnerVlanPri"), ("F3-BFD-MIB", "bfdSessExtOuterVlanControl"), ("F3-BFD-MIB", "bfdSessExtOuterVlanId"), ("F3-BFD-MIB", "bfdSessExtOuterVlanPri"), ("F3-BFD-MIB", "bfdSessExtIpPri"), ("F3-BFD-MIB", "bfdSessExtIpGateway"), ("F3-BFD-MIB", "bfdSessExtAdminState"), ("F3-BFD-MIB", "bfdSessExtOperationalState"), ("F3-BFD-MIB", "bfdSessExtSecondaryState"), ("F3-BFD-MIB", "bfdSessExtNegRxInterval"), ("F3-BFD-MIB", "bfdSessExtAlias"), ("F3-BFD-MIB", "bfdSessExtAction"), ("F3-BFD-MIB", "bfdSessExtIpv6Gateway"), ("F3-BFD-MIB", "f3BfdIpIfMemberObject"), ("F3-BFD-MIB", "f3BfdIpIfMemberStorageType"), ("F3-BFD-MIB", "f3BfdIpIfMemberRowStatus"), ("F3-BFD-MIB", "f3L3TrafficIPInterfaceExtBfdObject"), ("F3-BFD-MIB", "f3VrfExtBfdDesiredMinTxInterval"), ("F3-BFD-MIB", "f3VrfExtBfdReqMinRxInterval"), ("F3-BFD-MIB", "f3VrfExtBfdLocalMultiplier"), ("F3-BFD-MIB", "f3L3TrafficBgpPeerBfdDetect"), ("F3-BFD-MIB", "f3L3TrafficOspfInterfaceBfdDetect"), ("F3-BFD-MIB", "f3VrfBfdSessionIpAddress"), ("F3-BFD-MIB", "f3VrfBfdSessionInterface"), ("F3-BFD-MIB", "f3VrfBfdSessionNegotiatedTxInterval"), ("F3-BFD-MIB", "f3VrfBfdSessionNegotiatedDetectionTimer"), ("F3-BFD-MIB", "f3VrfBfdSessionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BfdConfigGroup = f3BfdConfigGroup.setStatus('current')
mibBuilder.exportSymbols("F3-BFD-MIB", f3L3TrafficIPInterfaceExtBfdReqMinRxInterval=f3L3TrafficIPInterfaceExtBfdReqMinRxInterval, f3VrfBfdSessionEntry=f3VrfBfdSessionEntry, f3L3TrafficIPInterfaceExtBfdObject=f3L3TrafficIPInterfaceExtBfdObject, bfdSessExtOperationalState=bfdSessExtOperationalState, bfdSessExtEntry=bfdSessExtEntry, bfdSessExtInnerVlanControl=bfdSessExtInnerVlanControl, f3L3TrafficIPInterfaceExtBfdDesiredMinTxInterval=f3L3TrafficIPInterfaceExtBfdDesiredMinTxInterval, bfdSessExtOuterVlanPri=bfdSessExtOuterVlanPri, f3BfdGroups=f3BfdGroups, f3L3TrafficIPInterfaceExtBfdTable=f3L3TrafficIPInterfaceExtBfdTable, f3L3TrafficOspfInterfaceExtBfdConfigTable=f3L3TrafficOspfInterfaceExtBfdConfigTable, bfdSessExtAlias=bfdSessExtAlias, bfdSessExtOuterVlanId=bfdSessExtOuterVlanId, bfdSessExtInnerVlanId=bfdSessExtInnerVlanId, bfdSessExtTable=bfdSessExtTable, f3BfdMIB=f3BfdMIB, f3BfdIpIfMemberStorageType=f3BfdIpIfMemberStorageType, f3L3TrafficOspfInterfaceBfdDetect=f3L3TrafficOspfInterfaceBfdDetect, bfdSessExtSecondaryState=bfdSessExtSecondaryState, f3BfdCompliance=f3BfdCompliance, f3BfdCompliances=f3BfdCompliances, f3L3TrafficBgpPeerBfdDetect=f3L3TrafficBgpPeerBfdDetect, f3BfdConfigGroup=f3BfdConfigGroup, bfdSessExtInnerVlanPri=bfdSessExtInnerVlanPri, bfdSessExtOuterVlanControl=bfdSessExtOuterVlanControl, bfdSessExtIpGateway=bfdSessExtIpGateway, f3VrfExtBfdReqMinRxInterval=f3VrfExtBfdReqMinRxInterval, bfdSessExtIpv6Gateway=bfdSessExtIpv6Gateway, f3BfdIpIfMemberEntry=f3BfdIpIfMemberEntry, bfdSessExtAction=bfdSessExtAction, f3BfdIpIfMemberObject=f3BfdIpIfMemberObject, f3L3TrafficBgpPeerExtBfdConfigTable=f3L3TrafficBgpPeerExtBfdConfigTable, f3L3TrafficIPInterfaceExtBfdEntry=f3L3TrafficIPInterfaceExtBfdEntry, bfdSessExtAdminState=bfdSessExtAdminState, f3L3TrafficBgpPeerExtBfdConfigEntry=f3L3TrafficBgpPeerExtBfdConfigEntry, PYSNMP_MODULE_ID=f3BfdMIB, bfdSessExtNegRxInterval=bfdSessExtNegRxInterval, f3L3TrafficOspfInterfaceExtBfdConfigEntry=f3L3TrafficOspfInterfaceExtBfdConfigEntry, bfdSessExtIpPri=bfdSessExtIpPri, f3VrfExtBfdConfigEntry=f3VrfExtBfdConfigEntry, f3VrfBfdSessionTable=f3VrfBfdSessionTable, f3VrfExtBfdLocalMultiplier=f3VrfExtBfdLocalMultiplier, f3VrfBfdSessionNegotiatedTxInterval=f3VrfBfdSessionNegotiatedTxInterval, f3VrfExtBfdConfigTable=f3VrfExtBfdConfigTable, f3VrfBfdSessionState=f3VrfBfdSessionState, f3VrfExtBfdDesiredMinTxInterval=f3VrfExtBfdDesiredMinTxInterval, f3BfdIpIfMemberRowStatus=f3BfdIpIfMemberRowStatus, f3BfdIpIfMemberTable=f3BfdIpIfMemberTable, f3VrfBfdSessionInterface=f3VrfBfdSessionInterface, BfdSessPerfAction=BfdSessPerfAction, f3L3TrafficIPInterfaceExtBfdLocalMultiplier=f3L3TrafficIPInterfaceExtBfdLocalMultiplier, f3VrfBfdSessionIpAddress=f3VrfBfdSessionIpAddress, f3VrfBfdSessionNegotiatedDetectionTimer=f3VrfBfdSessionNegotiatedDetectionTimer, f3BfdConfigObjects=f3BfdConfigObjects, f3BfdConformance=f3BfdConformance)
