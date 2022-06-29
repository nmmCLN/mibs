#
# PySNMP MIB module SIAE-SOFT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SOFT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:37 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
alarmTrap, = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap")
equipIpSnmpAgentAddress, = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, ObjectIdentity, ModuleIdentity, iso, TimeTicks, Counter32, MibIdentifier, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "iso", "TimeTicks", "Counter32", "MibIdentifier", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
software = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 7))
software.setRevisions(('2015-03-23 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: software.setLastUpdated('201503230000Z')
if mibBuilder.loadTexts: software.setOrganization('SIAE MICROELETTRONICA spa')
softwareMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareMibVersion.setStatus('current')
softwareEquipmentReleaseBench1 = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench1.setStatus('current')
softwareEquipmentReleaseBench1Status = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notLoaded", 1), ("loaded", 2), ("running", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench1Status.setStatus('current')
softwareEquipmentReleaseBench2 = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench2.setStatus('current')
softwareEquipmentReleaseBench2Status = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notLoaded", 1), ("loaded", 2), ("running", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench2Status.setStatus('current')
softwareIpAddressDwlServer = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareIpAddressDwlServer.setStatus('current')
softwareGosipAddressDwlServer = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareGosipAddressDwlServer.setStatus('current')
softwareDownloadfile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareDownloadfile.setStatus('current')
softwareActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareActionRequest.setStatus('current')
softwareDownloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("downloading", 1), ("completed", 2), ("interrupted", 3), ("perifDownloading", 4), ("configurationDownloading", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareDownloadStatus.setStatus('current')
softwareUnitTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11), )
if mibBuilder.loadTexts: softwareUnitTable.setStatus('current')
softwareUnitRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1), ).setIndexNames((0, "SIAE-SOFT-MIB", "softwareUnitId"), (0, "SIAE-SOFT-MIB", "softwareElementId"))
if mibBuilder.loadTexts: softwareUnitRecord.setStatus('current')
softwareUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitId.setStatus('current')
softwareElementId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareElementId.setStatus('current')
softwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("s-record", 1), ("image-FPGA", 2), ("volatile", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareType.setStatus('current')
softwareUnitReleaseBench1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitReleaseBench1.setStatus('current')
softwareUnitReleaseBench2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitReleaseBench2.setStatus('current')
softwareUnitActualRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitActualRelease.setStatus('current')
softwareDownloadStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 34))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 34))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareDownloadStatusTrapNotification.setStatus('current')
softwareRemoteIpAddressDwlServer = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 13), IpAddress().clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareRemoteIpAddressDwlServer.setStatus('current')
softwareDownloadStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 701)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-SOFT-MIB", "softwareDownloadStatus"))
if mibBuilder.loadTexts: softwareDownloadStatusTrap.setStatus('current')
mibBuilder.exportSymbols("SIAE-SOFT-MIB", softwareEquipmentReleaseBench2=softwareEquipmentReleaseBench2, software=software, softwareEquipmentReleaseBench1=softwareEquipmentReleaseBench1, softwareUnitRecord=softwareUnitRecord, softwareDownloadfile=softwareDownloadfile, softwareRemoteIpAddressDwlServer=softwareRemoteIpAddressDwlServer, softwareElementId=softwareElementId, softwareDownloadStatusTrap=softwareDownloadStatusTrap, softwareUnitId=softwareUnitId, softwareEquipmentReleaseBench1Status=softwareEquipmentReleaseBench1Status, softwareUnitReleaseBench1=softwareUnitReleaseBench1, PYSNMP_MODULE_ID=software, softwareUnitActualRelease=softwareUnitActualRelease, softwareIpAddressDwlServer=softwareIpAddressDwlServer, softwareDownloadStatusTrapNotification=softwareDownloadStatusTrapNotification, softwareEquipmentReleaseBench2Status=softwareEquipmentReleaseBench2Status, softwareGosipAddressDwlServer=softwareGosipAddressDwlServer, softwareUnitTable=softwareUnitTable, softwareUnitReleaseBench2=softwareUnitReleaseBench2, softwareDownloadStatus=softwareDownloadStatus, softwareActionRequest=softwareActionRequest, softwareMibVersion=softwareMibVersion, softwareType=softwareType)
