#
# PySNMP MIB module CTRON-SFPS-DIAGSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-DIAGSTATS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
sfpsFloodCounters, sfpsIsolatedSwitch, sfpsResetNVRAM, sfpsFloodCountersReset = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsFloodCounters", "sfpsIsolatedSwitch", "sfpsResetNVRAM", "sfpsFloodCountersReset")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sfpsFloodCountersTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1), )
if mibBuilder.loadTexts: sfpsFloodCountersTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersTable.setDescription('A table of flood count information.')
sfpsFloodCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-DIAGSTATS-MIB", "sfpsFloodCountersSource"))
if mibBuilder.loadTexts: sfpsFloodCountersEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersEntry.setDescription('Each entry is instanced by the Source MAC address.')
sfpsFloodCountersSource = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 1), SfpsAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersSource.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersSource.setDescription('Source Mac Address.')
sfpsFloodCountersNumFloods = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersNumFloods.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersNumFloods.setDescription('Number of floods caused by this Source MAC.')
sfpsFloodCountersLastSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersLastSeqNum.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersLastSeqNum.setDescription('Last Sequence number.')
sfpsFloodCountersNumDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersNumDrops.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersNumDrops.setDescription('Number of drops for that Source MAC..')
sfpsFloodCountersLastDropTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersLastDropTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersLastDropTime.setDescription('The time tick on when the last drop occurred for that \n                Source MAC..')
sfpsFloodCountersMaxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersMaxDrops.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersMaxDrops.setDescription('Maximum drops for that Source MAC.')
sfpsFloodCountersMaxDropsTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersMaxDropsTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersMaxDropsTime.setDescription('The time tick on when the maximum drops occurred\n                for that Source MAC.')
sfpsFloodCountersResetReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsFloodCountersResetReset.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersResetReset.setDescription('Reset the Flood counters (1 to reset).')
sfpsFloodCountersTotalDropped = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersTotalDropped.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersTotalDropped.setDescription('Total number of drops based on sequence numbers for the switch.')
sfpsFloodCountersTotalRunts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersTotalRunts.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersTotalRunts.setDescription('Total number of runt packets originated from the Flooder.')
sfpsFloodCountersTotalSelfOrig = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersTotalSelfOrig.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersTotalSelfOrig.setDescription('Total number of floods that the switch sees that were generated\n        from itself.')
sfpsFloodCountersNonNetPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersNonNetPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFloodCountersNonNetPort.setDescription('Total number of floods received on non-Network ports.')
sfpsIsolatedSwitchIsolatedSwitch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsIsolatedSwitchIsolatedSwitch.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsIsolatedSwitchIsolatedSwitch.setDescription('Designates whether this switch has determined that it is an\n        Isolated switch.')
sfpsIsolatedSwitchResetCounters = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsIsolatedSwitchResetCounters.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsIsolatedSwitchResetCounters.setDescription('Clears the INBDropped and INBNotSent counters.')
sfpsIsolatedSwitchINBDropped = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsIsolatedSwitchINBDropped.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsIsolatedSwitchINBDropped.setDescription('During the time that switch has not converged, this number should\n        increment. It should not increment once things are stable.')
sfpsIsolatedSwitchINBNotSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsIsolatedSwitchINBNotSent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsIsolatedSwitchINBNotSent.setDescription('Number of times the packet not sent out the INB. Used for debugging    \n        purposes.')
sfpsResetNVRAMPercentNvramAvailable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResetNVRAMPercentNvramAvailable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResetNVRAMPercentNvramAvailable.setDescription('Percent of Nvram available.')
sfpsResetNVRAMTotalNVRAM = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResetNVRAMTotalNVRAM.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResetNVRAMTotalNVRAM.setDescription('Total amount of Nvram.')
sfpsResetNVRAMOnetoResetNvramAndRestoreIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsResetNVRAMOnetoResetNvramAndRestoreIP.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResetNVRAMOnetoResetNvramAndRestoreIP.setDescription('')
sfpsResetNVRAMDelayTimer = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsResetNVRAMDelayTimer.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResetNVRAMDelayTimer.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-DIAGSTATS-MIB", sfpsIsolatedSwitchIsolatedSwitch=sfpsIsolatedSwitchIsolatedSwitch, sfpsFloodCountersEntry=sfpsFloodCountersEntry, SfpsAddress=SfpsAddress, sfpsResetNVRAMPercentNvramAvailable=sfpsResetNVRAMPercentNvramAvailable, sfpsFloodCountersNonNetPort=sfpsFloodCountersNonNetPort, sfpsFloodCountersTotalDropped=sfpsFloodCountersTotalDropped, sfpsFloodCountersNumDrops=sfpsFloodCountersNumDrops, sfpsIsolatedSwitchINBDropped=sfpsIsolatedSwitchINBDropped, sfpsFloodCountersMaxDrops=sfpsFloodCountersMaxDrops, sfpsFloodCountersTotalRunts=sfpsFloodCountersTotalRunts, sfpsIsolatedSwitchINBNotSent=sfpsIsolatedSwitchINBNotSent, sfpsFloodCountersTable=sfpsFloodCountersTable, sfpsFloodCountersLastDropTime=sfpsFloodCountersLastDropTime, sfpsFloodCountersLastSeqNum=sfpsFloodCountersLastSeqNum, sfpsIsolatedSwitchResetCounters=sfpsIsolatedSwitchResetCounters, sfpsResetNVRAMDelayTimer=sfpsResetNVRAMDelayTimer, sfpsResetNVRAMOnetoResetNvramAndRestoreIP=sfpsResetNVRAMOnetoResetNvramAndRestoreIP, sfpsFloodCountersTotalSelfOrig=sfpsFloodCountersTotalSelfOrig, sfpsFloodCountersNumFloods=sfpsFloodCountersNumFloods, sfpsFloodCountersResetReset=sfpsFloodCountersResetReset, sfpsResetNVRAMTotalNVRAM=sfpsResetNVRAMTotalNVRAM, sfpsFloodCountersMaxDropsTime=sfpsFloodCountersMaxDropsTime, sfpsFloodCountersSource=sfpsFloodCountersSource)
