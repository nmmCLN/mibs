#
# PySNMP MIB module SFA-INFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ddn/SFA-INFO
# Produced by pysmi-1.1.12 at Thu Apr  4 09:16:35 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, ModuleIdentity, NotificationType, ObjectIdentity, MibIdentifier, iso, Gauge32, Counter32, Bits, Integer32, Unsigned32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibIdentifier", "iso", "Gauge32", "Counter32", "Bits", "Integer32", "Unsigned32", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
datadirect = MibIdentifier((1, 3, 6, 1, 4, 1, 6894))
unit = MibIdentifier((1, 3, 6, 1, 4, 1, 6894, 2))
eventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 6894, 2, 10))
class DisplayString(OctetString):
    pass

tempNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempNumber.setStatus('mandatory')
tempTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 2), )
if mibBuilder.loadTexts: tempTable.setStatus('mandatory')
tempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1), ).setIndexNames((0, "SFA-INFO", "tempIndex"))
if mibBuilder.loadTexts: tempEntry.setStatus('mandatory')
tempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempIndex.setStatus('mandatory')
tempEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEncId.setStatus('mandatory')
tempEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEncPos.setStatus('mandatory')
tempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("critical", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempStatus.setStatus('mandatory')
fanNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNumber.setStatus('mandatory')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 4), )
if mibBuilder.loadTexts: fanTable.setStatus('mandatory')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1), ).setIndexNames((0, "SFA-INFO", "fanIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('mandatory')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanIndex.setStatus('mandatory')
fanEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEncId.setStatus('mandatory')
fanEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEncPos.setStatus('mandatory')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("healthy", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('mandatory')
powerNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerNumber.setStatus('mandatory')
powerTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 6), )
if mibBuilder.loadTexts: powerTable.setStatus('mandatory')
powerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1), ).setIndexNames((0, "SFA-INFO", "powerIndex"))
if mibBuilder.loadTexts: powerEntry.setStatus('mandatory')
powerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerIndex.setStatus('mandatory')
powerEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEncId.setStatus('mandatory')
powerEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEncPos.setStatus('mandatory')
powerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("healthy", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatus.setStatus('mandatory')
poolNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumber.setStatus('mandatory')
poolTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 8), )
if mibBuilder.loadTexts: poolTable.setStatus('mandatory')
poolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1), ).setIndexNames((0, "SFA-INFO", "poolIndex"))
if mibBuilder.loadTexts: poolEntry.setStatus('mandatory')
poolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolIndex.setStatus('mandatory')
poolId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolId.setStatus('mandatory')
poolType = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("storage", 1), ("spare", 2), ("unassigned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolType.setStatus('mandatory')
poolNumDisks = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumDisks.setStatus('mandatory')
physicalDiskTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 9), )
if mibBuilder.loadTexts: physicalDiskTable.setStatus('mandatory')
physicalDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1), ).setIndexNames((0, "SFA-INFO", "physDiskIndex"))
if mibBuilder.loadTexts: physicalDiskEntry.setStatus('mandatory')
physDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskIndex.setStatus('mandatory')
physDiskPoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskPoolId.setStatus('mandatory')
physDiskId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskId.setStatus('mandatory')
physDiskWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskWWN.setStatus('mandatory')
physDiskEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskEnc.setStatus('mandatory')
physDiskSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskSlot.setStatus('mandatory')
physDiskState = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("failed", 2), ("predictedfailure", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskState.setStatus('mandatory')
systemName = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemName.setStatus('mandatory')
eventLogTrapLevel = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogTrapLevel.setStatus('mandatory')
eventLogNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogNumEntries.setStatus('mandatory')
eventLogTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3), )
if mibBuilder.loadTexts: eventLogTable.setStatus('mandatory')
eventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1), ).setIndexNames((0, "SFA-INFO", "eventLogIndex"))
if mibBuilder.loadTexts: eventLogEntry.setStatus('mandatory')
eventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogIndex.setStatus('mandatory')
eventLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogLevel.setStatus('mandatory')
eventLogDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogDescr.setStatus('mandatory')
mibBuilder.exportSymbols("SFA-INFO", tempIndex=tempIndex, eventLogNumEntries=eventLogNumEntries, tempStatus=tempStatus, powerTable=powerTable, poolId=poolId, fanStatus=fanStatus, powerIndex=powerIndex, poolNumber=poolNumber, physDiskIndex=physDiskIndex, physDiskState=physDiskState, DisplayString=DisplayString, fanEncId=fanEncId, poolNumDisks=poolNumDisks, fanNumber=fanNumber, fanTable=fanTable, eventLogIndex=eventLogIndex, unit=unit, tempTable=tempTable, poolEntry=poolEntry, poolType=poolType, powerEncPos=powerEncPos, fanIndex=fanIndex, systemName=systemName, eventLogTable=eventLogTable, physDiskSlot=physDiskSlot, fanEntry=fanEntry, powerStatus=powerStatus, tempEntry=tempEntry, eventLogEntry=eventLogEntry, powerEncId=powerEncId, physDiskPoolId=physDiskPoolId, eventLog=eventLog, eventLogDescr=eventLogDescr, eventLogTrapLevel=eventLogTrapLevel, eventLogLevel=eventLogLevel, physicalDiskTable=physicalDiskTable, datadirect=datadirect, tempNumber=tempNumber, poolIndex=poolIndex, physDiskWWN=physDiskWWN, physicalDiskEntry=physicalDiskEntry, physDiskEnc=physDiskEnc, tempEncPos=tempEncPos, powerNumber=powerNumber, tempEncId=tempEncId, fanEncPos=fanEncPos, poolTable=poolTable, powerEntry=powerEntry, physDiskId=physDiskId)
