#
# PySNMP MIB module MDS-SERVICE-GPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SERVICE-GPS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:19:33 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
mdsServices, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsServices")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, iso, Integer32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Unsigned32, IpAddress, NotificationType, ObjectIdentity, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Unsigned32", "IpAddress", "NotificationType", "ObjectIdentity", "MibIdentifier", "ModuleIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
mdsGpsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12))
mdsGpsMIB.setRevisions(('2018-05-16 00:00', '2016-06-06 00:00', '2015-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsGpsMIB.setRevisionsDescriptions(('Updated conformance statments based on smilint.', 'Add Satellite status table.', 'Initial version.',))
if mibBuilder.loadTexts: mdsGpsMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsGpsMIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsGpsMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n         T 585-242-9600\n         F 585-242-9620\n\n         175 Science Parkway\n         Rochester, New York 14620\n         USA')
if mibBuilder.loadTexts: mdsGpsMIB.setDescription('The MIB module to describe the system.')
mGpsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1))
mGpsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 1))
mGpsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2))
mGpsStatusFixMode = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("nofix", 0), ("a2dfix", 1), ("a3dfix", 2))).clone('nofix')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusFixMode.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusFixMode.setDescription('Fix mode')
mGpsStatusTime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusTime.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusTime.setDescription('UTC Time')
mGpsStatusLatitude = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusLatitude.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusLatitude.setDescription('Latitude')
mGpsStatusLongitude = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusLongitude.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusLongitude.setDescription('Longitude')
mGpsStatusAltitude = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusAltitude.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusAltitude.setDescription('Altitude (ft)')
mGpsStatusSpeed = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusSpeed.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusSpeed.setDescription('Speed (mph)')
mGpsStatusHeading = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusHeading.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusHeading.setDescription('True Heading (degree)')
mGpsStatusSatellitesVisible = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusSatellitesVisible.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusSatellitesVisible.setDescription('The number of satellites currently visible')
mGpsStatusSatellitesUsed = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusSatellitesUsed.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusSatellitesUsed.setDescription('The number of satellites being used for GPS fix.')
mGpsSatellitesTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10), )
if mibBuilder.loadTexts: mGpsSatellitesTable.setStatus('current')
if mibBuilder.loadTexts: mGpsSatellitesTable.setDescription('The list of all visible satellites, and their status')
mGpsSatellitesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1), ).setIndexNames((0, "MDS-SERVICE-GPS-MIB", "mGpsSatellitesPrn"))
if mibBuilder.loadTexts: mGpsSatellitesEntry.setStatus('current')
if mibBuilder.loadTexts: mGpsSatellitesEntry.setDescription('Each entry contains information about a visible satellite')
mGpsSatellitesPrn = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mGpsSatellitesPrn.setStatus('current')
if mibBuilder.loadTexts: mGpsSatellitesPrn.setDescription('PRN (pseudorandom noise code) of satellite.')
mGpsSatellitesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesUsed.setStatus('current')
if mibBuilder.loadTexts: mGpsSatellitesUsed.setDescription('True if this satellite is used in current GPS fix.')
mGpsSatellitesElevation = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesElevation.setStatus('current')
if mibBuilder.loadTexts: mGpsSatellitesElevation.setDescription('Elevation of satellite.')
mGpsSatellitesAzimuth = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesAzimuth.setStatus('current')
if mibBuilder.loadTexts: mGpsSatellitesAzimuth.setDescription('Azimuth of satellite.')
mGpsSatellitesSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesSnr.setStatus('current')
if mibBuilder.loadTexts: mGpsSatellitesSnr.setDescription('Signal-to-Noise radio of satellite.')
mGpsSourcesTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3), )
if mibBuilder.loadTexts: mGpsSourcesTable.setStatus('current')
if mibBuilder.loadTexts: mGpsSourcesTable.setDescription('This table contains gps data sources in the system.')
mGpsSourcesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1), ).setIndexNames((0, "MDS-SERVICE-GPS-MIB", "mGpsSourceName"))
if mibBuilder.loadTexts: mGpsSourcesEntry.setStatus('current')
if mibBuilder.loadTexts: mGpsSourcesEntry.setDescription('Each entry contains information about the gps data source.')
mGpsSourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1, 1), DisplayString())
if mibBuilder.loadTexts: mGpsSourceName.setStatus('current')
if mibBuilder.loadTexts: mGpsSourceName.setDescription('GPS data source name.')
mGpsSourceDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSourceDevice.setStatus('current')
if mibBuilder.loadTexts: mGpsSourceDevice.setDescription('GPS data source device.')
mdsGpsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3))
mdsGpsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 1))
mdsGpsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2))
mGpsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 1, 1)).setObjects(("MDS-SERVICE-GPS-MIB", "mGpsStatusGroup"), ("MDS-SERVICE-GPS-MIB", "mGpsSourcesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mGpsCompliance = mGpsCompliance.setStatus('current')
if mibBuilder.loadTexts: mGpsCompliance.setDescription('The compliance statement for SNMP entities that \n            implement the MDS-GPS-MIB.')
mGpsStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2, 1)).setObjects(("MDS-SERVICE-GPS-MIB", "mGpsStatusFixMode"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusTime"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusLatitude"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusLongitude"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusAltitude"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusSpeed"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusHeading"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusSatellitesVisible"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusSatellitesUsed"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesUsed"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesElevation"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesAzimuth"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesSnr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mGpsStatusGroup = mGpsStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mGpsStatusGroup.setDescription('A collection of objects providing information about\n        orbit GPS data status.')
mGpsSourcesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2, 2)).setObjects(("MDS-SERVICE-GPS-MIB", "mGpsSourceDevice"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mGpsSourcesGroup = mGpsSourcesGroup.setStatus('current')
if mibBuilder.loadTexts: mGpsSourcesGroup.setDescription('A collection of objects providing information about\n        orbit GPS data sources.')
mibBuilder.exportSymbols("MDS-SERVICE-GPS-MIB", PYSNMP_MODULE_ID=mdsGpsMIB, mGpsStatusSpeed=mGpsStatusSpeed, mGpsSourcesEntry=mGpsSourcesEntry, mGpsSatellitesAzimuth=mGpsSatellitesAzimuth, mGpsStatusHeading=mGpsStatusHeading, mGpsStatus=mGpsStatus, mGpsSatellitesTable=mGpsSatellitesTable, mGpsSourcesGroup=mGpsSourcesGroup, mdsGpsMIB=mdsGpsMIB, mGpsStatusGroup=mGpsStatusGroup, mGpsStatusSatellitesVisible=mGpsStatusSatellitesVisible, mGpsStatusFixMode=mGpsStatusFixMode, mGpsSourcesTable=mGpsSourcesTable, mGpsSourceDevice=mGpsSourceDevice, mGpsStatusTime=mGpsStatusTime, mGpsStatusAltitude=mGpsStatusAltitude, mGpsStatusLongitude=mGpsStatusLongitude, mdsGpsMIBConformance=mdsGpsMIBConformance, mGpsMIBObjects=mGpsMIBObjects, mGpsSatellitesPrn=mGpsSatellitesPrn, mGpsStatusSatellitesUsed=mGpsStatusSatellitesUsed, mGpsStatusLatitude=mGpsStatusLatitude, mGpsSatellitesElevation=mGpsSatellitesElevation, mGpsConfig=mGpsConfig, mGpsSatellitesEntry=mGpsSatellitesEntry, mdsGpsMIBCompliances=mdsGpsMIBCompliances, mdsGpsMIBGroups=mdsGpsMIBGroups, mGpsSatellitesSnr=mGpsSatellitesSnr, mGpsCompliance=mGpsCompliance, mGpsSatellitesUsed=mGpsSatellitesUsed, mGpsSourceName=mGpsSourceName)
