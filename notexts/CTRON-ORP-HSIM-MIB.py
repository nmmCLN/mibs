#
# PySNMP MIB module CTRON-ORP-HSIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ORP-HSIM-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:39 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ctOrpHSIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctOrpHSIM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Bits, NotificationType, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Counter32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Counter32", "iso", "IpAddress")
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
mibBuilder.exportSymbols("CTRON-ORP-HSIM-MIB", ctOrpHSIMIndex=ctOrpHSIMIndex, ctOrpHSIMTable=ctOrpHSIMTable, ctOrpHSIMMACAddress=ctOrpHSIMMACAddress, ctOrpHSIMSlot=ctOrpHSIMSlot, ctOrpHSIMIfRef=ctOrpHSIMIfRef, ctOrpHSIMIPAddress=ctOrpHSIMIPAddress, ctOrpHSIMRWCommName=ctOrpHSIMRWCommName, ctOrpHSIMSUCommName=ctOrpHSIMSUCommName, ctOrpHSIMROCommName=ctOrpHSIMROCommName, ctOrpHSIMEntry=ctOrpHSIMEntry, ctOrpHSIMSubnetMask=ctOrpHSIMSubnetMask, MacAddress=MacAddress)
