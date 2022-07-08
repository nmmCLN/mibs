#
# PySNMP MIB module ICOTERA-I6800-SERIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/icotera/ICOTERA-I6800-SERIES-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:22:25 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, NotificationType, Unsigned32, MibIdentifier, Integer32, iso, Counter64, enterprises, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "NotificationType", "Unsigned32", "MibIdentifier", "Integer32", "iso", "Counter64", "enterprises", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
icotera = ModuleIdentity((1, 3, 6, 1, 4, 1, 29865))
icotera.setRevisions(('2016-03-11 13:07', '2015-08-26 12:40', '2015-08-26 08:15', '2015-08-21 10:12', '2015-08-10 14:33', '2015-06-22 14:49', '2015-03-12 12:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: icotera.setRevisionsDescriptions(('Additional parameters were added to CATV module. OMI and RFlevelOutput.\n\t Parameters are supported by special CATV solution. No data will be provided if CPE is not compatible.', 'Rebuilding file, adding missing objects. ', 'Small correction in the file done. Improved MacAddress presentation.', 'Additional parameters were added to check VOIP service.', 'DHCPd leases are now supported and presented, \n\tictDuplex MIB added ', 'Additional parameters were added to CATV module.', 'Created from ICOTERA-MIB.mib',))
if mibBuilder.loadTexts: icotera.setLastUpdated('201603111307Z')
if mibBuilder.loadTexts: icotera.setOrganization('Icotera A/S')
if mibBuilder.loadTexts: icotera.setContactInfo('Icotera A/S\n     Customer Support\n\n     Mail : Kongevejen 400D\n            2840 Holte\n            Danmark\n\n     Tel  : +45 7010 0033\n\n     E-mail: support@icotera.com\n     Web   : http://icotera.com')
if mibBuilder.loadTexts: icotera.setDescription('The Icotera management information base SMI definitions')
ictIGW4k = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12))
if mibBuilder.loadTexts: ictIGW4k.setStatus('current')
if mibBuilder.loadTexts: ictIGW4k.setDescription('Device related SNMP options')
ictMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 2))
ictServices = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 3))
ictDuplex = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 4))
ictReset = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 5))
ictDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 6))
ictCatv = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1))
if mibBuilder.loadTexts: ictCatv.setStatus('current')
if mibBuilder.loadTexts: ictCatv.setDescription('The MIB module for managing Icotera services')
ictCatvMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1))
if mibBuilder.loadTexts: ictCatvMib.setStatus('current')
if mibBuilder.loadTexts: ictCatvMib.setDescription('The MIB module for managing Icotera services')
catvModuleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleAdminStatus.setStatus('current')
if mibBuilder.loadTexts: catvModuleAdminStatus.setDescription('The administrative status of the module, this can be enabled(1) or\n    disabled(0).')
catvModuleFilter = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("pkg1", 1), ("pkg2", 2), ("pkg3", 3), ("pkg4", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleFilter.setStatus('current')
if mibBuilder.loadTexts: catvModuleFilter.setDescription('Package filter selected for catv module')
catvModuleRflevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("auto", 0), ("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleRflevel.setStatus('current')
if mibBuilder.loadTexts: catvModuleRflevel.setDescription('RF signal amplification on CATV output')
catvModuleLowSignal = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleLowSignal.setStatus('current')
if mibBuilder.loadTexts: catvModuleLowSignal.setDescription('Low signal level of catv led')
catvModuleSignalDetected = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleSignalDetected.setStatus('current')
if mibBuilder.loadTexts: catvModuleSignalDetected.setDescription('Tells whether CATV signal is detected: yes(1) - detected, no(0) - not detected.')
catvModulePowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModulePowerLevel.setStatus('current')
if mibBuilder.loadTexts: catvModulePowerLevel.setDescription('Current CATV power level. It can have one of the following values:\n     - any integer between -1299 and 199 when the power level is higher than -13.00 and lower than 2.00,\n       which is the power level in dBm multiplied by 100.\n     - a value of -2147483648 when the power level is lower than -13 dBm\n     - a value of 2147483647 when the power level is higher than 2 dBm.')
catvModuleRfOutputLevel = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleRfOutputLevel.setStatus('current')
if mibBuilder.loadTexts: catvModuleRfOutputLevel.setDescription('Parameter is supported by special CATV solution. No data will be provided if CPE is not compatible.\n     Calculated RF output value which should be expected.\n     - Expected value is presented in dBuV multiplied by 100.\n     - if value of 0 is received, either CATV fiber is not connected or CATV is turned off.')
catvModuleOmi = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catvModuleOmi.setStatus('current')
if mibBuilder.loadTexts: catvModuleOmi.setDescription('Parameter is supported by special CATV solution. No data will be provided if CPE is not compatible.\n     Currently OMI value set at CPE.')
ictVoip = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2))
if mibBuilder.loadTexts: ictVoip.setStatus('current')
if mibBuilder.loadTexts: ictVoip.setDescription('The MIB module for checking VoIP service')
ictVoipMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1))
if mibBuilder.loadTexts: ictVoipMib.setStatus('current')
if mibBuilder.loadTexts: ictVoipMib.setDescription('The MIB module for checking VoIP service status')
voipFXSport1 = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipFXSport1.setStatus('current')
if mibBuilder.loadTexts: voipFXSport1.setDescription('The administrative status of the FXS port 1')
voipFXSport2 = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipFXSport2.setStatus('current')
if mibBuilder.loadTexts: voipFXSport2.setDescription('The administrative status of the FXS port 2')
ictFacRst = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 5, 1))
if mibBuilder.loadTexts: ictFacRst.setStatus('current')
if mibBuilder.loadTexts: ictFacRst.setDescription('The MIB parent for CPE reset')
ictFacRstMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 5, 1, 1))
if mibBuilder.loadTexts: ictFacRstMib.setStatus('current')
if mibBuilder.loadTexts: ictFacRstMib.setDescription('The MIB which makes Factory Reset of CPE')
performFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("noActionRequested", 0), ("makeFactoryreset", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: performFactoryReset.setStatus('current')
if mibBuilder.loadTexts: performFactoryReset.setDescription('Status of FactoryReset feature.')
ictMgmtMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1))
if mibBuilder.loadTexts: ictMgmtMib.setStatus('current')
if mibBuilder.loadTexts: ictMgmtMib.setDescription('The MIB which allows managing the CPE')
ictFwUpg = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1))
if mibBuilder.loadTexts: ictFwUpg.setStatus('current')
if mibBuilder.loadTexts: ictFwUpg.setDescription('The MIB of firmware upgrade')
ictCfgUpdate = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2))
if mibBuilder.loadTexts: ictCfgUpdate.setStatus('current')
if mibBuilder.loadTexts: ictCfgUpdate.setDescription('The MIB of configuration update')
ictReboot = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 3))
if mibBuilder.loadTexts: ictReboot.setStatus('current')
if mibBuilder.loadTexts: ictReboot.setDescription('The MIB responsible for CPE reboot')
upgUrl = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upgUrl.setStatus('current')
if mibBuilder.loadTexts: upgUrl.setDescription('Path to file with firmware.')
upgExecute = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notUpgrading", 0), ("startUpgrade", 1), ("validatingUpgrade-CheckErrorCodeIfFailed", 2), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upgExecute.setStatus('current')
if mibBuilder.loadTexts: upgExecute.setDescription('MIB responsible for trigerring firmware upgrade.')
upgStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upgStatus.setStatus('current')
if mibBuilder.loadTexts: upgStatus.setDescription('MIB show upgrade status.')
cfgTftpPath = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgTftpPath.setStatus('current')
if mibBuilder.loadTexts: cfgTftpPath.setDescription('Path to cofiguration file stored at TFTP server.')
cfgExecute = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("notUpdating", 0), ("startUpdate", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgExecute.setStatus('current')
if mibBuilder.loadTexts: cfgExecute.setDescription('MIB responsible for trigerring config upload at CPE.')
cfgStatus = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgStatus.setStatus('current')
if mibBuilder.loadTexts: cfgStatus.setDescription('MIB show configuration upgrade status.')
performCpeReboot = MibScalar((1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("noActionRequested", 0), ("makeReboot", 1), ("someErrorOccured", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: performCpeReboot.setStatus('current')
if mibBuilder.loadTexts: performCpeReboot.setDescription('MIB responsible for trigerring CPE reboot.')
ictDHCPsrv = MibTable((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1), )
if mibBuilder.loadTexts: ictDHCPsrv.setStatus('current')
if mibBuilder.loadTexts: ictDHCPsrv.setDescription('Table of DHCPd leases.')
ictDHCPsrvLeases = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1), ).setIndexNames((0, "ICOTERA-I6800-SERIES", "ictDHCPsrvIndex"))
if mibBuilder.loadTexts: ictDHCPsrvLeases.setStatus('current')
if mibBuilder.loadTexts: ictDHCPsrvLeases.setDescription('An entry in the table, \n\t\t\tcontaining information\n\t\t\tabout lease.')
ictDHCPsrvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictDHCPsrvIndex.setStatus('current')
if mibBuilder.loadTexts: ictDHCPsrvIndex.setDescription('A unique value for LEASE index.')
ictMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictMacAddress.setStatus('current')
if mibBuilder.loadTexts: ictMacAddress.setDescription('MAC address of Lease.')
ictExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictExpire.setStatus('current')
if mibBuilder.loadTexts: ictExpire.setDescription('Lease time until Expire')
ictIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictIPaddress.setStatus('current')
if mibBuilder.loadTexts: ictIPaddress.setDescription('IP address learned from host.')
ictHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ictHostName.setStatus('current')
if mibBuilder.loadTexts: ictHostName.setDescription('Hostname.')
ictDuplexMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15))
if mibBuilder.loadTexts: ictDuplexMib.setStatus('current')
if mibBuilder.loadTexts: ictDuplexMib.setDescription('Initial release.')
duplexConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1))
ifDuplexTable = MibTable((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1), )
if mibBuilder.loadTexts: ifDuplexTable.setStatus('current')
if mibBuilder.loadTexts: ifDuplexTable.setDescription('A table containing interface duplex status.')
ifDuplexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ifDuplexEntry.setStatus('current')
if mibBuilder.loadTexts: ifDuplexEntry.setDescription('Status for a specific interface using ethernet-like medium.')
ifDuplexIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexIndex.setReference('RFC 2863, ifIndex')
if mibBuilder.loadTexts: ifDuplexIndex.setStatus('current')
if mibBuilder.loadTexts: ifDuplexIndex.setDescription('An index value that uniquely identifies an\n              interface to an ethernet-like medium.  The\n              interface identified by a particular value of\n              this index is the same interface as identified\n              by the same value of ifIndex.')
ifDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("halfDuplex", 2), ("fullDuplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexStatus.setStatus('current')
if mibBuilder.loadTexts: ifDuplexStatus.setDescription("The current duplex mode of operation of the interface. 'unknown'\n               indicates that the current duplex mode could not be determined.")
mibBuilder.exportSymbols("ICOTERA-I6800-SERIES", ifDuplexEntry=ifDuplexEntry, voipFXSport1=voipFXSport1, catvModuleFilter=catvModuleFilter, catvModuleAdminStatus=catvModuleAdminStatus, ictFacRst=ictFacRst, ictHostName=ictHostName, catvModuleSignalDetected=catvModuleSignalDetected, ictCatvMib=ictCatvMib, ictMgmtMib=ictMgmtMib, cfgExecute=cfgExecute, ifDuplexIndex=ifDuplexIndex, cfgTftpPath=cfgTftpPath, performCpeReboot=performCpeReboot, performFactoryReset=performFactoryReset, duplexConfig=duplexConfig, upgExecute=upgExecute, ictDuplexMib=ictDuplexMib, voipFXSport2=voipFXSport2, ictCfgUpdate=ictCfgUpdate, ifDuplexTable=ifDuplexTable, cfgStatus=cfgStatus, ictIPaddress=ictIPaddress, catvModuleLowSignal=catvModuleLowSignal, ictVoipMib=ictVoipMib, ictServices=ictServices, ictMgmt=ictMgmt, catvModulePowerLevel=catvModulePowerLevel, upgStatus=upgStatus, ictDHCPsrvLeases=ictDHCPsrvLeases, ictFwUpg=ictFwUpg, catvModuleRflevel=catvModuleRflevel, ifDuplexStatus=ifDuplexStatus, ictExpire=ictExpire, ictVoip=ictVoip, ictReset=ictReset, ictCatv=ictCatv, catvModuleRfOutputLevel=catvModuleRfOutputLevel, ictIGW4k=ictIGW4k, catvModuleOmi=catvModuleOmi, ictDuplex=ictDuplex, ictFacRstMib=ictFacRstMib, ictDHCPsrv=ictDHCPsrv, ictReboot=ictReboot, PYSNMP_MODULE_ID=icotera, ictDHCPsrvIndex=ictDHCPsrvIndex, ictDhcp=ictDhcp, upgUrl=upgUrl, ictMacAddress=ictMacAddress, icotera=icotera)
