#
# PySNMP MIB module SL-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-SONET-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:39 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfIntervalCount, PerfCurrentCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfCurrentCount", "PerfTotalCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, NotificationType, iso, MibIdentifier, ModuleIdentity, Counter32, TimeTicks, IpAddress, Integer32, Unsigned32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "NotificationType", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "TimeTicks", "IpAddress", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
slSonetMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 6))
if mibBuilder.loadTexts: slSonetMib.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slSonetMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slSonetMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slSonetMib.setDescription('This MIB module describes the SiteLight SONET Service.\n\t\tThe mib contains the extensions required for the rfc2558.')
class SignalLabel(TextualConvention, Integer32):
    description = 'STS path signal label -- one byte, C2, class A, is allocated to \n       indicate the construction of the STS SPE. \n       The following hex values of the C2 byte has been defined.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 18, 19, 20, 21, 22, 27))
    namedValues = NamedValues(("sigUnequipped", 0), ("sigEquipped", 1), ("sigPathFloatVt", 2), ("sigPathLoackedVt", 3), ("sigPathAsynchDs3", 4), ("sigPathSyntran", 5), ("sigPathAsyncDs4na", 18), ("sigPathAtm", 19), ("sigPathDqdb", 20), ("sigPathFddi", 21), ("sigPathHdlc", 22), ("sigPathGfp", 27))

slSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1))
slSonetOh = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2))
slSonetPos = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6))
slSonetAls = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7))
slSonetFs = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8))
slSonetTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 11))
slSonetOhTrace = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1))
slSonetOhSl = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2))
slSonetOhTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 3))
slSonetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1), )
if mibBuilder.loadTexts: slSonetConfigTable.setStatus('current')
if mibBuilder.loadTexts: slSonetConfigTable.setDescription('The SONET/SDH configuration table. This table has objects \n        for configuring sonet lines.')
slSonetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slSonetConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slSonetConfigEntry.setDescription("An entry in the table. There is an entry for each SONET line \n        in the table. Entries are automatically created for an \n        ifType value of sonet(39). 'ifAdminStatus' from the ifTable \n        must be used to enable or disable a line. By default, the \n        line state is down.")
slSonetConfigFrameScramble = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetConfigFrameScramble.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetConfigFrameScramble.setStatus('current')
if mibBuilder.loadTexts: slSonetConfigFrameScramble.setDescription('This object is used to disable or enable the Scrambling\n             option in SONET line. Please refer to GR-253-CORE for \n             frame scrambling.')
slSonetConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("sonetSts3", 1), ("sonetSts3c", 2), ("sonetSts12", 3), ("sonetSts12c", 4), ("sonetSts48c", 5), ("sonetSts3cx4", 6), ("sonetSts48", 7), ("sonetSts3cx16", 8), ("sonetSts3x16", 9), ("sonetSts12cx4", 10), ("sonetSts12x4", 11), ("sonetSts192c", 12), ("sonetStsOther", 13)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetConfigType.setStatus('current')
if mibBuilder.loadTexts: slSonetConfigType.setDescription('This object represents the configured line type for Trunks:\n           sonetSts48c(5)    - 1  x Sts48  (2.5GbTrunk)\n           sonetSts192c(12)  - 1  x Sts192 (10Gb Trunk)\n           sonetStsOther(13) - for OC-n interfaces see slSonetFsTable.')
slSonetConfigDccSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sonetLineDcc", 1), ("sonetSectionDcc", 2), ("sonetInband", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetConfigDccSelection.setStatus('current')
if mibBuilder.loadTexts: slSonetConfigDccSelection.setDescription('This object selects the DCC type.')
slSonetResetAllCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetResetAllCounters.setReference('ANSI T1.231-1997 clause 9.1.5.1.')
if mibBuilder.loadTexts: slSonetResetAllCounters.setStatus('current')
if mibBuilder.loadTexts: slSonetResetAllCounters.setDescription('Setting this variable to 1 will cause all of the counters\n        (performance regsters) on this SONET interface to be initialized \n        to zero (0).')
slSonetPortThresholdTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetPortThresholdTrapEnable.setReference('ANSI T1.231-1997 clause 9.1.5.2.')
if mibBuilder.loadTexts: slSonetPortThresholdTrapEnable.setStatus('current')
if mibBuilder.loadTexts: slSonetPortThresholdTrapEnable.setDescription('This variable indicates whether threshold traps \n        should be generated for this SONET interface.')
slSonetConfigSdThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 9)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetConfigSdThreshold.setStatus('current')
if mibBuilder.loadTexts: slSonetConfigSdThreshold.setDescription('This object contains the Bit Error Rate threshold for\n            Signal Degrade detection on the working line. Once this\n            threshold is exceeded, an APS switch will occur.\n            This value is 10 to -n where n is between 5 and 9\n            (read-write).')
slSonetConfigSfThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetConfigSfThreshold.setStatus('current')
if mibBuilder.loadTexts: slSonetConfigSfThreshold.setDescription('This object contains the Bit Error Rate threshold for\n        Signal Fault detection on the working line. Once this\n        threshold is exceeded, an APS switch will occur.\n        This value is 10 to the -n, where n is between 3 and 5.\n        (read-write)')
slSonetCompression = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("uncompress", 0), ("posCompress32", 1), ("posCompress16", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetCompression.setStatus('current')
if mibBuilder.loadTexts: slSonetCompression.setDescription('This object applies only for trunk ports.\n       It specifies if the packets should be compressed.\n       0 - Means no POS compression, \n       1 - Means POS compression with CRC-32.\n       2 - Means POS compression with CRC-16.\n       Note that the two connected trunks should be configured\n       to the same value.\n       Note also that the BW calculation of the OC-n should\n       be changed according to this value.')
slSonetOverheadTunneling = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("lineDcc", 1), ("k1k2", 2), ("full", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetOverheadTunneling.setStatus('current')
if mibBuilder.loadTexts: slSonetOverheadTunneling.setDescription('The section and line overhead tunneling configuration:\n       none(0)     - no tunneling support\n       lineDcc(1)  - line DCC tunneling\n       k1k2(2)     - line DCC + protection k byte\n       full(3)     - all transport overhead bytes are tunneled')
slSonetLopBitmask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetLopBitmask.setStatus('current')
if mibBuilder.loadTexts: slSonetLopBitmask.setDescription('The LOP status. Each bit of the bits represent the status\n       of the LOP alarm in corresponding STS.\n       For a path with more than a single STS, only the value of the\n       first STS in the path is relevant.\n       This object is relevant only for the OC-N cards and not\n       for the Trunk.\n       In the next future this object will be replaced with\n       an object of a new table that shall describe the OC-N\n       frame structure.')
slSonetTdmTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetTdmTrunk.setStatus('current')
if mibBuilder.loadTexts: slSonetTdmTrunk.setDescription('This object is applicable only to the OC-n ports.\n       TRUE  - means that the OC-n port is used as a TDM Trunk.\n       FLASE - means normal OC-n port.')
slSonetFsApply = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetFsApply.setStatus('current')
if mibBuilder.loadTexts: slSonetFsApply.setDescription('Writing to this object activate the slSonetFsTable setting.\n       This allow the NMS to do many changes to the slSonetFsTable\n       and then APPLY them at once. This prevent from going through\n       unconsistent steps.\n       This object always returns the value 0.')
slSonetTxLte = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5))).clone(namedValues=NamedValues(("ssb00", 1), ("ssb10", 2), ("auto", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetTxLte.setStatus('current')
if mibBuilder.loadTexts: slSonetTxLte.setDescription('The SS bits to transmit (bits 5,6 in H1,H1*).')
slSonetReceivedLte = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ssb00", 1), ("ssb10", 2), ("ssb01", 3), ("ssb11", 4), ("ssbinv", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetReceivedLte.setStatus('current')
if mibBuilder.loadTexts: slSonetReceivedLte.setDescription('The detected LTE type, according to the received SS bits\n       (bits 5,6 in H1,H1*).')
slSonetResetPmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetResetPmThreshold.setReference('ANSI T1.231-1997 clause 9.1.5.1.')
if mibBuilder.loadTexts: slSonetResetPmThreshold.setStatus('current')
if mibBuilder.loadTexts: slSonetResetPmThreshold.setDescription('Setting this variable to 1 will reset the PM threshold \n        parameters to the factory defaults.')
slSonetResetAlsParams = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetResetAlsParams.setReference('ANSI T1.231-1997 clause 9.1.5.1.')
if mibBuilder.loadTexts: slSonetResetAlsParams.setStatus('current')
if mibBuilder.loadTexts: slSonetResetAlsParams.setDescription('Setting this variable to 1 will reset the ALS \n        parameters to the factory defaults.')
slSonetTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("shortWave", 2), ("longWave", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetTransceiverType.setStatus('current')
if mibBuilder.loadTexts: slSonetTransceiverType.setDescription('The tranceiver type.')
slSonetTransceiverMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("sm", 2), ("mm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetTransceiverMedia.setStatus('current')
if mibBuilder.loadTexts: slSonetTransceiverMedia.setDescription('The tranceiver media.')
slSonetTraceTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1), )
if mibBuilder.loadTexts: slSonetTraceTable.setStatus('current')
if mibBuilder.loadTexts: slSonetTraceTable.setDescription('The SONET/SDH Trace table. This table contains \n            objects for tracing the sonet section and path.')
slSonetTraceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slSonetTraceEntry.setStatus('current')
if mibBuilder.loadTexts: slSonetTraceEntry.setDescription('An entry in the trace table. Entries exist for active sonet\n         interfaces. The objects in this table are used to verify \n         continued connection between the two ends of the line.')
slSonetTraceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("monitoring", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetTraceMode.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetTraceMode.setStatus('current')
if mibBuilder.loadTexts: slSonetTraceMode.setDescription('Determine the Trace Message Mode.')
slSonetTraceToTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetTraceToTransmit.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetTraceToTransmit.setStatus('current')
if mibBuilder.loadTexts: slSonetTraceToTransmit.setDescription('Sonet Trace To Transmit. This is string that\n             is transmitted to perform Sonet trace \n             diagnostics. The trace string is  repetitively \n             transmited so that a trace receiving terminal can \n             verify its continued connection to the intended \n             transmitter. The default value is a zero-length string.\n             Unless this object is set to a non-zero length string, \n             tracing will not be performed.\n             The Agent is responsible to pad the end of the string with <CR><LF>.')
slSonetTraceToExpect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetTraceToExpect.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetTraceToExpect.setStatus('current')
if mibBuilder.loadTexts: slSonetTraceToExpect.setDescription("Sonet Trace Massage To Expect. The receiving terminal \n             verifies if the incoming string matches this string. \n             The value of 'slSonetTraceFailure' indicates whether a \n             trace mismatch occurred. The default value is a \n             zero-length string.\n             The Agent is responsible to pad the end of the string with <CR><LF>.")
slSonetTraceFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetTraceFailure.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetTraceFailure.setStatus('current')
if mibBuilder.loadTexts: slSonetTraceFailure.setDescription("The value of this object is set to 'true' when Sonet \n         Section received trace does not match the \n         'slSonetTraceToExpect'.")
slSonetTraceReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetTraceReceived.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetTraceReceived.setStatus('current')
if mibBuilder.loadTexts: slSonetTraceReceived.setDescription('This object is used to view the Sonet Trace Message that \n\t\tis received by the receiving terminal.\n\t\tThe Agent is responsible to pad the end of the string with <CR><LF>.')
slSonetSlTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1), )
if mibBuilder.loadTexts: slSonetSlTable.setStatus('current')
if mibBuilder.loadTexts: slSonetSlTable.setDescription('The SONET/SDH Signal Label table. This table contains \n       signal label for the sonet path.')
slSonetSlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slSonetSlEntry.setStatus('current')
if mibBuilder.loadTexts: slSonetSlEntry.setDescription('An entry in the SONET/SDH Signal Label table. The entries \n        exist for active sonet lines. The objects in this table are \n        used to verify continued connection between the two ends of\n        the line.')
slSonetSlToTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 2), SignalLabel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetSlToTransmit.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetSlToTransmit.setStatus('current')
if mibBuilder.loadTexts: slSonetSlToTransmit.setDescription('Sonet Signal Label To Transmit.')
slSonetSlToExpect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 3), SignalLabel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetSlToExpect.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetSlToExpect.setStatus('current')
if mibBuilder.loadTexts: slSonetSlToExpect.setDescription('Sonet Signal Label To Expect.')
slSonetSlFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetSlFailure.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetSlFailure.setStatus('current')
if mibBuilder.loadTexts: slSonetSlFailure.setDescription("The value of this object is set to 'true' when Sonet\n         received signal label does not match the 'slSonetSlToExpect'.")
slSonetSlReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetSlReceived.setReference('GR-253-CORE')
if mibBuilder.loadTexts: slSonetSlReceived.setStatus('current')
if mibBuilder.loadTexts: slSonetSlReceived.setDescription('This object is used to view the Sonet Signal Label that is\n\t\treceived by the receiving terminal.')
slSonetPosTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1), )
if mibBuilder.loadTexts: slSonetPosTable.setStatus('current')
if mibBuilder.loadTexts: slSonetPosTable.setDescription('The POS PM Table.')
slSonetPosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slSonetPosEntry.setStatus('current')
if mibBuilder.loadTexts: slSonetPosEntry.setDescription('The entries exist for active Trunk sonet lines \n\t\tifType = pos(171). The objects in this table are \n\t\tused to moitor the POS layer.')
slSonetPosFcs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetPosFcs.setStatus('current')
if mibBuilder.loadTexts: slSonetPosFcs.setDescription('The Number of FCS Errors.')
slSonetPosAbort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetPosAbort.setStatus('current')
if mibBuilder.loadTexts: slSonetPosAbort.setDescription('The Number of Aborted packets.')
slSonetPosMinViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetPosMinViolation.setStatus('current')
if mibBuilder.loadTexts: slSonetPosMinViolation.setDescription('The Number of Minimum length violation packets.')
slSonetPosMaxViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetPosMaxViolation.setStatus('current')
if mibBuilder.loadTexts: slSonetPosMaxViolation.setDescription('The Number of Maximum length violation packets.')
slSonetPosRxfifoDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetPosRxfifoDiscard.setStatus('current')
if mibBuilder.loadTexts: slSonetPosRxfifoDiscard.setDescription('The Number of packets discarded due to RXFIFO error.')
slSonetPosPacketReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetPosPacketReceived.setStatus('current')
if mibBuilder.loadTexts: slSonetPosPacketReceived.setDescription('The Number of packets received.')
slSonetPosPacketReceivedOk = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetPosPacketReceivedOk.setStatus('current')
if mibBuilder.loadTexts: slSonetPosPacketReceivedOk.setDescription('The Number of error free packets.')
slSonetAlsTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1), )
if mibBuilder.loadTexts: slSonetAlsTable.setStatus('current')
if mibBuilder.loadTexts: slSonetAlsTable.setDescription('The ALS configuration Table.')
slSonetAlsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slSonetAlsEntry.setStatus('current')
if mibBuilder.loadTexts: slSonetAlsEntry.setDescription('The entries exist for active sonet lines \n\t\tifType = sonet(39). The objects in this table are \n\t\tused to configure the ALS algorithm.')
slSonetAlsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetAlsMode.setStatus('current')
if mibBuilder.loadTexts: slSonetAlsMode.setDescription("Enable/Disable the ALS algorithm.\n        Note that the if the Laser Admin Status is 'down' the\n        ALS mechanism is not operational.")
slSonetLosDeclareTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms500", 1), ("ms550", 2), ("ms600", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetLosDeclareTime.setStatus('current')
if mibBuilder.loadTexts: slSonetLosDeclareTime.setDescription('Time to declare optical LOS present or clear: 550 +- 50 msec.')
slSonetTestPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("s80", 1), ("s90", 2), ("s100", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetTestPulseTime.setStatus('current')
if mibBuilder.loadTexts: slSonetTestPulseTime.setDescription('Manual restart for test Pulse time (in manual restart) - 90+-10 sec.')
slSonetManualPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetManualPulseTime.setStatus('current')
if mibBuilder.loadTexts: slSonetManualPulseTime.setDescription('Manual restart Pulse time (in manual mode) - 2+-0.25 sec.')
slSonetAutomaticPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetAutomaticPulseTime.setStatus('current')
if mibBuilder.loadTexts: slSonetAutomaticPulseTime.setDescription('Automatic restart Pulse time (in automatic mode) - 2+-0.25 sec.')
slSonetAutomaticDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetAutomaticDelayTime.setStatus('current')
if mibBuilder.loadTexts: slSonetAutomaticDelayTime.setDescription('In Automatic mode. The delay between two laser re-activations.')
slSonetLaserTestActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetLaserTestActivate.setStatus('current')
if mibBuilder.loadTexts: slSonetLaserTestActivate.setDescription('Activate the laser for test operation.')
slSonetLaserManualActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetLaserManualActivate.setStatus('current')
if mibBuilder.loadTexts: slSonetLaserManualActivate.setDescription('Activate the laser manual operation.')
slSonetFsTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1), )
if mibBuilder.loadTexts: slSonetFsTable.setStatus('current')
if mibBuilder.loadTexts: slSonetFsTable.setDescription('The frame structure configuration Table.\n       In order to define a new path the NMS should create and configure\n       an entry in this table.\n       The table is also used to monitor the status of the LOP\n       alarm per path.')
slSonetFsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1), ).setIndexNames((0, "SL-SONET-MIB", "slSonetFsIfIndex"), (0, "SL-SONET-MIB", "slSonetFsSts"))
if mibBuilder.loadTexts: slSonetFsEntry.setStatus('current')
if mibBuilder.loadTexts: slSonetFsEntry.setDescription('The entries exist for sonet paths \n\t\tifType = sonet(39). The objects in this table are \n\t\tused to configure the frame structure.\n\t\tEach OC-N line interface shall maintain a static\n\t\ttable with number of lines equal to the N.\n\t\tInitially the table will be initialized to STS-Nc.')
slSonetFsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetFsIfIndex.setStatus('current')
if mibBuilder.loadTexts: slSonetFsIfIndex.setDescription('The interface index.')
slSonetFsSts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetFsSts.setStatus('current')
if mibBuilder.loadTexts: slSonetFsSts.setDescription('The number of the first STS in the path.\n\t\tNote that no all values are legal because there is no\n\t\tsupport for combus with mixed structure')
slSonetFsWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetFsWidth.setStatus('current')
if mibBuilder.loadTexts: slSonetFsWidth.setDescription("The number STS's in the path.\n\t\tThe width is only valid for the first STS in the path.\n\t\tThe other STSs of the path will have width=0.")
slSonetFsFullPathTermination = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetFsFullPathTermination.setStatus('current')
if mibBuilder.loadTexts: slSonetFsFullPathTermination.setDescription('FALSE - means partial path termination (only LOP alarm).\n\t\t TRUE  - include full support for path Alarms and PM counters.')
slSonetFsGranularity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vc4", 1), ("vc3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetFsGranularity.setStatus('current')
if mibBuilder.loadTexts: slSonetFsGranularity.setDescription('This value is set by the NMS according to the configured frame structure.\n\t\tEach VC-3 that is mapped to AUG-1 via VC-4 should have the value vc4(1).\n\t\tOtherwise the value should be vc3(2).')
slSonetFsTableChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 6, 11, 1)).setObjects(("SL-SONET-MIB", "slSonetFsIfIndex"))
if mibBuilder.loadTexts: slSonetFsTableChange.setStatus('current')
if mibBuilder.loadTexts: slSonetFsTableChange.setDescription('A slSonetFsTableChange trap is sent when the\n\t\tcontent of the slSonetFsTable is changed.\n\t\tThis trap may be used by the NMS to identify\n\t\tthe removal of path interfaces, or addition of\n\t\tnew path interfaces')
mibBuilder.exportSymbols("SL-SONET-MIB", slSonetPosMinViolation=slSonetPosMinViolation, slSonetAutomaticDelayTime=slSonetAutomaticDelayTime, slSonetFsSts=slSonetFsSts, slSonetSlEntry=slSonetSlEntry, slSonetSlReceived=slSonetSlReceived, slSonetConfigFrameScramble=slSonetConfigFrameScramble, slSonetFsTableChange=slSonetFsTableChange, slSonetPosAbort=slSonetPosAbort, slSonetAlsMode=slSonetAlsMode, slSonetTraceMode=slSonetTraceMode, slSonetResetPmThreshold=slSonetResetPmThreshold, slSonetPos=slSonetPos, slSonetFsIfIndex=slSonetFsIfIndex, slSonetOhSl=slSonetOhSl, slSonetTraceReceived=slSonetTraceReceived, slSonetPortThresholdTrapEnable=slSonetPortThresholdTrapEnable, slSonetTraceEntry=slSonetTraceEntry, slSonetLaserTestActivate=slSonetLaserTestActivate, slSonetTraceToTransmit=slSonetTraceToTransmit, slSonetSlToExpect=slSonetSlToExpect, slSonetPosFcs=slSonetPosFcs, slSonetFsEntry=slSonetFsEntry, slSonetAls=slSonetAls, slSonetConfigTable=slSonetConfigTable, slSonetAlsTable=slSonetAlsTable, slSonetFsTable=slSonetFsTable, SignalLabel=SignalLabel, slSonetSlFailure=slSonetSlFailure, slSonetLaserManualActivate=slSonetLaserManualActivate, slSonetFs=slSonetFs, slSonetOverheadTunneling=slSonetOverheadTunneling, slSonetResetAllCounters=slSonetResetAllCounters, slSonetPosPacketReceivedOk=slSonetPosPacketReceivedOk, slSonetOh=slSonetOh, slSonetTestPulseTime=slSonetTestPulseTime, slSonetPosRxfifoDiscard=slSonetPosRxfifoDiscard, slSonetConfigType=slSonetConfigType, slSonetConfigEntry=slSonetConfigEntry, slSonetConfigSfThreshold=slSonetConfigSfThreshold, slSonetTraceTable=slSonetTraceTable, slSonetConfigDccSelection=slSonetConfigDccSelection, slSonetTransceiverType=slSonetTransceiverType, slSonetAlsEntry=slSonetAlsEntry, slSonetFsGranularity=slSonetFsGranularity, slSonetFsApply=slSonetFsApply, slSonetTdmTrunk=slSonetTdmTrunk, slSonetReceivedLte=slSonetReceivedLte, slSonetTraceToExpect=slSonetTraceToExpect, slSonetPosPacketReceived=slSonetPosPacketReceived, slSonetAutomaticPulseTime=slSonetAutomaticPulseTime, slSonetOhTrace=slSonetOhTrace, slSonetTraceFailure=slSonetTraceFailure, slSonetOhTraps=slSonetOhTraps, slSonetPosTable=slSonetPosTable, slSonetTxLte=slSonetTxLte, slSonetConfig=slSonetConfig, slSonetResetAlsParams=slSonetResetAlsParams, slSonetTransceiverMedia=slSonetTransceiverMedia, slSonetFsWidth=slSonetFsWidth, slSonetSlTable=slSonetSlTable, slSonetMib=slSonetMib, slSonetPosEntry=slSonetPosEntry, slSonetConfigSdThreshold=slSonetConfigSdThreshold, slSonetPosMaxViolation=slSonetPosMaxViolation, slSonetSlToTransmit=slSonetSlToTransmit, slSonetLosDeclareTime=slSonetLosDeclareTime, slSonetCompression=slSonetCompression, slSonetLopBitmask=slSonetLopBitmask, slSonetManualPulseTime=slSonetManualPulseTime, PYSNMP_MODULE_ID=slSonetMib, slSonetTraps=slSonetTraps, slSonetFsFullPathTermination=slSonetFsFullPathTermination)
