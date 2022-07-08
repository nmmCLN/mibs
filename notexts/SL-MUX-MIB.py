#
# PySNMP MIB module SL-MUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-MUX-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:55 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
CleiCode, = mibBuilder.importSymbols("SL-ENTITY-MIB", "CleiCode")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, NotificationType, iso, MibIdentifier, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter64, Counter32, Integer32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "iso", "MibIdentifier", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter64", "Counter32", "Integer32", "ObjectIdentity", "Gauge32")
TruthValue, DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "TimeStamp")
slMux = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 5))
if mibBuilder.loadTexts: slMux.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slMux.setOrganization('PacketLight Networks Ltd.')
muxIfTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1), )
if mibBuilder.loadTexts: muxIfTable.setStatus('current')
muxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1), ).setIndexNames((0, "SL-MUX-MIB", "muxIfIndex"))
if mibBuilder.loadTexts: muxIfEntry.setStatus('current')
muxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfIndex.setStatus('current')
muxIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfType.setStatus('current')
muxIfWaveSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ghzNone", 0), ("ghz400", 1), ("ghz200", 2), ("ghz100", 3), ("ghz50", 4), ("ghz2500", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfWaveSpacing.setStatus('current')
muxIfWaveLengthNm = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfWaveLengthNm.setStatus('current')
muxIfOscWaveLengthNm = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfOscWaveLengthNm.setStatus('current')
mibBuilder.exportSymbols("SL-MUX-MIB", slMux=slMux, PYSNMP_MODULE_ID=slMux, muxIfType=muxIfType, muxIfWaveSpacing=muxIfWaveSpacing, muxIfEntry=muxIfEntry, muxIfOscWaveLengthNm=muxIfOscWaveLengthNm, muxIfIndex=muxIfIndex, muxIfWaveLengthNm=muxIfWaveLengthNm, muxIfTable=muxIfTable)
