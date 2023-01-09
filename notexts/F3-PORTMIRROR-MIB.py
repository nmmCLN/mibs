#
# PySNMP MIB module F3-PORTMIRROR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-PORTMIRROR-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:29 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
VlanId, PerfCounter64, TrafficDirection = mibBuilder.importSymbols("CM-COMMON-MIB", "VlanId", "PerfCounter64", "TrafficDirection")
shelfIndex, neIndex, slotIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "shelfIndex", "neIndex", "slotIndex")
cmEthernetAccPortEntry, = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmEthernetAccPortEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Counter64, iso, IpAddress, Integer32, Bits, ObjectIdentity, Counter32, Unsigned32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "iso", "IpAddress", "Integer32", "Bits", "ObjectIdentity", "Counter32", "Unsigned32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity")
DisplayString, StorageType, VariablePointer, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "VariablePointer", "TextualConvention", "RowStatus", "TruthValue")
f3PortMirrorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29))
f3PortMirrorMIB.setRevisions(('2013-10-14 00:00',))
if mibBuilder.loadTexts: f3PortMirrorMIB.setLastUpdated('201309200000Z')
if mibBuilder.loadTexts: f3PortMirrorMIB.setOrganization('ADVA Optical Networking')
class MirroredFramesAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("accept", 1), ("deny", 2))

class PortMirrorStatsAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noAction", 1), ("clearStats", 2))

f3PortMirrorConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1))
f3PortMirrorStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2))
f3PortMirrorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3))
f3PortMirrorFilterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4))
f3MirrorSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1), )
if mibBuilder.loadTexts: f3MirrorSessionTable.setStatus('current')
f3MirrorSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-PORTMIRROR-MIB", "f3MirrorSessionIndex"))
if mibBuilder.loadTexts: f3MirrorSessionEntry.setStatus('current')
f3MirrorSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: f3MirrorSessionIndex.setStatus('current')
f3MirrorSessionSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 2), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorSessionSourcePort.setStatus('current')
f3MirrorSessionMonitorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 3), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorSessionMonitorPort.setStatus('current')
f3MirrorSessionSourcePortDir = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 4), TrafficDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorSessionSourcePortDir.setStatus('current')
f3MirrorSessionTruncationCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3MirrorSessionTruncationCtrl.setStatus('current')
f3MirrorSessionTruncationLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(64, 1500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3MirrorSessionTruncationLength.setStatus('current')
f3MirrorSessionTimestampControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3MirrorSessionTimestampControl.setStatus('current')
f3MirrorSessionStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 8), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorSessionStorageType.setStatus('current')
f3MirrorSessionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorSessionRowStatus.setStatus('current')
f3MirrorSessionMirrRsrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 10), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorSessionMirrRsrcPort.setStatus('current')
f3MirrorSessionFilterProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 11), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorSessionFilterProfile.setStatus('current')
f3PortMirrorAccPortExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2), )
if mibBuilder.loadTexts: f3PortMirrorAccPortExtTable.setStatus('current')
f3PortMirrorAccPortExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1), )
cmEthernetAccPortEntry.registerAugmentions(("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtEntry"))
f3PortMirrorAccPortExtEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3PortMirrorAccPortExtEntry.setStatus('current')
f3PortMirrorAccPortExtMonitorEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PortMirrorAccPortExtMonitorEnabled.setStatus('current')
f3PortMirrorAccPortExtBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 15360))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PortMirrorAccPortExtBufferSize.setStatus('current')
f3PortMirrorAccPortExtMirrRsrcEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PortMirrorAccPortExtMirrRsrcEnabled.setStatus('current')
f3MonitorPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1), )
if mibBuilder.loadTexts: f3MonitorPortStatsTable.setStatus('current')
f3MonitorPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "F3-PORTMIRROR-MIB", "f3MonitorPortStatsIndex"))
if mibBuilder.loadTexts: f3MonitorPortStatsEntry.setStatus('current')
f3MonitorPortStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: f3MonitorPortStatsIndex.setStatus('current')
f3MonitorPortStatsTailDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1, 1, 2), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3MonitorPortStatsTailDropped.setStatus('current')
f3MirrorSessionStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2), )
if mibBuilder.loadTexts: f3MirrorSessionStatsTable.setStatus('current')
f3MirrorSessionStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-PORTMIRROR-MIB", "f3MirrorSessionStatsIndex"))
if mibBuilder.loadTexts: f3MirrorSessionStatsEntry.setStatus('current')
f3MirrorSessionStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: f3MirrorSessionStatsIndex.setStatus('current')
f3MirrorSessionStatsMirrFilterFrameDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1, 2), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3MirrorSessionStatsMirrFilterFrameDiscard.setStatus('current')
f3MirrorSessionStatsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1, 3), PortMirrorStatsAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3MirrorSessionStatsAction.setStatus('current')
f3MirrorFilterProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1), )
if mibBuilder.loadTexts: f3MirrorFilterProfileTable.setStatus('current')
f3MirrorFilterProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterProfileIndex"))
if mibBuilder.loadTexts: f3MirrorFilterProfileEntry.setStatus('current')
f3MirrorFilterProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: f3MirrorFilterProfileIndex.setStatus('current')
f3MirrorFilterProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileName.setStatus('current')
f3MirrorFilterProfileDefaultAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 3), MirroredFramesAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileDefaultAction.setStatus('current')
f3MirrorFilterProfileStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileStorageType.setStatus('current')
f3MirrorFilterProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileRowStatus.setStatus('current')
f3MirrorFilterProfileEntryTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2), )
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryTable.setStatus('current')
f3MirrorFilterProfileEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterProfileIndex"), (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryIndex"))
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryEntry.setStatus('current')
f3MirrorFilterProfileEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)))
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryIndex.setStatus('current')
f3MirrorFilterProfileEntryFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 2), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryFilter.setStatus('current')
f3MirrorFilterProfileEntryPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryPriority.setStatus('current')
f3MirrorFilterProfileEntryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 4), MirroredFramesAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryAction.setStatus('current')
f3MirrorFilterProfileEntryStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 5), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryStorageType.setStatus('current')
f3MirrorFilterProfileEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterProfileEntryRowStatus.setStatus('current')
f3MirrorFilterTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3), )
if mibBuilder.loadTexts: f3MirrorFilterTable.setStatus('current')
f3MirrorFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterIndex"))
if mibBuilder.loadTexts: f3MirrorFilterEntry.setStatus('current')
f3MirrorFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: f3MirrorFilterIndex.setStatus('current')
f3MirrorFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterName.setStatus('current')
f3MirrorFilterL2OuterVIDCtrlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL2OuterVIDCtrlEnabled.setStatus('current')
f3MirrorFilterL2OuterVIDLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 4), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL2OuterVIDLow.setStatus('current')
f3MirrorFilterL2OuterVIDHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 5), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL2OuterVIDHigh.setStatus('current')
f3MirrorFilterL2OuterPrioCtrlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL2OuterPrioCtrlEnabled.setStatus('current')
f3MirrorFilterL2OuterPrioLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL2OuterPrioLow.setStatus('current')
f3MirrorFilterL2OuterPrioHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL2OuterPrioHigh.setStatus('current')
f3MirrorFilterL3IPv4DstAddrCtrlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL3IPv4DstAddrCtrlEnabled.setStatus('current')
f3MirrorFilterL3IPv4DstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL3IPv4DstAddr.setStatus('current')
f3MirrorFilterL3IPv4DstAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL3IPv4DstAddrMask.setStatus('current')
f3MirrorFilterL3IPv4SrcAddrCtrlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL3IPv4SrcAddrCtrlEnabled.setStatus('current')
f3MirrorFilterL3IPv4SrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 13), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL3IPv4SrcAddr.setStatus('current')
f3MirrorFilterL3IPv4SrcAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterL3IPv4SrcAddrMask.setStatus('current')
f3MirrorFilterStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 15), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterStorageType.setStatus('current')
f3MirrorFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3MirrorFilterRowStatus.setStatus('current')
f3PortMirrorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 1))
f3PortMirrorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2))
f3PortMirrorCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 1, 1)).setObjects(("F3-PORTMIRROR-MIB", "f3MirrorSessionGroup"), ("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtGroup"), ("F3-PORTMIRROR-MIB", "f3MonitorPortStatsGroup"), ("F3-PORTMIRROR-MIB", "f3PortMirrorFilterGroup"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PortMirrorCompliance = f3PortMirrorCompliance.setStatus('current')
f3MirrorSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 1)).setObjects(("F3-PORTMIRROR-MIB", "f3MirrorSessionIndex"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionSourcePort"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionMonitorPort"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionSourcePortDir"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionTruncationCtrl"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionTruncationLength"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionTimestampControl"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionStorageType"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionRowStatus"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionMirrRsrcPort"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionFilterProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3MirrorSessionGroup = f3MirrorSessionGroup.setStatus('current')
f3PortMirrorAccPortExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 2)).setObjects(("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtMonitorEnabled"), ("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtBufferSize"), ("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtMirrRsrcEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PortMirrorAccPortExtGroup = f3PortMirrorAccPortExtGroup.setStatus('current')
f3MonitorPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 3)).setObjects(("F3-PORTMIRROR-MIB", "f3MonitorPortStatsIndex"), ("F3-PORTMIRROR-MIB", "f3MonitorPortStatsTailDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3MonitorPortStatsGroup = f3MonitorPortStatsGroup.setStatus('current')
f3MirrorSessionStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 4)).setObjects(("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsIndex"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsMirrFilterFrameDiscard"), ("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3MirrorSessionStatsGroup = f3MirrorSessionStatsGroup.setStatus('current')
f3PortMirrorFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 5)).setObjects(("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileIndex"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileName"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileDefaultAction"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileStorageType"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileRowStatus"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryIndex"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryFilter"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryPriority"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryAction"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryStorageType"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryRowStatus"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterIndex"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterName"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterVIDCtrlEnabled"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterVIDLow"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterVIDHigh"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterPrioCtrlEnabled"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterPrioLow"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterPrioHigh"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4DstAddrCtrlEnabled"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4DstAddr"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4DstAddrMask"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4SrcAddrCtrlEnabled"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4SrcAddr"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4SrcAddrMask"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterStorageType"), ("F3-PORTMIRROR-MIB", "f3MirrorFilterRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PortMirrorFilterGroup = f3PortMirrorFilterGroup.setStatus('current')
mibBuilder.exportSymbols("F3-PORTMIRROR-MIB", f3MirrorFilterIndex=f3MirrorFilterIndex, f3MirrorFilterProfileStorageType=f3MirrorFilterProfileStorageType, f3MirrorSessionGroup=f3MirrorSessionGroup, f3MirrorSessionSourcePort=f3MirrorSessionSourcePort, f3MirrorFilterProfileEntryRowStatus=f3MirrorFilterProfileEntryRowStatus, PortMirrorStatsAction=PortMirrorStatsAction, f3MonitorPortStatsTailDropped=f3MonitorPortStatsTailDropped, f3MirrorFilterProfileEntryFilter=f3MirrorFilterProfileEntryFilter, f3MirrorSessionMirrRsrcPort=f3MirrorSessionMirrRsrcPort, f3MirrorSessionStatsTable=f3MirrorSessionStatsTable, f3MirrorFilterL3IPv4DstAddrMask=f3MirrorFilterL3IPv4DstAddrMask, f3MirrorFilterProfileEntryAction=f3MirrorFilterProfileEntryAction, f3MirrorFilterProfileEntryIndex=f3MirrorFilterProfileEntryIndex, f3MirrorFilterName=f3MirrorFilterName, f3MirrorSessionRowStatus=f3MirrorSessionRowStatus, f3PortMirrorFilterObjects=f3PortMirrorFilterObjects, f3MirrorSessionStatsAction=f3MirrorSessionStatsAction, f3MirrorSessionTable=f3MirrorSessionTable, f3MirrorSessionEntry=f3MirrorSessionEntry, f3MirrorFilterL2OuterPrioLow=f3MirrorFilterL2OuterPrioLow, f3PortMirrorCompliances=f3PortMirrorCompliances, f3PortMirrorGroups=f3PortMirrorGroups, f3MirrorFilterL2OuterVIDCtrlEnabled=f3MirrorFilterL2OuterVIDCtrlEnabled, f3MirrorFilterL2OuterVIDLow=f3MirrorFilterL2OuterVIDLow, MirroredFramesAction=MirroredFramesAction, f3MirrorSessionSourcePortDir=f3MirrorSessionSourcePortDir, f3PortMirrorAccPortExtBufferSize=f3PortMirrorAccPortExtBufferSize, f3MirrorFilterL2OuterPrioCtrlEnabled=f3MirrorFilterL2OuterPrioCtrlEnabled, f3MirrorFilterStorageType=f3MirrorFilterStorageType, f3MirrorSessionStatsGroup=f3MirrorSessionStatsGroup, f3PortMirrorAccPortExtMirrRsrcEnabled=f3PortMirrorAccPortExtMirrRsrcEnabled, f3MirrorSessionStatsEntry=f3MirrorSessionStatsEntry, f3MirrorFilterProfileEntryStorageType=f3MirrorFilterProfileEntryStorageType, f3MirrorFilterProfileTable=f3MirrorFilterProfileTable, PYSNMP_MODULE_ID=f3PortMirrorMIB, f3PortMirrorMIB=f3PortMirrorMIB, f3MirrorFilterProfileEntryTable=f3MirrorFilterProfileEntryTable, f3MonitorPortStatsGroup=f3MonitorPortStatsGroup, f3MirrorSessionStatsIndex=f3MirrorSessionStatsIndex, f3PortMirrorConformance=f3PortMirrorConformance, f3MirrorFilterProfileEntry=f3MirrorFilterProfileEntry, f3MirrorFilterProfileDefaultAction=f3MirrorFilterProfileDefaultAction, f3MirrorSessionTimestampControl=f3MirrorSessionTimestampControl, f3PortMirrorAccPortExtEntry=f3PortMirrorAccPortExtEntry, f3PortMirrorStatsObjects=f3PortMirrorStatsObjects, f3MirrorSessionTruncationLength=f3MirrorSessionTruncationLength, f3MirrorSessionTruncationCtrl=f3MirrorSessionTruncationCtrl, f3MirrorSessionFilterProfile=f3MirrorSessionFilterProfile, f3MirrorSessionMonitorPort=f3MirrorSessionMonitorPort, f3MirrorFilterProfileName=f3MirrorFilterProfileName, f3MirrorSessionStorageType=f3MirrorSessionStorageType, f3MirrorFilterL2OuterPrioHigh=f3MirrorFilterL2OuterPrioHigh, f3MirrorSessionIndex=f3MirrorSessionIndex, f3MirrorFilterL3IPv4SrcAddrMask=f3MirrorFilterL3IPv4SrcAddrMask, f3MirrorFilterL3IPv4SrcAddr=f3MirrorFilterL3IPv4SrcAddr, f3MirrorFilterEntry=f3MirrorFilterEntry, f3PortMirrorFilterGroup=f3PortMirrorFilterGroup, f3MirrorFilterL3IPv4DstAddr=f3MirrorFilterL3IPv4DstAddr, f3PortMirrorConfigObjects=f3PortMirrorConfigObjects, f3MirrorFilterL3IPv4SrcAddrCtrlEnabled=f3MirrorFilterL3IPv4SrcAddrCtrlEnabled, f3PortMirrorAccPortExtGroup=f3PortMirrorAccPortExtGroup, f3MonitorPortStatsTable=f3MonitorPortStatsTable, f3PortMirrorAccPortExtTable=f3PortMirrorAccPortExtTable, f3MirrorFilterProfileIndex=f3MirrorFilterProfileIndex, f3MirrorFilterRowStatus=f3MirrorFilterRowStatus, f3PortMirrorCompliance=f3PortMirrorCompliance, f3MirrorFilterProfileEntryPriority=f3MirrorFilterProfileEntryPriority, f3MonitorPortStatsEntry=f3MonitorPortStatsEntry, f3MirrorFilterTable=f3MirrorFilterTable, f3MonitorPortStatsIndex=f3MonitorPortStatsIndex, f3MirrorSessionStatsMirrFilterFrameDiscard=f3MirrorSessionStatsMirrFilterFrameDiscard, f3MirrorFilterL3IPv4DstAddrCtrlEnabled=f3MirrorFilterL3IPv4DstAddrCtrlEnabled, f3MirrorFilterProfileRowStatus=f3MirrorFilterProfileRowStatus, f3MirrorFilterProfileEntryEntry=f3MirrorFilterProfileEntryEntry, f3MirrorFilterL2OuterVIDHigh=f3MirrorFilterL2OuterVIDHigh, f3PortMirrorAccPortExtMonitorEnabled=f3PortMirrorAccPortExtMonitorEnabled)
