#
# PySNMP MIB module SIAE-ECFM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-ECFM-EXT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:39 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, TimeTicks, iso, Counter64, Integer32, Unsigned32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "TimeTicks", "iso", "Counter64", "Integer32", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
siaeEcfmExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 94))
siaeEcfmExtMib.setRevisions(('2016-07-25 00:00', '2015-06-26 00:00', '2015-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: siaeEcfmExtMib.setRevisionsDescriptions(('MIB version 01.00.02\n             Added defLckConditionAlarm and mepLckConditionAlarmsSeverityCode\n            ', 'MIB version 01.00.01\n             Changed siaeMepAlarms8021agTable description.\n             Added siaeMepAlarmsY1731Table and Y1731 alarms severity code.\n            ', 'Initial version 01.00.00.\n            ',))
if mibBuilder.loadTexts: siaeEcfmExtMib.setLastUpdated('201607250000Z')
if mibBuilder.loadTexts: siaeEcfmExtMib.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: siaeEcfmExtMib.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail:  help@siaemic.com\n            ')
if mibBuilder.loadTexts: siaeEcfmExtMib.setDescription('This mib provides alarm objects to interface\n             ECFM MEP alarm condition to SIAE-ALARM module\n            ')
siaeEcfmExtMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: siaeEcfmExtMibVersion.setStatus('current')
if mibBuilder.loadTexts: siaeEcfmExtMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
siaeMepAlarms8021agTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2), )
if mibBuilder.loadTexts: siaeMepAlarms8021agTable.setStatus('current')
if mibBuilder.loadTexts: siaeMepAlarms8021agTable.setDescription('MEPs for the corresponding index (MdIndex, MaIndex and MepIdentifier).')
siaeMepAlarms8021agEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1), ).setIndexNames((0, "SIAE-ECFM-EXT-MIB", "defMIEcfmContextId"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMdIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMaIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMepIdentifier"))
if mibBuilder.loadTexts: siaeMepAlarms8021agEntry.setStatus('current')
if mibBuilder.loadTexts: siaeMepAlarms8021agEntry.setDescription('The  MEP alarm entry')
defMIEcfmContextId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmContextId.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmContextId.setDescription('context ID: as fsMIEcfmContextId of ARICENT-ECFM-MI-MIB')
defMIEcfmMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmMdIndex.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmMdIndex.setDescription('Mep Maintenance Domanin: as fsMIEcfmMdIndex of ARICENT-ECFM-MI-MIB')
defMIEcfmMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmMaIndex.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmMaIndex.setDescription('Mep Maintenance Association: as fsMIEcfmMaIndex of ARICENT-ECFM-MI-MIB')
defMIEcfmMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 4), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmMepIdentifier.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmMepIdentifier.setDescription('Mep Identifier: as fsMIEcfmIdentifier of ARICENT-ECFM-MI-MIB')
defRdiCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defRdiCcmAlarm.setStatus('current')
if mibBuilder.loadTexts: defRdiCcmAlarm.setDescription('A remote MEP is reported the RDI bit in its last CCM.\n         According to fsMIEcfmMepDefects (bit 1) in fsMIEcfmMepTable\n         -- ARICENT-ECFM-MI-MIB')
defMacStatusAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defMacStatusAlarm.setStatus('current')
if mibBuilder.loadTexts: defMacStatusAlarm.setDescription('Either some remote MEP is reporting its\n         Interface Status TLV as not isUp, or all remote\n         MEPs are reporting a Port Status TLV that\n         contains some value other than psUp.\n         According to fsMIEcfmMepDefects (bit 2) in fsMIEcfmMepTable\n         -- ARICENT-ECFM-MI-MIB')
defRemoteCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defRemoteCcmAlarm.setStatus('current')
if mibBuilder.loadTexts: defRemoteCcmAlarm.setDescription('The MEP is not receiving valid CCMs from at\n         least one of the remote MEPs.\n         According to fsMIEcfmMepDefects (bit 3) in fsMIEcfmMepTable\n         -- ARICENT-ECFM-MI-MIB')
defErrorCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defErrorCcmAlarm.setStatus('current')
if mibBuilder.loadTexts: defErrorCcmAlarm.setDescription('The MEP has received at least one invalid CCM\n         whose CCM Interval has not yet timed out.\n         According to fsMIEcfmMepDefects (bit 4) in fsMIEcfmMepTable\n         -- ARICENT-ECFM-MI-MIB')
defXconCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defXconCcmAlarm.setStatus('current')
if mibBuilder.loadTexts: defXconCcmAlarm.setDescription('The MEP has received at least one CCM from\n         either another MAID or a lower MD Level whose\n         CCM Interval has not yet timed out.\n         According to fsMIEcfmMepDefects (bit 5) in fsMIEcfmMepTable\n         -- ARICENT-ECFM-MI-MIB')
siaeMepAlarmsY1731Table = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3), )
if mibBuilder.loadTexts: siaeMepAlarmsY1731Table.setStatus('current')
if mibBuilder.loadTexts: siaeMepAlarmsY1731Table.setDescription('MEPs for the corresponding index (MegIndex, MeIndex and MepIdentifier).')
siaeMepAlarmsY1731Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1), ).setIndexNames((0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731ContextId"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MegIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MeIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MepIdentifier"))
if mibBuilder.loadTexts: siaeMepAlarmsY1731Entry.setStatus('current')
if mibBuilder.loadTexts: siaeMepAlarmsY1731Entry.setDescription('The  MEP alarm entry')
defMIEcfmY1731ContextId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731ContextId.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmY1731ContextId.setDescription('Context ID: as fsMIY1731ContextId of ARICENT-ECFM-Y1731-MI-MIB')
defMIEcfmY1731MegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731MegIndex.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmY1731MegIndex.setDescription('Mep Maintenance Entity Group: as fsMIY1731MegIndex of ARICENT-ECFM-Y1731-MI-MIB')
defMIEcfmY1731MeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731MeIndex.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmY1731MeIndex.setDescription('Mep Maintenance Entity: as fsMIY1731MeIndex of ARICENT-ECFM-Y1731-MI-MIB')
defMIEcfmY1731MepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 4), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731MepIdentifier.setStatus('current')
if mibBuilder.loadTexts: defMIEcfmY1731MepIdentifier.setDescription('Mep Identifier: as fsMIEcfmIdentifier of ARICENT-ECFM-Y1731-MI-MIB')
defRdiConditionAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defRdiConditionAlarm.setStatus('current')
if mibBuilder.loadTexts: defRdiConditionAlarm.setDescription('A MEP detects RDI with it receives a CCM frame with the RDI field set.\n         According to fsMI1731ErrorLogType (bit 1) in fsMI1731ErrorLogTable\n         -- ARICENT-ECFM-1731-MI-MIB')
defLossOfContinuityAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defLossOfContinuityAlarm.setStatus('current')
if mibBuilder.loadTexts: defLossOfContinuityAlarm.setDescription('A MEP detects LOC with a peer MEP when it stops receiving CCM frames\n         from that peer ME.\n         According to fsMI1731ErrorLogType (bit 2) in fsMI1731ErrorLogTable\n         -- ARICENT-ECFM-1731-MI-MIB')
defUnexpectedPeriodAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defUnexpectedPeriodAlarm.setStatus('current')
if mibBuilder.loadTexts: defUnexpectedPeriodAlarm.setDescription("A MEP detects UnexpectedPeriod with it receives a CCM frame with a\n         correct MEG Level (i.e.MEG Level equal to the MEPs own MEG Level),\n         a correct MEG Id, a correct MEP ID, but with Period field value \n         different than the MEP's own CCM transmission period.\n         According to fsMI1731ErrorLogType (bit 3) in fsMI1731ErrorLogTable\n         -- ARICENT-ECFM-1731-MI-MIB")
defUnexpectedMepAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defUnexpectedMepAlarm.setStatus('current')
if mibBuilder.loadTexts: defUnexpectedMepAlarm.setDescription("A MEP detects UnexpectedMEP when it receives a CCM frame with a correct\n         MEG Level (i.e.MEG Level equal to the MEPs own MEG Level), a correct\n         MEG ID but an unexpected MEP ID which includes the MEP's own MEP ID.\n         According to fsMI1731ErrorLogType (bit 4) in fsMI1731ErrorLogTable\n         -- ARICENT-ECFM-1731-MI-MIB")
defMisMergeAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defMisMergeAlarm.setStatus('current')
if mibBuilder.loadTexts: defMisMergeAlarm.setDescription("A MEP detects Mismerge when it receives a CCM frame with a correct\n         MEG Level(i.e. MEG Level same as MEPs own MEG Level) but incorrect\n         MEG ID (indicating that frames from a different service instance are\n         merged with the service instance represented by the MEP's own MEG ID).                                                                                                                                                                                                                                \n         According to fsMI1731ErrorLogType (bit 5) in fsMI1731ErrorLogTable\n         -- ARICENT-ECFM-1731-MI-MIB")
defUnexpectedMegLevelAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defUnexpectedMegLevelAlarm.setStatus('current')
if mibBuilder.loadTexts: defUnexpectedMegLevelAlarm.setDescription('A MEP detects UnexpectedMEGLevel with it receives a CCM frame with\n         incorrect MEG Level.\n         Incorrect MEG Level is less than the MEPs own MEG Level.\n         According to fsMI1731ErrorLogType (bit 6) in fsMI1731ErrorLogTable\n         -- ARICENT-ECFM-1731-MI-MIB')
defAisConditionAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defAisConditionAlarm.setStatus('current')
if mibBuilder.loadTexts: defAisConditionAlarm.setDescription('A MEP detects AIS when it receives an AIS frame.\n         Such a defect is caused by detection of signal fail condition at a \n         server layer or reception of AIS at a server (sub) layer MEP in the\n         case that the MEP does not use ETH-CC function.\n         According to fsMI1731ErrorLogType (bit 10) in fsMI1731ErrorLogTable\n         -- ARICENT-ECFM-1731-MI-MIB')
defLckConditionAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 12), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defLckConditionAlarm.setStatus('current')
if mibBuilder.loadTexts: defLckConditionAlarm.setDescription('To communicate the administrative locking of\n         a server (sub) layer MEP and consequential interruption of data traffic\n         forwarding towards the MEP expecting this traffic. \n         It allows a MEP receiving frames with ETH-LCK information to differentiate\n         between a defect condition and an administrative locking action at the \n         server (sub) layer MEP.')
mepRdiCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 4), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepRdiCcmAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepRdiCcmAlarmsSeverityCode.setDescription('Defines the severity associated to the defRdiCcmAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepMacStatusAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepMacStatusAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepMacStatusAlarmsSeverityCode.setDescription('Defines the severity associated to the defMacStatusAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepRemoteCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepRemoteCcmAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepRemoteCcmAlarmsSeverityCode.setDescription('Defines the severity associated to the defRemoteCcmAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepErrorCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepErrorCcmAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepErrorCcmAlarmsSeverityCode.setDescription('Defines the severity associated to the defErrorCcmAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepXconCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepXconCcmAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepXconCcmAlarmsSeverityCode.setDescription('Defines the severity associated to the defXconCcmAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepRdiConditionAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 9), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepRdiConditionAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepRdiConditionAlarmsSeverityCode.setDescription('Defines the severity associated to the defRdiConditionAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepLossOfContinuityAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 10), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepLossOfContinuityAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepLossOfContinuityAlarmsSeverityCode.setDescription('Defines the severity associated to the defLossOfContinuityAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepUnexpectedPeriodAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 11), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepUnexpectedPeriodAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepUnexpectedPeriodAlarmsSeverityCode.setDescription('Defines the severity associated to the defUnexpectedPeriodAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepUnexpectedMepAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 12), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepUnexpectedMepAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepUnexpectedMepAlarmsSeverityCode.setDescription('Defines the severity associated to the defUnexpectedMepAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepMisMergeAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 13), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepMisMergeAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepMisMergeAlarmsSeverityCode.setDescription('Defines the severity associated to the defMisMergeAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepUnexpectedMegLevelAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 14), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepUnexpectedMegLevelAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepUnexpectedMegLevelAlarmsSeverityCode.setDescription('Defines the severity associated to the defUnexpectedMegLevelAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepAisConditionAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 15), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepAisConditionAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepAisConditionAlarmsSeverityCode.setDescription('Defines the severity associated to the defAisConditionAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mepLckConditionAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 16), AlarmSeverityCode().clone('statusTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepLckConditionAlarmsSeverityCode.setStatus('current')
if mibBuilder.loadTexts: mepLckConditionAlarmsSeverityCode.setDescription('Defines the severity associated to the defLckConditionAlarm\n         and enables/disables the trap generation on status change event.\n        ')
mibBuilder.exportSymbols("SIAE-ECFM-EXT-MIB", defErrorCcmAlarm=defErrorCcmAlarm, siaeMepAlarmsY1731Entry=siaeMepAlarmsY1731Entry, defMIEcfmMaIndex=defMIEcfmMaIndex, defMIEcfmY1731MepIdentifier=defMIEcfmY1731MepIdentifier, mepUnexpectedPeriodAlarmsSeverityCode=mepUnexpectedPeriodAlarmsSeverityCode, mepMacStatusAlarmsSeverityCode=mepMacStatusAlarmsSeverityCode, mepUnexpectedMepAlarmsSeverityCode=mepUnexpectedMepAlarmsSeverityCode, mepMisMergeAlarmsSeverityCode=mepMisMergeAlarmsSeverityCode, defRemoteCcmAlarm=defRemoteCcmAlarm, defUnexpectedMegLevelAlarm=defUnexpectedMegLevelAlarm, defMIEcfmY1731MeIndex=defMIEcfmY1731MeIndex, siaeMepAlarmsY1731Table=siaeMepAlarmsY1731Table, defUnexpectedPeriodAlarm=defUnexpectedPeriodAlarm, mepRdiCcmAlarmsSeverityCode=mepRdiCcmAlarmsSeverityCode, mepXconCcmAlarmsSeverityCode=mepXconCcmAlarmsSeverityCode, mepRdiConditionAlarmsSeverityCode=mepRdiConditionAlarmsSeverityCode, mepAisConditionAlarmsSeverityCode=mepAisConditionAlarmsSeverityCode, defLossOfContinuityAlarm=defLossOfContinuityAlarm, mepLckConditionAlarmsSeverityCode=mepLckConditionAlarmsSeverityCode, defRdiConditionAlarm=defRdiConditionAlarm, defRdiCcmAlarm=defRdiCcmAlarm, siaeMepAlarms8021agEntry=siaeMepAlarms8021agEntry, mepRemoteCcmAlarmsSeverityCode=mepRemoteCcmAlarmsSeverityCode, defUnexpectedMepAlarm=defUnexpectedMepAlarm, siaeMepAlarms8021agTable=siaeMepAlarms8021agTable, defMIEcfmContextId=defMIEcfmContextId, mepErrorCcmAlarmsSeverityCode=mepErrorCcmAlarmsSeverityCode, PYSNMP_MODULE_ID=siaeEcfmExtMib, mepLossOfContinuityAlarmsSeverityCode=mepLossOfContinuityAlarmsSeverityCode, defMIEcfmY1731ContextId=defMIEcfmY1731ContextId, mepUnexpectedMegLevelAlarmsSeverityCode=mepUnexpectedMegLevelAlarmsSeverityCode, siaeEcfmExtMib=siaeEcfmExtMib, defXconCcmAlarm=defXconCcmAlarm, defLckConditionAlarm=defLckConditionAlarm, defAisConditionAlarm=defAisConditionAlarm, defMacStatusAlarm=defMacStatusAlarm, defMIEcfmY1731MegIndex=defMIEcfmY1731MegIndex, defMIEcfmMdIndex=defMIEcfmMdIndex, siaeEcfmExtMibVersion=siaeEcfmExtMibVersion, defMIEcfmMepIdentifier=defMIEcfmMepIdentifier, defMisMergeAlarm=defMisMergeAlarm)
