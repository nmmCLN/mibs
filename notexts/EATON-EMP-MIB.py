#
# PySNMP MIB module EATON-EMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eaton/EATON-EMP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:17:05 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
xupsEnvironment, = mibBuilder.importSymbols("EATON-OIDS", "xupsEnvironment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, ModuleIdentity, TimeTicks, iso, Counter32, NotificationType, Gauge32, Unsigned32, Bits, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "ModuleIdentity", "TimeTicks", "iso", "Counter32", "NotificationType", "Gauge32", "Unsigned32", "Bits", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eatonEMPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 534, 1, 6, 0))
eatonEMPMIB.setRevisions(('2007-03-12 00:00',))
if mibBuilder.loadTexts: eatonEMPMIB.setLastUpdated('200703120000Z')
if mibBuilder.loadTexts: eatonEMPMIB.setOrganization('Eaton Corporation')
xupsEnvRemoteTemp = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsEnvRemoteTemp.setStatus('current')
xupsEnvRemoteHumidity = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsEnvRemoteHumidity.setStatus('current')
xupsEnvNumContacts = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsEnvNumContacts.setStatus('current')
xupsContactSenseTable = MibTable((1, 3, 6, 1, 4, 1, 534, 1, 6, 8), )
if mibBuilder.loadTexts: xupsContactSenseTable.setStatus('current')
xupsContactsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1), ).setIndexNames((0, "EATON-EMP-MIB", "xupsContactIndex"))
if mibBuilder.loadTexts: xupsContactsTableEntry.setStatus('current')
xupsContactIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsContactIndex.setStatus('current')
xupsContactType = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normallyOpen", 1), ("normallyClosed", 2), ("anyChange", 3), ("notUsed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsContactType.setStatus('current')
xupsContactState = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("openWithNotice", 3), ("closedWithNotice", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsContactState.setStatus('current')
xupsContactDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsContactDescr.setStatus('current')
xupsEnvRemoteTempLowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteTempLowerLimit.setStatus('current')
xupsEnvRemoteTempUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteTempUpperLimit.setStatus('current')
xupsEnvRemoteHumidityLowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteHumidityLowerLimit.setStatus('current')
xupsEnvRemoteHumidityUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteHumidityUpperLimit.setStatus('current')
eatonEMPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2))
eatonEMPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 1)).setObjects(("EATON-EMP-MIB", "xupsEnvRemoteTemp"), ("EATON-EMP-MIB", "xupsEnvRemoteHumidity"), ("EATON-EMP-MIB", "xupsEnvRemoteTempLowerLimit"), ("EATON-EMP-MIB", "xupsEnvRemoteTempUpperLimit"), ("EATON-EMP-MIB", "xupsEnvRemoteHumidityLowerLimit"), ("EATON-EMP-MIB", "xupsEnvRemoteHumidityUpperLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eatonEMPGroup = eatonEMPGroup.setStatus('current')
eatonEMPTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 2)).setObjects(("EATON-EMP-MIB", "xupsEnvNumContacts"), ("EATON-EMP-MIB", "xupsContactIndex"), ("EATON-EMP-MIB", "xupsContactType"), ("EATON-EMP-MIB", "xupsContactState"), ("EATON-EMP-MIB", "xupsContactDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eatonEMPTableGroup = eatonEMPTableGroup.setStatus('current')
eatonEMPSimpleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 4)).setObjects(("EATON-EMP-MIB", "eatonEMPGroup"), ("EATON-EMP-MIB", "eatonEMPTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eatonEMPSimpleCompliance = eatonEMPSimpleCompliance.setStatus('current')
mibBuilder.exportSymbols("EATON-EMP-MIB", xupsContactSenseTable=xupsContactSenseTable, PYSNMP_MODULE_ID=eatonEMPMIB, eatonEMPTableGroup=eatonEMPTableGroup, eatonEMPMIB=eatonEMPMIB, xupsContactType=xupsContactType, xupsContactIndex=xupsContactIndex, xupsEnvRemoteHumidityUpperLimit=xupsEnvRemoteHumidityUpperLimit, xupsContactState=xupsContactState, eatonEMPConformance=eatonEMPConformance, eatonEMPSimpleCompliance=eatonEMPSimpleCompliance, xupsEnvRemoteTempUpperLimit=xupsEnvRemoteTempUpperLimit, xupsContactsTableEntry=xupsContactsTableEntry, xupsContactDescr=xupsContactDescr, xupsEnvRemoteHumidity=xupsEnvRemoteHumidity, xupsEnvRemoteTempLowerLimit=xupsEnvRemoteTempLowerLimit, xupsEnvNumContacts=xupsEnvNumContacts, xupsEnvRemoteTemp=xupsEnvRemoteTemp, xupsEnvRemoteHumidityLowerLimit=xupsEnvRemoteHumidityLowerLimit, eatonEMPGroup=eatonEMPGroup)
