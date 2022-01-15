#
# PySNMP MIB module SENSATRONICS-EM1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-EM1
# Produced by pysmi-1.1.8 at Sat Jan 15 20:34:12 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
envMonitors, = mibBuilder.importSymbols("SENSATRONICS-SMI", "envMonitors")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, Gauge32, TimeTicks, ModuleIdentity, iso, Counter32, Counter64, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Gauge32", "TimeTicks", "ModuleIdentity", "iso", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
productEM1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3))
productEM1.setRevisions(('2004-09-13 09:00',))
if mibBuilder.loadTexts: productEM1.setLastUpdated('200409130900Z')
if mibBuilder.loadTexts: productEM1.setOrganization('Sensatronics LLC')
unitInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1))
configData = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2))
sensorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3))
unitName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitName.setStatus('current')
unitModel = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitModel.setStatus('current')
unitManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitManufacturer.setStatus('current')
unitWeb = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(28, 28)).setFixedLength(28)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitWeb.setStatus('current')
unitFirmware = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFirmware.setStatus('current')
unitFWReleaseDate = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(18, 18)).setFixedLength(18)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFWReleaseDate.setStatus('current')
unitSerial = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitSerial.setStatus('current')
unitConfig = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitConfig.setStatus('current')
netInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1))
trapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2))
measurementSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 3))
netMode = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: netMode.setStatus('current')
netIP = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netIP.setStatus('current')
netNM = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netNM.setStatus('current')
netGW = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netGW.setStatus('current')
netHTTPPort = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netHTTPPort.setStatus('current')
managerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2, 1))
unitMode = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitMode.setStatus('current')
managerIP = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIP.setStatus('current')
group1 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1))
group2 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2))
group3 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3))
group4 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4))
group1Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1Name.setStatus('current')
group1TempName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1TempName.setStatus('current')
group1TempDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1TempDataStr.setStatus('current')
group1TempDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1000, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1TempDataInt.setStatus('current')
group1HumidName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1HumidName.setStatus('current')
group1HumidDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1HumidDataStr.setStatus('current')
group1HumidDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1HumidDataInt.setStatus('current')
group1WetName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1WetName.setStatus('current')
group1WetDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1WetDataStr.setStatus('current')
group1WetDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 110))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group1WetDataInt.setStatus('current')
group2Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2Name.setStatus('current')
group2TempName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2TempName.setStatus('current')
group2TempDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2TempDataStr.setStatus('current')
group2TempDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1000, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2TempDataInt.setStatus('current')
group2HumidName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2HumidName.setStatus('current')
group2HumidDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2HumidDataStr.setStatus('current')
group2HumidDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2HumidDataInt.setStatus('current')
group2WetName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2WetName.setStatus('current')
group2WetDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2WetDataStr.setStatus('current')
group2WetDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 110))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group2WetDataInt.setStatus('current')
group3Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3Name.setStatus('current')
group3TempName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3TempName.setStatus('current')
group3TempDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3TempDataStr.setStatus('current')
group3TempDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1000, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3TempDataInt.setStatus('current')
group3HumidName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3HumidName.setStatus('current')
group3HumidDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3HumidDataStr.setStatus('current')
group3HumidDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3HumidDataInt.setStatus('current')
group3WetName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3WetName.setStatus('current')
group3WetDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3WetDataStr.setStatus('current')
group3WetDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 110))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group3WetDataInt.setStatus('current')
group4Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4Name.setStatus('current')
group4TempName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4TempName.setStatus('current')
group4TempDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4TempDataStr.setStatus('current')
group4TempDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1000, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4TempDataInt.setStatus('current')
group4HumidName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4HumidName.setStatus('current')
group4HumidDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4HumidDataStr.setStatus('current')
group4HumidDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4HumidDataInt.setStatus('current')
group4WetName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4WetName.setStatus('current')
group4WetDataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4WetDataStr.setStatus('current')
group4WetDataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 110))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: group4WetDataInt.setStatus('current')
mibBuilder.exportSymbols("SENSATRONICS-EM1", netNM=netNM, group4HumidName=group4HumidName, unitManufacturer=unitManufacturer, unitMode=unitMode, group3TempName=group3TempName, group1WetName=group1WetName, group1WetDataStr=group1WetDataStr, group3WetDataInt=group3WetDataInt, group3HumidDataStr=group3HumidDataStr, group1TempDataInt=group1TempDataInt, group2HumidName=group2HumidName, netIP=netIP, group3WetName=group3WetName, productEM1=productEM1, group4WetDataInt=group4WetDataInt, group3TempDataInt=group3TempDataInt, netHTTPPort=netHTTPPort, netInfo=netInfo, group1Name=group1Name, group1WetDataInt=group1WetDataInt, group1=group1, sensorInfo=sensorInfo, group2TempName=group2TempName, group2Name=group2Name, PYSNMP_MODULE_ID=productEM1, group1TempDataStr=group1TempDataStr, unitModel=unitModel, group2HumidDataStr=group2HumidDataStr, group4TempDataStr=group4TempDataStr, netMode=netMode, group4HumidDataStr=group4HumidDataStr, group4HumidDataInt=group4HumidDataInt, group2=group2, group3Name=group3Name, group3WetDataStr=group3WetDataStr, group1HumidDataStr=group1HumidDataStr, group3TempDataStr=group3TempDataStr, group3HumidName=group3HumidName, group3HumidDataInt=group3HumidDataInt, unitConfig=unitConfig, group4WetDataStr=group4WetDataStr, group2WetName=group2WetName, unitFirmware=unitFirmware, netGW=netGW, group3=group3, group1HumidName=group1HumidName, group2TempDataStr=group2TempDataStr, group2HumidDataInt=group2HumidDataInt, measurementSystem=measurementSystem, trapConfig=trapConfig, group4Name=group4Name, group4WetName=group4WetName, managerConfig=managerConfig, managerIP=managerIP, unitName=unitName, group4=group4, group1TempName=group1TempName, unitInfo=unitInfo, configData=configData, unitFWReleaseDate=unitFWReleaseDate, group1HumidDataInt=group1HumidDataInt, group2WetDataInt=group2WetDataInt, group2TempDataInt=group2TempDataInt, group4TempName=group4TempName, unitSerial=unitSerial, unitWeb=unitWeb, group4TempDataInt=group4TempDataInt, group2WetDataStr=group2WetDataStr)
