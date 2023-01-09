#
# PySNMP MIB module CTINB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTINB2-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:52 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ctINBinfo2, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctINBinfo2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Integer32, ModuleIdentity, Gauge32, iso, TimeTicks, Counter64, IpAddress, Unsigned32, ObjectIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Integer32", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctInbUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1))
ctInbUtilInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctInbUtilInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilInterval.setDescription('The length of the sampling interval in seconds used for all INB\n            utilization measurements and calculations.')
ctInbUtilTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2), )
if mibBuilder.loadTexts: ctInbUtilTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilTable.setDescription('A list of byte counts and absolute utilization percentages reflecting\n           data transferred via the INB during the last sampling interval.')
ctInbUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1), ).setIndexNames((0, "CTINB2-MIB", "ctInbUtilSrcSlot"), (0, "CTINB2-MIB", "ctInbUtilDestSlot"))
if mibBuilder.loadTexts: ctInbUtilEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilEntry.setDescription('Byte counts and utilization percentages reflecting data transferred\n            from a source module to a destination module via the INB.')
ctInbUtilSrcSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilSrcSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilSrcSlot.setDescription('The chassis slot number containing the module from which bytes are\n            transmitted onto the INB.')
ctInbUtilDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilDestSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilDestSlot.setDescription('The chassis slot number containing the module to which bytes are\n            transmitted across the INB.')
ctInbUtilHiByteCountA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilHiByteCountA.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilHiByteCountA.setDescription('The high-order 32 bits of the 64-bit entity which represents the number\n            of bytes transferred from the source module to the destination module\n            across INB channel A during the last sampling interval.  This 64-bit\n            byte count may be calculated as:\n              ctInbUtilByteCountA = (ctInbUtilHiByteCountA * 2**32) + ctInbUtilLoByteCountA ')
ctInbUtilLoByteCountA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilLoByteCountA.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilLoByteCountA.setDescription('The low-order 32 bits of the 64-bit entity which represents the number\n            of bytes transferred from the source module to the destination module\n            across INB channel A during the last sampling interval.  This 64-bit\n            byte count may be calculated as:\n              ctInbUtilByteCountA = (ctInbUtilHiByteCountA * 2**32) + ctInbUtilLoByteCountA ')
ctInbUtilHiByteCountB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilHiByteCountB.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilHiByteCountB.setDescription('The high-order 32 bits of the 64-bit entity which represents the number\n            of bytes transferred from the source module to the destination module\n            across INB channel B during the last sampling interval.  This 64-bit\n            byte count may be calculated as:\n              ctInbUtilByteCountB = (ctInbUtilHiByteCountB * 2**32) + ctInbUtilLoByteCountB ')
ctInbUtilLoByteCountB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilLoByteCountB.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilLoByteCountB.setDescription('The low-order 32 bits of the 64-bit entity which represents the number\n            of bytes transferred from the source module to the destination module\n            across INB channel B during the last sampling interval.  This 64-bit\n            byte count may be calculated as:\n              ctInbUtilByteCountB = (ctInbUtilHiByteCountB * 2**32) + ctInbUtilLoByteCountB ')
ctInbUtilAbsoluteA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteA.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilAbsoluteA.setDescription('The percentage of absolute utilization of INB channel A by data transferred\n            from the source module to the destination module during the last sampling\n            interval.  This percentage is calculated by dividing ctInbUtilByteCountA\n            (a 64-bit entity which is calculated as specified above) by\n            the theoretical maximum number of bytes that could have traversed INB\n            channel A during the interval.  Note that in order to increase precision,\n            the value of this object is the actual percentage multiplied by 100 (that\n            is, to determine the actual percentage, divide the value of this object by\n            100).')
ctInbUtilAbsoluteB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteB.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilAbsoluteB.setDescription('The percentage of absolute utilization of INB channel B by data transferred\n            from the source module to the destination module during the last sampling\n            interval.  This percentage is calculated by dividing ctInbUtilByteCountB\n            (a 64-bit entity which is calculated as specified above) by\n            the theoretical maximum number of bytes that could have traversed INB\n            channel B during the interval.  Note that in order to increase precision,\n            the value of this object is the actual percentage multiplied by 100 (that\n            is, to determine the actual percentage, divide the value of this object by\n            100).')
ctInbUtilAbsoluteTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteTotal.setStatus('mandatory')
if mibBuilder.loadTexts: ctInbUtilAbsoluteTotal.setDescription('The percentage of absolute utilization of the total INB by data transferred\n            from the source module to the destination module during the last sampling\n            interval.  This percentage is calculated by dividing the sum of\n            ctInbUtilByteCountA and ctInbUtilByteCountB by the theoretical maximum number\n            of bytes that could have traversed both INB channels during the interval.\n            Note that in order to increase precision, the value of this object is the\n            actual percentage multiplied by 100 (that is, to determine the actual\n            percentage, divide the value of this object by 100).')
mibBuilder.exportSymbols("CTINB2-MIB", ctInbUtilSrcSlot=ctInbUtilSrcSlot, ctInbUtilHiByteCountA=ctInbUtilHiByteCountA, ctInbUtilEntry=ctInbUtilEntry, ctInbUtilDestSlot=ctInbUtilDestSlot, ctInbUtilHiByteCountB=ctInbUtilHiByteCountB, ctInbUtilAbsoluteB=ctInbUtilAbsoluteB, ctInbUtilAbsoluteTotal=ctInbUtilAbsoluteTotal, ctInbUtilAbsoluteA=ctInbUtilAbsoluteA, ctInbUtilLoByteCountB=ctInbUtilLoByteCountB, ctInbUtilLoByteCountA=ctInbUtilLoByteCountA, ctInbUtilTable=ctInbUtilTable, ctInbUtilInterval=ctInbUtilInterval, ctInbUtil=ctInbUtil)
