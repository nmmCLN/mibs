#
# PySNMP MIB module ROOMALERT12E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT12E-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:14 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Bits, Integer32, Counter32, NotificationType, IpAddress, Counter64, MibIdentifier, enterprises, Gauge32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Bits", "Integer32", "Counter32", "NotificationType", "IpAddress", "Counter64", "MibIdentifier", "enterprises", "Gauge32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
roomalert12E = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1))
lightTower = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2))
internal_sen = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1)).setLabel("internal-sen")
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3)).setLabel("digital-sen2")
digital_sen3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4)).setLabel("digital-sen3")
switch1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 5))
switch2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 6))
switch3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 7))
switch4 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 8))
analog = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 9))
relay = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 10))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 3))
internal_sen_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_1.setStatus('mandatory')
internal_sen_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_2.setStatus('mandatory')
internal_sen_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_3.setStatus('mandatory')
internal_sen_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_4.setStatus('mandatory')
internal_sen_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_5.setStatus('mandatory')
internal_sen_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 6), OctetString()).setLabel("internal-sen-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_6.setStatus('mandatory')
analog_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 9, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("analog-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog_1.setStatus('mandatory')
analog_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 9, 2), OctetString()).setLabel("analog-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog_2.setStatus('mandatory')
relay_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("relay-1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: relay_1.setStatus('mandatory')
relay_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 10, 2), OctetString()).setLabel("relay-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: relay_2.setStatus('mandatory')
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
digital_sen1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_5.setStatus('mandatory')
digital_sen1_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 6), OctetString()).setLabel("digital-sen1-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_6.setStatus('mandatory')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
digital_sen2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_5.setStatus('mandatory')
digital_sen2_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 6), OctetString()).setLabel("digital-sen2-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_6.setStatus('mandatory')
digital_sen3_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_1.setStatus('mandatory')
digital_sen3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_2.setStatus('mandatory')
digital_sen3_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_3.setStatus('mandatory')
digital_sen3_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_4.setStatus('mandatory')
digital_sen3_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_5.setStatus('mandatory')
digital_sen3_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 6), OctetString()).setLabel("digital-sen3-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_6.setStatus('mandatory')
switch_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1_1.setStatus('mandatory')
switch_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 5, 2), OctetString()).setLabel("switch-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1_2.setStatus('mandatory')
switch_sen2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen2.setStatus('mandatory')
switch_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 6, 2), OctetString()).setLabel("switch-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen2_2.setStatus('mandatory')
switch_sen3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen3").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen3.setStatus('mandatory')
switch_sen3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 7, 2), OctetString()).setLabel("switch-sen3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen3_2.setStatus('mandatory')
switch_sen4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen4").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen4.setStatus('mandatory')
switch_sen4_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 8, 2), OctetString()).setLabel("switch-sen4-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen4_2.setStatus('mandatory')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 3, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
lightTower_RE = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-RE").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_RE.setStatus('mandatory')
lightTower_OR = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-OR").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_OR.setStatus('mandatory')
lightTower_GR = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-GR").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_GR.setStatus('mandatory')
lightTower_WH = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-WH").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_WH.setStatus('mandatory')
lightTower_BL = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-BL").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_BL.setStatus('mandatory')
lightTower_A1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-A1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_A1.setStatus('mandatory')
lightTower_A2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-A2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_A2.setStatus('mandatory')
lightTower_RL = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-RL").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_RL.setStatus('mandatory')
tempalarm1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,1)).setLabel("tempalarm1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
room_alert_12E_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,2)).setLabel("room-alert-12E-snmp-trap").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
tempalarm2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,3)).setLabel("tempalarm2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
tempclear2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,4)).setLabel("tempclear2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
tempalarm3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,5)).setLabel("tempalarm3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
tempclear3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,6)).setLabel("tempclear3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
humidityalarm1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,7)).setLabel("humidityalarm1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
humidityclear1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,8)).setLabel("humidityclear1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
humidityalarm2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,9)).setLabel("humidityalarm2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
humidityclear2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,10)).setLabel("humidityclear2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
humidityalarm3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,11)).setLabel("humidityalarm3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
humidityclear3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,12)).setLabel("humidityclear3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchalarm1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,13)).setLabel("switchalarm1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchclear1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,14)).setLabel("switchclear1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchalarm2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,15)).setLabel("switchalarm2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchclear2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,16)).setLabel("switchclear2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchalarm3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,17)).setLabel("switchalarm3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchclear3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,18)).setLabel("switchclear3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchalarm4_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,19)).setLabel("switchalarm4-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
switchclear4_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,20)).setLabel("switchclear4-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
mibBuilder.exportSymbols("ROOMALERT12E-MIB", switch4=switch4, internal_sen_2=internal_sen_2, switch_sen4_2=switch_sen4_2, switchalarm3_12E=switchalarm3_12E, tempalarm1_12E=tempalarm1_12E, switchalarm4_12E=switchalarm4_12E, analog_1=analog_1, digital_sen3_3=digital_sen3_3, lightTower_BL=lightTower_BL, digital_sen2_4=digital_sen2_4, digital_sen2_5=digital_sen2_5, lightTower_RE=lightTower_RE, relay_2=relay_2, digital_sen2_6=digital_sen2_6, internal_sen_1=internal_sen_1, digital_sen3_2=digital_sen3_2, digital_sen3_4=digital_sen3_4, relay_1=relay_1, analog=analog, digital_sen3_5=digital_sen3_5, digital_sen3=digital_sen3, switchclear1_12E=switchclear1_12E, humidityalarm1_12E=humidityalarm1_12E, digital_sen2_1=digital_sen2_1, switchclear2_12E=switchclear2_12E, alarmmessage=alarmmessage, switchalarm1_12E=switchalarm1_12E, lightTower_A1=lightTower_A1, switch1=switch1, lightTower=lightTower, digital_sen2_3=digital_sen2_3, humidityalarm2_12E=humidityalarm2_12E, roomalert12E=roomalert12E, humidityclear1_12E=humidityclear1_12E, digital_sen2=digital_sen2, switchalarm2_12E=switchalarm2_12E, room_alert_12E_snmp_trap=room_alert_12E_snmp_trap, switchclear4_12E=switchclear4_12E, switch3=switch3, digital_sen1_3=digital_sen1_3, switch2=switch2, digital_sen1_5=digital_sen1_5, tempclear3_12E=tempclear3_12E, digital_sen2_2=digital_sen2_2, lightTower_OR=lightTower_OR, digital_sen1_6=digital_sen1_6, sensors=sensors, internal_sen_3=internal_sen_3, tempclear2_12E=tempclear2_12E, digital_sen3_6=digital_sen3_6, products=products, lightTower_WH=lightTower_WH, digital_sen3_1=digital_sen3_1, digital_sen1_4=digital_sen1_4, switch_sen4=switch_sen4, switch_sen2_2=switch_sen2_2, lightTower_GR=lightTower_GR, internal_sen_6=internal_sen_6, humidityclear2_12E=humidityclear2_12E, humidityalarm3_12E=humidityalarm3_12E, lightTower_A2=lightTower_A2, internal_sen=internal_sen, traps=traps, analog_2=analog_2, switch_sen3=switch_sen3, digital_sen1=digital_sen1, internal_sen_5=internal_sen_5, switch_sen3_2=switch_sen3_2, humidityclear3_12E=humidityclear3_12E, tempalarm2_12E=tempalarm2_12E, switch_sen1_2=switch_sen1_2, tempalarm3_12E=tempalarm3_12E, switch_sen2=switch_sen2, lightTower_RL=lightTower_RL, digital_sen1_2=digital_sen1_2, relay=relay, avtech=avtech, digital_sen1_1=digital_sen1_1, switchclear3_12E=switchclear3_12E, internal_sen_4=internal_sen_4, switch_sen1_1=switch_sen1_1)
