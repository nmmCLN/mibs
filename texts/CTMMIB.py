#
# PySNMP MIB module CTMMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ctm/CTMMIBV2
# Produced by pysmi-1.1.8 at Tue Jul 26 15:25:17 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Counter32, NotificationType, Bits, Integer32, Gauge32, IpAddress, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, MibIdentifier, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter32", "NotificationType", "Bits", "Integer32", "Gauge32", "IpAddress", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "MibIdentifier", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTMMIB", pwrS=pwrS, tempC=tempC, lastIP=lastIP, trpCntBM1=trpCntBM1, portSyncM=portSyncM, masterTempatureError=masterTempatureError, trpCntBM5=trpCntBM5, cbTrip=cbTrip, masterAutoRestartCBCompletedOK=masterAutoRestartCBCompletedOK, trpCntGM8=trpCntGM8, trpCntGM6=trpCntGM6, resetComplete=resetComplete, lastmilegear=lastmilegear, pwrP=pwrP, gpsSignalLost=gpsSignalLost, trpCntGM3=trpCntGM3, masterPrimayPowerLost=masterPrimayPowerLost, portPwrM3=portPwrM3, masterPrimaryPowerOK=masterPrimaryPowerOK, circuitBreakersOK=circuitBreakersOK, trpCntBM6=trpCntBM6, portOnM=portOnM, voltsM1=voltsM1, portPwrM4=portPwrM4, portPwrM6=portPwrM6, trpCntGM5=trpCntGM5, trpCntBM2=trpCntBM2, trpCntBM4=trpCntBM4, portPwrM2=portPwrM2, modeReqM=modeReqM, lastTime=lastTime, portPwrM8=portPwrM8, masterSecondaryPowerLost=masterSecondaryPowerLost, loginOK=loginOK, nSats=nSats, portPwrM7=portPwrM7, trpCntBM7=trpCntBM7, masterCircuitBreakerTripCode=masterCircuitBreakerTripCode, portPwrM5=portPwrM5, lostEthernetConnection=lostEthernetConnection, trpCntGM2=trpCntGM2, ethernetConnectionRestored=ethernetConnectionRestored, loginFailedAttempt=loginFailedAttempt, tempatureOK=tempatureOK, trpCntBM3=trpCntBM3, trpCntGM1=trpCntGM1, site=site, gpsSignalOK=gpsSignalOK, portPwrM1=portPwrM1, trpCntGM4=trpCntGM4, voltsM2=voltsM2, trpCntGM7=trpCntGM7, masterSecondaryPowerOK=masterSecondaryPowerOK, version=version, settingsChanged=settingsChanged, trpCntBM8=trpCntBM8, mibObjects=mibObjects)
