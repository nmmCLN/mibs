#
# PySNMP MIB module CTMMIBCUSTOM (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ctm/CTMMIBCUSTOM
# Produced by pysmi-1.1.8 at Fri Jul  8 09:15:25 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, NotificationType, MibIdentifier, Gauge32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, iso, Unsigned32, Counter64, IpAddress, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Gauge32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "iso", "Unsigned32", "Counter64", "IpAddress", "enterprises", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lastmilegear = MibIdentifier((1, 3, 6, 1, 4, 1, 25868))
mibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25868, 1))
version = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('mandatory')
if mibBuilder.loadTexts: version.setDescription('Version of Web GUI - Version of Web GUI Interface\n                            currently running on CTM')
site = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: site.setStatus('mandatory')
if mibBuilder.loadTexts: site.setDescription('Site Name - Site name as stored on CTM')
lastIP = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastIP.setStatus('mandatory')
if mibBuilder.loadTexts: lastIP.setDescription('Last IP Address Login - Last IP address captured\n                            at Login Attempt')
lastTime = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTime.setStatus('mandatory')
if mibBuilder.loadTexts: lastTime.setDescription('Last Time Login - Last time of Login attempt')
nSats = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nSats.setStatus('mandatory')
if mibBuilder.loadTexts: nSats.setDescription('Number Satellites in View - Number of Satellites\n                            in view of GPS Receiver Antenna being used for\n                            timing calculations')
pwrP = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrP.setStatus('mandatory')
if mibBuilder.loadTexts: pwrP.setDescription('Master Primary Power - Master ?1? = Power OK,\n                            ?0? = Power Off or Low')
pwrS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrS.setStatus('mandatory')
if mibBuilder.loadTexts: pwrS.setDescription('Master Secondary Power - Master ?1? = Power OK,\n                            ?0? = Power Off or Low')
cbTrip = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbTrip.setStatus('mandatory')
if mibBuilder.loadTexts: cbTrip.setDescription('Master Circuit Breaker Trip Bit Code - Master\n                            Breaker Tripped Code: 1=Port 1, 2=Port2, 4=Port\n                            3, 8=Port4, 16=Port5, 32=Port6, 64=Port7, 128=Port8\n                            Example: Code 5 means Port 3 and Port 1 Tripped')
tempC = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempC.setStatus('mandatory')
if mibBuilder.loadTexts: tempC.setDescription('Master Temperature')
voltsM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsM1.setStatus('mandatory')
if mibBuilder.loadTexts: voltsM1.setDescription('Master Primary Power In Voltage - In Tenths of\n                            a Volt')
voltsM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsM2.setStatus('mandatory')
if mibBuilder.loadTexts: voltsM2.setDescription('Master Secondary Power In Voltage - In Tenths\n                            of a Volt')
portOnM = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOnM.setStatus('mandatory')
if mibBuilder.loadTexts: portOnM.setDescription('Master Ports ON Enabled Status - Master ?1? =Sync\n                            Enabled, ?0? = Sync Off listed in order ?Port1?,\n                            ?Port2?, ?Port3?, ?Port4?, ?Port5?, ?Port6?,\n                            ?Port7?, ?Port8?')
portSyncM = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSyncM.setStatus('mandatory')
if mibBuilder.loadTexts: portSyncM.setDescription('Master Ports Sync Enabled Status - Master ?1?\n                            =Sync Enabled, ?0? = Sync Off listed in order\n                            ?Port1?, ?Port2?, ?Port3?, ?Port4?, ?Port5?,\n                            ?Port6?, ?Port7?, ?Port8?')
portPwrM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM1.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM1.setDescription('Master Power Port 1 - (in tenths of a Watt) delivered\n                            on Port 1')
portPwrM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM2.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM2.setDescription('Master Power Port 2 - (in tenths of a Watt) delivered\n                            on Port 2')
portPwrM3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM3.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM3.setDescription('Master Power Port 3 - (in tenths of a Watt) delivered\n                            on Port 3')
portPwrM4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM4.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM4.setDescription('Master Power Port 4 - (in tenths of a Watt) delivered\n                            on Port 4')
portPwrM5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM5.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM5.setDescription('Master Power Port 5 - (in tenths of a Watt) delivered\n                            on Port 5')
portPwrM6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM6.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM6.setDescription('Master Power Port 6 - (in tenths of a Watt) delivered\n                            on Port 6')
portPwrM7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM7.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM7.setDescription('Master Power Port 7 - (in tenths of a Watt) delivered\n                            on Port 7')
portPwrM8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM8.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrM8.setDescription('Master Power Port 8 - (in tenths of a Watt) delivered\n                            on Port 8')
pwrSP = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSP.setStatus('mandatory')
if mibBuilder.loadTexts: pwrSP.setDescription('Slave Primary Power - Master ?1? = Power OK,\n                            ?0? = Power Off or Low')
pwrSS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSS.setStatus('mandatory')
if mibBuilder.loadTexts: pwrSS.setDescription('Slave Secondary Power - Master ?1? = Power OK,\n                            ?0? = Power Off or Low')
voltsS1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsS1.setStatus('mandatory')
if mibBuilder.loadTexts: voltsS1.setDescription('Slave Primary Power In Voltage - In Tenths of\n                            a Volt')
voltsS2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsS2.setStatus('mandatory')
if mibBuilder.loadTexts: voltsS2.setDescription('Slave Secondary Power In Voltage - In Tenths\n                            of a Volt')
portOnS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 29), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOnS.setStatus('mandatory')
if mibBuilder.loadTexts: portOnS.setDescription('Slave Ports ON Enabled Status - Slave ?1? =Sync\n                            Enabled, ?0? = Sync Off listed in order ?Port1?,\n                            ?Port2?, ?Port3?, ?Port4?, ?Port5?, ?Port6?,\n                            ?Port7?, ?Port8?')
portSyncS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 30), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSyncS.setStatus('mandatory')
if mibBuilder.loadTexts: portSyncS.setDescription('Slave Ports Sync Enabled Status - Slave ?1?\n                            =Sync Enabled, ?0? = Sync Off listed in order\n                            ?Port1?, ?Port2?, ?Port3?, ?Port4?, ?Port5?,\n                            ?Port6?, ?Port7?, ?Port8?')
portPwrS1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS1.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS1.setDescription('Slave Power Port 1 - (in tenths of a Watt) delivered\n                            on Port 1')
portPwrS2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS2.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS2.setDescription('Slave Power Port 2 - (in tenths of a Watt) delivered\n                            on Port 2')
portPwrS3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS3.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS3.setDescription('Slave Power Port 3 - (in tenths of a Watt) delivered\n                            on Port 3')
portPwrS4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS4.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS4.setDescription('Slave Power Port 4 - (in tenths of a Watt) delivered\n                            on Port 4')
portPwrS5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS5.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS5.setDescription('Slave Power Port 5 - (in tenths of a Watt) delivered\n                            on Port 5')
portPwrS6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS6.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS6.setDescription('Slave Power Port 6 - (in tenths of a Watt) delivered\n                            on Port 6')
portPwrS7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS7.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS7.setDescription('Slave Power Port 7 - (in tenths of a Watt) delivered\n                            on Port 7')
portPwrS8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS8.setStatus('mandatory')
if mibBuilder.loadTexts: portPwrS8.setDescription('Slave Power Port 8 - (in tenths of a Watt) delivered\n                            on Port 8')
modeReqM = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 39), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modeReqM.setStatus('mandatory')
if mibBuilder.loadTexts: modeReqM.setDescription('Master CTM2 Port Type Setting - Master ?00?=Type\n                            A (Canopy) ?10?=Type B (OFDM), ?01? = Type C\n                            (POE 802.3at), ?11? (POE 802.3at 4 Pair), ?100?=(POE\n                            24V mode, CTM2 C Only) listed in order ?Port1?,\n                            ?Port2?, ?Port3?, ?Port4?, ?Port5?, ?Port6?,\n                            ?Port7?, ?Port8?')
trpCntGM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM1.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM1.setDescription('Master Auto Restart Count Port 1 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 1')
trpCntGM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM2.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM2.setDescription('Master Auto Restart Count Port 2 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 2')
trpCntGM3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM3.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM3.setDescription('Master Auto Restart Count Port 3 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 3')
trpCntGM4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM4.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM4.setDescription('Master Auto Restart Count Port 4 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 4')
trpCntGM5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 49), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM5.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM5.setDescription('Master Auto Restart Count Port 5 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 5')
trpCntGM6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM6.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM6.setDescription('Master Auto Restart Count Port 6 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 6')
trpCntGM7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 51), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM7.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM7.setDescription('Master Auto Restart Count Port 7 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 7')
trpCntGM8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM8.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntGM8.setDescription('Master Auto Restart Count Port 8 - Number of Times\n                            Auto Reset Feature has executed a Circuit Breaker\n                            Restart on Port 8')
trpCntBM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM1.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM1.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            1 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 1')
trpCntBM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM2.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM2.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            2 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 2')
trpCntBM3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM3.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM3.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            3 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 3')
trpCntBM4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM4.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM4.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            4 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 4')
trpCntBM5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM5.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM5.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            5 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 5')
trpCntBM6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM6.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM6.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            6 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 6')
trpCntBM7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 59), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM7.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM7.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            7 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 7')
trpCntBM8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 60), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM8.setStatus('mandatory')
if mibBuilder.loadTexts: trpCntBM8.setDescription('Master Ckt Breaker Auto Restart Fail Count Port\n                            8 - Number of Times Auto Reset Feature has failed\n                            to restart (after 7 tries) a Circuit Breaker\n                            on Port 8')
lostEthernetConnection = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,0))
if mibBuilder.loadTexts: lostEthernetConnection.setDescription('Lost Ethernet Connection')
masterPrimayPowerLost = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,1))
if mibBuilder.loadTexts: masterPrimayPowerLost.setDescription('Master Primary Power Lost')
masterSecondaryPowerLost = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,2))
if mibBuilder.loadTexts: masterSecondaryPowerLost.setDescription('Master Secondary Power Lost')
gpsSignalLost = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,3))
if mibBuilder.loadTexts: gpsSignalLost.setDescription('GPS Signal Lost')
masterTempatureError = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,4))
if mibBuilder.loadTexts: masterTempatureError.setDescription('Master Temperature Error')
masterCircuitBreakerTripCode = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,5))
if mibBuilder.loadTexts: masterCircuitBreakerTripCode.setDescription('Master Circuit Breaker Trip Code - Master Breaker Tripped\n                             Code: 1=Port 1, 2=Port2, 4=Port 3, 8=Port4, 16=Port5,\n                             32=Port6, 64=Port7, 128=Port8        Example: Code\n                             5 means Port 3 and Port 1 Tripped')
loginFailedAttempt = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,6))
if mibBuilder.loadTexts: loginFailedAttempt.setDescription('Login Failed Attempt')
settingsChanged = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,7))
if mibBuilder.loadTexts: settingsChanged.setDescription('CTM Settings Changed')
masterPrimaryPowerOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,10))
if mibBuilder.loadTexts: masterPrimaryPowerOK.setDescription('Master Primary Power OK')
masterSecondaryPowerOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,20))
if mibBuilder.loadTexts: masterSecondaryPowerOK.setDescription('Master Secondary Power OK')
gpsSignalOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,30))
if mibBuilder.loadTexts: gpsSignalOK.setDescription('GPS Signal OK')
tempatureOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,40))
if mibBuilder.loadTexts: tempatureOK.setDescription('Temperature OK')
circuitBreakersOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,50))
if mibBuilder.loadTexts: circuitBreakersOK.setDescription('Circuit Breakers OK')
masterAutoRestartCBCompletedOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,52))
if mibBuilder.loadTexts: masterAutoRestartCBCompletedOK.setDescription('Master Auto Restart CB Completed OK')
loginOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,60))
if mibBuilder.loadTexts: loginOK.setDescription('Login OK')
resetComplete = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,80))
if mibBuilder.loadTexts: resetComplete.setDescription('Reset Complete')
ethernetConnectionRestored = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,99))
if mibBuilder.loadTexts: ethernetConnectionRestored.setDescription('Ethernet Connection Restored')
mibBuilder.exportSymbols("CTMMIBCUSTOM", nSats=nSats, portPwrS5=portPwrS5, masterPrimaryPowerOK=masterPrimaryPowerOK, pwrP=pwrP, portPwrM4=portPwrM4, lastmilegear=lastmilegear, lastTime=lastTime, portPwrM5=portPwrM5, portSyncS=portSyncS, trpCntBM5=trpCntBM5, mibObjects=mibObjects, portPwrS2=portPwrS2, portPwrM1=portPwrM1, portPwrM6=portPwrM6, tempatureOK=tempatureOK, portPwrM3=portPwrM3, trpCntBM4=trpCntBM4, loginFailedAttempt=loginFailedAttempt, portPwrM7=portPwrM7, trpCntGM5=trpCntGM5, trpCntGM1=trpCntGM1, trpCntBM8=trpCntBM8, gpsSignalLost=gpsSignalLost, voltsM2=voltsM2, masterSecondaryPowerOK=masterSecondaryPowerOK, settingsChanged=settingsChanged, portPwrS8=portPwrS8, lastIP=lastIP, masterSecondaryPowerLost=masterSecondaryPowerLost, portPwrM8=portPwrM8, masterTempatureError=masterTempatureError, trpCntGM7=trpCntGM7, trpCntGM3=trpCntGM3, version=version, tempC=tempC, trpCntBM3=trpCntBM3, masterCircuitBreakerTripCode=masterCircuitBreakerTripCode, circuitBreakersOK=circuitBreakersOK, cbTrip=cbTrip, portPwrS4=portPwrS4, resetComplete=resetComplete, trpCntBM7=trpCntBM7, trpCntBM2=trpCntBM2, trpCntGM6=trpCntGM6, portPwrM2=portPwrM2, voltsS1=voltsS1, portPwrS6=portPwrS6, trpCntGM2=trpCntGM2, trpCntBM6=trpCntBM6, voltsS2=voltsS2, portSyncM=portSyncM, modeReqM=modeReqM, masterPrimayPowerLost=masterPrimayPowerLost, trpCntBM1=trpCntBM1, trpCntGM8=trpCntGM8, gpsSignalOK=gpsSignalOK, site=site, pwrS=pwrS, portOnM=portOnM, pwrSS=pwrSS, portPwrS1=portPwrS1, portPwrS3=portPwrS3, portPwrS7=portPwrS7, portOnS=portOnS, trpCntGM4=trpCntGM4, loginOK=loginOK, voltsM1=voltsM1, ethernetConnectionRestored=ethernetConnectionRestored, masterAutoRestartCBCompletedOK=masterAutoRestartCBCompletedOK, lostEthernetConnection=lostEthernetConnection, pwrSP=pwrSP)
