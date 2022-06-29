#
# PySNMP MIB module NETGEAR-BOXSERVICES-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netgear/NETGEAR-BOXSERVICES-PRIVATE-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:48 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ng7000managedswitch, = mibBuilder.importSymbols("NETGEAR-REF-MIB", "ng7000managedswitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, Counter64, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, IpAddress, MibIdentifier, NotificationType, TimeTicks, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Counter64", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "TimeTicks", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fastPathBoxServices = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 10, 43))
fastPathBoxServices.setRevisions(('2011-01-26 00:00', '2008-02-22 00:00',))
if mibBuilder.loadTexts: fastPathBoxServices.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathBoxServices.setOrganization('Netgear Inc')
class BoxsTemperatureStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("low", 0), ("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notpresent", 5), ("notoperational", 6))

boxServicesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1))
boxServicesNormalTempRangeMin = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesNormalTempRangeMin.setStatus('current')
boxServicesNormalTempRangeMax = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100)).clone(45)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesNormalTempRangeMax.setStatus('current')
boxServicesTemperatureTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesTemperatureTrapEnable.setStatus('current')
boxServicesPSMStateTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesPSMStateTrapEnable.setStatus('current')
boxServicesFanStateTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesFanStateTrapEnable.setStatus('current')
boxServicesThermalShutdownSensor = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 13), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxServicesThermalShutdownSensor.setStatus('current')
boxServicesThermalShutdownTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 14), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxServicesThermalShutdownTemperature.setStatus('current')
boxServicesFansTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6), )
if mibBuilder.loadTexts: boxServicesFansTable.setStatus('current')
boxServicesFansEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6, 1), ).setIndexNames((0, "NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesFanUnitIndex"), (0, "NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"))
if mibBuilder.loadTexts: boxServicesFansEntry.setStatus('current')
boxServicesFanUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanUnitIndex.setStatus('current')
boxServicesFansIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFansIndex.setStatus('current')
boxServicesFanItemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2), ("fixedAC", 3), ("removableDC", 4), ("fixedDC", 5), ("removableAC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanItemType.setStatus('current')
boxServicesFanItemState = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notpresent", 1), ("operational", 2), ("failed", 3), ("powering", 4), ("nopower", 5), ("notpowering", 6), ("incompatible", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanItemState.setStatus('current')
boxServicesFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(13, 13)).setFixedLength(13)).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanSpeed.setStatus('current')
boxServicesFanDutyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(13, 13)).setFixedLength(13)).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanDutyLevel.setStatus('current')
boxServicesPowSuppliesTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 7), )
if mibBuilder.loadTexts: boxServicesPowSuppliesTable.setStatus('current')
boxServicesPowSuppliesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 7, 1), ).setIndexNames((0, "NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesPowerSuppUnitIndex"), (0, "NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"))
if mibBuilder.loadTexts: boxServicesPowSuppliesEntry.setStatus('current')
boxServicesPowerSuppUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 7, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowerSuppUnitIndex.setStatus('current')
boxServicesPowSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyIndex.setStatus('current')
boxServicesPowSupplyItemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2), ("fixedAC", 3), ("removableDC", 4), ("fixedDC", 5), ("removableAC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyItemType.setStatus('current')
boxServicesPowSupplyItemState = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notpresent", 1), ("operational", 2), ("failed", 3), ("powering", 4), ("nopower", 5), ("notpowering", 6), ("incompatible", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyItemState.setStatus('current')
boxServicesTempSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 8), )
if mibBuilder.loadTexts: boxServicesTempSensorsTable.setStatus('current')
boxServicesTempSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 8, 1), ).setIndexNames((0, "NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesUnitIndex"), (0, "NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"))
if mibBuilder.loadTexts: boxServicesTempSensorsEntry.setStatus('current')
boxServicesUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesUnitIndex.setStatus('current')
boxServicesTempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorIndex.setStatus('current')
boxServicesTempSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2), ("fixedAC", 3), ("removableDC", 4), ("fixedDC", 5), ("removableAC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorType.setStatus('current')
boxServicesTempSensorState = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 8, 1, 4), BoxsTemperatureStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorState.setStatus('obsolete')
boxServicesTempSensorTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorTemperature.setStatus('current')
boxServicesTempUnitTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 15), )
if mibBuilder.loadTexts: boxServicesTempUnitTable.setStatus('current')
boxServicesTempUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 15, 1), ).setIndexNames((0, "NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesTempUnitIndex"))
if mibBuilder.loadTexts: boxServicesTempUnitEntry.setStatus('current')
boxServicesTempUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 15, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempUnitIndex.setStatus('current')
boxServicesTempUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 15, 1, 2), BoxsTemperatureStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempUnitState.setStatus('current')
boxServicesTempUnitTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 43, 1, 15, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempUnitTemperature.setStatus('current')
boxServicesNotificationsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10, 43, 2))
boxsItemStateChangeEvent = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("insertion", 1), ("removal", 2), ("becomeoperational", 3), ("failure", 4), ("losepower", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsItemStateChangeEvent.setStatus('current')
boxsTemperatureChangeEvent = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("abovethreshold", 1), ("belowthreshold", 2), ("withinnormalrange", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsTemperatureChangeEvent.setStatus('current')
boxsTemperatureStatusCurrentEvent = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 2, 3), BoxsTemperatureStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsTemperatureStatusCurrentEvent.setStatus('current')
boxsTemperatureStatusPreviousEvent = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 2, 4), BoxsTemperatureStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsTemperatureStatusPreviousEvent.setStatus('current')
fastPathBoxServicesTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10, 43, 0))
boxsFanStateChange = NotificationType((1, 3, 6, 1, 4, 1, 4526, 10, 43, 0, 1)).setObjects(("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"), ("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
if mibBuilder.loadTexts: boxsFanStateChange.setStatus('current')
boxsPowSupplyStateChange = NotificationType((1, 3, 6, 1, 4, 1, 4526, 10, 43, 0, 2)).setObjects(("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"), ("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
if mibBuilder.loadTexts: boxsPowSupplyStateChange.setStatus('current')
boxsTemperatureChange = NotificationType((1, 3, 6, 1, 4, 1, 4526, 10, 43, 0, 3)).setObjects(("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"), ("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureChangeEvent"))
if mibBuilder.loadTexts: boxsTemperatureChange.setStatus('obsolete')
boxsThermalShutdown = NotificationType((1, 3, 6, 1, 4, 1, 4526, 10, 43, 0, 4)).setObjects(("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesThermalShutdownSensor"), ("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesThermalShutdownTemperature"))
if mibBuilder.loadTexts: boxsThermalShutdown.setStatus('current')
boxsTemperatureStateChange = NotificationType((1, 3, 6, 1, 4, 1, 4526, 10, 43, 0, 5)).setObjects(("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxServicesTempUnitIndex"), ("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureStatusCurrentEvent"), ("NETGEAR-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureStatusPreviousEvent"))
if mibBuilder.loadTexts: boxsTemperatureStateChange.setStatus('current')
boxsLocatorLedConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10, 43, 4))
boxsLocatorLedUnit = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxsLocatorLedUnit.setStatus('current')
boxsLocatorLedTime = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 4, 2), Integer32().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxsLocatorLedTime.setStatus('current')
boxsLocatorLedEnable = MibScalar((1, 3, 6, 1, 4, 1, 4526, 10, 43, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxsLocatorLedEnable.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-BOXSERVICES-PRIVATE-MIB", boxsTemperatureChangeEvent=boxsTemperatureChangeEvent, boxsPowSupplyStateChange=boxsPowSupplyStateChange, boxsLocatorLedUnit=boxsLocatorLedUnit, boxServicesFansTable=boxServicesFansTable, boxServicesPowerSuppUnitIndex=boxServicesPowerSuppUnitIndex, PYSNMP_MODULE_ID=fastPathBoxServices, boxServicesNotificationsGroup=boxServicesNotificationsGroup, boxServicesTemperatureTrapEnable=boxServicesTemperatureTrapEnable, boxServicesPowSuppliesTable=boxServicesPowSuppliesTable, boxServicesTempSensorsTable=boxServicesTempSensorsTable, boxServicesPowSupplyItemState=boxServicesPowSupplyItemState, boxsLocatorLedTime=boxsLocatorLedTime, boxsTemperatureStatusCurrentEvent=boxsTemperatureStatusCurrentEvent, boxServicesFanItemState=boxServicesFanItemState, fastPathBoxServices=fastPathBoxServices, boxServicesFanStateTrapEnable=boxServicesFanStateTrapEnable, boxServicesTempSensorIndex=boxServicesTempSensorIndex, fastPathBoxServicesTraps=fastPathBoxServicesTraps, boxsLocatorLedEnable=boxsLocatorLedEnable, boxServicesFansIndex=boxServicesFansIndex, boxServicesTempUnitTemperature=boxServicesTempUnitTemperature, boxServicesThermalShutdownSensor=boxServicesThermalShutdownSensor, boxsTemperatureChange=boxsTemperatureChange, boxServicesFanDutyLevel=boxServicesFanDutyLevel, boxServicesThermalShutdownTemperature=boxServicesThermalShutdownTemperature, boxServicesTempUnitEntry=boxServicesTempUnitEntry, boxsTemperatureStateChange=boxsTemperatureStateChange, boxServicesFanSpeed=boxServicesFanSpeed, boxServicesNormalTempRangeMin=boxServicesNormalTempRangeMin, boxServicesTempSensorType=boxServicesTempSensorType, boxServicesNormalTempRangeMax=boxServicesNormalTempRangeMax, boxServicesFansEntry=boxServicesFansEntry, boxServicesPSMStateTrapEnable=boxServicesPSMStateTrapEnable, boxServicesPowSupplyIndex=boxServicesPowSupplyIndex, boxServicesUnitIndex=boxServicesUnitIndex, boxServicesPowSupplyItemType=boxServicesPowSupplyItemType, boxServicesTempSensorState=boxServicesTempSensorState, boxsItemStateChangeEvent=boxsItemStateChangeEvent, boxServicesPowSuppliesEntry=boxServicesPowSuppliesEntry, boxServicesTempUnitIndex=boxServicesTempUnitIndex, BoxsTemperatureStatus=BoxsTemperatureStatus, boxServicesTempUnitTable=boxServicesTempUnitTable, boxsLocatorLedConfigGroup=boxsLocatorLedConfigGroup, boxsTemperatureStatusPreviousEvent=boxsTemperatureStatusPreviousEvent, boxsThermalShutdown=boxsThermalShutdown, boxServicesFanUnitIndex=boxServicesFanUnitIndex, boxServicesTempSensorsEntry=boxServicesTempSensorsEntry, boxServicesGroup=boxServicesGroup, boxServicesFanItemType=boxServicesFanItemType, boxServicesTempUnitState=boxServicesTempUnitState, boxServicesTempSensorTemperature=boxServicesTempSensorTemperature, boxsFanStateChange=boxsFanStateChange)
