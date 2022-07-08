#
# PySNMP MIB module LIEBERT-GP-SRC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-SRC-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:23:58 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
lgpSrc, liebertSrcModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpSrc", "liebertSrcModuleReg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, IpAddress, Counter64, ModuleIdentity, Gauge32, Bits, Counter32, MibIdentifier, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "IpAddress", "Counter64", "ModuleIdentity", "Gauge32", "Bits", "Counter32", "MibIdentifier", "Integer32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
liebertGlobalProductsSrcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 12, 1))
liebertGlobalProductsSrcModule.setRevisions(('2017-11-10 00:00', '2017-10-16 00:00', '2017-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: liebertGlobalProductsSrcModule.setRevisionsDescriptions(('Added unknown(2147483647) for invalid SRC device readings', 'Added Temperature High/Low Threshold', 'Initial Version',))
if mibBuilder.loadTexts: liebertGlobalProductsSrcModule.setLastUpdated('201711100000Z')
if mibBuilder.loadTexts: liebertGlobalProductsSrcModule.setOrganization('Liebert Corporation')
if mibBuilder.loadTexts: liebertGlobalProductsSrcModule.setContactInfo('Contact:   Technical Support\n\n      Postal:\n      Liebert Corporation\n      1050 Dearborn Drive\n      P.O. Box 29186\n      Columbus OH, 43229\n      US\n\n      Tel: +1 (800) 222-5877\n\n      E-mail: liebert.monitoring@vertivco.com\n      Web:    www.vertivco.com\n\n      Author:  Colby Lin ')
if mibBuilder.loadTexts: liebertGlobalProductsSrcModule.setDescription("The MIB module used to register Liebert POWER related SNMP OIDs.\n\n      Copyright 2008-2008 Liebert Corporation. All rights reserved.\n      Reproduction of this document is authorized on the condition\n      that the forgoing copyright notice is included.\n\n      This Specification is supplied 'AS IS' and Liebert Corporation\n      makes no warranty, either express or implied, as to the use,\n      operation, condition, or performance of the Specification.")
lgpSrcTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1), )
if mibBuilder.loadTexts: lgpSrcTable.setStatus('current')
if mibBuilder.loadTexts: lgpSrcTable.setDescription('A table containing information about SRC device.')
lgpSrcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1), ).setIndexNames((0, "LIEBERT-GP-SRC-MIB", "lgpSrcDevId"))
if mibBuilder.loadTexts: lgpSrcEntry.setStatus('current')
if mibBuilder.loadTexts: lgpSrcEntry.setDescription("This entry defines the contents of the rows for the table\n        'lgpSrcTable'.  A row in this table cannot be created or deleted by\n        SNMP operations on columns of the table.")
lgpSrcDevId = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevId.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevId.setDescription("This value must remain constant between agent initializations.\n            This Device ID is used as an index of the table\n            'lgpSrcTable'.")
lgpSrcDevAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevAddress.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevAddress.setDescription("This value must remain constant between agent initializations.\n            This Device Address is used as an index of the table\n            'lgpSrcTable'.")
lgpSrcDevState = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("standbyOffline", 2), ("unavailableOffline", 3), ("absent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevState.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevState.setDescription('Indicates the current state of SRC device.  The value of this\n            object is set to enabled(1) if the SRC device has been enabled.\n            The value of this object is set to standbyOffline(2) if the SRC\n            device is waiting for an external action to activate it.  The value\n            of this object is set to unavailableOffline(3) if the SRC device is\n            present but cannot be used.  The value of this object is set to\n            absent(4) if the SRC device is not present or not detected.  The\n            value of this object will be one of the valid device state:\n            enabled(1), standbyOffline(2), unavailableOffline(3), or\n            absent(4).')
lgpSrcDevTemperatureDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevTemperatureDegF.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureDegF.setDescription('The measured temperature value in Fahrenheit.  The value of this\n            object is only vaild if the lgpSrcDevState object is set to\n            enabled(1).  The value of this object will be set to\n            unknown(2147483647) if the value of lgpSrcDevState object is set to\n            one of the following values: standbyOffline(2),\n            unavailableOffline(3) or absent(4).')
lgpSrcDevTemperatureSetpointDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureSetpointDegF.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureSetpointDegF.setDescription('The temperature setting in Fahrenheit for SRC.  This setting may\n            or may not be the setting used from control.  Some systems have the\n            capability to dynamically change the control setting based on\n            environmental conditions and/or user configuration.  The value of\n            this object is only vaild if the lgpSrcDevState object is set to\n            enabled(1).  The value of this object will be set to\n            unknown(2147483647) if the value of lgpSrcDevState object is set to\n            one of the following values: standbyOffline(2),\n            unavailableOffline(3) or absent(4).')
lgpSrcDevTemperatureDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevTemperatureDegC.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureDegC.setDescription('The measured temperature value in Celsius.  The value of this\n            object is only vaild if the lgpSrcDevState object is set to\n            enabled(1).  The value of this object will be set to\n            unknown(2147483647) if the value of lgpSrcDevState object is set to\n            one of the following values: standbyOffline(2),\n            unavailableOffline(3) or absent(4).')
lgpSrcDevTemperatureSetpointDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureSetpointDegC.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureSetpointDegC.setDescription('The temperature setting in Celsius for SRC.  This setting may or\n            may not be the setting used from control.  Some systems have the\n            capability to dynamically change the control setting based on\n            environmental conditions and/or user configuration.  The value of\n            this object is only vaild if the lgpSrcDevState object is set to\n            enabled(1).  The value of this object will be set to\n            unknown(2147483647) if the value of lgpSrcDevState object is set to\n            one of the following values: standbyOffline(2),\n            unavailableOffline(3) or absent(4).')
lgpSrcDevFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 2147483647))).clone(namedValues=NamedValues(("low", 1), ("middle", 2), ("high", 3), ("auto", 4), ("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevFanSpeed.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevFanSpeed.setDescription('The present fan speed of the SRC device.  This object will be one\n            of the valid fan speed:  low(1), middle(2), high(3) or auto(4) if\n            the value of lgpSrcDevState object is set to enabled(1).  The value\n            of this object will be set to unknown(2147483647) if the value of\n            lgpSrcDevState object is set to one of the following values:\n            standbyOffline(2), unavailableOffline(3) or absent(4).')
lgpSrcDevPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2147483647))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevPowerStatus.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevPowerStatus.setDescription('The value of this object specifies the power status of SRC device.\n            Power status cannot be configured by an operator.  The value of\n            this object is set to off(0) if the SRC device is powered off.\n            The value of this object is set to on(1) if the SRC device is\n            powered on.  The value of this object will be one of the valid power\n            status: off(0) or on(1) if lgpSrcDevState is enabled(1).  The value\n            of this object will be set to unknown(2147483647) if the value of\n            lgpSrcDevState object is set to one of the following values:\n            standbyOffline(2), unavailableOffline(3) or absent(4).')
lgpSrcDevOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 2147483647))).clone(namedValues=NamedValues(("cooling", 0), ("dehumidify", 1), ("fan", 2), ("ai", 3), ("heating", 4), ("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevOperatingMode.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevOperatingMode.setDescription('The present operating mode of the SRC device.  This object will be\n            one of the valid operating mode: cooling(0), dehumidify(1), fan(2),\n            ai(3) or heating(4) if the value of lgpSrcDevState object is set to\n            enabled(1).  The value of this object will be set to\n            unknown(2147483647) if the value of lgpSrcDevState object is set to\n            one of the following values: standbyOffline(2),\n            unavailableOffline(3) or absent(4).')
lgpSrcDevTemperatureHighThresholdDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Fahrenheit').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureHighThresholdDegF.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureHighThresholdDegF.setDescription("The high temperature notification threshold.  This is the maximum\n            value of 'lgpSrcDevTemperatureDegF' before the agent sends a\n            notification.  The value of this object is only vaild if the\n            lgpSrcDevState object is set to enabled(1).  The value of this\n            object will be set to unknown(2147483647) if the value of\n            lgpSrcDevState object is set to one of the following values:\n            standbyOffline(2), unavailableOffline(3) or absent(4).")
lgpSrcDevTemperatureLowThresholdDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Fahrenheit').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureLowThresholdDegF.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureLowThresholdDegF.setDescription("The low temperature notification threshold.  This is the minimum\n            value of 'lgpSrcDevTemperatureDegF' before the agent sends a\n            notification.  The value of this object is only vaild if the\n            lgpSrcDevState object is set to enabled(1).  The value of this\n            object will be set to unknown(2147483647) if the value of\n            lgpSrcDevState object is set to one of the following values:\n            standbyOffline(2), unavailableOffline(3) or absent(4).")
lgpSrcDevTemperatureHighThresholdDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureHighThresholdDegC.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureHighThresholdDegC.setDescription("The high temperature notification threshold.  This is the maximum\n            value of 'lgpSrcDevTemperatureDegC' before the agent sends a\n            notification.  The value of this object is only vaild if the\n            lgpSrcDevState object is set to enabled(1).  The value of this\n            object will be set to unknown(2147483647) if the value of\n            lgpSrcDevState object is set to one of the following values:\n            standbyOffline(2), unavailableOffline(3) or absent(4).")
lgpSrcDevTemperatureLowThresholdDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureLowThresholdDegC.setStatus('current')
if mibBuilder.loadTexts: lgpSrcDevTemperatureLowThresholdDegC.setDescription("The low temperature notification threshold.  This is the minimum\n            value of 'lgpSrcDevTemperatureDegC' before the agent sends a\n            notification.  The value of this object is only vaild if the\n            lgpSrcDevState object is set to enabled(1).  The value of this\n            object will be set to unknown(2147483647) if the value of\n            lgpSrcDevState object is set to one of the following values:\n            standbyOffline(2), unavailableOffline(3) or absent(4).")
mibBuilder.exportSymbols("LIEBERT-GP-SRC-MIB", PYSNMP_MODULE_ID=liebertGlobalProductsSrcModule, lgpSrcDevTemperatureSetpointDegC=lgpSrcDevTemperatureSetpointDegC, lgpSrcDevTemperatureLowThresholdDegF=lgpSrcDevTemperatureLowThresholdDegF, lgpSrcEntry=lgpSrcEntry, lgpSrcDevTemperatureHighThresholdDegC=lgpSrcDevTemperatureHighThresholdDegC, lgpSrcDevPowerStatus=lgpSrcDevPowerStatus, lgpSrcDevFanSpeed=lgpSrcDevFanSpeed, lgpSrcTable=lgpSrcTable, lgpSrcDevTemperatureHighThresholdDegF=lgpSrcDevTemperatureHighThresholdDegF, lgpSrcDevTemperatureLowThresholdDegC=lgpSrcDevTemperatureLowThresholdDegC, lgpSrcDevTemperatureDegF=lgpSrcDevTemperatureDegF, lgpSrcDevAddress=lgpSrcDevAddress, lgpSrcDevTemperatureSetpointDegF=lgpSrcDevTemperatureSetpointDegF, lgpSrcDevState=lgpSrcDevState, liebertGlobalProductsSrcModule=liebertGlobalProductsSrcModule, lgpSrcDevOperatingMode=lgpSrcDevOperatingMode, lgpSrcDevId=lgpSrcDevId, lgpSrcDevTemperatureDegC=lgpSrcDevTemperatureDegC)
