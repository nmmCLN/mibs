#
# PySNMP MIB module CTRON-TX-QUEUE-ARBITRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-TX-QUEUE-ARBITRATION-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:00 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ctTxQArb, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTxQArb")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, NotificationType, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctTxQArbConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1))
ctTxQBufferConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 2))
ctTxQPortGroupMapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1), )
if mibBuilder.loadTexts: ctTxQPortGroupMapTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQPortGroupMapTable.setDescription('The ctTxQPortGroupMapTable defines the mapping of interfaces\n        to a specific port group.')
ctTxQPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTxQPortGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQPortGroupEntry.setDescription('Defines a particular entry containing objects pertaining to\n       definition and control over interfaces supporting multiple transmit\n       queue arbitration.')
ctTxQPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTxQPortGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQPortGroup.setDescription('Indicates the transmit queue port group to which the interface\n       claims membership.  The specific interface is indicated\n       by the instancing information.')
ctTxQArbTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2), )
if mibBuilder.loadTexts: ctTxQArbTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQArbTable.setDescription('A table containing entries to specify the approximate priority\n       for servicing of each transmit queue for each port group on the \n       device.')
ctTxQArbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1), ).setIndexNames((0, "CTRON-TX-QUEUE-ARBITRATION-MIB", "ctTxQPortGroup"))
if mibBuilder.loadTexts: ctTxQArbEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQArbEntry.setDescription('Specifies the entries in the ctTxQArbTable.')
ctTxQArbNumQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTxQArbNumQueues.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQArbNumQueues.setDescription('The number of transmit queues for each port in this port group.')
ctTxQArbNumSlices = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTxQArbNumSlices.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQArbNumSlices.setDescription("The number of 'slices' into which transmit resources are divided.  This\n       determines the resolution with which transmit priority can be allocated\n       to each of the transmit queues.  For example, if the number of slices\n       is 16, then transmit resources may be allocated to each transmit queue\n       in units of 1/16 (6.25% of the total).  The numbers of slices allocated\n       to all queues must add up to the value of this object (i.e., 100%).")
ctTxQArbSetting = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTxQArbSetting.setStatus('mandatory')
if mibBuilder.loadTexts: ctTxQArbSetting.setDescription("The approximate percentage of a port's transmit resources to\n       be allocated to each transmit queue.  This allows for fine-tuning\n       of the 'strict priority' configuration.\n\n       Under strict priority, the highest queue (ctTxQArbNumQueues - 1)\n       has the highest priority, followed by (ctTxQArbNumQueues - 2), etc.\n       Queue 0 always has the lowest priority.  All entries in a higher\n       priority queue will be transmitted before any entries from the lower\n       priority queues.  This object allows the modification of the strict \n       priority scheme so that lower priority queues can be guaranteed some\n       access to the transmitter.\n\n       This object is an octet string in which the number of octets corresponds\n       to the number of transmit queues for each port in this port group,\n       as indicated by ctTxQArbNumQueues.  The value of the first octet \n       represents the number of 'slices' of transmit resources to allocate to \n       Queue 0, the second octet represents the number for Queue 1, and so\n       forth.  The sum of all the octets in the octet string must add up to \n       the total number of slices available for the port.\n\n       For example, on a port having 4 transmit queues and where transmit \n       resources are divided into 16 slices, writing an octet string of \n       {0x00, 0x04, 0x04, 0x08} would have the following effect:\n\n           At least 50% of the frames transmitted are from Queue 3\n           At least 25% of the frames transmitted are from Queue 2\n           At least 25% of the frames transmitted are from Queue 1\n           No frames will be transmitted from Queue 0 until Queues 1, 2 and 3\n           are empty.")
ctTxQBufferOptimizeEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTxQBufferOptimizeEnable.setStatus('optional')
if mibBuilder.loadTexts: ctTxQBufferOptimizeEnable.setDescription('enabled  (1) - optimize system buffer distribution for default CoS queue\n       disabled (2) - use default system buffer distribution.')
mibBuilder.exportSymbols("CTRON-TX-QUEUE-ARBITRATION-MIB", ctTxQArbConfig=ctTxQArbConfig, ctTxQBufferOptimizeEnable=ctTxQBufferOptimizeEnable, ctTxQPortGroupEntry=ctTxQPortGroupEntry, ctTxQArbSetting=ctTxQArbSetting, ctTxQBufferConfig=ctTxQBufferConfig, ctTxQArbEntry=ctTxQArbEntry, ctTxQArbNumSlices=ctTxQArbNumSlices, ctTxQPortGroup=ctTxQPortGroup, ctTxQArbNumQueues=ctTxQArbNumQueues, ctTxQArbTable=ctTxQArbTable, ctTxQPortGroupMapTable=ctTxQPortGroupMapTable)
