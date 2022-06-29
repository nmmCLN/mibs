#
# PySNMP MIB module MBG-SNMP-XPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-XPT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:30 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
mbgSnmpRoot, = mibBuilder.importSymbols("MBG-SNMP-ROOT-MIB", "mbgSnmpRoot")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, ModuleIdentity, Gauge32, Unsigned32, iso, IpAddress, ObjectIdentity, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Gauge32", "Unsigned32", "iso", "IpAddress", "ObjectIdentity", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mbgXPT = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597, 10))
mbgXPT.setRevisions(('2012-01-25 00:00', '2006-01-20 00:00',))
if mibBuilder.loadTexts: mbgXPT.setLastUpdated('201201250000Z')
if mibBuilder.loadTexts: mbgXPT.setOrganization('www.meinberg.de')
mbgGPSRefclock1 = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 2))
mbgGPSRefclock2 = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 3))
mbgSCU = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 4))
mbgXPTTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 5))
mbgGPSRefclock1Type = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1Type.setStatus('current')
mbgGPSRefclock1TypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1TypeVal.setStatus('current')
mbgGPSRefclock1Mode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1Mode.setStatus('current')
mbgGPSRefclock1ModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1ModeVal.setStatus('current')
mbgGPSRef1GpsState = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsState.setStatus('current')
mbgGPSRef1GpsStateVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsStateVal.setStatus('current')
mbgGPSRef1GpsPosition = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsPosition.setStatus('current')
mbgGPSRef1GpsSatellites = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellites.setStatus('current')
mbgGPSRef1GpsSatellitesGood = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellitesGood.setStatus('current')
mbgGPSRef1GpsSatellitesInView = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellitesInView.setStatus('current')
mbgGPSRefclock2Type = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2Type.setStatus('current')
mbgGPSRefclock2TypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2TypeVal.setStatus('current')
mbgGPSRefclock2Mode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2Mode.setStatus('current')
mbgGPSRefclock2ModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2ModeVal.setStatus('current')
mbgGPSRef2GpsState = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsState.setStatus('current')
mbgGPSRef2GpsStateVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsStateVal.setStatus('current')
mbgGPSRef2GpsPosition = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsPosition.setStatus('current')
mbgGPSRef2GpsSatellites = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellites.setStatus('current')
mbgGPSRef2GpsSatellitesGood = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellitesGood.setStatus('current')
mbgGPSRef2GpsSatellitesInView = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellitesInView.setStatus('current')
mbgSCUType = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUType.setStatus('current')
mbgSCUTypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTypeVal.setStatus('current')
mbgSCUMaster = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMaster.setStatus('current')
mbgSCUMasterVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMasterVal.setStatus('current')
mbgSCUMasterselect = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMasterselect.setStatus('current')
mbgSCUMasterselectVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMasterselectVal.setStatus('current')
mbgSCUTimeSync1 = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTimeSync1.setStatus('current')
mbgSCUTimeSync2 = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTimeSync2.setStatus('current')
mbgSCUTimelimitError = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTimelimitError.setStatus('current')
mbgSCUDisableOutputs = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUDisableOutputs.setStatus('current')
mbgSCUSelectedInput = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUSelectedInput.setStatus('current')
mbgSCUSelectedInputVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUSelectedInputVal.setStatus('current')
mbgSCUACOMode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUACOMode.setStatus('current')
mbgSCUPSUStatus = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUPSUStatus.setStatus('current')
mbgSCUPSU1Status = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUPSU1Status.setStatus('current')
mbgSCUPSU2Status = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUPSU2Status.setStatus('current')
mbgGPSTrapColdBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 1))
if mibBuilder.loadTexts: mbgGPSTrapColdBoot.setStatus('current')
mbgGPSTrapWarmBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 2))
if mibBuilder.loadTexts: mbgGPSTrapWarmBoot.setStatus('current')
mbgGPSNavSolved = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 3))
if mibBuilder.loadTexts: mbgGPSNavSolved.setStatus('current')
mbgGPSTrapReceiverNotResponding = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 4))
if mibBuilder.loadTexts: mbgGPSTrapReceiverNotResponding.setStatus('current')
mbgGPSTrapReceiverNotSync = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 5))
if mibBuilder.loadTexts: mbgGPSTrapReceiverNotSync.setStatus('current')
mbgGPSTrapAntennaFaulty = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 6))
if mibBuilder.loadTexts: mbgGPSTrapAntennaFaulty.setStatus('current')
mbgGPSTrapAntennaReconnect = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 7))
if mibBuilder.loadTexts: mbgGPSTrapAntennaReconnect.setStatus('current')
mbgGPSTrapLANXPTBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 8))
if mibBuilder.loadTexts: mbgGPSTrapLANXPTBoot.setStatus('current')
mbgGPSTrapLeapSecondAnnounced = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 9))
if mibBuilder.loadTexts: mbgGPSTrapLeapSecondAnnounced.setStatus('current')
mbgGPSTrapMasterclockSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 10))
if mibBuilder.loadTexts: mbgGPSTrapMasterclockSwitchover.setStatus('current')
mbgGPSTrapPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 11))
if mibBuilder.loadTexts: mbgGPSTrapPowerSupplyFailure.setStatus('current')
mbgGPSTrapPowerSupplyOK = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 12))
if mibBuilder.loadTexts: mbgGPSTrapPowerSupplyOK.setStatus('current')
mbgGPSTrapTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 99))
if mibBuilder.loadTexts: mbgGPSTrapTestNotification.setStatus('current')
mbgXPTConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 90))
mbgXPTCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 90, 1))
mbgXPTGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 90, 2))
mbgXPTCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5597, 10, 90, 1, 1)).setObjects(("MBG-SNMP-XPT-MIB", "mbgXPTObjectsGroup"), ("MBG-SNMP-XPT-MIB", "mbgXPTTrapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgXPTCompliance = mbgXPTCompliance.setStatus('current')
mbgXPTObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5597, 10, 90, 2, 1)).setObjects(("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1Type"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1TypeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1Mode"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1ModeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsState"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsStateVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsPosition"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellites"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellitesGood"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellitesInView"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2Type"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2TypeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2Mode"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2ModeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsState"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsStateVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsPosition"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellites"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellitesGood"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellitesInView"), ("MBG-SNMP-XPT-MIB", "mbgSCUType"), ("MBG-SNMP-XPT-MIB", "mbgSCUTypeVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUMaster"), ("MBG-SNMP-XPT-MIB", "mbgSCUMasterVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUMasterselect"), ("MBG-SNMP-XPT-MIB", "mbgSCUMasterselectVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUTimeSync1"), ("MBG-SNMP-XPT-MIB", "mbgSCUTimeSync2"), ("MBG-SNMP-XPT-MIB", "mbgSCUTimelimitError"), ("MBG-SNMP-XPT-MIB", "mbgSCUDisableOutputs"), ("MBG-SNMP-XPT-MIB", "mbgSCUSelectedInput"), ("MBG-SNMP-XPT-MIB", "mbgSCUSelectedInputVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUACOMode"), ("MBG-SNMP-XPT-MIB", "mbgSCUPSUStatus"), ("MBG-SNMP-XPT-MIB", "mbgSCUPSU1Status"), ("MBG-SNMP-XPT-MIB", "mbgSCUPSU2Status"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgXPTObjectsGroup = mbgXPTObjectsGroup.setStatus('current')
mbgXPTTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5597, 10, 90, 2, 2)).setObjects(("MBG-SNMP-XPT-MIB", "mbgGPSTrapColdBoot"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapWarmBoot"), ("MBG-SNMP-XPT-MIB", "mbgGPSNavSolved"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapReceiverNotResponding"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapReceiverNotSync"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapAntennaFaulty"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapAntennaReconnect"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapLANXPTBoot"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapLeapSecondAnnounced"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapMasterclockSwitchover"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapPowerSupplyFailure"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapPowerSupplyOK"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapTestNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgXPTTrapsGroup = mbgXPTTrapsGroup.setStatus('current')
mibBuilder.exportSymbols("MBG-SNMP-XPT-MIB", mbgGPSTrapTestNotification=mbgGPSTrapTestNotification, mbgGPSRef2GpsState=mbgGPSRef2GpsState, mbgGPSTrapWarmBoot=mbgGPSTrapWarmBoot, mbgGPSRefclock2TypeVal=mbgGPSRefclock2TypeVal, mbgGPSRefclock2Type=mbgGPSRefclock2Type, mbgGPSTrapPowerSupplyFailure=mbgGPSTrapPowerSupplyFailure, mbgGPSRef1GpsPosition=mbgGPSRef1GpsPosition, mbgSCUSelectedInputVal=mbgSCUSelectedInputVal, mbgSCUDisableOutputs=mbgSCUDisableOutputs, mbgGPSRefclock1ModeVal=mbgGPSRefclock1ModeVal, mbgGPSRef2GpsSatellites=mbgGPSRef2GpsSatellites, mbgGPSRef2GpsSatellitesGood=mbgGPSRef2GpsSatellitesGood, mbgGPSRefclock2Mode=mbgGPSRefclock2Mode, mbgSCUPSUStatus=mbgSCUPSUStatus, mbgGPSRefclock1Mode=mbgGPSRefclock1Mode, mbgGPSRef1GpsSatellitesInView=mbgGPSRef1GpsSatellitesInView, mbgSCUTimeSync2=mbgSCUTimeSync2, mbgSCUPSU1Status=mbgSCUPSU1Status, mbgGPSRefclock1TypeVal=mbgGPSRefclock1TypeVal, mbgSCUACOMode=mbgSCUACOMode, mbgGPSTrapReceiverNotSync=mbgGPSTrapReceiverNotSync, mbgGPSTrapMasterclockSwitchover=mbgGPSTrapMasterclockSwitchover, mbgSCUTypeVal=mbgSCUTypeVal, mbgSCUMasterselect=mbgSCUMasterselect, mbgSCUTimeSync1=mbgSCUTimeSync1, mbgGPSRefclock1=mbgGPSRefclock1, mbgGPSTrapColdBoot=mbgGPSTrapColdBoot, mbgGPSRef2GpsSatellitesInView=mbgGPSRef2GpsSatellitesInView, mbgSCU=mbgSCU, mbgGPSRef2GpsPosition=mbgGPSRef2GpsPosition, mbgGPSRefclock2=mbgGPSRefclock2, mbgGPSRef1GpsSatellitesGood=mbgGPSRef1GpsSatellitesGood, mbgGPSRef2GpsStateVal=mbgGPSRef2GpsStateVal, mbgGPSRefclock1Type=mbgGPSRefclock1Type, mbgGPSTrapAntennaFaulty=mbgGPSTrapAntennaFaulty, mbgGPSTrapLeapSecondAnnounced=mbgGPSTrapLeapSecondAnnounced, mbgXPTCompliances=mbgXPTCompliances, mbgXPTCompliance=mbgXPTCompliance, mbgXPTConformance=mbgXPTConformance, PYSNMP_MODULE_ID=mbgXPT, mbgSCUMasterVal=mbgSCUMasterVal, mbgXPTTrapsGroup=mbgXPTTrapsGroup, mbgSCUPSU2Status=mbgSCUPSU2Status, mbgSCUTimelimitError=mbgSCUTimelimitError, mbgSCUMaster=mbgSCUMaster, mbgGPSTrapReceiverNotResponding=mbgGPSTrapReceiverNotResponding, mbgGPSTrapAntennaReconnect=mbgGPSTrapAntennaReconnect, mbgXPTObjectsGroup=mbgXPTObjectsGroup, mbgXPTGroups=mbgXPTGroups, mbgSCUMasterselectVal=mbgSCUMasterselectVal, mbgGPSRef1GpsStateVal=mbgGPSRef1GpsStateVal, mbgGPSRefclock2ModeVal=mbgGPSRefclock2ModeVal, mbgSCUType=mbgSCUType, mbgGPSTrapLANXPTBoot=mbgGPSTrapLANXPTBoot, mbgSCUSelectedInput=mbgSCUSelectedInput, mbgGPSNavSolved=mbgGPSNavSolved, mbgXPT=mbgXPT, mbgGPSRef1GpsState=mbgGPSRef1GpsState, mbgXPTTraps=mbgXPTTraps, mbgGPSRef1GpsSatellites=mbgGPSRef1GpsSatellites, mbgGPSTrapPowerSupplyOK=mbgGPSTrapPowerSupplyOK)
