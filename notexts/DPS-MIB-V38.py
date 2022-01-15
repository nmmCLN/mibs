#
# PySNMP MIB module DPS-MIB-V38 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dpstelecom/DPS-MIB-V38
# Produced by pysmi-1.1.8 at Sat Jan 15 20:16:52 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212-MIB", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysDescr, sysLocation = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr", "sysLocation")
IpAddress, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, NotificationType, enterprises, TimeTicks, ObjectIdentity, Counter32, NotificationType, iso, Counter64, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "NotificationType", "enterprises", "TimeTicks", "ObjectIdentity", "Counter32", "NotificationType", "iso", "Counter64", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dpsInc = MibIdentifier((1, 3, 6, 1, 4, 1, 2682))
dpsAlarmControl = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1))
tmonXM = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 1))
tmonIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1))
tmonIdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonIdentManufacturer.setStatus('mandatory')
tmonIdentModel = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonIdentModel.setStatus('mandatory')
tmonIdentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonIdentSoftwareVersion.setStatus('mandatory')
tmonAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2), )
if mibBuilder.loadTexts: tmonAlarmTable.setStatus('mandatory')
tmonAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1), ).setIndexNames((0, "DPS-MIB-V38", "tmonAIndex"))
if mibBuilder.loadTexts: tmonAlarmEntry.setStatus('mandatory')
tmonAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAIndex.setStatus('mandatory')
tmonASite = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonASite.setStatus('mandatory')
tmonADesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADesc.setStatus('mandatory')
tmonAState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAState.setStatus('mandatory')
tmonASeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonASeverity.setStatus('mandatory')
tmonAChgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAChgDate.setStatus('mandatory')
tmonAChgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAChgTime.setStatus('mandatory')
tmonAAuxDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAAuxDesc.setStatus('mandatory')
tmonADispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADispDesc.setStatus('mandatory')
tmonAPntType = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAPntType.setStatus('mandatory')
tmonAPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAPort.setStatus('mandatory')
tmonAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAAddress.setStatus('mandatory')
tmonADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADisplay.setStatus('mandatory')
tmonAPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAPoint.setStatus('mandatory')
tmonAIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAIPAddr.setStatus('mandatory')
tmonADevDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADevDesc.setStatus('mandatory')
tmonCommandGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3))
tmonCPType = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCPType.setStatus('mandatory')
tmonCPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCPort.setStatus('mandatory')
tmonCAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCAddress.setStatus('mandatory')
tmonCDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCDisplay.setStatus('mandatory')
tmonCPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCPoint.setStatus('mandatory')
tmonCEvent = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCEvent.setStatus('mandatory')
tmonCAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 17, 18, 19))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3), ("ack", 17), ("tag", 18), ("untag", 19)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCAction.setStatus('mandatory')
tmonCAuxText = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCAuxText.setStatus('mandatory')
tmonCResult = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("pending", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonCResult.setStatus('mandatory')
dpsRTU = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 2))
dpsRTUIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1))
dpsRTUManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUManufacturer.setStatus('mandatory')
dpsRTUModel = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUModel.setStatus('mandatory')
dpsRTUFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUFirmwareVersion.setStatus('mandatory')
dpsRTUDateTime = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUDateTime.setStatus('mandatory')
dpsRTUSyncReq = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("sync", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUSyncReq.setStatus('mandatory')
dpsRTUDisplayGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2), )
if mibBuilder.loadTexts: dpsRTUDisplayGrid.setStatus('mandatory')
dpsRTUDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1), ).setIndexNames((0, "DPS-MIB-V38", "dpsRTUPort"), (0, "DPS-MIB-V38", "dpsRTUAddress"), (0, "DPS-MIB-V38", "dpsRTUDisplay"))
if mibBuilder.loadTexts: dpsRTUDisplayEntry.setStatus('mandatory')
dpsRTUPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUPort.setStatus('mandatory')
dpsRTUAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAddress.setStatus('mandatory')
dpsRTUDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUDisplay.setStatus('mandatory')
dpsRTUDispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUDispDesc.setStatus('mandatory')
dpsRTUPntMap = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUPntMap.setStatus('mandatory')
dpsRTUControlGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3))
dpsRTUCPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCPort.setStatus('mandatory')
dpsRTUCAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCAddress.setStatus('mandatory')
dpsRTUCDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCDisplay.setStatus('mandatory')
dpsRTUCPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCPoint.setStatus('mandatory')
dpsRTUCAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCAction.setStatus('mandatory')
dpsRTUAlarmGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5), )
if mibBuilder.loadTexts: dpsRTUAlarmGrid.setStatus('mandatory')
dpsRTUAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1), ).setIndexNames((0, "DPS-MIB-V38", "dpsRTUAPort"), (0, "DPS-MIB-V38", "dpsRTUAAddress"), (0, "DPS-MIB-V38", "dpsRTUADisplay"), (0, "DPS-MIB-V38", "dpsRTUAPoint"))
if mibBuilder.loadTexts: dpsRTUAlarmEntry.setStatus('mandatory')
dpsRTUAPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAPort.setStatus('mandatory')
dpsRTUAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAAddress.setStatus('mandatory')
dpsRTUADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUADisplay.setStatus('mandatory')
dpsRTUAPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAPoint.setStatus('mandatory')
dpsRTUAPntDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUAPntDesc.setStatus('mandatory')
dpsRTUAState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAState.setStatus('mandatory')
analogChannels = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6), )
if mibBuilder.loadTexts: analogChannels.setStatus('mandatory')
channelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1), ).setIndexNames((0, "DPS-MIB-V38", "channelNumber"))
if mibBuilder.loadTexts: channelEntry.setStatus('mandatory')
channelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumber.setStatus('mandatory')
enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: enabled.setStatus('mandatory')
description = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: description.setStatus('mandatory')
value = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: value.setStatus('mandatory')
thresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAlarms", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4), ("notDetected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thresholds.setStatus('mandatory')
tmonCRalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,10)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
tmonCRalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,11)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
tmonMJalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,12)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
tmonMJalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,13)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
tmonMNalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,14)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
tmonMNalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,15)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
tmonSTalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,16)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
tmonSTalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,17)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
dpsRTUPointSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,20)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"), ("DPS-MIB-V38", "dpsRTUAPort"), ("DPS-MIB-V38", "dpsRTUAAddress"), ("DPS-MIB-V38", "dpsRTUADisplay"), ("DPS-MIB-V38", "dpsRTUAPoint"), ("DPS-MIB-V38", "dpsRTUAPntDesc"), ("DPS-MIB-V38", "dpsRTUAState"))
dpsRTUPointClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,21)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"), ("DPS-MIB-V38", "dpsRTUAPort"), ("DPS-MIB-V38", "dpsRTUCAddress"), ("DPS-MIB-V38", "dpsRTUADisplay"), ("DPS-MIB-V38", "dpsRTUAPoint"), ("DPS-MIB-V38", "dpsRTUAPntDesc"), ("DPS-MIB-V38", "dpsRTUAState"))
dpsRTUsumPSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,101)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
dpsRTUsumPClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,102)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
dpsRTUcomFailed = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,103)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
dpsRTUcomRestored = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,104)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
mibBuilder.exportSymbols("DPS-MIB-V38", tmonMNalarmClr=tmonMNalarmClr, tmonCRalarmSet=tmonCRalarmSet, tmonCAuxText=tmonCAuxText, tmonCResult=tmonCResult, enabled=enabled, tmonXM=tmonXM, dpsRTUDisplayEntry=dpsRTUDisplayEntry, dpsRTUPointSet=dpsRTUPointSet, tmonCDisplay=tmonCDisplay, tmonIdentSoftwareVersion=tmonIdentSoftwareVersion, dpsRTUCPoint=dpsRTUCPoint, dpsRTUPntMap=dpsRTUPntMap, tmonMJalarmClr=tmonMJalarmClr, dpsRTUDisplay=dpsRTUDisplay, tmonCPort=tmonCPort, dpsRTUFirmwareVersion=dpsRTUFirmwareVersion, dpsRTUDisplayGrid=dpsRTUDisplayGrid, dpsRTUCDisplay=dpsRTUCDisplay, dpsRTUAlarmEntry=dpsRTUAlarmEntry, tmonAPort=tmonAPort, tmonCAction=tmonCAction, tmonCRalarmClr=tmonCRalarmClr, tmonADispDesc=tmonADispDesc, tmonAlarmTable=tmonAlarmTable, tmonAAuxDesc=tmonAAuxDesc, dpsRTUPointClr=dpsRTUPointClr, dpsRTUAlarmGrid=dpsRTUAlarmGrid, tmonAPoint=tmonAPoint, dpsRTUcomFailed=dpsRTUcomFailed, tmonCAddress=tmonCAddress, dpsRTUDispDesc=dpsRTUDispDesc, dpsRTUAPntDesc=dpsRTUAPntDesc, description=description, dpsRTUCAction=dpsRTUCAction, dpsRTUAPoint=dpsRTUAPoint, channelNumber=channelNumber, analogChannels=analogChannels, tmonCPoint=tmonCPoint, tmonAlarmEntry=tmonAlarmEntry, channelEntry=channelEntry, dpsRTUsumPSet=dpsRTUsumPSet, tmonAPntType=tmonAPntType, dpsRTUCPort=dpsRTUCPort, tmonASite=tmonASite, dpsRTUDateTime=dpsRTUDateTime, tmonADesc=tmonADesc, value=value, dpsRTUCAddress=dpsRTUCAddress, dpsRTUManufacturer=dpsRTUManufacturer, dpsRTUControlGrid=dpsRTUControlGrid, tmonIdent=tmonIdent, dpsRTUAddress=dpsRTUAddress, tmonADevDesc=tmonADevDesc, dpsRTU=dpsRTU, dpsAlarmControl=dpsAlarmControl, tmonAState=tmonAState, dpsRTUModel=dpsRTUModel, tmonAAddress=tmonAAddress, dpsRTUAState=dpsRTUAState, tmonAIndex=tmonAIndex, tmonMJalarmSet=tmonMJalarmSet, tmonCEvent=tmonCEvent, dpsRTUsumPClr=dpsRTUsumPClr, dpsRTUSyncReq=dpsRTUSyncReq, dpsRTUAAddress=dpsRTUAAddress, tmonIdentModel=tmonIdentModel, tmonAChgDate=tmonAChgDate, tmonASeverity=tmonASeverity, tmonADisplay=tmonADisplay, tmonSTalarmClr=tmonSTalarmClr, dpsRTUPort=dpsRTUPort, dpsInc=dpsInc, tmonAIPAddr=tmonAIPAddr, dpsRTUcomRestored=dpsRTUcomRestored, tmonMNalarmSet=tmonMNalarmSet, tmonIdentManufacturer=tmonIdentManufacturer, dpsRTUAPort=dpsRTUAPort, tmonCPType=tmonCPType, dpsRTUIdent=dpsRTUIdent, dpsRTUADisplay=dpsRTUADisplay, tmonCommandGrid=tmonCommandGrid, tmonAChgTime=tmonAChgTime, thresholds=thresholds, tmonSTalarmSet=tmonSTalarmSet)
