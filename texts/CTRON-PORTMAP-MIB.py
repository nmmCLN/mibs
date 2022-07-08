#
# PySNMP MIB module CTRON-PORTMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PORTMAP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:35 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ctPortMap, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPortMap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, ModuleIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "ModuleIdentity", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
portMap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1))
portMapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1), )
if mibBuilder.loadTexts: portMapTable.setStatus('mandatory')
if mibBuilder.loadTexts: portMapTable.setDescription('This table identifies the repeater which the port \n                 belongs to.')
portMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1), ).setIndexNames((0, "CTRON-PORTMAP-MIB", "portMapIndex"))
if mibBuilder.loadTexts: portMapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portMapEntry.setDescription('Provides basic mapping and capability for a specific port.')
portMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapIndex.setStatus('mandatory')
if mibBuilder.loadTexts: portMapIndex.setDescription('Returns an index to a port for which the information\n                 in this table pertains.')
portMapRepeater = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapRepeater.setStatus('mandatory')
if mibBuilder.loadTexts: portMapRepeater.setDescription('Gives the repeater number that this port is connected to.')
portMapCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapCapability.setStatus('mandatory')
if mibBuilder.loadTexts: portMapCapability.setDescription('This indicates the technology ability of the local hardware.\n                The value of this object is the logical OR of all supported\n                technologies, where each technology is given the values below:\n                         \n                other(1)                      Undefined, or ability not known\n                Auto-Negotiation(2)           Auto-Negotiation\n                10BASE-T(4)                   10BASE-T\n                100BASE-TX(8)                 100BASE-TX\n                1000BASE(16)                  1000BASE                  \n                \n                For example, a port that has the capability of supporting \n                10BASE-T and 100BASE-TX would have a value of 12 (4 + 8).')
portMapOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portMapOperationalMode.setStatus('mandatory')
if mibBuilder.loadTexts: portMapOperationalMode.setDescription(' This indicates the current operational mode of this port.\n                This value is a logical OR of the current operational mode,\n                where each technology is given the values below:\n\n                other(1)                      Undefined, or ability not known\n                Auto-Negotiation(2)           Auto-Negotiation\n                10BASE-T(4)                   10BASE-T\n                100BASE-TX(8)                 100BASE-TX\n                1000BASE(16)                  1000BASE                  \n\n                For example, a port that has auto-negotiated to a speed of \n                100BASE-TX would have a value of 10 (2 + 8).')
portMapLastSeenSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapLastSeenSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: portMapLastSeenSrcAddr.setDescription('Returns last source address seen by this repeater port.')
mibBuilder.exportSymbols("CTRON-PORTMAP-MIB", portMapOperationalMode=portMapOperationalMode, portMapIndex=portMapIndex, portMapCapability=portMapCapability, portMapEntry=portMapEntry, portMapTable=portMapTable, portMap=portMap, portMapRepeater=portMapRepeater, portMapLastSeenSrcAddr=portMapLastSeenSrcAddr)
