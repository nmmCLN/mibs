#
# PySNMP MIB module ExtendAirG2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/ExtendAirG2
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:10 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
systemConfig, = mibBuilder.importSymbols("ExaltComProducts", "systemConfig")
RadioSourceT, AcmPowerBoostEnableT, ModulationT, DiplexerConfigG2T, RadioTxPwr11gT, BandwidthT, ExaltEnableT, AcmBaseModulationT, AcmPolicyT, BuzTimeoutT, AcmTargetModulationT = mibBuilder.importSymbols("ExaltComm", "RadioSourceT", "AcmPowerBoostEnableT", "ModulationT", "DiplexerConfigG2T", "RadioTxPwr11gT", "BandwidthT", "ExaltEnableT", "AcmBaseModulationT", "AcmPolicyT", "BuzTimeoutT", "AcmTargetModulationT")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Bits, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, TimeTicks, IpAddress, MibIdentifier, Unsigned32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "TimeTicks", "IpAddress", "MibIdentifier", "Unsigned32", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
extendAirG2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57))
extendAirG2.setRevisions(('2013-04-26 10:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: extendAirG2.setRevisionsDescriptions(('This is rev. 1.00',))
if mibBuilder.loadTexts: extendAirG2.setLastUpdated('201304261021Z')
if mibBuilder.loadTexts: extendAirG2.setOrganization('Exalt')
if mibBuilder.loadTexts: extendAirG2.setContactInfo('Exalt Wireless Inc.\n                            250 E Hacienda Ave.,\n                            Campbell, CA, 95008\n                            USA')
if mibBuilder.loadTexts: extendAirG2.setDescription('This is the Device Specific configuration for\n                            the ExtendAirG2 Licensed radio.')
extendAirG2TxPower = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 1), RadioTxPwr11gT()).setUnits('Tenths of dBm.').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2TxPower.setStatus('current')
if mibBuilder.loadTexts: extendAirG2TxPower.setDescription('The Transmit Power level multiplied by 10.0 -<g45><s11>')
extendAirG2Bandwidth = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 2), BandwidthT()).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2Bandwidth.setStatus('current')
if mibBuilder.loadTexts: extendAirG2Bandwidth.setDescription('The RF bandwidth. -<g47><s12 *1>')
extendAirG2Modulation = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 3), ModulationT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2Modulation.setStatus('current')
if mibBuilder.loadTexts: extendAirG2Modulation.setDescription('The Mode. -<g52><s14 *1>')
extendAirG2TXfrequency = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 9))).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2TXfrequency.setStatus('current')
if mibBuilder.loadTexts: extendAirG2TXfrequency.setDescription('The TX Frequency/ -<g46 TX><s15 TX>.')
extendAirG2RXfrequency = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 9))).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2RXfrequency.setStatus('current')
if mibBuilder.loadTexts: extendAirG2RXfrequency.setDescription('The RX Frequency/ -<g46 RX><s15 RX>.')
extendAirG2DiplexerConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 6), DiplexerConfigG2T()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2DiplexerConfiguration.setStatus('current')
if mibBuilder.loadTexts: extendAirG2DiplexerConfiguration.setDescription('The diplexer (label 701-802) configuration/ -<g310><s197>.')
extendAirG2InsertionLoss = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('Hundredth dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2InsertionLoss.setStatus('current')
if mibBuilder.loadTexts: extendAirG2InsertionLoss.setDescription("Inserion Loss is applicable for 'OTHER' diplexer entities only/ -<g528><s28 * 100>.")
extendAirG2BuzTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 8), BuzTimeoutT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2BuzTimeout.setStatus('current')
if mibBuilder.loadTexts: extendAirG2BuzTimeout.setDescription('This sets buzzer timeout period. User Options are: buzzer off, \n\t                     10 minutes or 2 hours.')
extendAirG2AcmMode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 9), ExaltEnableT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmMode.setStatus('current')
if mibBuilder.loadTexts: extendAirG2AcmMode.setDescription('ACM Mode enable/disable.')
extendAirG2AcmPolicy = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 10), AcmPolicyT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmPolicy.setStatus('current')
if mibBuilder.loadTexts: extendAirG2AcmPolicy.setDescription('The ACM Policy (Conservative/agressive).')
extendAirG2AcmBaseModulation = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 11), AcmBaseModulationT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmBaseModulation.setStatus('current')
if mibBuilder.loadTexts: extendAirG2AcmBaseModulation.setDescription('The ACM Base Mode.')
extendAirG2AcmTargetModulation = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 12), AcmTargetModulationT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmTargetModulation.setStatus('current')
if mibBuilder.loadTexts: extendAirG2AcmTargetModulation.setDescription('The ACM Target Mode.')
extendAirG2AcmPowerBoostMode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 15), AcmPowerBoostEnableT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmPowerBoostMode.setStatus('current')
if mibBuilder.loadTexts: extendAirG2AcmPowerBoostMode.setDescription('The ACM Power Boost Mode.')
mibBuilder.exportSymbols("ExtendAirG2", extendAirG2TXfrequency=extendAirG2TXfrequency, extendAirG2AcmPowerBoostMode=extendAirG2AcmPowerBoostMode, extendAirG2DiplexerConfiguration=extendAirG2DiplexerConfiguration, PYSNMP_MODULE_ID=extendAirG2, extendAirG2AcmTargetModulation=extendAirG2AcmTargetModulation, extendAirG2RXfrequency=extendAirG2RXfrequency, extendAirG2Modulation=extendAirG2Modulation, extendAirG2=extendAirG2, extendAirG2InsertionLoss=extendAirG2InsertionLoss, extendAirG2Bandwidth=extendAirG2Bandwidth, extendAirG2TxPower=extendAirG2TxPower, extendAirG2BuzTimeout=extendAirG2BuzTimeout, extendAirG2AcmMode=extendAirG2AcmMode, extendAirG2AcmPolicy=extendAirG2AcmPolicy, extendAirG2AcmBaseModulation=extendAirG2AcmBaseModulation)
