#
# PySNMP MIB module CTRON-SMARTTRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SMARTTRUNK-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ctSmartTrunkBranch, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctSmartTrunkBranch")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
ctSmartTrunk = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1))
if mibBuilder.loadTexts: ctSmartTrunk.setLastUpdated('199812160000Z')
if mibBuilder.loadTexts: ctSmartTrunk.setOrganization('Cabletron Systems, Inc')
ctSmartTrunkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1))
ctSmartTrunkDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2))
class CTSmartTrunkProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noProtocol", 1), ("decHuntGroup", 2))

class CTSmartTrunkIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CTSmartTrunkName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class CTSmartTrunkLoadBalanceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("balancingUnspecified", 1), ("roundRobin", 2), ("linkUtilization", 3))

ctTrunkGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTrunkGlobalStatus.setStatus('current')
ctTrunkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3), )
if mibBuilder.loadTexts: ctTrunkConfigTable.setStatus('current')
ctTrunkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1), ).setIndexNames((0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"))
if mibBuilder.loadTexts: ctTrunkConfigEntry.setStatus('current')
ctTrunkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 1), CTSmartTrunkIndex())
if mibBuilder.loadTexts: ctTrunkIndex.setStatus('current')
ctTrunkConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 2), CTSmartTrunkName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigName.setStatus('current')
ctTrunkConfigProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 3), CTSmartTrunkProtocol().clone('decHuntGroup')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigProtocol.setStatus('current')
ctTrunkConfigLoadBalance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 4), CTSmartTrunkLoadBalanceType().clone('balancingUnspecified')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigLoadBalance.setStatus('current')
ctTrunkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkIfIndex.setStatus('current')
ctTrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkRowStatus.setStatus('current')
ctTrunkConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4), )
if mibBuilder.loadTexts: ctTrunkConnectionTable.setStatus('current')
ctTrunkConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTrunkConnectionEntry.setStatus('current')
ctTrunkPortRemoteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkPortRemoteIfIndex.setStatus('current')
ctTrunkLLAPRequirement = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("required", 1), ("notRequired", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkLLAPRequirement.setStatus('current')
ctTrunkMaxTrunks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkMaxTrunks.setStatus('current')
ctTrunkFlowDiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4), )
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticTable.setStatus('current')
ctTrunkFlowDiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1), ).setIndexNames((0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticEntry.setStatus('current')
ctTrunkFlowDiagnosticInstalledFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticInstalledFlows.setStatus('current')
ctTrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3))
ctTrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1))
ctTrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2))
ctTrunkComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1, 1)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkConfGroupV10"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkFlowDiagnosticGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkComplianceV10 = ctTrunkComplianceV10.setStatus('current')
ctTrunkConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 1)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkGlobalStatus"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkRowStatus"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigName"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigProtocol"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigLoadBalance"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkIfIndex"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkPortRemoteIfIndex"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkLLAPRequirement"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkMaxTrunks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkConfGroupV10 = ctTrunkConfGroupV10.setStatus('current')
ctTrunkFlowDiagnosticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 2)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkFlowDiagnosticInstalledFlows"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkFlowDiagnosticGroup = ctTrunkFlowDiagnosticGroup.setStatus('current')
mibBuilder.exportSymbols("CTRON-SMARTTRUNK-MIB", CTSmartTrunkLoadBalanceType=CTSmartTrunkLoadBalanceType, ctTrunkFlowDiagnosticTable=ctTrunkFlowDiagnosticTable, ctTrunkFlowDiagnosticGroup=ctTrunkFlowDiagnosticGroup, ctTrunkConfigTable=ctTrunkConfigTable, ctTrunkConfigName=ctTrunkConfigName, ctTrunkIndex=ctTrunkIndex, ctTrunkConfGroupV10=ctTrunkConfGroupV10, ctTrunkRowStatus=ctTrunkRowStatus, ctTrunkGroups=ctTrunkGroups, ctTrunkComplianceV10=ctTrunkComplianceV10, ctTrunkConnectionEntry=ctTrunkConnectionEntry, ctTrunkConfigLoadBalance=ctTrunkConfigLoadBalance, ctSmartTrunk=ctSmartTrunk, ctTrunkFlowDiagnosticInstalledFlows=ctTrunkFlowDiagnosticInstalledFlows, ctSmartTrunkDebug=ctSmartTrunkDebug, ctSmartTrunkConfig=ctSmartTrunkConfig, CTSmartTrunkIndex=CTSmartTrunkIndex, ctTrunkFlowDiagnosticEntry=ctTrunkFlowDiagnosticEntry, CTSmartTrunkProtocol=CTSmartTrunkProtocol, ctTrunkPortRemoteIfIndex=ctTrunkPortRemoteIfIndex, ctTrunkGlobalStatus=ctTrunkGlobalStatus, ctTrunkConfigProtocol=ctTrunkConfigProtocol, ctTrunkConformance=ctTrunkConformance, ctTrunkIfIndex=ctTrunkIfIndex, ctTrunkConnectionTable=ctTrunkConnectionTable, ctTrunkCompliances=ctTrunkCompliances, PYSNMP_MODULE_ID=ctSmartTrunk, ctTrunkLLAPRequirement=ctTrunkLLAPRequirement, CTSmartTrunkName=CTSmartTrunkName, ctTrunkMaxTrunks=ctTrunkMaxTrunks, ctTrunkConfigEntry=ctTrunkConfigEntry)
