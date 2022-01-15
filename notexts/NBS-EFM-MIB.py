#
# PySNMP MIB module NBS-EFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-EFM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:28:03 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, Unsigned16TC = mibBuilder.importSymbols("NBS-MIB", "nbs", "Unsigned16TC")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Gauge32, Counter64, TimeTicks, Counter32, ModuleIdentity, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, ObjectIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsEfmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 300))
if mibBuilder.loadTexts: nbsEfmMib.setLastUpdated('201610190000Z')
if mibBuilder.loadTexts: nbsEfmMib.setOrganization('NBS')
nbsEfmProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 300, 2))
nbsEfmNc316Nm = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 300, 2, 1))
nbsEfmObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 300, 1))
if mibBuilder.loadTexts: nbsEfmObjects.setStatus('current')
nbsEfmOamGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 300, 1, 3))
if mibBuilder.loadTexts: nbsEfmOamGrp.setStatus('current')
nbsEfmOamTable = MibTable((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1), )
if mibBuilder.loadTexts: nbsEfmOamTable.setStatus('current')
nbsEfmOamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1), ).setIndexNames((0, "NBS-EFM-MIB", "nbsEfmPhysicalIfIndex"))
if mibBuilder.loadTexts: nbsEfmOamEntry.setStatus('current')
nbsEfmPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmPhysicalIfIndex.setStatus('current')
nbsEfmOamIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamIfIndex.setStatus('current')
nbsEfmOamPeerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamPeerIfIndex.setStatus('current')
nbsEfmOamMode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("passive", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamMode.setStatus('current')
nbsEfmOamCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamCfg.setStatus('current')
nbsEfmOamPduCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 6), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamPduCfg.setStatus('current')
nbsEfmOamFlagsField = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamFlagsField.setStatus('current')
nbsEfmOamState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamState.setStatus('current')
nbsEfmOamVendorOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamVendorOUI.setStatus('current')
nbsEfmOamVendorDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 10), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamVendorDeviceId.setStatus('current')
nbsEfmOamVendorDeviceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 11), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamVendorDeviceVersion.setStatus('current')
nbsEfmOamPDUTx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamPDUTx.setStatus('current')
nbsEfmOamPDURx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamPDURx.setStatus('current')
nbsEfmOamUnsupportedCodesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamUnsupportedCodesRx.setStatus('current')
nbsEfmOamInformationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamInformationTx.setStatus('current')
nbsEfmOamInformationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamInformationRx.setStatus('current')
nbsEfmOamEventNotificationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamEventNotificationTx.setStatus('current')
nbsEfmOamUniEventNotificationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamUniEventNotificationRx.setStatus('current')
nbsEfmOamDupEventNotificationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamDupEventNotificationRx.setStatus('current')
nbsEfmOamLoopbackControlTx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamLoopbackControlTx.setStatus('current')
nbsEfmOamLoopbackControlRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamLoopbackControlRx.setStatus('current')
nbsEfmOamVariableRequestTx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamVariableRequestTx.setStatus('current')
nbsEfmOamVariableRequestRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamVariableRequestRx.setStatus('current')
nbsEfmOamVariableResponseTx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamVariableResponseTx.setStatus('current')
nbsEfmOamVariableResponseRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamVariableResponseRx.setStatus('current')
nbsEfmOamOrganizationSpecificTx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamOrganizationSpecificTx.setStatus('current')
nbsEfmOamOrganizationSpecificRx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamOrganizationSpecificRx.setStatus('current')
nbsEfmOamErrSymPerCfgDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrSymPerCfgDuration.setStatus('current')
nbsEfmOamErrSymPerCfgThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrSymPerCfgThreshld.setStatus('current')
nbsEfmOamErrSymPerEvtTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 30), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrSymPerEvtTime.setStatus('current')
nbsEfmOamErrSymPerEvtWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrSymPerEvtWindow.setStatus('current')
nbsEfmOamErrSymPerEvtThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrSymPerEvtThreshld.setStatus('current')
nbsEfmOamErrSymPerEvtCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrSymPerEvtCount.setStatus('current')
nbsEfmOamErrFrmCfgDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmCfgDuration.setStatus('current')
nbsEfmOamErrFrmCfgThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmCfgThreshld.setStatus('current')
nbsEfmOamErrFrmEvtTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 36), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmEvtTime.setStatus('current')
nbsEfmOamErrFrmEvtWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 37), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmEvtWindow.setStatus('current')
nbsEfmOamErrFrmEvtThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmEvtThreshld.setStatus('current')
nbsEfmOamErrFrmEvtCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmEvtCount.setStatus('current')
nbsEfmOamErrFrmPerCfgDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmPerCfgDuration.setStatus('current')
nbsEfmOamErrFrmPerCfgThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmPerCfgThreshld.setStatus('current')
nbsEfmOamErrFrmPerEvtTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 42), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmPerEvtTime.setStatus('current')
nbsEfmOamErrFrmPerEvtWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmPerEvtWindow.setStatus('current')
nbsEfmOamErrFrmPerEvtThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmPerEvtThreshld.setStatus('current')
nbsEfmOamErrFrmPerEvtCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmPerEvtCount.setStatus('current')
nbsEfmOamErrFrmSecSumCfgDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 46), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmSecSumCfgDuration.setStatus('current')
nbsEfmOamErrFrmSecSumCfgThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 47), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmSecSumCfgThreshld.setStatus('current')
nbsEfmOamErrFrmSecSumEvtTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 48), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmSecSumEvtTime.setStatus('current')
nbsEfmOamErrFrmSecSumEvtWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 49), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmSecSumEvtWindow.setStatus('current')
nbsEfmOamErrFrmSecSumEvtThreshld = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 50), Unsigned16TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmSecSumEvtThreshld.setStatus('current')
nbsEfmOamErrFrmSecSumEvtCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamErrFrmSecSumEvtCount.setStatus('current')
nbsEfmOamFramesLostDueToOamError = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamFramesLostDueToOamError.setStatus('current')
nbsEfmOamAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 53), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("disable", 2), ("enable", 3))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsEfmOamAdminState.setStatus('current')
nbsEfmOamOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 54), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsEfmOamOperState.setStatus('current')
nbsEfmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 300, 3))
nbsEfmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 300, 3, 1))
nbsEfmOamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 300, 3, 1, 3)).setObjects(("NBS-EFM-MIB", "nbsEfmPhysicalIfIndex"), ("NBS-EFM-MIB", "nbsEfmOamIfIndex"), ("NBS-EFM-MIB", "nbsEfmOamPeerIfIndex"), ("NBS-EFM-MIB", "nbsEfmOamMode"), ("NBS-EFM-MIB", "nbsEfmOamCfg"), ("NBS-EFM-MIB", "nbsEfmOamPduCfg"), ("NBS-EFM-MIB", "nbsEfmOamFlagsField"), ("NBS-EFM-MIB", "nbsEfmOamState"), ("NBS-EFM-MIB", "nbsEfmOamVendorOUI"), ("NBS-EFM-MIB", "nbsEfmOamVendorDeviceId"), ("NBS-EFM-MIB", "nbsEfmOamVendorDeviceVersion"), ("NBS-EFM-MIB", "nbsEfmOamPDUTx"), ("NBS-EFM-MIB", "nbsEfmOamPDURx"), ("NBS-EFM-MIB", "nbsEfmOamUnsupportedCodesRx"), ("NBS-EFM-MIB", "nbsEfmOamInformationTx"), ("NBS-EFM-MIB", "nbsEfmOamInformationRx"), ("NBS-EFM-MIB", "nbsEfmOamEventNotificationTx"), ("NBS-EFM-MIB", "nbsEfmOamUniEventNotificationRx"), ("NBS-EFM-MIB", "nbsEfmOamDupEventNotificationRx"), ("NBS-EFM-MIB", "nbsEfmOamLoopbackControlTx"), ("NBS-EFM-MIB", "nbsEfmOamLoopbackControlRx"), ("NBS-EFM-MIB", "nbsEfmOamVariableRequestTx"), ("NBS-EFM-MIB", "nbsEfmOamVariableRequestRx"), ("NBS-EFM-MIB", "nbsEfmOamVariableResponseTx"), ("NBS-EFM-MIB", "nbsEfmOamVariableResponseRx"), ("NBS-EFM-MIB", "nbsEfmOamOrganizationSpecificTx"), ("NBS-EFM-MIB", "nbsEfmOamOrganizationSpecificRx"), ("NBS-EFM-MIB", "nbsEfmOamErrSymPerCfgDuration"), ("NBS-EFM-MIB", "nbsEfmOamErrSymPerCfgThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtTime"), ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtWindow"), ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtCount"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmCfgDuration"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmCfgThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtTime"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtWindow"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtCount"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerCfgDuration"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerCfgThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtTime"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtWindow"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtCount"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumCfgDuration"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumCfgThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtTime"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtWindow"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtThreshld"), ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtCount"), ("NBS-EFM-MIB", "nbsEfmOamFramesLostDueToOamError"), ("NBS-EFM-MIB", "nbsEfmOamAdminState"), ("NBS-EFM-MIB", "nbsEfmOamOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nbsEfmOamGroup = nbsEfmOamGroup.setStatus('current')
mibBuilder.exportSymbols("NBS-EFM-MIB", nbsEfmOamState=nbsEfmOamState, nbsEfmOamLoopbackControlTx=nbsEfmOamLoopbackControlTx, nbsEfmOamFramesLostDueToOamError=nbsEfmOamFramesLostDueToOamError, nbsEfmOamVendorDeviceVersion=nbsEfmOamVendorDeviceVersion, nbsEfmOamErrFrmEvtCount=nbsEfmOamErrFrmEvtCount, nbsEfmOamErrFrmPerCfgThreshld=nbsEfmOamErrFrmPerCfgThreshld, nbsEfmOamErrFrmSecSumCfgDuration=nbsEfmOamErrFrmSecSumCfgDuration, nbsEfmOamUniEventNotificationRx=nbsEfmOamUniEventNotificationRx, nbsEfmOamErrFrmSecSumEvtWindow=nbsEfmOamErrFrmSecSumEvtWindow, PYSNMP_MODULE_ID=nbsEfmMib, nbsEfmOamVendorDeviceId=nbsEfmOamVendorDeviceId, nbsEfmOamErrFrmCfgThreshld=nbsEfmOamErrFrmCfgThreshld, nbsEfmOamInformationTx=nbsEfmOamInformationTx, nbsEfmOamErrFrmEvtThreshld=nbsEfmOamErrFrmEvtThreshld, nbsEfmOamErrFrmPerCfgDuration=nbsEfmOamErrFrmPerCfgDuration, nbsEfmOamErrSymPerEvtCount=nbsEfmOamErrSymPerEvtCount, nbsEfmOamCfg=nbsEfmOamCfg, nbsEfmMib=nbsEfmMib, nbsEfmOamMode=nbsEfmOamMode, nbsEfmOamFlagsField=nbsEfmOamFlagsField, nbsEfmObjects=nbsEfmObjects, nbsEfmOamErrSymPerEvtThreshld=nbsEfmOamErrSymPerEvtThreshld, nbsEfmOamVendorOUI=nbsEfmOamVendorOUI, nbsEfmOamInformationRx=nbsEfmOamInformationRx, nbsEfmOamGroup=nbsEfmOamGroup, nbsEfmOamLoopbackControlRx=nbsEfmOamLoopbackControlRx, nbsEfmOamVariableRequestTx=nbsEfmOamVariableRequestTx, nbsEfmOamErrFrmSecSumEvtTime=nbsEfmOamErrFrmSecSumEvtTime, nbsEfmOamErrFrmSecSumEvtCount=nbsEfmOamErrFrmSecSumEvtCount, nbsEfmProduct=nbsEfmProduct, nbsEfmOamVariableRequestRx=nbsEfmOamVariableRequestRx, nbsEfmOamErrFrmEvtWindow=nbsEfmOamErrFrmEvtWindow, nbsEfmGroups=nbsEfmGroups, nbsEfmOamPduCfg=nbsEfmOamPduCfg, nbsEfmOamTable=nbsEfmOamTable, nbsEfmOamIfIndex=nbsEfmOamIfIndex, nbsEfmOamErrFrmPerEvtThreshld=nbsEfmOamErrFrmPerEvtThreshld, nbsEfmOamGrp=nbsEfmOamGrp, nbsEfmOamErrSymPerCfgDuration=nbsEfmOamErrSymPerCfgDuration, nbsEfmOamUnsupportedCodesRx=nbsEfmOamUnsupportedCodesRx, nbsEfmOamErrFrmSecSumCfgThreshld=nbsEfmOamErrFrmSecSumCfgThreshld, nbsEfmOamOrganizationSpecificTx=nbsEfmOamOrganizationSpecificTx, nbsEfmOamErrFrmSecSumEvtThreshld=nbsEfmOamErrFrmSecSumEvtThreshld, nbsEfmOamVariableResponseRx=nbsEfmOamVariableResponseRx, nbsEfmOamErrSymPerCfgThreshld=nbsEfmOamErrSymPerCfgThreshld, nbsEfmOamOperState=nbsEfmOamOperState, nbsEfmOamEntry=nbsEfmOamEntry, nbsEfmOamDupEventNotificationRx=nbsEfmOamDupEventNotificationRx, nbsEfmOamVariableResponseTx=nbsEfmOamVariableResponseTx, nbsEfmOamErrSymPerEvtTime=nbsEfmOamErrSymPerEvtTime, nbsEfmOamErrFrmEvtTime=nbsEfmOamErrFrmEvtTime, nbsEfmOamErrFrmPerEvtWindow=nbsEfmOamErrFrmPerEvtWindow, nbsEfmOamPeerIfIndex=nbsEfmOamPeerIfIndex, nbsEfmOamEventNotificationTx=nbsEfmOamEventNotificationTx, nbsEfmOamPDUTx=nbsEfmOamPDUTx, nbsEfmNc316Nm=nbsEfmNc316Nm, nbsEfmOamErrFrmPerEvtTime=nbsEfmOamErrFrmPerEvtTime, nbsEfmOamErrFrmCfgDuration=nbsEfmOamErrFrmCfgDuration, nbsEfmOamAdminState=nbsEfmOamAdminState, nbsEfmConformance=nbsEfmConformance, nbsEfmOamOrganizationSpecificRx=nbsEfmOamOrganizationSpecificRx, nbsEfmOamPDURx=nbsEfmOamPDURx, nbsEfmOamErrFrmPerEvtCount=nbsEfmOamErrFrmPerEvtCount, nbsEfmOamErrSymPerEvtWindow=nbsEfmOamErrSymPerEvtWindow, nbsEfmPhysicalIfIndex=nbsEfmPhysicalIfIndex)
