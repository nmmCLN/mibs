#
# PySNMP MIB module RADLAN-HWENVIROMENT (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/RADLAN-HWENVIROMENT
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:29 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Counter64, MibIdentifier, NotificationType, IpAddress, Integer32, ObjectIdentity, Bits, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Counter64", "MibIdentifier", "NotificationType", "IpAddress", "Integer32", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlEnv = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 83))
rlEnv.setRevisions(('2003-09-21 00:00',))
if mibBuilder.loadTexts: rlEnv.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlEnv.setOrganization('Radlan Computer Communications Ltd.')
class RlEnvMonState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notPresent", 5), ("notFunctioning", 6))

rlEnvPhysicalDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 83, 1))
rlEnvMonFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 1, 1), )
if mibBuilder.loadTexts: rlEnvMonFanStatusTable.setStatus('current')
rlEnvMonFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1), ).setIndexNames((0, "RADLAN-HWENVIROMENT", "rlEnvMonFanStatusIndex"))
if mibBuilder.loadTexts: rlEnvMonFanStatusEntry.setStatus('current')
rlEnvMonFanStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rlEnvMonFanStatusIndex.setStatus('current')
rlEnvMonFanStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonFanStatusDescr.setStatus('current')
rlEnvMonFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 1, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonFanState.setStatus('current')
rlEnvMonSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 1, 2), )
if mibBuilder.loadTexts: rlEnvMonSupplyStatusTable.setStatus('current')
rlEnvMonSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1), ).setIndexNames((0, "RADLAN-HWENVIROMENT", "rlEnvMonSupplyStatusIndex"))
if mibBuilder.loadTexts: rlEnvMonSupplyStatusEntry.setStatus('current')
rlEnvMonSupplyStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rlEnvMonSupplyStatusIndex.setStatus('current')
rlEnvMonSupplyStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplyStatusDescr.setStatus('current')
rlEnvMonSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplyState.setStatus('current')
rlEnvMonSupplySource = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ac", 2), ("dc", 3), ("externalPowerSupply", 4), ("internalRedundant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplySource.setStatus('current')
mibBuilder.exportSymbols("RADLAN-HWENVIROMENT", rlEnvPhysicalDescription=rlEnvPhysicalDescription, rlEnvMonFanStatusEntry=rlEnvMonFanStatusEntry, rlEnvMonSupplyStatusTable=rlEnvMonSupplyStatusTable, rlEnvMonSupplyStatusDescr=rlEnvMonSupplyStatusDescr, rlEnvMonSupplySource=rlEnvMonSupplySource, rlEnvMonSupplyState=rlEnvMonSupplyState, rlEnvMonSupplyStatusEntry=rlEnvMonSupplyStatusEntry, rlEnvMonFanStatusTable=rlEnvMonFanStatusTable, RlEnvMonState=RlEnvMonState, rlEnvMonFanStatusIndex=rlEnvMonFanStatusIndex, rlEnvMonFanStatusDescr=rlEnvMonFanStatusDescr, rlEnv=rlEnv, rlEnvMonFanState=rlEnvMonFanState, rlEnvMonSupplyStatusIndex=rlEnvMonSupplyStatusIndex, PYSNMP_MODULE_ID=rlEnv)
