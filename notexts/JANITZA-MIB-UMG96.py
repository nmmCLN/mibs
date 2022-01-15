#
# PySNMP MIB module JANITZA-MIB-UMG96 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/janitza/JANITZA-MIB-UMG96
# Produced by pysmi-1.1.8 at Sat Jan 15 20:25:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
NotificationType, Integer32, IpAddress, MibIdentifier, mib_2, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Unsigned32, Counter32, Counter64, iso, TimeTicks, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "IpAddress", "MibIdentifier", "mib-2", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Unsigned32", "Counter32", "Counter64", "iso", "TimeTicks", "Bits", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
snmp = MibIdentifier((1, 3, 6, 1, 2, 1, 11))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDescr.setStatus('current')
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectID.setStatus('current')
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUpTime.setStatus('current')
sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysName.setStatus('current')
sysLocation = MibScalar((1, 3, 6, 1, 2, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLocation.setStatus('current')
sysServices = MibScalar((1, 3, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysServices.setStatus('current')
janitza = MibIdentifier((1, 3, 6, 1, 4, 1, 34278))
rmsPhase = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 1))
uLN1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uLN1.setStatus('mandatory')
uLN2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uLN2.setStatus('mandatory')
uLN3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uLN3.setStatus('mandatory')
uL1L2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uL1L2.setStatus('mandatory')
uL2L3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uL2L3.setStatus('mandatory')
uL3L1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uL3L1.setStatus('mandatory')
iL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL1.setStatus('mandatory')
iL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL2.setStatus('mandatory')
iL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL3.setStatus('mandatory')
iL4 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL4.setStatus('mandatory')
iL5 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL5.setStatus('mandatory')
iL6 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iL6.setStatus('mandatory')
pL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pL1.setStatus('mandatory')
pL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pL2.setStatus('mandatory')
pL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pL3.setStatus('mandatory')
qL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qL1.setStatus('mandatory')
qL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qL2.setStatus('mandatory')
qL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qL3.setStatus('mandatory')
sL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sL1.setStatus('mandatory')
sL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sL2.setStatus('mandatory')
sL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sL3.setStatus('mandatory')
cosPL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosPL1.setStatus('mandatory')
cosPL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosPL2.setStatus('mandatory')
cosPL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosPL3.setStatus('mandatory')
rmsSum = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 2))
p3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: p3.setStatus('mandatory')
q3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: q3.setStatus('mandatory')
s3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s3.setStatus('mandatory')
cosP3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cosP3.setStatus('mandatory')
energyPhase = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 3))
whL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: whL1.setStatus('mandatory')
whL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: whL2.setStatus('mandatory')
whL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: whL3.setStatus('mandatory')
qhL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qhL1.setStatus('mandatory')
qhL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qhL2.setStatus('mandatory')
qhL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qhL3.setStatus('mandatory')
energySum = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 4))
wh3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wh3.setStatus('mandatory')
qh3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qh3.setStatus('mandatory')
thd = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 5))
thdULN1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdULN1.setStatus('mandatory')
thdULN2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdULN2.setStatus('mandatory')
thdULN3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdULN3.setStatus('mandatory')
thdIL1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdIL1.setStatus('mandatory')
thdIL2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdIL2.setStatus('mandatory')
thdIL3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 5, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thdIL3.setStatus('mandatory')
misc = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 6))
frequence = MibScalar((1, 3, 6, 1, 4, 1, 34278, 6, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frequence.setStatus('mandatory')
temp1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 6, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temp1.setStatus('mandatory')
temp2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temp2.setStatus('mandatory')
user = MibIdentifier((1, 3, 6, 1, 4, 1, 34278, 7))
jasicVAR1 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR1.setStatus('mandatory')
jasicVAR2 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR2.setStatus('mandatory')
jasicVAR3 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR3.setStatus('mandatory')
jasicVAR4 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR4.setStatus('mandatory')
jasicVAR5 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR5.setStatus('mandatory')
jasicVAR6 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR6.setStatus('mandatory')
jasicVAR7 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR7.setStatus('mandatory')
jasicVAR8 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR8.setStatus('mandatory')
jasicVAR9 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR9.setStatus('mandatory')
jasicVAR10 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR10.setStatus('mandatory')
jasicVAR11 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR11.setStatus('mandatory')
jasicVAR12 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR12.setStatus('mandatory')
jasicVAR13 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR13.setStatus('mandatory')
jasicVAR14 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR14.setStatus('mandatory')
jasicVAR15 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR15.setStatus('mandatory')
jasicVAR16 = MibScalar((1, 3, 6, 1, 4, 1, 34278, 7, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jasicVAR16.setStatus('mandatory')
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0))
warmStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,1))
userTrap1 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,6))
userTrap2 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,7))
userTrap3 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,8))
userTrap4 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,9))
userTrap5 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,10))
userTrap6 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,11))
userTrap7 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,12))
userTrap8 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,13))
userTrap9 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,14))
userTrap10 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,15))
userTrap11 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,16))
userTrap12 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,17))
userTrap13 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,18))
userTrap14 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,19))
userTrap15 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,20))
userTrap16 = NotificationType((1, 3, 6, 1, 4, 1, 34278) + (0,21))
mibBuilder.exportSymbols("JANITZA-MIB-UMG96", sL1=sL1, cosP3=cosP3, energySum=energySum, rmsPhase=rmsPhase, sysLocation=sysLocation, temp2=temp2, frequence=frequence, thdULN2=thdULN2, energyPhase=energyPhase, sysDescr=sysDescr, qL2=qL2, uL2L3=uL2L3, thdIL3=thdIL3, jasicVAR15=jasicVAR15, system=system, sL2=sL2, pL1=pL1, userTrap11=userTrap11, jasicVAR9=jasicVAR9, whL3=whL3, user=user, cosPL2=cosPL2, qhL2=qhL2, thdULN3=thdULN3, sysObjectID=sysObjectID, jasicVAR16=jasicVAR16, userTrap4=userTrap4, jasicVAR8=jasicVAR8, userTrap8=userTrap8, wh3=wh3, userTrap1=userTrap1, jasicVAR4=jasicVAR4, warmStart=warmStart, thdULN1=thdULN1, userTrap7=userTrap7, iL1=iL1, qh3=qh3, jasicVAR1=jasicVAR1, sysUpTime=sysUpTime, cosPL1=cosPL1, q3=q3, userTrap3=userTrap3, userTrap5=userTrap5, coldStart=coldStart, jasicVAR10=jasicVAR10, qhL3=qhL3, p3=p3, uL1L2=uL1L2, jasicVAR3=jasicVAR3, userTrap13=userTrap13, userTrap9=userTrap9, sysServices=sysServices, userTrap10=userTrap10, pL2=pL2, thd=thd, temp1=temp1, userTrap16=userTrap16, whL2=whL2, userTrap6=userTrap6, uLN1=uLN1, iL5=iL5, sysName=sysName, qhL1=qhL1, pL3=pL3, userTrap2=userTrap2, qL3=qL3, iL2=iL2, snmp=snmp, jasicVAR13=jasicVAR13, uLN3=uLN3, iL3=iL3, userTrap12=userTrap12, whL1=whL1, misc=misc, jasicVAR6=jasicVAR6, sL3=sL3, thdIL1=thdIL1, cosPL3=cosPL3, uLN2=uLN2, iL4=iL4, iL6=iL6, jasicVAR7=jasicVAR7, uL3L1=uL3L1, userTrap15=userTrap15, jasicVAR5=jasicVAR5, rmsSum=rmsSum, jasicVAR12=jasicVAR12, thdIL2=thdIL2, janitza=janitza, userTrap14=userTrap14, qL1=qL1, s3=s3, jasicVAR11=jasicVAR11, jasicVAR2=jasicVAR2, jasicVAR14=jasicVAR14)
