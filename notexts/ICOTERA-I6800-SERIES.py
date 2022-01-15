#
# PySNMP MIB module ICOTERA-I6800-SERIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/icotera/ICOTERA-I6800-SERIES-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:24:53 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, iso, NotificationType, Unsigned32, Counter32, Gauge32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, ObjectIdentity, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "iso", "NotificationType", "Unsigned32", "Counter32", "Gauge32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "ObjectIdentity", "Bits", "ModuleIdentity")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
icotera = ModuleIdentity((1, 3, 6, 1, 4, 1, 29865))
icotera.setRevisions(('2016-03-11 13:07', '2015-08-26 12:40', '2015-08-26 08:15', '2015-08-21 10:12', '2015-08-10 14:33', '2015-06-22 14:49', '2015-03-12 12:27',))
if mibBuilder.loadTexts: icotera.setLastUpdated('201603111307Z')
if mibBuilder.loadTexts: icotera.setOrganization('Icotera A/S')
ictIGW4k = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12))
if mibBuilder.loadTexts: ictIGW4k.setStatus('current')
ictMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 2))
ictServices = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 3))
ictDuplex = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 4))
ictReset = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 5))
ictDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 6))
ictCatv = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1))
if mibBuilder.loadTexts: ictCatv.setStatus('current')
ictCatvMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1))
if mibBuilder.loadTexts: ictCatvMib.setStatus('current')
catvModuleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleAdminStatus.setStatus('current')
catvModuleFilter = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("pkg1", 1), ("pkg2", 2), ("pkg3", 3), ("pkg4", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleFilter.setStatus('current')
catvModuleRflevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("auto", 0), ("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleRflevel.setStatus('current')
catvModuleLowSignal = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleLowSignal.setStatus('current')
catvModuleSignalDetected = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleSignalDetected.setStatus('current')
catvModulePowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModulePowerLevel.setStatus('current')
catvModuleRfOutputLevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleRfOutputLevel.setStatus('current')
catvModuleOmi = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleOmi.setStatus('current')
ictVoip = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2))
if mibBuilder.loadTexts: ictVoip.setStatus('current')
ictVoipMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1))
if mibBuilder.loadTexts: ictVoipMib.setStatus('current')
voipFXSport1 = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipFXSport1.setStatus('current')
voipFXSport2 = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipFXSport2.setStatus('current')
ictFacRst = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 5, 1))
if mibBuilder.loadTexts: ictFacRst.setStatus('current')
ictFacRstMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 5, 1, 1))
if mibBuilder.loadTexts: ictFacRstMib.setStatus('current')
performFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("noActionRequested", 0), ("makeFactoryreset", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: performFactoryReset.setStatus('current')
ictMgmtMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1))
if mibBuilder.loadTexts: ictMgmtMib.setStatus('current')
ictFwUpg = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1))
if mibBuilder.loadTexts: ictFwUpg.setStatus('current')
ictCfgUpdate = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2))
if mibBuilder.loadTexts: ictCfgUpdate.setStatus('current')
ictReboot = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 3))
if mibBuilder.loadTexts: ictReboot.setStatus('current')
upgUrl = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upgUrl.setStatus('current')
upgExecute = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notUpgrading", 0), ("startUpgrade", 1), ("validatingUpgrade-CheckErrorCodeIfFailed", 2), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upgExecute.setStatus('current')
upgStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upgStatus.setStatus('current')
cfgTftpPath = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgTftpPath.setStatus('current')
cfgExecute = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("notUpdating", 0), ("startUpdate", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgExecute.setStatus('current')
cfgStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgStatus.setStatus('current')
performCpeReboot = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("noActionRequested", 0), ("makeReboot", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: performCpeReboot.setStatus('current')
ictDHCPsrv = MibTable((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1), )
if mibBuilder.loadTexts: ictDHCPsrv.setStatus('current')
ictDHCPsrvLeases = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1), ).setIndexNames((0, "ICOTERA-I6800-SERIES", "ictDHCPsrvIndex"))
if mibBuilder.loadTexts: ictDHCPsrvLeases.setStatus('current')
ictDHCPsrvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictDHCPsrvIndex.setStatus('current')
ictMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictMacAddress.setStatus('current')
ictExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictExpire.setStatus('current')
ictIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictIPaddress.setStatus('current')
ictHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictHostName.setStatus('current')
ictDuplexMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15))
if mibBuilder.loadTexts: ictDuplexMib.setStatus('current')
duplexConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1))
ifDuplexTable = MibTable((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1), )
if mibBuilder.loadTexts: ifDuplexTable.setStatus('current')
ifDuplexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ifDuplexEntry.setStatus('current')
ifDuplexIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexIndex.setStatus('current')
ifDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("halfDuplex", 2), ("fullDuplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexStatus.setStatus('current')
mibBuilder.exportSymbols("ICOTERA-I6800-SERIES", catvModulePowerLevel=catvModulePowerLevel, ictVoip=ictVoip, ictDHCPsrv=ictDHCPsrv, ictServices=ictServices, voipFXSport1=voipFXSport1, ictCfgUpdate=ictCfgUpdate, ictReboot=ictReboot, catvModuleSignalDetected=catvModuleSignalDetected, ictDuplex=ictDuplex, catvModuleOmi=catvModuleOmi, ictFacRstMib=ictFacRstMib, ictMgmtMib=ictMgmtMib, upgStatus=upgStatus, ictDuplexMib=ictDuplexMib, catvModuleFilter=catvModuleFilter, duplexConfig=duplexConfig, ifDuplexIndex=ifDuplexIndex, ifDuplexEntry=ifDuplexEntry, ictIGW4k=ictIGW4k, ictFacRst=ictFacRst, ictDHCPsrvIndex=ictDHCPsrvIndex, ictReset=ictReset, cfgTftpPath=cfgTftpPath, catvModuleAdminStatus=catvModuleAdminStatus, icotera=icotera, ifDuplexTable=ifDuplexTable, ictMgmt=ictMgmt, ictFwUpg=ictFwUpg, ictDhcp=ictDhcp, ictMacAddress=ictMacAddress, ictVoipMib=ictVoipMib, cfgStatus=cfgStatus, ictCatv=ictCatv, cfgExecute=cfgExecute, ictHostName=ictHostName, PYSNMP_MODULE_ID=icotera, upgExecute=upgExecute, performCpeReboot=performCpeReboot, voipFXSport2=voipFXSport2, ictDHCPsrvLeases=ictDHCPsrvLeases, upgUrl=upgUrl, ictIPaddress=ictIPaddress, ifDuplexStatus=ifDuplexStatus, ictExpire=ictExpire, performFactoryReset=performFactoryReset, catvModuleRflevel=catvModuleRflevel, ictCatvMib=ictCatvMib, catvModuleLowSignal=catvModuleLowSignal, catvModuleRfOutputLevel=catvModuleRfOutputLevel)
