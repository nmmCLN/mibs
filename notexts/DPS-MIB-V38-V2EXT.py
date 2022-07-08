#
# PySNMP MIB module DPS-MIB-V38-V2EXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dpstelecom/DPS-MIB-V38-V2EXT
# Produced by pysmi-1.1.8 at Fri Jul  8 09:17:34 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, Bits, Counter64, TimeTicks, NotificationType, Integer32, iso, MibIdentifier, ModuleIdentity, Gauge32, ObjectIdentity, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibIdentifier", "ModuleIdentity", "Gauge32", "ObjectIdentity", "IpAddress", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dpsInc = MibIdentifier((1, 3, 6, 1, 4, 1, 2682))
dpsAlarmControl = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1))
tmonXM = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 1))
tmonV2XM = ModuleIdentity((1, 3, 6, 1, 4, 1, 2682, 1, 3))
tmonV2XM.setRevisions(('2015-02-05 12:00',))
if mibBuilder.loadTexts: tmonV2XM.setLastUpdated('201502051200Z')
if mibBuilder.loadTexts: tmonV2XM.setOrganization('DPS Telecom')
tmonV2Ident = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1))
tmonV2IdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2IdentManufacturer.setStatus('current')
tmonV2IdentModel = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2IdentModel.setStatus('current')
tmonV2IdentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2IdentSoftwareVersion.setStatus('current')
tmonV2AlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2), )
if mibBuilder.loadTexts: tmonV2AlarmTable.setStatus('current')
tmonV2AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1), ).setIndexNames((0, "DPS-MIB-V38-V2EXT", "tmonV2AIndex"))
if mibBuilder.loadTexts: tmonV2AlarmEntry.setStatus('current')
tmonV2AIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: tmonV2AIndex.setStatus('current')
tmonV2ASite = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ASite.setStatus('current')
tmonV2ADesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADesc.setStatus('current')
tmonV2AState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AState.setStatus('current')
tmonV2ASeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ASeverity.setStatus('current')
tmonV2AChgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AChgDate.setStatus('current')
tmonV2AChgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AChgTime.setStatus('current')
tmonV2AAuxDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AAuxDesc.setStatus('current')
tmonV2ADispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADispDesc.setStatus('current')
tmonV2APntType = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2APntType.setStatus('current')
tmonV2APort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2APort.setStatus('current')
tmonV2AAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AAddress.setStatus('current')
tmonV2ADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADisplay.setStatus('current')
tmonV2APoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2APoint.setStatus('current')
tmonV2AEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AEvent.setStatus('current')
tmonV2AIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AIPAddr.setStatus('current')
tmonV2ADevDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADevDesc.setStatus('current')
tmonV2CommandGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3))
tmonV2CPType = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CPType.setStatus('current')
tmonV2CPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CPort.setStatus('current')
tmonV2CAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CAddress.setStatus('current')
tmonV2CDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CDisplay.setStatus('current')
tmonV2CPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CPoint.setStatus('current')
tmonV2CEvent = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CEvent.setStatus('current')
tmonV2CAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 17, 18, 19))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3), ("ack", 17), ("tag", 18), ("untag", 19)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CAction.setStatus('current')
tmonV2CAuxText = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CAuxText.setStatus('current')
tmonV2CResult = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("pending", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CResult.setStatus('current')
tmonV2CosEventTable = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4), )
if mibBuilder.loadTexts: tmonV2CosEventTable.setStatus('current')
tmonV2CosEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1), ).setIndexNames((0, "DPS-MIB-V38-V2EXT", "tmonV2AIndex"))
if mibBuilder.loadTexts: tmonV2CosEventEntry.setStatus('current')
tmonV2CosEIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: tmonV2CosEIndex.setStatus('current')
tmonV2CosESite = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosESite.setStatus('current')
tmonV2CosEDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEDesc.setStatus('current')
tmonV2CosEState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEState.setStatus('current')
tmonV2CosESeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosESeverity.setStatus('current')
tmonV2CosEChgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEChgDate.setStatus('current')
tmonV2CosEChgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEChgTime.setStatus('current')
tmonV2CosEAuxDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEAuxDesc.setStatus('current')
tmonV2CosEDispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEDispDesc.setStatus('current')
tmonV2CosEPntType = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEPntType.setStatus('current')
tmonV2CosEPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEPort.setStatus('current')
tmonV2CosEAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEAddress.setStatus('current')
tmonV2CosEDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEDisplay.setStatus('current')
tmonV2CosEPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEPoint.setStatus('current')
tmonV2CosEEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 4, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CosEEventID.setStatus('current')
tmonV2AlarmGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5), )
if mibBuilder.loadTexts: tmonV2AlarmGrid.setStatus('current')
tmonV2AlarmGridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1), ).setIndexNames((0, "DPS-MIB-V38-V2EXT", "tmonV2AIndex"))
if mibBuilder.loadTexts: tmonV2AlarmGridEntry.setStatus('current')
tmonV2AGIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: tmonV2AGIndex.setStatus('current')
tmonV2AGSite = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGSite.setStatus('current')
tmonV2AGDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGDesc.setStatus('current')
tmonV2AGState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGState.setStatus('current')
tmonV2AGSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGSeverity.setStatus('current')
tmonV2AGChgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGChgDate.setStatus('current')
tmonV2AGChgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGChgTime.setStatus('current')
tmonV2AGAuxDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGAuxDesc.setStatus('current')
tmonV2AGDispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGDispDesc.setStatus('current')
tmonV2AGPntType = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGPntType.setStatus('current')
tmonV2AGPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGPort.setStatus('current')
tmonV2AGAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGAddress.setStatus('current')
tmonV2AGDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGDisplay.setStatus('current')
tmonV2AGPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 5, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AGPoint.setStatus('current')
tmonV2analogChannels = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6), )
if mibBuilder.loadTexts: tmonV2analogChannels.setStatus('current')
tmonV2chanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanPort.setStatus('current')
tmonV2chanAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanAddress.setStatus('current')
tmonV2chanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanNumber.setStatus('current')
tmonV2chanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanEnabled.setStatus('current')
tmonV2chanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanDescription.setStatus('current')
tmonV2chanValueInt = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanValueInt.setStatus('current')
tmonV2chanValueInt100 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanValueInt100.setStatus('current')
tmonV2chanValueStr = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanValueStr.setStatus('current')
tmonV2chanDisplayunits = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanDisplayunits.setStatus('current')
tmonV2chanThresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("noAlarms", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2chanThresholds.setStatus('current')
dpsRTUv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 4))
dpsRTUv2Ident = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1))
dpsRTUv2Manufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Manufacturer.setStatus('current')
dpsRTUv2Model = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Model.setStatus('current')
dpsRTUv2FirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2FirmwareVersion.setStatus('current')
dpsRTUv2DateTime = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2DateTime.setStatus('current')
dpsRTUv2SyncReq = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("sync", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2SyncReq.setStatus('current')
dpsRTUv2DisplayGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2), )
if mibBuilder.loadTexts: dpsRTUv2DisplayGrid.setStatus('current')
dpsRTUv2DisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1), ).setIndexNames((0, "DPS-MIB-V38-V2EXT", "dpsRTUv2Port"), (0, "DPS-MIB-V38-V2EXT", "dpsRTUv2Address"), (0, "DPS-MIB-V38-V2EXT", "dpsRTUv2Display"))
if mibBuilder.loadTexts: dpsRTUv2DisplayEntry.setStatus('current')
dpsRTUv2Port = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Port.setStatus('current')
dpsRTUv2Address = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Address.setStatus('current')
dpsRTUv2Display = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Display.setStatus('current')
dpsRTUv2DispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2DispDesc.setStatus('current')
dpsRTUv2PntMap = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2PntMap.setStatus('current')
dpsRTUv2ControlGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3))
dpsRTUv2CPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CPort.setStatus('current')
dpsRTUv2CAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CAddress.setStatus('current')
dpsRTUv2CDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CDisplay.setStatus('current')
dpsRTUv2CPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CPoint.setStatus('current')
dpsRTUv2CAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CAction.setStatus('current')
dpsRTUv2AlarmGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5), )
if mibBuilder.loadTexts: dpsRTUv2AlarmGrid.setStatus('current')
dpsRTUv2AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1), ).setIndexNames((0, "DPS-MIB-V38-V2EXT", "dpsRTUv2APort"), (0, "DPS-MIB-V38-V2EXT", "dpsRTUv2AAddress"), (0, "DPS-MIB-V38-V2EXT", "dpsRTUv2ADisplay"), (0, "DPS-MIB-V38-V2EXT", "dpsRTUv2APoint"))
if mibBuilder.loadTexts: dpsRTUv2AlarmEntry.setStatus('current')
dpsRTUv2APort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2APort.setStatus('current')
dpsRTUv2AAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2AAddress.setStatus('current')
dpsRTUv2ADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2ADisplay.setStatus('current')
dpsRTUv2APoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2APoint.setStatus('current')
dpsRTUv2APntDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2APntDesc.setStatus('current')
dpsRTUv2AState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2AState.setStatus('current')
analogChannelsv2 = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6), )
if mibBuilder.loadTexts: analogChannelsv2.setStatus('current')
tmonV2channelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 3, 6, 1), ).setIndexNames((0, "DPS-MIB-V38-V2EXT", "channelNumberv2"))
if mibBuilder.loadTexts: tmonV2channelEntry.setStatus('current')
channelEntryv2 = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1), ).setIndexNames((0, "DPS-MIB-V38-V2EXT", "channelNumberv2"))
if mibBuilder.loadTexts: channelEntryv2.setStatus('current')
channelNumberv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumberv2.setStatus('current')
enabledv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: enabledv2.setStatus('current')
descriptionv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: descriptionv2.setStatus('current')
valuev2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: valuev2.setStatus('current')
thresholdsv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAlarms", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4), ("notDetected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thresholdsv2.setStatus('current')
tmonV2CRalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 10)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2CRalarmSet.setStatus('current')
tmonV2CRalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 11)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2CRalarmClr.setStatus('current')
tmonV2MJalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 12)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MJalarmSet.setStatus('current')
tmonV2MJalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 13)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MJalarmClr.setStatus('current')
tmonV2MNalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 14)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MNalarmSet.setStatus('current')
tmonV2MNalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 15)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MNalarmClr.setStatus('current')
tmonV2STalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 16)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2STalarmSet.setStatus('current')
tmonV2STalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 17)).setObjects(("DPS-MIB-V38-V2EXT", "tmonV2ASite"), ("DPS-MIB-V38-V2EXT", "tmonV2ADesc"), ("DPS-MIB-V38-V2EXT", "tmonV2AState"), ("DPS-MIB-V38-V2EXT", "tmonV2ASeverity"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgDate"), ("DPS-MIB-V38-V2EXT", "tmonV2AChgTime"), ("DPS-MIB-V38-V2EXT", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2EXT", "tmonV2APntType"), ("DPS-MIB-V38-V2EXT", "tmonV2APort"), ("DPS-MIB-V38-V2EXT", "tmonV2AAddress"), ("DPS-MIB-V38-V2EXT", "tmonV2ADisplay"), ("DPS-MIB-V38-V2EXT", "tmonV2APoint"), ("DPS-MIB-V38-V2EXT", "tmonV2CEvent"), ("DPS-MIB-V38-V2EXT", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2EXT", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2STalarmClr.setStatus('current')
mibBuilder.exportSymbols("DPS-MIB-V38-V2EXT", dpsRTUv2APntDesc=dpsRTUv2APntDesc, tmonV2AGDispDesc=tmonV2AGDispDesc, tmonV2AGAuxDesc=tmonV2AGAuxDesc, tmonV2APoint=tmonV2APoint, tmonV2MNalarmClr=tmonV2MNalarmClr, dpsRTUv2APort=dpsRTUv2APort, tmonV2CosEPoint=tmonV2CosEPoint, tmonV2AAuxDesc=tmonV2AAuxDesc, tmonV2CommandGrid=tmonV2CommandGrid, tmonV2CosEDesc=tmonV2CosEDesc, analogChannelsv2=analogChannelsv2, dpsRTUv2FirmwareVersion=dpsRTUv2FirmwareVersion, tmonV2chanValueInt=tmonV2chanValueInt, tmonV2CosEAddress=tmonV2CosEAddress, tmonV2CosEIndex=tmonV2CosEIndex, tmonV2XM=tmonV2XM, dpsRTUv2Model=dpsRTUv2Model, dpsRTUv2APoint=dpsRTUv2APoint, tmonV2AGDisplay=tmonV2AGDisplay, tmonV2chanDescription=tmonV2chanDescription, dpsRTUv2ADisplay=dpsRTUv2ADisplay, tmonV2AGAddress=tmonV2AGAddress, tmonV2chanAddress=tmonV2chanAddress, tmonV2AlarmGrid=tmonV2AlarmGrid, tmonV2chanDisplayunits=tmonV2chanDisplayunits, dpsInc=dpsInc, tmonV2CPType=tmonV2CPType, tmonV2AlarmTable=tmonV2AlarmTable, dpsRTUv2Address=dpsRTUv2Address, tmonV2CosEChgTime=tmonV2CosEChgTime, tmonXM=tmonXM, tmonV2AChgTime=tmonV2AChgTime, tmonV2AGSeverity=tmonV2AGSeverity, tmonV2CRalarmClr=tmonV2CRalarmClr, tmonV2AIPAddr=tmonV2AIPAddr, dpsRTUv2AlarmEntry=dpsRTUv2AlarmEntry, tmonV2AGSite=tmonV2AGSite, channelEntryv2=channelEntryv2, tmonV2ASite=tmonV2ASite, thresholdsv2=thresholdsv2, tmonV2CosEPort=tmonV2CosEPort, tmonV2ADispDesc=tmonV2ADispDesc, dpsRTUv2DateTime=dpsRTUv2DateTime, tmonV2IdentSoftwareVersion=tmonV2IdentSoftwareVersion, valuev2=valuev2, tmonV2MJalarmSet=tmonV2MJalarmSet, tmonV2Ident=tmonV2Ident, tmonV2AAddress=tmonV2AAddress, tmonV2AGIndex=tmonV2AGIndex, dpsRTUv2DispDesc=dpsRTUv2DispDesc, tmonV2MNalarmSet=tmonV2MNalarmSet, tmonV2CosEventEntry=tmonV2CosEventEntry, dpsAlarmControl=dpsAlarmControl, tmonV2CosEAuxDesc=tmonV2CosEAuxDesc, descriptionv2=descriptionv2, tmonV2STalarmSet=tmonV2STalarmSet, tmonV2CDisplay=tmonV2CDisplay, tmonV2MJalarmClr=tmonV2MJalarmClr, tmonV2chanValueStr=tmonV2chanValueStr, tmonV2chanPort=tmonV2chanPort, tmonV2CRalarmSet=tmonV2CRalarmSet, tmonV2AState=tmonV2AState, tmonV2AGPntType=tmonV2AGPntType, tmonV2CosESite=tmonV2CosESite, tmonV2ADevDesc=tmonV2ADevDesc, dpsRTUv2CAddress=dpsRTUv2CAddress, dpsRTUv2AAddress=dpsRTUv2AAddress, channelNumberv2=channelNumberv2, tmonV2AlarmEntry=tmonV2AlarmEntry, dpsRTUv2DisplayGrid=dpsRTUv2DisplayGrid, tmonV2AGChgDate=tmonV2AGChgDate, tmonV2chanEnabled=tmonV2chanEnabled, tmonV2channelEntry=tmonV2channelEntry, tmonV2CosEEventID=tmonV2CosEEventID, tmonV2CAuxText=tmonV2CAuxText, tmonV2CPoint=tmonV2CPoint, tmonV2AGState=tmonV2AGState, tmonV2AIndex=tmonV2AIndex, tmonV2AlarmGridEntry=tmonV2AlarmGridEntry, tmonV2analogChannels=tmonV2analogChannels, tmonV2CAddress=tmonV2CAddress, tmonV2STalarmClr=tmonV2STalarmClr, tmonV2APntType=tmonV2APntType, tmonV2CosEDispDesc=tmonV2CosEDispDesc, dpsRTUv2Ident=dpsRTUv2Ident, tmonV2chanNumber=tmonV2chanNumber, dpsRTUv2Display=dpsRTUv2Display, tmonV2CosEDisplay=tmonV2CosEDisplay, tmonV2ASeverity=tmonV2ASeverity, tmonV2chanValueInt100=tmonV2chanValueInt100, tmonV2AGDesc=tmonV2AGDesc, tmonV2CPort=tmonV2CPort, tmonV2CAction=tmonV2CAction, dpsRTUv2DisplayEntry=dpsRTUv2DisplayEntry, tmonV2AGChgTime=tmonV2AGChgTime, dpsRTUv2SyncReq=dpsRTUv2SyncReq, tmonV2IdentManufacturer=tmonV2IdentManufacturer, tmonV2CResult=tmonV2CResult, tmonV2AChgDate=tmonV2AChgDate, tmonV2CosEChgDate=tmonV2CosEChgDate, tmonV2AGPort=tmonV2AGPort, dpsRTUv2=dpsRTUv2, dpsRTUv2CPort=dpsRTUv2CPort, tmonV2AEvent=tmonV2AEvent, tmonV2ADisplay=tmonV2ADisplay, dpsRTUv2AlarmGrid=dpsRTUv2AlarmGrid, dpsRTUv2CAction=dpsRTUv2CAction, tmonV2CEvent=tmonV2CEvent, tmonV2CosESeverity=tmonV2CosESeverity, tmonV2CosEPntType=tmonV2CosEPntType, enabledv2=enabledv2, dpsRTUv2CDisplay=dpsRTUv2CDisplay, tmonV2AGPoint=tmonV2AGPoint, tmonV2APort=tmonV2APort, tmonV2ADesc=tmonV2ADesc, tmonV2CosEventTable=tmonV2CosEventTable, tmonV2CosEState=tmonV2CosEState, dpsRTUv2Manufacturer=dpsRTUv2Manufacturer, dpsRTUv2CPoint=dpsRTUv2CPoint, dpsRTUv2PntMap=dpsRTUv2PntMap, dpsRTUv2AState=dpsRTUv2AState, PYSNMP_MODULE_ID=tmonV2XM, tmonV2IdentModel=tmonV2IdentModel, dpsRTUv2Port=dpsRTUv2Port, dpsRTUv2ControlGrid=dpsRTUv2ControlGrid, tmonV2chanThresholds=tmonV2chanThresholds)
