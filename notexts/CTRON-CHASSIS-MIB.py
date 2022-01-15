#
# PySNMP MIB module CTRON-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:12 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctronChassis, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronChassis")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctChas = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1))
ctEnviron = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2))
ctFanModule = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3))
ctChasFNB = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasFNB.setStatus('mandatory')
ctChasAlarmEna = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("notSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctChasAlarmEna.setStatus('mandatory')
chassisAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("chassisNoFaultCondition", 1), ("chassisFaultCondition", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisAlarmState.setStatus('mandatory')
ctChasPowerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1), )
if mibBuilder.loadTexts: ctChasPowerTable.setStatus('mandatory')
ctChasPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1), ).setIndexNames((0, "CTRON-CHASSIS-MIB", "ctChasPowerSupplyNum"))
if mibBuilder.loadTexts: ctChasPowerEntry.setStatus('mandatory')
ctChasPowerSupplyNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyNum.setStatus('mandatory')
ctChasPowerSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("infoNotAvailable", 1), ("notInstalled", 2), ("installedAndOperating", 3), ("installedAndNotOperating", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyState.setStatus('mandatory')
ctChasPowerSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ac-dc", 1), ("dc-dc", 2), ("notSupported", 3), ("highOutput", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyType.setStatus('mandatory')
ctChasPowerSupplyRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("redundant", 1), ("notRedundant", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyRedundancy.setStatus('mandatory')
ctChasFanModuleTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1), )
if mibBuilder.loadTexts: ctChasFanModuleTable.setStatus('mandatory')
ctChasFanModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-CHASSIS-MIB", "ctChasFanModuleNum"))
if mibBuilder.loadTexts: ctChasFanModuleEntry.setStatus('mandatory')
ctChasFanModuleNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasFanModuleNum.setStatus('mandatory')
ctChasFanModuleState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("infoNotAvailable", 1), ("notInstalled", 2), ("installedAndOperating", 3), ("installedAndNotOperating", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasFanModuleState.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-CHASSIS-MIB", ctChasPowerTable=ctChasPowerTable, ctChasAlarmEna=ctChasAlarmEna, ctChasFanModuleEntry=ctChasFanModuleEntry, ctChasFanModuleNum=ctChasFanModuleNum, ctChasFanModuleState=ctChasFanModuleState, ctChasPowerSupplyRedundancy=ctChasPowerSupplyRedundancy, ctChasFanModuleTable=ctChasFanModuleTable, ctChasPowerSupplyNum=ctChasPowerSupplyNum, ctEnviron=ctEnviron, ctFanModule=ctFanModule, ctChasFNB=ctChasFNB, chassisAlarmState=chassisAlarmState, ctChasPowerEntry=ctChasPowerEntry, ctChasPowerSupplyState=ctChasPowerSupplyState, ctChasPowerSupplyType=ctChasPowerSupplyType, ctChas=ctChas)
