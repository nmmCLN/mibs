#
# PySNMP MIB module IEEE8021-FQTSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-FQTSS-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:08 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
BridgeId, = mibBuilder.importSymbols("BRIDGE-MIB", "BridgeId")
ieee8021BridgeBaseEntry, ieee8021BridgeBasePortEntry, ieee8021BridgeBaseComponentId, ieee8021BridgeBasePort = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseEntry", "ieee8021BridgeBasePortEntry", "ieee8021BridgeBaseComponentId", "ieee8021BridgeBasePort")
ieee802dot1mibs, IEEE8021PriorityValue = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs", "IEEE8021PriorityValue")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Unsigned32, Counter64, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, Counter32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "Counter32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
ieee8021FqtssMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 16))
ieee8021FqtssMib.setRevisions(('2018-10-04 00:00', '2018-06-28 00:00', '2015-12-02 00:00', '2014-12-15 00:00', '2011-02-27 00:00', '2009-10-01 00:00',))
if mibBuilder.loadTexts: ieee8021FqtssMib.setLastUpdated('201810040000Z')
if mibBuilder.loadTexts: ieee8021FqtssMib.setOrganization('IEEE 802.1 Working Group')
class IEEE8021FqtssTrafficClassValue(TextualConvention, Unsigned32):
    reference = '12.20.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021FqtssDeltaBandwidthValue(TextualConvention, Unsigned32):
    reference = '12.20.1, 34.4'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000000)

class IEEE8021FqtssTxSelectionAlgorithmIDValue(TextualConvention, Unsigned32):
    reference = '8.6.8, 12.20.2'
    status = 'current'
    displayHint = 'd'

ieee8021FqtssNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 0))
ieee8021FqtssObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1))
ieee8021FqtssConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2))
ieee8021FqtssBap = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 1))
ieee8021FqtssMappings = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 2))
ieee8021FqtssBapX = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 3))
ieee8021FqtssBapTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021FqtssBapTable.setStatus('current')
ieee8021FqtssBapEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPTrafficClass"))
if mibBuilder.loadTexts: ieee8021FqtssBapEntry.setStatus('current')
ieee8021FqtssBAPTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 1), IEEE8021FqtssTrafficClassValue())
if mibBuilder.loadTexts: ieee8021FqtssBAPTrafficClass.setStatus('current')
ieee8021FqtssDeltaBandwidth = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 2), IEEE8021FqtssDeltaBandwidthValue()).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssDeltaBandwidth.setStatus('current')
ieee8021FqtssOperIdleSlopeMs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 3), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeMs.setStatus('current')
ieee8021FqtssOperIdleSlopeLs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 4), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeLs.setStatus('current')
ieee8021FqtssAdminIdleSlopeMs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 5), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeMs.setStatus('current')
ieee8021FqtssAdminIdleSlopeLs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 6), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeLs.setStatus('current')
ieee8021FqtssBapRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssBapRowStatus.setStatus('current')
ieee8021FqtssTxSelectionAlgorithmTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmTable.setStatus('current')
ieee8021FqtssTxSelectionAlgorithmEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssTrafficClass"))
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmEntry.setStatus('current')
ieee8021FqtssTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 1), IEEE8021FqtssTrafficClassValue())
if mibBuilder.loadTexts: ieee8021FqtssTrafficClass.setStatus('current')
ieee8021FqtssTxSelectionAlgorithmID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 2), IEEE8021FqtssTxSelectionAlgorithmIDValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmID.setStatus('current')
ieee8021FqtssSrpRegenOverrideTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2), )
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideTable.setStatus('current')
ieee8021FqtssSrpRegenOverrideEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssSrClassPriority"))
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideEntry.setStatus('current')
ieee8021FqtssSrClassPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 1), IEEE8021PriorityValue())
if mibBuilder.loadTexts: ieee8021FqtssSrClassPriority.setStatus('current')
ieee8021FqtssPriorityRegenOverride = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 2), IEEE8021PriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssPriorityRegenOverride.setStatus('current')
ieee8021FqtssSrpBoundaryPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssSrpBoundaryPort.setStatus('current')
ieee8021FqtssSRClassToPriorityTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3), )
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityTable.setStatus('current')
ieee8021FqtssSRClassToPriorityEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssSrClassPriority"))
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityEntry.setStatus('current')
ieee8021FqtssSRClassToPrioritySrClassID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1, 1), IEEE8021FqtssTrafficClassValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPrioritySrClassID.setStatus('current')
ieee8021FqtssSRClassToPriorityRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssSRClassToPriorityRowStatus.setStatus('current')
ieee8021FqtssBapXTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1), )
if mibBuilder.loadTexts: ieee8021FqtssBapXTable.setStatus('current')
ieee8021FqtssBapXEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1), )
ieee8021FqtssBapEntry.registerAugmentions(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapXEntry"))
ieee8021FqtssBapXEntry.setIndexNames(*ieee8021FqtssBapEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021FqtssBapXEntry.setStatus('current')
ieee8021FqtssBAPClassMeasurementInterval = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssBAPClassMeasurementInterval.setStatus('current')
ieee8021FqtssBAPLockClassBandwidth = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssBAPLockClassBandwidth.setStatus('current')
ieee8021FqtssCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2, 1))
ieee8021FqtssGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2, 2))
ieee8021FqtssBapGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 1)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssDeltaBandwidth"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeMs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeLs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeMs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeLs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBapGroup = ieee8021FqtssBapGroup.setStatus('current')
ieee8021FqtssTxSelectionAlgorithmGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 2)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssTxSelectionAlgorithmID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssTxSelectionAlgorithmGroup = ieee8021FqtssTxSelectionAlgorithmGroup.setStatus('current')
ieee8021FqtssBoundaryPortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 3)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssPriorityRegenOverride"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSrpBoundaryPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBoundaryPortGroup = ieee8021FqtssBoundaryPortGroup.setStatus('current')
ieee8021FqtssBapMeasurementGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 4)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPClassMeasurementInterval"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPLockClassBandwidth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBapMeasurementGroup = ieee8021FqtssBapMeasurementGroup.setStatus('current')
ieee8021FqtssSRClassPriorityGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 5)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassToPrioritySrClassID"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassToPriorityRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssSRClassPriorityGroup = ieee8021FqtssSRClassPriorityGroup.setStatus('current')
ieee8021FqtssCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 16, 2, 1, 1)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssTxSelectionAlgorithmGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBoundaryPortGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapMeasurementGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassPriorityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssCompliance = ieee8021FqtssCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-FQTSS-MIB", ieee8021FqtssSrpRegenOverrideTable=ieee8021FqtssSrpRegenOverrideTable, ieee8021FqtssDeltaBandwidth=ieee8021FqtssDeltaBandwidth, ieee8021FqtssBapEntry=ieee8021FqtssBapEntry, ieee8021FqtssMib=ieee8021FqtssMib, ieee8021FqtssAdminIdleSlopeLs=ieee8021FqtssAdminIdleSlopeLs, ieee8021FqtssBapGroup=ieee8021FqtssBapGroup, ieee8021FqtssObjects=ieee8021FqtssObjects, ieee8021FqtssSRClassToPriorityTable=ieee8021FqtssSRClassToPriorityTable, ieee8021FqtssSRClassToPriorityEntry=ieee8021FqtssSRClassToPriorityEntry, ieee8021FqtssBAPClassMeasurementInterval=ieee8021FqtssBAPClassMeasurementInterval, ieee8021FqtssBapXTable=ieee8021FqtssBapXTable, ieee8021FqtssOperIdleSlopeMs=ieee8021FqtssOperIdleSlopeMs, ieee8021FqtssSrpRegenOverrideEntry=ieee8021FqtssSrpRegenOverrideEntry, ieee8021FqtssPriorityRegenOverride=ieee8021FqtssPriorityRegenOverride, PYSNMP_MODULE_ID=ieee8021FqtssMib, ieee8021FqtssBAPLockClassBandwidth=ieee8021FqtssBAPLockClassBandwidth, ieee8021FqtssSrpBoundaryPort=ieee8021FqtssSrpBoundaryPort, ieee8021FqtssTrafficClass=ieee8021FqtssTrafficClass, ieee8021FqtssTxSelectionAlgorithmTable=ieee8021FqtssTxSelectionAlgorithmTable, ieee8021FqtssTxSelectionAlgorithmID=ieee8021FqtssTxSelectionAlgorithmID, IEEE8021FqtssTrafficClassValue=IEEE8021FqtssTrafficClassValue, ieee8021FqtssCompliances=ieee8021FqtssCompliances, ieee8021FqtssBap=ieee8021FqtssBap, ieee8021FqtssBapRowStatus=ieee8021FqtssBapRowStatus, ieee8021FqtssSRClassToPrioritySrClassID=ieee8021FqtssSRClassToPrioritySrClassID, ieee8021FqtssSRClassToPriorityRowStatus=ieee8021FqtssSRClassToPriorityRowStatus, ieee8021FqtssBapTable=ieee8021FqtssBapTable, ieee8021FqtssBoundaryPortGroup=ieee8021FqtssBoundaryPortGroup, ieee8021FqtssNotifications=ieee8021FqtssNotifications, ieee8021FqtssOperIdleSlopeLs=ieee8021FqtssOperIdleSlopeLs, IEEE8021FqtssTxSelectionAlgorithmIDValue=IEEE8021FqtssTxSelectionAlgorithmIDValue, ieee8021FqtssBapMeasurementGroup=ieee8021FqtssBapMeasurementGroup, ieee8021FqtssTxSelectionAlgorithmEntry=ieee8021FqtssTxSelectionAlgorithmEntry, ieee8021FqtssTxSelectionAlgorithmGroup=ieee8021FqtssTxSelectionAlgorithmGroup, ieee8021FqtssCompliance=ieee8021FqtssCompliance, ieee8021FqtssBapX=ieee8021FqtssBapX, ieee8021FqtssMappings=ieee8021FqtssMappings, ieee8021FqtssAdminIdleSlopeMs=ieee8021FqtssAdminIdleSlopeMs, ieee8021FqtssBAPTrafficClass=ieee8021FqtssBAPTrafficClass, IEEE8021FqtssDeltaBandwidthValue=IEEE8021FqtssDeltaBandwidthValue, ieee8021FqtssBapXEntry=ieee8021FqtssBapXEntry, ieee8021FqtssConformance=ieee8021FqtssConformance, ieee8021FqtssSRClassPriorityGroup=ieee8021FqtssSRClassPriorityGroup, ieee8021FqtssSrClassPriority=ieee8021FqtssSrClassPriority, ieee8021FqtssGroups=ieee8021FqtssGroups)
