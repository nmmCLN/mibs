#
# PySNMP MIB module SL-MUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-MUX-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:44 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
CleiCode, = mibBuilder.importSymbols("SL-ENTITY-MIB", "CleiCode")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, ModuleIdentity, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, NotificationType, ObjectIdentity, Gauge32, Counter64, Bits, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Gauge32", "Counter64", "Bits", "iso", "IpAddress")
TimeStamp, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention", "TruthValue")
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
mibBuilder.exportSymbols("SL-MUX-MIB", PYSNMP_MODULE_ID=slMux, muxIfOscWaveLengthNm=muxIfOscWaveLengthNm, slMux=slMux, muxIfWaveSpacing=muxIfWaveSpacing, muxIfTable=muxIfTable, muxIfWaveLengthNm=muxIfWaveLengthNm, muxIfEntry=muxIfEntry, muxIfIndex=muxIfIndex, muxIfType=muxIfType)
