#
# PySNMP MIB module MBG-SNMP-XPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-XPT-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:10 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mbgSnmpRoot, = mibBuilder.importSymbols("MBG-SNMP-ROOT-MIB", "mbgSnmpRoot")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, IpAddress, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, NotificationType, Gauge32, MibIdentifier, Unsigned32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mbgXPT = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597, 10))
mbgXPT.setRevisions(('2012-01-25 00:00', '2006-01-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mbgXPT.setRevisionsDescriptions(('Update to new format referencing MBG-SNMP-ROOT-MIB', 'Covering LAN-XPT and SCU-XPT modules from Meinberg',))
if mibBuilder.loadTexts: mbgXPT.setLastUpdated('201201250000Z')
if mibBuilder.loadTexts: mbgXPT.setOrganization('www.meinberg.de')
if mibBuilder.loadTexts: mbgXPT.setContactInfo('postal:   Meinberg Funkuhren\n                    Auf der Landwehr 22\n                    31812 Bad Pyrmont\n\t            Germany\n\n          email:    info@meinberg.de')
if mibBuilder.loadTexts: mbgXPT.setDescription('Top-level infrastructure of the MBG-SNMP project enterprise MIB tree')
mbgGPSRefclock1 = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 2))
mbgGPSRefclock2 = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 3))
mbgSCU = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 4))
mbgXPTTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 5))
mbgGPSRefclock1Type = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1Type.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock1Type.setDescription('Type of clock')
mbgGPSRefclock1TypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1TypeVal.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock1TypeVal.setDescription('Type of refclock as value')
mbgGPSRefclock1Mode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1Mode.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock1Mode.setDescription('current Mode of refclock')
mbgGPSRefclock1ModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock1ModeVal.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock1ModeVal.setDescription('current Mode of refclock as value')
mbgGPSRef1GpsState = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsState.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef1GpsState.setDescription('current State of GPS refclock ')
mbgGPSRef1GpsStateVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsStateVal.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef1GpsStateVal.setDescription('current State of GPS refclock as value')
mbgGPSRef1GpsPosition = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsPosition.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef1GpsPosition.setDescription('current Position of GPS refclock ')
mbgGPSRef1GpsSatellites = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellites.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellites.setDescription('current Satellites in view and good of GPS refclock ')
mbgGPSRef1GpsSatellitesGood = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellitesGood.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellitesGood.setDescription('current good Satellites of GPS refclock as value')
mbgGPSRef1GpsSatellitesInView = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellitesInView.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef1GpsSatellitesInView.setDescription('current satellites in view of GPS refclock as value')
mbgGPSRefclock2Type = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2Type.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock2Type.setDescription('Type of clock')
mbgGPSRefclock2TypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2TypeVal.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock2TypeVal.setDescription('Type of refclock as value')
mbgGPSRefclock2Mode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2Mode.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock2Mode.setDescription('current Mode of refclock')
mbgGPSRefclock2ModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRefclock2ModeVal.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRefclock2ModeVal.setDescription('current Mode of refclock as value')
mbgGPSRef2GpsState = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsState.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef2GpsState.setDescription('current State of GPS refclock ')
mbgGPSRef2GpsStateVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsStateVal.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef2GpsStateVal.setDescription('current State of GPS refclock as value')
mbgGPSRef2GpsPosition = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsPosition.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef2GpsPosition.setDescription('current Position of GPS refclock ')
mbgGPSRef2GpsSatellites = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellites.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellites.setDescription('current Satellites in view and good of GPS refclock ')
mbgGPSRef2GpsSatellitesGood = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellitesGood.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellitesGood.setDescription('current good Satellites of GPS refclock as value')
mbgGPSRef2GpsSatellitesInView = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellitesInView.setStatus('current')
if mibBuilder.loadTexts: mbgGPSRef2GpsSatellitesInView.setDescription('current satellites in view of GPS refclock as value')
mbgSCUType = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUType.setStatus('current')
if mibBuilder.loadTexts: mbgSCUType.setDescription('Type of clock')
mbgSCUTypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTypeVal.setStatus('current')
if mibBuilder.loadTexts: mbgSCUTypeVal.setDescription('Type of Switchcard as value')
mbgSCUMaster = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMaster.setStatus('current')
if mibBuilder.loadTexts: mbgSCUMaster.setDescription('current selected masterclock of switchcard')
mbgSCUMasterVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMasterVal.setStatus('current')
if mibBuilder.loadTexts: mbgSCUMasterVal.setDescription('current selected masterclock of switchcard as value')
mbgSCUMasterselect = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMasterselect.setStatus('current')
if mibBuilder.loadTexts: mbgSCUMasterselect.setDescription('current masterselect mode of GPS Switchcard ')
mbgSCUMasterselectVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUMasterselectVal.setStatus('current')
if mibBuilder.loadTexts: mbgSCUMasterselectVal.setDescription('current masterselect mode of GPS switchcard as value')
mbgSCUTimeSync1 = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTimeSync1.setStatus('current')
if mibBuilder.loadTexts: mbgSCUTimeSync1.setDescription('current time sync status of clock 1')
mbgSCUTimeSync2 = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTimeSync2.setStatus('current')
if mibBuilder.loadTexts: mbgSCUTimeSync2.setDescription('current time sync status of clock 2')
mbgSCUTimelimitError = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUTimelimitError.setStatus('current')
if mibBuilder.loadTexts: mbgSCUTimelimitError.setDescription('current state of time limit alarm (not used)')
mbgSCUDisableOutputs = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUDisableOutputs.setStatus('current')
if mibBuilder.loadTexts: mbgSCUDisableOutputs.setDescription('current state of outputs (0=outputs disabled, 1=outputs enabled)')
mbgSCUSelectedInput = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUSelectedInput.setStatus('current')
if mibBuilder.loadTexts: mbgSCUSelectedInput.setDescription('current selected clock for status queries as a string')
mbgSCUSelectedInputVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUSelectedInputVal.setStatus('current')
if mibBuilder.loadTexts: mbgSCUSelectedInputVal.setDescription('current selected clock for status queries as an integer')
mbgSCUACOMode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUACOMode.setStatus('current')
if mibBuilder.loadTexts: mbgSCUACOMode.setDescription('current state of ACO (access control override)')
mbgSCUPSUStatus = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUPSUStatus.setStatus('current')
if mibBuilder.loadTexts: mbgSCUPSUStatus.setDescription('current status of power supply units as a string')
mbgSCUPSU1Status = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUPSU1Status.setStatus('current')
if mibBuilder.loadTexts: mbgSCUPSU1Status.setDescription('current status of power supply unit 1')
mbgSCUPSU2Status = MibScalar((1, 3, 6, 1, 4, 1, 5597, 10, 4, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgSCUPSU2Status.setStatus('current')
if mibBuilder.loadTexts: mbgSCUPSU2Status.setDescription('current status of power supply unit 2')
mbgGPSTrapColdBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 1))
if mibBuilder.loadTexts: mbgGPSTrapColdBoot.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapColdBoot.setDescription('trap to be sent when Refclock is in Cold Boot mode')
mbgGPSTrapWarmBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 2))
if mibBuilder.loadTexts: mbgGPSTrapWarmBoot.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapWarmBoot.setDescription('trap to be sent when Refclock is in Warm Boot mode')
mbgGPSNavSolved = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 3))
if mibBuilder.loadTexts: mbgGPSNavSolved.setStatus('current')
if mibBuilder.loadTexts: mbgGPSNavSolved.setDescription('trap to be sent when Refclock calculated its actual position')
mbgGPSTrapReceiverNotResponding = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 4))
if mibBuilder.loadTexts: mbgGPSTrapReceiverNotResponding.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapReceiverNotResponding.setDescription('trap to be sent when GPS receiver is not responding ')
mbgGPSTrapReceiverNotSync = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 5))
if mibBuilder.loadTexts: mbgGPSTrapReceiverNotSync.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapReceiverNotSync.setDescription('trap to be sent when GPS receiver is not synchronised ')
mbgGPSTrapAntennaFaulty = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 6))
if mibBuilder.loadTexts: mbgGPSTrapAntennaFaulty.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapAntennaFaulty.setDescription('trap to be sent when connection to antenna is broken ')
mbgGPSTrapAntennaReconnect = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 7))
if mibBuilder.loadTexts: mbgGPSTrapAntennaReconnect.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapAntennaReconnect.setDescription('trap to be sent when antenna has been reconnected ')
mbgGPSTrapLANXPTBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 8))
if mibBuilder.loadTexts: mbgGPSTrapLANXPTBoot.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapLANXPTBoot.setDescription('trap to be sent when LANXPT has been rebooted')
mbgGPSTrapLeapSecondAnnounced = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 9))
if mibBuilder.loadTexts: mbgGPSTrapLeapSecondAnnounced.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapLeapSecondAnnounced.setDescription('trap to be sent when a leap second has been announced ')
mbgGPSTrapMasterclockSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 10))
if mibBuilder.loadTexts: mbgGPSTrapMasterclockSwitchover.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapMasterclockSwitchover.setDescription('trap to be sent when masterclock changes ')
mbgGPSTrapPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 11))
if mibBuilder.loadTexts: mbgGPSTrapPowerSupplyFailure.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapPowerSupplyFailure.setDescription('trap to be sent when a power supply unit fails')
mbgGPSTrapPowerSupplyOK = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 12))
if mibBuilder.loadTexts: mbgGPSTrapPowerSupplyOK.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapPowerSupplyOK.setDescription('trap to be sent when a power supply unit restores operation')
mbgGPSTrapTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 5597, 10, 5, 99))
if mibBuilder.loadTexts: mbgGPSTrapTestNotification.setStatus('current')
if mibBuilder.loadTexts: mbgGPSTrapTestNotification.setDescription('trap to be sent when a test notification has been requested ')
mbgXPTConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 90))
mbgXPTCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 90, 1))
mbgXPTGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 10, 90, 2))
mbgXPTCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5597, 10, 90, 1, 1)).setObjects(("MBG-SNMP-XPT-MIB", "mbgXPTObjectsGroup"), ("MBG-SNMP-XPT-MIB", "mbgXPTTrapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgXPTCompliance = mbgXPTCompliance.setStatus('current')
if mibBuilder.loadTexts: mbgXPTCompliance.setDescription('The compliance statement for SNMP entities which implement version 2\n        of the XPT MIB')
mbgXPTObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5597, 10, 90, 2, 1)).setObjects(("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1Type"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1TypeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1Mode"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1ModeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsState"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsStateVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsPosition"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellites"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellitesGood"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellitesInView"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2Type"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2TypeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2Mode"), ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2ModeVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsState"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsStateVal"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsPosition"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellites"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellitesGood"), ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellitesInView"), ("MBG-SNMP-XPT-MIB", "mbgSCUType"), ("MBG-SNMP-XPT-MIB", "mbgSCUTypeVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUMaster"), ("MBG-SNMP-XPT-MIB", "mbgSCUMasterVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUMasterselect"), ("MBG-SNMP-XPT-MIB", "mbgSCUMasterselectVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUTimeSync1"), ("MBG-SNMP-XPT-MIB", "mbgSCUTimeSync2"), ("MBG-SNMP-XPT-MIB", "mbgSCUTimelimitError"), ("MBG-SNMP-XPT-MIB", "mbgSCUDisableOutputs"), ("MBG-SNMP-XPT-MIB", "mbgSCUSelectedInput"), ("MBG-SNMP-XPT-MIB", "mbgSCUSelectedInputVal"), ("MBG-SNMP-XPT-MIB", "mbgSCUACOMode"), ("MBG-SNMP-XPT-MIB", "mbgSCUPSUStatus"), ("MBG-SNMP-XPT-MIB", "mbgSCUPSU1Status"), ("MBG-SNMP-XPT-MIB", "mbgSCUPSU2Status"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgXPTObjectsGroup = mbgXPTObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: mbgXPTObjectsGroup.setDescription('The collection of objects for the MBG XPT MIB')
mbgXPTTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5597, 10, 90, 2, 2)).setObjects(("MBG-SNMP-XPT-MIB", "mbgGPSTrapColdBoot"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapWarmBoot"), ("MBG-SNMP-XPT-MIB", "mbgGPSNavSolved"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapReceiverNotResponding"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapReceiverNotSync"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapAntennaFaulty"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapAntennaReconnect"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapLANXPTBoot"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapLeapSecondAnnounced"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapMasterclockSwitchover"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapPowerSupplyFailure"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapPowerSupplyOK"), ("MBG-SNMP-XPT-MIB", "mbgGPSTrapTestNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgXPTTrapsGroup = mbgXPTTrapsGroup.setStatus('current')
if mibBuilder.loadTexts: mbgXPTTrapsGroup.setDescription('The collection of traps for the MBG XPT MIB')
mibBuilder.exportSymbols("MBG-SNMP-XPT-MIB", mbgGPSRef1GpsStateVal=mbgGPSRef1GpsStateVal, mbgGPSRefclock2Type=mbgGPSRefclock2Type, mbgGPSRef1GpsState=mbgGPSRef1GpsState, mbgXPTObjectsGroup=mbgXPTObjectsGroup, mbgGPSRef2GpsState=mbgGPSRef2GpsState, mbgSCUTypeVal=mbgSCUTypeVal, mbgSCUMaster=mbgSCUMaster, mbgXPTGroups=mbgXPTGroups, mbgXPTTrapsGroup=mbgXPTTrapsGroup, mbgGPSRef1GpsSatellitesGood=mbgGPSRef1GpsSatellitesGood, mbgSCUType=mbgSCUType, mbgGPSTrapPowerSupplyFailure=mbgGPSTrapPowerSupplyFailure, PYSNMP_MODULE_ID=mbgXPT, mbgXPTCompliances=mbgXPTCompliances, mbgGPSTrapPowerSupplyOK=mbgGPSTrapPowerSupplyOK, mbgGPSRefclock1Mode=mbgGPSRefclock1Mode, mbgGPSTrapAntennaReconnect=mbgGPSTrapAntennaReconnect, mbgGPSRef1GpsSatellites=mbgGPSRef1GpsSatellites, mbgGPSRef2GpsStateVal=mbgGPSRef2GpsStateVal, mbgSCUTimelimitError=mbgSCUTimelimitError, mbgGPSTrapReceiverNotSync=mbgGPSTrapReceiverNotSync, mbgGPSRefclock2ModeVal=mbgGPSRefclock2ModeVal, mbgGPSRef2GpsPosition=mbgGPSRef2GpsPosition, mbgGPSTrapAntennaFaulty=mbgGPSTrapAntennaFaulty, mbgSCU=mbgSCU, mbgXPTTraps=mbgXPTTraps, mbgXPT=mbgXPT, mbgSCUACOMode=mbgSCUACOMode, mbgGPSRefclock1=mbgGPSRefclock1, mbgGPSRefclock2=mbgGPSRefclock2, mbgSCUPSUStatus=mbgSCUPSUStatus, mbgSCUTimeSync1=mbgSCUTimeSync1, mbgSCUMasterVal=mbgSCUMasterVal, mbgSCUTimeSync2=mbgSCUTimeSync2, mbgGPSTrapLeapSecondAnnounced=mbgGPSTrapLeapSecondAnnounced, mbgGPSRefclock1TypeVal=mbgGPSRefclock1TypeVal, mbgXPTCompliance=mbgXPTCompliance, mbgSCUPSU1Status=mbgSCUPSU1Status, mbgSCUMasterselectVal=mbgSCUMasterselectVal, mbgGPSRefclock2Mode=mbgGPSRefclock2Mode, mbgGPSNavSolved=mbgGPSNavSolved, mbgGPSTrapReceiverNotResponding=mbgGPSTrapReceiverNotResponding, mbgGPSRef1GpsSatellitesInView=mbgGPSRef1GpsSatellitesInView, mbgGPSTrapMasterclockSwitchover=mbgGPSTrapMasterclockSwitchover, mbgSCUSelectedInput=mbgSCUSelectedInput, mbgGPSRefclock2TypeVal=mbgGPSRefclock2TypeVal, mbgXPTConformance=mbgXPTConformance, mbgGPSRefclock1ModeVal=mbgGPSRefclock1ModeVal, mbgGPSRef2GpsSatellitesInView=mbgGPSRef2GpsSatellitesInView, mbgGPSTrapLANXPTBoot=mbgGPSTrapLANXPTBoot, mbgGPSTrapTestNotification=mbgGPSTrapTestNotification, mbgGPSRefclock1Type=mbgGPSRefclock1Type, mbgGPSRef2GpsSatellitesGood=mbgGPSRef2GpsSatellitesGood, mbgSCUSelectedInputVal=mbgSCUSelectedInputVal, mbgGPSRef1GpsPosition=mbgGPSRef1GpsPosition, mbgGPSTrapColdBoot=mbgGPSTrapColdBoot, mbgGPSRef2GpsSatellites=mbgGPSRef2GpsSatellites, mbgSCUDisableOutputs=mbgSCUDisableOutputs, mbgSCUPSU2Status=mbgSCUPSU2Status, mbgGPSTrapWarmBoot=mbgGPSTrapWarmBoot, mbgSCUMasterselect=mbgSCUMasterselect)
