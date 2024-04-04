#
# PySNMP MIB module SCTE-HMS-QAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/scte/SCTE-HMS-QAM-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:13:45 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
QAMChannelInterleaveMode, QAMChannelModulationFormat = mibBuilder.importSymbols("SCTE-HMS-HEADENDIDENT-TC-MIB", "QAMChannelInterleaveMode", "QAMChannelModulationFormat")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Integer32, Gauge32, enterprises, ModuleIdentity, NotificationType, TimeTicks, ObjectIdentity, iso, Counter32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Integer32", "Gauge32", "enterprises", "ModuleIdentity", "NotificationType", "TimeTicks", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
heDigitalQamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1))
heDigitalQamMIB.setRevisions(('2008-07-16 03:05', '2008-04-18 10:55', '2008-02-04 18:50', '2007-12-17 11:50', '2007-10-03 17:00', '2007-10-02 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: heDigitalQamMIB.setRevisionsDescriptions(('Updated Objects based on Comments at 7/11/08 meeting.\n\t\t1. Made QAMChannelInterleave mode an imported enumeration and used the\n\t\tvalues from the docsiFDownChannelInterleave enumeration.\n\t      2. Changed name of QAMModulationFormat to QAMChannelModulationFormat.\n\t\t3. Added unknown and other to qamChannelAnnexMode\n\t\t4. For consistency changed values names for qamChannelCommonOutputBw, \n\t\tqamChannelCommonUtilization to add the word Common to the names.\n\t    5. Changed description clause of qamConfigQamChannelIdMin and \n\t        qamConfigQamChannelIdMax to reference entPhysicalIndex. ', 'Renumbered objects in qamConfigTable to remove gaps.', 'Changes based on comments, \n\t\t1. Changed description of qamChannelPower.\n\t\t2. Added units to qamChannelOutputBw.\n\t\t3. Changed Units on qamChannelUtilization to 0.1 Percent.', 'Changes based on comments, \n\t\t1. Removed IpAddress import.\n\t\t2. Changed UNITS,comment, SYNTAX on qamChannelUtilization.', 'Added SCTE-HMS-HEADENDIDENT-TC name to file. Added\n\t\tQAMModulationFormat textual convention.', 'Prepare MIB for ballot.',))
if mibBuilder.loadTexts: heDigitalQamMIB.setLastUpdated('200807160305Z')
if mibBuilder.loadTexts: heDigitalQamMIB.setOrganization('SCTE HMS Working Group')
if mibBuilder.loadTexts: heDigitalQamMIB.setContactInfo('SCTE HMS Subcommittee, Chairman\n\t\tmailto:standards@scte.org ')
if mibBuilder.loadTexts: heDigitalQamMIB.setDescription("This MIB module is for representing Edge QAM equipment present \n                 in the headend (or indoor) and is supported by a SNMP agent.\n                 It defines QAM channel related configuration MIB objects \n                 associated with both QAM channel's physical and logical\n                 characteristics.\n                 \n                 qamChannelTable is optional for devices that are supporting \n                 equivalent DOCSIS MIB objects.\n\n                 qamConfigTable is optional and applies to devices that choose to \n                 provide logical level configuration. ")
qamMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1))
if mibBuilder.loadTexts: qamMIBObjects.setStatus('current')
if mibBuilder.loadTexts: qamMIBObjects.setDescription('This branch specifies the QAM MIB objects.')
qamMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2))
if mibBuilder.loadTexts: qamMIBConformance.setStatus('current')
if mibBuilder.loadTexts: qamMIBConformance.setDescription('This branch describes the different QAM MIB object groups and \n\t\tthe different level of compliance.')
qamMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1))
if mibBuilder.loadTexts: qamMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: qamMIBCompliances.setDescription('The different levels of compliance to the QAM MIB.')
qamMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2))
if mibBuilder.loadTexts: qamMIBGroups.setStatus('current')
if mibBuilder.loadTexts: qamMIBGroups.setDescription('The QAM MIB object groups.')
qamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1), )
if mibBuilder.loadTexts: qamChannelTable.setStatus('current')
if mibBuilder.loadTexts: qamChannelTable.setDescription('This table describes the configuration and attributes of each\n\t\tQAM channel of the QAM designated by ifIndex.')
qamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qamChannelEntry.setStatus('current')
if mibBuilder.loadTexts: qamChannelEntry.setDescription('There is an entry in the table for each QAM channel. The index \n\t\tto this table is the ifIndex of each QAM channel.')
qamChannelFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 1), Unsigned32()).setUnits('Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelFrequency.setStatus('current')
if mibBuilder.loadTexts: qamChannelFrequency.setDescription('The center frequency of the QAM channel.')
qamChannelModulationFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 2), QAMChannelModulationFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelModulationFormat.setStatus('current')
if mibBuilder.loadTexts: qamChannelModulationFormat.setDescription('RF Modululation for this output QAM channel when \n\t\tqamChannelContWaveMode is off.')
qamChannelInterleaverLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("level1", 1), ("level2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelInterleaverLevel.setStatus('current')
if mibBuilder.loadTexts: qamChannelInterleaverLevel.setDescription('The interleaver level for FEC coding. \n\t\t\n\t\tlevel1 - implies interleaver level 1\n\t\tlevel2 - implies interleaver level 2\n\t\t\n\t\tThis object is only valid when AnnexMode has the value annexB.')
qamChannelInterleaverMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 4), QAMChannelInterleaveMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelInterleaverMode.setReference('ITU-T J.83 Annex B.')
if mibBuilder.loadTexts: qamChannelInterleaverMode.setStatus('current')
if mibBuilder.loadTexts: qamChannelInterleaverMode.setDescription("The interleaving depth or operation mode of the interleaver.\t\t\n    'taps8Increment16':   protection 5.9/4.1 usec,\n                                    latency .22/.15 msec\n    'taps16Increment8':   protection 12/8.2 usec,\n                           latency .48/.33 msec\n    'taps32Increment4':   protection 24/16 usec,\n                           latency .98/.68 msec\n    'taps64Increment2':   protection 47/33 usec,\n                           latency 2/1.4 msec\n    'taps128Increment1':  protection 95/66 usec,\n                           latency 4/2.8 msec\n    'taps12increment17':  protection 18/14 usec,\n                           latency 0.43/0.32 msec\n    'taps128increment2':  protection 190/132 usec,\n                           latency 8/5.6 msec\n    'taps128increment3': protection 285/198 usec,\n                           latency 12/8.4 msec\n    'taps128increment4': protection 380/264 usec,\n                           latency 16/11 msec\n    'taps128increment5': protection 475/330 usec,\n                           latency 20/14 msec\n    'taps128increment6': protection 570/396 usec,\n                           latency 24/17 msec\n    'taps128increment7: protection 664/462 usec,\n                           latency 28/20 msec\n    'taps128increment8': protection 759/528 usec,\n                           latency 32/22 msec\n    \n    The value 'taps12increment17' is supported by EuroDOCSIS\n    cable systems only, and the others by DOCSIS cable systems.\n\n    If the QAM chammel interface is down, this object either \n    returns the configured value,\n    or the value of 'unknown'.\n    The value of 'other' is returned if the interleave\n    is known but not defined in the above list.\n    \n    When the qamChannelInterleaverLevel is set to 'level 1', a \n\t\tsingle interleaving depth is supported, namely 'taps128Increment1'.\n\t\t\n\t\tWhen the qamChannelInterleaverLevel is set to 'level2', all the \n\t\tother interleaving depths are also supported.")
qamChannelPower = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 5), Integer32()).setUnits('0.1 dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelPower.setStatus('current')
if mibBuilder.loadTexts: qamChannelPower.setDescription('The output power of the QAM channel. If the QAM channel is muted,\n\t\tvalue is not valid.')
qamChannelSquelch = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unmuted", 1), ("muted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelSquelch.setStatus('current')
if mibBuilder.loadTexts: qamChannelSquelch.setDescription('Indicates whether the QAM port is muted or not.')
qamChannelContWaveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cwmOff", 1), ("cwmOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelContWaveMode.setStatus('current')
if mibBuilder.loadTexts: qamChannelContWaveMode.setDescription('Indicates whether Continuous Wave mode is enabled or not for\n\t\toutput.')
qamChannelAnnexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("annexA", 3), ("annexB", 4), ("annexC", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelAnnexMode.setStatus('current')
if mibBuilder.loadTexts: qamChannelAnnexMode.setDescription('Specifies the ITU-T standard supported by the QAM channel\n\t\t\n\t\tannexA - standard specified by Annex A of ITU-T J.83\n\t\tannexB - standard specified by Annex B of ITU-T J.83\n\t\tannexC - standard specified by Annex C of ITU-T J.83\n\t\tOther  - other standard that may apply.')
qamChannelCommonTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2), )
if mibBuilder.loadTexts: qamChannelCommonTable.setStatus('current')
if mibBuilder.loadTexts: qamChannelCommonTable.setDescription('This table decribes MPEG and DOCSIS characteristics that are\n\t\tnot part of the DOCSIS-IF-MIB.')
qamChannelCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qamChannelCommonEntry.setStatus('current')
if mibBuilder.loadTexts: qamChannelCommonEntry.setDescription('Each entry of this table describes attributes of an RF channel\n\t\tfor both MPEG and DOCSIS QAMs.')
qamChannelCommonOutputBw = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1, 1), Integer32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelCommonOutputBw.setStatus('current')
if mibBuilder.loadTexts: qamChannelCommonOutputBw.setDescription('The QAM channel output bandwidth or capacity.')
qamChannelCommonUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1000), ))).setUnits('0.1 Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelCommonUtilization.setStatus('current')
if mibBuilder.loadTexts: qamChannelCommonUtilization.setDescription('The utilization of the QAM channel in 0.1 percentage.\n\t\tThis rate may be calculated as transport stream packets / \n\t\t( transport stream packets + null packets ). If not \n            applicable, a value of -1 is returned.')
qamConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3), )
if mibBuilder.loadTexts: qamConfigTable.setStatus('current')
if mibBuilder.loadTexts: qamConfigTable.setDescription("This table is designed to show the IP addresses configuration\n\t\tfor the QAM channels, optionally UDP port range, Program Number\n\t\trange associated with QAM channels. Configuring these parameters\n\t\tis necessary when performing session-based provisioning. A  \n\t\tsession-based provisioning request must conform to the\n\t\tconfigurations in this table. The QAM channels within an QAM \n\t\tdevice may be partitioned to support multiple UDP, QAM or\n\t\tProgramNo ranges. Though it's helpful to partition the QAM\n\t\tchannels when the total number of QAM channel increases, this is\n\t\tnot a must. This table may also be used to show the reserved UDP\n\t\tports, or program numbers for special purposes instead of using\n\t\tdefault ones allowed by hardware, software, or MPEG protocol.")
qamConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "SCTE-HMS-QAM-MIB", "qamConfigIndex"))
if mibBuilder.loadTexts: qamConfigEntry.setStatus('current')
if mibBuilder.loadTexts: qamConfigEntry.setDescription('Each entry corresponds to the configuration of a QAM channel\n\t\trange.')
qamConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: qamConfigIndex.setStatus('current')
if mibBuilder.loadTexts: qamConfigIndex.setDescription('The table index.')
qamConfigQamChannelIdMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 2), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigQamChannelIdMin.setStatus('current')
if mibBuilder.loadTexts: qamConfigQamChannelIdMin.setDescription('QAMChannelId maybe within a line card or global depending on\n\t\tentPhysicalIndex.')
qamConfigQamChannelIdMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigQamChannelIdMax.setStatus('current')
if mibBuilder.loadTexts: qamConfigQamChannelIdMax.setDescription('QAMChannelId maybe within a line card or global depending on\n\t\tentPhysicalIndex.')
qamConfigIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 4), InetAddressType().clone('ipv4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigIPAddrType.setStatus('current')
if mibBuilder.loadTexts: qamConfigIPAddrType.setDescription('The type of the program destination address as defined by \n\t\tinetAddressType. The default value is 1 for ipv4(1)')
qamConfigIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigIPAddr.setStatus('current')
if mibBuilder.loadTexts: qamConfigIPAddr.setDescription('IP address of the QAM channel.')
qamConfigUdpPortRangeMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigUdpPortRangeMin.setStatus('current')
if mibBuilder.loadTexts: qamConfigUdpPortRangeMin.setDescription('The lowest UDP port of the UDP port range that can be used\n\t\ton this QAM channel.')
qamConfigUdpPortRangeMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigUdpPortRangeMax.setStatus('current')
if mibBuilder.loadTexts: qamConfigUdpPortRangeMax.setDescription('The highest UDP port of the UDP port range that can be used on\n\t\tthis QAM channel.')
qamConfigOutputProgNoMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigOutputProgNoMin.setStatus('current')
if mibBuilder.loadTexts: qamConfigOutputProgNoMin.setDescription('The lowest MPEG output program number that can be used on the\n\t\tQAM channel.')
qamConfigOutputProgNoMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigOutputProgNoMax.setStatus('current')
if mibBuilder.loadTexts: qamConfigOutputProgNoMax.setDescription('The highest MPEG output program number that can be used on the\n\t\tQAM channel.')
qamSupport = ModuleCompliance((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1, 1)).setObjects(("SCTE-HMS-QAM-MIB", "qamChannelGroup"), ("SCTE-HMS-QAM-MIB", "qamConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamSupport = qamSupport.setStatus('current')
if mibBuilder.loadTexts: qamSupport.setDescription('These objects describe the support level for QAM.')
docsisSupport = ModuleCompliance((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1, 2)).setObjects(("SCTE-HMS-QAM-MIB", "qamMpegDocsisCommonGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsisSupport = docsisSupport.setStatus('current')
if mibBuilder.loadTexts: docsisSupport.setDescription('These objects are not covered by any DOCSIS MIB, but\n\t\tthey would need to be supported by a DOCSIS EQAM.')
qamMpegDocsisCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 1)).setObjects(("SCTE-HMS-QAM-MIB", "qamChannelCommonOutputBw"), ("SCTE-HMS-QAM-MIB", "qamChannelCommonUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamMpegDocsisCommonGroup = qamMpegDocsisCommonGroup.setStatus('current')
if mibBuilder.loadTexts: qamMpegDocsisCommonGroup.setDescription('These objects are not covered by any DOCSIS MIB. It is\n\t\tlegitimate for a DOCSIS QAM to support them.')
qamChannelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 2)).setObjects(("SCTE-HMS-QAM-MIB", "qamChannelFrequency"), ("SCTE-HMS-QAM-MIB", "qamChannelModulationFormat"), ("SCTE-HMS-QAM-MIB", "qamChannelInterleaverLevel"), ("SCTE-HMS-QAM-MIB", "qamChannelInterleaverMode"), ("SCTE-HMS-QAM-MIB", "qamChannelPower"), ("SCTE-HMS-QAM-MIB", "qamChannelSquelch"), ("SCTE-HMS-QAM-MIB", "qamChannelContWaveMode"), ("SCTE-HMS-QAM-MIB", "qamChannelAnnexMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamChannelGroup = qamChannelGroup.setStatus('current')
if mibBuilder.loadTexts: qamChannelGroup.setDescription('The objects characterizing the RF channel and that may be\n\t\tsupported by an equivalent DOCSIS MIB object.')
qamConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 3)).setObjects(("SCTE-HMS-QAM-MIB", "qamConfigQamChannelIdMin"), ("SCTE-HMS-QAM-MIB", "qamConfigQamChannelIdMax"), ("SCTE-HMS-QAM-MIB", "qamConfigIPAddrType"), ("SCTE-HMS-QAM-MIB", "qamConfigIPAddr"), ("SCTE-HMS-QAM-MIB", "qamConfigUdpPortRangeMin"), ("SCTE-HMS-QAM-MIB", "qamConfigUdpPortRangeMax"), ("SCTE-HMS-QAM-MIB", "qamConfigOutputProgNoMin"), ("SCTE-HMS-QAM-MIB", "qamConfigOutputProgNoMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamConfigGroup = qamConfigGroup.setStatus('current')
if mibBuilder.loadTexts: qamConfigGroup.setDescription('QAM configuration objects.')
mibBuilder.exportSymbols("SCTE-HMS-QAM-MIB", qamChannelContWaveMode=qamChannelContWaveMode, docsisSupport=docsisSupport, qamConfigUdpPortRangeMin=qamConfigUdpPortRangeMin, qamConfigOutputProgNoMin=qamConfigOutputProgNoMin, qamChannelGroup=qamChannelGroup, qamChannelCommonEntry=qamChannelCommonEntry, qamMIBCompliances=qamMIBCompliances, qamChannelCommonOutputBw=qamChannelCommonOutputBw, qamConfigTable=qamConfigTable, qamMpegDocsisCommonGroup=qamMpegDocsisCommonGroup, qamChannelModulationFormat=qamChannelModulationFormat, qamMIBGroups=qamMIBGroups, qamConfigQamChannelIdMin=qamConfigQamChannelIdMin, qamChannelCommonTable=qamChannelCommonTable, qamConfigQamChannelIdMax=qamConfigQamChannelIdMax, heDigitalQamMIB=heDigitalQamMIB, qamChannelEntry=qamChannelEntry, qamMIBObjects=qamMIBObjects, qamChannelTable=qamChannelTable, qamConfigIndex=qamConfigIndex, qamChannelPower=qamChannelPower, qamMIBConformance=qamMIBConformance, qamConfigIPAddr=qamConfigIPAddr, qamChannelCommonUtilization=qamChannelCommonUtilization, qamChannelInterleaverMode=qamChannelInterleaverMode, qamChannelSquelch=qamChannelSquelch, qamChannelInterleaverLevel=qamChannelInterleaverLevel, qamSupport=qamSupport, qamChannelFrequency=qamChannelFrequency, qamConfigUdpPortRangeMax=qamConfigUdpPortRangeMax, qamConfigOutputProgNoMax=qamConfigOutputProgNoMax, qamConfigEntry=qamConfigEntry, qamConfigGroup=qamConfigGroup, qamConfigIPAddrType=qamConfigIPAddrType, qamChannelAnnexMode=qamChannelAnnexMode, PYSNMP_MODULE_ID=heDigitalQamMIB)
