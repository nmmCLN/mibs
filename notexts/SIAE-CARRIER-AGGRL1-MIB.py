#
# PySNMP MIB module SIAE-CARRIER-AGGRL1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-CARRIER-AGGRL1-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:16 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, TimeTicks, Counter32, Unsigned32, ModuleIdentity, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
carrierAggr = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 104))
carrierAggr.setRevisions(('2016-08-23 00:00',))
if mibBuilder.loadTexts: carrierAggr.setLastUpdated('201608230000Z')
if mibBuilder.loadTexts: carrierAggr.setOrganization('SIAE MICROELETTRONICA spa')
carrierAggrMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrMibVersion.setStatus('current')
carrierAggrSensorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2), )
if mibBuilder.loadTexts: carrierAggrSensorTable.setStatus('current')
carrierAggrSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1), ).setIndexNames((0, "SIAE-CARRIER-AGGRL1-MIB", "carrierAggrSensorIndex"))
if mibBuilder.loadTexts: carrierAggrSensorEntry.setStatus('current')
carrierAggrSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrSensorIndex.setStatus('current')
carrierAggrSensorRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorRowstatus.setStatus('current')
carrierAggrSensorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorAdminStatus.setStatus('current')
carrierAggrSensorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorIfIndex.setStatus('current')
carrierAggrSensorHitlessCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 5), Bits().clone(namedValues=NamedValues(("hitlessAvailable", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrSensorHitlessCapability.setStatus('current')
carrierAggrSensorHitlessBehaviour = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorHitlessBehaviour.setStatus('current')
carrierAggrSensorHitlessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2))).clone('auto')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorHitlessMode.setStatus('current')
carrierAggrSensorHitlessProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 8), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorHitlessProfile.setStatus('current')
carrierAggrSensorHitlessStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("goodZone", 1), ("hitlessZone", 2), ("badZone", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrSensorHitlessStatus.setStatus('current')
carrierAggrActuatorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3), )
if mibBuilder.loadTexts: carrierAggrActuatorTable.setStatus('current')
carrierAggrActuatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1), ).setIndexNames((0, "SIAE-CARRIER-AGGRL1-MIB", "carrierAggrActuatorIndex"))
if mibBuilder.loadTexts: carrierAggrActuatorEntry.setStatus('current')
carrierAggrActuatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrActuatorIndex.setStatus('current')
carrierAggrActuatorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorRowStatus.setStatus('current')
carrierAggrActuatorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorAdminStatus.setStatus('current')
carrierAggrActuatorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorIfIndex.setStatus('current')
carrierAggrActuatorSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorSensorIndex.setStatus('current')
carrierAggrActuatorConcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrActuatorConcIpAddr.setStatus('current')
mibBuilder.exportSymbols("SIAE-CARRIER-AGGRL1-MIB", carrierAggrSensorHitlessStatus=carrierAggrSensorHitlessStatus, carrierAggrActuatorRowStatus=carrierAggrActuatorRowStatus, carrierAggrSensorIfIndex=carrierAggrSensorIfIndex, carrierAggrSensorTable=carrierAggrSensorTable, carrierAggrSensorAdminStatus=carrierAggrSensorAdminStatus, carrierAggrSensorRowstatus=carrierAggrSensorRowstatus, PYSNMP_MODULE_ID=carrierAggr, carrierAggrSensorHitlessCapability=carrierAggrSensorHitlessCapability, carrierAggrSensorIndex=carrierAggrSensorIndex, carrierAggrSensorEntry=carrierAggrSensorEntry, carrierAggrSensorHitlessMode=carrierAggrSensorHitlessMode, carrierAggrActuatorIndex=carrierAggrActuatorIndex, carrierAggr=carrierAggr, carrierAggrSensorHitlessBehaviour=carrierAggrSensorHitlessBehaviour, carrierAggrMibVersion=carrierAggrMibVersion, carrierAggrActuatorAdminStatus=carrierAggrActuatorAdminStatus, carrierAggrActuatorConcIpAddr=carrierAggrActuatorConcIpAddr, carrierAggrSensorHitlessProfile=carrierAggrSensorHitlessProfile, carrierAggrActuatorTable=carrierAggrActuatorTable, carrierAggrActuatorSensorIndex=carrierAggrActuatorSensorIndex, carrierAggrActuatorEntry=carrierAggrActuatorEntry, carrierAggrActuatorIfIndex=carrierAggrActuatorIfIndex)
