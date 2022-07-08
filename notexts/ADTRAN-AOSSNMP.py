#
# PySNMP MIB module ADTRAN-AOSSNMP (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSSNMP
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:13 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Bits, Counter32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Unsigned32, ObjectIdentity, ModuleIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Bits", "Counter32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "iso", "Counter64")
TAddress, DisplayString, TextualConvention, RowStatus, TDomain = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "DisplayString", "TextualConvention", "RowStatus", "TDomain")
adGenAOSSnmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 2))
adGenAOSSnmpMib.setRevisions(('2008-10-20 00:00', '2008-10-09 00:00', '2004-09-24 00:00',))
if mibBuilder.loadTexts: adGenAOSSnmpMib.setLastUpdated('200409240000Z')
if mibBuilder.loadTexts: adGenAOSSnmpMib.setOrganization('ADTRAN, Inc.')
adGenAOSSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2))
adAOSSNMPCommunitiesTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1), )
if mibBuilder.loadTexts: adAOSSNMPCommunitiesTable.setStatus('current')
adAOSSNMPCommunitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesIndex"))
if mibBuilder.loadTexts: adAOSSNMPCommunitiesEntry.setStatus('current')
adAOSSNMPCommunitiesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)))
if mibBuilder.loadTexts: adAOSSNMPCommunitiesIndex.setStatus('current')
adAOSSNMPCommunitiesString = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesString.setStatus('current')
adAOSSNMPCommunitiesPrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("get", 1), ("set", 2))).clone('get')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesPrivilege.setStatus('current')
adAOSSNMPCommunitiesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesStatus.setStatus('current')
adAOSSNMPTrapsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2), )
if mibBuilder.loadTexts: adAOSSNMPTrapsTable.setStatus('current')
adAOSSNMPTrapsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1), ).setIndexNames((0, "ADTRAN-AOSSNMP", "adAOSSNMPTrapsIndex"))
if mibBuilder.loadTexts: adAOSSNMPTrapsEntry.setStatus('current')
adAOSSNMPTrapsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: adAOSSNMPTrapsIndex.setStatus('current')
adAOSSNMPTrapsString = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsString.setStatus('current')
adAOSSNMPTrapsMngmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsMngmtAddr.setStatus('current')
adAOSSNMPTrapsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsStatus.setStatus('current')
adAOSSNMPEnableTraps = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSSNMPEnableTraps.setStatus('current')
adAOSSNMPAuthenticationTraps = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSSNMPAuthenticationTraps.setStatus('current')
adGenAOSSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2))
adAOSSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1))
adAOSSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2))
adAOSSnmpConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1, 1)).setObjects(("ADTRAN-AOSSNMP", "adAOSSNMPConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSSnmpConfigCompliance = adAOSSnmpConfigCompliance.setStatus('current')
adAOSSNMPConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2, 1)).setObjects(("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesString"), ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesPrivilege"), ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesStatus"), ("ADTRAN-AOSSNMP", "adAOSSNMPEnableTraps"), ("ADTRAN-AOSSNMP", "adAOSSNMPAuthenticationTraps"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsString"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsMngmtAddr"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSSNMPConfigGroup = adAOSSNMPConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOSSNMP", adAOSSnmpGroups=adAOSSnmpGroups, adAOSSNMPTrapsTable=adAOSSNMPTrapsTable, adAOSSNMPTrapsString=adAOSSNMPTrapsString, adAOSSNMPCommunitiesIndex=adAOSSNMPCommunitiesIndex, adAOSSNMPCommunitiesStatus=adAOSSNMPCommunitiesStatus, adAOSSnmpCompliances=adAOSSnmpCompliances, PYSNMP_MODULE_ID=adGenAOSSnmpMib, adGenAOSSnmp=adGenAOSSnmp, adAOSSNMPCommunitiesPrivilege=adAOSSNMPCommunitiesPrivilege, adAOSSNMPAuthenticationTraps=adAOSSNMPAuthenticationTraps, adAOSSNMPCommunitiesTable=adAOSSNMPCommunitiesTable, adAOSSNMPCommunitiesString=adAOSSNMPCommunitiesString, adAOSSNMPTrapsEntry=adAOSSNMPTrapsEntry, adAOSSNMPConfigGroup=adAOSSNMPConfigGroup, adAOSSnmpConfigCompliance=adAOSSnmpConfigCompliance, adAOSSNMPCommunitiesEntry=adAOSSNMPCommunitiesEntry, adAOSSNMPEnableTraps=adAOSSNMPEnableTraps, adGenAOSSnmpMib=adGenAOSSnmpMib, adGenAOSSnmpConformance=adGenAOSSnmpConformance, adAOSSNMPTrapsMngmtAddr=adAOSSNMPTrapsMngmtAddr, adAOSSNMPTrapsIndex=adAOSSNMPTrapsIndex, adAOSSNMPTrapsStatus=adAOSSNMPTrapsStatus)
