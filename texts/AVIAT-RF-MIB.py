#
# PySNMP MIB module AVIAT-RF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-RF-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:12 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
AviatModulationType, AviatDecibel, AviatPowerLevel, AviatRfuSideBandType = mibBuilder.importSymbols("AVIAT-TEXTCONVENTION-MIB", "AviatModulationType", "AviatDecibel", "AviatPowerLevel", "AviatRfuSideBandType")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, ObjectIdentity, Bits, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "ObjectIdentity", "Bits", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatRfModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 5))
aviatRfModule.setRevisions(('2015-11-05 14:30', '2015-07-29 08:45', '2015-02-10 09:48', '2015-01-27 02:46', '2014-11-07 02:47', '2014-01-21 01:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aviatRfModule.setRevisionsDescriptions(('Added Tx power limit capability.', 'Added side band and Tx Rx spacing capability indications.', 'Added external RF switch indication.', 'Added 5.8GHz/ L6GHz selection support.', 'Added Semiconductor Technology.', 'Initial Version.',))
if mibBuilder.loadTexts: aviatRfModule.setLastUpdated('201511051430Z')
if mibBuilder.loadTexts: aviatRfModule.setOrganization('Aviat Networks')
if mibBuilder.loadTexts: aviatRfModule.setContactInfo('Aviat Networks\n                         Customer Service\n\n                         Postal: 5200 Great America Parkway\n                                 Santa Clara\n                                 California 95054\n                                 United States of America\n\n                         Tel: 408 567 7000\n\n                         E-mail: mibsupport@aviatnet.com')
if mibBuilder.loadTexts: aviatRfModule.setDescription('This MIB module supports the RF Fault Management functions of\n                 the radio.')
aviatRfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1))
aviatRfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 1))
aviatRfCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 2))
aviatRfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2))
aviatRfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1), )
if mibBuilder.loadTexts: aviatRfConfigTable.setStatus('current')
if mibBuilder.loadTexts: aviatRfConfigTable.setDescription('A table containing the RF configuration objects for a\n                         particular entity of the system.')
aviatRfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: aviatRfConfigEntry.setDescription('This is a row in the RF configuration table.')
aviatRfFreqTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfFreqTx.setStatus('current')
if mibBuilder.loadTexts: aviatRfFreqTx.setDescription('This specifies the transmit frequency of the unit.')
aviatRfFreqRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfFreqRx.setStatus('current')
if mibBuilder.loadTexts: aviatRfFreqRx.setDescription('This specifies the receive frequency of the unit.')
aviatRfPowerSet = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 3), AviatPowerLevel()).setUnits('0.1 dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfPowerSet.setStatus('current')
if mibBuilder.loadTexts: aviatRfPowerSet.setDescription('This specifies the desired output power for the\n                         transmitter of the unit.')
aviatRfTxMute = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfTxMute.setStatus('current')
if mibBuilder.loadTexts: aviatRfTxMute.setDescription("This specifies the status of the factory mute of the\n                         unit. If set to TRUE, the transmitter output will be\n                         muted. It should be set to FALSE otherwise.\n\n                         This setting is 'ORed' with other conditions\n                         (including diagnostic functions and configuration\n                         validation) to control the transmitter output status.")
aviatRfHighGain = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfHighGain.setStatus('current')
if mibBuilder.loadTexts: aviatRfHighGain.setDescription('This specifies whether to assign a high power license\n                         to this RF interface. If set to TRUE a license has\n                         been assigned, FALSE otherwise.')
aviatRfBandSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upper5g8", 1), ("lower6g", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfBandSelection.setStatus('current')
if mibBuilder.loadTexts: aviatRfBandSelection.setDescription('This is used to select a sub-band within the frequency\n                         range of the attached RFU. It is intended to limit the\n                         frequencies available for configuration of the RFU.')
aviatRfATPCTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2), )
if mibBuilder.loadTexts: aviatRfATPCTable.setStatus('current')
if mibBuilder.loadTexts: aviatRfATPCTable.setDescription('A table containing the RF ATPC configuration objects\n                         for a particular entity of the system.')
aviatRfATPCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfATPCEntry.setStatus('current')
if mibBuilder.loadTexts: aviatRfATPCEntry.setDescription('This is a row in the RF ATPC table.')
aviatRfATPCEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCEnabled.setStatus('current')
if mibBuilder.loadTexts: aviatRfATPCEnabled.setDescription('This is the control to enable or disable the Automatic\n                         Transmit Power Control (ATPC) function on the unit.')
aviatRfATPCTargetFadeMargin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 2), AviatDecibel().clone(100)).setUnits('0.1 dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCTargetFadeMargin.setStatus('current')
if mibBuilder.loadTexts: aviatRfATPCTargetFadeMargin.setDescription('This specifies the desired nominal fade margin that\n                         the Automatic Transmit Power Control function should\n                         attempt to maintain.')
aviatRfATPCMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 3), AviatPowerLevel().clone(200)).setUnits('0.1 dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCMaximumPower.setStatus('current')
if mibBuilder.loadTexts: aviatRfATPCMaximumPower.setDescription('This specifies the maximum power level that the\n                         Automatic Transmit Power Control function may set.')
aviatRfATPCMinimumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 4), AviatPowerLevel()).setUnits('0.1 dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCMinimumPower.setStatus('current')
if mibBuilder.loadTexts: aviatRfATPCMinimumPower.setDescription('This specifies the minimum power level that the\n                         Automatic Transmit Power Control function may set.')
aviatRfATPCFCCCompliant = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCFCCCompliant.setStatus('current')
if mibBuilder.loadTexts: aviatRfATPCFCCCompliant.setDescription('This is the control to enable or disable the Federal\n                         Communications Commission (FCC) compliant Automatic\n                         Transmit Power Control function.')
aviatRfuCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3), )
if mibBuilder.loadTexts: aviatRfuCapabilityTable.setStatus('current')
if mibBuilder.loadTexts: aviatRfuCapabilityTable.setDescription('A table containing the capabilities of an attached\n                         RFU.')
aviatRfuCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfuCapabilityEntry.setStatus('current')
if mibBuilder.loadTexts: aviatRfuCapabilityEntry.setDescription('This is a row in the RFU capabilities table.')
aviatRfuTxFreqMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxFreqMax.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxFreqMax.setDescription('The RFU maximum transmit frequency capability.')
aviatRfuTxFreqMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxFreqMin.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxFreqMin.setDescription('The RFU minimum Tx frequency capability.')
aviatRfuRxFreqMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuRxFreqMax.setStatus('current')
if mibBuilder.loadTexts: aviatRfuRxFreqMax.setDescription('The RFU maximum Rx frequency capability.')
aviatRfuRxFreqMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuRxFreqMin.setStatus('current')
if mibBuilder.loadTexts: aviatRfuRxFreqMin.setDescription('The RFU minimum Rx frequency capability.')
aviatRfuFreqStepMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuFreqStepMin.setStatus('current')
if mibBuilder.loadTexts: aviatRfuFreqStepMin.setDescription('The RFU minimum frequency step size capability.')
aviatRfuBandwidthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuBandwidthMax.setStatus('current')
if mibBuilder.loadTexts: aviatRfuBandwidthMax.setDescription('The RFU maximum bandwidth capability.')
aviatRfuTxRxSpacingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxRxSpacingMax.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxRxSpacingMax.setDescription('The RFU maximum Tx Rx spacing capability.')
aviatRfuTxRxSpacingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxRxSpacingMin.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxRxSpacingMin.setDescription('The RFU minimum Tx Rx spacing capability.')
aviatRfuTxPowerMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxPowerMax.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxPowerMax.setDescription('The RFU maximum Tx power capability.')
aviatRfuTxPowerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxPowerMin.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxPowerMin.setDescription('The RFU minimum Tx power capability.')
aviatRfuPowerStep = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuPowerStep.setStatus('current')
if mibBuilder.loadTexts: aviatRfuPowerStep.setDescription('The RFU power step capability.')
aviatRfuNoiseFigure = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuNoiseFigure.setStatus('current')
if mibBuilder.loadTexts: aviatRfuNoiseFigure.setDescription('The RFU noise figure capability.')
aviatRfuModulationMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 13), AviatModulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuModulationMax.setStatus('current')
if mibBuilder.loadTexts: aviatRfuModulationMax.setDescription('This RFU maximum modulation capability.')
aviatRfuTxRxSpacingPreset = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxRxSpacingPreset.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxRxSpacingPreset.setDescription('Indicates if the valid RFU Tx Rx spacing range is limited\n                         to the preset values provided by aviatRfuTxSpacingTable.')
aviatRfuTxSideBand = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 15), AviatRfuSideBandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxSideBand.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxSideBand.setDescription('Indicates the RFU side band.')
aviatRfuTxPowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxPowerLimit.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxPowerLimit.setDescription('RFU maximum Tx power limit for any modulation.')
aviatRfuTxSpacingTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4), )
if mibBuilder.loadTexts: aviatRfuTxSpacingTable.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxSpacingTable.setDescription('A table containing the allowed spacings for an\n                         attached RFU.')
aviatRfuTxSpacingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-RF-MIB", "aviatRfuTxSpacingIndex"))
if mibBuilder.loadTexts: aviatRfuTxSpacingEntry.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxSpacingEntry.setDescription('This is a row in the RFU Tx spacing table.')
aviatRfuTxSpacingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1, 1), Gauge32())
if mibBuilder.loadTexts: aviatRfuTxSpacingIndex.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxSpacingIndex.setDescription('An index representing a TxRx Spacing entry for an\n                         entity.')
aviatRfuTxSpacingFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxSpacingFreq.setStatus('current')
if mibBuilder.loadTexts: aviatRfuTxSpacingFreq.setDescription('A TxRx spacing entry valid for the system.')
aviatRfuDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5), )
if mibBuilder.loadTexts: aviatRfuDetailsTable.setStatus('current')
if mibBuilder.loadTexts: aviatRfuDetailsTable.setDescription('A table containing the details of an attached RFU.')
aviatRfuDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfuDetailsEntry.setStatus('current')
if mibBuilder.loadTexts: aviatRfuDetailsEntry.setDescription('This is a row in the RFU details table.')
aviatRfuType = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuType.setStatus('current')
if mibBuilder.loadTexts: aviatRfuType.setDescription('The type indentification of the attached RFU.')
aviatRfuFreqBand = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuFreqBand.setStatus('current')
if mibBuilder.loadTexts: aviatRfuFreqBand.setDescription('The frequency band indication of the attached RFU.')
aviatRfuPowerAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuPowerAmp.setStatus('current')
if mibBuilder.loadTexts: aviatRfuPowerAmp.setDescription('The power amplifier type of the attached RFU.')
aviatRfuSemiconductorTech = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("gaas", 0), ("gan", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuSemiconductorTech.setStatus('current')
if mibBuilder.loadTexts: aviatRfuSemiconductorTech.setDescription('The semiconductor technology used in the power\n                         amplifier of the attached RFU. This is used to\n                         determine whether IDQ optimization is necessary\n                         for GaN type devices.')
aviatRfuUnlicensed5G8Cap = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuUnlicensed5G8Cap.setStatus('current')
if mibBuilder.loadTexts: aviatRfuUnlicensed5G8Cap.setDescription('Indicates that a 5.8GHz capable RFU is attached. This\n                         unit can operate across frequency ranges which are\n                         unlicensed in some markets.')
aviatRfuExternalCoaxPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuExternalCoaxPresent.setStatus('current')
if mibBuilder.loadTexts: aviatRfuExternalCoaxPresent.setDescription('Indicates if an external RF switch is present.')
aviatRfObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 1, 1)).setObjects(("AVIAT-RF-MIB", "aviatRfFreqTx"), ("AVIAT-RF-MIB", "aviatRfFreqRx"), ("AVIAT-RF-MIB", "aviatRfPowerSet"), ("AVIAT-RF-MIB", "aviatRfTxMute"), ("AVIAT-RF-MIB", "aviatRfHighGain"), ("AVIAT-RF-MIB", "aviatRfBandSelection"), ("AVIAT-RF-MIB", "aviatRfATPCEnabled"), ("AVIAT-RF-MIB", "aviatRfATPCTargetFadeMargin"), ("AVIAT-RF-MIB", "aviatRfATPCMaximumPower"), ("AVIAT-RF-MIB", "aviatRfATPCMinimumPower"), ("AVIAT-RF-MIB", "aviatRfATPCFCCCompliant"), ("AVIAT-RF-MIB", "aviatRfuTxFreqMax"), ("AVIAT-RF-MIB", "aviatRfuTxFreqMin"), ("AVIAT-RF-MIB", "aviatRfuRxFreqMax"), ("AVIAT-RF-MIB", "aviatRfuRxFreqMin"), ("AVIAT-RF-MIB", "aviatRfuFreqStepMin"), ("AVIAT-RF-MIB", "aviatRfuBandwidthMax"), ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingMax"), ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingMin"), ("AVIAT-RF-MIB", "aviatRfuTxPowerMax"), ("AVIAT-RF-MIB", "aviatRfuTxPowerMin"), ("AVIAT-RF-MIB", "aviatRfuPowerStep"), ("AVIAT-RF-MIB", "aviatRfuNoiseFigure"), ("AVIAT-RF-MIB", "aviatRfuModulationMax"), ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingPreset"), ("AVIAT-RF-MIB", "aviatRfuTxSideBand"), ("AVIAT-RF-MIB", "aviatRfuTxPowerLimit"), ("AVIAT-RF-MIB", "aviatRfuTxSpacingFreq"), ("AVIAT-RF-MIB", "aviatRfuType"), ("AVIAT-RF-MIB", "aviatRfuFreqBand"), ("AVIAT-RF-MIB", "aviatRfuPowerAmp"), ("AVIAT-RF-MIB", "aviatRfuSemiconductorTech"), ("AVIAT-RF-MIB", "aviatRfuUnlicensed5G8Cap"), ("AVIAT-RF-MIB", "aviatRfuExternalCoaxPresent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRfObjectGroup = aviatRfObjectGroup.setStatus('current')
if mibBuilder.loadTexts: aviatRfObjectGroup.setDescription('These objects specify the RF capabilities and settings\n                         of the unit.')
aviatRfComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 2, 1)).setObjects(("AVIAT-RF-MIB", "aviatRfObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRfComplV1 = aviatRfComplV1.setStatus('current')
if mibBuilder.loadTexts: aviatRfComplV1.setDescription('The implementation requirements for this MIB.')
mibBuilder.exportSymbols("AVIAT-RF-MIB", aviatRfTxMute=aviatRfTxMute, aviatRfComplV1=aviatRfComplV1, aviatRfuTxFreqMin=aviatRfuTxFreqMin, aviatRfuType=aviatRfuType, aviatRfuUnlicensed5G8Cap=aviatRfuUnlicensed5G8Cap, aviatRfuTxSideBand=aviatRfuTxSideBand, aviatRfuModulationMax=aviatRfuModulationMax, aviatRfuFreqStepMin=aviatRfuFreqStepMin, aviatRfConfigEntry=aviatRfConfigEntry, aviatRfATPCTable=aviatRfATPCTable, aviatRfuTxRxSpacingMax=aviatRfuTxRxSpacingMax, aviatRfuTxRxSpacingPreset=aviatRfuTxRxSpacingPreset, aviatRfuFreqBand=aviatRfuFreqBand, aviatRfuRxFreqMax=aviatRfuRxFreqMax, aviatRfATPCTargetFadeMargin=aviatRfATPCTargetFadeMargin, aviatRfuTxPowerLimit=aviatRfuTxPowerLimit, aviatRfPowerSet=aviatRfPowerSet, aviatRfuCapabilityEntry=aviatRfuCapabilityEntry, aviatRfuTxSpacingFreq=aviatRfuTxSpacingFreq, aviatRfATPCFCCCompliant=aviatRfATPCFCCCompliant, aviatRfBandSelection=aviatRfBandSelection, aviatRfuSemiconductorTech=aviatRfuSemiconductorTech, aviatRfuRxFreqMin=aviatRfuRxFreqMin, aviatRfATPCMaximumPower=aviatRfATPCMaximumPower, aviatRfFreqTx=aviatRfFreqTx, aviatRfuTxRxSpacingMin=aviatRfuTxRxSpacingMin, aviatRfModule=aviatRfModule, aviatRfuTxSpacingTable=aviatRfuTxSpacingTable, aviatRfATPCEnabled=aviatRfATPCEnabled, aviatRfATPCMinimumPower=aviatRfATPCMinimumPower, aviatRfHighGain=aviatRfHighGain, aviatRfuTxPowerMax=aviatRfuTxPowerMax, aviatRfuCapabilityTable=aviatRfuCapabilityTable, aviatRfObjectGroup=aviatRfObjectGroup, aviatRfConformance=aviatRfConformance, aviatRfConfigTable=aviatRfConfigTable, PYSNMP_MODULE_ID=aviatRfModule, aviatRfuPowerStep=aviatRfuPowerStep, aviatRfuTxSpacingEntry=aviatRfuTxSpacingEntry, aviatRfuTxFreqMax=aviatRfuTxFreqMax, aviatRfuDetailsEntry=aviatRfuDetailsEntry, aviatRfuExternalCoaxPresent=aviatRfuExternalCoaxPresent, aviatRfATPCEntry=aviatRfATPCEntry, aviatRfuPowerAmp=aviatRfuPowerAmp, aviatRfGroups=aviatRfGroups, aviatRfuBandwidthMax=aviatRfuBandwidthMax, aviatRfuNoiseFigure=aviatRfuNoiseFigure, aviatRfuTxPowerMin=aviatRfuTxPowerMin, aviatRfuDetailsTable=aviatRfuDetailsTable, aviatRfCompliance=aviatRfCompliance, aviatRfFreqRx=aviatRfFreqRx, aviatRfuTxSpacingIndex=aviatRfuTxSpacingIndex, aviatRfMIBObjects=aviatRfMIBObjects)
