#
# PySNMP MIB module INTEGRATED-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/INTEGRATED-SERVICES-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:28:29 2022
# On host fv-az128-12 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, mib_2, Gauge32, IpAddress, NotificationType, Integer32, MibIdentifier, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "mib-2", "Gauge32", "IpAddress", "NotificationType", "Integer32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Unsigned32", "Counter32", "Bits")
TruthValue, RowStatus, TextualConvention, DisplayString, TimeInterval, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString", "TimeInterval", "TestAndIncr")
intSrv = ModuleIdentity((1, 3, 6, 1, 2, 1, 52))
if mibBuilder.loadTexts: intSrv.setLastUpdated('9511030500Z')
if mibBuilder.loadTexts: intSrv.setOrganization('IETF Integrated Services Working Group')
intSrvObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 1))
intSrvGenObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 2))
intSrvNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 3))
intSrvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4))
class SessionNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Protocol(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class SessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class Port(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 4)

class MessageSize(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BitRate(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BurstSize(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class QosService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 5))
    namedValues = NamedValues(("bestEffort", 1), ("guaranteedDelay", 2), ("controlledLoad", 5))

intSrvIfAttribTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 1), )
if mibBuilder.loadTexts: intSrvIfAttribTable.setStatus('current')
intSrvIfAttribEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvIfAttribEntry.setStatus('current')
intSrvIfAttribAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 1), BitRate()).setUnits('Bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBits.setStatus('current')
intSrvIfAttribMaxAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 2), BitRate()).setUnits('Bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribMaxAllocatedBits.setStatus('current')
intSrvIfAttribAllocatedBuffer = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 3), BurstSize()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBuffer.setStatus('current')
intSrvIfAttribFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribFlows.setStatus('current')
intSrvIfAttribPropagationDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 5), Integer32()).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribPropagationDelay.setStatus('current')
intSrvIfAttribStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribStatus.setStatus('current')
intSrvFlowTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 2), )
if mibBuilder.loadTexts: intSrvFlowTable.setStatus('current')
intSrvFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 2, 1), ).setIndexNames((0, "INTEGRATED-SERVICES-MIB", "intSrvFlowNumber"))
if mibBuilder.loadTexts: intSrvFlowEntry.setStatus('current')
intSrvFlowNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 1), SessionNumber())
if mibBuilder.loadTexts: intSrvFlowNumber.setStatus('current')
intSrvFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 2), SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowType.setStatus('current')
intSrvFlowOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("rsvp", 2), ("management", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOwner.setStatus('current')
intSrvFlowDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddr.setStatus('current')
intSrvFlowSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddr.setStatus('current')
intSrvFlowDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddrLength.setStatus('current')
intSrvFlowSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddrLength.setStatus('current')
intSrvFlowProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 8), Protocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowProtocol.setStatus('current')
intSrvFlowDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 9), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestPort.setStatus('current')
intSrvFlowPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 10), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowPort.setStatus('current')
intSrvFlowFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowFlowId.setStatus('current')
intSrvFlowInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 12), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowInterface.setStatus('current')
intSrvFlowIfAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowIfAddr.setStatus('current')
intSrvFlowRate = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 14), BitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowRate.setStatus('current')
intSrvFlowBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 15), BurstSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowBurst.setStatus('current')
intSrvFlowWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowWeight.setStatus('current')
intSrvFlowQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowQueue.setStatus('current')
intSrvFlowMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 18), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMinTU.setStatus('current')
intSrvFlowMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 19), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMaxTU.setStatus('current')
intSrvFlowBestEffort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowBestEffort.setStatus('current')
intSrvFlowPoliced = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowPoliced.setStatus('current')
intSrvFlowDiscard = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDiscard.setStatus('current')
intSrvFlowService = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 23), QosService()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowService.setStatus('current')
intSrvFlowOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOrder.setStatus('current')
intSrvFlowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowStatus.setStatus('current')
intSrvFlowNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 52, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intSrvFlowNewIndex.setStatus('current')
intSrvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))
intSrvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 4, 2, 1)).setObjects(("INTEGRATED-SERVICES-MIB", "intSrvIfAttribGroup"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvCompliance = intSrvCompliance.setStatus('current')
intSrvIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 1)).setObjects(("INTEGRATED-SERVICES-MIB", "intSrvIfAttribAllocatedBits"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribMaxAllocatedBits"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribAllocatedBuffer"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribFlows"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribPropagationDelay"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvIfAttribGroup = intSrvIfAttribGroup.setStatus('current')
intSrvFlowsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 2)).setObjects(("INTEGRATED-SERVICES-MIB", "intSrvFlowType"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowOwner"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowSenderAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestAddrLength"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowSenderAddrLength"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowProtocol"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestPort"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowPort"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowInterface"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowBestEffort"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowRate"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowBurst"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowWeight"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowQueue"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowMinTU"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDiscard"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowPoliced"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowService"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowIfAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowOrder"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvFlowsGroup = intSrvFlowsGroup.setStatus('current')
mibBuilder.exportSymbols("INTEGRATED-SERVICES-MIB", intSrvGenObjects=intSrvGenObjects, intSrvFlowBestEffort=intSrvFlowBestEffort, intSrvIfAttribAllocatedBuffer=intSrvIfAttribAllocatedBuffer, intSrvFlowQueue=intSrvFlowQueue, intSrvFlowDestAddr=intSrvFlowDestAddr, intSrvFlowDiscard=intSrvFlowDiscard, intSrvFlowNumber=intSrvFlowNumber, intSrvIfAttribEntry=intSrvIfAttribEntry, intSrvFlowPoliced=intSrvFlowPoliced, intSrvFlowStatus=intSrvFlowStatus, intSrvCompliances=intSrvCompliances, intSrvFlowRate=intSrvFlowRate, intSrvIfAttribMaxAllocatedBits=intSrvIfAttribMaxAllocatedBits, intSrvFlowFlowId=intSrvFlowFlowId, intSrvFlowOwner=intSrvFlowOwner, Protocol=Protocol, SessionNumber=SessionNumber, SessionType=SessionType, intSrvIfAttribGroup=intSrvIfAttribGroup, intSrvIfAttribFlows=intSrvIfAttribFlows, intSrvGroups=intSrvGroups, MessageSize=MessageSize, PYSNMP_MODULE_ID=intSrv, intSrvIfAttribStatus=intSrvIfAttribStatus, intSrvConformance=intSrvConformance, intSrvFlowTable=intSrvFlowTable, BitRate=BitRate, intSrvObjects=intSrvObjects, intSrvNotifications=intSrvNotifications, intSrv=intSrv, intSrvFlowsGroup=intSrvFlowsGroup, intSrvIfAttribTable=intSrvIfAttribTable, intSrvFlowIfAddr=intSrvFlowIfAddr, QosService=QosService, intSrvFlowPort=intSrvFlowPort, intSrvFlowMinTU=intSrvFlowMinTU, intSrvFlowSenderAddr=intSrvFlowSenderAddr, intSrvCompliance=intSrvCompliance, intSrvFlowMaxTU=intSrvFlowMaxTU, BurstSize=BurstSize, intSrvFlowDestAddrLength=intSrvFlowDestAddrLength, intSrvFlowInterface=intSrvFlowInterface, intSrvIfAttribAllocatedBits=intSrvIfAttribAllocatedBits, intSrvFlowSenderAddrLength=intSrvFlowSenderAddrLength, intSrvFlowNewIndex=intSrvFlowNewIndex, intSrvFlowService=intSrvFlowService, intSrvFlowProtocol=intSrvFlowProtocol, intSrvFlowBurst=intSrvFlowBurst, intSrvFlowWeight=intSrvFlowWeight, Port=Port, intSrvFlowOrder=intSrvFlowOrder, intSrvFlowType=intSrvFlowType, intSrvFlowDestPort=intSrvFlowDestPort, intSrvIfAttribPropagationDelay=intSrvIfAttribPropagationDelay, intSrvFlowEntry=intSrvFlowEntry)
