#
# PySNMP MIB module PT-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MONITOR-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:37 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, ModuleIdentity, TimeTicks, NotificationType, MibIdentifier, ObjectIdentity, IpAddress, Counter64, Gauge32, Unsigned32, Bits, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "Unsigned32", "Bits", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ptMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 4))
ptMonitor.setRevisions(('2016-03-09 12:30', '2016-02-10 12:30',))
if mibBuilder.loadTexts: ptMonitor.setLastUpdated('201603091230Z')
if mibBuilder.loadTexts: ptMonitor.setOrganization('Ericsson')
ptMonitorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2))
class HealthStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eOK", 1), ("eNOTOK", 2), ("eUNKNOWN", 3))

hwDiagnosticsTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1), )
if mibBuilder.loadTexts: hwDiagnosticsTable.setStatus('current')
hwDiagnosticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1), ).setIndexNames((0, "PT-MONITOR-MIB", "hwIndex"))
if mibBuilder.loadTexts: hwDiagnosticsEntry.setStatus('current')
hwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwIndex.setStatus('current')
temperatureStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureStatus.setStatus('current')
healthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 3), HealthStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: healthStatus.setStatus('current')
ptMonitorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 1))
ptMonitorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 2))
ptMonitorFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 1, 1)).setObjects(("PT-MONITOR-MIB", "ptMonitorCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptMonitorFullCompliance = ptMonitorFullCompliance.setStatus('current')
ptMonitorCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 2, 1)).setObjects(("PT-MONITOR-MIB", "temperatureStatus"), ("PT-MONITOR-MIB", "healthStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptMonitorCompleteGroup = ptMonitorCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-MONITOR-MIB", ptMonitorCompleteGroup=ptMonitorCompleteGroup, healthStatus=healthStatus, hwDiagnosticsTable=hwDiagnosticsTable, ptMonitorFullCompliance=ptMonitorFullCompliance, HealthStatusTC=HealthStatusTC, ptMonitor=ptMonitor, PYSNMP_MODULE_ID=ptMonitor, hwDiagnosticsEntry=hwDiagnosticsEntry, temperatureStatus=temperatureStatus, ptMonitorGroups=ptMonitorGroups, ptMonitorCompliances=ptMonitorCompliances, ptMonitorConformance=ptMonitorConformance, hwIndex=hwIndex)
