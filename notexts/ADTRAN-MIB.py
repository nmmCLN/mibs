#
# PySNMP MIB module ADTRAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:13 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, IpAddress, TimeTicks, iso, ObjectIdentity, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, enterprises, Unsigned32, ModuleIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "TimeTicks", "iso", "ObjectIdentity", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "enterprises", "Unsigned32", "ModuleIdentity", "NotificationType", "Counter64")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
adtran = ModuleIdentity((1, 3, 6, 1, 4, 1, 664))
if mibBuilder.loadTexts: adtran.setLastUpdated('0208090000Z')
if mibBuilder.loadTexts: adtran.setOrganization('ADTRAN, Inc.')
adProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 1))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 3))
adPerform = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 4))
adShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5))
adIdentity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6))
adIdentityShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000))
adAgentCapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 7))
adAgentCapProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 7, 1))
adAgentCapShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 7, 2))
adConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99))
adComplianceShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 10000))
adProductInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 3, 1))
adProdName = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdName.setStatus('current')
adProdPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdPartNumber.setStatus('current')
adProdCLEIcode = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdCLEIcode.setStatus('current')
adProdSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdSerialNumber.setStatus('current')
adProdRevision = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdRevision.setStatus('current')
adProdSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdSwVersion.setStatus('current')
adProdPhysAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdPhysAddress.setStatus('current')
adProdProductID = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 8), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdProductID.setStatus('current')
adProdTransType = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdTransType.setStatus('current')
adCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 1))
adMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 2))
adCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 99, 1, 1)).setObjects(("ADTRAN-MIB", "adBaseGroup"), ("ADTRAN-MIB", "adCNDGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adCompliance = adCompliance.setStatus('current')
adBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 99, 2, 1)).setObjects(("ADTRAN-MIB", "adProdName"), ("ADTRAN-MIB", "adProdPartNumber"), ("ADTRAN-MIB", "adProdCLEIcode"), ("ADTRAN-MIB", "adProdSerialNumber"), ("ADTRAN-MIB", "adProdRevision"), ("ADTRAN-MIB", "adProdSwVersion"), ("ADTRAN-MIB", "adProdPhysAddress"), ("ADTRAN-MIB", "adProdProductID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adBaseGroup = adBaseGroup.setStatus('current')
adCNDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 99, 2, 2)).setObjects(("ADTRAN-MIB", "adProdTransType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adCNDGroup = adCNDGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MIB", adtran=adtran, adMIBGroups=adMIBGroups, adProdTransType=adProdTransType, adCompliance=adCompliance, adMgmt=adMgmt, adShared=adShared, adComplianceShared=adComplianceShared, adProductInfo=adProductInfo, adProdProductID=adProdProductID, PYSNMP_MODULE_ID=adtran, adAdmin=adAdmin, adConformance=adConformance, adAgentCapModule=adAgentCapModule, adIdentityShared=adIdentityShared, adProdSwVersion=adProdSwVersion, adCompliances=adCompliances, adCNDGroup=adCNDGroup, adProdName=adProdName, adProdSerialNumber=adProdSerialNumber, adProdPartNumber=adProdPartNumber, adAgentCapProduct=adAgentCapProduct, adIdentity=adIdentity, adProdRevision=adProdRevision, adAgentCapShared=adAgentCapShared, adProdPhysAddress=adProdPhysAddress, adPerform=adPerform, adBaseGroup=adBaseGroup, adProducts=adProducts, adProdCLEIcode=adProdCLEIcode)
