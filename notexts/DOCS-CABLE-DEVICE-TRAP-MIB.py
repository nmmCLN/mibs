#
# PySNMP MIB module DOCS-CABLE-DEVICE-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/DOCS-CABLE-DEVICE-TRAP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:05 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
docsDev, docsDevEvLevel, docsDevNotification, docsDevServerTime, docsDevServerDhcp, docsDevSwServer, docsDevSwFilename, docsDevEvText, docsDevEvId = mibBuilder.importSymbols("DOCS-CABLE-DEVICE-MIB", "docsDev", "docsDevEvLevel", "docsDevNotification", "docsDevServerTime", "docsDevServerDhcp", "docsDevSwServer", "docsDevSwFilename", "docsDevEvText", "docsDevEvId")
docsIfDocsisOperMode, docsIfCmtsCmStatusDocsisMode, docsIfDocsisCapability = mibBuilder.importSymbols("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode", "docsIfCmtsCmStatusDocsisMode", "docsIfDocsisCapability")
docsIfCmCmtsAddress, docsIfDocsisBaseCapability, docsIfCmtsCmStatusDocsisRegMode, docsIfCmStatusModulationType, docsIfCmtsCmStatusModulationType, docsIfCmtsCmStatusMacAddress, docsIfCmStatusDocsisOperMode = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmCmtsAddress", "docsIfDocsisBaseCapability", "docsIfCmtsCmStatusDocsisRegMode", "docsIfCmStatusModulationType", "docsIfCmtsCmStatusModulationType", "docsIfCmtsCmStatusMacAddress", "docsIfCmStatusDocsisOperMode")
ifPhysAddress, = mibBuilder.importSymbols("IF-MIB", "ifPhysAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Unsigned32, NotificationType, Counter64, Integer32, TimeTicks, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Unsigned32", "NotificationType", "Counter64", "Integer32", "TimeTicks", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
docsDevTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 69, 10))
docsDevTrapMIB.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: docsDevTrapMIB.setLastUpdated('0202250000Z')
if mibBuilder.loadTexts: docsDevTrapMIB.setOrganization('Cisco Systems, Inc.')
docsDevTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1))
docsDevTrapControl = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 1))
docsDevCmTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0))
docsDevCmtsTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0))
docsDevCmTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 69, 2, 1, 1, 1), Bits().clone(namedValues=NamedValues(("cmInitTLVUnknownTrap", 0), ("cmDynServReqFailTrap", 1), ("cmDynServRspFailTrap", 2), ("cmDynServAckFailTrap", 3), ("cmBpiInitTrap", 4), ("cmBPKMTrap", 5), ("cmDynamicSATrap", 6), ("cmDHCPFailTrap", 7), ("cmSwUpgradeInitTrap", 8), ("cmSwUpgradeFailTrap", 9), ("cmSwUpgradeSuccessTrap", 10), ("cmSwUpgradeCVCTrap", 11), ("cmTODFailTrap", 12), ("cmDCCReqFailTrap", 13), ("cmDCCRspFailTrap", 14), ("cmDCCAckFailTrap", 15))).clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsDevCmTrapControl.setStatus('current')
docsDevCmtsTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 69, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("cmtsInitRegReqFailTrap", 0), ("cmtsInitRegRspFailTrap", 1), ("cmtsInitRegAckFailTrap", 2), ("cmtsDynServReqFailTrap", 3), ("cmtsDynServRspFailTrap", 4), ("cmtsDynServAckFailTrap", 5), ("cmtsBpiInitTrap", 6), ("cmtsBPKMTrap", 7), ("cmtsDynamicSATrap", 8), ("cmtsDCCReqFailTrap", 9), ("cmtsDCCRspFailTrap", 10), ("cmtsDCCAckFailTrap", 11))).clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsDevCmtsTrapControl.setStatus('current')
docsDevCmInitTLVUnknownTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 1)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmInitTLVUnknownTrap.setStatus('current')
docsDevCmDynServReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 2)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDynServReqFailTrap.setStatus('current')
docsDevCmDynServRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 3)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDynServRspFailTrap.setStatus('current')
docsDevCmDynServAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 4)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDynServAckFailTrap.setStatus('current')
docsDevCmBpiInitTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 5)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmBpiInitTrap.setStatus('current')
docsDevCmBPKMTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 6)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmBPKMTrap.setStatus('current')
docsDevCmDynamicSATrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 7)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDynamicSATrap.setStatus('current')
docsDevCmDHCPFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 8)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcp"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDHCPFailTrap.setStatus('current')
docsDevCmSwUpgradeInitTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 9)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeInitTrap.setStatus('current')
docsDevCmSwUpgradeFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 10)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeFailTrap.setStatus('current')
docsDevCmSwUpgradeSuccessTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 11)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeSuccessTrap.setStatus('current')
docsDevCmSwUpgradeCVCFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 12)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeCVCFailTrap.setStatus('current')
docsDevCmTODFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 13)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTime"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmTODFailTrap.setStatus('current')
docsDevCmDCCReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 14)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDCCReqFailTrap.setStatus('current')
docsDevCmDCCRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 15)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDCCRspFailTrap.setStatus('current')
docsDevCmDCCAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 16)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"), ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmDCCAckFailTrap.setStatus('current')
docsDevCmtsInitRegReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 1)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsInitRegReqFailTrap.setStatus('current')
docsDevCmtsInitRegRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 2)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsInitRegRspFailTrap.setStatus('current')
docsDevCmtsInitRegAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 3)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsInitRegAckFailTrap.setStatus('current')
docsDevCmtsDynServReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 4)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsDynServReqFailTrap.setStatus('current')
docsDevCmtsDynServRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 5)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsDynServRspFailTrap.setStatus('current')
docsDevCmtsDynServAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 6)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsDynServAckFailTrap.setStatus('current')
docsDevCmtsBpiInitTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 7)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsBpiInitTrap.setStatus('current')
docsDevCmtsBPKMTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 8)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsBPKMTrap.setStatus('current')
docsDevCmtsDynamicSATrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 9)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsDynamicSATrap.setStatus('current')
docsDevCmtsDCCReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 10)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsDCCReqFailTrap.setStatus('current')
docsDevCmtsDCCRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 11)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsDCCRspFailTrap.setStatus('current')
docsDevCmtsDCCAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 12)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"), ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
if mibBuilder.loadTexts: docsDevCmtsDCCAckFailTrap.setStatus('current')
docsDevTrapConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 4))
docsDevTrapGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 1))
docsDevTrapCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 2))
docsDevCmTrapCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 2, 1)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTrapControlGroup"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmTrapCompliance = docsDevCmTrapCompliance.setStatus('current')
docsDevCmTrapControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 1, 1)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTrapControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmTrapControlGroup = docsDevCmTrapControlGroup.setStatus('current')
docsDevCmNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 1, 2)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmInitTLVUnknownTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServAckFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmBpiInitTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmBPKMTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynamicSATrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDHCPFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeInitTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeSuccessTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeCVCFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTODFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCAckFailTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmNotificationGroup = docsDevCmNotificationGroup.setStatus('current')
docsDevCmtsTrapCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 2, 2)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsTrapControlGroup"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmtsTrapCompliance = docsDevCmtsTrapCompliance.setStatus('current')
docsDevCmtsTrapControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 1, 3)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsTrapControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmtsTrapControlGroup = docsDevCmtsTrapControlGroup.setStatus('current')
docsDevCmtsNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 4, 1, 4)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegAckFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServAckFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsBpiInitTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsBPKMTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynamicSATrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCAckFailTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmtsNotificationGroup = docsDevCmtsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DOCS-CABLE-DEVICE-TRAP-MIB", docsDevCmtsDynamicSATrap=docsDevCmtsDynamicSATrap, docsDevCmtsDCCAckFailTrap=docsDevCmtsDCCAckFailTrap, docsDevCmtsDynServRspFailTrap=docsDevCmtsDynServRspFailTrap, docsDevCmTrapControlGroup=docsDevCmTrapControlGroup, PYSNMP_MODULE_ID=docsDevTrapMIB, docsDevCmDCCRspFailTrap=docsDevCmDCCRspFailTrap, docsDevCmtsDCCReqFailTrap=docsDevCmtsDCCReqFailTrap, docsDevCmtsTrapControl=docsDevCmtsTrapControl, docsDevCmBPKMTrap=docsDevCmBPKMTrap, docsDevCmtsBpiInitTrap=docsDevCmtsBpiInitTrap, docsDevTraps=docsDevTraps, docsDevCmtsInitRegRspFailTrap=docsDevCmtsInitRegRspFailTrap, docsDevCmDynamicSATrap=docsDevCmDynamicSATrap, docsDevCmTODFailTrap=docsDevCmTODFailTrap, docsDevCmtsTrapCompliance=docsDevCmtsTrapCompliance, docsDevCmtsTrapControlGroup=docsDevCmtsTrapControlGroup, docsDevCmtsNotificationGroup=docsDevCmtsNotificationGroup, docsDevCmtsDCCRspFailTrap=docsDevCmtsDCCRspFailTrap, docsDevTrapCompliances=docsDevTrapCompliances, docsDevCmSwUpgradeInitTrap=docsDevCmSwUpgradeInitTrap, docsDevCmDCCAckFailTrap=docsDevCmDCCAckFailTrap, docsDevCmSwUpgradeSuccessTrap=docsDevCmSwUpgradeSuccessTrap, docsDevTrapControl=docsDevTrapControl, docsDevCmtsInitRegReqFailTrap=docsDevCmtsInitRegReqFailTrap, docsDevCmDHCPFailTrap=docsDevCmDHCPFailTrap, docsDevCmDCCReqFailTrap=docsDevCmDCCReqFailTrap, docsDevTrapGroups=docsDevTrapGroups, docsDevCmDynServAckFailTrap=docsDevCmDynServAckFailTrap, docsDevCmTrapCompliance=docsDevCmTrapCompliance, docsDevCmtsDynServReqFailTrap=docsDevCmtsDynServReqFailTrap, docsDevTrapConformance=docsDevTrapConformance, docsDevCmDynServRspFailTrap=docsDevCmDynServRspFailTrap, docsDevCmTraps=docsDevCmTraps, docsDevCmtsDynServAckFailTrap=docsDevCmtsDynServAckFailTrap, docsDevTrapMIB=docsDevTrapMIB, docsDevCmInitTLVUnknownTrap=docsDevCmInitTLVUnknownTrap, docsDevCmBpiInitTrap=docsDevCmBpiInitTrap, docsDevCmSwUpgradeCVCFailTrap=docsDevCmSwUpgradeCVCFailTrap, docsDevCmtsInitRegAckFailTrap=docsDevCmtsInitRegAckFailTrap, docsDevCmNotificationGroup=docsDevCmNotificationGroup, docsDevCmtsBPKMTrap=docsDevCmtsBPKMTrap, docsDevCmSwUpgradeFailTrap=docsDevCmSwUpgradeFailTrap, docsDevCmtsTraps=docsDevCmtsTraps, docsDevCmDynServReqFailTrap=docsDevCmDynServReqFailTrap, docsDevCmTrapControl=docsDevCmTrapControl)
