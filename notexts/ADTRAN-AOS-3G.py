#
# PySNMP MIB module ADTRAN-AOS-3G (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-3G
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:42 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSWan, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSWan", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Gauge32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Integer32, Counter32, Counter64, TimeTicks, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Integer32", "Counter32", "Counter64", "TimeTicks", "MibIdentifier", "Unsigned32", "iso")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
adGenAOS3GMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 6, 2))
adGenAOS3GMib.setRevisions(('2010-01-05 00:00', '2010-01-14 00:00',))
if mibBuilder.loadTexts: adGenAOS3GMib.setLastUpdated('201001050000Z')
if mibBuilder.loadTexts: adGenAOS3GMib.setOrganization('ADTRAN, Inc.')
adGenAOS3G = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2))
adGenAOS3GTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0))
if mibBuilder.loadTexts: adGenAOS3GTraps.setStatus('current')
adGenAOS3GTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1), )
if mibBuilder.loadTexts: adGenAOS3GTable.setStatus('current')
adGenAOS3GEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOS3GEntry.setStatus('current')
adGenAOS3GNetworkAccessID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GNetworkAccessID.setStatus('current')
adGenAOS3GHASS = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("unset", 0), ("set", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHASS.setStatus('current')
adGenAOS3GHASPI = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHASPI.setStatus('current')
adGenAOS3GAAASS = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 4), Bits().clone(namedValues=NamedValues(("unset", 0), ("set", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GAAASS.setStatus('current')
adGenAOS3GAAASPI = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GAAASPI.setStatus('current')
adGenAOS3GReverseTunneling = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 6), Bits().clone(namedValues=NamedValues(("unset", 0), ("set", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GReverseTunneling.setStatus('current')
adGenAOS3GHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHomeAddress.setStatus('current')
adGenAOS3GPrimaryHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GPrimaryHomeAddress.setStatus('current')
adGenAOS3GSecHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GSecHomeAddress.setStatus('current')
adGenAOS3GRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GRSSI.setStatus('current')
adGenAOS3GECIO = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GECIO.setStatus('current')
adGenAOS3GPnOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GPnOffset.setStatus('current')
adGenAOS3GServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GServiceType.setStatus('current')
adGenAOS3GServiceTypePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 9, 10))).clone(namedValues=NamedValues(("modeAUTO", 4), ("mode1xRTT", 9), ("mode1xEVDO", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GServiceTypePreference.setStatus('current')
adGenAOS3GConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GConnectionState.setStatus('current')
adGenAOS3GECIOIntegerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GECIOIntegerValue.setStatus('current')
adGenAOS3GHardwareDataTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2), )
if mibBuilder.loadTexts: adGenAOS3GHardwareDataTable.setStatus('current')
adGenAOS3GHardwareDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOS3GHardwareDataEntry.setStatus('current')
adGenAOS3GSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GSystemID.setStatus('current')
adGenAOS3GNetworkID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GNetworkID.setStatus('current')
adGenAOS3GPrefferedRoamList = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GPrefferedRoamList.setStatus('current')
adGenAOS3GMobileDirNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GMobileDirNumber.setStatus('current')
adGenAOS3GESN = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GESN.setStatus('current')
adGenAOS3GMobileStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GMobileStationID.setStatus('current')
adGenAOS3GHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHardwareVersion.setStatus('current')
adGenAOS3GFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GFirmwareVersion.setStatus('current')
adGenAOS3GThresholdDataTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3), )
if mibBuilder.loadTexts: adGenAOS3GThresholdDataTable.setStatus('current')
adGenAOS3GThresholdDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOS3GThresholdDataEntry.setStatus('current')
adGenAOS3GEnableTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GEnableTraps.setStatus('current')
adGenAOS3GRSSIThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-200, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GRSSIThreshold.setStatus('current')
adGenAOS3GECIOThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-200, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GECIOThreshold.setStatus('current')
rssiDataRangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"))
if mibBuilder.loadTexts: rssiDataRangeAlarm.setStatus('current')
ecioDataRangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GECIO"))
if mibBuilder.loadTexts: ecioDataRangeAlarm.setStatus('current')
rssiDataRangeClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"))
if mibBuilder.loadTexts: rssiDataRangeClear.setStatus('current')
ecioDataRangeClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GECIO"))
if mibBuilder.loadTexts: ecioDataRangeClear.setStatus('current')
configValueSet = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: configValueSet.setStatus('current')
modemResetAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 6)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: modemResetAlarm.setStatus('current')
serviceTypeChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 7)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GServiceType"))
if mibBuilder.loadTexts: serviceTypeChangeAlarm.setStatus('current')
connectionStateDownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 8)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: connectionStateDownAlarm.setStatus('current')
adGenAOS3GConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9))
adGenAOS3GGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1))
adGenAOS3GCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 2))
adGenAOS3GFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 2, 1)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GTableGroup"), ("ADTRAN-AOS-3G", "adGenAOS3GHardwareDataGroup"), ("ADTRAN-AOS-3G", "adGenAOS3GThresholdDataGroup"), ("ADTRAN-AOS-3G", "adGenAOS3GTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GFullCompliance = adGenAOS3GFullCompliance.setStatus('current')
adGenAOS3GTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 1)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GNetworkAccessID"), ("ADTRAN-AOS-3G", "adGenAOS3GHASS"), ("ADTRAN-AOS-3G", "adGenAOS3GHASPI"), ("ADTRAN-AOS-3G", "adGenAOS3GAAASS"), ("ADTRAN-AOS-3G", "adGenAOS3GAAASPI"), ("ADTRAN-AOS-3G", "adGenAOS3GReverseTunneling"), ("ADTRAN-AOS-3G", "adGenAOS3GHomeAddress"), ("ADTRAN-AOS-3G", "adGenAOS3GPrimaryHomeAddress"), ("ADTRAN-AOS-3G", "adGenAOS3GSecHomeAddress"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"), ("ADTRAN-AOS-3G", "adGenAOS3GECIO"), ("ADTRAN-AOS-3G", "adGenAOS3GPnOffset"), ("ADTRAN-AOS-3G", "adGenAOS3GServiceType"), ("ADTRAN-AOS-3G", "adGenAOS3GServiceTypePreference"), ("ADTRAN-AOS-3G", "adGenAOS3GConnectionState"), ("ADTRAN-AOS-3G", "adGenAOS3GECIOIntegerValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GTableGroup = adGenAOS3GTableGroup.setStatus('current')
adGenAOS3GHardwareDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 2)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GSystemID"), ("ADTRAN-AOS-3G", "adGenAOS3GNetworkID"), ("ADTRAN-AOS-3G", "adGenAOS3GPrefferedRoamList"), ("ADTRAN-AOS-3G", "adGenAOS3GMobileDirNumber"), ("ADTRAN-AOS-3G", "adGenAOS3GESN"), ("ADTRAN-AOS-3G", "adGenAOS3GMobileStationID"), ("ADTRAN-AOS-3G", "adGenAOS3GHardwareVersion"), ("ADTRAN-AOS-3G", "adGenAOS3GFirmwareVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GHardwareDataGroup = adGenAOS3GHardwareDataGroup.setStatus('current')
adGenAOS3GThresholdDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 3)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GEnableTraps"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSIThreshold"), ("ADTRAN-AOS-3G", "adGenAOS3GECIOThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GThresholdDataGroup = adGenAOS3GThresholdDataGroup.setStatus('current')
adGenAOS3GTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 4)).setObjects(("ADTRAN-AOS-3G", "rssiDataRangeAlarm"), ("ADTRAN-AOS-3G", "ecioDataRangeAlarm"), ("ADTRAN-AOS-3G", "rssiDataRangeClear"), ("ADTRAN-AOS-3G", "ecioDataRangeClear"), ("ADTRAN-AOS-3G", "configValueSet"), ("ADTRAN-AOS-3G", "modemResetAlarm"), ("ADTRAN-AOS-3G", "serviceTypeChangeAlarm"), ("ADTRAN-AOS-3G", "connectionStateDownAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GTrapGroup = adGenAOS3GTrapGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-3G", adGenAOS3GRSSI=adGenAOS3GRSSI, adGenAOS3GAAASPI=adGenAOS3GAAASPI, adGenAOS3GTableGroup=adGenAOS3GTableGroup, adGenAOS3GESN=adGenAOS3GESN, modemResetAlarm=modemResetAlarm, adGenAOS3GThresholdDataEntry=adGenAOS3GThresholdDataEntry, adGenAOS3GMobileStationID=adGenAOS3GMobileStationID, adGenAOS3GConformance=adGenAOS3GConformance, PYSNMP_MODULE_ID=adGenAOS3GMib, adGenAOS3GTrapGroup=adGenAOS3GTrapGroup, ecioDataRangeAlarm=ecioDataRangeAlarm, rssiDataRangeClear=rssiDataRangeClear, adGenAOS3GNetworkAccessID=adGenAOS3GNetworkAccessID, adGenAOS3GHardwareDataEntry=adGenAOS3GHardwareDataEntry, adGenAOS3GThresholdDataGroup=adGenAOS3GThresholdDataGroup, adGenAOS3GHASS=adGenAOS3GHASS, adGenAOS3GNetworkID=adGenAOS3GNetworkID, adGenAOS3GHardwareDataGroup=adGenAOS3GHardwareDataGroup, adGenAOS3GECIO=adGenAOS3GECIO, adGenAOS3GServiceTypePreference=adGenAOS3GServiceTypePreference, adGenAOS3GSecHomeAddress=adGenAOS3GSecHomeAddress, adGenAOS3GReverseTunneling=adGenAOS3GReverseTunneling, adGenAOS3GCompliances=adGenAOS3GCompliances, adGenAOS3GMib=adGenAOS3GMib, adGenAOS3GFullCompliance=adGenAOS3GFullCompliance, adGenAOS3GPrimaryHomeAddress=adGenAOS3GPrimaryHomeAddress, adGenAOS3GServiceType=adGenAOS3GServiceType, adGenAOS3GPrefferedRoamList=adGenAOS3GPrefferedRoamList, adGenAOS3GTable=adGenAOS3GTable, rssiDataRangeAlarm=rssiDataRangeAlarm, adGenAOS3GGroup=adGenAOS3GGroup, adGenAOS3GRSSIThreshold=adGenAOS3GRSSIThreshold, adGenAOS3G=adGenAOS3G, adGenAOS3GFirmwareVersion=adGenAOS3GFirmwareVersion, adGenAOS3GEnableTraps=adGenAOS3GEnableTraps, serviceTypeChangeAlarm=serviceTypeChangeAlarm, adGenAOS3GHardwareDataTable=adGenAOS3GHardwareDataTable, ecioDataRangeClear=ecioDataRangeClear, adGenAOS3GAAASS=adGenAOS3GAAASS, adGenAOS3GEntry=adGenAOS3GEntry, connectionStateDownAlarm=connectionStateDownAlarm, adGenAOS3GHardwareVersion=adGenAOS3GHardwareVersion, adGenAOS3GHomeAddress=adGenAOS3GHomeAddress, adGenAOS3GConnectionState=adGenAOS3GConnectionState, adGenAOS3GSystemID=adGenAOS3GSystemID, adGenAOS3GThresholdDataTable=adGenAOS3GThresholdDataTable, adGenAOS3GTraps=adGenAOS3GTraps, adGenAOS3GECIOThreshold=adGenAOS3GECIOThreshold, adGenAOS3GPnOffset=adGenAOS3GPnOffset, adGenAOS3GECIOIntegerValue=adGenAOS3GECIOIntegerValue, adGenAOS3GHASPI=adGenAOS3GHASPI, configValueSet=configValueSet, adGenAOS3GMobileDirNumber=adGenAOS3GMobileDirNumber)
