#
# PySNMP MIB module EATON-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eaton/EATON-OIDS
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:08 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, enterprises, TimeTicks, IpAddress, Counter32, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "enterprises", "TimeTicks", "IpAddress", "Counter32", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eaton = ModuleIdentity((1, 3, 6, 1, 4, 1, 534))
eaton.setRevisions(('2018-11-13 00:00', '2014-02-19 00:00', '2010-01-24 00:00', '2009-06-18 00:00', '2007-08-06 00:00', '2007-07-05 00:00', '2006-10-15 00:00', '2006-05-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eaton.setRevisionsDescriptions(('Added assignments for eatonSensor MIB.', 'Added assignments for stsMIB.', 'Added assignments for eatonEpdu and eatonEpduMa.', 'Added assignments for powerCmnd and OSDCIIMIB.', 'Added assignments for pcdMIB and pxmMIB.\n             Added common Textual Conventions for Integers.', 'Added assignment for eatonEpduMIB.\n             Cleaned up file for public consumption.', 'Added assignments for powerChain and pxgMIB.', 'Revised from the original assignments in XUPS-MIB.txt.\n             Note that enterprises.534. was originally assigned to Exide \n             Electronics before Powerware was acquired by Eaton.',))
if mibBuilder.loadTexts: eaton.setLastUpdated('201811130000Z')
if mibBuilder.loadTexts: eaton.setOrganization('Eaton Corporation')
if mibBuilder.loadTexts: eaton.setContactInfo('Eaton Power Quality Technical Support (PQTS) group\n            www.eaton.com/powerxpert \n            Technical Resource Center phone numbers \n            United States:  1.800.843.9433 or 919.870.3028\n            Canada:  1.800.461.9166 ext. 260\n            All other countries:  Call your local service representative.')
if mibBuilder.loadTexts: eaton.setDescription("Assigns major branches from the root of \n             Eaton's OID tree (534).\n\n            Copyright (C) Exide Electronics 1992-98\n            Copyright (C) Powerware Corporation 1999-2004\n            Copyright (C) Eaton Corporation (2005-).")
xupsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1))
xupsEnvironment = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1, 6))
xupsObjectId = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2))
powerwareEthernetSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 1))
powerwareNetworkSnmpAdapterEther = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 2))
powerwareNetworkSnmpAdapterToken = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 3))
onlinetDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 4))
connectUPSAdapterEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 5))
powerwareNetworkDigitalIOEther = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 6))
connectUPSAdapterTokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 7))
simpleSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 8))
powerwareEliSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 9))
powerwareBasicEmbeddedEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 10))
eatonPowerChainGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 11))
eatonPowerChainDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 12))
eatonPowerXpertMeter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 13))
xupsIoMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 3))
powerVision = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 4))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6))
pduAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6))
hdpdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 2))
eatonPdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4))
sensorAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 8))
dataCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 7))
environmentalMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 7, 1))
itProjects = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 7))
pki = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 7, 1))
powerChain = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 8))
powerCmnd = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 9))
sts = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10))
class PositiveInteger(TextualConvention, Integer32):
    description = 'This data type is a non-zero and non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    description = 'This data type is a non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("EATON-OIDS", xupsMIB=xupsMIB, powerwareEliSnmpAdapter=powerwareEliSnmpAdapter, environmentalMonitor=environmentalMonitor, powerVision=powerVision, xupsObjectId=xupsObjectId, onlinetDaemon=onlinetDaemon, eatonPowerXpertMeter=eatonPowerXpertMeter, products=products, xupsIoMIB=xupsIoMIB, dataCenter=dataCenter, NonNegativeInteger=NonNegativeInteger, PYSNMP_MODULE_ID=eaton, eatonPowerChainDevice=eatonPowerChainDevice, itProjects=itProjects, PositiveInteger=PositiveInteger, powerwareNetworkSnmpAdapterEther=powerwareNetworkSnmpAdapterEther, eaton=eaton, powerwareNetworkDigitalIOEther=powerwareNetworkDigitalIOEther, pduAgent=pduAgent, sensorAgent=sensorAgent, powerwareEthernetSnmpAdapter=powerwareEthernetSnmpAdapter, connectUPSAdapterTokenRing=connectUPSAdapterTokenRing, powerwareBasicEmbeddedEthernet=powerwareBasicEmbeddedEthernet, hdpdu=hdpdu, sts=sts, simpleSnmpAdapter=simpleSnmpAdapter, connectUPSAdapterEthernet=connectUPSAdapterEthernet, pki=pki, xupsEnvironment=xupsEnvironment, powerCmnd=powerCmnd, eatonPowerChainGateway=eatonPowerChainGateway, powerwareNetworkSnmpAdapterToken=powerwareNetworkSnmpAdapterToken, eatonPdu=eatonPdu, powerChain=powerChain)
