#
# PySNMP MIB module QUIDOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/papouch/QUIDOS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:59 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Counter32, Integer32, ModuleIdentity, Unsigned32, enterprises, Counter64, Gauge32, NotificationType, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Counter32", "Integer32", "ModuleIdentity", "Unsigned32", "enterprises", "Counter64", "Gauge32", "NotificationType", "Bits", "iso")
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
if mibBuilder.loadTexts: temperatureReading.setDescription('temperature value / 10')
temperature_S_Reading = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 1, 2), DisplayString()).setLabel("temperature-S-Reading").setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature_S_Reading.setStatus('current')
if mibBuilder.loadTexts: temperature_S_Reading.setDescription('temperature value as string')
user_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 1, 3), DisplayString()).setLabel("user-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: user_name.setStatus('current')
if mibBuilder.loadTexts: user_name.setDescription('user name is user string')
device_msg = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 1, 4), DisplayString()).setLabel("device-msg").setMaxAccess("readonly")
if mibBuilder.loadTexts: device_msg.setStatus('current')
if mibBuilder.loadTexts: device_msg.setDescription('msg')
temp_msg = NotificationType((1, 3, 6, 1, 4, 1, 18248, 16, 1) + (0,1)).setLabel("temp-msg").setObjects(("QUIDOS-MIB", "user_name"), ("QUIDOS-MIB", "device_msg"))
if mibBuilder.loadTexts: temp_msg.setDescription('tento trap je odesilan pri zmenach vstupu ')
inTable = MibTable((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1), )
if mibBuilder.loadTexts: inTable.setStatus('current')
if mibBuilder.loadTexts: inTable.setDescription('')
inEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1), ).setIndexNames((0, "QUIDOS-MIB", "index"))
if mibBuilder.loadTexts: inEntry.setStatus('current')
if mibBuilder.loadTexts: inEntry.setDescription('')
pysmi_in = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 1), OnOff()).setLabel("in").setMaxAccess("readonly")
if mibBuilder.loadTexts: pysmi_in.setStatus('current')
if mibBuilder.loadTexts: pysmi_in.setDescription('0 = OFF, 1 = ON')
in_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 2), DisplayString()).setLabel("in-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: in_name.setStatus('current')
if mibBuilder.loadTexts: in_name.setDescription('user name is user string')
citrwS = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 3), StatCit()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: citrwS.setStatus('current')
if mibBuilder.loadTexts: citrwS.setDescription('0 = none, 1 = rising, 2 = falling, 3 = both')
citrw = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: citrw.setStatus('current')
if mibBuilder.loadTexts: citrw.setDescription('cteni citacu nebo odecet od citace')
outTable = MibTable((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1), )
if mibBuilder.loadTexts: outTable.setStatus('current')
if mibBuilder.loadTexts: outTable.setDescription('')
outEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1), ).setIndexNames((0, "QUIDOS-MIB", "index"))
if mibBuilder.loadTexts: outEntry.setStatus('current')
if mibBuilder.loadTexts: outEntry.setDescription('')
out = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 1), OnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: out.setStatus('current')
if mibBuilder.loadTexts: out.setDescription('0 = OFF, 1 = ON')
out_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 2), DisplayString()).setLabel("out-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: out_name.setStatus('current')
if mibBuilder.loadTexts: out_name.setDescription('user name is user string')
outTwr = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outTwr.setStatus('current')
if mibBuilder.loadTexts: outTwr.setDescription('0 - 255')
termTable = MibTable((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1), )
if mibBuilder.loadTexts: termTable.setStatus('current')
if mibBuilder.loadTexts: termTable.setDescription('')
termEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1), ).setIndexNames((0, "QUIDOS-MIB", "index"))
if mibBuilder.loadTexts: termEntry.setStatus('current')
if mibBuilder.loadTexts: termEntry.setDescription('')
modeTerm = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modeTerm.setStatus('current')
if mibBuilder.loadTexts: modeTerm.setDescription('0 = vypnut,\n                     1 = prekroci li teplota hodnotu mezHi1 sepne rele1, klesne li pod hodnotu mezLo1 rozepne rele1\n                     2 = prekroci li teplota hodnotu mezHi1 rozepne rele1, klesne li pod hodnotu mezLo1 sepne rele1                  \n                     3 = prekroci li teplota hodnotu mezHi1 sepne rele1 na dobu v parametru time1.\n                         pri opetovnem prekroceni se udalost vyvola klesla li teplota od\n                         predchozi udalosti na hodnotu v mezLo1\n                     4 = prekroci li teplota hodnotu mezHi1 rozepne rele1 na dobu v parametru time1.\n                         pri opetovnem prekroceni se udalost vyvola klesla li teplota od\n                         predchozi udalosti na hodnotu v mezLo1   \n                     5 = klesne li teplota pod hodnotu mezLo1 sepne rele1 na dobu v parametru time1.\n                         pri opetovnem poklesu teploty se udalost vyvola stoupla li teplota od \n                         predchozi udalosti na hodnotu v mezHi1   \n                     6 = klesne li teplota pod hodnotu mezLo1 sepne rele1 na dobu v parametru time1.\n                         pri opetovnem poklesu teploty se udalost vyvola stoupla li teplota od \n                         predchozi udalosti na hodnotu v mezHi1                                                  \n                    ')
mezHi = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mezHi.setStatus('current')
if mibBuilder.loadTexts: mezHi.setDescription('nastavuji horni mez teploty v intervalu -550 .. +1250\n                     zpusob zapisu: pozadovana hodnota * 10\n                     nesmi byt mensi nez mezLo1    \n                    ')
mezLo = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mezLo.setStatus('current')
if mibBuilder.loadTexts: mezLo.setDescription('nastavuji dolni mez teploty v intervalu -550 .. +1250\n                     zpusob zapisu: pozadovana hodnota * 10\n                     nesmi byt vetsi nez mezHi1    \n                    ')
time = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: time.setStatus('current')
if mibBuilder.loadTexts: time.setDescription('zde je uvedena doba po kterou bude rele1 po vyvolani udalosti sepnuto nebo rozepnuto\n                     tato doba je ve vterinach\n                    ')
err = MibTableColumn((1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: err.setStatus('current')
if mibBuilder.loadTexts: err.setDescription('parametr urcujici v jakem stavu ma byt rele2 dojde li k chybe teplotniho cidla\n                         0 = nechat ve stavu ve kterem se rele nachazi\n                         1 = rozepnout rele2\n                         2 = sepnout rele2\n                        ')
mibBuilder.exportSymbols("QUIDOS-MIB", user_name=user_name, modeTerm=modeTerm, OnOff=OnOff, device_msg=device_msg, PositiveInteger=PositiveInteger, pysmi_in=pysmi_in, inTable=inTable, out_name=out_name, table_out=table_out, termEntry=termEntry, quido_var=quido_var, quidos=quidos, outTable=outTable, outEntry=outEntry, time=time, in_name=in_name, outTwr=outTwr, termTable=termTable, table_in=table_in, inEntry=inEntry, temp_msg=temp_msg, citrw=citrw, papouchProjekt=papouchProjekt, StatCit=StatCit, mezLo=mezLo, table_term=table_term, mezHi=mezHi, err=err, temperature_S_Reading=temperature_S_Reading, temperatureReading=temperatureReading, out=out, citrwS=citrwS)
