#
# PySNMP MIB module CTRMONXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRMONXT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:12 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctronRmon, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronRmon")
OwnerString, EntryStatus = mibBuilder.importSymbols("RMON-MIB", "OwnerString", "EntryStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctDiscovery = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20))
ctDiscoveryProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1))
ctProtIP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 1))
ctProtNetware = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 2))
ctProtDecNet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 3))
ctDiscoveryControlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2), )
if mibBuilder.loadTexts: ctDiscoveryControlTable.setStatus('mandatory')
ctDiscoveryControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1), ).setIndexNames((0, "CTRMONXT-MIB", "ctDiscoveryControlIndex"))
if mibBuilder.loadTexts: ctDiscoveryControlEntry.setStatus('mandatory')
ctDiscoveryControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryControlIndex.setStatus('mandatory')
ctDiscoveryControlDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlDataSource.setStatus('mandatory')
ctDiscoveryControlProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlProtocol.setStatus('mandatory')
ctDiscoveryControlTableSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryControlTableSize.setStatus('mandatory')
ctDiscoveryControlLastDeleteTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryControlLastDeleteTime.setStatus('mandatory')
ctDiscoveryControlAgeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlAgeInterval.setStatus('mandatory')
ctDiscoveryControlOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 7), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlOwner.setStatus('mandatory')
ctDiscoveryControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 8), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDiscoveryControlStatus.setStatus('mandatory')
ctDiscoveryMNTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3), )
if mibBuilder.loadTexts: ctDiscoveryMNTable.setStatus('mandatory')
ctDiscoveryMNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1), ).setIndexNames((0, "CTRMONXT-MIB", "ctDiscoveryMNIndex"), (0, "CTRMONXT-MIB", "ctDiscoveryMNMACAddress"), (0, "CTRMONXT-MIB", "ctDiscoveryMNNetworkAddress"))
if mibBuilder.loadTexts: ctDiscoveryMNEntry.setStatus('mandatory')
ctDiscoveryMNMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNMACAddress.setStatus('mandatory')
ctDiscoveryMNNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNNetworkAddress.setStatus('mandatory')
ctDiscoveryMNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNIndex.setStatus('mandatory')
ctDiscoveryMNCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNCreationTime.setStatus('mandatory')
ctDiscoveryMNLastTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNLastTransmitTime.setStatus('mandatory')
ctDiscoveryMNBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNBoard.setStatus('mandatory')
ctDiscoveryMNPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryMNPort.setStatus('mandatory')
ctDiscoveryNMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4), )
if mibBuilder.loadTexts: ctDiscoveryNMTable.setStatus('mandatory')
ctDiscoveryNMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1), ).setIndexNames((0, "CTRMONXT-MIB", "ctDiscoveryNMIndex"), (0, "CTRMONXT-MIB", "ctDiscoveryNMNetworkAddress"), (0, "CTRMONXT-MIB", "ctDiscoveryNMMACAddress"))
if mibBuilder.loadTexts: ctDiscoveryNMEntry.setStatus('mandatory')
ctDiscoveryNMNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMNetworkAddress.setStatus('mandatory')
ctDiscoveryNMMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMMACAddress.setStatus('mandatory')
ctDiscoveryNMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMIndex.setStatus('mandatory')
ctDiscoveryNMCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMCreationTime.setStatus('mandatory')
ctDiscoveryNMLastTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMLastTransmitTime.setStatus('mandatory')
ctDiscoveryNMBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMBoard.setStatus('mandatory')
ctDiscoveryNMPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDiscoveryNMPort.setStatus('mandatory')
mibBuilder.exportSymbols("CTRMONXT-MIB", ctDiscoveryNMPort=ctDiscoveryNMPort, ctDiscoveryControlEntry=ctDiscoveryControlEntry, ctDiscovery=ctDiscovery, ctDiscoveryNMTable=ctDiscoveryNMTable, ctDiscoveryControlLastDeleteTime=ctDiscoveryControlLastDeleteTime, ctDiscoveryControlAgeInterval=ctDiscoveryControlAgeInterval, ctDiscoveryMNEntry=ctDiscoveryMNEntry, ctDiscoveryNMIndex=ctDiscoveryNMIndex, ctDiscoveryControlIndex=ctDiscoveryControlIndex, ctDiscoveryControlTableSize=ctDiscoveryControlTableSize, ctDiscoveryControlTable=ctDiscoveryControlTable, ctDiscoveryControlProtocol=ctDiscoveryControlProtocol, ctDiscoveryNMBoard=ctDiscoveryNMBoard, ctDiscoveryNMEntry=ctDiscoveryNMEntry, ctDiscoveryNMLastTransmitTime=ctDiscoveryNMLastTransmitTime, ctProtIP=ctProtIP, ctDiscoveryNMNetworkAddress=ctDiscoveryNMNetworkAddress, ctProtDecNet=ctProtDecNet, ctDiscoveryControlOwner=ctDiscoveryControlOwner, ctDiscoveryNMCreationTime=ctDiscoveryNMCreationTime, ctDiscoveryMNCreationTime=ctDiscoveryMNCreationTime, ctDiscoveryMNLastTransmitTime=ctDiscoveryMNLastTransmitTime, ctDiscoveryMNMACAddress=ctDiscoveryMNMACAddress, ctProtNetware=ctProtNetware, ctDiscoveryMNPort=ctDiscoveryMNPort, ctDiscoveryMNIndex=ctDiscoveryMNIndex, ctDiscoveryControlStatus=ctDiscoveryControlStatus, ctDiscoveryProtocol=ctDiscoveryProtocol, ctDiscoveryNMMACAddress=ctDiscoveryNMMACAddress, ctDiscoveryControlDataSource=ctDiscoveryControlDataSource, ctDiscoveryMNBoard=ctDiscoveryMNBoard, ctDiscoveryMNNetworkAddress=ctDiscoveryMNNetworkAddress, ctDiscoveryMNTable=ctDiscoveryMNTable)
