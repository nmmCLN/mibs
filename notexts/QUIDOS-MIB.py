#
# PySNMP MIB module QUIDOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/papouch/QUIDOS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:46 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, ObjectIdentity, MibIdentifier, NotificationType, NotificationType, enterprises, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Counter32, TimeTicks, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "NotificationType", "NotificationType", "enterprises", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Counter32", "TimeTicks", "iso", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
papouchProjekt = MibIdentifier((1, 3, 6, 1, 4, 1, 18248))
quidos = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 16))
quido_var = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 16, 1)).setLabel("quido-var")
table_in = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 16, 2)).setLabel("table-in")
table_out = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 16, 3)).setLabel("table-out")
table_term = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 16, 4)).setLabel("table-term")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class OnOff(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class StatCit(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("falling", 1), ("rising", 2), ("both", 3))

temperatureReading = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureReading.setStatus('current')
temperature_S_Reading = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 1, 2), DisplayString()).setLabel("temperature-S-Reading").setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature_S_Reading.setStatus('current')
user_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 1, 3), DisplayString()).setLabel("user-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: user_name.setStatus('current')
device_msg = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 1, 4), DisplayString()).setLabel("device-msg").setMaxAccess("readonly")
if mibBuilder.loadTexts: device_msg.setStatus('current')
temp_msg = NotificationType((1, 3, 6, 1, 4, 1, 18248, 16, 1) + (0,1)).setLabel("temp-msg").setObjects(("QUIDOS-MIB", "user_name"), ("QUIDOS-MIB", "device_msg"))
inTable = MibTable((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1), )
if mibBuilder.loadTexts: inTable.setStatus('current')
inEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1), ).setIndexNames((0, "QUIDOS-MIB", "index"))
if mibBuilder.loadTexts: inEntry.setStatus('current')
pysmi_in = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 1), OnOff()).setLabel("in").setMaxAccess("readonly")
if mibBuilder.loadTexts: pysmi_in.setStatus('current')
in_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 2), DisplayString()).setLabel("in-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: in_name.setStatus('current')
citrwS = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 3), StatCit()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: citrwS.setStatus('current')
citrw = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: citrw.setStatus('current')
outTable = MibTable((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1), )
if mibBuilder.loadTexts: outTable.setStatus('current')
outEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1), ).setIndexNames((0, "QUIDOS-MIB", "index"))
if mibBuilder.loadTexts: outEntry.setStatus('current')
out = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 1), OnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: out.setStatus('current')
out_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 2), DisplayString()).setLabel("out-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: out_name.setStatus('current')
outTwr = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outTwr.setStatus('current')
termTable = MibTable((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1), )
if mibBuilder.loadTexts: termTable.setStatus('current')
termEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1), ).setIndexNames((0, "QUIDOS-MIB", "index"))
if mibBuilder.loadTexts: termEntry.setStatus('current')
modeTerm = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modeTerm.setStatus('current')
mezHi = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mezHi.setStatus('current')
mezLo = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mezLo.setStatus('current')
time = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: time.setStatus('current')
err = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: err.setStatus('current')
mibBuilder.exportSymbols("QUIDOS-MIB", quidos=quidos, out_name=out_name, StatCit=StatCit, outEntry=outEntry, table_out=table_out, inTable=inTable, termEntry=termEntry, in_name=in_name, table_in=table_in, citrwS=citrwS, outTable=outTable, PositiveInteger=PositiveInteger, temperature_S_Reading=temperature_S_Reading, pysmi_in=pysmi_in, err=err, user_name=user_name, mezHi=mezHi, temperatureReading=temperatureReading, mezLo=mezLo, OnOff=OnOff, table_term=table_term, inEntry=inEntry, citrw=citrw, outTwr=outTwr, time=time, temp_msg=temp_msg, termTable=termTable, out=out, device_msg=device_msg, modeTerm=modeTerm, quido_var=quido_var, papouchProjekt=papouchProjekt)
