#
# PySNMP MIB module SIAE-MAB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-MAB-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:34:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter32, NotificationType, Gauge32, MibIdentifier, Bits, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "ModuleIdentity")
TextualConvention, MacAddress, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "RowStatus", "DisplayString")
mabMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 93))
mabMib.setRevisions(('2015-02-17 00:00',))
if mibBuilder.loadTexts: mabMib.setLastUpdated('201502170000Z')
if mibBuilder.loadTexts: mabMib.setOrganization('SIAE MICROELETTRONICA spa')
class MabBwCalculationMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("average", 1), ("min", 2), ("max", 3))

class MabPduCompliance(TextualConvention, Integer32):
    reference = '[1] - MW CAPACITY MANAGEMENT (MCM) - FUNCTIONAL DESCRIPTION This document provides a description of the MW Capacity Management (MCM) feature developed by SIAE MICROELETTRONICA and Cisco. [2] - E-OAM Extensions for Microwave Adaptive Modulation Cisco Document Number EDCS-997459 [3] - Draft revised Recommendation ITU-T G.8021/Y.1341 (for Consent, 5 December 2014) [4] - Draft Amendment 1 to Recommendation ITU-T G.8013/Y.1731(2013) (for Consent, 5 December 2014) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("stdMcmCompliant", 1), ("extMcmCompliant", 2), ("ituG8013Compliant", 3))

class MabSenderOption(TextualConvention, Bits):
    reference = '[3] - Draft revised Recommendation ITU-T G.8021/Y.1341 (for Consent, 5 December 2014) '
    status = 'current'
    namedValues = NamedValues(("enableAlways", 0), ("enableSignalFail", 1))

mabMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mabMibVersion.setStatus('current')
mabSensorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2), )
if mibBuilder.loadTexts: mabSensorTable.setStatus('current')
mabSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1), ).setIndexNames((0, "SIAE-MAB-MIB", "mabSensorIndex"))
if mibBuilder.loadTexts: mabSensorEntry.setStatus('current')
mabSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mabSensorIndex.setStatus('current')
mabSensorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorRowStatus.setStatus('current')
mabSensorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorAdminStatus.setStatus('current')
mabSensorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorIfIndex.setStatus('current')
mabSensorLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorLinkId.setStatus('current')
mabSensorBwMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 6), MabBwCalculationMethod().clone('average')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorBwMode.setStatus('current')
mabSensorHoldoffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorHoldoffTime.setStatus('current')
mabSensorObservationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(10, 10), ValueRangeConstraint(60, 60), )).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorObservationTime.setStatus('current')
mabSensorFastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 59)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorFastTime.setStatus('current')
mabSensorFastCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabSensorFastCount.setStatus('current')
mabSensorStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3), )
if mibBuilder.loadTexts: mabSensorStatusTable.setStatus('current')
mabSensorStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1), ).setIndexNames((0, "SIAE-MAB-MIB", "mabSensorIndex"))
if mibBuilder.loadTexts: mabSensorStatusEntry.setStatus('current')
mabSensorNominalBw = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mabSensorNominalBw.setStatus('current')
mabSensorCurrentBw = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mabSensorCurrentBw.setStatus('current')
mabPduSenderTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4), )
if mibBuilder.loadTexts: mabPduSenderTable.setStatus('current')
mabPduSenderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1), ).setIndexNames((0, "SIAE-MAB-MIB", "mabPduSenderIndex"))
if mibBuilder.loadTexts: mabPduSenderEntry.setStatus('current')
mabPduSenderIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: mabPduSenderIndex.setStatus('current')
mabPduSenderRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderRowStatus.setStatus('current')
mabPduSenderAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderAdminStatus.setStatus('current')
mabPduSenderIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderIfIndex.setStatus('current')
mabPduSenderSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderSensorIndex.setStatus('current')
mabPduSenderVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderVlanId.setStatus('current')
mabPduSenderPcp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderPcp.setStatus('current')
mabPduSenderOamMaintLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderOamMaintLevel.setStatus('current')
mabPduSenderDAType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multicastDA", 1), ("unicastDA", 2))).clone('multicastDA')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderDAType.setStatus('current')
mabPduSenderUnicastDA = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 10), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderUnicastDA.setStatus('current')
mabPduSenderOption = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 11), MabSenderOption()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderOption.setStatus('current')
mabPduSenderPduCompliance = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 12), MabPduCompliance().clone('stdMcmCompliant')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mabPduSenderPduCompliance.setStatus('current')
mibBuilder.exportSymbols("SIAE-MAB-MIB", mabPduSenderTable=mabPduSenderTable, mabSensorAdminStatus=mabSensorAdminStatus, PYSNMP_MODULE_ID=mabMib, mabPduSenderPduCompliance=mabPduSenderPduCompliance, mabSensorIndex=mabSensorIndex, mabPduSenderEntry=mabPduSenderEntry, mabSensorLinkId=mabSensorLinkId, mabSensorHoldoffTime=mabSensorHoldoffTime, mabSensorIfIndex=mabSensorIfIndex, mabPduSenderAdminStatus=mabPduSenderAdminStatus, mabPduSenderIndex=mabPduSenderIndex, mabPduSenderDAType=mabPduSenderDAType, mabSensorEntry=mabSensorEntry, mabPduSenderPcp=mabPduSenderPcp, mabPduSenderSensorIndex=mabPduSenderSensorIndex, mabSensorStatusTable=mabSensorStatusTable, MabBwCalculationMethod=MabBwCalculationMethod, mabPduSenderOamMaintLevel=mabPduSenderOamMaintLevel, mabSensorTable=mabSensorTable, mabSensorRowStatus=mabSensorRowStatus, mabSensorBwMode=mabSensorBwMode, mabMibVersion=mabMibVersion, MabPduCompliance=MabPduCompliance, mabSensorNominalBw=mabSensorNominalBw, mabSensorStatusEntry=mabSensorStatusEntry, mabMib=mabMib, mabPduSenderIfIndex=mabPduSenderIfIndex, MabSenderOption=MabSenderOption, mabSensorFastCount=mabSensorFastCount, mabSensorObservationTime=mabSensorObservationTime, mabSensorFastTime=mabSensorFastTime, mabPduSenderRowStatus=mabPduSenderRowStatus, mabPduSenderOption=mabPduSenderOption, mabSensorCurrentBw=mabSensorCurrentBw, mabPduSenderUnicastDA=mabPduSenderUnicastDA, mabPduSenderVlanId=mabPduSenderVlanId)
