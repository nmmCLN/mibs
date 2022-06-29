#
# PySNMP MIB module RADLAN-MAC-BASE-PRIO (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-MAC-BASE-PRIO
# Produced by pysmi-1.1.8 at Wed Jun 29 13:14:41 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
RowStatus, = mibBuilder.importSymbols("RADLAN-SNMPv2", "RowStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, Gauge32, NotificationType, TimeTicks, ModuleIdentity, IpAddress, ObjectIdentity, Counter32, Counter64, Unsigned32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "NotificationType", "TimeTicks", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "Unsigned32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
rlMacBasePrio = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 101))
rlMacBasePrioMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMacBasePrioMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioMibVersion.setDescription('Indicates the snmp support version that is supported by\n        this device.')
rlMacBasePrioSupport = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMacBasePrioSupport.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSupport.setDescription('indicates which features of the max base prio\n        are supported:\n            (bit 0 is the most significant bit)\n            bit 0 - ForceL3Cos\n            bit 1 - SADA_TC\n        ')
rlMacBasePrioForceL3CosEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosEnable.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosEnable.setDescription('This variable controlls the activation of ForceL3Cos feature in Mac base\n        priority')
rlMacBasePrioForceL3CosTable = MibTable((1, 3, 6, 1, 4, 1, 89, 101, 4), )
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosTable.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosTable.setDescription('A table that contains information about ranges\n        of addresses that are used in the mac based ptiority\n        with the ForceL3Cos feature.')
rlMacBasePrioForceL3CosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 101, 4, 1), ).setIndexNames((0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosAddress"), (0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosMask"))
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosEntry.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosEntry.setDescription('Information about ranges of  MAC addresses\n        that are used in the mac based priority with\n        the ForeL3Cos feature')
rlMacBasePrioForceL3CosAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 4, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosAddress.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosAddress.setDescription('The range of address of this entry.\n        The range may not hold MAC multicast addresses. ')
rlMacBasePrioForceL3CosMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 4, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosMask.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosMask.setDescription('Indicate the mask to be logical-ANDed with the\n        learned  address  before  being compared to\n        the value  in  the  rlMacBasePrioForceL3CosAddress  field.')
rlMacBasePrioForceL3CosRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosRowStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
rlMacBasePrioForceL3CosParamsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 101, 5), )
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsTable.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsTable.setDescription('The table holds the global parameters of\n        the L3 cos :TC, UP,DSCP.')
rlMacBasePrioForceL3CosParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 101, 5, 1), ).setIndexNames((0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosParamsEntryIndex"))
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntry.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntry.setDescription('')
rlMacBasePrioForceL3CosParamsEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryIndex.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryIndex.setDescription('Index of the ForceL3Cos parameters table.')
rlMacBasePrioForceL3CosParamsEntryTC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryTC.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryTC.setDescription('The value of the globla TC')
rlMacBasePrioForceL3CosParamsEntryUP = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryUP.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryUP.setDescription('The value of the globla UP')
rlMacBasePrioForceL3CosParamsEntryDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryDSCP.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryDSCP.setDescription('The value of the globla DSCP')
rlMacBasePrioSADATCEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCEnable.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSADATCEnable.setDescription('This variable controlls the activation of SA/DA priority feature in Mac base\n        priority')
rlMacBasePrioSADATCTable = MibTable((1, 3, 6, 1, 4, 1, 89, 101, 7), )
if mibBuilder.loadTexts: rlMacBasePrioSADATCTable.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSADATCTable.setDescription('A table that contains information about ranges\n        of addresses that are used in the mac based ptiority\n        with the ForceL3Cos feature.')
rlMacBasePrioSADATCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 101, 7, 1), ).setIndexNames((0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioSADATCAddress"), (0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioSADATCMask"))
if mibBuilder.loadTexts: rlMacBasePrioSADATCEntry.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSADATCEntry.setDescription('Information about ranges of  MAC addresses\n        that are used in the mac based priority with\n        the ForeL3Cos feature')
rlMacBasePrioSADATCAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCAddress.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSADATCAddress.setDescription('The range of address of this entry.\n        The range may not hold MAC multicast addresses. ')
rlMacBasePrioSADATCMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCMask.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSADATCMask.setDescription('Indicate the mask to be logical-ANDed with the\n        learned  address  before  being compared to\n        the value  in  the  rlMacBasePrioSADATCAddress  field.')
rlMacBasePrioSADATCPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCPrio.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSADATCPrio.setDescription('The priority that will assign to all MAC\n        addresses that are match the range of this entry.')
rlMacBasePrioSADATCRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlMacBasePrioSADATCRowStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
mibBuilder.exportSymbols("RADLAN-MAC-BASE-PRIO", rlMacBasePrioForceL3CosParamsEntryUP=rlMacBasePrioForceL3CosParamsEntryUP, rlMacBasePrioSADATCMask=rlMacBasePrioSADATCMask, rlMacBasePrioForceL3CosEnable=rlMacBasePrioForceL3CosEnable, rlMacBasePrioSADATCPrio=rlMacBasePrioSADATCPrio, rlMacBasePrioForceL3CosAddress=rlMacBasePrioForceL3CosAddress, rlMacBasePrioSADATCAddress=rlMacBasePrioSADATCAddress, rlMacBasePrioSADATCEntry=rlMacBasePrioSADATCEntry, rlMacBasePrioSADATCTable=rlMacBasePrioSADATCTable, rlMacBasePrioForceL3CosEntry=rlMacBasePrioForceL3CosEntry, rlMacBasePrioForceL3CosParamsEntry=rlMacBasePrioForceL3CosParamsEntry, rlMacBasePrioSADATCEnable=rlMacBasePrioSADATCEnable, rlMacBasePrioForceL3CosMask=rlMacBasePrioForceL3CosMask, rlMacBasePrioSupport=rlMacBasePrioSupport, rlMacBasePrioForceL3CosRowStatus=rlMacBasePrioForceL3CosRowStatus, rlMacBasePrioForceL3CosParamsEntryTC=rlMacBasePrioForceL3CosParamsEntryTC, rlMacBasePrioForceL3CosParamsTable=rlMacBasePrioForceL3CosParamsTable, rlMacBasePrioForceL3CosTable=rlMacBasePrioForceL3CosTable, rlMacBasePrioForceL3CosParamsEntryDSCP=rlMacBasePrioForceL3CosParamsEntryDSCP, rlMacBasePrioSADATCRowStatus=rlMacBasePrioSADATCRowStatus, rlMacBasePrioForceL3CosParamsEntryIndex=rlMacBasePrioForceL3CosParamsEntryIndex, rlMacBasePrio=rlMacBasePrio, rlMacBasePrioMibVersion=rlMacBasePrioMibVersion)
