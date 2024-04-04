#
# PySNMP MIB module SIAE-SOFT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SOFT-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:16 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
alarmTrap, = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap")
equipIpSnmpAgentAddress, = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, TimeTicks, Counter32, Unsigned32, ModuleIdentity, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "iso")
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
mibBuilder.exportSymbols("SIAE-SOFT-MIB", softwareRemoteIpAddressDwlServer=softwareRemoteIpAddressDwlServer, softwareType=softwareType, softwareGosipAddressDwlServer=softwareGosipAddressDwlServer, softwareUnitActualRelease=softwareUnitActualRelease, softwareDownloadfile=softwareDownloadfile, softwareUnitTable=softwareUnitTable, softwareMibVersion=softwareMibVersion, software=software, softwareUnitReleaseBench1=softwareUnitReleaseBench1, softwareEquipmentReleaseBench2=softwareEquipmentReleaseBench2, softwareIpAddressDwlServer=softwareIpAddressDwlServer, PYSNMP_MODULE_ID=software, softwareUnitId=softwareUnitId, softwareDownloadStatusTrapNotification=softwareDownloadStatusTrapNotification, softwareDownloadStatus=softwareDownloadStatus, softwareEquipmentReleaseBench1Status=softwareEquipmentReleaseBench1Status, softwareDownloadStatusTrap=softwareDownloadStatusTrap, softwareEquipmentReleaseBench2Status=softwareEquipmentReleaseBench2Status, softwareUnitRecord=softwareUnitRecord, softwareElementId=softwareElementId, softwareUnitReleaseBench2=softwareUnitReleaseBench2, softwareActionRequest=softwareActionRequest, softwareEquipmentReleaseBench1=softwareEquipmentReleaseBench1)
