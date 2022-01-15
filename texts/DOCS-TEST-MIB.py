#
# PySNMP MIB module DOCS-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DOCS-TEST-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, enterprises, ModuleIdentity, Unsigned32, NotificationType, MibIdentifier, iso, Integer32, Bits, Counter32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "ModuleIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "iso", "Integer32", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
cableLabs = MibIdentifier((1, 3, 6, 1, 4, 1, 4491))
clabFunction = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 1))
clabFuncMib2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 1, 1))
clabFuncProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 1, 2))
clabProject = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2))
clabProjDocsis = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1))
clabProjPacketCable = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2))
clabProjOpenCable = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 3))
clabProjCableHome = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4))
docsTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12))
if mibBuilder.loadTexts: docsTestMIB.setLastUpdated('0203150000Z')
if mibBuilder.loadTexts: docsTestMIB.setOrganization('DOCSIS 2.0 ATP Working Group')
if mibBuilder.loadTexts: docsTestMIB.setContactInfo('        David Raftus\n               Postal: Terayon Canada Ltd\n                       340 Terry Fox Drive, Suite 202\n                       Ottawa Ontario\n                       Canada\n               Phone:  +1 613 592 1052\n               E-mail: david.raftus@terayon.com\n\n               DOCSIS 2.0 ATP Working Group\n               General Discussion: docsis-20@cablelabs.com,\n               docsis-20-atp@cablelabs.com')
if mibBuilder.loadTexts: docsTestMIB.setDescription('This is the MIB Module supporting programmable test features\n               for DOCSIS 2.0 compliant Cable Modems (CM) and Cable Modem\n               Termination Systems (CMTS).')
docsTestMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1))
docsTestBaseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1))
docsTestSetupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2))
docsTestCapability = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsTestCapability.setStatus('current')
if mibBuilder.loadTexts: docsTestCapability.setDescription('Indicates the ability of this device to support the\n             programmable features identified by the TYPE field from\n             the CM/CMTS TLV table in [17].\n             Each octet within this octet string represents eight tests.\n             For example, the first octet represents tests one through eight\n             (with the msb representing test one) as identified by the TYPE\n             field.')
docsTestStatus = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsTestStatus.setStatus('current')
if mibBuilder.loadTexts: docsTestStatus.setDescription('Indicates the current operating status of tests initiated\n             through the docsTestSetupObjects. The octet representation is\n             identical to that used by docsTestCapability. A bit representation\n             of one indicates that a test is currently active, while zero\n             indicates the test is inactive or has completed.')
docsTestType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsTestType.setStatus('current')
if mibBuilder.loadTexts: docsTestType.setDescription('Corresponds to the TYPE field from the CM/CMTS TLV Table\n             in [17]. The default value of zero indicates\n             no test has yet been initiated.\n             A WrongValueError should be returned in response to a write\n             request for a test not supported by the device. A read request\n             will return the docsTestType value last successfully written,\n             whether that test is active or inactive.')
docsTestData = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsTestData.setStatus('current')
if mibBuilder.loadTexts: docsTestData.setDescription('The OCTET STRING length and value correspond to the\n             LENGTH and VALUE fields from the CM/CMTS TLV\n             Table in [17]. A read request will return the\n             docsTestData value last successfully written, whether that test\n             is active or inactive.')
docsTestEnable = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsTestEnable.setStatus('current')
if mibBuilder.loadTexts: docsTestEnable.setDescription('Used to initiate or stop the tests setup through the docsTestType\n             and docsTestData objects.\n             A CommitFailedError should be returned in response to a TRUE\n             Write request if the values in docsTestType and docsTestData are\n             incompatible, or a test could not be initiated for any other\n             reason.')
docsTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2))
docsTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 1))
docsTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 2))
docsTestBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 1, 1)).setObjects(("DOCS-TEST-MIB", "docsTestGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsTestBasicCompliance = docsTestBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: docsTestBasicCompliance.setDescription('The compliance statement for devices that implement\n             the DOCSIS compliant programmable test features.')
docsTestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 2, 1)).setObjects(("DOCS-TEST-MIB", "docsTestCapability"), ("DOCS-TEST-MIB", "docsTestStatus"), ("DOCS-TEST-MIB", "docsTestType"), ("DOCS-TEST-MIB", "docsTestData"), ("DOCS-TEST-MIB", "docsTestEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsTestGroup = docsTestGroup.setStatus('current')
if mibBuilder.loadTexts: docsTestGroup.setDescription('Group of objects implemented in both Cable Modems and\n             Cable Modem Termination Systems.')
mibBuilder.exportSymbols("DOCS-TEST-MIB", docsTestConformance=docsTestConformance, docsTestGroups=docsTestGroups, docsTestBasicCompliance=docsTestBasicCompliance, docsTestGroup=docsTestGroup, docsTestEnable=docsTestEnable, clabProjCableHome=clabProjCableHome, clabFuncMib2=clabFuncMib2, docsTestStatus=docsTestStatus, docsTestMIB=docsTestMIB, clabFunction=clabFunction, docsTestMibObjects=docsTestMibObjects, clabProject=clabProject, clabFuncProprietary=clabFuncProprietary, docsTestData=docsTestData, docsTestCapability=docsTestCapability, docsTestType=docsTestType, PYSNMP_MODULE_ID=docsTestMIB, clabProjPacketCable=clabProjPacketCable, cableLabs=cableLabs, docsTestCompliances=docsTestCompliances, clabProjOpenCable=clabProjOpenCable, clabProjDocsis=clabProjDocsis, docsTestBaseObjects=docsTestBaseObjects, docsTestSetupObjects=docsTestSetupObjects)
