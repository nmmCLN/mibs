#
# PySNMP MIB module SIAE-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-USER-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:16 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, TimeTicks, Counter32, Unsigned32, ModuleIdentity, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "iso")
RowStatus, StorageType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "DisplayString")
accessControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 5))
accessControl.setRevisions(('2016-09-17 00:00', '2014-04-08 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: accessControl.setLastUpdated('201609170000Z')
if mibBuilder.loadTexts: accessControl.setOrganization('SIAE MICROELETTRONICA spa')
accessControlMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlMibVersion.setStatus('current')
accessControlGroupTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2), )
if mibBuilder.loadTexts: accessControlGroupTable.setStatus('current')
accessControlGroupRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlGroupName"))
if mibBuilder.loadTexts: accessControlGroupRecord.setStatus('current')
accessControlGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupName.setStatus('current')
accessControlGroupProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("admin", 1), ("readwrite", 2), ("maintenance", 3), ("readonly", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupProfile.setStatus('current')
accessControlGroupHttp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupHttp.setStatus('current')
accessControlGroupHttps = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupHttps.setStatus('current')
accessControlGroupSnmp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("deny", 1), ("allowV1", 2), ("allowV2c", 3), ("allowV3", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupSnmp.setStatus('current')
accessControlGroupFtp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupFtp.setStatus('current')
accessControlGroupSftp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupSftp.setStatus('current')
accessControlGroupSsh = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupSsh.setStatus('current')
accessControlGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupRowStatus.setStatus('current')
accessControlGroupCli = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlGroupCli.setStatus('current')
accessControlUserTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3), )
if mibBuilder.loadTexts: accessControlUserTable.setStatus('current')
accessControlUserRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlUserName"))
if mibBuilder.loadTexts: accessControlUserRecord.setStatus('current')
accessControlUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserName.setStatus('current')
accessControlUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserGroupName.setStatus('current')
accessControlUserPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserPwd.setStatus('current')
accessControlUserSnmpAuthProt = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuth", 1), ("md5", 2), ("sha", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpAuthProt.setStatus('current')
accessControlUserSnmpAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpAuthKey.setStatus('current')
accessControlUserSnmpPrivProt = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noPriv", 1), ("des", 2), ("aes", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpPrivProt.setStatus('current')
accessControlUserSnmpPrivKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpPrivKey.setStatus('current')
accessControlUserTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(300)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserTimeout.setStatus('current')
accessControlUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserRowStatus.setStatus('current')
accessControlLoginTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4), )
if mibBuilder.loadTexts: accessControlLoginTable.setStatus('current')
accessControlLoginRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlLoginIpAddress"), (0, "SIAE-USER-MIB", "accessControlLoginUserName"), (0, "SIAE-USER-MIB", "accessControlLoginType"))
if mibBuilder.loadTexts: accessControlLoginRecord.setStatus('current')
accessControlLoginUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginUserName.setStatus('current')
accessControlLoginIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginIpAddress.setStatus('current')
accessControlLoginRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("logout", 2), ("forcelogout", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessControlLoginRequest.setStatus('current')
accessControlLoginTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessControlLoginTrapEnable.setStatus('current')
accessControlLoginType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("web", 1), ("snmp", 2), ("cli", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginType.setStatus('current')
accessControlLoginPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessControlLoginPwd.setStatus('current')
accessControlLoginPolling = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("polling", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginPolling.setStatus('current')
accessControlClientTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5), )
if mibBuilder.loadTexts: accessControlClientTable.setStatus('current')
accessControlClientRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlClientService"))
if mibBuilder.loadTexts: accessControlClientRecord.setStatus('current')
accessControlClientService = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ftp", 1), ("sftp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientService.setStatus('current')
accessControlClientServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientServiceStatus.setStatus('current')
accessControlClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientName.setStatus('current')
accessControlClientPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientPwd.setStatus('current')
accessControlClientStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientStorageType.setStatus('current')
accessControlClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientRowStatus.setStatus('current')
accessControlExtLoginTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6), )
if mibBuilder.loadTexts: accessControlExtLoginTable.setStatus('current')
accessControlExtLoginRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1), )
accessControlLoginRecord.registerAugmentions(("SIAE-USER-MIB", "accessControlExtLoginRecord"))
accessControlExtLoginRecord.setIndexNames(*accessControlLoginRecord.getIndexNames())
if mibBuilder.loadTexts: accessControlExtLoginRecord.setStatus('current')
accessControlExtLoginProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("admin", 1), ("readwrite", 2), ("maintenance", 3), ("readonly", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlExtLoginProfile.setStatus('current')
accessControlExtLoginAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlExtLoginAuthMode.setStatus('current')
mibBuilder.exportSymbols("SIAE-USER-MIB", accessControlLoginTable=accessControlLoginTable, accessControlUserPwd=accessControlUserPwd, accessControlClientRecord=accessControlClientRecord, accessControlGroupTable=accessControlGroupTable, accessControlGroupHttp=accessControlGroupHttp, accessControlClientService=accessControlClientService, accessControlClientServiceStatus=accessControlClientServiceStatus, accessControlGroupRecord=accessControlGroupRecord, accessControlExtLoginProfile=accessControlExtLoginProfile, accessControlUserTimeout=accessControlUserTimeout, accessControlGroupFtp=accessControlGroupFtp, accessControlExtLoginTable=accessControlExtLoginTable, accessControlUserRowStatus=accessControlUserRowStatus, accessControlExtLoginRecord=accessControlExtLoginRecord, accessControlUserSnmpPrivProt=accessControlUserSnmpPrivProt, accessControlMibVersion=accessControlMibVersion, accessControlUserSnmpAuthKey=accessControlUserSnmpAuthKey, accessControlGroupRowStatus=accessControlGroupRowStatus, accessControlLoginTrapEnable=accessControlLoginTrapEnable, accessControlClientTable=accessControlClientTable, accessControlClientName=accessControlClientName, accessControlLoginRecord=accessControlLoginRecord, accessControlClientPwd=accessControlClientPwd, accessControlGroupSsh=accessControlGroupSsh, accessControlClientRowStatus=accessControlClientRowStatus, PYSNMP_MODULE_ID=accessControl, accessControlLoginPwd=accessControlLoginPwd, accessControlUserRecord=accessControlUserRecord, accessControlGroupName=accessControlGroupName, accessControlGroupCli=accessControlGroupCli, accessControlUserGroupName=accessControlUserGroupName, accessControlClientStorageType=accessControlClientStorageType, accessControlGroupHttps=accessControlGroupHttps, accessControlGroupProfile=accessControlGroupProfile, accessControl=accessControl, accessControlLoginIpAddress=accessControlLoginIpAddress, accessControlLoginPolling=accessControlLoginPolling, accessControlLoginUserName=accessControlLoginUserName, accessControlUserSnmpAuthProt=accessControlUserSnmpAuthProt, accessControlLoginRequest=accessControlLoginRequest, accessControlUserTable=accessControlUserTable, accessControlLoginType=accessControlLoginType, accessControlUserSnmpPrivKey=accessControlUserSnmpPrivKey, accessControlGroupSftp=accessControlGroupSftp, accessControlUserName=accessControlUserName, accessControlGroupSnmp=accessControlGroupSnmp, accessControlExtLoginAuthMode=accessControlExtLoginAuthMode)
