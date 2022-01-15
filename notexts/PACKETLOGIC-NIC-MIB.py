#
# PySNMP MIB module PACKETLOGIC-NIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-NIC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:31:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, Bits, NotificationType, IpAddress, Unsigned32, Counter64, ObjectIdentity, iso, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "NotificationType", "IpAddress", "Unsigned32", "Counter64", "ObjectIdentity", "iso", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
nic = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2))
nic.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: nic.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: nic.setOrganization('Procera Networks, Inc.')
slots = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1), )
if mibBuilder.loadTexts: slots.setStatus('current')
slotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1), ).setIndexNames((0, "PACKETLOGIC-NIC-MIB", "slotEntryIndex"))
if mibBuilder.loadTexts: slotEntry.setStatus('current')
slotEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slotEntryIndex.setStatus('current')
channels = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2), )
if mibBuilder.loadTexts: channels.setStatus('current')
channelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1), ).setIndexNames((0, "PACKETLOGIC-NIC-MIB", "channelEntryIndex"))
if mibBuilder.loadTexts: channelEntry.setStatus('current')
channelEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: channelEntryIndex.setStatus('current')
slotLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotLabel.setStatus('current')
slotState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotState.setStatus('current')
slotBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotBypass.setStatus('current')
slotChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotChannels.setStatus('current')
slotInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotInterface.setStatus('current')
slotPartNo = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotPartNo.setStatus('current')
slotPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotPorts.setStatus('current')
slotSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotSpeed.setStatus('current')
channelLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelLocation.setStatus('current')
channelLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelLabel.setStatus('current')
channelSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelSlot.setStatus('current')
totalThroughput = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalThroughput.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-NIC-MIB", slotState=slotState, slotInterface=slotInterface, slotPorts=slotPorts, nic=nic, channelEntry=channelEntry, channels=channels, slotLabel=slotLabel, channelLocation=channelLocation, totalThroughput=totalThroughput, channelEntryIndex=channelEntryIndex, PYSNMP_MODULE_ID=nic, slotEntryIndex=slotEntryIndex, slotPartNo=slotPartNo, channelSlot=channelSlot, slotChannels=slotChannels, slotEntry=slotEntry, slots=slots, slotBypass=slotBypass, channelLabel=channelLabel, slotSpeed=slotSpeed)
