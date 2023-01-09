#
# PySNMP MIB module CTRON-PPC-BAD-PACKETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PPC-BAD-PACKETS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:52 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ctFWDebug, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFWDebug")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Integer32, ModuleIdentity, Gauge32, iso, TimeTicks, Counter64, IpAddress, Unsigned32, ObjectIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Integer32", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctPPCBadPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1))
ctPPCBadPktsTotalTx = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTotalTx.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTotalTx.setDescription('The total number of Transmit Errors PPC has registered on this device (all ports)')
ctPPCBadPktsTotalRx = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTotalRx.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTotalRx.setDescription('The total number of Receive Errors PPC has registered on this device (all ports)')
ctPPCBadPktsTxTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3), )
if mibBuilder.loadTexts: ctPPCBadPktsTxTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxTable.setDescription('Provides traffic error statistics (Transmit side)')
ctPPCBadPktsTxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1), ).setIndexNames((0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsTxIndex"))
if mibBuilder.loadTexts: ctPPCBadPktsTxEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxEntry.setDescription('Defines a particular entry containing objects pertaining to\n       each port.')
ctPPCBadPktsTxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxIndex.setDescription('A value which uniquely identifies a conceptual row in the\n         table. Physical port id.')
ctPPCBadPktsTxQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxQueues.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxQueues.setDescription('The number of Transmit Queues this port is able to support.')
ctPPCBadPktsTxFulls = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxFulls.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxFulls.setDescription('The number of xmit events with queue been full.')
ctPPCBadPktsTxQDepthTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4), )
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepthTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepthTable.setDescription('Provides the current usage for each Tx Queue')
ctPPCBadPktsTxQDepthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1), ).setIndexNames((0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsTxQIndex"), (0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsQ"))
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepthEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepthEntry.setDescription('Defines a particular entry containing objects pertaining to\n       each port and queue.')
ctPPCBadPktsTxQIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxQIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxQIndex.setDescription('A value which uniquely identifies a conceptual row in the\n         table. Physical port id.')
ctPPCBadPktsQ = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsQ.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsQ.setDescription('Index to the queue array.')
ctPPCBadPktsTxQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepth.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepth.setDescription('The number of currently used entries in this queue.')
ctPPCBadPktsRxTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5), )
if mibBuilder.loadTexts: ctPPCBadPktsRxTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxTable.setDescription('Provides traffic error statistics (receive side)')
ctPPCBadPktsRxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1), ).setIndexNames((0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsRxIndex"))
if mibBuilder.loadTexts: ctPPCBadPktsRxEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxEntry.setDescription('Defines a particular entry containing objects pertaining to\n       each port.')
ctPPCBadPktsRxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxIndex.setDescription('A value which uniquely identifies a conceptual row in the\n         table. Physical port id.')
ctPPCBadPktsRxTotalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxTotalErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxTotalErrors.setDescription('The number of bad packets received on this port.')
ctPPCBadPktsRxDescHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDescHigh.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxDescHigh.setDescription('The first half of last bad packet descriptor.')
ctPPCBadPktsRxDescLow = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDescLow.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxDescLow.setDescription('The second half of last bad packet descriptor.')
ctPPCBadPktsRxDaSa0 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa0.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa0.setDescription('The first word of DaSa field from the last bad packet.')
ctPPCBadPktsRxDaSa1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa1.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa1.setDescription('The second word of DaSa field from the last bad packet.')
ctPPCBadPktsRxDaSa2 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa2.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa2.setDescription('The third word of DaSa field from the last bad packet.')
ctPPCBadPktsRxData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxData.setStatus('mandatory')
if mibBuilder.loadTexts: ctPPCBadPktsRxData.setDescription('Data word (maybe tag) from the last bad packet. ')
mibBuilder.exportSymbols("CTRON-PPC-BAD-PACKETS-MIB", ctPPCBadPktsTxQDepthTable=ctPPCBadPktsTxQDepthTable, ctPPCBadPktsTxTable=ctPPCBadPktsTxTable, ctPPCBadPktsTotalRx=ctPPCBadPktsTotalRx, ctPPCBadPktsTxQueues=ctPPCBadPktsTxQueues, ctPPCBadPktsQ=ctPPCBadPktsQ, ctPPCBadPktsRxIndex=ctPPCBadPktsRxIndex, ctPPCBadPktsRxDaSa2=ctPPCBadPktsRxDaSa2, ctPPCBadPktsRxDaSa1=ctPPCBadPktsRxDaSa1, ctPPCBadPktsTxQDepth=ctPPCBadPktsTxQDepth, ctPPCBadPktsTxQIndex=ctPPCBadPktsTxQIndex, ctPPCBadPktsTxIndex=ctPPCBadPktsTxIndex, ctPPCBadPktsRxDaSa0=ctPPCBadPktsRxDaSa0, ctPPCBadPktsTotalTx=ctPPCBadPktsTotalTx, ctPPCBadPktsTxFulls=ctPPCBadPktsTxFulls, ctPPCBadPktsTxQDepthEntry=ctPPCBadPktsTxQDepthEntry, ctPPCBadPktsRxDescHigh=ctPPCBadPktsRxDescHigh, ctPPCBadPkts=ctPPCBadPkts, ctPPCBadPktsRxTable=ctPPCBadPktsRxTable, ctPPCBadPktsTxEntry=ctPPCBadPktsTxEntry, ctPPCBadPktsRxEntry=ctPPCBadPktsRxEntry, ctPPCBadPktsRxDescLow=ctPPCBadPktsRxDescLow, ctPPCBadPktsRxData=ctPPCBadPktsRxData, ctPPCBadPktsRxTotalErrors=ctPPCBadPktsRxTotalErrors)
