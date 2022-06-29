#
# PySNMP MIB module CTRON-SFPS-PATH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-PATH-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:00 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
sfpsSwitchPathStats, sfpsPathMaskObj, sfpsStaticPath, sfpsSwitchPath, sfpsChassisRIPPath, sfpsISPSwitchPath, sfpsSwitchPathAPI, sfpsPathAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsSwitchPathStats", "sfpsPathMaskObj", "sfpsStaticPath", "sfpsSwitchPath", "sfpsChassisRIPPath", "sfpsISPSwitchPath", "sfpsSwitchPathAPI", "sfpsPathAPI")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, NotificationType, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class HexInteger(Integer32):
    pass

sfpsServiceCenterPathTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1), )
if mibBuilder.loadTexts: sfpsServiceCenterPathTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathTable.setDescription('This table gives path semantics to call processing.')
sfpsServiceCenterPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PATH-MIB", "sfpsServiceCenterPathHashLeaf"))
if mibBuilder.loadTexts: sfpsServiceCenterPathEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathEntry.setDescription('Each entry contains the configuration of the Path Entry.')
sfpsServiceCenterPathHashLeaf = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPathHashLeaf.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathHashLeaf.setDescription('Server hash, part of instance key.')
sfpsServiceCenterPathMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPathMetric.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathMetric.setDescription('Defines order servers are called low to high.')
sfpsServiceCenterPathName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPathName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathName.setDescription('Server name.')
sfpsServiceCenterPathOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPathOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathOperStatus.setDescription('Operational state of entry.')
sfpsServiceCenterPathAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsServiceCenterPathAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathAdminStatus.setDescription('Administrative State of Entry.')
sfpsServiceCenterPathStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPathStatusTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathStatusTime.setDescription('Time Tick of last operStatus change.')
sfpsServiceCenterPathRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPathRequests.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathRequests.setDescription('Requests made to server.')
sfpsServiceCenterPathResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPathResponses.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPathResponses.setDescription('GOOD replies by server.')
sfpsPathAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("add", 2), ("delete", 3), ("uplink", 4), ("downlink", 5), ("diameter", 6), ("flood-add", 7), ("flood-delete", 8), ("force-idle-traffic", 9), ("remove-traffic-cnx", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPIVerb.setDescription('')
sfpsPathAPISwitchMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 2), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPISwitchMac.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPISwitchMac.setDescription('')
sfpsPathAPIPortName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPIPortName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPIPortName.setDescription('')
sfpsPathAPICost = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPICost.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPICost.setDescription('')
sfpsPathAPIHop = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPIHop.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPIHop.setDescription('')
sfpsPathAPIID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPIID.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPIID.setDescription('')
sfpsPathAPIInPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 7), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPIInPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPIInPort.setDescription('')
sfpsPathAPISrcMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 8), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPISrcMac.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPISrcMac.setDescription('')
sfpsPathAPIDstMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 9), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathAPIDstMac.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathAPIDstMac.setDescription('')
sfpsStaticPathTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1), )
if mibBuilder.loadTexts: sfpsStaticPathTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsStaticPathTable.setDescription('')
sfpsStaticPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PATH-MIB", "sfpsStaticPathPort"))
if mibBuilder.loadTexts: sfpsStaticPathEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsStaticPathEntry.setDescription('')
sfpsStaticPathPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsStaticPathPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsStaticPathPort.setDescription('')
sfpsStaticPathFloodEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsStaticPathFloodEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsStaticPathFloodEnabled.setDescription('')
sfpsStaticPathUplinkEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsStaticPathUplinkEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsStaticPathUplinkEnabled.setDescription('')
sfpsStaticPathDownlinkEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsStaticPathDownlinkEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsStaticPathDownlinkEnabled.setDescription('')
sfpsPathMaskObjLogPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjLogPortMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjLogPortMask.setDescription('')
sfpsPathMaskObjPhysPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjPhysPortMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjPhysPortMask.setDescription('')
sfpsPathMaskObjLogResolveMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjLogResolveMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjLogResolveMask.setDescription('')
sfpsPathMaskObjLogFloodNoINB = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjLogFloodNoINB.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjLogFloodNoINB.setDescription('')
sfpsPathMaskObjPhysResolveMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjPhysResolveMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjPhysResolveMask.setDescription('')
sfpsPathMaskObjPhysFloodNoINB = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjPhysFloodNoINB.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjPhysFloodNoINB.setDescription('')
sfpsPathMaskObjOldLogPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjOldLogPortMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjOldLogPortMask.setDescription('')
sfpsPathMaskObjPathChangeEvent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathMaskObjPathChangeEvent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjPathChangeEvent.setDescription('')
sfpsPathMaskObjPathChangeCounter = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjPathChangeCounter.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjPathChangeCounter.setDescription('')
sfpsPathMaskObjLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjLastChangeTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjLastChangeTime.setDescription('')
sfpsPathMaskObjPathCounterReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPathMaskObjPathCounterReset.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjPathCounterReset.setDescription('')
sfpsPathMaskObjIsolatedSwitchMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjIsolatedSwitchMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjIsolatedSwitchMask.setDescription('')
sfpsPathMaskObjPyhsIsolatedSwitchMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjPyhsIsolatedSwitchMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjPyhsIsolatedSwitchMask.setDescription('')
sfpsPathMaskObjLogDownlinkMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjLogDownlinkMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjLogDownlinkMask.setDescription('')
sfpsPathMaskObjCoreUplinkMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjCoreUplinkMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjCoreUplinkMask.setDescription('')
sfpsPathMaskObjOverrideFloodMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("disable", 2), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPathMaskObjOverrideFloodMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPathMaskObjOverrideFloodMask.setDescription('')
sfpsSwitchPathStatsNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsNumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsNumEntries.setDescription('')
sfpsSwitchPathStatsMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsMaxEntries.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsMaxEntries.setDescription('')
sfpsSwitchPathStatsTableSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsTableSize.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsTableSize.setDescription('')
sfpsSwitchPathStatsMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsMemUsage.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsMemUsage.setDescription('')
sfpsSwitchPathStatsActiveLocal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsActiveLocal.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsActiveLocal.setDescription('')
sfpsSwitchPathStatsActiveRemote = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsActiveRemote.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsActiveRemote.setDescription('')
sfpsSwitchPathStatsStaticRemote = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsStaticRemote.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsStaticRemote.setDescription('')
sfpsSwitchPathStatsDeadLocal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsDeadLocal.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsDeadLocal.setDescription('')
sfpsSwitchPathStatsDeadRemote = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsDeadRemote.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsDeadRemote.setDescription('')
sfpsSwitchPathStatsReapReady = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsReapReady.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsReapReady.setDescription('')
sfpsSwitchPathStatsReapAt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsReapAt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsReapAt.setDescription('')
sfpsSwitchPathStatsReapCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsReapCount.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsReapCount.setDescription('')
sfpsSwitchPathStatsPathReq = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathReq.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathReq.setDescription('')
sfpsSwitchPathStatsPathAck = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathAck.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathAck.setDescription('')
sfpsSwitchPathStatsPathNak = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathNak.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathNak.setDescription('')
sfpsSwitchPathStatsPathUnk = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathUnk.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsPathUnk.setDescription('')
sfpsSwitchPathStatsLocateReq = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateReq.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateReq.setDescription('')
sfpsSwitchPathStatsLocateAck = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateAck.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateAck.setDescription('')
sfpsSwitchPathStatsLocateNak = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateNak.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateNak.setDescription('')
sfpsSwitchPathStatsLocateUnk = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateUnk.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsLocateUnk.setDescription('')
sfpsSwitchPathStatsSndDblBack = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsSndDblBack.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsSndDblBack.setDescription('')
sfpsSwitchPathStatsRcdDblBack = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathStatsRcdDblBack.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathStatsRcdDblBack.setDescription('')
sfpsSwitchPathAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("addFind", 2), ("lose", 3), ("delete", 4), ("clearTable", 5), ("resetStats", 6), ("setReapAt", 7), ("setMaxRcvDblBck", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSwitchPathAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathAPIVerb.setDescription('')
sfpsSwitchPathAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSwitchPathAPIPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathAPIPort.setDescription('')
sfpsSwitchPathAPIBaseMAC = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 3), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSwitchPathAPIBaseMAC.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathAPIBaseMAC.setDescription('')
sfpsSwitchPathAPIReapAt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSwitchPathAPIReapAt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathAPIReapAt.setDescription('')
sfpsSwitchPathAPIMaxRcvDblBack = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSwitchPathAPIMaxRcvDblBack.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathAPIMaxRcvDblBack.setDescription('')
sfpsSwitchPathTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3), )
if mibBuilder.loadTexts: sfpsSwitchPathTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTable.setDescription('')
sfpsSwitchPathTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1), ).setIndexNames((0, "CTRON-SFPS-PATH-MIB", "sfpsSwitchPathTableSwitchMAC"), (0, "CTRON-SFPS-PATH-MIB", "sfpsSwitchPathTablePort"))
if mibBuilder.loadTexts: sfpsSwitchPathTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableEntry.setDescription('.')
sfpsSwitchPathTableSwitchMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 1), SfpsAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableSwitchMAC.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableSwitchMAC.setDescription('')
sfpsSwitchPathTablePort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTablePort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTablePort.setDescription('')
sfpsSwitchPathTableIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableIsActive.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableIsActive.setDescription('')
sfpsSwitchPathTableIsStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableIsStatic.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableIsStatic.setDescription('')
sfpsSwitchPathTableIsLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableIsLocal.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableIsLocal.setDescription('')
sfpsSwitchPathTableRefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableRefCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableRefCnt.setDescription('')
sfpsSwitchPathTableRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableRefTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableRefTime.setDescription('')
sfpsSwitchPathTableFoundCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableFoundCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableFoundCnt.setDescription('')
sfpsSwitchPathTableFoundTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableFoundTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableFoundTime.setDescription('')
sfpsSwitchPathTableLostCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableLostCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableLostCnt.setDescription('')
sfpsSwitchPathTableLostTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableLostTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableLostTime.setDescription('')
sfpsSwitchPathTableSrcDblBackCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableSrcDblBackCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableSrcDblBackCnt.setDescription('')
sfpsSwitchPathTableSrcDblBackTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableSrcDblBackTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableSrcDblBackTime.setDescription('')
sfpsSwitchPathTableRcvDblBackCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableRcvDblBackCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableRcvDblBackCnt.setDescription('')
sfpsSwitchPathTableRcvDblBackTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableRcvDblBackTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableRcvDblBackTime.setDescription('')
sfpsSwitchPathTableDirReapCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableDirReapCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableDirReapCnt.setDescription('')
sfpsSwitchPathTableDirReapTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 17), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSwitchPathTableDirReapTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSwitchPathTableDirReapTime.setDescription('')
sfpsChassisRIPPathNumInTable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRIPPathNumInTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRIPPathNumInTable.setDescription('')
sfpsChassisRIPPathNumRequests = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRIPPathNumRequests.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRIPPathNumRequests.setDescription('')
sfpsChassisRIPPathNumReplyAck = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRIPPathNumReplyAck.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRIPPathNumReplyAck.setDescription('')
sfpsChassisRIPPathNumReplyUnk = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRIPPathNumReplyUnk.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRIPPathNumReplyUnk.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-PATH-MIB", sfpsPathMaskObjPathChangeCounter=sfpsPathMaskObjPathChangeCounter, sfpsSwitchPathStatsLocateReq=sfpsSwitchPathStatsLocateReq, sfpsSwitchPathTableFoundTime=sfpsSwitchPathTableFoundTime, sfpsPathAPISrcMac=sfpsPathAPISrcMac, sfpsSwitchPathStatsReapAt=sfpsSwitchPathStatsReapAt, sfpsServiceCenterPathMetric=sfpsServiceCenterPathMetric, sfpsSwitchPathTableIsLocal=sfpsSwitchPathTableIsLocal, sfpsSwitchPathTableRefTime=sfpsSwitchPathTableRefTime, sfpsSwitchPathStatsLocateAck=sfpsSwitchPathStatsLocateAck, HexInteger=HexInteger, sfpsSwitchPathStatsPathNak=sfpsSwitchPathStatsPathNak, sfpsServiceCenterPathRequests=sfpsServiceCenterPathRequests, sfpsSwitchPathStatsSndDblBack=sfpsSwitchPathStatsSndDblBack, sfpsServiceCenterPathAdminStatus=sfpsServiceCenterPathAdminStatus, sfpsServiceCenterPathEntry=sfpsServiceCenterPathEntry, sfpsSwitchPathTableSwitchMAC=sfpsSwitchPathTableSwitchMAC, sfpsSwitchPathStatsLocateUnk=sfpsSwitchPathStatsLocateUnk, sfpsChassisRIPPathNumInTable=sfpsChassisRIPPathNumInTable, sfpsSwitchPathStatsReapCount=sfpsSwitchPathStatsReapCount, sfpsPathMaskObjPhysPortMask=sfpsPathMaskObjPhysPortMask, sfpsPathAPICost=sfpsPathAPICost, sfpsSwitchPathStatsStaticRemote=sfpsSwitchPathStatsStaticRemote, sfpsSwitchPathStatsActiveRemote=sfpsSwitchPathStatsActiveRemote, sfpsSwitchPathStatsDeadRemote=sfpsSwitchPathStatsDeadRemote, sfpsSwitchPathTableLostCnt=sfpsSwitchPathTableLostCnt, sfpsStaticPathPort=sfpsStaticPathPort, sfpsSwitchPathTableFoundCnt=sfpsSwitchPathTableFoundCnt, sfpsSwitchPathAPIPort=sfpsSwitchPathAPIPort, sfpsSwitchPathStatsMemUsage=sfpsSwitchPathStatsMemUsage, sfpsSwitchPathStatsNumEntries=sfpsSwitchPathStatsNumEntries, sfpsPathAPIHop=sfpsPathAPIHop, sfpsPathAPISwitchMac=sfpsPathAPISwitchMac, sfpsStaticPathFloodEnabled=sfpsStaticPathFloodEnabled, sfpsSwitchPathTableSrcDblBackTime=sfpsSwitchPathTableSrcDblBackTime, sfpsPathMaskObjPathChangeEvent=sfpsPathMaskObjPathChangeEvent, sfpsSwitchPathAPIMaxRcvDblBack=sfpsSwitchPathAPIMaxRcvDblBack, sfpsSwitchPathStatsTableSize=sfpsSwitchPathStatsTableSize, sfpsPathMaskObjLogDownlinkMask=sfpsPathMaskObjLogDownlinkMask, sfpsStaticPathTable=sfpsStaticPathTable, sfpsPathMaskObjIsolatedSwitchMask=sfpsPathMaskObjIsolatedSwitchMask, sfpsServiceCenterPathOperStatus=sfpsServiceCenterPathOperStatus, sfpsSwitchPathStatsRcdDblBack=sfpsSwitchPathStatsRcdDblBack, sfpsServiceCenterPathStatusTime=sfpsServiceCenterPathStatusTime, sfpsServiceCenterPathHashLeaf=sfpsServiceCenterPathHashLeaf, sfpsPathAPIID=sfpsPathAPIID, sfpsPathMaskObjLogFloodNoINB=sfpsPathMaskObjLogFloodNoINB, sfpsSwitchPathStatsPathUnk=sfpsSwitchPathStatsPathUnk, SfpsAddress=SfpsAddress, sfpsSwitchPathTableLostTime=sfpsSwitchPathTableLostTime, sfpsStaticPathDownlinkEnabled=sfpsStaticPathDownlinkEnabled, sfpsPathMaskObjLogResolveMask=sfpsPathMaskObjLogResolveMask, sfpsPathMaskObjOldLogPortMask=sfpsPathMaskObjOldLogPortMask, sfpsChassisRIPPathNumRequests=sfpsChassisRIPPathNumRequests, sfpsSwitchPathTableRcvDblBackTime=sfpsSwitchPathTableRcvDblBackTime, sfpsPathMaskObjPyhsIsolatedSwitchMask=sfpsPathMaskObjPyhsIsolatedSwitchMask, sfpsSwitchPathStatsDeadLocal=sfpsSwitchPathStatsDeadLocal, sfpsSwitchPathStatsPathReq=sfpsSwitchPathStatsPathReq, sfpsSwitchPathTable=sfpsSwitchPathTable, sfpsSwitchPathTableRefCnt=sfpsSwitchPathTableRefCnt, sfpsSwitchPathAPIReapAt=sfpsSwitchPathAPIReapAt, sfpsPathAPIPortName=sfpsPathAPIPortName, sfpsPathMaskObjPathCounterReset=sfpsPathMaskObjPathCounterReset, sfpsServiceCenterPathResponses=sfpsServiceCenterPathResponses, sfpsSwitchPathTableRcvDblBackCnt=sfpsSwitchPathTableRcvDblBackCnt, sfpsSwitchPathStatsActiveLocal=sfpsSwitchPathStatsActiveLocal, sfpsPathMaskObjPhysFloodNoINB=sfpsPathMaskObjPhysFloodNoINB, sfpsStaticPathUplinkEnabled=sfpsStaticPathUplinkEnabled, sfpsPathMaskObjPhysResolveMask=sfpsPathMaskObjPhysResolveMask, sfpsPathMaskObjLogPortMask=sfpsPathMaskObjLogPortMask, sfpsSwitchPathStatsMaxEntries=sfpsSwitchPathStatsMaxEntries, sfpsChassisRIPPathNumReplyAck=sfpsChassisRIPPathNumReplyAck, sfpsPathAPIVerb=sfpsPathAPIVerb, sfpsSwitchPathTableSrcDblBackCnt=sfpsSwitchPathTableSrcDblBackCnt, sfpsSwitchPathStatsLocateNak=sfpsSwitchPathStatsLocateNak, sfpsSwitchPathTableIsStatic=sfpsSwitchPathTableIsStatic, sfpsSwitchPathTableEntry=sfpsSwitchPathTableEntry, sfpsServiceCenterPathName=sfpsServiceCenterPathName, sfpsPathAPIDstMac=sfpsPathAPIDstMac, sfpsSwitchPathTablePort=sfpsSwitchPathTablePort, sfpsPathAPIInPort=sfpsPathAPIInPort, sfpsStaticPathEntry=sfpsStaticPathEntry, sfpsSwitchPathTableDirReapTime=sfpsSwitchPathTableDirReapTime, sfpsServiceCenterPathTable=sfpsServiceCenterPathTable, sfpsPathMaskObjLastChangeTime=sfpsPathMaskObjLastChangeTime, sfpsPathMaskObjCoreUplinkMask=sfpsPathMaskObjCoreUplinkMask, sfpsPathMaskObjOverrideFloodMask=sfpsPathMaskObjOverrideFloodMask, sfpsSwitchPathAPIBaseMAC=sfpsSwitchPathAPIBaseMAC, sfpsChassisRIPPathNumReplyUnk=sfpsChassisRIPPathNumReplyUnk, sfpsSwitchPathAPIVerb=sfpsSwitchPathAPIVerb, sfpsSwitchPathStatsReapReady=sfpsSwitchPathStatsReapReady, sfpsSwitchPathTableIsActive=sfpsSwitchPathTableIsActive, sfpsSwitchPathStatsPathAck=sfpsSwitchPathStatsPathAck, sfpsSwitchPathTableDirReapCnt=sfpsSwitchPathTableDirReapCnt)
