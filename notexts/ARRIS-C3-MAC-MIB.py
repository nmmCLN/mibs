#
# PySNMP MIB module ARRIS-C3-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-MAC-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:26 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
TenthdB, TenthdBmV = mibBuilder.importSymbols("DOCS-IF-MIB", "TenthdB", "TenthdBmV")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, TimeTicks, NotificationType, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter64, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "Counter32")
TruthValue, DisplayString, TextualConvention, TimeInterval, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "TimeInterval", "RowStatus")
cmtsC3MACMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6))
cmtsC3MACMIB.setRevisions(('2004-11-21 00:00', '2004-11-26 00:00', '2004-12-03 00:00',))
if mibBuilder.loadTexts: cmtsC3MACMIB.setLastUpdated('200412030000Z')
if mibBuilder.loadTexts: cmtsC3MACMIB.setOrganization('Arris International')
class DocsisMacType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("docsis", 1), ("euroDocsis", 2), ("mixed", 3), ("custom", 4))

dcxMACObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1))
dcxMACCmtsMacTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1), )
if mibBuilder.loadTexts: dcxMACCmtsMacTable.setStatus('current')
dcxMACCmtsMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dcxMACCmtsMacEntry.setStatus('current')
dcxMACCmtsMacMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 1), DocsisMacType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACCmtsMacMode.setStatus('current')
dcxMACCableAdvanceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("static", 0), ("dynamic", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACCableAdvanceType.setStatus('current')
dcxMACPlantLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 161))).setUnits('kilometers').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACPlantLength.setStatus('current')
dcxMACFlapAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 864000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACFlapAgingTime.setStatus('current')
dcxMACFlapInsertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACFlapInsertTime.setStatus('current')
dcxMACFlapMissThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setUnits('misses').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACFlapMissThresh.setStatus('current')
dcxMACFlapListSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 6000))).setUnits('entries').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACFlapListSize.setStatus('current')
dcxMACCmOfflineAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3600, 864000)).clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACCmOfflineAgingTime.setStatus('current')
dcxMACUccMaxFailedAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 10), Unsigned32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUccMaxFailedAttempts.setStatus('current')
dcxMACDownstreamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2), )
if mibBuilder.loadTexts: dcxMACDownstreamChannelTable.setStatus('current')
dcxMACDownstreamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dcxMACDownstreamChannelEntry.setStatus('current')
dcxMACDownChannelMacMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 1), DocsisMacType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACDownChannelMacMode.setStatus('current')
dcxMACDownChannelUpconverter = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("external", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACDownChannelUpconverter.setStatus('current')
dcxMACDownChannelIfFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10000000, 60000000))).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACDownChannelIfFrequency.setStatus('current')
dcxMACDownChannelWirelessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACDownChannelWirelessMode.setStatus('current')
dcxMACDownChannelSymbolRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1250000, 6952000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACDownChannelSymbolRate.setStatus('current')
dcxMACDownChannelAlpha = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 6), Integer32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxMACDownChannelAlpha.setStatus('current')
dcxMACUpstreamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3), )
if mibBuilder.loadTexts: dcxMACUpstreamChannelTable.setStatus('current')
dcxMACUpstreamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dcxMACUpstreamChannelEntry.setStatus('current')
dcxMACUpChannelMacMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 1), DocsisMacType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelMacMode.setStatus('current')
dcxMACUpChannelAmpAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 2), TenthdBmV()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelAmpAttenuation.setStatus('current')
dcxMACUpChannelIngressCancellation = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("tdmaOnly", 2), ("scdmaSec", 3), ("scdmaInc1", 4), ("scdmaInc2", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelIngressCancellation.setStatus('current')
dcxMACUpChannelGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelGroupId.setStatus('current')
dcxMACUpChannelShortPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 5), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelShortPollInterval.setStatus('current')
dcxMACUpChannelPeriodicPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 6), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(100, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelPeriodicPollInterval.setStatus('current')
dcxMACUpChannelInputPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("automatic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelInputPowerMode.setStatus('current')
dcxMACUpChannelPower = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 8), TenthdBmV()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelPower.setStatus('current')
dcxMACUpChannelPlantLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 320))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelPlantLength.setStatus('current')
dcxMACUpChannelMaxCmMapProcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelMaxCmMapProcTime.setStatus('current')
dcxMACUpChannelConcatenation = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelConcatenation.setStatus('current')
dcxMACUpChannelSpMgtTriggerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelSpMgtTriggerIndex.setStatus('current')
dcxMACUpChannelLowPowerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 13), TenthdBmV().subtype(subtypeSpec=ValueRangeConstraint(-100, -10)).clone(-60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelLowPowerOffset.setStatus('current')
dcxMACUpChannelHighPowerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 14), TenthdBmV().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelHighPowerOffset.setStatus('current')
dcxMACUpChannelLogSnrAveTimeconstant = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelLogSnrAveTimeconstant.setStatus('current')
dcxMACUpChannelImpulseMitigation = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelImpulseMitigation.setStatus('current')
dcxMACUpChannelRngPreambleGuardSymbols = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 17), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelRngPreambleGuardSymbols.setStatus('current')
dcxMACUpChannelNrngPreambleGuardSymbols = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 18), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelNrngPreambleGuardSymbols.setStatus('current')
dcxMACUpChannelExtendedFrequencyErrorDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("initialRanging", 1), ("periodicRanging", 2), ("allRanging", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelExtendedFrequencyErrorDetect.setStatus('current')
dcxMACUpChannelLogC3SnrTimeconstant = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 20), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelLogC3SnrTimeconstant.setStatus('current')
dcxMACUpChannelSignalNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 21), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxMACUpChannelSignalNoise.setStatus('current')
dcxMACUpChannelSafeConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 22), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelSafeConfig.setStatus('current')
dcxMACUpChannelInitialRangingDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(300, 3000))).setUnits('microseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxMACUpChannelInitialRangingDelay.setStatus('current')
dcxMACUpstreamGroupTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4), )
if mibBuilder.loadTexts: dcxMACUpstreamGroupTable.setStatus('current')
dcxMACUpstreamGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1), ).setIndexNames((0, "ARRIS-C3-MAC-MIB", "dcxMACUpstreamGroupId"))
if mibBuilder.loadTexts: dcxMACUpstreamGroupEntry.setStatus('current')
dcxMACUpstreamGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: dcxMACUpstreamGroupId.setStatus('current')
dcxMACUpstreamGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamGroupName.setStatus('current')
dcxMACUpstreamGroupLoadBalancing = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("initialNumeric", 2), ("periodic", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamGroupLoadBalancing.setStatus('current')
dcxMACUpstreamGroupFrequencyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamGroupFrequencyIndex.setStatus('current')
dcxMACUpstreamGroupSpMgtTriggerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamGroupSpMgtTriggerIndex.setStatus('current')
dcxMACUpstreamGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamGroupStatus.setStatus('current')
dcxMACUpstreamFrequencyTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5), )
if mibBuilder.loadTexts: dcxMACUpstreamFrequencyTable.setStatus('current')
dcxMACUpstreamFrequencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1), ).setIndexNames((0, "ARRIS-C3-MAC-MIB", "dcxMACUpstreamFrequencyIndex"), (0, "ARRIS-C3-MAC-MIB", "dcxMACUpstreamFrequencyRegion"))
if mibBuilder.loadTexts: dcxMACUpstreamFrequencyEntry.setStatus('current')
dcxMACUpstreamFrequencyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: dcxMACUpstreamFrequencyIndex.setStatus('current')
dcxMACUpstreamFrequencyRegion = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: dcxMACUpstreamFrequencyRegion.setStatus('current')
dcxMACUpstreamFrequencyStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 3), Integer32()).setUnits('hertz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamFrequencyStart.setStatus('current')
dcxMACUpstreamFrequencyStop = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 4), Integer32()).setUnits('hertz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamFrequencyStop.setStatus('current')
dcxMACUpstreamFrequencyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACUpstreamFrequencyStatus.setStatus('current')
dcxMACSpectralMgtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6))
dcxMACSpectralMgtTriggerTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1), )
if mibBuilder.loadTexts: dcxMACSpectralMgtTriggerTable.setStatus('current')
dcxMACSpectralMgtTriggerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1), ).setIndexNames((0, "ARRIS-C3-MAC-MIB", "dcxMACSpMgtTriggerIndex"), (0, "ARRIS-C3-MAC-MIB", "dcxMACSpMgtTriggerNumber"))
if mibBuilder.loadTexts: dcxMACSpectralMgtTriggerEntry.setStatus('current')
dcxMACSpMgtTriggerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: dcxMACSpMgtTriggerIndex.setStatus('current')
dcxMACSpMgtTriggerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: dcxMACSpMgtTriggerNumber.setStatus('current')
dcxMACSpMgtTriggerType = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerType.setStatus('current')
dcxMACSpMgtTriggerAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerAction.setStatus('current')
dcxMACSpMgtTriggerParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam1.setStatus('current')
dcxMACSpMgtTriggerParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam2.setStatus('current')
dcxMACSpMgtTriggerParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam3.setStatus('current')
dcxMACSpMgtTriggerParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam4.setStatus('current')
dcxMACSpMgtTriggerParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam5.setStatus('current')
dcxMACSpMgtTriggerParam6 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam6.setStatus('current')
dcxMACSpMgtTriggerParam7 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam7.setStatus('current')
dcxMACSpMgtTriggerParam8 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerParam8.setStatus('current')
dcxMACSpMgtTriggerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtTriggerStatus.setStatus('current')
dcxMACSpectralMgtActionTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2), )
if mibBuilder.loadTexts: dcxMACSpectralMgtActionTable.setStatus('current')
dcxMACSpectralMgtActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1), ).setIndexNames((0, "ARRIS-C3-MAC-MIB", "dcxMACSpMgtActionIndex"))
if mibBuilder.loadTexts: dcxMACSpectralMgtActionEntry.setStatus('current')
dcxMACSpMgtActionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: dcxMACSpMgtActionIndex.setStatus('current')
dcxMACSpMgtActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionType.setStatus('current')
dcxMACSpMgtActionParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam1.setStatus('current')
dcxMACSpMgtActionParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam2.setStatus('current')
dcxMACSpMgtActionParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam3.setStatus('current')
dcxMACSpMgtActionParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam4.setStatus('current')
dcxMACSpMgtActionParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam5.setStatus('current')
dcxMACSpMgtActionParam6 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam6.setStatus('current')
dcxMACSpMgtActionParam7 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam7.setStatus('current')
dcxMACSpMgtActionParam8 = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionParam8.setStatus('current')
dcxMACSpMgtActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSpMgtActionStatus.setStatus('current')
dcxMACSharedSecretTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7), )
if mibBuilder.loadTexts: dcxMACSharedSecretTable.setStatus('current')
dcxMACSharedSecretEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ARRIS-C3-MAC-MIB", "dcxMACSharedSecretId"))
if mibBuilder.loadTexts: dcxMACSharedSecretEntry.setStatus('current')
dcxMACSharedSecretId = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: dcxMACSharedSecretId.setStatus('current')
dcxMACSharedSecretStr = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSharedSecretStr.setStatus('current')
dcxMACSharedSecretStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxMACSharedSecretStatus.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-MAC-MIB", dcxMACUpstreamGroupEntry=dcxMACUpstreamGroupEntry, dcxMACUpstreamFrequencyStart=dcxMACUpstreamFrequencyStart, dcxMACCmOfflineAgingTime=dcxMACCmOfflineAgingTime, dcxMACSpMgtActionStatus=dcxMACSpMgtActionStatus, dcxMACDownChannelUpconverter=dcxMACDownChannelUpconverter, dcxMACFlapListSize=dcxMACFlapListSize, dcxMACUpstreamFrequencyRegion=dcxMACUpstreamFrequencyRegion, dcxMACSpectralMgtActionEntry=dcxMACSpectralMgtActionEntry, dcxMACObjects=dcxMACObjects, dcxMACFlapAgingTime=dcxMACFlapAgingTime, dcxMACUpstreamGroupSpMgtTriggerIndex=dcxMACUpstreamGroupSpMgtTriggerIndex, dcxMACUpChannelSignalNoise=dcxMACUpChannelSignalNoise, dcxMACDownChannelSymbolRate=dcxMACDownChannelSymbolRate, dcxMACSpMgtTriggerParam3=dcxMACSpMgtTriggerParam3, dcxMACUpstreamGroupFrequencyIndex=dcxMACUpstreamGroupFrequencyIndex, dcxMACSpMgtActionParam4=dcxMACSpMgtActionParam4, dcxMACSharedSecretStr=dcxMACSharedSecretStr, dcxMACSpMgtTriggerParam4=dcxMACSpMgtTriggerParam4, dcxMACSpMgtTriggerParam8=dcxMACSpMgtTriggerParam8, dcxMACUpChannelSpMgtTriggerIndex=dcxMACUpChannelSpMgtTriggerIndex, dcxMACSpMgtActionParam1=dcxMACSpMgtActionParam1, dcxMACUpChannelPeriodicPollInterval=dcxMACUpChannelPeriodicPollInterval, dcxMACUpChannelMaxCmMapProcTime=dcxMACUpChannelMaxCmMapProcTime, dcxMACSpMgtTriggerParam7=dcxMACSpMgtTriggerParam7, dcxMACSpMgtActionParam6=dcxMACSpMgtActionParam6, dcxMACUpstreamChannelEntry=dcxMACUpstreamChannelEntry, dcxMACUpChannelHighPowerOffset=dcxMACUpChannelHighPowerOffset, dcxMACUpstreamGroupId=dcxMACUpstreamGroupId, dcxMACCmtsMacTable=dcxMACCmtsMacTable, dcxMACSpMgtTriggerStatus=dcxMACSpMgtTriggerStatus, dcxMACUpstreamGroupLoadBalancing=dcxMACUpstreamGroupLoadBalancing, dcxMACUpChannelAmpAttenuation=dcxMACUpChannelAmpAttenuation, dcxMACUpChannelSafeConfig=dcxMACUpChannelSafeConfig, dcxMACSpectralMgtTriggerTable=dcxMACSpectralMgtTriggerTable, dcxMACCableAdvanceType=dcxMACCableAdvanceType, dcxMACUpChannelIngressCancellation=dcxMACUpChannelIngressCancellation, dcxMACSpMgtActionParam7=dcxMACSpMgtActionParam7, dcxMACSpMgtActionParam8=dcxMACSpMgtActionParam8, dcxMACSpMgtActionParam3=dcxMACSpMgtActionParam3, dcxMACUpChannelLogSnrAveTimeconstant=dcxMACUpChannelLogSnrAveTimeconstant, dcxMACSpMgtTriggerType=dcxMACSpMgtTriggerType, dcxMACSpectralMgtTriggerEntry=dcxMACSpectralMgtTriggerEntry, dcxMACUpChannelLowPowerOffset=dcxMACUpChannelLowPowerOffset, dcxMACUccMaxFailedAttempts=dcxMACUccMaxFailedAttempts, dcxMACUpstreamFrequencyIndex=dcxMACUpstreamFrequencyIndex, dcxMACSpMgtActionParam5=dcxMACSpMgtActionParam5, dcxMACSharedSecretTable=dcxMACSharedSecretTable, dcxMACSpMgtActionParam2=dcxMACSpMgtActionParam2, dcxMACUpChannelNrngPreambleGuardSymbols=dcxMACUpChannelNrngPreambleGuardSymbols, dcxMACSpMgtActionIndex=dcxMACSpMgtActionIndex, dcxMACUpChannelLogC3SnrTimeconstant=dcxMACUpChannelLogC3SnrTimeconstant, dcxMACUpChannelInitialRangingDelay=dcxMACUpChannelInitialRangingDelay, dcxMACSpMgtTriggerParam6=dcxMACSpMgtTriggerParam6, dcxMACSpMgtActionType=dcxMACSpMgtActionType, dcxMACUpChannelConcatenation=dcxMACUpChannelConcatenation, dcxMACSpMgtTriggerParam5=dcxMACSpMgtTriggerParam5, dcxMACDownstreamChannelEntry=dcxMACDownstreamChannelEntry, dcxMACUpChannelRngPreambleGuardSymbols=dcxMACUpChannelRngPreambleGuardSymbols, dcxMACUpChannelPlantLength=dcxMACUpChannelPlantLength, dcxMACDownChannelMacMode=dcxMACDownChannelMacMode, dcxMACUpstreamFrequencyEntry=dcxMACUpstreamFrequencyEntry, dcxMACDownChannelWirelessMode=dcxMACDownChannelWirelessMode, dcxMACUpstreamFrequencyTable=dcxMACUpstreamFrequencyTable, dcxMACUpstreamChannelTable=dcxMACUpstreamChannelTable, dcxMACSharedSecretStatus=dcxMACSharedSecretStatus, dcxMACUpChannelInputPowerMode=dcxMACUpChannelInputPowerMode, dcxMACSpMgtTriggerNumber=dcxMACSpMgtTriggerNumber, dcxMACUpChannelGroupId=dcxMACUpChannelGroupId, dcxMACSpMgtTriggerAction=dcxMACSpMgtTriggerAction, dcxMACUpstreamGroupName=dcxMACUpstreamGroupName, dcxMACFlapInsertTime=dcxMACFlapInsertTime, dcxMACUpChannelImpulseMitigation=dcxMACUpChannelImpulseMitigation, dcxMACUpChannelMacMode=dcxMACUpChannelMacMode, dcxMACUpstreamGroupStatus=dcxMACUpstreamGroupStatus, dcxMACUpChannelExtendedFrequencyErrorDetect=dcxMACUpChannelExtendedFrequencyErrorDetect, dcxMACSpectralMgtActionTable=dcxMACSpectralMgtActionTable, PYSNMP_MODULE_ID=cmtsC3MACMIB, dcxMACSpMgtTriggerParam2=dcxMACSpMgtTriggerParam2, DocsisMacType=DocsisMacType, dcxMACUpChannelShortPollInterval=dcxMACUpChannelShortPollInterval, dcxMACDownChannelAlpha=dcxMACDownChannelAlpha, cmtsC3MACMIB=cmtsC3MACMIB, dcxMACUpstreamFrequencyStop=dcxMACUpstreamFrequencyStop, dcxMACDownChannelIfFrequency=dcxMACDownChannelIfFrequency, dcxMACCmtsMacEntry=dcxMACCmtsMacEntry, dcxMACSharedSecretId=dcxMACSharedSecretId, dcxMACDownstreamChannelTable=dcxMACDownstreamChannelTable, dcxMACPlantLength=dcxMACPlantLength, dcxMACCmtsMacMode=dcxMACCmtsMacMode, dcxMACSpectralMgtObjects=dcxMACSpectralMgtObjects, dcxMACUpstreamGroupTable=dcxMACUpstreamGroupTable, dcxMACSpMgtTriggerParam1=dcxMACSpMgtTriggerParam1, dcxMACUpChannelPower=dcxMACUpChannelPower, dcxMACUpstreamFrequencyStatus=dcxMACUpstreamFrequencyStatus, dcxMACSpMgtTriggerIndex=dcxMACSpMgtTriggerIndex, dcxMACFlapMissThresh=dcxMACFlapMissThresh, dcxMACSharedSecretEntry=dcxMACSharedSecretEntry)
