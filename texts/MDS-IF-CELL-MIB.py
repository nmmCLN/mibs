#
# PySNMP MIB module MDS-IF-CELL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-CELL-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:20:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, Integer32, Unsigned32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, NotificationType, Counter32, Gauge32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Unsigned32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "NotificationType", "Counter32", "Gauge32", "Bits", "IpAddress")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
mdsIfCellMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1))
mdsIfCellMIB.setRevisions(('2019-12-23 00:00', '2019-10-11 00:00', '2018-05-16 00:00', '2018-02-28 00:00', '2016-10-11 00:00', '2016-02-25 00:00', '2015-09-15 00:00', '2015-08-03 00:00', '2015-07-23 00:00', '2015-01-29 00:00', '2014-11-25 00:00', '2014-10-20 00:00', '2013-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsIfCellMIB.setRevisionsDescriptions(('Added fwRequired mIfCellModemState.', 'Added 4Gd-lte modem types.', 'Updated conformance statments based on smilint.', 'Added 4Gy/z modem types and firmware status table.', 'Added EZ1 (band 31) modem type.', 'Added more status parameters.', 'Reordered sim state enum.', 'Added unknown sim state.', 'Add 4GP (band 26) modem type. Also, added LTE RSRP/RSRQ.', 'Add sprint modem type.', 'Add modem type and firmware package information.', 'Removed hyphens from enumerations.', 'Initial version.',))
if mibBuilder.loadTexts: mdsIfCellMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfCellMIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsIfCellMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n         T 585-242-9600\n         F 585-242-9620\n\n         175 Science Parkway\n         Rochester, New York 14620\n         USA')
if mibBuilder.loadTexts: mdsIfCellMIB.setDescription('The MIB module to describe the cellular interface.')
mIfCellMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1))
mIfCellConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 1))
mIfCellStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2))
mIfCellFwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3))
class UnsignedByte(TextualConvention, Unsigned32):
    description = 'xs:unsignedByte'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class SimSlotState(TextualConvention, Integer32):
    description = 'SIM slot state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notInserted", 0), ("inserted", 1))

mIfCellStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1), )
if mibBuilder.loadTexts: mIfCellStatusTable.setStatus('current')
if mibBuilder.loadTexts: mIfCellStatusTable.setDescription('This table contains status of cellular interfaces. This table has\n         a sparse dependent relationship on the ifTable. For each entry in\n         this table, there exists an entry in the ifTable.')
mIfCellStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfCellStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mIfCellStatusEntry.setDescription('Each entry contains status of a cellular interface.')
mIfCellImsi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellImsi.setStatus('current')
if mibBuilder.loadTexts: mIfCellImsi.setDescription('The International Mobile Subscriber Identity.')
mIfCellImei = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellImei.setStatus('current')
if mibBuilder.loadTexts: mIfCellImei.setDescription('International mobile equipment identity')
mIfCellIccid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellIccid.setStatus('current')
if mibBuilder.loadTexts: mIfCellIccid.setDescription('Unique serial number of the SIM card')
mIfCellMdn = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellMdn.setStatus('current')
if mibBuilder.loadTexts: mIfCellMdn.setDescription('Mobile directory number')
mIfCellApn = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellApn.setStatus('current')
if mibBuilder.loadTexts: mIfCellApn.setDescription('Access Point Name')
mIfCellAppSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellAppSwVersion.setStatus('current')
if mibBuilder.loadTexts: mIfCellAppSwVersion.setDescription('Application software version')
mIfCellModemSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemSwVersion.setStatus('current')
if mibBuilder.loadTexts: mIfCellModemSwVersion.setDescription('Modem software version')
mIfCellSimState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("notInserted", 0), ("locked", 1), ("ready", 2), ("failed", 3), ("unknown", 4))).clone('notInserted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSimState.setStatus('current')
if mibBuilder.loadTexts: mIfCellSimState.setDescription('SIM state of cellular modem')
mIfCellModemState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("notRegistered", 1), ("searching", 2), ("registrationDenied", 3), ("idle", 4), ("connected", 5), ("fwRequired", 6))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemState.setStatus('current')
if mibBuilder.loadTexts: mIfCellModemState.setDescription('Device state of cellular modem')
mIfCellRoamingState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("home", 1), ("roaming", 2))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRoamingState.setStatus('current')
if mibBuilder.loadTexts: mIfCellRoamingState.setDescription('Roaming state of cellular modem')
mIfCellServiceState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("none", 0), ("gprs", 1), ("edge", 2), ("umts", 3), ("hsdpa", 4), ("hsupa", 5), ("hspaPlus", 6), ("is95a", 7), ("is95b", 8), ("onexRtt", 9), ("evdoRev0", 10), ("evdoReva", 11), ("evdoRevb", 12), ("evdoEhrpd", 13), ("lte", 14))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellServiceState.setStatus('current')
if mibBuilder.loadTexts: mIfCellServiceState.setDescription('Service state of cellular modem')
mIfCellRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRssi.setStatus('current')
if mibBuilder.loadTexts: mIfCellRssi.setDescription('Received signal strength indicator (dBm). Indicates total received power including signal, interference and noise')
mIfCellRsrp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRsrp.setStatus('current')
if mibBuilder.loadTexts: mIfCellRsrp.setDescription('Received signal reference power (dBm). Indicates power of LTE reference signals')
mIfCellRsrq = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRsrq.setStatus('current')
if mibBuilder.loadTexts: mIfCellRsrq.setDescription('Received signal receive quality (dB). Indicates LTE signal quality')
mIfCellSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSnr.setStatus('current')
if mibBuilder.loadTexts: mIfCellSnr.setDescription('Received signal to noise ratio (dB). Indicates received signal quality.')
mIfCellEcio = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellEcio.setStatus('current')
if mibBuilder.loadTexts: mIfCellEcio.setDescription('Ec/Io (dBm). Indicates received signal quality for CDMA/UMTS.')
mIfCellModemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("typeUnknown", 0), ("typeE4VLteNaVerizon", 1), ("type3G1GsmGlobal", 2), ("typeE4xLteEmea", 3), ("type4GxLteNa", 4), ("type4GPLteNa", 5), ("typeEZ1LteEmea", 6), ("type4GyLteNaEu", 7), ("type4GzLteApac", 8), ("type4GaLteGlobal", 9), ("type4GbLteAmericas", 10), ("type4GcLteEu", 11), ("type4GdLteGlobal", 12))).clone('typeUnknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemType.setStatus('current')
if mibBuilder.loadTexts: mIfCellModemType.setDescription('Type of cellular modem')
mIfCellModemPackageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemPackageVersion.setStatus('current')
if mibBuilder.loadTexts: mIfCellModemPackageVersion.setDescription('Modem package version')
mIfCellTac = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellTac.setStatus('current')
if mibBuilder.loadTexts: mIfCellTac.setDescription('Tracking Area Code')
mIfCellGlobalCellId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellGlobalCellId.setStatus('current')
if mibBuilder.loadTexts: mIfCellGlobalCellId.setDescription('Global Cell ID (0xFFFFFFFF = not available)')
mIfCellPhysicalCellId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellPhysicalCellId.setStatus('current')
if mibBuilder.loadTexts: mIfCellPhysicalCellId.setDescription('Physical Cell ID (Normal Range: 0-503, 0xFFFF = not available)')
mIfCellBand = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellBand.setStatus('current')
if mibBuilder.loadTexts: mIfCellBand.setDescription('LTE Band (0xFF = invalid)')
mIfCellBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("bwUnknown", 0), ("bw1dot4Mhz", 1), ("bw3Mhz", 2), ("bw5Mhz", 3), ("bw10Mhz", 4), ("bw15Mhz", 5), ("bw20Mhz", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellBandwidth.setStatus('current')
if mibBuilder.loadTexts: mIfCellBandwidth.setDescription('LTE Bandwidth')
mIfCellTxChan = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellTxChan.setStatus('current')
if mibBuilder.loadTexts: mIfCellTxChan.setDescription('TX channel (0xFFFF = not available)')
mIfCellRxChan = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRxChan.setStatus('current')
if mibBuilder.loadTexts: mIfCellRxChan.setDescription('RX channel (0xFFFF = not available)')
mIfCellEmmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emmUnknown", 0), ("emmDeregistered", 1), ("emmRegInitiated", 2), ("emmRegistered", 3), ("emmTauInitiated", 4), ("emmSrInitiated", 5), ("emmDeregInitiated", 6), ("emmInvalid", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellEmmState.setStatus('current')
if mibBuilder.loadTexts: mIfCellEmmState.setDescription('EPS mobility management (EMM) state')
mIfCellRrcState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("rrcUnknown", 0), ("rrcIdle", 1), ("rrcWaiting", 2), ("rrcConnected", 3), ("rrcReleasing", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRrcState.setStatus('current')
if mibBuilder.loadTexts: mIfCellRrcState.setDescription('Radio Resource Control (RRC) state')
mIfCellActiveSimSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("simA", 0), ("simB", 1))).clone('simA')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellActiveSimSlot.setStatus('current')
if mibBuilder.loadTexts: mIfCellActiveSimSlot.setDescription('Active SIM slot')
mIfCellSimASlotState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 29), SimSlotState().clone('notInserted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSimASlotState.setStatus('current')
if mibBuilder.loadTexts: mIfCellSimASlotState.setDescription('SIM A slot state')
mIfCellSimBSlotState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 30), SimSlotState().clone('notInserted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSimBSlotState.setStatus('current')
if mibBuilder.loadTexts: mIfCellSimBSlotState.setDescription('SIM B slot state')
mIfCellFwStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1), )
if mibBuilder.loadTexts: mIfCellFwStatusTable.setStatus('current')
if mibBuilder.loadTexts: mIfCellFwStatusTable.setDescription('This table contains firmware status of cellular interfaces. This table has\n         a sparse dependent relationship on the ifTable. For each entry in\n         this table, there exists an entry in the ifTable.')
mIfCellFwStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-CELL-MIB", "mIfCellFwId"))
if mibBuilder.loadTexts: mIfCellFwStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mIfCellFwStatusEntry.setDescription('Each entry contains firmware status of a cellular interface.')
mIfCellFwId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 1), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellFwId.setStatus('current')
if mibBuilder.loadTexts: mIfCellFwId.setDescription('The storage location of this modem firmware image.')
mIfCellFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellFwVersion.setStatus('current')
if mibBuilder.loadTexts: mIfCellFwVersion.setDescription('The version of modem firmware stored at this location.')
mIfCellFwActive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellFwActive.setStatus('current')
if mibBuilder.loadTexts: mIfCellFwActive.setDescription('Indicates whether this is the currently running modem firmware.')
mdsIfCellMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3))
mdsIfCellMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 1))
mdsIfCellMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2))
mIfCellCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 1, 1)).setObjects(("MDS-IF-CELL-MIB", "mIfCellStatusGroup"), ("MDS-IF-CELL-MIB", "mIfCellFwStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfCellCompliance = mIfCellCompliance.setStatus('current')
if mibBuilder.loadTexts: mIfCellCompliance.setDescription('The compliance statement for SNMP entities that\n            implement the MDS-IF-CELL-MIB.')
mIfCellStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2, 1)).setObjects(("MDS-IF-CELL-MIB", "mIfCellImsi"), ("MDS-IF-CELL-MIB", "mIfCellImei"), ("MDS-IF-CELL-MIB", "mIfCellIccid"), ("MDS-IF-CELL-MIB", "mIfCellMdn"), ("MDS-IF-CELL-MIB", "mIfCellApn"), ("MDS-IF-CELL-MIB", "mIfCellAppSwVersion"), ("MDS-IF-CELL-MIB", "mIfCellModemSwVersion"), ("MDS-IF-CELL-MIB", "mIfCellSimState"), ("MDS-IF-CELL-MIB", "mIfCellModemState"), ("MDS-IF-CELL-MIB", "mIfCellRoamingState"), ("MDS-IF-CELL-MIB", "mIfCellServiceState"), ("MDS-IF-CELL-MIB", "mIfCellRssi"), ("MDS-IF-CELL-MIB", "mIfCellRsrp"), ("MDS-IF-CELL-MIB", "mIfCellRsrq"), ("MDS-IF-CELL-MIB", "mIfCellSnr"), ("MDS-IF-CELL-MIB", "mIfCellEcio"), ("MDS-IF-CELL-MIB", "mIfCellModemType"), ("MDS-IF-CELL-MIB", "mIfCellModemPackageVersion"), ("MDS-IF-CELL-MIB", "mIfCellTac"), ("MDS-IF-CELL-MIB", "mIfCellGlobalCellId"), ("MDS-IF-CELL-MIB", "mIfCellPhysicalCellId"), ("MDS-IF-CELL-MIB", "mIfCellBand"), ("MDS-IF-CELL-MIB", "mIfCellBandwidth"), ("MDS-IF-CELL-MIB", "mIfCellTxChan"), ("MDS-IF-CELL-MIB", "mIfCellRxChan"), ("MDS-IF-CELL-MIB", "mIfCellEmmState"), ("MDS-IF-CELL-MIB", "mIfCellRrcState"), ("MDS-IF-CELL-MIB", "mIfCellActiveSimSlot"), ("MDS-IF-CELL-MIB", "mIfCellSimASlotState"), ("MDS-IF-CELL-MIB", "mIfCellSimBSlotState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfCellStatusGroup = mIfCellStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mIfCellStatusGroup.setDescription('A collection of objects providing information about\n        cellular interface status.')
mIfCellFwStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2, 2)).setObjects(("MDS-IF-CELL-MIB", "mIfCellFwId"), ("MDS-IF-CELL-MIB", "mIfCellFwVersion"), ("MDS-IF-CELL-MIB", "mIfCellFwActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfCellFwStatusGroup = mIfCellFwStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mIfCellFwStatusGroup.setDescription('A collection of objects providing information about\n        cellular interface firmware status.')
mibBuilder.exportSymbols("MDS-IF-CELL-MIB", mIfCellRoamingState=mIfCellRoamingState, mIfCellSimBSlotState=mIfCellSimBSlotState, mIfCellEcio=mIfCellEcio, mIfCellModemSwVersion=mIfCellModemSwVersion, mIfCellBand=mIfCellBand, mIfCellCompliance=mIfCellCompliance, mIfCellEmmState=mIfCellEmmState, mdsIfCellMIBConformance=mdsIfCellMIBConformance, mdsIfCellMIB=mdsIfCellMIB, mIfCellTac=mIfCellTac, mIfCellFwStatus=mIfCellFwStatus, mIfCellPhysicalCellId=mIfCellPhysicalCellId, mIfCellApn=mIfCellApn, mIfCellFwStatusTable=mIfCellFwStatusTable, mIfCellAppSwVersion=mIfCellAppSwVersion, mIfCellIccid=mIfCellIccid, mIfCellFwActive=mIfCellFwActive, UnsignedByte=UnsignedByte, mIfCellActiveSimSlot=mIfCellActiveSimSlot, mIfCellFwId=mIfCellFwId, mIfCellStatusGroup=mIfCellStatusGroup, mdsIfCellMIBCompliances=mdsIfCellMIBCompliances, mIfCellStatusEntry=mIfCellStatusEntry, mIfCellImsi=mIfCellImsi, mdsIfCellMIBGroups=mdsIfCellMIBGroups, PYSNMP_MODULE_ID=mdsIfCellMIB, mIfCellStatusTable=mIfCellStatusTable, mIfCellMdn=mIfCellMdn, mIfCellBandwidth=mIfCellBandwidth, mIfCellImei=mIfCellImei, mIfCellServiceState=mIfCellServiceState, mIfCellRxChan=mIfCellRxChan, mIfCellFwVersion=mIfCellFwVersion, mIfCellFwStatusEntry=mIfCellFwStatusEntry, mIfCellMIBObjects=mIfCellMIBObjects, mIfCellRssi=mIfCellRssi, mIfCellSnr=mIfCellSnr, mIfCellSimState=mIfCellSimState, mIfCellTxChan=mIfCellTxChan, mIfCellGlobalCellId=mIfCellGlobalCellId, SimSlotState=SimSlotState, mIfCellModemState=mIfCellModemState, mIfCellRsrp=mIfCellRsrp, mIfCellStatus=mIfCellStatus, mIfCellSimASlotState=mIfCellSimASlotState, mIfCellRsrq=mIfCellRsrq, mIfCellConfig=mIfCellConfig, mIfCellModemPackageVersion=mIfCellModemPackageVersion, mIfCellModemType=mIfCellModemType, mIfCellRrcState=mIfCellRrcState, mIfCellFwStatusGroup=mIfCellFwStatusGroup)
