#
# PySNMP MIB module MICROSEMI-PDSINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/microsemi/MICROSEMI-PDSINE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:27:43 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ObjectIdentity, TimeTicks, Counter64, Gauge32, IpAddress, Counter32, ModuleIdentity, NotificationType, Integer32, Bits, MibIdentifier, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "TimeTicks", "Counter64", "Gauge32", "IpAddress", "Counter32", "ModuleIdentity", "NotificationType", "Integer32", "Bits", "MibIdentifier", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
polPowerOverLan = ModuleIdentity((1, 3, 6, 1, 4, 1, 7428))
if mibBuilder.loadTexts: polPowerOverLan.setLastUpdated('201111150000Z')
if mibBuilder.loadTexts: polPowerOverLan.setOrganization('')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1))
description = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1))
sysObjectID = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1))
pseDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 2))
portObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1))
mainObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2))
poeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 3))
midspanUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 1))
midspan6portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 2))
midspan6portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 3))
midspan12portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 4))
midspan12portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 5))
midspan24portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 6))
midspan24portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 7))
midspan48portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 8))
midspan48portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 9))
midspan6portHPAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 10))
midspan6portHPACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 11))
midspan12portHPAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 12))
midspan12portHPACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 13))
midspanGigabit6portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 14))
midspanGigabit12portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 15))
midspanGigabit24portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 16))
midspanHiPoEGigabit6portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 17))
midspanHiPoEGigabit12portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 18))
midspanHiPoEGigabit24portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 19))
midspanHiPoEATGigabit6portAC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 20))
midspanHiPoEATGigabit12portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 21))
midspanHiPoEATGigabit24portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 22))
midspan4PairATGigabit6portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 23))
midspan4PairATGigabit12portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 24))
midspanHiPoEATGigabit6portDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 25))
midspanHiPoEATGigabit12portDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 26))
midspanHiPoEATGigabit24portDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 27))
midspan4PairATGigabit24portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 28))
midspanEEPoEGigabit24portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 29))
midspanPoHGigabit6portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 30))
midspanPoHGigabit12portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 31))
midspanPoHGigabit24portACDC = MibIdentifier((1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 32))
portTable = MibTable((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1), )
if mibBuilder.loadTexts: portTable.setStatus('current')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1), ).setIndexNames((0, "MICROSEMI-PDSINE-MIB", "portGroupIndex"), (0, "MICROSEMI-PDSINE-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('current')
portGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: portGroupIndex.setStatus('current')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: portIndex.setStatus('current')
portConsumptionPower = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 3), Gauge32()).setUnits('Watt').setMaxAccess("readonly")
if mibBuilder.loadTexts: portConsumptionPower.setStatus('current')
portMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setUnits('Watt').setMaxAccess("readwrite")
if mibBuilder.loadTexts: portMaxPower.setStatus('current')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twopair", 1), ("fourpair", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portType.setStatus('current')
mainPseTable = MibTable((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1), )
if mibBuilder.loadTexts: mainPseTable.setStatus('current')
mainPseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1), ).setIndexNames((0, "MICROSEMI-PDSINE-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: mainPseEntry.setStatus('current')
mainGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mainGroupIndex.setStatus('current')
mainVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('Volt').setMaxAccess("readonly")
if mibBuilder.loadTexts: mainVoltage.setStatus('current')
mainDetectionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ieee8023afat", 1), ("ieee8023afatandlegacy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mainDetectionMethod.setStatus('current')
mainPowerUsageBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: mainPowerUsageBudget.setStatus('current')
mainPSEMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: mainPSEMaxPower.setStatus('current')
highPowerLegacyPDSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: highPowerLegacyPDSupport.setStatus('current')
highPowerExtendedPortPower = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: highPowerExtendedPortPower.setStatus('current')
powerBackupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standalone", 1), ("powerbackupbyrps", 2), ("powerbackupbymidspan", 3), ("incompatiblepowerbackupdevice", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerBackupStatus.setStatus('current')
internalPowerSourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: internalPowerSourceStatus.setStatus('current')
externalPowerSourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("fail", 2), ("notsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: externalPowerSourceStatus.setStatus('current')
temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 11), Integer32()).setUnits('Degree').setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
temperatureformat = MibTableColumn((1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("celcius", 1), ("fahrenheit", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temperatureformat.setStatus('current')
powerBackupStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 7428, 1, 3, 1)).setObjects(("MICROSEMI-PDSINE-MIB", "powerBackupStatus"))
if mibBuilder.loadTexts: powerBackupStatusNotification.setStatus('current')
internalPowerSourceStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 7428, 1, 3, 2)).setObjects(("MICROSEMI-PDSINE-MIB", "internalPowerSourceStatus"))
if mibBuilder.loadTexts: internalPowerSourceStatusNotification.setStatus('current')
externalPowerSourceStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 7428, 1, 3, 3)).setObjects(("MICROSEMI-PDSINE-MIB", "externalPowerSourceStatus"))
if mibBuilder.loadTexts: externalPowerSourceStatusNotification.setStatus('current')
mibBuilder.exportSymbols("MICROSEMI-PDSINE-MIB", portConsumptionPower=portConsumptionPower, highPowerExtendedPortPower=highPowerExtendedPortPower, midspan6portHPACDC=midspan6portHPACDC, mainVoltage=mainVoltage, mainObjects=mainObjects, internalPowerSourceStatusNotification=internalPowerSourceStatusNotification, midspanHiPoEATGigabit24portACDC=midspanHiPoEATGigabit24portACDC, midspan48portACDC=midspan48portACDC, midspanGigabit24portAC=midspanGigabit24portAC, mainPseEntry=mainPseEntry, portType=portType, midspan48portAC=midspan48portAC, powerBackupStatus=powerBackupStatus, polPowerOverLan=polPowerOverLan, portObjects=portObjects, midspan6portAC=midspan6portAC, externalPowerSourceStatusNotification=externalPowerSourceStatusNotification, mainDetectionMethod=mainDetectionMethod, mainPowerUsageBudget=mainPowerUsageBudget, temperature=temperature, sysObjectID=sysObjectID, midspanUnknown=midspanUnknown, midspan4PairATGigabit12portACDC=midspan4PairATGigabit12portACDC, midspanHiPoEGigabit6portAC=midspanHiPoEGigabit6portAC, portTable=portTable, internalPowerSourceStatus=internalPowerSourceStatus, mainGroupIndex=mainGroupIndex, products=products, midspan6portACDC=midspan6portACDC, midspan12portHPACDC=midspan12portHPACDC, poeNotifications=poeNotifications, midspan6portHPAC=midspan6portHPAC, midspan24portACDC=midspan24portACDC, midspanPoHGigabit12portACDC=midspanPoHGigabit12portACDC, portIndex=portIndex, midspanHiPoEATGigabit12portACDC=midspanHiPoEATGigabit12portACDC, midspan4PairATGigabit6portACDC=midspan4PairATGigabit6portACDC, midspanHiPoEGigabit24portAC=midspanHiPoEGigabit24portAC, midspanGigabit6portAC=midspanGigabit6portAC, midspan12portACDC=midspan12portACDC, midspanPoHGigabit24portACDC=midspanPoHGigabit24portACDC, PYSNMP_MODULE_ID=polPowerOverLan, midspanHiPoEATGigabit6portAC=midspanHiPoEATGigabit6portAC, highPowerLegacyPDSupport=highPowerLegacyPDSupport, midspanGigabit12portAC=midspanGigabit12portAC, midspanPoHGigabit6portACDC=midspanPoHGigabit6portACDC, pseDevice=pseDevice, midspan12portAC=midspan12portAC, externalPowerSourceStatus=externalPowerSourceStatus, mainPSEMaxPower=mainPSEMaxPower, midspanHiPoEATGigabit12portDC=midspanHiPoEATGigabit12portDC, midspan12portHPAC=midspan12portHPAC, temperatureformat=temperatureformat, midspanEEPoEGigabit24portACDC=midspanEEPoEGigabit24portACDC, mainPseTable=mainPseTable, midspanHiPoEATGigabit24portDC=midspanHiPoEATGigabit24portDC, midspanHiPoEATGigabit6portDC=midspanHiPoEATGigabit6portDC, description=description, portMaxPower=portMaxPower, midspanHiPoEGigabit12portAC=midspanHiPoEGigabit12portAC, powerBackupStatusNotification=powerBackupStatusNotification, midspan24portAC=midspan24portAC, midspan4PairATGigabit24portACDC=midspan4PairATGigabit24portACDC, portGroupIndex=portGroupIndex, portEntry=portEntry)
