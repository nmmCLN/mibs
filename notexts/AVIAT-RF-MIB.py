#
# PySNMP MIB module AVIAT-RF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-RF-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:29 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
AviatRfuSideBandType, AviatPowerLevel, AviatModulationType, AviatDecibel = mibBuilder.importSymbols("AVIAT-TEXTCONVENTION-MIB", "AviatRfuSideBandType", "AviatPowerLevel", "AviatModulationType", "AviatDecibel")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32, ModuleIdentity, Unsigned32, Gauge32, Bits, TimeTicks, Counter32, ObjectIdentity, NotificationType, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "Unsigned32", "Gauge32", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "NotificationType", "Counter64", "iso")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatRfModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 5))
aviatRfModule.setRevisions(('2015-11-05 14:30', '2015-07-29 08:45', '2015-02-10 09:48', '2015-01-27 02:46', '2014-11-07 02:47', '2014-01-21 01:57',))
if mibBuilder.loadTexts: aviatRfModule.setLastUpdated('201511051430Z')
if mibBuilder.loadTexts: aviatRfModule.setOrganization('Aviat Networks')
aviatRfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1))
aviatRfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 1))
aviatRfCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 2))
aviatRfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2))
aviatRfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1), )
if mibBuilder.loadTexts: aviatRfConfigTable.setStatus('current')
aviatRfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfConfigEntry.setStatus('current')
aviatRfFreqTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfFreqTx.setStatus('current')
aviatRfFreqRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfFreqRx.setStatus('current')
aviatRfPowerSet = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 3), AviatPowerLevel()).setUnits('0.1 dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfPowerSet.setStatus('current')
aviatRfTxMute = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfTxMute.setStatus('current')
aviatRfHighGain = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfHighGain.setStatus('current')
aviatRfBandSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upper5g8", 1), ("lower6g", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfBandSelection.setStatus('current')
aviatRfATPCTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2), )
if mibBuilder.loadTexts: aviatRfATPCTable.setStatus('current')
aviatRfATPCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfATPCEntry.setStatus('current')
aviatRfATPCEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCEnabled.setStatus('current')
aviatRfATPCTargetFadeMargin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 2), AviatDecibel().clone(100)).setUnits('0.1 dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCTargetFadeMargin.setStatus('current')
aviatRfATPCMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 3), AviatPowerLevel().clone(200)).setUnits('0.1 dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCMaximumPower.setStatus('current')
aviatRfATPCMinimumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 4), AviatPowerLevel()).setUnits('0.1 dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCMinimumPower.setStatus('current')
aviatRfATPCFCCCompliant = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRfATPCFCCCompliant.setStatus('current')
aviatRfuCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3), )
if mibBuilder.loadTexts: aviatRfuCapabilityTable.setStatus('current')
aviatRfuCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfuCapabilityEntry.setStatus('current')
aviatRfuTxFreqMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxFreqMax.setStatus('current')
aviatRfuTxFreqMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxFreqMin.setStatus('current')
aviatRfuRxFreqMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuRxFreqMax.setStatus('current')
aviatRfuRxFreqMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuRxFreqMin.setStatus('current')
aviatRfuFreqStepMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuFreqStepMin.setStatus('current')
aviatRfuBandwidthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuBandwidthMax.setStatus('current')
aviatRfuTxRxSpacingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxRxSpacingMax.setStatus('current')
aviatRfuTxRxSpacingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxRxSpacingMin.setStatus('current')
aviatRfuTxPowerMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxPowerMax.setStatus('current')
aviatRfuTxPowerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxPowerMin.setStatus('current')
aviatRfuPowerStep = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuPowerStep.setStatus('current')
aviatRfuNoiseFigure = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuNoiseFigure.setStatus('current')
aviatRfuModulationMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 13), AviatModulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuModulationMax.setStatus('current')
aviatRfuTxRxSpacingPreset = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxRxSpacingPreset.setStatus('current')
aviatRfuTxSideBand = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 15), AviatRfuSideBandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxSideBand.setStatus('current')
aviatRfuTxPowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxPowerLimit.setStatus('current')
aviatRfuTxSpacingTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4), )
if mibBuilder.loadTexts: aviatRfuTxSpacingTable.setStatus('current')
aviatRfuTxSpacingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-RF-MIB", "aviatRfuTxSpacingIndex"))
if mibBuilder.loadTexts: aviatRfuTxSpacingEntry.setStatus('current')
aviatRfuTxSpacingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1, 1), Gauge32())
if mibBuilder.loadTexts: aviatRfuTxSpacingIndex.setStatus('current')
aviatRfuTxSpacingFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuTxSpacingFreq.setStatus('current')
aviatRfuDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5), )
if mibBuilder.loadTexts: aviatRfuDetailsTable.setStatus('current')
aviatRfuDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRfuDetailsEntry.setStatus('current')
aviatRfuType = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuType.setStatus('current')
aviatRfuFreqBand = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuFreqBand.setStatus('current')
aviatRfuPowerAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuPowerAmp.setStatus('current')
aviatRfuSemiconductorTech = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("gaas", 0), ("gan", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuSemiconductorTech.setStatus('current')
aviatRfuUnlicensed5G8Cap = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuUnlicensed5G8Cap.setStatus('current')
aviatRfuExternalCoaxPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRfuExternalCoaxPresent.setStatus('current')
aviatRfObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 1, 1)).setObjects(("AVIAT-RF-MIB", "aviatRfFreqTx"), ("AVIAT-RF-MIB", "aviatRfFreqRx"), ("AVIAT-RF-MIB", "aviatRfPowerSet"), ("AVIAT-RF-MIB", "aviatRfTxMute"), ("AVIAT-RF-MIB", "aviatRfHighGain"), ("AVIAT-RF-MIB", "aviatRfBandSelection"), ("AVIAT-RF-MIB", "aviatRfATPCEnabled"), ("AVIAT-RF-MIB", "aviatRfATPCTargetFadeMargin"), ("AVIAT-RF-MIB", "aviatRfATPCMaximumPower"), ("AVIAT-RF-MIB", "aviatRfATPCMinimumPower"), ("AVIAT-RF-MIB", "aviatRfATPCFCCCompliant"), ("AVIAT-RF-MIB", "aviatRfuTxFreqMax"), ("AVIAT-RF-MIB", "aviatRfuTxFreqMin"), ("AVIAT-RF-MIB", "aviatRfuRxFreqMax"), ("AVIAT-RF-MIB", "aviatRfuRxFreqMin"), ("AVIAT-RF-MIB", "aviatRfuFreqStepMin"), ("AVIAT-RF-MIB", "aviatRfuBandwidthMax"), ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingMax"), ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingMin"), ("AVIAT-RF-MIB", "aviatRfuTxPowerMax"), ("AVIAT-RF-MIB", "aviatRfuTxPowerMin"), ("AVIAT-RF-MIB", "aviatRfuPowerStep"), ("AVIAT-RF-MIB", "aviatRfuNoiseFigure"), ("AVIAT-RF-MIB", "aviatRfuModulationMax"), ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingPreset"), ("AVIAT-RF-MIB", "aviatRfuTxSideBand"), ("AVIAT-RF-MIB", "aviatRfuTxPowerLimit"), ("AVIAT-RF-MIB", "aviatRfuTxSpacingFreq"), ("AVIAT-RF-MIB", "aviatRfuType"), ("AVIAT-RF-MIB", "aviatRfuFreqBand"), ("AVIAT-RF-MIB", "aviatRfuPowerAmp"), ("AVIAT-RF-MIB", "aviatRfuSemiconductorTech"), ("AVIAT-RF-MIB", "aviatRfuUnlicensed5G8Cap"), ("AVIAT-RF-MIB", "aviatRfuExternalCoaxPresent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRfObjectGroup = aviatRfObjectGroup.setStatus('current')
aviatRfComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 2, 1)).setObjects(("AVIAT-RF-MIB", "aviatRfObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRfComplV1 = aviatRfComplV1.setStatus('current')
mibBuilder.exportSymbols("AVIAT-RF-MIB", aviatRfHighGain=aviatRfHighGain, aviatRfuTxSpacingTable=aviatRfuTxSpacingTable, aviatRfComplV1=aviatRfComplV1, aviatRfuTxPowerMin=aviatRfuTxPowerMin, aviatRfuTxFreqMax=aviatRfuTxFreqMax, aviatRfATPCEntry=aviatRfATPCEntry, aviatRfuTxPowerLimit=aviatRfuTxPowerLimit, aviatRfuExternalCoaxPresent=aviatRfuExternalCoaxPresent, aviatRfuSemiconductorTech=aviatRfuSemiconductorTech, aviatRfATPCFCCCompliant=aviatRfATPCFCCCompliant, aviatRfuTxRxSpacingPreset=aviatRfuTxRxSpacingPreset, aviatRfuDetailsTable=aviatRfuDetailsTable, aviatRfATPCTargetFadeMargin=aviatRfATPCTargetFadeMargin, aviatRfPowerSet=aviatRfPowerSet, aviatRfuRxFreqMax=aviatRfuRxFreqMax, aviatRfConformance=aviatRfConformance, aviatRfBandSelection=aviatRfBandSelection, aviatRfuTxFreqMin=aviatRfuTxFreqMin, aviatRfuRxFreqMin=aviatRfuRxFreqMin, aviatRfuTxSpacingEntry=aviatRfuTxSpacingEntry, aviatRfuType=aviatRfuType, aviatRfuUnlicensed5G8Cap=aviatRfuUnlicensed5G8Cap, aviatRfObjectGroup=aviatRfObjectGroup, aviatRfModule=aviatRfModule, aviatRfFreqTx=aviatRfFreqTx, aviatRfuCapabilityTable=aviatRfuCapabilityTable, aviatRfuCapabilityEntry=aviatRfuCapabilityEntry, aviatRfuNoiseFigure=aviatRfuNoiseFigure, aviatRfuTxSpacingIndex=aviatRfuTxSpacingIndex, aviatRfGroups=aviatRfGroups, aviatRfCompliance=aviatRfCompliance, aviatRfuTxSpacingFreq=aviatRfuTxSpacingFreq, aviatRfMIBObjects=aviatRfMIBObjects, aviatRfuTxRxSpacingMin=aviatRfuTxRxSpacingMin, aviatRfuPowerAmp=aviatRfuPowerAmp, aviatRfuTxRxSpacingMax=aviatRfuTxRxSpacingMax, aviatRfTxMute=aviatRfTxMute, aviatRfATPCMinimumPower=aviatRfATPCMinimumPower, aviatRfuTxPowerMax=aviatRfuTxPowerMax, aviatRfuFreqStepMin=aviatRfuFreqStepMin, aviatRfuModulationMax=aviatRfuModulationMax, aviatRfuFreqBand=aviatRfuFreqBand, aviatRfATPCEnabled=aviatRfATPCEnabled, aviatRfuTxSideBand=aviatRfuTxSideBand, aviatRfConfigTable=aviatRfConfigTable, aviatRfuBandwidthMax=aviatRfuBandwidthMax, aviatRfATPCMaximumPower=aviatRfATPCMaximumPower, aviatRfuPowerStep=aviatRfuPowerStep, aviatRfuDetailsEntry=aviatRfuDetailsEntry, aviatRfFreqRx=aviatRfFreqRx, PYSNMP_MODULE_ID=aviatRfModule, aviatRfConfigEntry=aviatRfConfigEntry, aviatRfATPCTable=aviatRfATPCTable)
