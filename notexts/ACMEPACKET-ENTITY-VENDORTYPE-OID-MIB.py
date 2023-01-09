#
# PySNMP MIB module ACMEPACKET-ENTITY-VENDORTYPE-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-ENTITY-VENDORTYPE-OID-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketModules, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketModules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, MibIdentifier, iso, Unsigned32, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "iso", "Unsigned32", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acmepacketEntityVendortypeOIDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 6, 1))
acmepacketEntityVendortypeOIDMIB.setRevisions(('2014-06-26 00:00', '2018-08-06 00:00', '2019-05-04 00:00',))
if mibBuilder.loadTexts: acmepacketEntityVendortypeOIDMIB.setLastUpdated('201905040000Z')
if mibBuilder.loadTexts: acmepacketEntityVendortypeOIDMIB.setOrganization('Oracle Communications')
apevMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1))
apevOther = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 1))
apevUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 2))
apevChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3))
apevChassisUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 1))
apevChassisSD = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2))
apevChassisSDUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 1))
apevChassisSD1 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 2))
apevChassisSD2 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 3))
apevChassisSD2QoS = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 4))
apevChassisSD3 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 5))
apevChassisSD4 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 6))
apevChassisSD5 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 7))
apevChassisSD6 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 8))
apevChassisSR = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 3))
apevContainer = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4))
apevContainerUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 1))
apevContainerSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2))
apevContainerSlotUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2, 1))
apevContainerSlotPHY = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2, 2))
apevContainerSlotPCMCIA = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2, 3))
apevContainerDaughterCard = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3))
apevContainerDaughterCardUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 1))
apevContainerDaughterCardCAM = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 2))
apevContainerDaughterCardCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 3))
apevContainerDaughterCardPMC = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 4))
apevContainerDaughterCardMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 5))
apevContainerDaughterCardTLS = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 6))
apevContainerPowerTray = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 4))
apevContainerFanTray = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 5))
apevContainerModules = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 6))
apevPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5))
apevPowerSupplyUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 1))
apevPowerSupply150W = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 2))
apevPowerSupply300W = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 3))
apevPowerSupply1100W = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 4))
apevPowerSupply60W = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 5))
apevPowerSupply500W = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 6))
apevPowerSupply800W = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 7))
apevFan = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6))
apevFanUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 1))
apevFan40x20 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 2))
apevFan40x28 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 3))
apevFan40x10 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 4))
apevFan40x56 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 5))
apevSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7))
apevSensorUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 1))
apevSensorTemperature = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 2))
apevSensorVoltage = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 3))
apevSensorFanSpeed = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 4))
apevModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8))
apevModuleUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 1))
apevModulePHYCard = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2))
apevPHYCardUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 1))
apevPHY1GigPortMultiMode = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 2))
apevPHY1GigPortSingleMode = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 3))
apevPHY2GigPortstMultiMode = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 4))
apevPHY2GigPortsSingleMode = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 5))
apecPHY4FEPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 6))
apevPHY4FEPorts1089 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 7))
apevPHY2GigPortsSec = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 8))
apevPHY2FEPortsSec = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 9))
apevPHY4GigPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 10))
apevPHY4SFPPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 11))
apevPHY44SFPPortsSecQos = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 12))
apevPHY4SFPPortsQos = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 13))
apevPHY4SFPPortsSec = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 14))
apevPHY8FEPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 15))
apevPHY4SFPPortsSecQosCav = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 16))
apevPHY210GigPortsDataPlane = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 17))
apevPHYTranscodingCarrier = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 18))
apevPHYISR = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 19))
apevPHY210GigSecPortsDataPlane = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 20))
apevPHY410GigSecPortsDataPlane = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 21))
apevModuleCAM = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3))
apevModuleCAMUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3, 1))
apevModuleCAMAMCC = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3, 2))
apevModuleCAMIDT = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3, 3))
apevModuleHostProcessor = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4))
apevModuleHPUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 1))
apevModuleHP7451 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 2))
apevModuleHP7455 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 3))
apevModuleHP7457 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4))
apevModuleHPT2500 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 5))
apevModuleHPCeleron = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 6))
apevModuleHPT9400 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 7))
apevHP7457Unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 1))
apevHP7457DC8MB = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 2))
apevHP7457DC4MB = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 3))
apevHP7457AC8MB = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 4))
apevHP7457AC4MB = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 5))
apevHP7457ACDC8MB = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 6))
apevModulePMC = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 5))
apevModulePMCUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 5, 1))
apevModulePCMCIA = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6))
apevModulePCMCIAUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6, 1))
apevModulePCMCIAATA = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6, 2))
apevModulePCMCIALinear = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6, 3))
apevModuleMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7))
apevModuleMemoryUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7, 1))
apevModuleMemory1G = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7, 2))
apevModuleMemory4G = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7, 3))
apevModuleCard = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8))
apevModuleSPU = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 1))
apevModuleNPU = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 2))
apevModuleTCU = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 3))
apevModuleMIU = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 4))
apevModulePHY = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 5))
apevModuleTLS = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 6))
apevModuleMain = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 7))
apevModuleMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 8))
apevModuleFlex = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 9))
apevPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9))
apevPortUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 1))
apevPortGigE = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 2))
apevPortFE = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 3))
apevPort2Gig = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 4))
apevPortMMFiber = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 5))
apevPortSMFiber = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 6))
apevPort10GFiber = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 7))
apevStack = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 10))
mibBuilder.exportSymbols("ACMEPACKET-ENTITY-VENDORTYPE-OID-MIB", apevPowerSupply300W=apevPowerSupply300W, apevContainerSlotUnknown=apevContainerSlotUnknown, apevPortMMFiber=apevPortMMFiber, apevPowerSupply500W=apevPowerSupply500W, apevHP7457AC8MB=apevHP7457AC8MB, apevChassisUnknown=apevChassisUnknown, apevFan40x20=apevFan40x20, apevChassisSD1=apevChassisSD1, apevModuleMemory=apevModuleMemory, apevPowerSupply=apevPowerSupply, apevPort=apevPort, apevModulePHYCard=apevModulePHYCard, apevPHY2GigPortstMultiMode=apevPHY2GigPortstMultiMode, apevModulePCMCIAATA=apevModulePCMCIAATA, apevModuleUnknown=apevModuleUnknown, apevPowerSupply800W=apevPowerSupply800W, apevModuleHP7451=apevModuleHP7451, apevModulePMC=apevModulePMC, apevModuleCAMIDT=apevModuleCAMIDT, apevHP7457Unknown=apevHP7457Unknown, apevChassisSD2QoS=apevChassisSD2QoS, apevFan40x28=apevFan40x28, apevModuleTCU=apevModuleTCU, apevModulePCMCIALinear=apevModulePCMCIALinear, apevModuleHostProcessor=apevModuleHostProcessor, apevHP7457ACDC8MB=apevHP7457ACDC8MB, apevModuleTLS=apevModuleTLS, apevModule=apevModule, apevChassisSD4=apevChassisSD4, apevContainerDaughterCardTLS=apevContainerDaughterCardTLS, apevContainerSlot=apevContainerSlot, apevModuleCAMUnknown=apevModuleCAMUnknown, apevPHY4SFPPorts=apevPHY4SFPPorts, apevPHY8FEPorts=apevPHY8FEPorts, apevPHY4SFPPortsSecQosCav=apevPHY4SFPPortsSecQosCav, apevContainerSlotPCMCIA=apevContainerSlotPCMCIA, apevContainerDaughterCard=apevContainerDaughterCard, PYSNMP_MODULE_ID=acmepacketEntityVendortypeOIDMIB, apevModuleFlex=apevModuleFlex, apevUnknown=apevUnknown, apevModuleCAMAMCC=apevModuleCAMAMCC, apevSensorUnknown=apevSensorUnknown, apevMIBObjects=apevMIBObjects, apevHP7457DC4MB=apevHP7457DC4MB, apevSensorVoltage=apevSensorVoltage, apevContainerDaughterCardCAM=apevContainerDaughterCardCAM, apevModulePCMCIAUnknown=apevModulePCMCIAUnknown, apevPHY2GigPortsSingleMode=apevPHY2GigPortsSingleMode, apevPHYTranscodingCarrier=apevPHYTranscodingCarrier, apevChassis=apevChassis, apevOther=apevOther, apevChassisSR=apevChassisSR, apevStack=apevStack, apevContainerUnknown=apevContainerUnknown, apevModuleHP7455=apevModuleHP7455, apevModuleMemory4G=apevModuleMemory4G, apevChassisSD3=apevChassisSD3, apevPHY4SFPPortsSec=apevPHY4SFPPortsSec, apevContainerDaughterCardMemory=apevContainerDaughterCardMemory, apevPortSMFiber=apevPortSMFiber, apevPowerSupply60W=apevPowerSupply60W, apevPHY1GigPortMultiMode=apevPHY1GigPortMultiMode, apevChassisSD6=apevChassisSD6, apevModulePCMCIA=apevModulePCMCIA, apevContainerSlotPHY=apevContainerSlotPHY, apevModuleHPUnknown=apevModuleHPUnknown, apevSensor=apevSensor, apevModuleCard=apevModuleCard, apevPowerSupplyUnknown=apevPowerSupplyUnknown, apevPowerSupply1100W=apevPowerSupply1100W, apevHP7457DC8MB=apevHP7457DC8MB, apevChassisSD5=apevChassisSD5, apevContainerDaughterCardCPU=apevContainerDaughterCardCPU, apevFan40x56=apevFan40x56, apevModulePHY=apevModulePHY, apevHP7457AC4MB=apevHP7457AC4MB, apevPortGigE=apevPortGigE, apevContainerModules=apevContainerModules, apevChassisSD=apevChassisSD, apevPort2Gig=apevPort2Gig, apevChassisSD2=apevChassisSD2, apevSensorTemperature=apevSensorTemperature, apevSensorFanSpeed=apevSensorFanSpeed, apevPHYISR=apevPHYISR, apevPHY210GigPortsDataPlane=apevPHY210GigPortsDataPlane, apevContainerPowerTray=apevContainerPowerTray, apevPHY2FEPortsSec=apevPHY2FEPortsSec, apevContainer=apevContainer, apevModuleHPT9400=apevModuleHPT9400, apevModuleMgmt=apevModuleMgmt, apevFan40x10=apevFan40x10, apevModuleMain=apevModuleMain, apevModuleHPT2500=apevModuleHPT2500, apevPowerSupply150W=apevPowerSupply150W, apevContainerDaughterCardPMC=apevContainerDaughterCardPMC, apevPHYCardUnknown=apevPHYCardUnknown, apevPHY44SFPPortsSecQos=apevPHY44SFPPortsSecQos, apevModulePMCUnknown=apevModulePMCUnknown, apevChassisSDUnknown=apevChassisSDUnknown, apevModuleMemoryUnknown=apevModuleMemoryUnknown, apevFan=apevFan, apevContainerDaughterCardUnknown=apevContainerDaughterCardUnknown, apevModuleHP7457=apevModuleHP7457, apevPHY410GigSecPortsDataPlane=apevPHY410GigSecPortsDataPlane, apevPHY210GigSecPortsDataPlane=apevPHY210GigSecPortsDataPlane, apevPHY1GigPortSingleMode=apevPHY1GigPortSingleMode, apevModuleHPCeleron=apevModuleHPCeleron, apevModuleMIU=apevModuleMIU, apevPHY4FEPorts1089=apevPHY4FEPorts1089, acmepacketEntityVendortypeOIDMIB=acmepacketEntityVendortypeOIDMIB, apevModuleSPU=apevModuleSPU, apevPortUnknown=apevPortUnknown, apecPHY4FEPorts=apecPHY4FEPorts, apevFanUnknown=apevFanUnknown, apevModuleMemory1G=apevModuleMemory1G, apevPHY2GigPortsSec=apevPHY2GigPortsSec, apevPortFE=apevPortFE, apevModuleNPU=apevModuleNPU, apevModuleCAM=apevModuleCAM, apevContainerFanTray=apevContainerFanTray, apevPHY4GigPorts=apevPHY4GigPorts, apevPort10GFiber=apevPort10GFiber, apevPHY4SFPPortsQos=apevPHY4SFPPortsQos)
