#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 09:58:31 2023
# On host fv-az573-126 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmServiceAffect, slAlarmActive, slAlarmIfIndex, slAlarmType, slAlarmSeverity = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmServiceAffect", "slAlarmActive", "slAlarmIfIndex", "slAlarmType", "slAlarmSeverity")
edfaStatus, edfaIfIndex, edfaOperControlMode = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaStatus", "edfaIfIndex", "edfaOperControlMode")
slEventInventorySerial, slGenEventType, slEventInventoryIfIndex, slEventType, slEventInventoryAction, slGenEventVal, slEventInventoryPartnum, slEventUser, slEventIfIndex, slGenEventIfIndex, slEventVal, slGenEventUser, slEventInventoryType = mibBuilder.importSymbols("SL-EVENT-MIB", "slEventInventorySerial", "slGenEventType", "slEventInventoryIfIndex", "slEventType", "slEventInventoryAction", "slGenEventVal", "slEventInventoryPartnum", "slEventUser", "slEventIfIndex", "slGenEventIfIndex", "slEventVal", "slGenEventUser", "slEventInventoryType")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigActiveConnectionRx, optApsConfigUserWorkingIndex = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx", "optApsConfigUserWorkingIndex")
slTestsIfLoopType, slTestsTrapsLoopbackActive, slTestsIfLoopIfIndex = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopType", "slTestsTrapsLoopbackActive", "slTestsIfLoopIfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, IpAddress, NotificationType, Bits, ModuleIdentity, ObjectIdentity, TimeTicks, Integer32, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "IpAddress", "NotificationType", "Bits", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Integer32", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
slAlarmTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,101)).setObjects(("SL-ALARM-MIB", "slAlarmIfIndex"), ("SL-ALARM-MIB", "slAlarmType"), ("SL-ALARM-MIB", "slAlarmSeverity"), ("SL-ALARM-MIB", "slAlarmServiceAffect"), ("SL-ALARM-MIB", "slAlarmActive"))
slTestsTrapsLoopbackTableChangedV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,122)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
edfaStatusChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,128)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaStatus"))
edfaControlModeChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,129)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaOperControlMode"))
optApsTrapSwitchoverV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,130)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
slEventTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,131)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
tftpStatusChangeTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,132)).setObjects(("RAD-MIB", "tftpStatus"))
slEventInventoryTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,133)).setObjects(("SL-EVENT-MIB", "slEventInventoryIfIndex"), ("SL-EVENT-MIB", "slEventInventoryAction"), ("SL-EVENT-MIB", "slEventInventoryType"), ("SL-EVENT-MIB", "slEventInventorySerial"), ("SL-EVENT-MIB", "slEventInventoryPartnum"))
slGenEventTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,134)).setObjects(("SL-EVENT-MIB", "slGenEventIfIndex"), ("SL-EVENT-MIB", "slGenEventType"), ("SL-EVENT-MIB", "slGenEventVal"), ("SL-EVENT-MIB", "slGenEventUser"))
mibBuilder.exportSymbols("SL-TRAP-MIB", slAlarmTrapV1=slAlarmTrapV1, edfaControlModeChangeV1=edfaControlModeChangeV1, slEventInventoryTrapV1=slEventInventoryTrapV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slEventTrapV1=slEventTrapV1, edfaStatusChangeV1=edfaStatusChangeV1, slGenEventTrapV1=slGenEventTrapV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1)
