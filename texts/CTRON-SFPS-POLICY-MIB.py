#
# PySNMP MIB module CTRON-SFPS-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-POLICY-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:35 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
sfpsVMMatrix, sfpsVlanMatrix, sfpsVlanMatrixApi, sfpsISPPolicy = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsVMMatrix", "sfpsVlanMatrix", "sfpsVlanMatrixApi", "sfpsISPPolicy")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, ModuleIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "ModuleIdentity", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

sfpsServiceCenterPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1), )
if mibBuilder.loadTexts: sfpsServiceCenterPolicyTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyTable.setDescription('This table gives policy semantics to call processing.')
sfpsServiceCenterPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-POLICY-MIB", "sfpsServiceCenterPolicyHashLeaf"))
if mibBuilder.loadTexts: sfpsServiceCenterPolicyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyEntry.setDescription('Each entry contains the configuration of the Policy Entry.')
sfpsServiceCenterPolicyHashLeaf = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyHashLeaf.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyHashLeaf.setDescription('Server hash, part of instance key.')
sfpsServiceCenterPolicyMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyMetric.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyMetric.setDescription('Defines order servers are called low to high.')
sfpsServiceCenterPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyName.setDescription('Server name.')
sfpsServiceCenterPolicyOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyOperStatus.setDescription('Operational state of entry.')
sfpsServiceCenterPolicyAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyAdminStatus.setDescription('Administrative State of Entry.')
sfpsServiceCenterPolicyStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyStatusTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyStatusTime.setDescription('Time Tick of last operStatus change.')
sfpsServiceCenterPolicyRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyRequests.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyRequests.setDescription('Requests made to server.')
sfpsServiceCenterPolicyResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterPolicyResponses.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterPolicyResponses.setDescription('GOOD replies by server.')
sfpsMatrixTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1), )
if mibBuilder.loadTexts: sfpsMatrixTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixTable.setDescription(' ')
sfpsMatrixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixRowId"), (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixColId"))
if mibBuilder.loadTexts: sfpsMatrixEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixEntry.setDescription('')
sfpsMatrixRowId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixRowId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixRowId.setDescription('')
sfpsMatrixColId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixColId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixColId.setDescription('')
sfpsMatrixUser1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixUser1Type.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixUser1Type.setDescription('')
sfpsMatrixUser1Load = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixUser1Load.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixUser1Load.setDescription('')
sfpsMatrixUser2Type = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixUser2Type.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixUser2Type.setDescription('')
sfpsMatrixUser2Load = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixUser2Load.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixUser2Load.setDescription('')
sfpsMatrixConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixConnect.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixConnect.setDescription('')
sfpsMatrixFlood = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixFlood.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixFlood.setDescription('')
sfpsMatrixInfoTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2), )
if mibBuilder.loadTexts: sfpsMatrixInfoTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoTable.setDescription(' ')
sfpsMatrixInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1), ).setIndexNames((0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixInfoAddrType"), (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixInfoAddrHash"), (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixInfoHashIndex"))
if mibBuilder.loadTexts: sfpsMatrixInfoEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoEntry.setDescription('')
sfpsMatrixInfoAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixInfoAddrType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoAddrType.setDescription('')
sfpsMatrixInfoAddrHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixInfoAddrHash.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoAddrHash.setDescription('')
sfpsMatrixInfoHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixInfoHashIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoHashIndex.setDescription('')
sfpsMatrixInfoAddrValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixInfoAddrValue.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoAddrValue.setDescription('')
sfpsMatrixInfoTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixInfoTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoTableIndex.setDescription('')
sfpsMatrixInfoDefConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixInfoDefConnect.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoDefConnect.setDescription('')
sfpsMatrixInfoDefFlood = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMatrixInfoDefFlood.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoDefFlood.setDescription('')
sfpsMatrixInfoVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("other", 1), ("addEntry", 2), ("deleteEntry", 3), ("setFlagValue", 4), ("clearFlagValue", 5), ("setFlagGlobal", 6), ("clearFlagGlobal", 7), ("setDefaults", 8), ("resetToDefaults", 9), ("setFilter1", 10), ("setFilter2", 11), ("clearFilter1", 12), ("clearFitler2", 13), ("clearTable", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoVerb.setDescription('')
sfpsMatrixInfoIndex1Tag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoIndex1Tag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoIndex1Tag.setDescription('')
sfpsMatrixInfoIndex1Load = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoIndex1Load.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoIndex1Load.setDescription('')
sfpsMatrixInfoIndex2Tag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoIndex2Tag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoIndex2Tag.setDescription('')
sfpsMatrixInfoIndex2Load = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoIndex2Load.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoIndex2Load.setDescription('')
sfpsMatrixInfoMatrixFlag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connect", 1), ("flood", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoMatrixFlag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoMatrixFlag.setDescription('')
sfpsMatrixInfoFlagMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 7), HexInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoFlagMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoFlagMask.setDescription('')
sfpsMatrixInfoFilter1Tag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoFilter1Tag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoFilter1Tag.setDescription('')
sfpsMatrixInfoFilter1Load = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoFilter1Load.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoFilter1Load.setDescription('')
sfpsMatrixInfoFilter2Tag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 10), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoFilter2Tag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoFilter2Tag.setDescription('')
sfpsMatrixInfoFilter2Load = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 11), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMatrixInfoFilter2Load.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMatrixInfoFilter2Load.setDescription('')
sfpsVMMatrixRowIndex = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVMMatrixRowIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVMMatrixRowIndex.setDescription('')
sfpsVMMatrixCellIndexMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVMMatrixCellIndexMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVMMatrixCellIndexMask.setDescription('')
sfpsVMMatrixAction = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 4, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVMMatrixAction.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVMMatrixAction.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-POLICY-MIB", sfpsServiceCenterPolicyOperStatus=sfpsServiceCenterPolicyOperStatus, sfpsServiceCenterPolicyStatusTime=sfpsServiceCenterPolicyStatusTime, sfpsMatrixInfoVerb=sfpsMatrixInfoVerb, sfpsMatrixInfoIndex2Tag=sfpsMatrixInfoIndex2Tag, sfpsVMMatrixCellIndexMask=sfpsVMMatrixCellIndexMask, sfpsMatrixInfoMatrixFlag=sfpsMatrixInfoMatrixFlag, sfpsMatrixInfoTableIndex=sfpsMatrixInfoTableIndex, sfpsServiceCenterPolicyName=sfpsServiceCenterPolicyName, sfpsServiceCenterPolicyHashLeaf=sfpsServiceCenterPolicyHashLeaf, sfpsMatrixInfoTable=sfpsMatrixInfoTable, sfpsMatrixEntry=sfpsMatrixEntry, HexInteger=HexInteger, sfpsMatrixInfoFilter1Tag=sfpsMatrixInfoFilter1Tag, sfpsMatrixInfoAddrType=sfpsMatrixInfoAddrType, sfpsMatrixInfoIndex1Tag=sfpsMatrixInfoIndex1Tag, sfpsMatrixInfoFilter1Load=sfpsMatrixInfoFilter1Load, sfpsMatrixUser1Type=sfpsMatrixUser1Type, sfpsServiceCenterPolicyEntry=sfpsServiceCenterPolicyEntry, sfpsMatrixInfoHashIndex=sfpsMatrixInfoHashIndex, sfpsVMMatrixAction=sfpsVMMatrixAction, sfpsMatrixInfoAddrValue=sfpsMatrixInfoAddrValue, sfpsServiceCenterPolicyAdminStatus=sfpsServiceCenterPolicyAdminStatus, sfpsServiceCenterPolicyRequests=sfpsServiceCenterPolicyRequests, sfpsMatrixTable=sfpsMatrixTable, sfpsMatrixUser1Load=sfpsMatrixUser1Load, sfpsMatrixInfoDefFlood=sfpsMatrixInfoDefFlood, sfpsMatrixConnect=sfpsMatrixConnect, sfpsMatrixInfoIndex1Load=sfpsMatrixInfoIndex1Load, sfpsMatrixFlood=sfpsMatrixFlood, sfpsServiceCenterPolicyResponses=sfpsServiceCenterPolicyResponses, sfpsMatrixInfoEntry=sfpsMatrixInfoEntry, sfpsMatrixInfoFlagMask=sfpsMatrixInfoFlagMask, sfpsServiceCenterPolicyTable=sfpsServiceCenterPolicyTable, sfpsMatrixInfoAddrHash=sfpsMatrixInfoAddrHash, sfpsMatrixInfoDefConnect=sfpsMatrixInfoDefConnect, sfpsMatrixInfoFilter2Load=sfpsMatrixInfoFilter2Load, sfpsMatrixInfoIndex2Load=sfpsMatrixInfoIndex2Load, sfpsMatrixUser2Load=sfpsMatrixUser2Load, sfpsServiceCenterPolicyMetric=sfpsServiceCenterPolicyMetric, sfpsMatrixUser2Type=sfpsMatrixUser2Type, sfpsMatrixInfoFilter2Tag=sfpsMatrixInfoFilter2Tag, sfpsMatrixColId=sfpsMatrixColId, sfpsMatrixRowId=sfpsMatrixRowId, sfpsVMMatrixRowIndex=sfpsVMMatrixRowIndex)
