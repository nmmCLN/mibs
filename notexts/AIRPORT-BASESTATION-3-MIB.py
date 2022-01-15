#
# PySNMP MIB module AIRPORT-BASESTATION-3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/airport/AIRPORT-BASESTATION-3-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:09 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Integer32, iso, ModuleIdentity, enterprises, MibIdentifier, IpAddress, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Integer32", "iso", "ModuleIdentity", "enterprises", "MibIdentifier", "IpAddress", "Counter32", "Counter64")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
baseStation3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 63, 501, 3))
if mibBuilder.loadTexts: baseStation3.setLastUpdated('200301160001Z')
if mibBuilder.loadTexts: baseStation3.setOrganization('Apple Computer, Inc.')
apple = MibIdentifier((1, 3, 6, 1, 4, 1, 63))
airport = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501))
abs3SysConf = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 1))
sysConfName = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysConfName.setStatus('current')
sysConfContact = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysConfContact.setStatus('current')
sysConfLocation = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysConfLocation.setStatus('current')
sysConfUptime = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysConfUptime.setStatus('current')
sysConfFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysConfFirmwareVersion.setStatus('current')
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 2))
wirelessNumber = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessNumber.setStatus('current')
wirelessClientsTable = MibTable((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2), )
if mibBuilder.loadTexts: wirelessClientsTable.setStatus('current')
wirelessClient = MibTableRow((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1), ).setIndexNames((0, "AIRPORT-BASESTATION-3-MIB", "wirelessPhysAddress"))
if mibBuilder.loadTexts: wirelessClient.setStatus('current')
wirelessPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessPhysAddress.setStatus('current')
wirelessType = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sta", 1), ("wds", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessType.setStatus('current')
wirelessDataRates = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessDataRates.setStatus('current')
wirelessTimeAssociated = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessTimeAssociated.setStatus('current')
wirelessLastRefreshTime = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessLastRefreshTime.setStatus('current')
wirelessStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessStrength.setStatus('current')
wirelessNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessNoise.setStatus('current')
wirelessRate = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessRate.setStatus('current')
wirelessNumRX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessNumRX.setStatus('current')
wirelessNumTX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessNumTX.setStatus('current')
wirelessNumRXErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessNumRXErrors.setStatus('current')
wirelessNumTXErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wirelessNumTXErrors.setStatus('current')
dhcpServer = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 3))
dhcpNumber = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpNumber.setStatus('current')
dhcpClientsTable = MibTable((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2), )
if mibBuilder.loadTexts: dhcpClientsTable.setStatus('current')
dhcpClient = MibTableRow((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1), ).setIndexNames((0, "AIRPORT-BASESTATION-3-MIB", "dhcpPhysAddress"))
if mibBuilder.loadTexts: dhcpClient.setStatus('current')
dhcpPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPhysAddress.setStatus('current')
dhcpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpIpAddress.setStatus('current')
dhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpClientID.setStatus('current')
dhcpLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseTime.setStatus('current')
physicalInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 4))
physicalInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceCount.setStatus('current')
physicalInterfacesTable = MibTable((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2), )
if mibBuilder.loadTexts: physicalInterfacesTable.setStatus('current')
physicalInterface = MibTableRow((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1), ).setIndexNames((0, "AIRPORT-BASESTATION-3-MIB", "physicalInterfaceIndex"))
if mibBuilder.loadTexts: physicalInterface.setStatus('current')
physicalInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceIndex.setStatus('current')
physicalInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceName.setStatus('current')
physicalInterfaceUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceUnit.setStatus('current')
physicalInterfaceSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceSpeed.setStatus('current')
physicalInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("linkDown", 0), ("linkUp", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceState.setStatus('current')
physicalInterfaceDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("half", 0), ("full", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceDuplex.setStatus('current')
physicalInterfaceNumTX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceNumTX.setStatus('current')
physicalInterfaceNumRX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceNumRX.setStatus('current')
physicalInterfaceNumTXError = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceNumTXError.setStatus('current')
physicalInterfaceNumRXError = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalInterfaceNumRXError.setStatus('current')
mibBuilder.exportSymbols("AIRPORT-BASESTATION-3-MIB", wirelessNumber=wirelessNumber, wirelessNumTXErrors=wirelessNumTXErrors, dhcpLeaseTime=dhcpLeaseTime, dhcpNumber=dhcpNumber, physicalInterfaceNumRXError=physicalInterfaceNumRXError, physicalInterfaceUnit=physicalInterfaceUnit, dhcpPhysAddress=dhcpPhysAddress, wirelessPhysAddress=wirelessPhysAddress, wirelessNumRXErrors=wirelessNumRXErrors, dhcpClientsTable=dhcpClientsTable, physicalInterfacesTable=physicalInterfacesTable, physicalInterfaceNumTXError=physicalInterfaceNumTXError, wirelessType=wirelessType, physicalInterfaceIndex=physicalInterfaceIndex, sysConfUptime=sysConfUptime, dhcpClient=dhcpClient, physicalInterface=physicalInterface, baseStation3=baseStation3, dhcpServer=dhcpServer, dhcpClientID=dhcpClientID, physicalInterfaceState=physicalInterfaceState, PYSNMP_MODULE_ID=baseStation3, wirelessTimeAssociated=wirelessTimeAssociated, wirelessNumRX=wirelessNumRX, physicalInterfaceNumRX=physicalInterfaceNumRX, wirelessClientsTable=wirelessClientsTable, physicalInterfaceNumTX=physicalInterfaceNumTX, sysConfName=sysConfName, wirelessRate=wirelessRate, dhcpIpAddress=dhcpIpAddress, apple=apple, physicalInterfaceCount=physicalInterfaceCount, sysConfLocation=sysConfLocation, physicalInterfaceSpeed=physicalInterfaceSpeed, abs3SysConf=abs3SysConf, sysConfContact=sysConfContact, airport=airport, wireless=wireless, physicalInterfaceDuplex=physicalInterfaceDuplex, wirelessNumTX=wirelessNumTX, wirelessNoise=wirelessNoise, wirelessStrength=wirelessStrength, wirelessLastRefreshTime=wirelessLastRefreshTime, sysConfFirmwareVersion=sysConfFirmwareVersion, physicalInterfaces=physicalInterfaces, wirelessClient=wirelessClient, wirelessDataRates=wirelessDataRates, physicalInterfaceName=physicalInterfaceName)
