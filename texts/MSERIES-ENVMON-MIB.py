#
# PySNMP MIB module MSERIES-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-ENVMON-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 16:51:47 2022
# On host fv-az545-99 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, Bits, iso, Unsigned32, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Counter32, Counter64, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Bits", "iso", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
smartEnvMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 1, 4))
smartEnvMon.setRevisions(('2014-02-15 10:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: smartEnvMon.setRevisionsDescriptions(('The initial revision of the MSERIES Enviroment Monitor MIB.',))
if mibBuilder.loadTexts: smartEnvMon.setLastUpdated('201402151034Z')
if mibBuilder.loadTexts: smartEnvMon.setOrganization('SmartOptics')
if mibBuilder.loadTexts: smartEnvMon.setContactInfo('http://www.smartoptics.com')
if mibBuilder.loadTexts: smartEnvMon.setDescription('This is the enterprise specific Enviroment Monitor MIB for SmartOptics M-Series.')
smartEnvMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1))
smartEnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2))
smartEnvMonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1))
smartEnvMonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2))
smartEnvMonTemperatureTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1), )
if mibBuilder.loadTexts: smartEnvMonTemperatureTable.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureTable.setDescription('This table contains one row per temperature sensor.')
smartEnvMonTemperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1), ).setIndexNames((0, "MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"))
if mibBuilder.loadTexts: smartEnvMonTemperatureEntry.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureEntry.setDescription('Information about a particular temperature sensor.')
smartEnvMonTemperatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureIndex.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureIndex.setDescription('An unique index for each temperature sensor.')
smartEnvMonTemperatureDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureDescr.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureDescr.setDescription('The name of the temperature sensor.')
smartEnvMonTemperatureValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 3), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureValue.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureValue.setDescription('The temperature in Celsius measured by the sensor.')
smartEnvMonTemperatureGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1, 1)).setObjects(("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"), ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureDescr"), ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartEnvMonTemperatureGroupV1 = smartEnvMonTemperatureGroupV1.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureGroupV1.setDescription('The EnvMon Temperatue MIB objects v1.')
smartEnvMonBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2, 1)).setObjects(("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartEnvMonBasicComplV1 = smartEnvMonBasicComplV1.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonBasicComplV1.setDescription('Basic implementation requirements for the ENVMON MIB.')
mibBuilder.exportSymbols("MSERIES-ENVMON-MIB", smartEnvMonTemperatureGroupV1=smartEnvMonTemperatureGroupV1, smartEnvMonCompliances=smartEnvMonCompliances, smartEnvMonTemperatureIndex=smartEnvMonTemperatureIndex, smartEnvMonGroups=smartEnvMonGroups, smartEnvMonTemperatureEntry=smartEnvMonTemperatureEntry, smartEnvMonBasicComplV1=smartEnvMonBasicComplV1, smartEnvMonTemperatureDescr=smartEnvMonTemperatureDescr, smartEnvMon=smartEnvMon, smartEnvMonTemperatureTable=smartEnvMonTemperatureTable, smartEnvMonMIBConformance=smartEnvMonMIBConformance, PYSNMP_MODULE_ID=smartEnvMon, smartEnvMonObjects=smartEnvMonObjects, smartEnvMonTemperatureValue=smartEnvMonTemperatureValue)
