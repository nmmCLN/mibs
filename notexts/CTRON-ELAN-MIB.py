#
# PySNMP MIB module CTRON-ELAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ELAN-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ctAtmfLanEmulation, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctAtmfLanEmulation")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class CtLaneDebugLevel(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("user", 1), ("all", 2), ("error", 3), ("warning", 4), ("informational", 5), ("detailed", 6), ("trace", 7))

class ElanLocalIndex(Integer32):
    pass

ctLeClient = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 1))
ctElan = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2))
ctLes = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 3))
ctBus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4))
ctElanConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1))
ctElanConfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1), )
if mibBuilder.loadTexts: ctElanConfTable.setStatus('mandatory')
ctElanConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-ELAN-MIB", "ctElanConfIndex"))
if mibBuilder.loadTexts: ctElanConfEntry.setStatus('mandatory')
ctElanConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 1), ElanLocalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanConfIndex.setStatus('mandatory')
ctElanConfUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanConfUnitNumber.setStatus('mandatory')
ctElanConfPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("secure", 1), ("nonsecure", 2))).clone('nonsecure')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanConfPolicy.setStatus('mandatory')
ctElanConfDelPolicyWithElan = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanConfDelPolicyWithElan.setStatus('mandatory')
ctElanConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanConfRowStatus.setStatus('mandatory')
ctElanSFDSPeerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2), )
if mibBuilder.loadTexts: ctElanSFDSPeerTable.setStatus('mandatory')
ctElanSFDSPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2, 1), ).setIndexNames((0, "CTRON-ELAN-MIB", "ctElanSFDSPeerIP"))
if mibBuilder.loadTexts: ctElanSFDSPeerEntry.setStatus('mandatory')
ctElanSFDSPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanSFDSPeerIP.setStatus('mandatory')
ctElanSFDSPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanSFDSPeerRowStatus.setStatus('mandatory')
ctElanConfDirectoryServicesIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanConfDirectoryServicesIP.setStatus('mandatory')
ctElanDSStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connected", 1), ("connectionLost", 2), ("unknown", 3))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanDSStatus.setStatus('mandatory')
ctElanUNIVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("uni30", 2), ("uni31", 3), ("uni40", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanUNIVersion.setStatus('mandatory')
ctElanLaneDbgOutputFile = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanLaneDbgOutputFile.setStatus('mandatory')
ctElanLaneDbgConnectionServices = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 7), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanLaneDbgConnectionServices.setStatus('mandatory')
ctElanLaneDbgDatabaseManagement = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 8), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanLaneDbgDatabaseManagement.setStatus('mandatory')
ctElanCtLaneDbgSNMP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 9), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanCtLaneDbgSNMP.setStatus('mandatory')
ctElanLaneDbgLECS = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 10), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanLaneDbgLECS.setStatus('mandatory')
ctElanCtLaneDbgLES = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 11), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctElanCtLaneDbgLES.setStatus('mandatory')
ctElanHotStandbyStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initial", 1), ("active", 2), ("standby", 3), ("unknown", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanHotStandbyStatus.setStatus('mandatory')
ctElanConfHotStandbyIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctElanConfHotStandbyIP.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ELAN-MIB", ctElanConfHotStandbyIP=ctElanConfHotStandbyIP, ctElanLaneDbgOutputFile=ctElanLaneDbgOutputFile, ctElanLaneDbgDatabaseManagement=ctElanLaneDbgDatabaseManagement, ctElanCtLaneDbgLES=ctElanCtLaneDbgLES, ctElanUNIVersion=ctElanUNIVersion, ctLeClient=ctLeClient, ctElanConfGroup=ctElanConfGroup, ctElanConfTable=ctElanConfTable, ctElanConfUnitNumber=ctElanConfUnitNumber, ctElan=ctElan, ctElanDSStatus=ctElanDSStatus, ctElanConfPolicy=ctElanConfPolicy, ctElanCtLaneDbgSNMP=ctElanCtLaneDbgSNMP, ElanLocalIndex=ElanLocalIndex, ctElanSFDSPeerIP=ctElanSFDSPeerIP, ctElanConfDelPolicyWithElan=ctElanConfDelPolicyWithElan, ctElanConfRowStatus=ctElanConfRowStatus, ctElanSFDSPeerRowStatus=ctElanSFDSPeerRowStatus, ctElanConfDirectoryServicesIP=ctElanConfDirectoryServicesIP, ctElanConfIndex=ctElanConfIndex, ctElanSFDSPeerEntry=ctElanSFDSPeerEntry, ctElanHotStandbyStatus=ctElanHotStandbyStatus, CtLaneDebugLevel=CtLaneDebugLevel, ctElanLaneDbgLECS=ctElanLaneDbgLECS, ctElanConfEntry=ctElanConfEntry, ctBus=ctBus, ctLes=ctLes, ctElanSFDSPeerTable=ctElanSFDSPeerTable, ctElanLaneDbgConnectionServices=ctElanLaneDbgConnectionServices)
