#
# PySNMP MIB module JANITZA-MIB-UMG96 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/janitza/JANITZA-MIB-UMG96
# Produced by pysmi-1.1.8 at Sat Jan 15 20:25:36 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Unsigned32, TimeTicks, Counter32, IpAddress, mib_2, Bits, iso, Integer32, Counter64, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter32", "IpAddress", "mib-2", "Bits", "iso", "Integer32", "Counter64", "enterprises", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
snmp = MibIdentifier((1, 3, 6, 1, 2, 1, 11))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDescr.setStatus('current')
if mibBuilder.loadTexts: sysDescr.setDescription("A textual description of the entity.  This value should\n            include the full name and version identification of\n            the system's hardware type, software operating-system,\n            and networking software.")
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectID.setStatus('current')
if mibBuilder.loadTexts: sysObjectID.setDescription("The vendor's authoritative identification of the\n            network management subsystem contained in the entity.\n            This value is allocated within the SMI enterprises\n            subtree (1.3.6.1.4.1) and provides an easy and\n            unambiguous means for determining `what kind of box' is\n            being managed.  For example, if vendor `Flintstones,\n            Inc.' was assigned the subtree 1.3.6.1.4.1.424242,\n            it could assign the identifier 1.3.6.1.4.1.424242.1.1\n            to its `Fred Router'.")
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUpTime.setStatus('current')
if mibBuilder.loadTexts: sysUpTime.setDescription('The time (in hundredths of a second) since the\n\t\t\tnetwork management portion of the system was last\n\t\t\tre-initialized.')
sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysName.setStatus('current')
if mibBuilder.loadTexts: sysName.setDescription("An administratively-assigned name for this managed\n            node.  By convention, this is the node's fully-qualified\n            domain name.  If the name is unknown, the value is\n            the zero-length string.")
sysLocation = MibScalar((1, 3, 6, 1, 2, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLocation.setStatus('current')
if mibBuilder.loadTexts: sysLocation.setDescription("The physical location of this node (e.g., 'telephone\n            closet, 3rd floor').  If the location is unknown, the\n            value is the zero-length string.")
sysServices = MibScalar((1, 3, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysServices.setStatus('current')
if mibBuilder.loadTexts: sysServices.setDescription('A value which indicates the set of services that this\n            entity may potentially offer.  The value is a sum.\n\n            This sum initially takes the value zero. Then, for\n            each layer, L, in the range 1 through 7, that this node\n            performs transactions for, 2 raised to (L - 1) is added\n            to the sum.  For example, a node which performs only\n            routing functions would have a value of 4 (2^(3-1)).\n            In contrast, a node which is a host offering application\n            services would have a value of 72 (2^(4-1) + 2^(7-1)).\n            Note that in the context of the Internet suite of\n            protocols, values should be calculated accordingly:\n\n                 layer      functionality\n                   1        physical (e.g., repeaters)\n                   2        datalink/subnetwork (e.g., bridges)\n                   3        internet (e.g., supports the IP)\n                   4        end-to-end  (e.g., supports the TCP)\n                   7        applications (e.g., supports the SMTP)\n\n            For systems including OSI protocols, layers 5 and 6\n            may also be counted.')
janitza = MibIdentifier((1, 3, 6, 1, 4, 1, 34278))
rmsPhase = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 1))
uLN1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uLN1.setStatus('mandatory')
if mibBuilder.loadTexts: uLN1.setDescription('Voltage Phase L1 in 100mV')
uLN2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uLN2.setStatus('mandatory')
if mibBuilder.loadTexts: uLN2.setDescription('Voltage Phase L2 in 100mV')
uLN3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uLN3.setStatus('mandatory')
if mibBuilder.loadTexts: uLN3.setDescription('Voltage Phase L3 in 100mV')
uL1L2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uL1L2.setStatus('mandatory')
if mibBuilder.loadTexts: uL1L2.setDescription('Voltage Phase L1-L2 in 100mV')
uL2L3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uL2L3.setStatus('mandatory')
if mibBuilder.loadTexts: uL2L3.setDescription('Voltage Phase L2-L3 in 100mV')
uL3L1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uL3L1.setStatus('mandatory')
if mibBuilder.loadTexts: uL3L1.setDescription('Voltage Phase L3-L1 in 100mV')
iL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL1.setStatus('mandatory')
if mibBuilder.loadTexts: iL1.setDescription('Current Phase L1  in 1mA')
iL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL2.setStatus('mandatory')
if mibBuilder.loadTexts: iL2.setDescription('Current Phase L2  in 1mA')
iL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL3.setStatus('mandatory')
if mibBuilder.loadTexts: iL3.setDescription('Current Phase L3  in 1mA')
iL4 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL4.setStatus('mandatory')
if mibBuilder.loadTexts: iL4.setDescription('Current Phase L4  in 1mA')
iL5 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL5.setStatus('mandatory')
if mibBuilder.loadTexts: iL5.setDescription('Current Phase L5  in 1mA')
iL6 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL6.setStatus('mandatory')
if mibBuilder.loadTexts: iL6.setDescription('Current Phase L6 in 1mA')
pL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pL1.setStatus('mandatory')
if mibBuilder.loadTexts: pL1.setDescription('Real Power L1  in Watt')
pL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pL2.setStatus('mandatory')
if mibBuilder.loadTexts: pL2.setDescription('Real Power L2  in Watt')
pL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pL3.setStatus('mandatory')
if mibBuilder.loadTexts: pL3.setDescription('Real Power L3  in Watt')
qL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qL1.setStatus('mandatory')
if mibBuilder.loadTexts: qL1.setDescription('Reaktiv Power L1  in VAr')
qL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qL2.setStatus('mandatory')
if mibBuilder.loadTexts: qL2.setDescription('Reaktiv Power L2  in VAr')
qL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qL3.setStatus('mandatory')
if mibBuilder.loadTexts: qL3.setDescription('Reaktiv Power L3  in VAr')
sL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sL1.setStatus('mandatory')
if mibBuilder.loadTexts: sL1.setDescription('Power L1  in VA')
sL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sL2.setStatus('mandatory')
if mibBuilder.loadTexts: sL2.setDescription('Power L2  in VA')
sL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sL3.setStatus('mandatory')
if mibBuilder.loadTexts: sL3.setDescription('Power L3  in VA')
cosPL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosPL1.setStatus('mandatory')
if mibBuilder.loadTexts: cosPL1.setDescription('Cos(Phi) L1 * 0.001')
cosPL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosPL2.setStatus('mandatory')
if mibBuilder.loadTexts: cosPL2.setDescription('Cos(Phi) L2 * 0.001')
cosPL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosPL3.setStatus('mandatory')
if mibBuilder.loadTexts: cosPL3.setDescription('Cos(Phi) L3 * 0.001')
rmsSum = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 2))
p3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: p3.setStatus('mandatory')
if mibBuilder.loadTexts: p3.setDescription('Real Power Sum L1..L3  in Watt')
q3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: q3.setStatus('mandatory')
if mibBuilder.loadTexts: q3.setDescription('Reaktiv Power Sum L1..L3  in Watt')
s3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s3.setStatus('mandatory')
if mibBuilder.loadTexts: s3.setDescription('Power Sum L1..L3  in Watt')
cosP3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosP3.setStatus('mandatory')
if mibBuilder.loadTexts: cosP3.setDescription('COS(Phi) Sum L1..L3  *0.001')
energyPhase = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 3))
whL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: whL1.setStatus('mandatory')
if mibBuilder.loadTexts: whL1.setDescription('Active Energy  Phase L1 in 0.1 KWh')
whL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: whL2.setStatus('mandatory')
if mibBuilder.loadTexts: whL2.setDescription('Active Energy  Phase L2 in 0.1 KWh')
whL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: whL3.setStatus('mandatory')
if mibBuilder.loadTexts: whL3.setDescription('Active Energy  Phase L3 in 0.1 KWh')
qhL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qhL1.setStatus('mandatory')
if mibBuilder.loadTexts: qhL1.setDescription('Reactive Energy  Phase L1 in 0.1 KVArh')
qhL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qhL2.setStatus('mandatory')
if mibBuilder.loadTexts: qhL2.setDescription('Reactive Energy  Phase L2 in 0.1 KVArh')
qhL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qhL3.setStatus('mandatory')
if mibBuilder.loadTexts: qhL3.setDescription('Reactive Energy  Phase L3 in 0.1 KVArh')
energySum = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 4))
wh3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wh3.setStatus('mandatory')
if mibBuilder.loadTexts: wh3.setDescription('Active Energy  Sum L1..L3 in 0.1 KWh')
qh3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qh3.setStatus('mandatory')
if mibBuilder.loadTexts: qh3.setDescription('Reactive Energy  Sum L1..L3 in 0.1 KWh')
thd = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 5))
thdULN1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdULN1.setStatus('mandatory')
if mibBuilder.loadTexts: thdULN1.setDescription('Total Harmonic Distortion Voltage Phase L1 * 0.1%')
thdULN2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdULN2.setStatus('mandatory')
if mibBuilder.loadTexts: thdULN2.setDescription('Total Harmonic Distortion Voltage Phase L2 * 0.1%')
thdULN3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdULN3.setStatus('mandatory')
if mibBuilder.loadTexts: thdULN3.setDescription('Total Harmonic Distortion Voltage Phase L3 * 0.1%')
thdIL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdIL1.setStatus('mandatory')
if mibBuilder.loadTexts: thdIL1.setDescription('Total Harmonic Distortion Current Phase L1 * 0.1%')
thdIL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdIL2.setStatus('mandatory')
if mibBuilder.loadTexts: thdIL2.setDescription('Total Harmonic Distortion Current Phase L2 * 0.1%')
thdIL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdIL3.setStatus('mandatory')
if mibBuilder.loadTexts: thdIL3.setDescription('Total Harmonic Distortion Current Phase L3 * 0.1%')
misc = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 6))
frequence = MibScalar((1, 3, 6, 1, 4, 1, 34278, 6, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frequence.setStatus('mandatory')
if mibBuilder.loadTexts: frequence.setDescription('Frequence* 0.01 Hz')
temp1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 6, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temp1.setStatus('mandatory')
if mibBuilder.loadTexts: temp1.setDescription('Temperatur1 in °C * 10')
temp2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temp2.setStatus('mandatory')
if mibBuilder.loadTexts: temp2.setDescription('Temperatur2 in °C * 10')
user = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 7))
jasicVAR1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR1.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR1.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[0]')
jasicVAR2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR2.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR2.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[1]')
jasicVAR3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR3.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR3.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[2]')
jasicVAR4 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR4.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR4.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[3]')
jasicVAR5 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR5.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR5.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[4]')
jasicVAR6 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR6.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR6.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[5]')
jasicVAR7 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR7.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR7.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[6]')
jasicVAR8 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR8.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR8.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[7]')
jasicVAR9 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR9.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR9.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[8]')
jasicVAR10 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR10.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR10.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[9]')
jasicVAR11 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR11.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR11.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[10]')
jasicVAR12 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR12.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR12.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[11]')
jasicVAR13 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR13.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR13.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[12]')
jasicVAR14 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR14.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR14.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[13]')
jasicVAR15 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR15.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR15.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[14]')
jasicVAR16 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR16.setStatus('mandatory')
if mibBuilder.loadTexts: jasicVAR16.setDescription('Jasic User Variable  to user for Jasic :_snmp_uservar[15]')
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0))
if mibBuilder.loadTexts: coldStart.setDescription("A coldStart trap signifies that the sending\n                          protocol entity is reinitializing itself such\n                          that the agent's configuration or the rotocol\n                          entity implementation may be altered.")
warmStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,1))
if mibBuilder.loadTexts: warmStart.setDescription('A warmStart trap signifies that the sending\n                          protocol entity is reinitializing itself such\n                          that neither the agent configuration nor the\n                          protocol entity implementation is altered.')
userTrap1 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,6))
if mibBuilder.loadTexts: userTrap1.setDescription('Jasic Trap  : use type=6 , subtype = 6')
userTrap2 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,7))
if mibBuilder.loadTexts: userTrap2.setDescription('Jasic Trap  : use type=6 , subtype = 7')
userTrap3 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,8))
if mibBuilder.loadTexts: userTrap3.setDescription('Jasic Trap  : use type=6 , subtype = 8')
userTrap4 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,9))
if mibBuilder.loadTexts: userTrap4.setDescription('Jasic Trap  : use type=6 , subtype = 9')
userTrap5 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,10))
if mibBuilder.loadTexts: userTrap5.setDescription('Jasic Trap  : use type=6 , subtype = 10')
userTrap6 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,11))
if mibBuilder.loadTexts: userTrap6.setDescription('Jasic Trap  : use type=6 , subtype = 11')
userTrap7 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,12))
if mibBuilder.loadTexts: userTrap7.setDescription('Jasic Trap  : use type=6 , subtype = 12')
userTrap8 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,13))
if mibBuilder.loadTexts: userTrap8.setDescription('Jasic Trap  : use type=6 , subtype = 13')
userTrap9 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,14))
if mibBuilder.loadTexts: userTrap9.setDescription('Jasic Trap  : use type=6 , subtype = 14')
userTrap10 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,15))
if mibBuilder.loadTexts: userTrap10.setDescription('Jasic Trap  : use type=6 , subtype = 15')
userTrap11 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,16))
if mibBuilder.loadTexts: userTrap11.setDescription('Jasic Trap  : use type=6 , subtype = 16')
userTrap12 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,17))
if mibBuilder.loadTexts: userTrap12.setDescription('Jasic Trap  : use type=6 , subtype = 17')
userTrap13 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,18))
if mibBuilder.loadTexts: userTrap13.setDescription('Jasic Trap  : use type=6 , subtype = 18')
userTrap14 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,19))
if mibBuilder.loadTexts: userTrap14.setDescription('Jasic Trap  : use type=6 , subtype = 19')
userTrap15 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,20))
if mibBuilder.loadTexts: userTrap15.setDescription('Jasic Trap  : use type=6 , subtype = 20')
userTrap16 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,21))
if mibBuilder.loadTexts: userTrap16.setDescription('Jasic Trap  : use type=6 , subtype = 21')
mibBuilder.exportSymbols("JANITZA-MIB-UMG96", s3=s3, whL2=whL2, jasicVAR7=jasicVAR7, uLN2=uLN2, userTrap14=userTrap14, sL1=sL1, qL3=qL3, userTrap7=userTrap7, userTrap5=userTrap5, iL4=iL4, cosP3=cosP3, thdIL2=thdIL2, sysName=sysName, userTrap8=userTrap8, userTrap13=userTrap13, energyPhase=energyPhase, qL1=qL1, misc=misc, jasicVAR4=jasicVAR4, uL2L3=uL2L3, uL1L2=uL1L2, thd=thd, jasicVAR2=jasicVAR2, iL1=iL1, userTrap6=userTrap6, pL3=pL3, userTrap11=userTrap11, pL1=pL1, whL1=whL1, rmsPhase=rmsPhase, system=system, cosPL2=cosPL2, snmp=snmp, userTrap16=userTrap16, userTrap9=userTrap9, uL3L1=uL3L1, sL2=sL2, user=user, janitza=janitza, cosPL1=cosPL1, temp2=temp2, userTrap1=userTrap1, thdIL3=thdIL3, sysLocation=sysLocation, wh3=wh3, uLN1=uLN1, frequence=frequence, iL3=iL3, jasicVAR1=jasicVAR1, uLN3=uLN3, energySum=energySum, pL2=pL2, userTrap2=userTrap2, qL2=qL2, jasicVAR16=jasicVAR16, userTrap3=userTrap3, jasicVAR15=jasicVAR15, sysObjectID=sysObjectID, jasicVAR6=jasicVAR6, qhL1=qhL1, whL3=whL3, jasicVAR5=jasicVAR5, temp1=temp1, userTrap4=userTrap4, thdULN3=thdULN3, jasicVAR8=jasicVAR8, userTrap10=userTrap10, thdIL1=thdIL1, sL3=sL3, qhL3=qhL3, cosPL3=cosPL3, jasicVAR12=jasicVAR12, warmStart=warmStart, sysServices=sysServices, sysDescr=sysDescr, qh3=qh3, userTrap12=userTrap12, iL2=iL2, jasicVAR10=jasicVAR10, jasicVAR11=jasicVAR11, jasicVAR3=jasicVAR3, thdULN1=thdULN1, jasicVAR9=jasicVAR9, jasicVAR14=jasicVAR14, userTrap15=userTrap15, q3=q3, coldStart=coldStart, p3=p3, iL6=iL6, rmsSum=rmsSum, iL5=iL5, thdULN2=thdULN2, sysUpTime=sysUpTime, qhL2=qhL2, jasicVAR13=jasicVAR13)
