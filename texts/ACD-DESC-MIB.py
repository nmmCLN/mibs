#
# PySNMP MIB module ACD-DESC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-DESC-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:38 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
acdProducts, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdProducts")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Gauge32, Unsigned32, Counter32, TimeTicks, Integer32, NotificationType, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, IpAddress, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Counter32", "TimeTicks", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso")
DisplayString, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "MacAddress")
acdDesc = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 1, 1))
acdDesc.setRevisions(('2010-11-10 01:00', '2010-06-30 01:00', '2009-02-04 01:00', '2008-12-01 01:00', '2006-08-06 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acdDesc.setRevisionsDescriptions(('Fix compliance statement.', 'Revision for 10GE product introduction.', 'Add sysName in power lost (Dying gasp) notification.', 'Add power lost (Dying gasp) notification.', 'Initial version of MIB module ACD-DESC-MIB.',))
if mibBuilder.loadTexts: acdDesc.setLastUpdated('201011100100Z')
if mibBuilder.loadTexts: acdDesc.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: acdDesc.setContactInfo('Accedian Technical Assistance Center\n             Accedian Networks, Inc.\n             4878 Levy, suite 202\n             Saint-Laurent, Quebec Canada H4R 2P1\n             E-mail: support@accedian.com')
if mibBuilder.loadTexts: acdDesc.setDescription('The Accedian Networks device Description MIB.')
acdDescNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 0))
acdDescMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15))
acdDescConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1))
acdDescCommercialName = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCommercialName.setStatus('current')
if mibBuilder.loadTexts: acdDescCommercialName.setDescription('This string is to describe the type of device.')
acdDescMacBaseAddr = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescMacBaseAddr.setStatus('current')
if mibBuilder.loadTexts: acdDescMacBaseAddr.setDescription('This is the Base of the EtherNID MAC addresses.')
acdDescIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescIdentifier.setStatus('current')
if mibBuilder.loadTexts: acdDescIdentifier.setDescription('Identifies the EtherNID on your network.')
acdDescFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: acdDescFirmwareVersion.setDescription('Indicates the version of the firmware currently loaded.')
acdDescHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescHardwareVersion.setStatus('current')
if mibBuilder.loadTexts: acdDescHardwareVersion.setDescription('Indicates the assembly ID of the hardware.')
acdDescSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescSerialNumber.setStatus('current')
if mibBuilder.loadTexts: acdDescSerialNumber.setDescription('Indicates the serial number.')
acdDescCpuUsageCurrent = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 20), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageCurrent.setStatus('current')
if mibBuilder.loadTexts: acdDescCpuUsageCurrent.setDescription('Indicates the current percentage of CPU usage.')
acdDescCpuUsageAverage15 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 21), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage15.setStatus('current')
if mibBuilder.loadTexts: acdDescCpuUsageAverage15.setDescription('Indicates the average percentage of CPU usage over the last 15 seconds.\n         This object range from (0..100).')
acdDescCpuUsageAverage30 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 22), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage30.setStatus('current')
if mibBuilder.loadTexts: acdDescCpuUsageAverage30.setDescription('Indicates the average percentage of CPU usage over the last 30 seconds.\n         This object range from (0..100).')
acdDescCpuUsageAverage60 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 23), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage60.setStatus('current')
if mibBuilder.loadTexts: acdDescCpuUsageAverage60.setDescription('Indicates the average percentage of CPU usage over the last 60 seconds.\n         This object range from (0..100).')
acdDescCpuUsageAverage900 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 24), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage900.setStatus('current')
if mibBuilder.loadTexts: acdDescCpuUsageAverage900.setDescription('Indicates the average percentage of CPU usage over the last 900\n         seconds. This object range from (0..100).')
acdDescConnectorTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10), )
if mibBuilder.loadTexts: acdDescConnectorTable.setStatus('current')
if mibBuilder.loadTexts: acdDescConnectorTable.setDescription('Table of all connectors info')
acdDescConnectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1), ).setIndexNames((0, "ACD-DESC-MIB", "acdDescConnectorID"))
if mibBuilder.loadTexts: acdDescConnectorEntry.setStatus('current')
if mibBuilder.loadTexts: acdDescConnectorEntry.setDescription('This is the product connector definition.')
acdDescConnectorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: acdDescConnectorID.setStatus('current')
if mibBuilder.loadTexts: acdDescConnectorID.setDescription('Unique value for each connector. Starting to one from left to right.')
acdDescConnectorName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescConnectorName.setStatus('current')
if mibBuilder.loadTexts: acdDescConnectorName.setDescription('Identifies the connector on the silkscreen.')
acdDescConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("other", 1), ("rj45", 2), ("rj45S", 3), ("db9", 4), ("bnc", 5), ("fAUI", 6), ("mAUI", 7), ("fiberSC", 8), ("fiberMIC", 9), ("fiberST", 10), ("telco", 11), ("mtrj", 12), ("hssdc", 13), ("fiberLC", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescConnectorType.setStatus('current')
if mibBuilder.loadTexts: acdDescConnectorType.setDescription('Describe the connector type, for instance an RJ-45 or an SFP.')
acdDescConnectorPoESupport = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescConnectorPoESupport.setStatus('current')
if mibBuilder.loadTexts: acdDescConnectorPoESupport.setDescription('This is to indicate if the port support PoE or not.')
acdDescPwrTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11), )
if mibBuilder.loadTexts: acdDescPwrTable.setStatus('current')
if mibBuilder.loadTexts: acdDescPwrTable.setDescription('Table of all Power Supplies')
acdDescPwrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1), ).setIndexNames((0, "ACD-DESC-MIB", "acdDescPwrID"))
if mibBuilder.loadTexts: acdDescPwrEntry.setStatus('current')
if mibBuilder.loadTexts: acdDescPwrEntry.setDescription('This is the product available power supplies information.')
acdDescPwrID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: acdDescPwrID.setStatus('current')
if mibBuilder.loadTexts: acdDescPwrID.setDescription('Unique value for each power supply.')
acdDescPwrName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescPwrName.setStatus('current')
if mibBuilder.loadTexts: acdDescPwrName.setDescription('Identifies the power supply.')
acdDescPwrType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pwrplus5volts", 1), ("pwrminus48volts", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescPwrType.setStatus('current')
if mibBuilder.loadTexts: acdDescPwrType.setDescription('Describe the Power Supply type.')
acdDescPwrPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescPwrPresent.setStatus('current')
if mibBuilder.loadTexts: acdDescPwrPresent.setDescription('This is to indicate if the power supply is present or not.')
acdDescTsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12), )
if mibBuilder.loadTexts: acdDescTsTable.setStatus('current')
if mibBuilder.loadTexts: acdDescTsTable.setDescription('Table of all Teperature Sensors.')
acdDescTsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1), ).setIndexNames((0, "ACD-DESC-MIB", "acdDescTsID"))
if mibBuilder.loadTexts: acdDescTsEntry.setStatus('current')
if mibBuilder.loadTexts: acdDescTsEntry.setDescription('This is the product available Temperature sensor information.')
acdDescTsID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: acdDescTsID.setStatus('current')
if mibBuilder.loadTexts: acdDescTsID.setDescription('Unique value for each Temperature Sensor.')
acdDescTsCurrentTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsCurrentTemp.setStatus('current')
if mibBuilder.loadTexts: acdDescTsCurrentTemp.setDescription('Current temperature in Celsius around the temperature sensor.')
acdDescTsFirstThres = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsFirstThres.setStatus('current')
if mibBuilder.loadTexts: acdDescTsFirstThres.setDescription('Temperature value in Celsius to declare this threshold crossed.')
acdDescTsFisrtThresPass = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsFisrtThresPass.setStatus('current')
if mibBuilder.loadTexts: acdDescTsFisrtThresPass.setDescription('This is to indicate if the temperature cross the first threshold.')
acdDescTsSecondThres = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsSecondThres.setStatus('current')
if mibBuilder.loadTexts: acdDescTsSecondThres.setDescription('Temperature value in Celsius to declare this second threshold crossed.')
acdDescTsSecondThresPass = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsSecondThresPass.setStatus('current')
if mibBuilder.loadTexts: acdDescTsSecondThresPass.setDescription('This is to indicate if the temperature cross the second threshold.')
acdPowerLost = NotificationType((1, 3, 6, 1, 4, 1, 22420, 1, 1, 0, 1)).setObjects(("ACD-DESC-MIB", "acdDescCommercialName"), ("ACD-DESC-MIB", "acdDescMacBaseAddr"), ("ACD-DESC-MIB", "acdDescIdentifier"), ("ACD-DESC-MIB", "acdDescSerialNumber"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: acdPowerLost.setStatus('current')
if mibBuilder.loadTexts: acdPowerLost.setDescription("The SNMP trap that is generated by a unit when it detect a power lost.\n         It's the equivalent of the 802.3ah dying gasp.")
acdDescCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 1))
acdDescGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2))
acdDescGenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 1)).setObjects(("ACD-DESC-MIB", "acdDescCommercialName"), ("ACD-DESC-MIB", "acdDescMacBaseAddr"), ("ACD-DESC-MIB", "acdDescIdentifier"), ("ACD-DESC-MIB", "acdDescFirmwareVersion"), ("ACD-DESC-MIB", "acdDescHardwareVersion"), ("ACD-DESC-MIB", "acdDescSerialNumber"), ("ACD-DESC-MIB", "acdDescCpuUsageCurrent"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage15"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage30"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage60"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage900"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescGenGroup = acdDescGenGroup.setStatus('current')
if mibBuilder.loadTexts: acdDescGenGroup.setDescription('.')
acdDescConnectorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 2)).setObjects(("ACD-DESC-MIB", "acdDescConnectorName"), ("ACD-DESC-MIB", "acdDescConnectorType"), ("ACD-DESC-MIB", "acdDescConnectorPoESupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescConnectorGroup = acdDescConnectorGroup.setStatus('current')
if mibBuilder.loadTexts: acdDescConnectorGroup.setDescription('.')
acdDescPwrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 3)).setObjects(("ACD-DESC-MIB", "acdDescPwrName"), ("ACD-DESC-MIB", "acdDescPwrType"), ("ACD-DESC-MIB", "acdDescPwrPresent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescPwrGroup = acdDescPwrGroup.setStatus('current')
if mibBuilder.loadTexts: acdDescPwrGroup.setDescription('.')
acdDescTsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 4)).setObjects(("ACD-DESC-MIB", "acdDescTsCurrentTemp"), ("ACD-DESC-MIB", "acdDescTsFirstThres"), ("ACD-DESC-MIB", "acdDescTsFisrtThresPass"), ("ACD-DESC-MIB", "acdDescTsSecondThres"), ("ACD-DESC-MIB", "acdDescTsSecondThresPass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescTsGroup = acdDescTsGroup.setStatus('current')
if mibBuilder.loadTexts: acdDescTsGroup.setDescription('.')
acdDescNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 5)).setObjects(("ACD-DESC-MIB", "acdPowerLost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescNotificationsGroup = acdDescNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: acdDescNotificationsGroup.setDescription('Objects for the Notifications group.')
acdAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 1, 1)).setObjects(("ACD-DESC-MIB", "acdDescGenGroup"), ("ACD-DESC-MIB", "acdDescConnectorGroup"), ("ACD-DESC-MIB", "acdDescPwrGroup"), ("ACD-DESC-MIB", "acdDescTsGroup"), ("ACD-DESC-MIB", "acdDescNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmCompliance = acdAlarmCompliance.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCompliance.setDescription('The compliance statement for support of the ACD-DESC-MIB module.')
mibBuilder.exportSymbols("ACD-DESC-MIB", acdDescTsTable=acdDescTsTable, acdDescCpuUsageAverage15=acdDescCpuUsageAverage15, acdDescMacBaseAddr=acdDescMacBaseAddr, acdDescConnectorGroup=acdDescConnectorGroup, acdDescConnectorName=acdDescConnectorName, acdDescCompliances=acdDescCompliances, acdDesc=acdDesc, acdDescConnectorType=acdDescConnectorType, acdDescPwrGroup=acdDescPwrGroup, acdDescTsSecondThresPass=acdDescTsSecondThresPass, acdDescIdentifier=acdDescIdentifier, acdDescPwrPresent=acdDescPwrPresent, acdDescCpuUsageAverage60=acdDescCpuUsageAverage60, acdDescPwrTable=acdDescPwrTable, PYSNMP_MODULE_ID=acdDesc, acdDescTsSecondThres=acdDescTsSecondThres, acdDescPwrEntry=acdDescPwrEntry, acdDescTsID=acdDescTsID, acdDescCpuUsageAverage900=acdDescCpuUsageAverage900, acdDescFirmwareVersion=acdDescFirmwareVersion, acdDescTsFisrtThresPass=acdDescTsFisrtThresPass, acdPowerLost=acdPowerLost, acdDescPwrID=acdDescPwrID, acdDescMIBObjects=acdDescMIBObjects, acdDescGroups=acdDescGroups, acdDescConnectorTable=acdDescConnectorTable, acdDescNotificationsGroup=acdDescNotificationsGroup, acdDescConnectorPoESupport=acdDescConnectorPoESupport, acdDescPwrType=acdDescPwrType, acdDescCpuUsageAverage30=acdDescCpuUsageAverage30, acdAlarmCompliance=acdAlarmCompliance, acdDescNotifications=acdDescNotifications, acdDescCpuUsageCurrent=acdDescCpuUsageCurrent, acdDescTsCurrentTemp=acdDescTsCurrentTemp, acdDescTsGroup=acdDescTsGroup, acdDescGenGroup=acdDescGenGroup, acdDescCommercialName=acdDescCommercialName, acdDescSerialNumber=acdDescSerialNumber, acdDescConnectorID=acdDescConnectorID, acdDescConnectorEntry=acdDescConnectorEntry, acdDescPwrName=acdDescPwrName, acdDescTsEntry=acdDescTsEntry, acdDescTsFirstThres=acdDescTsFirstThres, acdDescHardwareVersion=acdDescHardwareVersion, acdDescConformance=acdDescConformance)
