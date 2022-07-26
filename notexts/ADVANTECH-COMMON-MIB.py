#
# PySNMP MIB module ADVANTECH-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/advantech/ADVANTECH-COMMON-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:41 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, TimeTicks, Unsigned32, ObjectIdentity, IpAddress, enterprises, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, MibIdentifier, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "TimeTicks", "Unsigned32", "ObjectIdentity", "IpAddress", "enterprises", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "MibIdentifier", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC-v1", "DateAndTime", "DisplayString")
advantech = MibIdentifier((1, 3, 6, 1, 4, 1, 10297))
advantechCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10297, 100))
advantechCommonMIB.setRevisions(('2013-05-25 00:00', '2013-08-28 00:00', '2013-08-29 00:00', '2013-09-06 00:00', '2014-10-13 00:00', '2014-10-22 00:00', '2015-01-06 00:00',))
if mibBuilder.loadTexts: advantechCommonMIB.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: advantechCommonMIB.setOrganization('Advantech eAutomation Group')
atSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 1))
atMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 2))
atPciConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 3))
sysModuleID = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysModuleID.setStatus('mandatory')
sysDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDeviceName.setStatus('current')
sysDescr = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDescr.setStatus('current')
sysImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysImageVersion.setStatus('mandatory')
sysReleaseDate = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysReleaseDate.setStatus('mandatory')
sysFirstBootTime = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFirstBootTime.setStatus('mandatory')
sysBootTime = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysBootTime.setStatus('mandatory')
sysBootCount = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysBootCount.setStatus('mandatory')
snmpTrapSrvObj = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1))
snmpTrapSrvNumber = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapSrvNumber.setStatus('mandatory')
snmpTrapSrvTable = MibTable((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2), )
if mibBuilder.loadTexts: snmpTrapSrvTable.setStatus('mandatory')
snmpTrapSrvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1), ).setIndexNames((0, "ADVANTECH-COMMON-MIB", "snmpTrapSrvIndex"))
if mibBuilder.loadTexts: snmpTrapSrvEntry.setStatus('mandatory')
snmpTrapSrvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapSrvIndex.setStatus('mandatory')
snmpTrapSrvIP = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvIP.setStatus('mandatory')
snmpTrapSrvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvPort.setStatus('mandatory')
snmpTrapSrvAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvAuthentication.setStatus('mandatory')
snmpTrapSrvCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvCommunity.setStatus('mandatory')
snmpTrapVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v1", 1), ("v2c", 2), ("v3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapVersion.setStatus('mandatory')
pciConfigObj = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1))
psNumber = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psNumber.setStatus('current')
pciSlotTable = MibTable((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2), )
if mibBuilder.loadTexts: pciSlotTable.setStatus('current')
pciSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1), ).setIndexNames((0, "ADVANTECH-COMMON-MIB", "psIndex"))
if mibBuilder.loadTexts: pciSlotEntry.setStatus('current')
psIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psIndex.setStatus('mandatory')
psBusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBusIndex.setStatus('mandatory')
psDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceIndex.setStatus('mandatory')
psFunctionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFunctionIndex.setStatus('mandatory')
psDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDisplayName.setStatus('mandatory')
psDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDescr.setStatus('mandatory')
psVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psVendorID.setStatus('mandatory')
psDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceID.setStatus('mandatory')
psSubsysVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSubsysVendorID.setStatus('mandatory')
psSubsysDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSubsysDeviceID.setStatus('mandatory')
psClassCode = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psClassCode.setStatus('mandatory')
psManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psManufacturer.setStatus('current')
psLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psLocation.setStatus('current')
psBaseAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(80, 80)).setFixedLength(80)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBaseAddress.setStatus('mandatory')
psLength = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(80, 80)).setFixedLength(80)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psLength.setStatus('mandatory')
psIRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psIRQ.setStatus('mandatory')
psState = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psState.setStatus('current')
psModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("com", 1), ("can", 2), ("amonet", 3), ("motion", 4), ("wireless", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psModuleType.setStatus('current')
psModulePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psModulePorts.setStatus('current')
mibBuilder.exportSymbols("ADVANTECH-COMMON-MIB", psModuleType=psModuleType, snmpTrapSrvNumber=snmpTrapSrvNumber, psBusIndex=psBusIndex, sysDescr=sysDescr, sysModuleID=sysModuleID, psClassCode=psClassCode, pciSlotTable=pciSlotTable, psVendorID=psVendorID, snmpTrapSrvEntry=snmpTrapSrvEntry, snmpTrapSrvTable=snmpTrapSrvTable, atPciConfig=atPciConfig, sysFirstBootTime=sysFirstBootTime, snmpTrapSrvIP=snmpTrapSrvIP, psIndex=psIndex, psSubsysDeviceID=psSubsysDeviceID, psDeviceIndex=psDeviceIndex, psFunctionIndex=psFunctionIndex, psNumber=psNumber, psModulePorts=psModulePorts, atMgmt=atMgmt, sysBootCount=sysBootCount, psLength=psLength, sysImageVersion=sysImageVersion, sysDeviceName=sysDeviceName, advantech=advantech, psIRQ=psIRQ, atSystem=atSystem, snmpTrapSrvObj=snmpTrapSrvObj, snmpTrapSrvAuthentication=snmpTrapSrvAuthentication, psLocation=psLocation, psState=psState, snmpTrapSrvIndex=snmpTrapSrvIndex, pciSlotEntry=pciSlotEntry, sysReleaseDate=sysReleaseDate, snmpTrapVersion=snmpTrapVersion, pciConfigObj=pciConfigObj, psDescr=psDescr, psDisplayName=psDisplayName, psManufacturer=psManufacturer, sysBootTime=sysBootTime, psSubsysVendorID=psSubsysVendorID, psBaseAddress=psBaseAddress, snmpTrapSrvPort=snmpTrapSrvPort, PYSNMP_MODULE_ID=advantechCommonMIB, snmpTrapSrvCommunity=snmpTrapSrvCommunity, psDeviceID=psDeviceID, advantechCommonMIB=advantechCommonMIB)
