#
# PySNMP MIB module SUPERMICRO-HEALTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/supermicro/SUPERMICRO-HEALTH-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:35:16 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, Integer32, ModuleIdentity, Bits, Counter32, Unsigned32, TimeTicks, ObjectIdentity, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Integer32", "ModuleIdentity", "Bits", "Counter32", "Unsigned32", "TimeTicks", "ObjectIdentity", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
smHealth, = mibBuilder.importSymbols("SUPERMICRO-SMI", "smHealth")
smHealthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 2, 1))
if mibBuilder.loadTexts: smHealthMIB.setLastUpdated('200110260000Z')
if mibBuilder.loadTexts: smHealthMIB.setOrganization('Super Micro Computer Inc.')
class SMHealthInfoTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 64)

smHealthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1))
smHealthMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1), )
if mibBuilder.loadTexts: smHealthMonitorTable.setStatus('current')
smHealthMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1), ).setIndexNames((0, "SUPERMICRO-HEALTH-MIB", "smHealthMonitorIndex"))
if mibBuilder.loadTexts: smHealthMonitorEntry.setStatus('current')
smHealthMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: smHealthMonitorIndex.setStatus('current')
smHealthMonitorName = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorName.setStatus('current')
smHealthMonitorType = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 3), SMHealthInfoTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorType.setStatus('current')
smHealthMonitorReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorReading.setStatus('current')
smHealthMonitorHighLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorHighLimit.setStatus('current')
smHealthMonitorLowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorLowLimit.setStatus('current')
smHealthMonitorMaxReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorMaxReading.setStatus('current')
smHealthMonitorMinReading = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorMinReading.setStatus('current')
smHealthMonitorDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorDivisor.setStatus('current')
smHealthMonitorMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smHealthMonitorMonitor.setStatus('current')
smHealthMonitorReadingUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorReadingUnit.setStatus('current')
smHealthMonitorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthMonitorStatus.setStatus('current')
smHealthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 2))
smHealthConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3))
smHealthCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1))
smHealthGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2))
smHealthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1, 1)).setObjects(("SUPERMICRO-HEALTH-MIB", "smHealthMonitorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smHealthCompliance = smHealthCompliance.setStatus('current')
smHealthMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2, 1)).setObjects(("SUPERMICRO-HEALTH-MIB", "smHealthMonitorType"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorName"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorHighLimit"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorLowLimit"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMaxReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMinReading"), ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMonitor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smHealthMonitorGroup = smHealthMonitorGroup.setStatus('current')
smHealthAllinoneStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthAllinoneStatus.setStatus('current')
smHealthAllinoneMsg = MibScalar((1, 3, 6, 1, 4, 1, 10876, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smHealthAllinoneMsg.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-HEALTH-MIB", smHealthMonitorReading=smHealthMonitorReading, smHealthMonitorLowLimit=smHealthMonitorLowLimit, smHealthMonitorEntry=smHealthMonitorEntry, smHealthMonitorIndex=smHealthMonitorIndex, smHealthMonitorTable=smHealthMonitorTable, smHealthMonitorDivisor=smHealthMonitorDivisor, smHealthNotifications=smHealthNotifications, smHealthMonitorMaxReading=smHealthMonitorMaxReading, smHealthMonitorName=smHealthMonitorName, smHealthMonitorMinReading=smHealthMonitorMinReading, smHealthMonitorGroup=smHealthMonitorGroup, smHealthObjects=smHealthObjects, PYSNMP_MODULE_ID=smHealthMIB, smHealthMonitorHighLimit=smHealthMonitorHighLimit, SMHealthInfoTypes=SMHealthInfoTypes, smHealthMonitorMonitor=smHealthMonitorMonitor, smHealthMIB=smHealthMIB, smHealthConformance=smHealthConformance, smHealthGroups=smHealthGroups, smHealthMonitorReadingUnit=smHealthMonitorReadingUnit, smHealthMonitorStatus=smHealthMonitorStatus, smHealthMonitorType=smHealthMonitorType, smHealthCompliances=smHealthCompliances, smHealthAllinoneMsg=smHealthAllinoneMsg, smHealthCompliance=smHealthCompliance, smHealthAllinoneStatus=smHealthAllinoneStatus)
