#
# PySNMP MIB module CTRON-ORP-HSIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ORP-HSIM-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ctOrpHSIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctOrpHSIM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

ctOrpHSIMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1), )
if mibBuilder.loadTexts: ctOrpHSIMTable.setStatus('mandatory')
ctOrpHSIMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1), ).setIndexNames((0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMSlot"), (0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMIndex"))
if mibBuilder.loadTexts: ctOrpHSIMEntry.setStatus('mandatory')
ctOrpHSIMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMSlot.setStatus('mandatory')
ctOrpHSIMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIndex.setStatus('mandatory')
ctOrpHSIMIfRef = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIfRef.setStatus('mandatory')
ctOrpHSIMMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMMACAddress.setStatus('mandatory')
ctOrpHSIMIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMIPAddress.setStatus('mandatory')
ctOrpHSIMSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSubnetMask.setStatus('mandatory')
ctOrpHSIMROCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMROCommName.setStatus('mandatory')
ctOrpHSIMRWCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMRWCommName.setStatus('mandatory')
ctOrpHSIMSUCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSUCommName.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ORP-HSIM-MIB", ctOrpHSIMIndex=ctOrpHSIMIndex, ctOrpHSIMTable=ctOrpHSIMTable, ctOrpHSIMIPAddress=ctOrpHSIMIPAddress, ctOrpHSIMIfRef=ctOrpHSIMIfRef, ctOrpHSIMSubnetMask=ctOrpHSIMSubnetMask, ctOrpHSIMSlot=ctOrpHSIMSlot, ctOrpHSIMSUCommName=ctOrpHSIMSUCommName, ctOrpHSIMRWCommName=ctOrpHSIMRWCommName, ctOrpHSIMEntry=ctOrpHSIMEntry, ctOrpHSIMMACAddress=ctOrpHSIMMACAddress, MacAddress=MacAddress, ctOrpHSIMROCommName=ctOrpHSIMROCommName)
