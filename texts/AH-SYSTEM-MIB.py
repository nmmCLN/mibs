#
# PySNMP MIB module AH-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:18 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ahProduct, = mibBuilder.importSymbols("AH-SMI-MIB", "ahProduct")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, TimeTicks, iso, Gauge32, Unsigned32, NotificationType, MibIdentifier, IpAddress, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "TimeTicks", "iso", "Gauge32", "Unsigned32", "NotificationType", "MibIdentifier", "IpAddress", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ahSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 2))
if mibBuilder.loadTexts: ahSystem.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: ahSystem.setOrganization('Aerohive Networks, Inc')
if mibBuilder.loadTexts: ahSystem.setContactInfo('info@aerohive.com\n                        1011 McCarthy Boulevard\n                        Milpitas, CA 95035')
if mibBuilder.loadTexts: ahSystem.setDescription('This module contains the MIB definition of \n\t\t\taerohive system related information.')
ahSystemName = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSystemName.setStatus('current')
if mibBuilder.loadTexts: ahSystemName.setDescription('aerohive platform system name')
ahSystemDescription = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSystemDescription.setStatus('current')
if mibBuilder.loadTexts: ahSystemDescription.setDescription('aerohive platform system description')
ahCpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahCpuUtilization.setStatus('current')
if mibBuilder.loadTexts: ahCpuUtilization.setDescription('aerohive platform cpu utilization')
ahMemUtilization = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahMemUtilization.setStatus('current')
if mibBuilder.loadTexts: ahMemUtilization.setDescription('aerohive platform memory utilization')
ahSystemSerial = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSystemSerial.setStatus('current')
if mibBuilder.loadTexts: ahSystemSerial.setDescription('aerohive platform system serial-number')
ahDeviceMode = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahDeviceMode.setStatus('current')
if mibBuilder.loadTexts: ahDeviceMode.setDescription('aerohive device mode type')
ahUpTime = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahUpTime.setStatus('current')
if mibBuilder.loadTexts: ahUpTime.setDescription('aerohive platform up time')
ahHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahHwVersion.setStatus('current')
if mibBuilder.loadTexts: ahHwVersion.setDescription('aerohive platform hardware version')
ahClientCount = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientCount.setStatus('current')
if mibBuilder.loadTexts: ahClientCount.setDescription('the counter of devices connected to aerohive products')
ahEnvirmentTemp = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahEnvirmentTemp.setStatus('current')
if mibBuilder.loadTexts: ahEnvirmentTemp.setDescription('aerohive envirment temp-ditection')
ahEnvirmentFan = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahEnvirmentFan.setStatus('current')
if mibBuilder.loadTexts: ahEnvirmentFan.setDescription('aerohive envirment fan speed,  unit as RPM')
ahFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: ahFirmwareVersion.setDescription('aerohive platform fireware version')
mibBuilder.exportSymbols("AH-SYSTEM-MIB", ahSystemDescription=ahSystemDescription, ahSystem=ahSystem, ahMemUtilization=ahMemUtilization, ahClientCount=ahClientCount, ahFirmwareVersion=ahFirmwareVersion, ahDeviceMode=ahDeviceMode, ahSystemSerial=ahSystemSerial, ahSystemName=ahSystemName, ahCpuUtilization=ahCpuUtilization, ahEnvirmentTemp=ahEnvirmentTemp, ahEnvirmentFan=ahEnvirmentFan, ahUpTime=ahUpTime, PYSNMP_MODULE_ID=ahSystem, ahHwVersion=ahHwVersion)
