#
# PySNMP MIB module ADVA-FSPR7-CFM-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/ADVA-FSPR7-CFM-EXTENSION-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:07:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
TrapAlarmSeverity, ServiceImpairment, neEventLogIdentityTranslation, neEventLogTimeStamp, fspR7 = mibBuilder.importSymbols("ADVA-MIB", "TrapAlarmSeverity", "ServiceImpairment", "neEventLogIdentityTranslation", "neEventLogTimeStamp", "fspR7")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
flowEntityIndexEth, flowEntityIndexFlow = mibBuilder.importSymbols("FspR7-LAYER2-MIB", "flowEntityIndexEth", "flowEntityIndexFlow")
dot1agCfmMaIndex, dot1agCfmMepIdentifier, dot1agCfmMdIndex = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMaIndex", "dot1agCfmMepIdentifier", "dot1agCfmMdIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Integer32, iso, Unsigned32, Bits, Counter32, Counter64, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Integer32", "iso", "Unsigned32", "Bits", "Counter32", "Counter64", "Gauge32", "TimeTicks")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
cfmExtensionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6))
cfmExtensionMIB.setRevisions(('2011-02-03 00:00',))
if mibBuilder.loadTexts: cfmExtensionMIB.setLastUpdated('201102030000Z')
if mibBuilder.loadTexts: cfmExtensionMIB.setOrganization('ADVA Optical Networking')
cfmAlarmMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1))
cfmAlarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1))
cfmAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2))
cfmAlarmsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0))
cfmStatusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2))
cfmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1))
class CfmAlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 13000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010))
    namedValues = NamedValues(("undefined", 0), ("cfmOosDisabled", 13000), ("cfmOosManagement", 13001), ("cfmOosMaintenance", 13002), ("cfmOosAins", 13003), ("cfmPriVidNotEqualExtVid", 13004), ("cfmServerSignalFailure", 13005), ("cfmRemoteDefectIndication", 13006), ("cfmCcmMacStatus", 13007), ("cfmCcmError", 13008), ("cfmCcmLost", 13009), ("cfmCcmXConn", 13010))

mepAlarmSeverityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10), )
if mibBuilder.loadTexts: mepAlarmSeverityTable.setStatus('current')
mepAlarmSeverityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1), ).setIndexNames((0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMdIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMaNetIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMepIdentifier"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityType"))
if mibBuilder.loadTexts: mepAlarmSeverityEntry.setStatus('current')
mepAlarmSeverityMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mepAlarmSeverityMdIndex.setStatus('current')
mepAlarmSeverityMaNetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 2), Unsigned32())
if mibBuilder.loadTexts: mepAlarmSeverityMaNetIndex.setStatus('current')
mepAlarmSeverityMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 3), Unsigned32())
if mibBuilder.loadTexts: mepAlarmSeverityMepIdentifier.setStatus('current')
mepAlarmSeverityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 4), CfmAlarmType())
if mibBuilder.loadTexts: mepAlarmSeverityType.setStatus('current')
mepAlarmSeverityValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 5), TrapAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepAlarmSeverityValue.setStatus('current')
mepAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11), )
if mibBuilder.loadTexts: mepAlarmTable.setStatus('current')
mepAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1), ).setIndexNames((0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMdIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMaNetIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMepIdentifier"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmType"))
if mibBuilder.loadTexts: mepAlarmEntry.setStatus('current')
mepAlarmMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mepAlarmMdIndex.setStatus('current')
mepAlarmMaNetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 2), Unsigned32())
if mibBuilder.loadTexts: mepAlarmMaNetIndex.setStatus('current')
mepAlarmMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 3), Unsigned32())
if mibBuilder.loadTexts: mepAlarmMepIdentifier.setStatus('current')
mepAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 4), CfmAlarmType())
if mibBuilder.loadTexts: mepAlarmType.setStatus('current')
mepAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 5), TrapAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mepAlarmSeverity.setStatus('current')
mepAlarmAffect = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 6), ServiceImpairment()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mepAlarmAffect.setStatus('current')
mepAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mepAlarmTimeStamp.setStatus('current')
alarmCfmOosDisabled = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13000)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosDisabled.setStatus('current')
alarmCfmOosManagement = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13001)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosManagement.setStatus('current')
alarmCfmOosMaintenance = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13002)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosMaintenance.setStatus('current')
alarmCfmOosAins = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13003)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosAins.setStatus('current')
alarmCfmPriVidNotEqualExtVid = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13004)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmPriVidNotEqualExtVid.setStatus('current')
alarmCfmServerSignalFailure = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13005)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmServerSignalFailure.setStatus('current')
alarmCfmRemoteDefectIndication = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13006)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmRemoteDefectIndication.setStatus('current')
alarmCfmCcmMacStatus = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13007)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmMacStatus.setStatus('current')
alarmCfmCcmError = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13008)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmError.setStatus('current')
alarmCfmCcmLost = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13009)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmLost.setStatus('current')
alarmCfmCcmXConn = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13010)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmXConn.setStatus('current')
mepOnFlowTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1), )
if mibBuilder.loadTexts: mepOnFlowTable.setStatus('current')
mepOnFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1, 1), ).setIndexNames((0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"), (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: mepOnFlowEntry.setStatus('current')
mepOnFlowMepString = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mepOnFlowMepString.setStatus('current')
cfmExtensionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2))
cfmExtensionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1))
cfmExtensionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2))
cfmExtensionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "cfmExtensionObjectGroup"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "cfmExtensionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtensionMIBCompliance = cfmExtensionMIBCompliance.setStatus('current')
cfmExtensionObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2, 1)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityValue"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtensionObjectGroup = cfmExtensionObjectGroup.setStatus('current')
cfmExtensionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2, 2)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosDisabled"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosManagement"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosMaintenance"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosAins"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmPriVidNotEqualExtVid"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmServerSignalFailure"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmRemoteDefectIndication"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmMacStatus"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmError"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmLost"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmXConn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtensionNotificationGroup = cfmExtensionNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADVA-FSPR7-CFM-EXTENSION-MIB", cfmExtensionMIB=cfmExtensionMIB, cfmExtensionMIBConformance=cfmExtensionMIBConformance, alarmCfmOosMaintenance=alarmCfmOosMaintenance, alarmCfmCcmMacStatus=alarmCfmCcmMacStatus, mepAlarmSeverity=mepAlarmSeverity, cfmAlarmMIB=cfmAlarmMIB, alarmCfmCcmXConn=alarmCfmCcmXConn, cfmAlarmObjects=cfmAlarmObjects, cfmAlarms=cfmAlarms, mepAlarmAffect=mepAlarmAffect, mepAlarmSeverityType=mepAlarmSeverityType, CfmAlarmType=CfmAlarmType, cfmStatusMIB=cfmStatusMIB, mepAlarmSeverityValue=mepAlarmSeverityValue, cfmExtensionObjectGroup=cfmExtensionObjectGroup, mepAlarmMaNetIndex=mepAlarmMaNetIndex, alarmCfmServerSignalFailure=alarmCfmServerSignalFailure, cfmExtensionMIBGroups=cfmExtensionMIBGroups, mepAlarmSeverityMdIndex=mepAlarmSeverityMdIndex, PYSNMP_MODULE_ID=cfmExtensionMIB, mepAlarmSeverityTable=mepAlarmSeverityTable, alarmCfmOosDisabled=alarmCfmOosDisabled, alarmCfmOosAins=alarmCfmOosAins, cfmExtensionMIBCompliances=cfmExtensionMIBCompliances, cfmExtensionNotificationGroup=cfmExtensionNotificationGroup, alarmCfmPriVidNotEqualExtVid=alarmCfmPriVidNotEqualExtVid, cfmStatus=cfmStatus, mepAlarmSeverityEntry=mepAlarmSeverityEntry, mepOnFlowTable=mepOnFlowTable, cfmExtensionMIBCompliance=cfmExtensionMIBCompliance, mepAlarmType=mepAlarmType, mepAlarmTable=mepAlarmTable, alarmCfmRemoteDefectIndication=alarmCfmRemoteDefectIndication, alarmCfmCcmError=alarmCfmCcmError, mepAlarmSeverityMepIdentifier=mepAlarmSeverityMepIdentifier, alarmCfmOosManagement=alarmCfmOosManagement, alarmCfmCcmLost=alarmCfmCcmLost, mepAlarmSeverityMaNetIndex=mepAlarmSeverityMaNetIndex, mepOnFlowEntry=mepOnFlowEntry, cfmAlarmsPrefix=cfmAlarmsPrefix, mepAlarmEntry=mepAlarmEntry, mepAlarmMepIdentifier=mepAlarmMepIdentifier, mepOnFlowMepString=mepOnFlowMepString, mepAlarmTimeStamp=mepAlarmTimeStamp, mepAlarmMdIndex=mepAlarmMdIndex)
