#
# PySNMP MIB module SYNOLOGY-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:28:44 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, iso, enterprises, Counter32, NotificationType, Integer32, Bits, IpAddress, ModuleIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "iso", "enterprises", "Counter32", "NotificationType", "Integer32", "Bits", "IpAddress", "ModuleIdentity", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 1))
synoSystem.setRevisions(('2013-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synoSystem.setRevisionsDescriptions(('Second draft.',))
if mibBuilder.loadTexts: synoSystem.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoSystem.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synoSystem.setContactInfo('postal:   Jay Pan\n          email:    jaypan@synology.com')
if mibBuilder.loadTexts: synoSystem.setDescription('Characteristics of the system information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
systemStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatus.setStatus('current')
if mibBuilder.loadTexts: systemStatus.setDescription('Synology system status\n\t Each meanings of status represented describe below.\n\t Normal(1): System functionals normally.\n\t Failed(2): Volume has crashed.\n\t')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('Synology system temperature\n\t The temperature of Disk Station uses Celsius degree.\n\t')
powerStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatus.setDescription('Synology power status\n\t Each meanings of status represented describe below.\n\t Normal(1): All power supplies functional normally.\n\t Failed(2): One of power supply has failed.\n\t')
fan = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 4))
systemFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemFanStatus.setStatus('current')
if mibBuilder.loadTexts: systemFanStatus.setDescription('Synology system fan status\n\t Each meanings of status represented describe below.\n\t Normal(1): All Internal fans functional normally.\n\t Failed(2): One of internal fan stopped.\n\t')
cpuFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuFanStatus.setStatus('current')
if mibBuilder.loadTexts: cpuFanStatus.setDescription('Synology cpu fan status\n\t Each meanings of status represented describe below.\n\t Normal(1): All CPU fans functional normally.\n\t Failed(2): One of CPU fan stopped.\n\t')
dsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 5))
modelName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modelName.setStatus('current')
if mibBuilder.loadTexts: modelName.setDescription('The Model name of this NAS')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('The serial number of this NAS')
version = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
if mibBuilder.loadTexts: version.setDescription('The version of this DSM')
upgradeAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upgradeAvailable.setStatus('current')
if mibBuilder.loadTexts: upgradeAvailable.setDescription('This oid is for checking whether there is a latest DSM can be upgraded.\n\t Available(1): There is version ready for download.\n\t Unavailable(2): The DSM is latest version.\n\t Connecting(3): Checking for the latest DSM.\n\t Disconnected(4): Failed to connect to server.\n\t Others(5): If DSM is upgrading or downloading, the status will show others.')
systemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6))
systemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6, 1))
systemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6, 2))
systemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 1, 6, 1, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemCompliance = systemCompliance.setStatus('current')
if mibBuilder.loadTexts: systemCompliance.setDescription('The compliance statement for synoSystem entities which\n            implement the SYNOLOGY SYSTEM MIB.')
systemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 1, 6, 2, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemStatus"), ("SYNOLOGY-SYSTEM-MIB", "temperature"), ("SYNOLOGY-SYSTEM-MIB", "powerStatus"), ("SYNOLOGY-SYSTEM-MIB", "systemFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "cpuFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "modelName"), ("SYNOLOGY-SYSTEM-MIB", "serialNumber"), ("SYNOLOGY-SYSTEM-MIB", "version"), ("SYNOLOGY-SYSTEM-MIB", "upgradeAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemGroup = systemGroup.setStatus('current')
if mibBuilder.loadTexts: systemGroup.setDescription('A collection of objects providing basic information\n             of an synology system entity.')
mibBuilder.exportSymbols("SYNOLOGY-SYSTEM-MIB", serialNumber=serialNumber, PYSNMP_MODULE_ID=synoSystem, systemConformance=systemConformance, temperature=temperature, systemGroup=systemGroup, systemFanStatus=systemFanStatus, systemCompliances=systemCompliances, systemStatus=systemStatus, powerStatus=powerStatus, modelName=modelName, upgradeAvailable=upgradeAvailable, systemCompliance=systemCompliance, fan=fan, synology=synology, version=version, synoSystem=synoSystem, systemGroups=systemGroups, dsmInfo=dsmInfo, cpuFanStatus=cpuFanStatus)
