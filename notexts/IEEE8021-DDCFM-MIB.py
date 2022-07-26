#
# PySNMP MIB module IEEE8021-DDCFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-DDCFM-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:03 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
Dot1agCfmMpDirection, Dot1agCfmMDLevel = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMpDirection", "Dot1agCfmMDLevel")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, TimeTicks, Counter64, NotificationType, MibIdentifier, ModuleIdentity, Counter32, ObjectIdentity, Unsigned32, Bits, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter64", "NotificationType", "MibIdentifier", "ModuleIdentity", "Counter32", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, RowStatus, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString", "MacAddress")
ieee8021DdcfmMIB = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 11))
ieee8021DdcfmMIB.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2011-02-27 00:00', '2009-04-06 00:00',))
if mibBuilder.loadTexts: ieee8021DdcfmMIB.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021DdcfmMIB.setOrganization('IEEE 802.1 Working Group')
ieee8021MIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 1))
ieee8021DdcfmConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 2))
ieee8021DdcfmStack = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 1, 1))
ieee8021DdcfmRr = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 1, 2))
ieee8021DdcfmRFMReceiver = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 1, 3))
ieee8021DdcfmDr = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 1, 4))
ieee8021DdcfmSFMOriginator = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 1, 5))
ieee8021DdcfmStackTable = MibTable((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021DdcfmStackTable.setStatus('current')
ieee8021DdcfmStackEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackIfIndex"))
if mibBuilder.loadTexts: ieee8021DdcfmStackEntry.setStatus('current')
ieee8021DdcfmStackIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021DdcfmStackIfIndex.setStatus('current')
ieee8021DdcfmStackRrMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 2), Dot1agCfmMDLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackRrMdLevel.setStatus('current')
ieee8021DdcfmStackRrDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 3), Dot1agCfmMpDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackRrDirection.setStatus('current')
ieee8021DdcfmStackRFMreceiverMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 4), Dot1agCfmMDLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackRFMreceiverMdLevel.setStatus('current')
ieee8021DdcfmStackDrMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 5), Dot1agCfmMDLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackDrMdLevel.setStatus('current')
ieee8021DdcfmStackDrVlanIdOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 6), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackDrVlanIdOrNone.setStatus('current')
ieee8021DdcfmStackSFMOriginatorMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 7), Dot1agCfmMDLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackSFMOriginatorMdLevel.setStatus('current')
ieee8021DdcfmStackSFMOriginatorVlanIdOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 8), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackSFMOriginatorVlanIdOrNone.setStatus('current')
ieee8021DdcfmStackSFMOriginatorDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 9), Dot1agCfmMpDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmStackSFMOriginatorDirection.setStatus('current')
ieee8021DdcfmRrTable = MibTable((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021DdcfmRrTable.setStatus('current')
ieee8021DdcfmRrEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrIfIndex"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrMdIndex"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrDirection"))
if mibBuilder.loadTexts: ieee8021DdcfmRrEntry.setStatus('current')
ieee8021DdcfmRrIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021DdcfmRrIfIndex.setStatus('current')
ieee8021DdcfmRrMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 2), Dot1agCfmMDLevel())
if mibBuilder.loadTexts: ieee8021DdcfmRrMdIndex.setStatus('current')
ieee8021DdcfmRrDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 3), Dot1agCfmMpDirection())
if mibBuilder.loadTexts: ieee8021DdcfmRrDirection.setStatus('current')
ieee8021DdcfmRrPrimaryVlanIdOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 4), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrPrimaryVlanIdOrNone.setStatus('current')
ieee8021DdcfmRrFilter = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1500))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrFilter.setStatus('current')
ieee8021DdcfmRrSamplingInterval = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 6), Unsigned32()).setUnits('miliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrSamplingInterval.setStatus('current')
ieee8021DdcfmRrTargetAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrTargetAddress.setStatus('current')
ieee8021DdcfmRrContinueFlag = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrContinueFlag.setStatus('current')
ieee8021DdcfmRrDuration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrDuration.setStatus('current')
ieee8021DdcfmRrDurationInTimeFlag = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrDurationInTimeFlag.setStatus('current')
ieee8021DdcfmRrVlanPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrVlanPriority.setStatus('current')
ieee8021DdcfmRrVlanDropEligible = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrVlanDropEligible.setStatus('current')
ieee8021DdcfmRrFloodingFlag = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 13), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrFloodingFlag.setStatus('current')
ieee8021DdcfmRrTruncationFlag = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 14), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrTruncationFlag.setStatus('current')
ieee8021DdcfmRrActivationStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmRrActivationStatus.setStatus('current')
ieee8021DdcfmRrRemainDuration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 16), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmRrRemainDuration.setStatus('current')
ieee8021DdcfmRrNextRfmTransID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmRrNextRfmTransID.setStatus('current')
ieee8021DdcfmRrRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRrRowStatus.setStatus('current')
ieee8021DdcfmRFMReceiverTable = MibTable((1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1), )
if mibBuilder.loadTexts: ieee8021DdcfmRFMReceiverTable.setStatus('current')
ieee8021DdcfmRFMReceiverEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRfmReceiverIfIndex"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRfmReceiverMdIndex"))
if mibBuilder.loadTexts: ieee8021DdcfmRFMReceiverEntry.setStatus('current')
ieee8021DdcfmRfmReceiverIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021DdcfmRfmReceiverIfIndex.setStatus('current')
ieee8021DdcfmRfmReceiverMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1, 2), Dot1agCfmMDLevel())
if mibBuilder.loadTexts: ieee8021DdcfmRfmReceiverMdIndex.setStatus('current')
ieee8021DdcfmRFMRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmRFMRowStatus.setStatus('current')
ieee8021DdcfmDrTable = MibTable((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1), )
if mibBuilder.loadTexts: ieee8021DdcfmDrTable.setStatus('current')
ieee8021DdcfmDrEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1), ).setIndexNames((0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrIfIndex"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrMdIndex"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrVlanIdOrNone"))
if mibBuilder.loadTexts: ieee8021DdcfmDrEntry.setStatus('current')
ieee8021DdcfmDrIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021DdcfmDrIfIndex.setStatus('current')
ieee8021DdcfmDrMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 2), Dot1agCfmMDLevel())
if mibBuilder.loadTexts: ieee8021DdcfmDrMdIndex.setStatus('current')
ieee8021DdcfmDrVlanIdOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 3), VlanIdOrNone())
if mibBuilder.loadTexts: ieee8021DdcfmDrVlanIdOrNone.setStatus('current')
ieee8021DdcfmDrSfmOriginator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmDrSfmOriginator.setStatus('current')
ieee8021DdcfmDrSourceAddressStayFlag = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmDrSourceAddressStayFlag.setStatus('current')
ieee8021DdcfmDrFloodingFlag = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmDrFloodingFlag.setStatus('current')
ieee8021DdcfmDrDuration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 7), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmDrDuration.setStatus('current')
ieee8021DdcfmDrActivationStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmDrActivationStatus.setStatus('current')
ieee8021DdcfmDrRemainDuration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmDrRemainDuration.setStatus('current')
ieee8021DdcfmDrSFMsequenceErrors = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 10), Unsigned32()).setUnits('integer').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmDrSFMsequenceErrors.setStatus('current')
ieee8021DdcfmDrRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmDrRowStatus.setStatus('current')
ieee8021DdcfmSoTable = MibTable((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1), )
if mibBuilder.loadTexts: ieee8021DdcfmSoTable.setStatus('current')
ieee8021DdcfmSoEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1), ).setIndexNames((0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSfmIfIndex"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoMdIndex"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoVlanIdOrNone"), (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoDirection"))
if mibBuilder.loadTexts: ieee8021DdcfmSoEntry.setStatus('current')
ieee8021DdcfmSfmIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021DdcfmSfmIfIndex.setStatus('current')
ieee8021DdcfmSoMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 2), Dot1agCfmMDLevel())
if mibBuilder.loadTexts: ieee8021DdcfmSoMdIndex.setStatus('current')
ieee8021DdcfmSoVlanIdOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 3), VlanIdOrNone())
if mibBuilder.loadTexts: ieee8021DdcfmSoVlanIdOrNone.setStatus('current')
ieee8021DdcfmSoDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 4), Dot1agCfmMpDirection())
if mibBuilder.loadTexts: ieee8021DdcfmSoDirection.setStatus('current')
ieee8021DdcfmSoDrMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmSoDrMacAddress.setStatus('current')
ieee8021DdcfmSoDuration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmSoDuration.setStatus('current')
ieee8021DdcfmSoActivationStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmSoActivationStatus.setStatus('current')
ieee8021DdcfmSoRemainDuration = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021DdcfmSoRemainDuration.setStatus('current')
ieee8021DdcfmSoRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021DdcfmSoRowStatus.setStatus('current')
ieee8021DdcfmCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 2, 1))
ieee8021DdcfmGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 11, 2, 2))
ieee8021DdcfmStackGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 1)).setObjects(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackRrMdLevel"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackRrDirection"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackRFMreceiverMdLevel"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackDrMdLevel"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackDrVlanIdOrNone"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackSFMOriginatorMdLevel"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackSFMOriginatorVlanIdOrNone"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackSFMOriginatorDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021DdcfmStackGroup = ieee8021DdcfmStackGroup.setStatus('current')
ieee8021DdcfmRrGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 2)).setObjects(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrPrimaryVlanIdOrNone"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrFilter"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrSamplingInterval"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrTargetAddress"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrContinueFlag"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrDuration"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrDurationInTimeFlag"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrVlanPriority"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrVlanDropEligible"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrFloodingFlag"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrTruncationFlag"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrActivationStatus"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrRemainDuration"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrNextRfmTransID"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021DdcfmRrGroup = ieee8021DdcfmRrGroup.setStatus('current')
ieee8021DdcfmRFMReceiverGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 3)).setObjects(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRFMRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021DdcfmRFMReceiverGroup = ieee8021DdcfmRFMReceiverGroup.setStatus('current')
ieee8021DdcfmDrGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 4)).setObjects(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrSourceAddressStayFlag"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrSfmOriginator"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrFloodingFlag"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrDuration"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrActivationStatus"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrRemainDuration"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrSFMsequenceErrors"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021DdcfmDrGroup = ieee8021DdcfmDrGroup.setStatus('current')
ieee8021DdcfmSoGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 5)).setObjects(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoDrMacAddress"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoDuration"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoActivationStatus"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoRemainDuration"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021DdcfmSoGroup = ieee8021DdcfmSoGroup.setStatus('current')
ieee8021DdcfmCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 11, 2, 1, 1)).setObjects(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackGroup"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrGroup"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRFMReceiverGroup"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrGroup"), ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021DdcfmCompliance = ieee8021DdcfmCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-DDCFM-MIB", ieee8021DdcfmRrSamplingInterval=ieee8021DdcfmRrSamplingInterval, ieee8021DdcfmDrFloodingFlag=ieee8021DdcfmDrFloodingFlag, ieee8021DdcfmSoGroup=ieee8021DdcfmSoGroup, ieee8021DdcfmRfmReceiverIfIndex=ieee8021DdcfmRfmReceiverIfIndex, ieee8021DdcfmRFMReceiverTable=ieee8021DdcfmRFMReceiverTable, ieee8021DdcfmSoTable=ieee8021DdcfmSoTable, ieee8021DdcfmRrTable=ieee8021DdcfmRrTable, ieee8021DdcfmSoDrMacAddress=ieee8021DdcfmSoDrMacAddress, ieee8021DdcfmRrMdIndex=ieee8021DdcfmRrMdIndex, ieee8021DdcfmStackDrMdLevel=ieee8021DdcfmStackDrMdLevel, ieee8021DdcfmRrActivationStatus=ieee8021DdcfmRrActivationStatus, ieee8021DdcfmSFMOriginator=ieee8021DdcfmSFMOriginator, ieee8021MIBObjects=ieee8021MIBObjects, ieee8021DdcfmRrRemainDuration=ieee8021DdcfmRrRemainDuration, ieee8021DdcfmSoVlanIdOrNone=ieee8021DdcfmSoVlanIdOrNone, ieee8021DdcfmRrGroup=ieee8021DdcfmRrGroup, ieee8021DdcfmMIB=ieee8021DdcfmMIB, ieee8021DdcfmDrVlanIdOrNone=ieee8021DdcfmDrVlanIdOrNone, ieee8021DdcfmConformance=ieee8021DdcfmConformance, ieee8021DdcfmDrSfmOriginator=ieee8021DdcfmDrSfmOriginator, ieee8021DdcfmStackDrVlanIdOrNone=ieee8021DdcfmStackDrVlanIdOrNone, ieee8021DdcfmSoRowStatus=ieee8021DdcfmSoRowStatus, PYSNMP_MODULE_ID=ieee8021DdcfmMIB, ieee8021DdcfmDr=ieee8021DdcfmDr, ieee8021DdcfmRrDirection=ieee8021DdcfmRrDirection, ieee8021DdcfmSoActivationStatus=ieee8021DdcfmSoActivationStatus, ieee8021DdcfmCompliances=ieee8021DdcfmCompliances, ieee8021DdcfmRrPrimaryVlanIdOrNone=ieee8021DdcfmRrPrimaryVlanIdOrNone, ieee8021DdcfmRrRowStatus=ieee8021DdcfmRrRowStatus, ieee8021DdcfmSoEntry=ieee8021DdcfmSoEntry, ieee8021DdcfmSoDuration=ieee8021DdcfmSoDuration, ieee8021DdcfmStack=ieee8021DdcfmStack, ieee8021DdcfmRrEntry=ieee8021DdcfmRrEntry, ieee8021DdcfmRFMReceiverGroup=ieee8021DdcfmRFMReceiverGroup, ieee8021DdcfmStackGroup=ieee8021DdcfmStackGroup, ieee8021DdcfmGroups=ieee8021DdcfmGroups, ieee8021DdcfmRr=ieee8021DdcfmRr, ieee8021DdcfmRrVlanDropEligible=ieee8021DdcfmRrVlanDropEligible, ieee8021DdcfmCompliance=ieee8021DdcfmCompliance, ieee8021DdcfmDrIfIndex=ieee8021DdcfmDrIfIndex, ieee8021DdcfmRFMRowStatus=ieee8021DdcfmRFMRowStatus, ieee8021DdcfmRfmReceiverMdIndex=ieee8021DdcfmRfmReceiverMdIndex, ieee8021DdcfmRrDurationInTimeFlag=ieee8021DdcfmRrDurationInTimeFlag, ieee8021DdcfmDrGroup=ieee8021DdcfmDrGroup, ieee8021DdcfmSfmIfIndex=ieee8021DdcfmSfmIfIndex, ieee8021DdcfmStackTable=ieee8021DdcfmStackTable, ieee8021DdcfmDrRemainDuration=ieee8021DdcfmDrRemainDuration, ieee8021DdcfmStackSFMOriginatorVlanIdOrNone=ieee8021DdcfmStackSFMOriginatorVlanIdOrNone, ieee8021DdcfmSoRemainDuration=ieee8021DdcfmSoRemainDuration, ieee8021DdcfmSoDirection=ieee8021DdcfmSoDirection, ieee8021DdcfmStackIfIndex=ieee8021DdcfmStackIfIndex, ieee8021DdcfmStackRrMdLevel=ieee8021DdcfmStackRrMdLevel, ieee8021DdcfmRrFloodingFlag=ieee8021DdcfmRrFloodingFlag, ieee8021DdcfmStackSFMOriginatorMdLevel=ieee8021DdcfmStackSFMOriginatorMdLevel, ieee8021DdcfmRrDuration=ieee8021DdcfmRrDuration, ieee8021DdcfmStackRrDirection=ieee8021DdcfmStackRrDirection, ieee8021DdcfmRrTargetAddress=ieee8021DdcfmRrTargetAddress, ieee8021DdcfmRrFilter=ieee8021DdcfmRrFilter, ieee8021DdcfmRrNextRfmTransID=ieee8021DdcfmRrNextRfmTransID, ieee8021DdcfmStackRFMreceiverMdLevel=ieee8021DdcfmStackRFMreceiverMdLevel, ieee8021DdcfmRrIfIndex=ieee8021DdcfmRrIfIndex, ieee8021DdcfmRrVlanPriority=ieee8021DdcfmRrVlanPriority, ieee8021DdcfmSoMdIndex=ieee8021DdcfmSoMdIndex, ieee8021DdcfmDrSFMsequenceErrors=ieee8021DdcfmDrSFMsequenceErrors, ieee8021DdcfmStackSFMOriginatorDirection=ieee8021DdcfmStackSFMOriginatorDirection, ieee8021DdcfmDrEntry=ieee8021DdcfmDrEntry, ieee8021DdcfmDrMdIndex=ieee8021DdcfmDrMdIndex, ieee8021DdcfmDrRowStatus=ieee8021DdcfmDrRowStatus, ieee8021DdcfmRrContinueFlag=ieee8021DdcfmRrContinueFlag, ieee8021DdcfmStackEntry=ieee8021DdcfmStackEntry, ieee8021DdcfmDrActivationStatus=ieee8021DdcfmDrActivationStatus, ieee8021DdcfmRFMReceiver=ieee8021DdcfmRFMReceiver, ieee8021DdcfmRrTruncationFlag=ieee8021DdcfmRrTruncationFlag, ieee8021DdcfmDrDuration=ieee8021DdcfmDrDuration, ieee8021DdcfmDrSourceAddressStayFlag=ieee8021DdcfmDrSourceAddressStayFlag, ieee8021DdcfmRFMReceiverEntry=ieee8021DdcfmRFMReceiverEntry, ieee8021DdcfmDrTable=ieee8021DdcfmDrTable)
